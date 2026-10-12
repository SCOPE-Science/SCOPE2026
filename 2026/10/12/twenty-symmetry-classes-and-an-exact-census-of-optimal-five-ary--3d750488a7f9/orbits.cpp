#include <bits/stdc++.h>
using namespace std;
constexpr int N=80640;
vector<string> C(N); unordered_map<string,int> idx;
int maps[4][52],par[N],sz[N];
int root(int i){return par[i]==i?i:par[i]=root(par[i]);}
void join(int i,int j){i=root(i);j=root(j);if(i==j)return;if(sz[i]<sz[j])swap(i,j);par[j]=i;sz[i]+=sz[j];}
string transform(const string&s,int g){
 unsigned char tmp[52];
 for(int l=0;l<13;l++)for(int j=0;j<4;j++)tmp[maps[g][4*l+j]]=((unsigned char)s[l]>>(2*j))&3;
 int remap[4];for(int j=0;j<4;j++)remap[tmp[j]]=j;
 string out(13,'\0');for(int l=0;l<13;l++)for(int j=0;j<4;j++)out[l] = (unsigned char)out[l] | (remap[tmp[4*l+j]]<<(2*j));
 return out;
}
int main(){ifstream f("colorings.bin",ios::binary);
 for(int i=0;i<N;i++){C[i].resize(13);f.read(C[i].data(),13);if(!f)throw runtime_error("truncated");idx[C[i]]=i;par[i]=i;sz[i]=1;}assert(idx.size()==N);
 ifstream m("gmap.txt");for(int g=0;g<4;g++)for(int k=0;k<52;k++)m>>maps[g][k];
 for(int g=0;g<4;g++){
  for(int i=0;i<N;i++){auto s=transform(C[i],g);auto it=idx.find(s);if(it==idx.end()){cerr<<"FAIL_CLOSED "<<g<<" "<<i<<"\n";return 1;}join(i,it->second);}
 }
 map<int,int> counts;vector<pair<int,int>> reps;
 for(int i=0;i<N;i++)if(par[i]==i){counts[sz[i]]++;reps.push_back({sz[i],i});}
 sort(reps.begin(),reps.end(),greater<>());
 cout<<"normalized="<<N<<" group_order=5616 orbit_count="<<reps.size()<<"\n";
 for(auto [s,n]:counts)cout<<"orbit_size="<<s<<" num_orbits="<<n<<" code_count_normalized="<<(long long)s*n<<" stabilizer="<<5616/s<<"\n";
 ofstream o("orbit_representatives.txt");
 for(int z=0;z<(int)reps.size();z++){
  auto [s,i]=reps[z];o<<"class "<<z+1<<" norm_orbit_size "<<s<<" stabilizer "<<5616/s<<" colors_hex ";
  for(unsigned char c:C[i])o<<hex<<setw(2)<<setfill('0')<<(int)c;
  o<<dec<<"\n";
 }
}
