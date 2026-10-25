#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define N 9765625
#define K 10
int g[5][K][K];uint8_t *marked;uint32_t *queue;
int inv5[5]={0,1,3,2,4};
uint32_t apply(uint32_t m,int k){int coeff[K],out[K]={0};for(int i=0;i<K;i++){coeff[i]=m%5;m/=5;}for(int i=0;i<K;i++)for(int j=0;j<K;j++)out[i]+=g[k][i][j]*coeff[j];int first=0;uint32_t n=0,base=1;for(int i=0;i<K;i++)out[i]%=5;for(int i=0;i<K;i++)if(out[i]){first=out[i];break;}for(int i=0;i<K;i++){n+=((out[i]*inv5[first])%5)*base;base*=5;}return n;}
int main(){FILE *fp=fopen("generators.txt","r");for(int k=0;k<5;k++)for(int i=0;i<K;i++)for(int j=0;j<K;j++)if(fscanf(fp,"%d",&g[k][i][j])!=1)return 3;fclose(fp);
 marked=calloc(N,1);queue=malloc(4*N);fp=fopen("maximizers.bin","rb");uint32_t m;int n=0;while(fread(&m,4,1,fp)==1){marked[m]=1;n++;}fclose(fp);printf("maximizers %d\n",n);
 int orbits=0;fp=fopen("maximizers.bin","rb");while(fread(&m,4,1,fp)==1){if(marked[m]!=1)continue;int lo=0,hi=0;queue[hi++]=m;marked[m]=2;
 while(lo<hi){uint32_t key=queue[lo++];for(int k=0;k<5;k++){uint32_t b=apply(key,k);if(marked[b]==0){printf("ERROR orbit moves outside maximum %u => %u\n",key,b);return 2;}if(marked[b]==1){marked[b]=2;queue[hi++]=b;}}}
 printf("orbit %d: seed_index %u size %d stabilizer %d coeff:",++orbits,m,hi,372000/hi);uint32_t w=m;for(int j=0;j<10;j++){printf(" %d",w%5);w/=5;}printf("\n");}
 fclose(fp);printf("orbits %d\n",orbits);
 return 0;
}
