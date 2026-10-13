#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
U forbid[27][27];int hist[28]={}; vector<vector<int>> maxsets;uint64_t cnt=0;
bool des(int z,int x,int y){for(int j=0;j<3;j++){if(z%3!=x%3&&z%3!=y%3)return false;z/=3;x/=3;y/=3;}return true;}
void recur(U avail,U chosen){cnt++;
 if (!avail){} // avail for ascending only; check maximal globally
 U can=~chosen&((1u<<27)-1);for(int i=0;i<27;i++)if(chosen>>i&1)for(int j=i+1;j<27;j++)if(chosen>>j&1)can &=~forbid[i][j];
 if(!can){int n=__builtin_popcount(chosen);hist[n]++;vector<int> ss;for(int v=0;v<27;v++)if(chosen>>v&1)ss.push_back(v);maxsets.push_back(ss);}
 while(avail){int v=__builtin_ctz(avail);avail&=avail-1;
 U rem=avail;
 for(int i=0;i<27;i++)if(chosen>>i&1)rem&=~forbid[i][v];
 recur(rem,chosen|(1u<<v));
 }
}
int main(){
 for(int a=0;a<27;a++)for(int b=a+1;b<27;b++)for(int c=0;c<27;c++)
  if(c!=a&&c!=b&&(des(a,b,c)||des(b,a,c)||des(c,a,b)))forbid[a][b]|=1u<<c;
 recur((1u<<27)-1,0);
 int expected[28]={};expected[3]=27;expected[4]=162;expected[5]=540;
 expected[6]=27;expected[7]=324;expected[9]=12;
 for(int i=0;i<28;i++)assert(hist[i]==expected[i]);
 assert(cnt==14584);assert(maxsets.size()==1092);
 vector<pair<int,U>> canon;
 for (const auto& c:maxsets){ U m=0;for(int v:c){int u=9*(v%3)+3*((v/3)%3)+((v/9)%3);m|=1u<<u;}canon.emplace_back((int)c.size(),m); }
 sort(canon.begin(),canon.end());
 ofstream out("maximal_codes_cpp.txt");
 for(auto [n,m]:canon){out<<n<<":";bool first=true;
  for(int u=0;u<27;u++)if(m>>u&1){
   if(!first)out<<",";first=false;
   out<<char('0'+u/9)<<char('0'+(u/3)%3)<<char('0'+u%3);
  }out<<"\n";
 }
 out.close();
 cout<<"VERIFICATION_OK: "<<cnt<<" feasible codes, "<<maxsets.size()<<" maximal codes\n";
 for(int i=0;i<28;i++)if(hist[i])cout<<i<<":"<<hist[i]<<" ";cout<<"\n";
}
