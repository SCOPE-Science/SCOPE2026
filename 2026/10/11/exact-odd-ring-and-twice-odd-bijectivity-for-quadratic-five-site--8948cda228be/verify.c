/* Exact finite-state verification for odd-ring and 2-mod-4-ring bijectivity
   of quadratic five-input binary cellular automata. C11, no libraries beyond libc. */
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define V 256
#define NM 65536
static uint32_t basis[16], local_truth[NM];
static unsigned char to[V][4], from[V][4], deg[V], indeg[V];

static void make_basis(void) {
  for (unsigned word = 0; word < 32; ++word) {
    basis[0] |= UINT32_C(1) << word;
    for (int j = 0; j < 5; ++j)
      if ((word >> j) & 1U) basis[1+j] |= UINT32_C(1) << word;
    int z = 6;
    for (int j = 0; j < 5; ++j)
      for (int k = j + 1; k < 5; ++k, ++z)
        if (((word >> j) & 1U) && ((word >> k) & 1U))
          basis[z] |= UINT32_C(1) << word;
  }
  for (unsigned mask = 1; mask < NM; ++mask) {
    int k = __builtin_ctz(mask);
    local_truth[mask] = local_truth[mask & (mask-1)] ^ basis[k];
  }
}

static void make_graph(unsigned mask) {
  uint32_t truth = local_truth[mask];
  memset(deg,0,sizeof(deg)); memset(indeg,0,sizeof(indeg));
  for (int a=0;a<16;++a) for(int b=0;b<16;++b) {
    int u=16*a+b;
    for(int x=0;x<2;++x) for(int y=0;y<2;++y) {
      int pa=a+16*x,pb=b+16*y;
      if (((truth>>pa) & 1U) != ((truth>>pb) & 1U)) continue;
      int v=16*((a>>1)+8*x)+(b>>1)+8*y;
      assert(deg[u]<4 && indeg[v]<4);
      to[u][deg[u]++]=(unsigned char)v;
      from[v][indeg[v]++]=(unsigned char)u;
    }
  }
}

/* First route: Tarjan SCC decomposition and edge-voltage coloring. */
static int dfn[V],low[V],active[V],stack[V],top,tick,nc,component[V],different[V];
static void tarjan(int u) {
  dfn[u]=low[u]=++tick; stack[top++]=u;active[u]=1;
  for(int j=0;j<deg[u];++j){int v=to[u][j];
    if (!dfn[v]) {tarjan(v);if(low[v]<low[u])low[u]=low[v];}
    else if(active[v] && dfn[v]<low[u])low[u]=dfn[v];
  }
  if(low[u]==dfn[u]){int v;do{v=stack[--top];active[v]=0;component[v]=nc;
    if((v>>4)!=(v&15))different[nc]=1;
  }while(v!=u);++nc;}
}
static void method_coloring(int *all_odd,int *all_two) {
  memset(dfn,0,sizeof(dfn)); memset(active,0,sizeof(active));
  memset(different,0,sizeof(different));top=tick=nc=0;
  for(int u=0;u<V;++u)if(!dfn[u])tarjan(u);
  int color[V];for(int u=0;u<V;++u)color[u]=-1;
  *all_odd=*all_two=1;
  for(int u=0;u<V;++u)if(color[u]<0){
    int queue[V],head=0,tail=0;queue[tail++]=u;color[u]=0;
    while(head<tail){int v=queue[head++];
      for(int j=0;j<deg[v];++j){int w=to[v][j];
        if(component[v]!=component[w])continue;
        int expected=(color[v]+1)%4;
        if(color[w]<0){color[w]=expected;queue[tail++]=w;}
        else if(different[component[v]]){
          if((color[w]&1)!=(expected&1))*all_odd=0;
          if(color[w]!=expected)*all_two=0;
        }
      }
    }
  }
}

/* Independent route: Kosaraju SCC decomposition; period = gcd of depth
   discrepancies depth(u)+1-depth(v) over internal edges. */
static int used[V],order[V],len,cc[V],comp_different[V];
static void dfs1(int u) {
  used[u]=1;
  for(int j=0;j<deg[u];++j)if(!used[to[u][j]])dfs1(to[u][j]);
  order[len++]=u;
}
static void dfs2(int u,int id){cc[u]=id;
  if((u>>4)!=(u&15))comp_different[id]=1;
  for(int j=0;j<indeg[u];++j)if(cc[from[u][j]]<0)dfs2(from[u][j],id);
}
static int gcd_int(int a,int b){if(a<0)a=-a;if(b<0)b=-b;
  while(b){int t=a%b;a=b;b=t;}return a;
}
static void method_period(int *all_odd,int *all_two) {
  memset(used,0,sizeof(used));len=0;
  for(int u=0;u<V;++u)if(!used[u])dfs1(u);
  for(int u=0;u<V;++u)cc[u]=-1;
  memset(comp_different,0,sizeof(comp_different));int nc2=0;
  for(int k=len-1;k>=0;--k){int u=order[k];
    if(cc[u]<0)dfs2(u,nc2++);
  }
  int depth[V];for(int u=0;u<V;++u)depth[u]=-1;
  int periods[V];memset(periods,0,sizeof(periods));
  for(int root=0;root<V;++root)if(depth[root]<0){
    int queue[V],head=0,tail=0;queue[tail++]=root;depth[root]=0;
    while(head<tail){int u=queue[head++];
      for(int j=0;j<deg[u];++j){int v=to[u][j];
        if(cc[u]!=cc[v])continue;
        if(depth[v]<0){depth[v]=depth[u]+1;queue[tail++]=v;}
      }
    }
  }
  for(int u=0;u<V;++u)for(int j=0;j<deg[u];++j){int v=to[u][j];
    if(cc[u]==cc[v])periods[cc[u]]=gcd_int(periods[cc[u]],depth[u]+1-depth[v]);
  }
  *all_odd=*all_two=1;
  for(int k=0;k<nc2;++k)if(comp_different[k]){
    if(periods[k]%2)*all_odd=0;
    if(periods[k]%4)*all_two=0;
  }
}

