#include <bits/stdc++.h>
using namespace std;
struct G {int d,N;vector<vector<int>> t;vector<int> fvec;
  G(int n,int negative){d=2*n;N=2*(1<<d);t.assign(N,vector<int>(N));
  for(int x=0;x<N;x++)for(int y=0;y<N;y++){
   int v=x>>1,w=y>>1,z=(x&1)^(y&1),f=0;
   for(int b=0;b<n;b++){
    int a=(v>>(2*b))&1, c=(v>>(2*b+1))&1;
    int p=(w>>(2*b))&1,r=(w>>(2*b+1))&1;
    f ^= (a&r);
    if(negative && b==0)f ^= (a&p)^(c&r);
   }
   t[x][y]=((v^w)<<1)|(z^f);
  }
 }
};
uint64_t atom_sig(const vector<vector<int>>&M,int x,int y,int z){
  int a[3]={x,y,z};uint64_t bits=0;int i=0;
  for(int j=0;j<3;j++){if(a[j]==0)bits |= (1ULL<<i);i++;}
  for(int j=0;j<3;j++)for(int k=j+1;k<3;k++){if(a[j]==a[k])bits|=(1ULL<<i);i++;}
  for(int j=0;j<3;j++)for(int k=0;k<3;k++)for(int l=0;l<3;l++){
   if(M[a[j]][a[k]]==a[l])bits|=(1ULL<<i);
   i++;
  }
  return bits;
}
string encodeSet(vector<int>&x){sort(x.begin(),x.end());x.erase(unique(x.begin(),x.end()),x.end());string s;for(int a:x)s+=to_string(a)+',';return s;}
map<vector<uint64_t>,int> global_a; map<vector<int>,int> global_b;
void inspect(int n,int neg){
 G Gg(n,neg);int N=Gg.N;
 auto &a_id=global_a;vector<int> first(N), profilefreq;
 auto &b_id=global_b;vector<int> pointed(N);
 for(int x=0;x<N;x++){
  vector<int> ytypes;
  for(int y=0;y<N;y++){
   vector<uint64_t> atoms;atoms.reserve(N);
   for(int z=0;z<N;z++)atoms.push_back(atom_sig(Gg.t,x,y,z));
   sort(atoms.begin(),atoms.end());atoms.erase(unique(atoms.begin(),atoms.end()),atoms.end());
   auto [it,ins]=a_id.emplace(atoms,a_id.size());ytypes.push_back(it->second);
  }
  sort(ytypes.begin(),ytypes.end());ytypes.erase(unique(ytypes.begin(),ytypes.end()),ytypes.end());
  auto[it,ins]=b_id.emplace(ytypes,b_id.size());pointed[x]=it->second;
  if(n==2 && (x==0 || x==1 || x==2 || x==3 || x==4 || x==5 || x==6 || x==7)){cerr<<"  x="<<x<<" xtype="<<it->second<<" q="<<(Gg.t[x][x]==0?0:1)<<" yprofiles=";for(int v:ytypes)cerr<<v<<",";cerr<<"\n";}
 }
 vector<int> top=pointed;sort(top.begin(),top.end());top.erase(unique(top.begin(),top.end()),top.end());
 cerr<<"signature=";for(int c:top)cerr<<c<<",";cerr<<" n="<<n<<" sign="<<(neg?"minus":"plus")<<" group_order="<<N<<" atomic_pair_ext="<<a_id.size()<<" pointed="<<top.size()<<"\n";
 cout<<n<<" "<<neg<<" ";
 for(int x=0;x<N;x++)cout<<pointed[x]<<",";
 cout<<"\n";
}
int main(){for(int n=1;n<=3;n++)for(int sign=0;sign<2;sign++)inspect(n,sign);}
