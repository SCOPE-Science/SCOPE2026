#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define N 7
#define NN 128
#define G 20
#define TOTAL (1u<<20)

int orbit_id[NN];
int orbit_min[G];
int orbit_wt[G];

int rot_r(int v){
    return ((v>>1) | ((v&1)<<6)) & 0x7F;
}

void build_orbits(){
    int visited[NN]={0};
    int tmp_orbits[G][NN];
    int tmp_sz[G];
    int cnt=0;
    for(int v=0; v<NN; v++) if(!visited[v]){
        int cur=v;
        int sz=0;
        for(int k=0;k<N;k++){
            if(!visited[cur]){ visited[cur]=1; tmp_orbits[cnt][sz++]=cur; }
            cur=rot_r(cur);
            if(cur==v) break;
        }
        tmp_sz[cnt]=sz;
        cnt++;
    }
    // sort by min
    // simple bubble
    for(int i=0;i<cnt;i++)for(int j=i+1;j<cnt;j++){
        int mi=tmp_orbits[i][0], mj=tmp_orbits[j][0];
        for(int k=1;k<tmp_sz[i];k++) if(tmp_orbits[i][k]<mi) mi=tmp_orbits[i][k];
        for(int k=1;k<tmp_sz[j];k++) if(tmp_orbits[j][k]<mj) mj=tmp_orbits[j][k];
        if(mj<mi){
            int t[NN]; memcpy(t,tmp_orbits[i],sizeof(t)); memcpy(tmp_orbits[i],tmp_orbits[j],sizeof(t)); memcpy(tmp_orbits[j],t,sizeof(t));
            int ts=tmp_sz[i]; tmp_sz[i]=tmp_sz[j]; tmp_sz[j]=ts;
        }
    }
    for(int i=0;i<G;i++){
        int mn=tmp_orbits[i][0];
        for(int k=1;k<tmp_sz[i];k++) if(tmp_orbits[i][k]<mn) mn=tmp_orbits[i][k];
        orbit_min[i]=mn;
        // weight = popcount of mn (rotation preserves weight)
        int w=0, x=mn; while(x){w+=x&1;x>>=1;}
        orbit_wt[i]=w;
        for(int k=0;k<tmp_sz[i];k++) orbit_id[tmp_orbits[i][k]]=i;
    }
}

// Mobius (ANF) transform in place over GF2, array of 0/1 length NN
void mobius(uint8_t *a){
    for(int len=1; len<NN; len<<=1){
        for(int i=0;i<NN;i+=len<<1){
            for(int j=0;j<len;j++){
                a[i+j+len] ^= a[i+j];
            }
        }
    }
}

// FWHT for Walsh, int array length NN
void fwht(int *a){
    for(int len=1; len<NN; len<<=1){
        for(int i=0;i<NN;i+=len<<1){
            for(int j=0;j<len;j++){
                int u=a[i+j], v=a[i+j+len];
                a[i+j]=u+v; a[i+j+len]=u-v;
            }
        }
    }
}

