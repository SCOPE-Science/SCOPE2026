#include <bits/stdc++.h>
using namespace std;
int N; vector<uint8_t> seen,lyndon; vector<uint32_t> words; vector<unsigned long long> freq; vector<int> opt, value; vector<unsigned long long> optcount; vector<vector<int>> optw;
void dfs(int depth,unsigned mask,int count){
 if(depth){freq[depth]++;if(count>opt[depth]){opt[depth]=count;optcount[depth]=0;optw[depth].clear();}if(count==opt[depth]){optcount[depth]++;if(optw[depth].size()<20)optw[depth].push_back(mask);}}
 if(depth==N)return;
 for(int c=0;c<2;c++){
  int sz=words.size(),gain=0;
  for(int i=0;i<sz;i++){
   uint32_t v=(words[i]<<1)|c;
   if(!seen[v]){seen[v]=1;words.push_back(v);gain+=lyndon[v];}
  }
  dfs(depth+1,(mask<<1)|c,count+gain);
  for(int i=sz;i<(int)words.size();i++)seen[words[i]]=0;
  words.resize(sz);
 }
}
int main(int argc,char**argv){N=argc>1?atoi(argv[1]):16;if(N<1||N>21)return 1;
 const int lim=1<<(N+1);seen.assign(lim,0);lyndon.assign(lim,0);
 for(int k=1;k<=N;k++){
  const unsigned b=1u<<k;
  for(unsigned w=0;w<b;w++){
   bool yes=true;
   for(int s=1;s<k;s++){
    unsigned v=((w<<s)&(b-1))|(w>>(k-s));
    if(w>=v){yes=false;break;}
   }
   lyndon[b+w]=yes;
  }
 }
 vector<int> nL(N+1,0);for(int k=1;k<=N;k++){for(int i=(1<<k);i<(1<<(k+1));i++)nL[k]+=lyndon[i];}
 cerr<<"Lyndon length counts:";for(int k=1;k<=N;k++)cerr<<' '<<nL[k];cerr<<'\n';
 freq.assign(N+1,0);opt.assign(N+1,-1);optcount.assign(N+1,0);optw.resize(N+1);
 seen[1]=1;words.push_back(1);dfs(0,0,0);
 const int expected_max[]={0,1,3,4,6,8,13,18,28,41,63,96,141,225,335,538,803,1292,1941,3132,4701};
 const int expected_ties[]={0,2,1,2,1,4,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1};
 for(int k=1;k<=N;k++){
  if(opt[k]!=expected_max[k]||optcount[k]!=(unsigned long long)expected_ties[k]||freq[k]!=(1ULL<<k)){
   cerr<<"CENSUS_MISMATCH n="<<k<<"\n";return 2;
  }
  cout<<"n="<<k<<" max="<<opt[k]<<" optimizers="<<optcount[k]<<" first=";
  for(int v:optw[k]){for(int j=k-1;j>=0;j--)cout<<((v>>j)&1);cout<<',';}
  cout<<" total_words="<<freq[k]<<"\n";
 }
 cout<<"CENSUS_OK n=1.."<<N<<"\n";
}
