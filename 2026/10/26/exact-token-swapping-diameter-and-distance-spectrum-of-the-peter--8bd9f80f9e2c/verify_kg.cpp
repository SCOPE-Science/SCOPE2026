// Independent token/vertex encoding and Petersen construction.
#include <bits/stdc++.h>
using namespace std;
constexpr int N=10, SZ=3628800;
int factorial[11];
int R(const array<uint8_t,N>& a){int k=0;int seen=0;for(int i=0;i<N;i++){int x=a[i];int smaller=__builtin_popcount((unsigned)(seen&((1u<<x)-1)));k+=(x-smaller)*factorial[9-i];seen|=(1u<<x);}return k;}
array<uint8_t,N> U(int k){array<uint8_t,N> a;int used=0;for(int i=0;i<N;i++){int t=k/factorial[9-i]; k%=factorial[9-i];for(int v=0;v<N;v++)if(!(used>>v&1)){if(t--==0){a[i]=v;used|=1<<v;break;}}}return a;}
int main(){factorial[0]=1;for(int i=1;i<=N;i++)factorial[i]=i*factorial[i-1];
  vector<pair<int,int>> labels;for(int x=0;x<5;x++)for(int y=x+1;y<5;y++)labels.emplace_back(x,y);
  vector<pair<int,int>> ed;for(int i=0;i<N;i++)for(int j=i+1;j<N;j++) if(labels[i].first!=labels[j].first&&labels[i].first!=labels[j].second&&labels[i].second!=labels[j].first&&labels[i].second!=labels[j].second)ed.emplace_back(i,j);
  vector<uint8_t> D(SZ,255); vector<int> Q(SZ);Q[0]=0;D[0]=0;int in=1,out=0;vector<int> shell(1,1);
  while(out<in){int k=Q[out++];auto a=U(k);for(auto [v,w]:ed){auto b=a;for(int i=0;i<N;i++){if(b[i]==v)b[i]=w;else if(b[i]==w)b[i]=v;}int kk=R(b);if(D[kk]!=255)continue;D[kk]=D[k]+1;Q[in++]=kk;if(D[kk]>=shell.size())shell.push_back(0);shell[D[kk]]++;}}
  cout<<"EDGES "<<ed.size()<<" STATES "<<in<<" SHELL ";for(int i=0;i<shell.size();i++)cout<<(i?",":"")<<shell[i];cout<<"\n";
  
  int d[10][10];for(int i=0;i<N;i++)for(int j=0;j<N;j++)d[i][j]=(i==j?0:3);
  for(auto [x,y]:ed)d[x][y]=d[y][x]=1;
  for(int k=0;k<N;k++)for(int i=0;i<N;i++)for(int j=0;j<N;j++)d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
  map<int,long long> gaps;map<string,int> types;int maxgap=-1;
  for(int k=0;k<SZ;k++){
    auto inv=U(k);int total=0;for(int token=0;token<N;token++)total+=d[inv[token]][token];
    int gap=int(D[k])-(total+1)/2;gaps[gap]++;maxgap=max(maxgap,gap);
    if(D[k]==13){bool seen[N]={};vector<int> ct;for(int i=0;i<N;i++)if(!seen[i]){int cur=i,c=0;do{seen[cur]=true;cur=inv[cur];c++;}while(cur!=i);ct.push_back(c);}sort(ct.rbegin(),ct.rend());string st;for(int t:ct)st+=to_string(t)+",";types[st]++;}
  }
  cout<<"GAPS ";for(auto [k,v]:gaps)cout<<k<<":"<<v<<",";cout<<"\n";
  cout<<"TYPES ";for(auto [k,v]:types)cout<<k<<":"<<v<<",";cout<<"\n";
  const vector<int> expected{1,15,135,955,5504,26096,99739,297535,655169,984833,923838,493350,130014,11616};
  const map<int,long long> expectedGaps{{0,431532},{1,1509516},{2,1382012},{3,299060},{4,6680}};
  const map<string,int> expectedTypes{{"10,",5832},{"2,2,2,2,2,",24},{"4,3,3,",960},{"4,4,2,",960},{"5,3,2,",2280},{"6,2,2,",1320},{"6,3,1,",240}};
  if(in!=SZ||ed.size()!=15||shell!=expected||maxgap!=4||gaps!=expectedGaps||types!=expectedTypes)return 1;
  cout<<"VERIFY_OK\n";
}
