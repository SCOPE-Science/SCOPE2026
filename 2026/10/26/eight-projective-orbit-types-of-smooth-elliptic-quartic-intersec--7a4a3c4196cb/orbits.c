#define main count_main
#include "count.c"
#undef main
static int genmap[4][1024];
static void matrices(int gen, int A[4][4]){memset(A,0,16*sizeof(int));for(int i=0;i<4;i++)A[i][i]=1;if(gen<3){int z=gen;for(int j=0;j<4;j++){int x=A[z][j];A[z][j]=A[z+1][j];A[z+1][j]=x;}}else A[0][1]^=1;}
static int trans(int mask,int A[4][4]){int r=0;for(int i=0;i<4;i++)if(mask&(1<<i))for(int j=0;j<4;j++)if(A[i][j])r^=(1<<j);for(int k=0;k<6;k++)if(mask&(1<<(4+k))){int i=pairidx[k][0],j=pairidx[k][1];for(int x=0;x<4;x++)if(A[i][x]&&A[j][x])r^=(1<<x);for(int m=0;m<6;m++){int x=pairidx[m][0],y=pairidx[m][1];if((A[i][x]&A[j][y])^(A[i][y]&A[j][x]))r^=(1<<(4+m));}}return r;}
static int pf(int a){return (((a>>4)&1)&((a>>9)&1))^(((a>>5)&1)&((a>>8)&1))^(((a>>6)&1)&((a>>7)&1));}
static int qzeros(int q){int n=0;for(int x=1;x<16;x++){int v=0;for(int j=0;j<4;j++)v^=((q>>j)&1)*((x>>j)&1);for(int k=0;k<6;k++)v^=((q>>(4+k))&1)*((x>>pairidx[k][0])&1)*((x>>pairidx[k][1])&1);if(v==0)n++;}return n;}
static int cmp(const void *aa,const void *bb){int a=*(int*)aa,b=*(int*)bb;return (a>b)-(a<b);}
static int code(int a,int b){int c=a^b; if(a>b){int q=a;a=b;b=q;}if(b>c){int q=b;b=c;c=q;}if(a>b){int q=a;a=b;b=q;}return (a<<10)|b;}
static int npoints(int a,int b){int n=0;for(int x=1;x<16;x++){int vs[2]={0,0};for(int m=0;m<2;m++){int q=m?b:a;for(int j=0;j<4;j++)vs[m]^=((q>>j)&1)*((x>>j)&1);for(int k=0;k<6;k++)vs[m]^=((q>>(4+k))&1)*((x>>pairidx[k][0])&1)*((x>>pairidx[k][1])&1);}if(!vs[0]&&!vs[1])n++;}return n;}
int main(){int genA[4][4];for(int g=0;g<4;g++){matrices(g,genA);for(int m=0;m<1024;m++)genmap[g][m]=trans(m,genA);}uint8_t *smoothset=calloc(1024*1024,1),*vis=calloc(1024*1024,1);int *queue=malloc(sizeof(int)*180000);int total=0,orbits=0;
  for(int a=1;a<1024;a++)for(int b=a+1;b<1024;b++)if((a^b)>b && smooth(a,b)){smoothset[code(a,b)]=1;total++;}
  printf("smooth total %d\n",total);
  for(int a=1;a<1024;a++)for(int b=a+1;b<1024;b++)if((a^b)>b && smoothset[code(a,b)] && !vis[code(a,b)]){
    int front=0,end=1;queue[0]=code(a,b);vis[queue[0]]=1;while(front<end){int id=queue[front++],x=id>>10,y=id&1023;for(int g=0;g<4;g++){int newc=code(genmap[g][x],genmap[g][y]);if(!smoothset[newc]){printf("NOT SMOOTH under gen %d %d -> %d %d (original %d %d)\n",g,newc,newc>>10,newc&1023,x,y);return 2;}if(!vis[newc]){vis[newc]=1;queue[end++]=newc;}}}
    printf("orbit %d size %d points %d rep (%d,%d,%d) quadric_pts (%d,%d,%d) pf (%d,%d,%d) stab=%d\n",++orbits,end,npoints(a,b),a,b,a^b,qzeros(a),qzeros(b),qzeros(a^b),pf(a),pf(b),pf(a^b),20160/end);
  }
  printf("orbits %d\n",orbits);free(queue);free(vis);free(smoothset);return 0;
}
