// Exact independent additive-convolution census from the finite list of smooth quartic masks.
// Input masks are supplied by the rank enumeration, in the common monomial order:
// X^i Y^j Z^(4-i-j), decreasing i then decreasing j.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
constexpr int N=32768;
void fwht(vector<int64_t>& a){
 for(int w=1;w<N;w*=2)for(int k=0;k<N;k+=2*w)for(int j=0;j<w;j++){
  int64_t p=a[k+j],q=a[k+j+w];a[k+j]=p+q;a[k+j+w]=p-q;
 }
}
int main(){
 vector<uint8_t> is_smooth(N);ifstream in("smooth_form_masks.txt");assert(in);
 int num=0,t;while(in>>t){assert(t>0&&t<N&&!is_smooth[t]);is_smooth[t]=1;num++;}assert(num==10920);
 array<uint16_t,7> point_evaluations{};
 int col=0;
 for(int i=4;i>=0;i--)for(int j=4-i;j>=0;j--){int k=4-i-j;
  for(int pt=1;pt<=7;pt++){
   bool nonzero=(!(i>0&&(pt&1)==0) && !(j>0&&(pt&2)==0) && !(k>0&&(pt&4)==0));
   if(nonzero)point_evaluations[pt-1] ^= uint16_t(1)<<col;
  }
  col++;
 }
 assert(col==15);
 vector<uint8_t> roots(N);
 for(int a=1;a<N;a++)for(int p=0;p<7;p++){
  if((__builtin_popcount(unsigned(a&point_evaluations[p]))&1)==0)roots[a]|=1<<p;
 }
 array<int64_t,8> M{},exact{};
 for(int subset=0;subset<128;subset++){
  vector<int64_t> vals(N);
  for(int a=1;a<N;a++)if(is_smooth[a] && (roots[a]&subset)==subset)vals[a]=1;
  fwht(vals);
  int64_t cube_sum=0;
  for(int k=0;k<N;k++)cube_sum+=vals[k]*vals[k]*vals[k];
  assert(cube_sum%N==0);
  int64_t ordered=cube_sum/N;
  assert(ordered%6==0);
  M[__builtin_popcount(unsigned(subset))] += ordered/6;
 }
 for(int r=7;r>=0;r--){
  int64_t t=M[r];
  for(int s=r+1;s<=7;s++){
   // Compute the binomial coefficient exactly.
   int64_t numer=1;for(int z=0;z<r;z++)numer*=s-z;
   for(int z=2;z<=r;z++)numer/=z;
   t-=numer*exact[s];
  }
  exact[r]=t;
 }
 cout<<"fourier_total_pencils="<<exact[0]+exact[1]+exact[2]+exact[3]+exact[4]+exact[5]+exact[6]+exact[7]<<"\n";
 for(int r=0;r<=7;r++)cout<<"fourier_base_rational "<<r<<" "<<exact[r]<<"\n";
 for(int r=0;r<=7;r++)cout<<"moment "<<r<<" "<<M[r]<<"\n";
}
