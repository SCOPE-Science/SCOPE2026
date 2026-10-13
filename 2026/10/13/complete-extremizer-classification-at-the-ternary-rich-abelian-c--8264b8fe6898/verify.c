#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

#define MAXN 181
#define NSOL 4

static unsigned char w[MAXN];
static int pref[3][MAXN+1];
static unsigned long long cnt[MAXN+1];
static char sol[NSOL][MAXN+1];
static int nsol=0;

static const char *expected[NSOL] = {
"001001210010012100100122122100122122100100121001001210110121011012100100121001001221221001221221001001210010012101101210110121001001210010012212210012212210010012100100121011012101",
"001221001001210010012212210012212210010012100100121011012101101210010012100100122122100122122100100121001001210110121011012100100121001001221221001221221001001210010012101101210110",
"010201001020110110201101102202201102202201101102011011020100102010010201101102011011022022011022022011011020110110201001020100102011011020110110220220110220220110110201101102011011",
"011012101101210010012100100122122100122122100100121001001210110121011012100100121001001221221001221221001001210010012101101210110121001001210010012212210012212210010012100100122100"
};

static inline int pal_suffix(int n, int L){
    int s=n-L;
    for(int i=0;i<L/2;i++) if(w[s+i]!=w[n-1-i]) return 0;
    return 1;
}

/* Assuming the prefix of length n-1 is rich, Theorem 2.1's
   unioccurrent-palindromic-suffix criterion reduces richness after one
   extension to uniqueness of the longest palindromic suffix. */
static inline int rich_extension_ok(int n){
    int L;
    for(L=n;L>=1;--L) if(pal_suffix(n,L)) break;
    int s=n-L;
    for(int j=0;j<s;j++){
        int k=0;
        for(;k<L;k++) if(w[j+k]!=w[s+k]) break;
        if(k==L) return 0;
    }
    return 1;
}

/* Assuming the prefix of length n-1 is abelian-cube-free, every newly
   created forbidden factor must end at n.  Test all possible block lengths. */
static inline int abelian_cube_extension_ok(int n){
    for(int m=1;3*m<=n;m++){
        int s=n-3*m;
        int same=1;
        for(int a=0;a<3;a++){
            int c1=pref[a][s+m]-pref[a][s];
            int c2=pref[a][s+2*m]-pref[a][s+m];
            int c3=pref[a][s+3*m]-pref[a][s+2*m];
            if(c1!=c2 || c1!=c3){ same=0; break; }
        }
        if(same) return 0;
    }
    return 1;
}

static void dfs(int n,int max_seen){
    cnt[n]++;
    if(n==180 && nsol<NSOL){
        for(int i=0;i<n;i++) sol[nsol][i]=(char)('0'+w[i]);
        sol[nsol][n]='\0';
        nsol++;
    }
    if(n==MAXN) return;

    /* Restricted-growth strings: one representative of every orbit under
       alphabet permutation, including words using fewer than three symbols. */
    int lim = max_seen<2 ? max_seen+1 : 2;
    for(int ch=0; ch<=lim; ch++){
        w[n]=(unsigned char)ch;
        for(int a=0;a<3;a++) pref[a][n+1]=pref[a][n]+(a==ch);
        if(!rich_extension_ok(n+1)) continue;
        if(!abelian_cube_extension_ok(n+1)) continue;
        dfs(n+1, ch>max_seen?ch:max_seen);
    }
}

static int direct_rich(const char *s,int n){
    /* Count distinct palindromes including the empty word by explicit comparison.
       Only used on the four final words, so cubic work is harmless. */
    int cap=n*n+1, np=1;
    char **pals=(char**)calloc((size_t)cap,sizeof(char*));
    if(!pals) return 0;
    pals[0]=(char*)malloc(1);
    if(!pals[0]){free(pals); return 0;}
    pals[0][0]='\0';
    for(int i=0;i<n;i++){
        for(int j=i+1;j<=n;j++){
            int L=j-i, ok=1;
            for(int k=0;k<L/2;k++) if(s[i+k]!=s[j-1-k]) {ok=0;break;}
            if(!ok) continue;
            int seen=0;
            for(int q=0;q<np;q++){
                if((int)strlen(pals[q])==L && memcmp(pals[q],s+i,(size_t)L)==0){seen=1;break;}
            }
            if(!seen){
                pals[np]=(char*)malloc((size_t)L+1);
                memcpy(pals[np],s+i,(size_t)L); pals[np][L]='\0'; np++;
            }
        }
    }
    for(int q=0;q<np;q++) free(pals[q]);
    free(pals);
    return np==n+1;
}

static int direct_ab3_free(const char *s,int n){
    int pc[3][MAXN+1]={{0}};
    for(int i=0;i<n;i++){
        for(int a=0;a<3;a++) pc[a][i+1]=pc[a][i]+(s[i]-'0'==a);
    }
    for(int i=0;i<n;i++){
        for(int m=1;i+3*m<=n;m++){
            int same=1;
            for(int a=0;a<3;a++){
                int c1=pc[a][i+m]-pc[a][i];
                int c2=pc[a][i+2*m]-pc[a][i+m];
                int c3=pc[a][i+3*m]-pc[a][i+2*m];
                if(c1!=c2 || c1!=c3){same=0;break;}
            }
            if(same) return 0;
        }
    }
    return 1;
}

static void canon_reverse(const char *s,char *out){
    int map[3]={-1,-1,-1}, next=0;
    for(int i=0;i<180;i++){
        int c=s[179-i]-'0';
        if(map[c]<0) map[c]=next++;
        out[i]=(char)('0'+map[c]);
    }
    out[180]='\0';
}

int main(void){
    memset(pref,0,sizeof(pref));
    memset(cnt,0,sizeof(cnt));
    w[0]=0; pref[0][1]=1;
    if(rich_extension_ok(1) && abelian_cube_extension_ok(1)) dfs(1,0);

    if(cnt[180]!=4 || cnt[181]!=0 || nsol!=4){
        fprintf(stderr,"bad census %llu %llu %d\n",cnt[180],cnt[181],nsol);
        return 2;
    }
    for(int i=0;i<NSOL;i++){
        if(strcmp(sol[i],expected[i])!=0){fprintf(stderr,"solution mismatch %d\n",i);return 3;}
        if(!direct_rich(sol[i],180)){fprintf(stderr,"direct richness fail %d\n",i);return 4;}
        if(!direct_ab3_free(sol[i],180)){fprintf(stderr,"direct cube check fail %d\n",i);return 5;}
    }
    int pair[4]={2,3,0,1};
    for(int i=0;i<4;i++){
        char cr[181]; canon_reverse(sol[i],cr);
        if(strcmp(cr,sol[pair[i]])!=0){fprintf(stderr,"reverse pairing fail %d\n",i);return 6;}
    }

    printf("VERIFY_OK canonical180=4 canonical181=0 labeled180=24 perm_orbits=4 perm_reversal_orbits=2 reverse_pairs=1-3,2-4 direct_checks=4\n");
    return 0;
}
