#include <bits/stdc++.h>
// Exact self-contained checker for a finite matching complex.
using namespace std;using ull=uint64_t;using i64=long long;
int main(){auto started=chrono::steady_clock::now();vector<pair<int,int>> E;for(int v=0;v<8;v++)for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)E.push_back({3*v+i,3*v+j});for(int v=0;v<8;v++)for(int i=0;i<3;i++)if(!(v>>i&1))E.push_back({3*v+i,3*(v^(1<<i))+i});
 if(E.size()!=36){cerr<<"FAIL: graph edge count";return 1;}
 vector<int> degree(24);set<pair<int,int>> edgeset;for(auto [u,v]:E){if(u>v)swap(u,v);if(!edgeset.insert({u,v}).second){cerr<<"FAIL: duplicate graph edge";return 1;}degree[u]++;degree[v]++;}for(int d:degree)if(d!=3){cerr<<"FAIL: graph degree";return 1;}
 int triangles=0;for(int a=0;a<24;a++)for(int b=a+1;b<24;b++)for(int c=b+1;c<24;c++)if(edgeset.count({a,b})&&edgeset.count({a,c})&&edgeset.count({b,c}))triangles++;if(triangles!=8){cerr<<"FAIL: triangle count";return 1;}
 vector<ull> clash(E.size());for(int i=0;i<36;i++)for(int j=0;j<36;j++){auto[u,v]=E[i];auto[x,y]=E[j];if(u==x||u==y||v==x||v==y)clash[i]|=1ULL<<j;}
 vector<ull> faces;faces.reserve(1100000);function<void(int,ull,ull)> gen=[&](int i,ull mask,ull bad){if(mask)faces.push_back(mask);for(int j=i;j<36;j++)if(!(bad>>j&1))gen(j+1,mask|(1ULL<<j),bad|clash[j]);};gen(0,0,0);
 vector<int> level_count(13);for(auto m:faces)level_count[__builtin_popcountll(m)]++;vector<int> expected={0,36,558,4876,26421,92016,206676,292872,249420,117600,26928,2304,32};if(level_count!=expected){cerr<<"FAIL: face vector";return 1;}
 const int N=faces.size();cerr<<"faces="<<N<<"\n";unordered_map<ull,int> ix;ix.reserve(N*2);for(int i=0;i<N;i++)ix.emplace(faces[i],i);vector<int> mate(N,-1);int pair_ct=0;
 for(int j=0;j<36;j++){ull b=1ULL<<j;for(int i=0;i<N;i++)if(mate[i]==-1 && !(faces[i]&b)){auto it=ix.find(faces[i]|b);if(it!=ix.end() && mate[it->second]==-1){mate[i]=it->second;mate[it->second]=i;pair_ct++;}}}
 if(pair_ct!=509667){cerr<<"FAIL: pair count";return 1;}
 vector<int> crit_by_size(14), crit7,crit8;for(int i=0;i<N;i++)if(mate[i]<0){int s=__builtin_popcountll(faces[i]);crit_by_size[s]++;if(s==8)crit7.push_back(i);if(s==9)crit8.push_back(i);}cerr<<"pairs="<<pair_ct<<" critical:";for(int i=1;i<14;i++)if(crit_by_size[i])cerr<<" dim"<<i-1<<"="<<crit_by_size[i];cerr<<"\n";
 if(crit_by_size[1]!=1 || crit_by_size[8]!=368 || crit_by_size[9]!=36){cerr<<"FAIL: critical dimensions";return 1;}for(int d=1;d<14;d++)if(d!=1 && d!=8 && d!=9 && crit_by_size[d]){cerr<<"FAIL: extra critical cells";return 1;}
 vector<int> deg(N,0);long long incidences=0;
 for(int i=0;i<N;i++){ull m=faces[i];if(__builtin_popcountll(m)<2)continue;while(m){int k=__builtin_ctzll(m);m&=m-1;int j=ix.at(faces[i]^(1ULL<<k));if(mate[i]==j)deg[i]++;else deg[j]++;incidences++;}}
 vector<int> Q;Q.reserve(N);for(int i=0;i<N;i++)if(deg[i]==0)Q.push_back(i);for(size_t qi=0;qi<Q.size();qi++){int i=Q[qi];int mi=mate[i];if(mi>=0 && __builtin_popcountll(faces[mi])==__builtin_popcountll(faces[i])+1){if(--deg[mi]==0)Q.push_back(mi);}ull m=faces[i];if(__builtin_popcountll(m)>=2)while(m){int k=__builtin_ctzll(m);m&=m-1;int j=ix.at(faces[i]^(1ULL<<k));if(mi==j)continue;if(--deg[j]==0)Q.push_back(j);}}
 cerr<<"incidences="<<incidences<<" topo_nodes="<<Q.size()<<" acyclic="<<(Q.size()==N)<<"\n";if(Q.size()!=(size_t)N || incidences!=7220436)return 2;
 unordered_map<int,int> cri7index;for(int i=0;i<(int)crit7.size();i++)cri7index[crit7[i]]=i;
 // Morse boundary via 8/7-dimensional gradient paths (recursive reduction)
 vector<map<int,i64>> cache(N);vector<char> state(N,0);int visits=0,maxsp=0;
 function<map<int,i64>&(int,int)> red=[&](int lo,int depth)->map<int,i64>&{maxsp=max(maxsp,depth);if(state[lo]==2)return cache[lo];if(state[lo]==1){cerr<<"CYCLE-in-k-reduction\n";exit(3);}state[lo]=1;visits++;auto ci=cri7index.find(lo);if(ci!=cri7index.end()){cache[lo][ci->second]=1;}else{int up=mate[lo];if(up>=0 && __builtin_popcountll(faces[up])==9){int rm=__builtin_ctzll(faces[up]^faces[lo]); // ordinal of removed bit among ordered vertices
 auto sign=[&](ull upper,int bit){return (__builtin_popcountll(upper & ((1ULL<<bit)-1))%2==0)?1:-1;};int pivot=sign(faces[up],rm);ull m=faces[up];while(m){int b=__builtin_ctzll(m);m&=m-1;if(b==rm)continue;int l2=ix.at(faces[up]^(1ULL<<b));auto &t=red(l2,depth+1);int coef=-pivot*sign(faces[up],b);for(auto[k,z]:t){auto &ref=cache[lo][k];ref+=coef*z;if(ref==0)cache[lo].erase(k);}}}}
 state[lo]=2;return cache[lo];};
 vector<vector<i64>> M(crit7.size(),vector<i64>(crit8.size(),0));for(int c=0;c<(int)crit8.size();c++){ull m=faces[crit8[c]];while(m){int b=__builtin_ctzll(m);m&=m-1;int lo=ix.at(faces[crit8[c]]^(1ULL<<b));int sign=(__builtin_popcountll(faces[crit8[c]]&((1ULL<<b)-1))%2==0)?1:-1;auto &r=red(lo,1);for(auto[k,z]:r)M[k][c]+=sign*z;}}cerr<<"boundary solved visited="<<visits<<" maxdepth="<<maxsp<<"\n";
 int maxabs=0,nonzero=0;for(auto &v:M)for(auto z:v){maxabs=max(maxabs,(int)abs(z));nonzero+=z!=0;}cerr<<"boundary matrix size="<<M.size()<<"x"<<crit8.size()<<" nonzero="<<nonzero<<" maxabs="<<maxabs<<"\n";
 // Independently compute all 36 columns by forwarding signed coefficients in the full acyclic Hasse order.
 // This does not use the memoized recursion, and must agree entrywise.
 vector<int> lower_order;
 for(int id:Q)if(__builtin_popcountll(faces[id])==8)lower_order.push_back(id);
 auto sign2=[](ull m,int bit){return (__builtin_popcountll(m&((1ULL<<bit)-1))%2==0)?1:-1;};
 for(int c=0;c<(int)crit8.size();c++){
   vector<i64> weights(N,0);ull bmask=faces[crit8[c]];
   while(bmask){int b=__builtin_ctzll(bmask);bmask&=bmask-1;weights[ix.at(faces[crit8[c]]^(1ULL<<b))]+=sign2(faces[crit8[c]],b);}
   for(int lo:lower_order){i64 z=weights[lo];if(!z)continue;int up=mate[lo];
     if(up<0){int r=cri7index.at(lo);if(z!=M[r][c]){cerr<<"FAIL: independent differential check at row="<<r<<" col="<<c<<" expected="<<M[r][c]<<" got="<<z<<"\n";return 4;}}
     else if(__builtin_popcountll(faces[up])==9){int b=__builtin_ctzll(faces[up]^faces[lo]);int p=sign2(faces[up],b);ull m=faces[up];while(m){int t=__builtin_ctzll(m);m&=m-1;if(t==b)continue;int other=ix.at(faces[up]^(1ULL<<t));__int128 w=(__int128)weights[other]-(__int128)p*sign2(faces[up],t)*z;if(w>LLONG_MAX||w<LLONG_MIN){cerr<<"FAIL: coefficient overflow\n";return 4;}weights[other]=(i64)w;}}
   }
 }
 if(nonzero!=698||maxabs!=1){cerr<<"FAIL: expected sparse differential\n";return 4;}
 cerr<<"independent gradient-path computation agrees on all 368x36 entries\n";
 // Find unimodular full rank via elementary row and column operations on integer matrix; pivot +-1.
 int rank=0;int rows=M.size(),cols=crit8.size();int maxel=0;
 for(int p=0;p<min(rows,cols);p++){int ii=-1,jj=-1;for(int i=p;i<rows && ii<0;i++)for(int j=p;j<cols;j++)if(abs(M[i][j])==1){ii=i;jj=j;break;}if(ii<0){cerr<<"No unit pivot at "<<p<<"\n";break;}swap(M[p],M[ii]);for(int i=0;i<rows;i++)swap(M[i][p],M[i][jj]);i64 pv=M[p][p];for(int i=p+1;i<rows;i++){i64 val=M[i][p];if(val==0)continue;for(int j=p;j<cols;j++){__int128 t=(__int128)M[i][j]-(__int128)val*pv*M[p][j];if(t>LLONG_MAX||t<LLONG_MIN){cerr<<"overflow\n";exit(7);}M[i][j]=(i64)t;maxel=max(maxel,(int)abs(M[i][j]));}}rank++;}
 cerr<<"unit_rank="<<rank<<" max_after_elim="<<maxel<<" elapsed="<<chrono::duration<double>(chrono::steady_clock::now()-started).count()<<"\n";
 if(rank!=36){cerr<<"FAIL: Smith rank";return 5;}cout<<"VERIFY_OK\n";
}
