#include <bits/stdc++.h>
using namespace std;
struct S { int n,m,D; vector<pair<int,int>> cells; uint64_t pairbit[60][60]; uint64_t target; long long tested=0; vector<int> chosen,solution; bool found=false;
 int index(int dx,int dy) {if(dx<0 ||(dx==0 && dy<0)){dx=-dx;dy=-dy;} if(dx==0) return dy-1; return m+(dx-1)*(2*m+1)+(dy+m);}
 void setup(int nn,int mm) {n=nn;m=mm;D=2*n*m+n+m;target=(1ULL<<D)-1;cells={{0,0},{0,m},{n,0},{n,m}};
  for(int x=0;x<=n;++x)for(int y=0;y<=m;++y)if(!((x==0||x==n)&&(y==0||y==m))) cells.push_back({x,y});
  for(int i=0;i<(int)cells.size();i++)for(int j=i+1;j<(int)cells.size();j++){int dx=cells[j].first-cells[i].first,dy=cells[j].second-cells[i].second;pairbit[i][j]=1ULL<<index(dx,dy);}
 }
 bool rec(int cursor,int remaining,uint64_t cover){ if(found) return true; if(!remaining){tested++;if(cover==target){solution=chosen;found=true;return true;}return false;}
 if((int)cells.size()-cursor<remaining) return false;
 // pairs with currently selected and future remaining, upper count pruning
 int k=chosen.size(); int left=D-__builtin_popcountll(cover);
 if(left>remaining*k+remaining*(remaining-1)/2) return false;
 for(int i=cursor;i<=(int)cells.size()-remaining;++i){
  uint64_t c=cover;for(int j:chosen){int a=min(i,j),b=max(i,j);c|=pairbit[a][b];}
  chosen.push_back(i);if(rec(i+1,remaining-1,c)) return true;chosen.pop_back();
 }return false; }
 void run(int k){tested=0;found=false;chosen={0,1,2,3};solution={};uint64_t cover=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)cover|=pairbit[i][j];auto start=chrono::steady_clock::now();rec(4,k-4,cover);cerr<<"grid="<<n<<"x"<<m<<" marks="<<k<<" tested="<<tested<<" found="<<found<<" secs="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";if(found){cout<<"n="<<n<<" k="<<k<<" solution=";for(int i:solution)cout<<"("<<cells[i].first<<","<<cells[i].second<<")";cout<<"\n";}}
};
int main(int argc,char**argv){int up=argc>1?atoi(argv[1]):5; if(up!=5){cerr<<"Use ./verify 5 for the complete certified census\n";return 2;} const int expected[6][6]={{0},{0,4,5,6,7,8},{0,0,7,8,9,10},{0,0,0,9,11,12},{0,0,0,0,12,13},{0,0,0,0,0,15}}; int cases=0;for(int n=1;n<=up;n++)for(int m=n;m<=up;m++){S s;s.setup(n,m);int lower=1;while(lower*(lower-1)/2<s.D)lower++;for(int k=max(4,lower);k<=(n+1)*(m+1);k++){s.run(k);if(s.found){if(k!=expected[n][m]){cerr<<"MISMATCH grid="<<n<<"x"<<m<<" found="<<k<<" expected="<<expected[n][m]<<"\n";return 1;}cases++;break;}}}if(cases!=15)return 1;cout<<"VERIFY_OK rectangles=15 max_span=5 M2(6,6)=15\n";}
