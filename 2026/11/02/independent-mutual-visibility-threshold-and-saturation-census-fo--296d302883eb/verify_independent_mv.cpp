// Direct graph-distance verifier for independent mutual-visibility in P_L square K_m.
// Compile: c++ -O3 -std=c++17 verify_independent_mv.cpp -o verify_independent_mv
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int L, m, want, best;
vector<int> choice, used;
uint64_t count_best, admissible_count, checked_candidates;

bool has_geodesic_without_other_landmarks(int p, int q){
    int a=p/m, b=q/m;
    int expected=abs(a-b)+(p%m != q%m);
    array<int,50> distance;
    distance.fill(-1);
    int queue_[50], front=0, back=0;
    queue_[back++]=p; distance[p]=0;
    while(front<back){
      int x=queue_[front++];
      if(x==q) return distance[x]==expected;
      if(distance[x]>=expected) continue;
      int layer=x/m, color=x%m;
      auto add = [&](int y){
        if(distance[y]!=-1) return;
        int layer_y=y/m, color_y=y%m;
        if(y!=q && y!=p && choice[layer_y]==color_y) return;
        distance[y]=distance[x]+1; queue_[back++]=y;
      };
      if(layer>0) add(x-m);
      if(layer+1<L) add(x+m);
      for(int c=0;c<m;c++) if(c!=color) add(layer*m+c);
    }
    return false;
}

bool is_independent_visible(){
   vector<int> landmarks;
   for(int i=0;i<L;i++) if(choice[i]>=0) landmarks.push_back(i*m+choice[i]);
   for(size_t i=0;i<landmarks.size();i++)
     for(size_t j=i+1;j<landmarks.size();j++)
       if(!has_geodesic_without_other_landmarks(landmarks[i], landmarks[j])) return false;
   return true;
}

void search(int i,int chosen){
    if(chosen+L-i<want) return;
    if(i==L){
       checked_candidates++;
       if(is_independent_visible()){
          admissible_count++;
          if(chosen>best){best=chosen;count_best=0;}
          if(chosen==best) count_best++;
       }
       return;
    }
    choice[i]=-1; search(i+1,chosen);
    for(int c=0;c<m;c++){
       if(used[c]==2) continue;
       if(i>0 && choice[i-1]==c) continue;
       used[c]++; choice[i]=c;search(i+1,chosen+1);used[c]--;
    }
    choice[i]=-1;
}

uint64_t fact(int k){uint64_t x=1;for(int i=2;i<=k;i++) x*=i;return x;}
uint64_t binom(int n,int k){if(n<k || k<0)return 0; uint64_t x=1;for(int j=1;j<=k;j++) x=x*(n-j+1)/j;return x;}

int main(){
    for(int colors=2;colors<=4;colors++){
      for(int layers=2;layers<=2*colors+3;layers++){
        L=layers;m=colors;
        want=(L<2*m ? L : (L==2*m ? 2*m-1 : 2*m));
        choice.assign(L,-1);used.assign(m,0);best=-1;
        count_best=admissible_count=checked_candidates=0;
        search(0,0);
        if(best!=want){cerr<<"FAIL dimension m="<<m<<" L="<<L<<" got="<<best<<" want="<<want<<"\n";return 1;}
        if(L>=2*m+1){
           uint64_t target=fact(m)*fact(m)*binom(L-1,2*m);
           if(count_best!=target){cerr<<"FAIL count m="<<m<<" L="<<L<<" got="<<count_best<<" want="<<target<<"\n";return 2;}
        }
        cout << "m="<<m<<" L="<<L<<" maximum="<<best
             <<" optimal_count="<<count_best
             <<" candidates_tested="<<checked_candidates<<"\n";
      }
    }
    cout << "VERIFY_OK\n";
}
