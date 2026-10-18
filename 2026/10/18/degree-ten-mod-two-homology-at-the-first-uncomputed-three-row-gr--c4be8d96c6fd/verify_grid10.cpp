// Reproducible finite simplicial chain computation over GF(2).
// The graph is the 3-by-10 rectangular grid; vertices of the matching complex are grid edges.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
int N,E,D;vector<pair<int,int>> edges;vector<U> base,face,crit9,crit10;
// lower (D-1) cells matched to upper D cells: size D -> size D+1
unordered_map<U,U> partner;
void gen(int i,U occ,U mask){if(i==E){base.push_back(mask);return;}gen(i+1,occ,mask);auto[u,v]=edges[i];U q=(1ull<<u)|(1ull<<v);if(!(q&occ))gen(i+1,occ|q,mask|(1ull<<i));}
using Vec=array<U,8>;unordered_map<U,Vec> memo;unordered_set<U> active;
size_t calls=0;bool cycle=false;
Vec project_cell(U f){
 auto it=memo.find(f);if(it!=memo.end())return it->second;
 if(!active.insert(f).second){fprintf(stderr,"Morse gradient cycle at %llu\n",(unsigned long long)f);cycle=true;throw 3;}
 Vec r{};
 auto p=partner.find(f);
 if(p!=partner.end()){
  U u=p->second;
  for(int i=0;i<E;i++)if((u>>i)&1){U g=u^(1ull<<i);if(g==f)continue;Vec z=project_cell(g);for(int j=0;j<8;j++)r[j]^=z[j];}
 } else {
   auto c=lower_bound(crit9.begin(),crit9.end(),f);
   if(c!=crit9.end() && *c==f){int j=c-crit9.begin();r[j/64]^=1ull<<(j%64);}
 }
 active.erase(f);memo[f]=r;calls++;
 if(calls%1000000==0)fprintf(stderr,"memo=%zu size=%zu\n",calls,memo.size());
 return r;
}
int main(int argc,char**argv){if(argc<2){fprintf(stderr,"Usage: checker ascending|descending [matrix_output.txt]\n");return 2;}
string mode=argv[1];if(mode!="ascending" && mode!="descending")return 2;
N=10;D=N;for(int r=0;r<3;r++)for(int c=0;c<N;c++){if(r+1<3)edges.push_back({r*N+c,(r+1)*N+c});if(c+1<N)edges.push_back({r*N+c,r*N+c+1});}E=edges.size();auto t=chrono::steady_clock::now();gen(0,0,0);sort(base.begin(),base.end());fprintf(stderr,"Build %zu faces %.2fs\n",base.size(),chrono::duration<double>(chrono::steady_clock::now()-t).count());face.swap(base);
 vector<int> order(E);iota(order.begin(),order.end(),0);if(mode=="descending")reverse(order.begin(),order.end());
 for(int i:order){
  U bit=1ull<<i; vector<U>a,b;a.reserve(face.size());b.reserve(face.size()/3);
  for(U x:face){if(x&bit)b.push_back(x^bit);else a.push_back(x);}face.clear();size_t j=0,k=0;
  while(j<a.size()||k<b.size()){
   if(k==b.size()||(j<a.size()&&a[j]<b[k]))face.push_back(a[j++]);
   else if(j==a.size()||b[k]<a[j])face.push_back(b[k++]|bit);
   else{
    U x=a[j]; if(__builtin_popcountll(x)==D)partner.emplace(x,x|bit);
    j++;k++;
   }
  }
  sort(face.begin(),face.end());
 }
 for(U x:face){int k=__builtin_popcountll(x);if(k==D)crit9.push_back(x);else if(k==D+1)crit10.push_back(x);else fprintf(stderr,"unexpected dim=%d\n",k-1);}
 fprintf(stderr,"critical %zu lower %zu upper, partner %zu, elapsed %.2fs\n",crit9.size(),crit10.size(),partner.size(),chrono::duration<double>(chrono::steady_clock::now()-t).count());
 if(crit9.size()>512)return 1;
 vector<Vec> matrix;
 for(int i=0;i<(int)crit10.size();i++){
  U x=crit10[i];Vec row{};
  for(int j=0;j<E;j++)if((x>>j)&1){Vec z=project_cell(x^(1ull<<j));for(int k=0;k<8;k++)row[k]^=z[k];}
  matrix.push_back(row);
  if(i%10==0)fprintf(stderr,"critical column %d/%zu memo=%zu elapsed=%.2fs\n",i,crit10.size(),memo.size(),chrono::duration<double>(chrono::steady_clock::now()-t).count());
 }
 // compute rank of rows mod2
 vector<Vec> pivot(512); vector<bool>used(512);int rk=0;
 for(auto row:matrix){for(int j=(int)crit9.size()-1;j>=0;j--){if(!(row[j/64]>>j%64&1))continue;if(!used[j]){pivot[j]=row;used[j]=true;rk++;break;}for(int k=0;k<8;k++)row[k]^=pivot[j][k];}}
 printf("N=%d rankmod2=%d criticalLower=%zu criticalUpper=%zu projected %zu\n",N,rk,crit9.size(),crit10.size(),memo.size());
 const string output=(argc>2)?argv[2]:"morse_matrix.txt";
 FILE* fp=fopen(output.c_str(),"w");if(!fp)return 3;
 for(int i=0;i<(int)crit10.size();i++){fprintf(fp,"%llu ",(unsigned long long)crit10[i]);for(int j=0;j<(int)crit9.size();j++)fprintf(fp,"%d",(int)(matrix[i][j/64]>>(j%64)&1));fprintf(fp,"\n");}
 fclose(fp);
}