/* Directly enumerate the finite cyclic configurations independently of the
   equal-output pair graph. */
static unsigned seen[1<<15];
static int direct_bijective(unsigned mask,int n,unsigned *stamp){
  unsigned M=(1U<<n),tag=++*stamp;
  uint32_t table=local_truth[mask];
  for(unsigned x=0;x<M;++x){unsigned out=0;
    for(int pos=0;pos<n;++pos){unsigned word=0;
      for(int j=0;j<5;++j){int t=(pos+j-2+n)%n;
        word|=((x>>t)&1U)<<j;
      }
      out|=((table>>word)&1U)<<pos;
    }
    if(seen[out]==tag)return 0;
    seen[out]=tag;
  }
  return 1;
}

static const unsigned base_odd[16]={
  74,76,162,168,1030,1034,1044,1048,
  8204,8212,8232,8240,16394,16418,32792,32808
};
static const unsigned base_two[4]={162,168,16394,16418};
/* Independently confirm that the accepted coefficient masks implement precisely
   the known odd-ring reversible elementary rules on four spacing patterns. */
static unsigned mask_truth(unsigned mask) { return local_truth[mask]; }
static unsigned eca_output(unsigned rule,unsigned word,const int pos[3]) {
  unsigned idx=4*((word>>pos[0])&1U)+2*((word>>pos[1])&1U)+((word>>pos[2])&1U);
  return (rule>>idx)&1U;
}
static void verify_eca_patterns(void){
  static const int pos[4][3]={{0,1,2},{1,2,3},{2,3,4},{0,2,4}};
  static const unsigned eca[8]={45,75,89,101,154,166,180,210};
  unsigned seen_odd[NM]={0},seen_two[NM]={0};
  int count_odd=0,count_two=0;
  for(int s=0;s<4;++s) for(int r=0;r<8;++r){
    unsigned target=0;
    for(unsigned w=0;w<32;++w)target|=eca_output(eca[r],w,pos[s])<<w;
    int found=0;
    for(unsigned mask=0;mask<NM;++mask) if(mask_truth(mask)==target){
      assert((mask&0xffc0U)!=0);
      assert(!seen_odd[mask]);seen_odd[mask]=1;++count_odd;
      if(s==3){assert(!seen_two[mask]);seen_two[mask]=1;++count_two;}
      found=1;break;
    }
    assert(found);
  }
  assert(count_odd==32 && count_two==8);
  for(unsigned mask=0;mask<NM;++mask){
    int expected_odd=0,expected_two=0;
    for(int i=0;i<16;++i) if(mask==base_odd[i] || mask==(base_odd[i]^1U)) expected_odd=1;
    for(int i=0;i<4;++i) if(mask==base_two[i] || mask==(base_two[i]^1U)) expected_two=1;
    assert((unsigned)expected_odd==seen_odd[mask]);
    assert((unsigned)expected_two==seen_two[mask]);
  }
}
static int in_expected(unsigned mask,const unsigned *v,int len){
  for(int i=0;i<len;++i)if(mask==v[i] || mask==(v[i]^1U))return 1;
  return 0;
}
int main(void){make_basis();verify_eca_patterns();unsigned total=0,odd_count=0,two_count=0;
  int sample_n[3]={9,10,15},sample_counts[3]={0,0,0};
  unsigned stamp=0;
  for(unsigned mask=0;mask<NM;++mask){
    if(!(mask & 0xffc0U))continue;  /* at least one quadratic coefficient */
    ++total;make_graph(mask);
    int a,b,c,d;method_coloring(&a,&b);method_period(&c,&d);
    if(a!=c || b!=d){fprintf(stderr,"independent graph mismatch at %u\n",mask);return 2;}
    if(a!=in_expected(mask,base_odd,16) || b!=in_expected(mask,base_two,4)){
      fprintf(stderr,"classification mismatch at %u\n",mask);return 3;
    }
    odd_count+=(unsigned)a;two_count+=(unsigned)b;
    for(int j=0;j<3;++j)sample_counts[j]+=direct_bijective(mask,sample_n[j],&stamp);
  }
  if(total!=65472 || odd_count!=32 || two_count!=8 ||
     sample_counts[0]!=42 || sample_counts[1]!=8 || sample_counts[2]!=32)
    return 4;
  printf("VERIFY_OK: %u exact-degree-two rules; odd=%u; 2mod4=%u; finite counts n9=%d n10=%d n15=%d; two independent graph methods agree.\n",
         total,odd_count,two_count,sample_counts[0],sample_counts[1],sample_counts[2]);
  return 0;
}
