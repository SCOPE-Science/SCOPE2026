// Exact enumeration of left-right crossing for 4x2 bond percolation.
// Vertices: (x,y), 0<=x<=4, 0<=y<=2. vid = y*5+x (15 vertices).
// Edges: 22 total.
//   horizontal: for y in 0..2, x in 0..3: ((x,y),(x+1,y)) -> index y*4+x (0..11)
//   vertical:   for x in 0..4, y in 0..1: ((x,y),(x,y+1)) -> index 12 + y*5+x (12..21)
// Enumerate all 2^22 subsets (each equally likely at p=1/2), BFS from left side,
// check reaching right side. Exact integer count.
#include <stdio.h>
#include <stdint.h>

#define NV 15
#define NE 22
#define NCONF (1u<<22)  // 4194304

static int eu[NE], ev[NE];

int main(void){
    int k=0;
    for(int y=0;y<3;y++) for(int x=0;x<4;x++){
        int a=y*5+x, b=y*5+(x+1);
        eu[k]=a; ev[k]=b; k++;
    }
    for(int x=0;x<5;x++) for(int y=0;y<2;y++){
        // keep deterministic order: x outer to match doc? we said 12+y*5+x
        int a=y*5+x, b=(y+1)*5+x;
        eu[12+y*5+x]=a; ev[12+y*5+x]=b;
    }
    // adjacency: for each vertex list of (neighbor, edge)
    long long count=0;
    // BFS buffers
    int q[NV], seen[NV];
    for(uint32_t mask=0; mask<NCONF; mask++){
        for(int i=0;i<NV;i++) seen[i]=0;
        int qh=0, qt=0;
        // left side vertices: (0,y) -> vid y*5+0
        for(int y=0;y<3;y++){ int v=y*5; if(!seen[v]){seen[v]=1; q[qt++]=v;} }
        int reached=0;
        while(qh<qt){
            int v=q[qh++];
            int vx=v%5, vy=v/5;
            if(vx==4){ reached=1; break; }
            // neighbors: left/right via horizontal edges, up/down via vertical
            // right: edge (vx,vy)-(vx+1,vy) exists if vx<4: index vy*4+vx
            // left:  edge (vx-1,vy)-(vx,vy) if vx>0: index vy*4+(vx-1)
            // up:    edge (vx,vy)-(vx,vy+1) if vy<2: index 12+vy*5+vx
            // down:  edge (vx,vy-1)-(vx,vy) if vy>0: index 12+(vy-1)*5+vx
            int e, w;
            if(vx<4){ e=vy*4+vx; if(mask&(1u<<e)){ w=v+1; if(!seen[w]){seen[w]=1;q[qt++]=w;} } }
            if(vx>0){ e=vy*4+(vx-1); if(mask&(1u<<e)){ w=v-1; if(!seen[w]){seen[w]=1;q[qt++]=w;} } }
            if(vy<2){ e=12+vy*5+vx; if(mask&(1u<<e)){ w=v+5; if(!seen[w]){seen[w]=1;q[qt++]=w;} } }
            if(vy>0){ e=12+(vy-1)*5+vx; if(mask&(1u<<e)){ w=v-5; if(!seen[w]){seen[w]=1;q[qt++]=w;} } }
        }
        if(reached) count++;
    }
    printf("count=%lld total=%u\n", count, NCONF);
    // reduce fraction
    long long tot=NCONF;
    printf("prob=%.10f\n", (double)count/(double)tot);
    return 0;
}
