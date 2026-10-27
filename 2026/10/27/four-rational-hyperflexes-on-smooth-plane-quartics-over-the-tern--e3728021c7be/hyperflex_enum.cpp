#include <bits/stdc++.h>
using namespace std;
using vec=array<uint8_t,15>;
int main(){
 ifstream in("hyperflex_flags.json");string s((istreambuf_iterator<char>(in)),{});
 auto start=s.find("\"flags\"");s=s.substr(start);
 vector<array<array<int,15>,4>> rows;vector<array<int,15>> transverse;
 for(size_t pos=0;;){
  pos=s.find("\"rows\"",pos);if(pos==string::npos)break;
  auto parse=[&](size_t& pos,int n){vector<int> v;while(pos<s.size()&&v.size()<(size_t)n){if(isdigit(s[pos]))v.push_back(s[pos]-'0');pos++;}return v;};
  pos=s.find('[',pos); auto v=parse(pos,60);array<array<int,15>,4> r{};
  for(int i=0;i<4;++i)for(int j=0;j<15;++j)r[i][j]=v[i*15+j];rows.push_back(r);
  pos=s.find("\"transverse\"",pos);pos=s.find('[',pos);auto t=parse(pos,15);array<int,15> x{};for(int j=0;j<15;++j)x[j]=t[j];transverse.push_back(x);
 }
 cerr<<"flags="<<rows.size()<<"\n";
 const int N=14348907;
 vector<uint8_t> count(N,0);
 int pow3[16];pow3[0]=1;for(int i=1;i<=15;i++)pow3[i]=pow3[i-1]*3;
 long long pair_count=0;int wrong=0;
 for(int fi=0;fi<(int)rows.size();fi++){
  auto a=rows[fi];vector<int> piv;int rank=0;
  for(int col=0;col<15&&rank<4;col++){
   int rr=-1;for(int k=rank;k<4;k++)if(a[k][col]){rr=k;break;}
   if(rr<0)continue;
   swap(a[rank],a[rr]);if(a[rank][col]==2)for(int k=0;k<15;k++)a[rank][k]=2*a[rank][k]%3;
   for(int k=0;k<4;k++)if(k!=rank&&a[k][col]){int c=a[k][col];for(int j=0;j<15;j++)a[k][j]=(a[k][j]+3-c*a[rank][j]%3)%3;}
   piv.push_back(col);rank++;
  }
  if(rank!=4){cerr<<"rank bad "<<fi<<" "<<rank<<"\n";return 1;}
  vector<int> freecols;for(int j=0;j<15;j++)if(find(piv.begin(),piv.end(),j)==piv.end())freecols.push_back(j);
  array<vec,11> basis{};
  for(int k=0;k<11;k++){
   basis[k][freecols[k]]=1;
   for(int i=0;i<4;i++)basis[k][piv[i]]=(3-a[i][freecols[k]])%3;
  }
  vec v{};int digits[11]={};
  int maxnum=177147;
  for(int z=0;z<maxnum;z++){
   if(z){for(int j=0;j<11;j++){
    int d=digits[j];digits[j]=(d+1)%3;
    for(int k=0;k<15;k++)v[k]=(v[k]+basis[j][k])%3;
    if(d!=2)break;
   }}
   int first=-1;for(int k=0;k<15;k++)if(v[k]){first=k;break;}
   if(first<0||v[first]!=1)continue;
   int t=0;for(int k=0;k<15;k++)t+=v[k]*transverse[fi][k];
   if(t%3==0)continue;
   int idx=0;for(int k=0;k<15;k++)idx+=v[k]*pow3[k];
   if(count[idx]==255){wrong++;continue;}count[idx]++;pair_count++;
  }
 }
 cerr<<"hyperflex incidences "<<pair_count<<" wrong "<<wrong<<"\n";
 int maxval=0;long long hist[53]={};vector<int> maximizers;
 for(int i=0;i<N;i++)if(count[i]){hist[count[i]]++;if(count[i]>maxval){maxval=count[i];maximizers={i};}else if(count[i]==maxval)maximizers.push_back(i);}
 cout<<"all hyperflex eligible counts max "<<maxval<<"\n";
 for(int i=0;i<=maxval;i++)if(hist[i])cout<<i<<":"<<hist[i]<<" ";cout<<"\n";
 cerr<<"writing candidates...\n";
 FILE* f=fopen("hyperflex_counts.bin","wb");fwrite(count.data(),1,count.size(),f);fclose(f);
 for(int i=1;i<=maxval;i++){
  vector<int> rowsel;for(int j=0;j<N;j++)if(count[j]==i)rowsel.push_back(j);
  if(i>=4){ofstream f2("hyperflex_count_"+to_string(i)+".txt");for(int z:rowsel)f2<<z<<"\n";}
  cout<<"count="<<i<<" forms="<<rowsel.size()<<" sample="<<(rowsel.size()?rowsel[0]:0)<<"\n";
 }
}