int main(){
    build_orbits();
    printf("orbits:\n");
    for(int i=0;i<G;i++) printf(" %2d min=%3d wt=%d\n", i, orbit_min[i], orbit_wt[i]);
    printf("g=%d formula=%d\n", G, (128+12)/7);

    // Precompute truth->ANF row masks (20-bit)
    uint32_t row_mask[G];
    memset(row_mask,0,sizeof(row_mask));
    // M[j][k]: ANF orbit j when truth = single orbit k
    for(int k=0;k<G;k++){
        uint8_t T[NN];
        for(int v=0;v<NN;v++) T[v]=(orbit_id[v]==k)?1:0;
        mobius(T);
        // read ANF orbit values: value at orbit_min[j]
        for(int j=0;j<G;j++){
            int rep=orbit_min[j];
            if(T[rep]) row_mask[j] |= (1u<<k);
        }
    }
    printf("row masks (ANF orbit j <- truth mask):\n");
    for(int j=0;j<G;j++) printf(" j=%2d min=%3d wt=%d mask=0x%05x\n", j, orbit_min[j], orbit_wt[j], row_mask[j]);
    // check invertibility via rank over GF2
    {
        uint32_t m[G]; for(int j=0;j<G;j++) m[j]=row_mask[j];
        // Actually matrix rows j, cols k. Compute rank by Gaussian elimination on 20x20
        int rank=0;
        uint32_t a[G]; for(int i=0;i<G;i++) a[i]=m[i];
        // transpose? rank same either way; eliminate
        int r=0;
        for(int c=0;c<G && r<G;c++){
            int piv=-1;
            for(int i=r;i<G;i++) if((a[i]>>c)&1u){piv=i;break;}
            if(piv<0) continue;
            uint32_t tmp=a[r]; a[r]=a[piv]; a[piv]=tmp;
            for(int i=0;i<G;i++) if(i!=r && ((a[i]>>c)&1u)) a[i]^=a[r];
            r++; rank++;
        }
        printf("ANF map rank=%d (expect 20)\n", rank);
    }

    long hist[129]={0};
    int32_t best_truth[129];
    uint32_t best_anf[129];
    int seen[129]={0};
    for(int i=0;i<129;i++) best_truth[i]=-1;

    // lex compare: bit0 most significant
    // helper inline
    int W[NN];
    for(uint32_t mask=0; mask<TOTAL; mask++){
        // build polarity
        // unrolled: a[v] = ((mask>>orbit_id[v])&1)? -1: 1
        for(int v=0;v<NN;v++) W[v]=((mask>>orbit_id[v])&1u)?-1:1;
        fwht(W);
        int mx=0;
        for(int v=0;v<NN;v++){int a=W[v]<0?-W[v]:W[v]; if(a>mx) mx=a;}
        int nl = 64 - mx/2;
        hist[nl]++;
        // ANF mask
        uint32_t anf=0;
        for(int j=0;j<G;j++){
            uint32_t inter = mask & row_mask[j];
            // parity
            // __builtin_parity
            if(__builtin_parity(inter)) anf|=(1u<<j);
        }
        if(!seen[nl]){
            seen[nl]=1; best_truth[nl]=(int32_t)mask; best_anf[nl]=anf;
        } else {
            uint32_t cur=best_anf[nl];
            // lex compare anf vs cur
            int less=0, greater=0;
            for(int k=0;k<G;k++){
                int ak=(anf>>k)&1u, ck=(cur>>k)&1u;
                if(ak!=ck){ if(ak<ck) less=1; else greater=1; break; }
            }
            if(less){ best_truth[nl]=(int32_t)mask; best_anf[nl]=anf; }
            else if(!greater){
                // equal ANF => keep smaller truth mask (already first)
            }
        }
        if((mask & 0xFFFFF)==0xFFFFF || mask==TOTAL-1){
            // progress occasionally? avoid spam
        }
        if((mask % 200000)==0) { printf("progress %u / %u\n", mask, TOTAL); fflush(stdout); }
    }
    printf("done\n");
    long sum=0; int mn=999,mx=-1;
    for(int i=0;i<129;i++) if(hist[i]){ sum+=hist[i]; if(i<mn)mn=i; if(i>mx)mx=i; }
    printf("sum=%ld mn=%d mx=%d\n", sum, mn, mx);
    printf("histogram (nl:count):\n");
    for(int i=0;i<129;i++) if(hist[i]) printf("%d:%ld\n", i, hist[i]);

    // write CSV
    FILE *f=fopen("output/artifacts/nl_histogram.csv","w");
    fprintf(f,"nl,count\n");
    for(int i=0;i<129;i++) if(hist[i]||1) {
        // only write nonzero? write all 0..64? nl range 0..64 but only even? write nonzero
        if(hist[i]) fprintf(f,"%d,%ld\n",i,hist[i]);
    }
    fclose(f);
    FILE *g2=fopen("output/artifacts/best_per_nl.csv","w");
    fprintf(g2,"nl,count,best_truth_mask,best_anf_mask,best_truth_hex20,degree\n");
    for(int i=0;i<129;i++) if(hist[i]){
        uint32_t tm=(uint32_t)best_truth[i], am=best_anf[i];
        // degree from anf
        int deg=-1;
        if(am==0) deg=-1;
        else { deg=0; for(int j=0;j<G;j++) if((am>>j)&1u) if(orbit_wt[j]>deg) deg=orbit_wt[j]; }
        fprintf(g2,"%d,%ld,%u,%u,0x%05x,%d\n",i,hist[i],tm,am,tm,deg);
    }
    fclose(g2);
    // save row masks + orbits for audit
    FILE *h=fopen("output/artifacts/orbits_and_map.txt","w");
    fprintf(h,"n=7 N=128 G=20\nbit convention: integer v=0..127 with bit i (LSB=x0) = xi; rotation rho(v)=(v>>1)|((v&1)<<6) (right rotate by 1), i.e. (x0..x6)->(x1..x6,x0)\n");
    fprintf(h,"dot product a.x = parity(a&x) with same bit assignment; FWHT with natural binary order computes W(a)=sum_x (-1)^(f(x)+a.x)\n");
    fprintf(h,"orbit order: sorted by minimal element ascending; mask bit k = f value on orbit k (k=0 is {0}, k=19 is {127})\n");
    for(int i=0;i<G;i++) fprintf(h,"orbit %2d min=%3d wt=%d size=%s row_mask=0x%05x\n",i,orbit_min[i],orbit_wt[i],(orbit_min[i]==0||orbit_min[i]==127)?"1":"7",row_mask[i]);
    fprintf(h,"orbit_id[0..127]:\n");
    for(int v=0;v<NN;v++) fprintf(h,"%d%s",orbit_id[v],(v%16==15)?"\n":" ");
    fclose(h);
    // maximizer info
    printf("max nl=%d count=%ld best_truth=%d best_anf=%u\n", mx, hist[mx], best_truth[mx], best_anf[mx]);
    return 0;
}
