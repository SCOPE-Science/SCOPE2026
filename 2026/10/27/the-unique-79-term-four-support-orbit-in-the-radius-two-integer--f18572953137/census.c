/* Exhaustive four-support positive-circuit enumeration in the integer cube.
   Compile: cc -O2 -std=c99 -Wall -Wextra census.c -o census
   Run: ./census extremizers.tsv
   All arithmetic is exact in signed 32-bit int for m=2. */
#include <stdio.h>
#include <stdlib.h>
#define M 2
#define SIDE (2*M+1)
#define N (SIDE*SIDE*SIDE)
static int vertex[N][3];
static int gcd2(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b != 0) {int t=a%b; a=b; b=t;}
    return a;
}
static int det3(const int *a, const int *b, const int *c) {
    return a[0]*(b[1]*c[2]-b[2]*c[1])
         - a[1]*(b[0]*c[2]-b[2]*c[0])
         + a[2]*(b[0]*c[1]-b[1]*c[0]);
}
static int relation(int a, int b, int c, int d, int out[4]) {
    int r[4]={det3(vertex[b],vertex[c],vertex[d]),
             -det3(vertex[a],vertex[c],vertex[d]),
              det3(vertex[a],vertex[b],vertex[d]),
             -det3(vertex[a],vertex[b],vertex[c])};
    for (int i=0;i<4;i++) if (!r[i]) return 0;
    int sign=(r[0]<0) ? -1:1;
    for (int i=1;i<4;i++) if (sign*r[i]<=0) return 0;
    int g=gcd2(gcd2(r[0],r[1]),gcd2(r[2],r[3]));
    int length=0;
    for (int i=0;i<4;i++){out[i]=sign*r[i]/g; length+=out[i];}
    return length;
}
int main(int argc, char **argv) {
    if (argc!=2) {fprintf(stderr,"Usage: census extremizers.tsv\n"); return 2;}
    for (int x=-M,h=0;x<=M;x++) for(int y=-M;y<=M;y++)
        for(int z=-M;z<=M;z++,h++) {
            vertex[h][0]=x;vertex[h][1]=y;vertex[h][2]=z;
        }
    long long combinations=0, positives=0;
    int maxlen=0, maxcount=0;
    for (int a=0;a<N;a++) for(int b=a+1;b<N;b++)
      for(int c=b+1;c<N;c++) for(int d=c+1;d<N;d++) {
        int m[4], length=relation(a,b,c,d,m);
        combinations++;
        if (!length) continue;
        positives++;
        if (length>maxlen) {maxlen=length;maxcount=1;}
        else if (length==maxlen) maxcount++;
      }
    if (combinations!=9691375LL || positives!=779864LL || maxlen!=79 || maxcount!=48){
       fprintf(stderr,"Unexpected exhaustive totals.\n"); return 3;
    }
    FILE *f=fopen(argv[1],"wb");
    if (!f){perror("fopen"); return 4;}
    fputs("a\tb\tc\td\tn_a\tn_b\tn_c\tn_d\n", f);
    int wrote=0;
    for (int a=0;a<N;a++) for(int b=a+1;b<N;b++)
      for(int c=b+1;c<N;c++) for(int d=c+1;d<N;d++) {
        int mult[4], length=relation(a,b,c,d,mult);
        if (length!=maxlen)continue;
        fprintf(f,"%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n",a,b,c,d,mult[0],mult[1],mult[2],mult[3]);
        wrote++;
      }
    if (fclose(f)!=0 || wrote!=48) {fprintf(stderr,"Census write failed.\n");return 5;}
    printf("CENSUS_OK vertices=%d combinations=%lld positive_circuits=%lld max_length=%d maximizers=%d\n",N,combinations,positives,maxlen,maxcount);
    return 0;
}
