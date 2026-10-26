#include <bits/stdc++.h>
using namespace std;
static const int N=10, ST=3628800;
int fact[11];
inline int rankp(uint64_t p){
 int r=0, seen=0;
 for(int i=0;i<N;++i){
  int a=(p>>(4*i))&15;
  int k=__builtin_popcount((unsigned)(seen&((1<<a)-1)));
  r+=(a-k)*fact[9-i];seen|=1<<a;
 }
 return r;
}
inline uint64_t unrank(int r){
 int used=0;uint64_t p=0;
 for(int i=0;i<N;++i){
  int d=r/fact[9-i];r%=fact[9-i];
  int a=0;for(;a<N;a++){if(used>>a&1)continue;if(d--==0)break;}
  used|=1<<a;p|=(uint64_t)a<<(i*4);
 }
 return p;
}
inline int cmp_dist(int a, int b) {return a==b;}
int main(int argc,char**argv){
 fact[0]=1;for(int i=1;i<=10;i++)fact[i]=i*fact[i-1];
 vector<pair<int,int>> edges;
 for(int i=0;i<5;i++) { edges.push_back({i,(i+1)%5});edges.push_back({i,i+5});edges.push_back({i+5,5+(i+2)%5}); }
 sort(edges.begin(),edges.end());
 vector<unsigned char> dist(ST,255);vector<int> Q(ST);
 dist[0]=0;Q[0]=0;int head=0,tail=1;
 vector<long long> shell(1,1);int maxd=0;
 while(head<tail){
   int s=Q[head++];int depth=dist[s];uint64_t p=unrank(s);
   for(auto [u,v]:edges){
     uint64_t t=p;unsigned long long a=(t>>(4*u))&15,b=(t>>(4*v))&15;
     t^=(a^b)<<(4*u);t^=(a^b)<<(4*v);
     int k=rankp(t);
     if(dist[k]!=255)continue;
     dist[k]=depth+1;Q[tail++]=k;
     if(depth+1>maxd) {maxd=depth+1;shell.push_back(0);}
     shell[depth+1]++;
   }
 }
 long long sum=0;for(auto x:shell)sum+=x;
 cerr<<"visited "<<tail<<" states, max="<<maxd<<" shells="<<shell.size()<<"\n";
 cout<<"STATES "<<tail<<" EDGES "<<edges.size()<<" DIAMETER "<<maxd<<"\n";
 cout<<"SHELL ";for(size_t i=0;i<shell.size();i++)cout<<(i?",":"")<<shell[i];cout<<"\n";
 map<string,int> typ;int anti=0;
 for(int i=0;i<ST;i++) if(dist[i]==maxd){
  uint64_t p=unrank(i);bool vis[10]={};vector<int> c;
  for(int j=0;j<10;j++)if(!vis[j]) {int k=j,sz=0;do{vis[k]=true;sz++;k=(p>>(4*k))&15;}while(k!=j);c.push_back(sz);}
  sort(c.rbegin(),c.rend());string st;for(int k:c)st+=to_string(k)+",";typ[st]++;
 }
 
 int Gdist[10][10];for(int i=0;i<10;i++)for(int j=0;j<10;j++)Gdist[i][j]=i==j?0:3;
 for(auto [i,j]:edges)Gdist[i][j]=Gdist[j][i]=1;
 for(int k=0;k<10;k++)for(int i=0;i<10;i++)for(int j=0;j<10;j++)Gdist[i][j]=min(Gdist[i][j],Gdist[i][k]+Gdist[k][j]);
 int mxgap=-100,witness=-1,shortbound=-1;map<int,long long> gaps;
 for(int x=0;x<ST;x++){
  uint64_t p=unrank(x);int sumdist=0;
  for(int i=0;i<10;i++)sumdist+=Gdist[i][(p>>(4*i))&15];
  int bound=(sumdist+1)/2;
  if((int)dist[x]-bound>mxgap){mxgap=(int)dist[x]-bound;} gaps[(int)dist[x]-bound]++;
  if(dist[x]==maxd && witness<0){witness=x;shortbound=bound;}
 }
 cout<<"WITNESS_RANK "<<witness<<" WITNESS_ONE_LINE ";uint64_t witnessp=unrank(witness);for(int i=0;i<10;i++)cout<<(i?",":"")<<((witnessp>>(4*i))&15);cout<<" TRANSPORT_LOWER_BOUND "<<shortbound<<"\n";
 cout<<"MAX_DISTANCE_MINUS_TRANSPORT_BOUND "<<mxgap<<"\n";cout<<"GAP_SPECTRUM ";for(auto [g,v]:gaps)cout<<g<<":"<<v<<",";cout<<"\n";
 cout<<"ANTIPODES "<<shell.back()<<"\n";
for(auto [k,v]:typ)cout<<"TYPE "<<k<<" "<<v<<"\n";
 // Check transpositions neighboring identity and rank round trip samples.
 for(int s=0;s<ST;s++)if(rankp(unrank(s))!=s) {cout<<"FAIL_RANK "<<s<<"\n";return 1;}
 cout<<"CHECKSUM "<<sum<<"\n";
 const vector<long long> expected{1,15,135,955,5504,26096,99739,297535,655169,984833,923838,493350,130014,11616};
 const map<int,long long> expectedGaps{{0,431532},{1,1509516},{2,1382012},{3,299060},{4,6680}};
 const map<string,int> expectedTypes{{"10,",5832},{"2,2,2,2,2,",24},{"4,3,3,",960},{"4,4,2,",960},{"5,3,2,",2280},{"6,2,2,",1320},{"6,3,1,",240}};
 if(shell!=expected||gaps!=expectedGaps||typ!=expectedTypes||tail!=ST||sum!=ST||maxd!=13||mxgap!=4||shortbound!=9||witness!=114135) return 2;
 cout<<"VERIFY_OK\n";
}
