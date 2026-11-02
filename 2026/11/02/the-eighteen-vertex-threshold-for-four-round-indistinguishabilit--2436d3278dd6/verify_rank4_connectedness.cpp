#include <bits/stdc++.h>
using namespace std;
map<vector<int>,int> pool[5]; int nextid[5]={1,1,1,1,1};
int intern(int level, vector<int>&v){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());auto it=pool[level].find(v);if(it!=pool[level].end())return it->second;int z=nextid[level]++;pool[level][v]=z;return z;}
int atomcode(int a,int b,int c,int d,const vector<vector<uint8_t>>& adj){int arr[4]={a,b,c,d},bits=0;int k=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){int w=(arr[i]==arr[j]?2:(adj[arr[i]][arr[j]]?1:0));bits|=w<<(2*k++);}return bits;}
int type4(const vector<int>&cs){int n=accumulate(cs.begin(),cs.end(),0); vector<vector<uint8_t>> adj(n,vector<uint8_t>(n));int v=0;for(int c:cs){for(int j=0;j<c;j++){int a=v+j,b=v+(j+1)%c;adj[a][b]=adj[b][a]=1;}v+=c;}
vector<int> t1(n*n*n); vector<int> tmp;tmp.reserve(n);for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++){tmp.clear();for(int d=0;d<n;d++)tmp.push_back(atomcode(a,b,c,d,adj));t1[(a*n+b)*n+c]=intern(1,tmp);} 
vector<int> t2(n*n);for(int a=0;a<n;a++)for(int b=0;b<n;b++){tmp.clear();for(int c=0;c<n;c++)tmp.push_back(t1[(a*n+b)*n+c]);t2[a*n+b]=intern(2,tmp);}
vector<int> t3(n);for(int a=0;a<n;a++){tmp.clear();for(int b=0;b<n;b++)tmp.push_back(t2[a*n+b]);t3[a]=intern(3,tmp);}tmp.clear();for(int a=0;a<n;a++)tmp.push_back(t3[a]);return intern(4,tmp);}
void parts(int remain,int min, vector<int>&cur, vector<vector<int>>&out){if(!remain){out.push_back(cur);return;}for(int a=min;a<=remain;a++){if(a<3)continue;cur.push_back(a);parts(remain-a,a,cur,out);cur.pop_back();}}
int main(){
  vector<int> T(12);for(int n=3;n<=11;n++)T[n]=type4({n});
  for(int a=3;a<=11;a++)for(int b=a+1;b<=11;b++)if(T[a]==T[b]){cerr<<"ERR_CONNECTED_COLLISION "<<a<<" "<<b<<"\n";return 1;}
  int count=0;vector<int> cur;for(int n=6;n<18;n++){
    vector<vector<int>> plist;parts(n,3,cur,plist);
    for(auto &p:plist)if(p.size()>=2){int id=type4(p);count++;
      for(int m=3;m<=11;m++)if(id==T[m]){cerr<<"ERR_TOO_EARLY n="<<n<<" cycle="<<m<<"\n";return 2;}
    }
  }
  if(count!=105){cerr<<"ERR_ENUM_COUNT "<<count<<"\n";return 3;}
  int pairs=0;for(int a=9;a<=11;a++)for(int b=a;b<=11;b++){
    int id=type4({a,b});if(id!=T[11]){cerr<<"ERR_BASE_PAIR "<<a<<" "<<b<<"\n";return 4;}pairs++;
  }
  cout<<"ALL_CONNECTED_TYPES_C3_C11_DISTINCT\n";
  cout<<"DISCONNECTED_BELOW_18_COUNT="<<count<<"\n";
  cout<<"SIX_TWO_CYCLE_BASE_IDENTITIES="<<pairs<<"\n";
  cout<<"EXACT_RANK4_CHECKS_OK\n";
  return 0;
}