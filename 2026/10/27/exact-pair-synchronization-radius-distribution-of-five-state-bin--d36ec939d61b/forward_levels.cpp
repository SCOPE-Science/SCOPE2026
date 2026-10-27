#include <array>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <cstdint>
using namespace std;
static int id[5][5];
int main(){
 int cnt=0; for(int a=0;a<5;a++)for(int b=a+1;b<5;b++) id[a][b]=id[b][a]=cnt++;
 array<unsigned long long,12> hist{}; array<unsigned long long,12> ext{};
 int representatives[12]{}; unsigned long long sync=0;
 int maxr=-1; array<int,10> exA{}; array<int,10> exPair{};
 for(int ai=0;ai<3125;ai++){
  int A[5]; for(int i=0,t=ai;i<5;i++,t/=5)A[i]=t%5;
  for(int bi=0;bi<3125;bi++){
    int B[5]; for(int i=0,t=bi;i<5;i++,t/=5)B[i]=t%5;
    int succ[10][2];int k=0;
    for(int u=0;u<5;u++)for(int v=u+1;v<5;v++){
      succ[k][0]=(A[u]==A[v]?-1:id[A[u]][A[v]]);
      succ[k][1]=(B[u]==B[v]?-1:id[B[u]][B[v]]); k++;
    }
    int d[10]; for(int x=0;x<10;x++)d[x]=-1;
    for(int x=0;x<10;x++)if(succ[x][0]==-1||succ[x][1]==-1)d[x]=1;
    int changed=1;
    for(int t=2;t<=10&&changed;t++){
      changed=0;
      for(int x=0;x<10;x++)if(d[x]==-1){for(int c=0;c<2;c++){int y=succ[x][c];if(y>=0&&d[y]!=-1&&d[y]<t){d[x]=t;changed=1;break;}}}
    }
    int R=0;for(int x=0;x<10;x++){if(d[x]<0){R=-1;break;}R=max(R,d[x]);}
    if(R>=0){hist[R]++;sync++;if(R>maxr){maxr=R;for(int j=0;j<5;j++){exA[j]=A[j];exA[j+5]=B[j];}for(int j=0;j<10;j++)exPair[j]=d[j];}}
   }
 }
 cout<<"TOTAL "<<3125ULL*3125<<" SYNC "<<sync<<" NON "<<3125ULL*3125-sync<<" MAX "<<maxr<<"\n";
 for(int j=1;j<=10;j++)cout<<j<<" "<<hist[j]<<"\n";
 cout<<"REP a=";for(int i=0;i<5;i++)cout<<exA[i]<<",";cout<<" b=";for(int i=5;i<10;i++)cout<<exA[i]<<",";cout<<"\nPAIR D:";for(int i=0;i<10;i++)cout<<exPair[i]<<",";cout<<"\n";
}
