#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <vector>

// Exact finite certificate for perfect matching cuts in GP(n,3).
// Compile: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify

void demand(bool ok, const char *why) {
    if (!ok) throw std::runtime_error(why);
}
int bit(int x,int i) { return (x>>i)&1; }
int local_b(const int a[9],int mid) {
    const int d=(a[mid]!=a[mid-1])+(a[mid]!=a[mid+1]);
    if(d==2) return -1;
    return d==0 ? 1-a[mid] : a[mid];
}
bool valid_window(int nine) {
    int a[9];
    for(int j=0;j<9;j++) a[j]=bit(nine,j);
    int left=local_b(a,1),mid=local_b(a,4),right=local_b(a,7);
    if(left<0||mid<0||right<0) return false;
    return (mid!=left)+(mid!=right)+(mid!=a[4])==1;
}
int expected(int n) { return 1+(n%4==0?2:0)+(n%5==0?5:0); }
int main(){
    try {
        std::vector<std::vector<int>> adj(256);
        for(int s=0;s<256;s++) for(int q=0;q<2;q++) {
            int nine=s|(q<<8);
            if(valid_window(nine)) adj[s].push_back((s>>1)|(q<<7));
        }
        int edges=0;for(const auto &v:adj) edges+=(int)v.size();
        demand(edges==90,"nine-bit edge count");
        std::set<int> core;for(int x=0;x<256;x++)core.insert(x);
        int rounds[4]={256,42,20,16};
        for(int round=1;round<=3;round++) {
            std::set<int> next;
            for(int v:core){
                bool outgoing=false,incoming=false;
                for(int w:adj[v])if(core.count(w))outgoing=true;
                for(int u:core)if(std::find(adj[u].begin(),adj[u].end(),v)!=adj[u].end())incoming=true;
                if(outgoing&&incoming)next.insert(v);
            }
            core.swap(next);
            demand((int)core.size()==rounds[round],"pruning core size");
        }
        std::map<int,int> expected_arc={
            {0,0},{255,255},
            {51,153},{153,204},{204,102},{102,51},
            {24,140},{140,198},{198,99},{99,49},{49,24},
            {57,156},{156,206},{206,231},{231,115},{115,57}
        };
        demand(core.size()==expected_arc.size(),"number of recurrent states");
        for(int v:core) {
            demand(expected_arc.count(v),"unexpected recurrent state");
            std::vector<int> inner;
            for(int w:adj[v])if(core.count(w))inner.push_back(w);
            demand(inner.size()==1&&inner[0]==expected_arc.at(v),"unexpected recurrent arc");
        }
        for(int n=7;n<=100;n++) {
            int closed=0;
            for(int start:core){
                int cur=start;
                for(int k=0;k<n;k++)cur=expected_arc.at(cur);
                if(cur==start)closed++;
            }
            int oriented=2*expected(n);
            demand(closed==oriented,"closed-walk enumeration");
        }
        // Independent verification: enumerate ALL vertex 2-colorings with
        // the first outer vertex fixed to zero, and check original graph edges.
        std::uint64_t assignments=0;
        for(int n=7;n<=12;n++) {
            const std::uint64_t limit=(1ULL<<(2*n-1));
            std::map<int,int> by_spokes;
            for(std::uint64_t x=0;x<limit;x++) {
                std::uint64_t mask=x<<1;
                bool good=true;
                for(int i=0;i<n;i++){
                    int a=(mask>>i)&1;
                    int left=(mask>>((i+n-1)%n))&1;
                    int right=(mask>>((i+1)%n))&1;
                    int b=(mask>>(n+i))&1;
                    if((a!=left)+(a!=right)+(a!=b)!=1){good=false;break;}
                }
                if(!good)continue;
                int spoke_count=0;
                for(int i=0;i<n;i++){
                    int a=(mask>>i)&1;
                    int b=(mask>>(n+i))&1;
                    int left=(mask>>(n+((i+n-3)%n)))&1;
                    int right=(mask>>(n+((i+3)%n)))&1;
                    if((b!=left)+(b!=right)+(b!=a)!=1){good=false;break;}
                    spoke_count+=(a!=b);
                }
                if(good)by_spokes[spoke_count]++;
            }
            int count=0;for(auto [spoke,c]:by_spokes)count+=c;
            demand(count==expected(n),"independent all-colorings test");
            std::map<int,int> target={{n,1}};
            if(n%4==0)target[0]=2;
            if(n%5==0)target[n/5]=5;
            demand(by_spokes==target,"spoke-stratum counts");
            assignments+=limit;
        }
        // Directly verify representatives of both nontrivial families at multiples.
        auto witness=[](int n,const std::vector<int> &a0,const std::vector<int> &b0){
            std::vector<int>a(n),b(n);
            for(int i=0;i<n;i++){a[i]=a0[i%(int)a0.size()];b[i]=b0[i%(int)b0.size()];}
            for(int i=0;i<n;i++){
                if((a[i]!=a[(i+n-1)%n])+(a[i]!=a[(i+1)%n])+(a[i]!=b[i])!=1)return false;
                if((b[i]!=b[(i+n-3)%n])+(b[i]!=b[(i+3)%n])+(b[i]!=a[i])!=1)return false;
            }
            return true;
        };
        for(int n=8;n<=100;n+=4) demand(witness(n,{0,0,1,1},{0,0,1,1}),"period-4 family");
        for(int n=10;n<=100;n+=5) demand(witness(n,{0,0,0,1,1},{0,1,0,1,1}),"period-5 family");
        std::cout<<"VERIFY_OK core=16 cycles=1,1,4,5,5; full-graph n=7..12; colorings_examined="
                 <<assignments<<"; checked n through 100\n";
        return 0;
    }catch(const std::exception &e){std::cerr<<"VERIFY_FAILED "<<e.what()<<"\n";return 1;}
}
