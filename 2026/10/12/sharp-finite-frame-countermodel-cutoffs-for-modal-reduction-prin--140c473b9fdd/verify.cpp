#include <cstdio>
#include <vector>
#include <numeric>
#include <cstdint>
using namespace std;
using U=unsigned long long;
int main(){ unsigned long long frames=0,serialframes=0,cases=0; for(int n=1;n<=4;n++){bool all[7][13],allSerial[7][13];for(int m=1;m<=6;m++)for(int k=1;k<=12;k++)all[m][k]=allSerial[m][k]=true;
 for(int g=0;g<(1<<(n*n));g++){frames++;vector<U> rows(n);for(int i=0;i<n;i++)for(int j=0;j<n;j++) if(g&(1<<(i*n+j)))rows[i]|=U(1)<<j; bool serial=true;for(U r:rows)serial&=(r!=0);if(serial)serialframes++;
 vector<vector<U>> power(19,vector<U>(n));for(int i=0;i<n;i++)power[0][i]=U(1)<<i;for(int t=1;t<=18;t++)for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(power[t-1][i]&(U(1)<<j))power[t][i]|=rows[j];
 for(int m=1;m<=6;m++)for(int k=1;k<=12;k++){bool good=true;for(int i=0;i<n;i++)if(power[m][i]&~power[m+k][i])good=false;all[m][k]&=good;if(serial)allSerial[m][k]&=good;cases++;}}
 int L=1;for(int d=2;d<=n;d++)L=L/std::gcd(L,d)*d;
 for(int m=1;m<=6;m++)for(int k=1;k<=12;k++){bool pred=(m>=n && k%L==0);bool preds=(m>=n-1 && k%L==0);if(pred!=all[m][k]||preds!=allSerial[m][k]){printf("FAIL n=%d m=%d k=%d all=%d pred=%d serial=%d preds=%d\n",n,m,k,all[m][k],pred,allSerial[m][k],preds);return 1;}}}
 printf("VERIFY_OK frames=%llu serial=%llu graph_parameter_tests=%llu families=4; m=1..6 k=1..12\n",frames,serialframes,cases);}
