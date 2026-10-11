#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using W=std::vector<int>;
static W norm(W p){auto it=std::find(p.begin(),p.end(),0); std::rotate(p.begin(),it,p.end()); return p;}
static bool Tminus(const W&p){int n=p.size();for(int i=0;i<n;i++) if(std::abs(p[i]-p[(i+1)%n])==1) return true; return false;}
static bool Xmove(const W&p){int N=p.size(),n=(N-1)/2; for(int b=0;b<N;b++){std::vector<std::array<int,2>> P; for(int j=0;j<n;j++){int x=p[(b+1+2*j)%N],y=p[(b+2+2*j)%N]; if(x>y)std::swap(x,y);P.push_back({x,y});}
 for(int m=0;m<=N-4;m++)for(int w=m+2;w<=N-2;w++){int A=-1,B=-1;std::array<int,2>a={m,w+1},d={m+1,w}; if(a[0]>a[1])std::swap(a[0],a[1]); if(d[0]>d[1])std::swap(d[0],d[1]); for(int j=0;j<n;j++){if(P[j]==a)A=j;if(P[j]==d)B=j;} if(A<0||B<0||A==B)continue; bool ok=true; for(int j=0;j<n;j++)if(j!=A&&j!=B){bool x=P[j][0]>=m+2&&P[j][0]<=w-1;bool y=P[j][1]>=m+2&&P[j][1]<=w-1;if(x!=y){ok=false;break;}} if(ok)return true; }} return false;}
static W R(W p){for(int&x:p)x=(x+1)%p.size();return norm(p);} static W S(W p){int N=p.size();std::reverse(p.begin(),p.end());for(int&x:p)x=N-1-x;return norm(p);} 
static uint64_t key(const W&p){uint64_t z=0;for(size_t i=0;i<p.size();i++)z|=(uint64_t)p[i]<<(4*i);return z;}
static std::set<uint64_t> orbit(W p){int N=p.size();std::set<uint64_t>o;for(int k=0;k<N;k++){o.insert(key(p));o.insert(key(S(p)));p=R(p);}return o;}
int main(){
 // source Example 3.1: X applies to (4,2,0,6,5,1,3)
 if(!Xmove(W{4,2,0,6,5,1,3})) return 3;
 // source hard reps have no T- and no X.
 for(W p: {W{0,2,4,1,5,7,3,8,6},W{0,2,5,3,8,1,7,4,6},W{0,2,4,7,3,8,6,1,5}}) if(Tminus(p)||Xmove(p)) return 4;
 W tail;for(int i=1;i<11;i++)tail.push_back(i); uint64_t total=0,noT=0,noX=0,local=0; std::unordered_set<uint64_t> lr;lr.reserve(400000);
 do{W p(11);p[0]=0;for(int i=1;i<11;i++)p[i]=tail[i-1];total++;bool t=Tminus(p),x=Xmove(p);if(!t)noT++;if(!x)noX++;if(!t&&!x){local++;lr.insert(key(p));}}while(std::next_permutation(tail.begin(),tail.end()));
 std::unordered_set<uint64_t> done;done.reserve(lr.size());std::map<int,uint64_t>hist;uint64_t goodwords=0,goodorbits=0;
 for(uint64_t k:lr){if(done.count(k))continue;W p(11);for(int i=0;i<11;i++)p[i]=(k>>(4*i))&15;auto o=orbit(p);bool good=true;for(auto u:o)if(!lr.count(u)){good=false;break;} if(good){for(auto u:o)done.insert(u);hist[(int)o.size()]++;goodwords+=o.size();goodorbits++;} else done.insert(k);}
 if(total!=3628800ULL||noT!=393410ULL||noX!=1971006ULL||local!=325398ULL||goodwords!=270630ULL||goodorbits!=12786ULL||hist[1]!=8ULL||hist[11]!=954ULL||hist[22]!=11824ULL) return 5;
 std::cout<<"VERIFY_OK total="<<total<<" no_Tminus="<<noT<<" no_X="<<noX<<" local_rigid="<<local<<" dihedrally_local_rigid_words="<<goodwords<<" dihedral_orbits="<<goodorbits<<" orbit_sizes=1:"<<hist[1]<<",11:"<<hist[11]<<",22:"<<hist[22]<<"\n";
}
