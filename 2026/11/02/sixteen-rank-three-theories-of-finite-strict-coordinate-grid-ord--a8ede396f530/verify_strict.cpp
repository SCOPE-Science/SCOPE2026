// Exact three-round Ehrenfeucht-Fraisse types of strict-coordinate chain products.
// Compile: g++ -std=c++17 -O2 verify_strict.cpp -o verify_strict
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>
using namespace std;
using V = vector<int>;

static int intern(map<V, int>& dictionary, V v) {
  sort(v.begin(),v.end());
  v.erase(unique(v.begin(),v.end()),v.end());
  auto it=dictionary.find(v);
  if (it!=dictionary.end()) return it->second;
  int result=(int)dictionary.size()+1;
  dictionary.emplace(move(v),result);
  return result;
}

int main() {
  map<V,int> level1,level2,level3;
  map<pair<int,int>,int> signatures;
  map<int,pair<int,int>> root_to_signature;
  int count=0;
  for (int m=1;m<=7;m++) for (int n=m;n<=7;n++) {
    int N=m*n;
    vector<pair<int,int>> point;
    for (int i=0;i<m;i++) for (int j=0;j<n;j++) point.emplace_back(i,j);
    vector<unsigned char> le(N*N);
    for (int a=0;a<N;a++) for (int b=0;b<N;b++) {
      le[a*N+b] = point[a].first<point[b].first && point[a].second<point[b].second;
    }
    vector<int> T1(N*N);
    for (int a=0;a<N;a++) for (int b=0;b<N;b++) {
      V successors; successors.reserve(N);
      for (int c=0;c<N;c++) {
        int triple[3]={a,b,c}; int atomic=0;
        for (int i=0;i<3;i++) for (int j=0;j<3;j++) {
          atomic |= int(le[triple[i]*N+triple[j]])<<(3*i+j);
        }
        for (int i=0;i<3;i++) for (int j=i+1;j<3;j++) atomic |= int(triple[i]==triple[j])<<(9+i*3+j);
        successors.push_back(atomic);
      }
      T1[a*N+b]=intern(level1,move(successors));
    }
    V T2(N);
    for (int a=0;a<N;a++) {
      V successors; successors.reserve(N);
      for (int b=0;b<N;b++) successors.push_back(T1[a*N+b]);
      T2[a]=intern(level2,move(successors));
    }
    int root=intern(level3,move(T2));
    int a=min(m,7), b=min(n,7);
    int cap=(a==1?3:(a==2?4:(a==3?5:6)));
    pair<int,int> key = a==7 ? make_pair(7,7):make_pair(a,min(b,cap));
    auto it=signatures.find(key);
    if (it==signatures.end()) signatures.emplace(key,root);
    else assert(it->second==root);
    auto jt=root_to_signature.find(root);
    if (jt==root_to_signature.end()) root_to_signature.emplace(root,key);
    else assert(jt->second==key);
    count++;
  }
  assert(count==28); // all unordered pairs of sizes 1,...,7
  assert(signatures.size()==16 && root_to_signature.size()==16);
  int largest=0;
  cout << "exact_root_classes=16\n";
  for (const auto& [key, root]:signatures) {
    int elements=key.first*key.second;
    largest=max(largest,elements);
    cout << key.first << ',' << key.second << ":" << elements << "\n";
  }
  assert(largest==49);
  cout << "sharp_within_family_representative_size=49\n";
  cout << "unordered_tested_pairs=" << count << "\n";
  cout << "verification=PASS\n";
}
