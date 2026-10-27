#include <bits/stdc++.h>
using namespace std;
int main(){
 ifstream fi("hyperflex_actions.json");string s((istreambuf_iterator<char>(fi)),{});vector<int> num;
 for(int i=0;i<(int)s.size();++i)if(isdigit(s[i]))num.push_back(s[i]-'0');
 if(num.size()!=4*15*15)return 1;
 int m[4][15][15];int t=0;for(int g=0;g<4;g++)for(int a=0;a<15;a++)for(int b=0;b<15;b++)m[g][a][b]=num[t++];
 auto act=[&](int F,int g){int c[15]={},o[15]={};for(int i=0;i<15;i++){c[i]=F%3;F/=3;}
 for(int i=0;i<15;i++)if(c[i])for(int j=0;j<15;j++)o[j]=(o[j]+c[i]*m[g][i][j])%3;
 int factor=0;for(int i=0;i<15;i++)if(o[i]){factor=o[i];break;}
 if(factor==2)for(int &v:o)v=(2*v)%3;
 int out=0,k=1;for(int v:o){out+=k*v;k*=3;}return out;
 };
 ifstream f("hyperflex_rsmooth_4.txt");unordered_set<int> remaining;int x;while(f>>x)remaining.insert(x);
 cerr<<"candidates "<<remaining.size()<<"\n";
 vector<pair<int,vector<int>>> orbits;
 while(!remaining.empty()){
  int start=*remaining.begin();vector<int> orb{start};remaining.erase(start);
  for(int i=0;i<(int)orb.size();i++)for(int g=0;g<4;g++){
   int b=act(orb[i],g);
   if(remaining.erase(b))orb.push_back(b);
   else if(find(orb.begin(),orb.end(),b)==orb.end()){
    // if missing in candidate and unseen closure, means either group action code error or flag check error
    static int errors=0;if(errors++<2)cerr<<"unexpected "<<start<<" to "<<b<<"\n";
   }
  }
  sort(orb.begin(),orb.end());orbits.push_back({orb[0],move(orb)});
 }
 sort(orbits.begin(),orbits.end(),[](auto&a,auto&b){return a.second.size()>b.second.size();});
 cout<<"orbits "<<orbits.size()<<"\n";
 ofstream out("hyperflex_orbits.json");out<<"[";
 for(int i=0;i<(int)orbits.size();i++){
  if(i)out<<",";
  out<<"{\"rep\":"<<orbits[i].first<<",\"size\":"<<orbits[i].second.size()<<",\"members\":[";
  for(int j=0;j<(int)orbits[i].second.size();j++){
   if(j)out<<",";out<<orbits[i].second[j];
  }out<<"]}";
  cout<<orbits[i].first<<":"<<orbits[i].second.size()<<" ";
 }
 cout<<"\n";out<<"]";
}
