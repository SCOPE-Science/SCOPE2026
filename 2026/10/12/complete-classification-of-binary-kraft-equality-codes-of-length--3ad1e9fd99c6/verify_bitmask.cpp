#include <bits/stdc++.h>
using namespace std;
// Binary words length 3 (0..7) and length 4 (0..15). State ID for residual r of length l is (1<<l)-2 + r.
static int sid(int l,int x){return (1<<l)-2+x;}
static int maskpop(int x){return __builtin_popcount((unsigned)x);}
static unsigned short trans3[14][8], trans4[14][16];
static long long counts[8][4]; // [a][0 UD finite,1 UD infinite,2 not UD,3 prefix]
static long long depth[8][16];
static int maxdepth=0;

static unsigned short edge[14], visited, running;
static bool dfs_cycle(int v){
  int m=1<<v;
  if(running & m) return true;
  if(visited & m) return false;
  running |= m;
  unsigned t=edge[v];
  while(t){int w=__builtin_ctz(t);t&=t-1; if(dfs_cycle(w))return true;}
  running ^= m; visited|=m;return false;
}
static int height(int v, int *memo){
  if(memo[v]>=0) return memo[v];
  int t=edge[v],h=1;
  while(t){int w=__builtin_ctz((unsigned)t);t&=t-1;h=max(h,1+height(w,memo));}
  return memo[v]=h;
}
int main(){
  for(int l=1;l<=3;l++)for(int x=0;x<(1<<l);x++){
    int r=sid(l,x);
    for(int y=0;y<8;y++)if(l<3 && (y>>(3-l))==x)trans3[r][y]=1<<sid(3-l,y&((1<<(3-l))-1));
    for(int y=0;y<16;y++)if((y>>(4-l))==x)trans4[r][y]=1<<sid(4-l,y&((1<<(4-l))-1));
  }
  for(int m3=1;m3<255;m3++){
    int a=maskpop(m3), b=16-2*a;
    if(b<=0 || b>=16) continue;
    for(int m4=0;m4<65536;m4++){
      if(maskpop(m4)!=b) continue;

      int ini=0;
      for(int y=0;y<16;y++)if(m4>>y&1 && m3>>(y>>1)&1)ini|=1<<sid(1,y&1);
      if(ini==0){counts[a][0]++; counts[a][3]++;depth[a][0]++;continue;}
      for(int v=0;v<14;v++){
        unsigned t=0;
        for(int y=0;y<8;y++)if(m3>>y&1)t|=trans3[v][y];
        for(int y=0;y<16;y++)if(m4>>y&1)t|=trans4[v][y];
        edge[v]=t;
      }
      unsigned reached=ini, pending=ini;
      while(pending){int v=__builtin_ctz(pending); pending&=pending-1;
        int add=edge[v]&~reached;
        reached|=add;pending|=add;
      }
      // If any length-3 residual is a codeword, SP confirms ambiguity.
      bool bad= false;
      for(int y=0;y<8;y++)if(m3>>y&1 && (reached>>(sid(3,y))&1)){bad=true;break;}
      if(bad){counts[a][2]++;continue;}
      visited=running=0;bool cyc=false;
      for(int v=0;v<14;v++)if((reached>>v&1)&&!(visited>>v&1))if(dfs_cycle(v)){cyc=true;break;}
      if(cyc){counts[a][1]++;
        bool suffix=true;
        for(int y=0;y<16;y++)if(m4>>y&1 && m3>>(y&7)&1){suffix=false;break;}
        if(!suffix){cout<<"EXCEPTION a="<<a<<" m3="<<m3<<" m4="<<m4<<" short=";
          for(int y=0;y<8;y++)if(m3>>y&1)cout<<bitset<3>(y)<<" ";
          cout<<" long=";for(int y=0;y<16;y++)if(m4>>y&1)cout<<bitset<4>(y)<<" ";cout<<"\n";}
        continue;}
      counts[a][0]++;
      int memo[14];fill(memo,memo+14,-1);int h=0;
      for(int v=0;v<14;v++)if(ini>>v&1)h=max(h,height(v,memo));
      depth[a][h]++;maxdepth=max(maxdepth,h);
    }
  }
  cout<<"a,b,total,finite,infinite,notUD,prefix\n";
  for(int a=1;a<=7;a++){
    cout<<a<<","<<16-2*a<<","<<counts[a][0]+counts[a][1]+counts[a][2]<<","<<counts[a][0]<<","<<counts[a][1]<<","<<counts[a][2]<<","<<counts[a][3]<<"\n";
  }
  if(counts[1][0]!=8 || counts[2][0]!=28 || counts[3][0]!=56 ||
    counts[4][0]!=70 || counts[5][0]!=56 || counts[6][0]!=28 || counts[7][0]!=8)
      {cerr<<"unexpected finite-delay counts"<<endl; return 1;}
  if(counts[1][1]!=8 || counts[2][1]!=28 || counts[3][1]!=56 ||
    counts[4][1]!=70 || counts[5][1]!=60 || counts[6][1]!=28 || counts[7][1]!=8)
      {cerr<<"unexpected infinite-delay counts"<<endl; return 1;}
  cout<<"depth_count (SP steps)\n";
  for(int a=1;a<=7;a++)for(int h=0;h<=maxdepth;h++)if(depth[a][h])cout<<a<<","<<h<<","<<depth[a][h]<<"\n";
}
