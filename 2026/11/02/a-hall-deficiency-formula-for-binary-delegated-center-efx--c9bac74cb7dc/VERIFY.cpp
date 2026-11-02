// Exact finite cross-check of an EFX deficit theorem for two-person centers.
// Only binary additive values and one good per individual are considered.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <random>
#include <vector>
using namespace std;

// Independent brute-force enumeration of maximum distinct good representatives.
int match_rank(int k, const vector<int>& like) {
    int m=2*k, best=0;
    auto rec = [&](auto&& self,int i,int used,int count)->void {
        if(i==k){best=max(best,count);return;}
        self(self,i+1,used,count);
        for(int g=0;g<m;g++) if((like[i]&(1<<g)) && !(used&(1<<g)))
            self(self,i+1,used|(1<<g),count+1);
    };
    rec(rec,0,0,0);return best;
}

bool check(int k,const vector<int>& agents) {
    int m=2*k;
    vector<int> like(k,0);
    for(int i=0;i<k;i++) like[i]=agents[2*i]|agents[2*i+1];
    int active=0;
    for(int a:like) active+=(a!=0);
    int delta=active-match_rank(k,like);
    vector<int> goods(m), best(4,0);
    for(int g=0;g<m;g++) goods[g]=g;
    do {
        int count[4]={0,0,0,0};
        for(int i=0;i<k;i++) {
            int g=goods[2*i],h=goods[2*i+1];
            auto val=[&](int person,int item){return (agents[person]>>item)&1;};
            int realized=val(2*i,g)+val(2*i+1,h);
            int ip= ((like[i]>>g)&1)+((like[i]>>h)&1);
            int bp=max(realized,val(2*i,h)+val(2*i+1,g));
            int own[4]={ip,realized,bp,realized};
            for(int type=0;type<4;type++){
                bool good=true;
                for(int j=0;j<k;j++) if(j!=i){
                    // Removing each of the other center's two singleton goods
                    // leaves a singleton with potential value 0 or 1.
                    int a=goods[2*j],b=goods[2*j+1];
                    int after_remove_a=(like[i]>>b)&1;
                    int after_remove_b=(like[i]>>a)&1;
                    if(own[type]<after_remove_a || own[type]<after_remove_b){good=false;break;}
                }
                count[type]+=good;
            }
        }
        for(int t=0;t<4;t++) best[t]=max(best[t],count[t]);
    } while(next_permutation(goods.begin(),goods.end()));
    for(int t=0;t<4;t++) if(best[t]!=k-delta) {
        printf("COUNTEREXAMPLE k=%d type=%d active=%d rank=%d best=%d masks:",k,t,active,active-delta,best[t]);
        for(int z:agents) printf(" %d",z);
        printf("\n");
        return false;
    }
    return true;
}
int main(){
    long long exhaustive=0,samples=0;
    for(unsigned mask=0;mask<(1u<<16);mask++) {
        vector<int> agents(4);
        for(int i=0;i<4;i++)agents[i]=(mask>>(4*i))&15;
        if(!check(2,agents))return 1;
        exhaustive++;
    }
    mt19937 rng(431726);
    for(int t=0;t<1024;t++){
        vector<int> agents(6);
        for(int &a:agents)a=rng()&63;
        if(!check(3,agents))return 2;
        samples++;
    }
    // Capacity-three boundary: both centers want precisely the same three of six goods.
    // Every center receives three goods, and no split of three desirable goods is EFX.
    vector<int> b(6); for(int i=0;i<6;i++) b[i]=7;
    vector<int> seq={0,1,2,3,4,5};
    int valid=0, total=0;
    do {
       total++;
       int a=0,c=0;
       for(int j=0;j<3;j++) a+=((7>>seq[j])&1);
       for(int j=3;j<6;j++) c+=((7>>seq[j])&1);
       bool efx=(a>=c-((c==3)?1:0)) && (c>=a-((a==3)?1:0));
       // The formula above cannot replace the actual all-removals test: if a center
       // has any unliked good, removing it leaves the full count of liked goods.
       bool direct=true;
       for(int i=0;i<2;i++) {
         int self=0;
         for(int j=0;j<3;j++) self+=((7>>seq[3*i+j])&1);
         for(int r=0;r<3;r++) {
           int rem=0;
           for(int j=0;j<3;j++) if(j!=r) rem+=((7>>seq[3*(1-i)+j])&1);
           if(self<rem) direct=false;
         }
       }
       (void)efx;
       valid+=direct;
    } while(next_permutation(seq.begin(),seq.end()));
    if(valid!=0 || total!=720) return 3;
    printf("VERIFY_OK exhaustive_two_center_agent_profiles=%lld random_three_center_profiles=%lld valuation_variants=4 capacity_three_boundary=720/720_infeasible\n",exhaustive,samples);
}
