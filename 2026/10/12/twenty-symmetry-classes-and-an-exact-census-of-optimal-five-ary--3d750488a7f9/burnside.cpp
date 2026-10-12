#include <bits/stdc++.h>
using namespace std;
int main(){vector<array<unsigned char,52>> colors;ifstream f("colorings.bin",ios::binary);unsigned char bytes[13];
 while(f.read((char*)bytes,13)){array<unsigned char,52> x;for(int i=0;i<13;i++)for(int j=0;j<4;j++)x[4*i+j]=(bytes[i]>>(2*j))&3;colors.push_back(x);}
 assert(colors.size()==80640);
 ifstream cl("conjugacy_reps.txt");long long fixedsum=0;int gn=0;
 while(cl){int ct,per[52];cl>>ct;if(!cl)break;for(int i=0;i<52;i++)cl>>per[i];
  int fixed=0;
  for(auto &x:colors){unsigned char y[52],ch[4];for(int j=0;j<52;j++)y[per[j]]=x[j];for(int j=0;j<4;j++)ch[y[j]]=j;
   bool eq=true;for(int j=0;j<52;j++)if(ch[y[j]]!=x[j]){eq=false;break;}
   fixed+=eq;
  }
  cout<<"class_size="<<ct<<" fixed_normalized="<<fixed<<" contrib="<<(long long)ct*fixed<<"\n";
  fixedsum+=(long long)ct*fixed;gn++;
 }
 cout<<"BURNSIDE_SUM="<<fixedsum<<" group_order=5616 orbit_count="<<fixedsum/5616<<"\n";
 assert(gn==12 && fixedsum==5616*20);
}
