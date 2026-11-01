#include <cstdint>
#include <iostream>
#include <vector>
#include <stdexcept>
#include <string>
#include <array>
using U = std::uint64_t;
struct Graph {
    int n;
    std::vector<U> neigh;
    Graph(int p,int q) : n(1+2*p+4*q), neigh(n,0) {
        int next=1;
        auto attach=[&](int length){
            std::vector<int> vertices{0};
            for(int i=1;i<length;i++) vertices.push_back(next++);
            for(int i=0;i<length;i++) {
                int u=vertices[i],v=vertices[(i+1)%length];
                neigh[u] |= U(1)<<v;
                neigh[v] |= U(1)<<u;
            }
        };
        for(int i=0;i<p;i++) attach(3);
        for(int j=0;j<q;j++) attach(5);
        if (next!=n || n>63) throw std::runtime_error("invalid graph");
    }
    U step(U state) const {
        U out=0;
        for(int v=0;v<n;v++) {
            if(__builtin_parityll(state & neigh[v]))out |= U(1)<<v;
        }
        return out;
    }
};
U power_two(int k){return U(1)<<k;}
int main(){
  U total=0, checked_even=0,checked_odd=0;
  int pairs=0,max_n=0;
  for(int p=0;p<=8;p++) for(int q=0;q<=4;q++) {
    if(p+q==0)continue;
    Graph g(p,q);
    if(g.n>17)continue;
    max_n=std::max(max_n,g.n);
    std::array<U,4> observed{0,0,0,0};
    U lim=power_two(g.n);
    for(U x=0;x<lim;x++){
       U y=x; std::array<U,8> z{};z[0]=x;
       for(int t=1;t<=7;t++){y=g.step(y);z[t]=y;}
       if(z[7]!=z[1]) {std::cerr<<"A7 != A at p="<<p<<",q="<<q<<",state="<<x<<"\n";return 1;}
       if(__builtin_parityll(x)==0){
          if(z[6]!=x){std::cerr<<"even state not periodic\n";return 2;}
          if(z[1]==x)observed[0]++;
          if(z[2]==x)observed[1]++;
          if(z[3]==x)observed[2]++;
          if(z[6]==x)observed[3]++;
          checked_even++;
       } else {
          if(z[6]==x){std::cerr<<"odd state periodic\n";return 3;}
          checked_odd++;
       }
    }
    int eP=p%2,eQ=q%2;
    std::array<U,4> predicted{
      power_two(p+eP),power_two(2*p),
      power_two(p+2*q+eP+2*eQ),power_two(2*p+4*q)
    };
    if(observed!=predicted){
       std::cerr<<"count failure p="<<p<<" q="<<q<<"\n";
       for(int t=0;t<4;t++)std::cerr<<t<<":"<<observed[t]<<" vs "<<predicted[t]<<"\n";
       return 4;
    }
    U f1=predicted[0],f2=predicted[1],f3=predicted[2],f6=predicted[3];
    if((f2-f1)%2 ||(f3-f1)%3 ||(f6-f2-f3+f1)%6){
        std::cerr<<"Möbius divisibility failure\n";return 5;
    }
    std::cout<<"p="<<p<<" q="<<q<<" n="<<g.n
        <<" fixed="<<f1<<" two="<<(f2-f1)/2
        <<" three="<<(f3-f1)/3<<" six="<<(f6-f2-f3+f1)/6<<"\n";
    ++pairs;total+=lim;
  }
  std::cout<<"VERIFIED: "<<pairs<<" complete parameter pairs, "<<total
     <<" labelled states; "<<checked_even<<" periodic at time zero, "
     <<checked_odd<<" first periodic at time one, max_n="<<max_n<<"\n";
  return 0;
}
