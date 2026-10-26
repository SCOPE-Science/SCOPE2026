// Independent exact symmetric-matrix pencil census in dimension four over F3.
#include <iostream>
#include <array>
using namespace std;
int mod3(int z){z%=3;return z<0?z+3:z;}
int main(){
  const int pairs[10][2]={{0,0},{1,1},{2,2},{3,3},{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
  int perm[24][4];int signs[24];int np=0;
  for(int a=0;a<4;a++)for(int b=0;b<4;b++)if(b!=a)
  for(int c=0;c<4;c++)if(c!=a&&c!=b)
  for(int d=0;d<4;d++)if(d!=a&&d!=b&&d!=c){
    int p[4]={a,b,c,d};int inv=0;
    for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(p[i]>p[j])inv++;
    for(int i=0;i<4;i++)perm[np][i]=p[i];
    signs[np++]=inv%2?-1:1;
  }
  if(np!=24)return 2;
  long long form_count[3]={0,0,0};
  for(int code=0;code<59049;code++){
    int v=code,a[4][4]={{0}};
    for(int k=0;k<10;k++){
      int t=v%3;v/=3;
      a[pairs[k][0]][pairs[k][1]]=a[pairs[k][1]][pairs[k][0]]=t;
    }
    int det=0;
    for(int ip=0;ip<24;ip++){
      int factor=signs[ip];
      for(int i=0;i<4;i++)factor*=a[i][perm[ip][i]];
      det=mod3(det+factor);
    }
    form_count[det]++;
  }
  cout<<"F3 nonsingular symmetric 4x4 matrices by determinant squareclass: "
      <<form_count[1]<<" (square), "<<form_count[2]<<" (nonsquare)\n";
  if(form_count[1]!=21060||form_count[2]!=16848)return 5;
  long long good_second[3]={0,0,0};
  for(int last=1;last<=2;last++){
    long long good=0,rootfree=0;
    const int s[4]={1,1,1,last};
    for(int code=0;code<59049;code++){
      int v=code,a[4][4]={{0}};
      for(int k=0;k<10;k++){
        int t=v%3;v/=3;
        a[pairs[k][0]][pairs[k][1]]=a[pairs[k][1]][pairs[k][0]]=t;
      }
      // monic determinant polynomial f(T)=det(T I - B0^{-1} B1).
      // Since B0 is diagonal, B0^{-1}=B0 and entries are mod-3.
      int coeff[5]={0};
      for(int ip=0;ip<24;ip++){
        int pol[5]={1,0,0,0,0},degree=0;
        for(int i=0;i<4;i++){
          int j=perm[ip][i], w=mod3(-s[i]*a[i][j]);
          int diag=(i==j);
          int next[5]={0};
          for(int z=0;z<=degree;z++){
            next[z]=mod3(next[z]+w*pol[z]);
            if(diag)next[z+1]=mod3(next[z+1]+pol[z]);
          }
          degree+=diag;
          for(int z=0;z<5;z++)pol[z]=next[z];
        }
        for(int z=0;z<5;z++)coeff[z]=mod3(coeff[z]+signs[ip]*pol[z]);
      }
      if(coeff[4]!=1){cerr<<"nonmonic\n";return 3;}
      bool roots=false;
      for(int t=0;t<3;t++){
        int value=0;
        for(int z=4;z>=0;z--)value=mod3(value*t+coeff[z]);
        if(value==0)roots=true;
      }
      if(roots)continue;
      rootfree++;
      // Root-free quartic is nonsquarefree iff it equals square of one of
      // the three irreducible monic quadratics over F3.
      bool bad=false;
      for(int b=0;b<3;b++)for(int c=0;c<3;c++){
        bool qroot=false;
        for(int t=0;t<3;t++)if(mod3(t*t+b*t+c)==0)qroot=true;
        if(qroot)continue;
        int sq[5]={mod3(c*c),mod3(2*b*c),mod3(b*b+2*c),mod3(2*b),1};
        bool same=true;
        for(int z=0;z<5;z++)if(sq[z]!=coeff[z])same=false;
        if(same)bad=true;
      }
      if(!bad)good++;
    }
    cout<<"F3 4x4 diag(1,1,1,"<<last<<") rootfree="<<rootfree
        <<" separable="<<good<<" expected="<<(last==1?12096:15120)<<"\n";
    if(good!=(last==1?12096:15120))return 4;
    good_second[last]=good;
  }
  long long ordered=form_count[1]*good_second[1]+form_count[2]*good_second[2];
  if(ordered!=509483520||ordered/48!=10614240||ordered%48!=0)return 6;
  cout<<"F3 4x4: ordered_valid_pairs="<<ordered
      <<" unordered_pencils="<<ordered/48<<"\n";
  cout<<"INDEPENDENT_MATRIX_CENSUS_PASS\n";
}
