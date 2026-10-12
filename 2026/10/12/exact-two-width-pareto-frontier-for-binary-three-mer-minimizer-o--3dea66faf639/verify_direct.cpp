// Exhaustive independent word-by-word density and Pareto verification.
// Build: c++ -std=c++17 -O3 verify_direct.cpp -o verify_direct
#include <array>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using Order = array<int,8>;
int main(){
    array<array<int,10>,4096> words{};
    for(int mask=0;mask<4096;mask++)
      for(int p=0;p<10;p++) words[mask][p]=(mask>>(9-p))&7;
    Order order{0,1,2,3,4,5,6,7};
    map<pair<int,int>,int> frequencies;
    map<int,int> best9by4;
    int min4=100000, min9=100000, total=0;
    set<Order> optim4, optim9;
    do {
      int rank[8];for(int j=0;j<8;j++)rank[order[j]]=j;
      int d4=0,d9=0;
      for(int mask=0;mask<4096;mask++) {
        const auto &km=words[mask];
        // The last w+3 bits encode a binary word containing w+1 3-mers.
        for(int w: {4,9}) {
          if(w==4 && mask>=128) continue;
          int shift=9-w;
          int minold=8;
          for(int p=0;p<w;p++)minold=min(minold,rank[km[p+shift]]);
          bool changed=(rank[km[shift]]==minold) || (rank[km[w+shift]]<minold);
          if(changed){if(w==4)d4++;else d9++;}
        }
      }
      frequencies[{d4,d9}]++;
      if(d4<min4){min4=d4;optim4.clear();}if(d4==min4)optim4.insert(order);
      if(d9<min9){min9=d9;optim9.clear();}if(d9==min9)optim9.insert(order);
      total++;
    } while(next_permutation(order.begin(),order.end()));
    vector<pair<int,int>> pareto;
    int lower9=100000;
    for(auto [scores, count]:frequencies){
      if(scores.second<lower9){pareto.push_back(scores);lower9=scores.second;}
    }
    cout << "orders="<<total<<" distinct_score_pairs="<<frequencies.size()<<"\n";
    cout << "w4_min="<<min4<<" count="<<optim4.size()<<" w9_min="<<min9<<" count="<<optim9.size()<<"\n";
    cout << "intersection=";
    int inter=0;for(auto o:optim4)if(optim9.count(o))inter++;cout<<inter<<"\n";
    for(auto p:pareto)cout<<"PARETO="<<p.first<<","<<p.second<<" count="<<frequencies[p]<<"\n";
    if(total!=40320 || min4!=46 || min9!=750 || optim4.size()!=48 || optim9.size()!=48 || inter!=0 || pareto!=vector<pair<int,int>>({{46,759},{50,750}}) || frequencies[{46,759}]!=48 || frequencies[{50,750}]!=32)
      return 1;
    cout<<"VERIFY_OK\n";
    return 0;
}
