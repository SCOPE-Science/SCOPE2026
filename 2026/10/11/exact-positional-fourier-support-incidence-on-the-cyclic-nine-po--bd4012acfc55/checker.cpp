// Exact support-incidence census for the order-nine Fourier matrix.
// Two split-prime reductions are jointly an exact cyclotomic rank certificate.
#include <bits/stdc++.h>
using namespace std;
using U = uint64_t;
using W = unsigned __int128;
static constexpr int N=9, SZ=1<<9;
static constexpr U P1=100000000000099ULL,P2=100000001000377ULL;
U power(U a,U b,U m){U v=1;while(b){if(b&1)v=(U)((W)v*a%m);a=(U)((W)a*a%m);b>>=1;}return v;}
int pop(int x){return __builtin_popcount((unsigned)x);}
bool is_prime(U n) { // Elementary trial division, not a probable-prime test.
 if(n<2)return false;
 if((n&1)==0)return n==2;
 for(U d=3;d<=n/d;d+=2)if(n%d==0)return false;
 return true;
}
int action_mask(int mask,int unit,int shift){
 int out=0;
 for(int x=0;x<9;x++)if(mask>>x&1)out|=1<<((unit*x+shift)%9);
 return out;
}

struct FieldRank {
 U p, root, F[N][N];
 unordered_map<U,U> inverses;
 FieldRank(U prime):p(prime){
  U generator=2;while(power(generator,(p-1)/3,p)==1||power(generator,(p-1)/2,p)==1)++generator;
  // An element of exact order nine is certified by r^9=1 and r^3!=1.
  root=power(generator,(p-1)/9,p);
  if(power(root,9,p)!=1 || power(root,3,p)==1) throw runtime_error("nonprimitive ninth root");
  for(int i=0;i<N;i++)for(int j=0;j<N;j++)F[i][j]=power(root,(i*j)%9,p);
  cerr<<"prime="<<p<<" ninth_root="<<root<<"\n";
 }
 U inverse(U x){auto it=inverses.find(x);if(it!=inverses.end())return it->second;
  U val=power(x,p-2,p);inverses.emplace(x,val);return val;}
 unsigned char rank(int A,int R){
  U X[9][9]{};int nc=0,nr=0,cols[9];
  for(int j=0;j<9;j++)if(A>>j&1)cols[nc++]=j;
  for(int i=0;i<9;i++)if(R>>i&1){for(int j=0;j<nc;j++)X[nr][j]=F[i][cols[j]];nr++;}
  int rk=0;
  for(int j=0;j<nc&&rk<nr;j++){
   int t=rk;while(t<nr&&X[t][j]==0)t++;
   if(t==nr)continue;
   if(t!=rk)for(int k=j;k<nc;k++)swap(X[rk][k],X[t][k]);
   U inv=inverse(X[rk][j]);
   for(int i=rk+1;i<nr;i++){
    U f=(U)((W)X[i][j]*inv%p);
    if(f==0)continue;
    for(int k=j+1;k<nc;k++){
     U sub=(U)((W)f*X[rk][k]%p);
     X[i][k]=X[i][k]>=sub?X[i][k]-sub:X[i][k]+p-sub;
    }
    X[i][j]=0;
   }
   rk++;
  }
  return (unsigned char)rk;
 }
};
int main(){
 // Hadamard: for each minor of order k <=9 and each of the 6 embeddings,
 // |sigma(det)| <= k^(k/2). Thus |Norm det| <= k^(3k) <= 9^27.
 W bound=1;for(int i=0;i<27;i++)bound*=9;
 if((W)P1*(W)P2<=bound)throw runtime_error("insufficient norm bound");
 if(!is_prime(P1)||!is_prime(P2))throw runtime_error("composite reduction modulus");
 cerr<<"PRIMES_VERIFIED\n";
 vector<unsigned char> ranks1(SZ*SZ),ranks2(SZ*SZ);
 for(int z=0;z<2;z++){
   FieldRank fld(z?P2:P1);
   auto& arr=z?ranks2:ranks1;
   for(int A=0;A<SZ;A++)for(int R=0;R<SZ;R++)arr[A*SZ+R]=fld.rank(A,R);
   cerr<<"rank table "<<z+1<<" complete, inverse_cache="<<fld.inverses.size()<<"\n";
 }
 auto rank=[&](int A,int R){return max(ranks1[A*SZ+R],ranks2[A*SZ+R]);};
 long long matrix[10][10]{};long long total=0;
 vector<unsigned char> realized(SZ*SZ);
 for(int A=1;A<SZ;A++)for(int B=1;B<SZ;B++){
   int R=511^B, r=rank(A,R), aa=pop(A);
   if(r>=aa)continue;
   bool valid=true;
   for(int a=0;a<9&&valid;a++)if(A>>a&1)if(rank(A^(1<<a),R)!=r)valid=false;
   for(int b=0;b<9&&valid;b++)if(B>>b&1)if(rank(A,R|(1<<b))==r)valid=false;
   if(valid){matrix[aa][pop(B)]++;total++;realized[A*SZ+B]=1;}
 }
 cout<<"ORDER_9_EXACT_SUPPORT_PAIRS "<<total<<"\n";
 for(int a=1;a<=9;a++){
   cout<<a<<": ";for(int b=1;b<=9;b++)cout<<matrix[a][b]<<(b==9?'\n':' ');
   for(int b=1;b<=9;b++)if(matrix[a][b]!=matrix[b][a])throw runtime_error("Fourier transpose fails");
 }
 auto orbit_census=[&](bool dual){
 vector<unsigned char> seen(SZ*SZ);
 map<int,int> counts;map<int,map<int,int>> by_size;int norbits=0;
 for(int A=1;A<SZ;A++)for(int B=1;B<SZ;B++){
  int seed=A*SZ+B;
  if(!realized[seed]||seen[seed])continue;
  vector<int> todo{seed};seen[seed]=1;
  for(size_t j=0;j<todo.size();j++){
   int id=todo[j],x=id/SZ,y=id%SZ;
   int a[4]={action_mask(x,1,1),x,action_mask(x,2,0),y};
   int b[4]={y,action_mask(y,1,1),action_mask(y,5,0),action_mask(x,8,0)};
   for(int k=0;k<(dual?4:3);k++){
    int nxt=a[k]*SZ+b[k];
    if(!realized[nxt])throw runtime_error("claimed Fourier symmetry not preserving incidence");
    if(!seen[nxt]){seen[nxt]=1;todo.push_back(nxt);}
   }
  }
  counts[(int)todo.size()]++;by_size[10*pop(A)+pop(B)][(int)todo.size()]++;norbits++;
 }
 cout<<(dual?"AFFINE_AND_FOURIER_DUAL":"AFFINE_ONLY")<<"_ORBITS "<<norbits<<" SIZES";
 long long check=0;
 for(auto [sz,num]:counts){cout<<" "<<sz<<":"<<num;check+=sz*num;}
 cout<<"\n";if(check!=total)throw runtime_error("orbit size checksum");
 if(!dual)for(int key:{33,45,55,26,46}){
  cout<<"AFFINE_SIZE_PAIR_"<<key/10<<"_"<<key%10<<" ORBITS";
  for(auto [n,num]:by_size[key])cout<<" "<<n<<":"<<num;
  cout<<"\n";
 }
 };
 orbit_census(false);orbit_census(true);
 if(total!=92236)throw runtime_error("independent small-prime count mismatch");
 cout<<"CHECK_PASS\n";
}
