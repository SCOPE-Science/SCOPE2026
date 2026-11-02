#include <bits/stdc++.h>
using namespace std;
using LL=long long;
// Original-graph exhaustive simulator and independent algebraic enumerator.
vector<LL> mult(vector<LL> a,const vector<LL>&b,int N){
 vector<LL> c(N+1);
 for(int i=0;i<(int)a.size();i++)for(int j=0;j<(int)b.size();j++)if(i+j<=N)c[i+j]+=a[i]*b[j];
 return c;
}
int main(){
 for(int n=3;n<=9;n++){
   int N=2*n;
   vector<vector<int>> nei(N);
   for(int i=0;i<n;i++){
     auto edge=[&](int a,int b){nei[a].push_back(b);nei[b].push_back(a);};
     edge(i,(i+1)%n);edge(i,n+i);
   }
   vector<LL> pred2(N+1),pred3(N+1),seen2(N+1),seen3(N+1);
   // Derive the full threshold-two polynomial by choosing all initially infected cycle cores,
   // then permitting zero or one unsupported pair in every intervening cyclic gap.
   for(int cm=1;cm<(1<<n);cm++){
     vector<int> pos;for(int i=0;i<n;i++)if(cm>>i&1)pos.push_back(i);
     vector<LL> poly(1,1);
     for(int i=0;i<(int)pos.size();i++){
       int a=pos[i],b=pos[(i+1)%pos.size()];
       int gap=(b-a-1+n)%n;
       if(pos.size()==1)gap=n-1;
       vector<LL> w(max(2,gap+1),0);
       w[gap]++;
       if(gap>0)w[gap-1]+=gap;
       // Core seeded, optional pendant also seeded: weight z+z^2.
       w=mult(w,vector<LL>{0,1,1},N);
       poly=mult(poly,w,N);
     }
     for(int k=0;k<=N && k<(int)poly.size();k++)pred2[k]+=poly[k];
   }
   // Independently sum full threshold-three polynomial over independent leaf-only positions.
   for(int st=0;st<(1<<n);st++){
     bool indep=true;
     for(int i=0;i<n;i++)if((st>>i&1)&&(st>>((i+1)%n)&1))indep=false;
     if(!indep)continue;
     int j=__builtin_popcount((unsigned)st);
     for(int other=0;other<(1<<(n-j));other++)pred3[n+__builtin_popcount((unsigned)other)]++;
   }
   for(int threshold=1;threshold<=3;threshold++){
     int best=N+1;LL mincount=0;
     for(unsigned mask=1;mask<(1u<<N);mask++){
       unsigned active=mask;
       while(1){
         unsigned added=0;
         for(int v=0;v<N;v++)if(!(active>>v&1)){
           int req=(v<n?threshold:1), cnt=0;
           for(int u:nei[v])cnt+=(active>>u&1);
           if(cnt>=req)added|=1u<<v;
         }
         if(!added)break;
         active|=added;
       }
       bool success=(active==(1u<<N)-1);
       if(threshold==2){
         vector<int> cores;for(int i=0;i<n;i++)if(mask>>i&1)cores.push_back(i);
         bool predicted=!cores.empty();
         if(predicted)for(int k=0;k<(int)cores.size();k++){
           int a=cores[k],b=cores[(k+1)%cores.size()];
           int gap=(b-a-1+n)%n;
           if(cores.size()==1)gap=n-1;
           int unsupported=0;
           for(int t=1;t<=gap;t++){
             int i=(a+t)%n;
             if(!(mask>>i&1)&&!(mask>>(n+i)&1))unsupported++;
           }
           if(unsupported>=2)predicted=false;
         }
         if(predicted!=success){cerr<<"GAP_CLASSIFICATION_FAIL n="<<n<<" mask="<<mask<<"\n";return 1;}
       }
       if(!success)continue;
       int size=__builtin_popcount(mask);
       if(size<best){best=size;mincount=0;}
       if(size==best)mincount++;
       if(threshold==2)seen2[size]++;
       if(threshold==3)seen3[size]++;
     }
     int m=(threshold==1?1:threshold==2?(n+1)/2:n);
     LL cnt=threshold==1?2LL*n:threshold==2?(n%2?3LL*n:2LL):pred3[n];
     if(best!=m||mincount!=cnt){cerr<<"MINIMUM_FAIL n="<<n<<" th="<<threshold<<" got="<<best<<","<<mincount<<" expected="<<m<<","<<cnt<<"\n";return 2;}
     cout<<"DIRECT_ALL_SUBSETS_MINIMUM_OK n="<<n<<" threshold="<<threshold<<" minimum="<<best<<" minimizers="<<mincount<<"\n";
   }
   if(pred2!=seen2){cerr<<"THRESHOLD_TWO_POLYNOMIAL_FAIL n="<<n<<"\n";return 3;}
   if(pred3!=seen3){cerr<<"THRESHOLD_THREE_POLYNOMIAL_FAIL n="<<n<<"\n";return 4;}
   cout<<"FULL_POLYNOMIAL_AND_GAP_CLASSIFICATION_OK n="<<n<<" all_subsets="<<(1u<<N)<<"\n";
 }
 cout<<"VERIFY_OK\n";
}
