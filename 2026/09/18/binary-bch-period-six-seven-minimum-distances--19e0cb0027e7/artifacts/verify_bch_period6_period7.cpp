#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

static int deg_poly(uint32_t a){ return a ? 31-__builtin_clz(a) : -1; }
static uint32_t poly_mod(uint32_t a,uint32_t b){ int db=deg_poly(b); while(a && deg_poly(a)>=db) a ^= b << (deg_poly(a)-db); return a; }
static uint32_t poly_gcd(uint32_t a,uint32_t b){ while(b){ uint32_t r=poly_mod(a,b); a=b; b=r; } return a; }

struct GF2m {
  int m; uint32_t mod, mask;
  uint32_t mul(uint32_t a,uint32_t b) const {
    uint32_t r=0;
    while(b){
      if(b&1u) r^=a;
      b>>=1; a<<=1;
      if(a&(1u<<m)) a^=mod;
    }
    return r&mask;
  }
  uint32_t pw(uint32_t a,uint64_t e) const {
    uint32_t r=1;
    while(e){ if(e&1u) r=mul(r,a); a=mul(a,a); e>>=1; }
    return r;
  }
  bool irreducible(const vector<int>& prime_divisors_of_m) const {
    uint32_t x=2u, y=x;
    vector<uint32_t> frob(m+1); frob[0]=x;
    for(int i=1;i<=m;i++){ y=mul(y,y); frob[i]=y; }
    if(frob[m]!=x) return false;
    for(int p:prime_divisors_of_m){
      int k=m/p;
      if(poly_gcd(mod,frob[k]^x)!=1u) return false;
    }
    return true;
  }
};

static vector<int> distinct_prime_factors(uint64_t n){
  vector<int> out;
  for(uint64_t p=2;p*p<=n;p+=(p==2?1:2)) if(n%p==0){ out.push_back((int)p); while(n%p==0)n/=p; }
  if(n>1) out.push_back((int)n);
  return out;
}

static bool has_exact_order(const GF2m& F,uint32_t a,uint64_t order){
  if(F.pw(a,order)!=1u) return false;
  for(int p:distinct_prime_factors(order)) if(F.pw(a,order/p)==1u) return false;
  return true;
}

static uint64_t syndrome(uint32_t a,uint32_t a3,int m){ return (uint64_t(a)<<m)|a3; }

struct PairEntry {
  uint64_t key; uint16_t i,j;
  bool operator<(PairEntry const& o) const { return key<o.key; }
};

static bool exhaustive_weight5_absence_4161(const GF2m& F,uint32_t theta){
  const int N=4161;
  vector<uint64_t> s(N);
  uint32_t a=1,a3=1,th3=F.mul(F.mul(theta,theta),theta);
  for(int i=0;i<N;i++){
    s[i]=syndrome(a,a3,F.m);
    a=F.mul(a,theta); a3=F.mul(a3,th3);
  }
  vector<PairEntry> pairs;
  pairs.reserve(uint64_t(N-1)*(N-2)/2);
  for(int i=1;i<N;i++) for(int j=i+1;j<N;j++) pairs.push_back({s[i]^s[j],(uint16_t)i,(uint16_t)j});
  sort(pairs.begin(),pairs.end());
  const uint64_t target=s[0];
  for(const auto& e:pairs){
    uint64_t want=e.key^target;
    auto it=lower_bound(pairs.begin(),pairs.end(),PairEntry{want,0,0});
    for(;it!=pairs.end() && it->key==want;++it){
      if(e.i!=it->i && e.i!=it->j && e.j!=it->i && e.j!=it->j) return false;
    }
  }
  return true;
}

static bool relation_zero(const GF2m& F,uint32_t theta,const vector<int>& exps){
  uint32_t s1=0,s3=0;
  for(int e:exps){ uint32_t z=F.pw(theta,e); s1^=z; s3^=F.pw(z,3); }
  return s1==0 && s3==0;
}

