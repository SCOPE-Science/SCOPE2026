#define main oldmain
#include "quadric_p4.cpp"
#undef main
int bil(int a,int b){return (((a>>0&1)&&(b>>1&1))^((a>>1&1)&&(b>>0&1))^((a>>2&1)&&(b>>3&1))^((a>>3&1)&&(b>>2&1)));}
int q0(int x){return ((x>>0&1)&&(x>>1&1))^((x>>2&1)&&(x>>3&1))^(x>>4&1);}
int action(int q,const array<int,5>& v){int c[5];for(int i=0;i<5;i++)c[i]=qeval(q,v[i]);int out=0;for(int i=0;i<5;i++)out|=c[i]<<i;for(int k=0;k<10;k++){int i=E[k][0],j=E[k][1];int x=qeval(q,v[i]^v[j])^c[i]^c[j];out|=x<<(5+k);}return out;}
int main(){for(int k=0;k<10;k++)edge[E[k][0]][E[k][1]]=edge[E[k][1]][E[k][0]]=k;
int fixed=(1<<4)|(1<<5)|(1<<12);vector<int> good;for(int m=1;m<32768;m++){int r=radical(m);if(!r||!qeval(m,r))continue;smooth[m]=1;good.push_back(m);}
if(!smooth[fixed])abort();vector<array<int,5>> sympl; vector<int> v;for(int x=1;x<32;x++)if(q0(x)==0)v.push_back(x);
for(int a:v)for(int b:v)if(bil(a,b)==1)for(int c:v)if(!bil(a,c)&&!bil(b,c))for(int d:v)if(!bil(a,d)&&!bil(b,d)&&bil(c,d)==1){array<int,5> t={a,b,c,d,16};if(action(fixed,t)!=fixed)abort();sympl.push_back(t);}
cout<<"orthogonal_group "<<sympl.size()<<" fixed="<<fixed<<"\n";
set<int> goodP;for(int m:good)if(smooth[m^fixed] && m<(m^fixed))goodP.insert(m);
cout<<"pencils_through_fixed "<<goodP.size()<<"\n";
vector<int> reps;int ix=0;while(!goodP.empty()){int m=*goodP.begin();auto d=delta(fixed,m);int typ=mod_poly(d,7)==0;int seen=0;for(auto &L:sympl){int m2=action(m,L);m2=min(m2,m2^fixed);if(goodP.erase(m2))seen++;}cout<<"orbit "<<(++ix)<<" rep="<<m<<" size="<<seen<<" type="<<(typ?"2+3":"5")<<" delta="<<int(d)<<"\n"; reps.push_back(m);} 
}