static vector<int> cyclotomic_coset(int a,int n){
  vector<int> c;
  int x=a%n, start=x;
  do{ c.push_back(x); x=(2*x)%n; }while(x!=start);
  return c;
}
static bool disjoint_cosets(const vector<int>& a,const vector<int>& b){
  for(int x:a) if(find(b.begin(),b.end(),x)!=b.end()) return false;
  return true;
}

int main(){
  // s=6: F_2^18 = F_2[t]/(t^18+t^3+1), with primitive element g=t^3+t (integer 10).
  GF2m F18{18,(1u<<18)|(1u<<3)|1u,(1u<<18)-1};
  const uint64_t Q18=(1u<<18)-1, N6=4161;
  uint32_t g18=10u, theta6=F18.pw(g18,Q18/N6);
  bool p18_irred=F18.irreducible({2,3});
  bool g18_primitive=has_exact_order(F18,g18,Q18);
  bool theta6_order=has_exact_order(F18,theta6,N6);
  vector<int> w6={0,7,1801,2305,3181,3244};
  bool w6_ok=relation_zero(F18,theta6,w6);
  bool no_w5=exhaustive_weight5_absence_4161(F18,theta6);
  auto C1_6=cyclotomic_coset(1,N6), C3_6=cyclotomic_coset(3,N6);
  int c1_6=(int)C1_6.size(), c3_6=(int)C3_6.size();
  bool disj6=disjoint_cosets(C1_6,C3_6);

  // period 7: F_2^21 = F_2[t]/(t^21+t^2+1), where t is primitive.
  GF2m F21{21,(1u<<21)|(1u<<2)|1u,(1u<<21)-1};
  const uint64_t Q21=(1u<<21)-1, M7=16513;
  uint32_t g21=2u, theta7=F21.pw(g21,Q21/M7);
  bool p21_irred=F21.irreducible({3,7});
  bool g21_primitive=has_exact_order(F21,g21,Q21);
  bool theta7_order=has_exact_order(F21,theta7,M7);
  vector<int> w5_7={0,254,267,1729,2966};
  bool w5_7_ok=relation_zero(F21,theta7,w5_7);
  auto C1_7=cyclotomic_coset(1,M7), C3_7=cyclotomic_coset(3,M7);
  int c1_7=(int)C1_7.size(), c3_7=(int)C3_7.size();
  bool disj7=disjoint_cosets(C1_7,C3_7);

  cout << "p18_irreducible=" << p18_irred << "\n";
  cout << "g18_primitive=" << g18_primitive << "\n";
  cout << "theta6_order_4161=" << theta6_order << "\n";
  cout << "s6_weight6_relation=" << w6_ok << " support=0,7,1801,2305,3181,3244\n";
  cout << "s6_no_weight5_exhaustive=" << no_w5 << "\n";
  cout << "s6_coset_sizes=" << c1_6 << "," << c3_6 << " disjoint=" << disj6 << " dimension=" << (N6-c1_6-c3_6) << "\n";
  cout << "p21_irreducible=" << p21_irred << "\n";
  cout << "g21_primitive=" << g21_primitive << "\n";
  cout << "theta7_order_16513=" << theta7_order << "\n";
  cout << "period7_weight5_relation=" << w5_7_ok << " support=0,254,267,1729,2966\n";
  cout << "s7_coset_sizes=" << c1_7 << "," << c3_7 << " disjoint=" << disj7 << " dimension=" << (M7-c1_7-c3_7) << "\n";

  bool ok=p18_irred&&g18_primitive&&theta6_order&&w6_ok&&no_w5&&c1_6==18&&c3_6==18&&disj6
       &&p21_irred&&g21_primitive&&theta7_order&&w5_7_ok&&c1_7==21&&c3_7==21&&disj7;
  cout << "VERDICT=" << (ok?"PASS":"FAIL") << "\n";
  return ok?0:1;
}
