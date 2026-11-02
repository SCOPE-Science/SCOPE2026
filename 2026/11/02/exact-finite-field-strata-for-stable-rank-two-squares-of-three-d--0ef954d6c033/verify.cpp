#include<bits/stdc++.h>
using namespace std;
struct V{int x[3];}; int q,M[8][8],A[8][8];
int mul(int x,int y){return M[x][y];} int add(int x,int y){return A[x][y];} int neg(int x){for(int j=0;j<q;j++)if(add(x,j)==0)return j;return -1;}
int sub(int x,int y){return add(x,neg(y));}
int det2(V u,V v){for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if(sub(mul(u.x[i],v.x[j]),mul(u.x[j],v.x[i]))!=0)return 1;return 0;}
int det3(V u,V v,V w){int z=0;for(int i=0;i<3;i++)z=add(z,mul(u.x[i],sub(mul(v.x[(i+1)%3],w.x[(i+2)%3]),mul(v.x[(i+2)%3],w.x[(i+1)%3]))));return z!=0;}
V scale_add(V u,int a,V v,int b){V z;for(int j=0;j<3;j++)z.x[j]=add(mul(a,u.x[j]),mul(b,v.x[j]));return z;}
V mult(V u,V v,V aa,V bb,V cc){V z;for(int j=0;j<3;j++){z.x[j]=0;z.x[j]=add(z.x[j],mul(mul(u.x[0],v.x[0]),aa.x[j]));z.x[j]=add(z.x[j],mul(mul(u.x[1],v.x[1]),bb.x[j]));z.x[j]=add(z.x[j],mul(mul(u.x[2],v.x[2]),cc.x[j]));}return z;}
int iszero(V x){return x.x[0]==0&&x.x[1]==0&&x.x[2]==0;}
int main(int argc,char**argv){q=atoi(argv[1]);for(int i=0;i<q;i++)for(int j=0;j<q;j++){
 if(q==4){A[i][j]=i^j;int z=0;for(int a=0;a<2;a++)for(int b=0;b<2;b++)if((i>>a&1)&&(j>>b&1))z ^= (1<<(a+b)); if(z&4)z^=7;M[i][j]=z;}
 else {A[i][j]=(i+j)%q;M[i][j]=(i*j)%q;}}
 vector<V> vs;for(int i=0;i<q*q*q;i++){int a=i;V z;for(int k=0;k<3;k++){z.x[k]=a%q;a/=q;}vs.push_back(z);}vector<pair<int,int>> lines;for(int j=0;j<q;j++)lines.push_back({1,j});lines.push_back({0,1});
 long long ranktwo=0,stable=0,split=0,doub=0,irred=0;
 for(V aa:vs)for(V bb:vs)for(V cc:vs){if(det3(aa,bb,cc))continue;V u,v;if(det2(aa,bb)){u=aa;v=bb;}else if(det2(aa,cc)){u=aa;v=cc;}else if(det2(bb,cc)){u=bb;v=cc;}else continue;ranktwo++;
 V uu=mult(u,u,aa,bb,cc),uv=mult(u,v,aa,bb,cc),vv=mult(v,v,aa,bb,cc);if(!(det2(uu,uv)||det2(uu,vv)||det2(uv,vv)))continue;stable++;
 vector<V> l;for(auto [a,b]:lines)l.push_back(scale_add(u,a,v,b));bool found=false;for(int i=0;i<(int)l.size()&&!found;i++)for(int j=i+1;j<(int)l.size()&&!found;j++)if(iszero(mult(l[i],l[j],aa,bb,cc)))found=true;
 if(found){split++;continue;}for(V t:l)if(iszero(mult(t,t,aa,bb,cc))){found=true;break;}if(found)doub++;else irred++;
 }
 long long gl=(long long)(q*q-1)*(q*q-q);long long ps=((long long)(q-1)*(q-1)*q*(q+1)/2+3LL*q*q*q)*gl;long long pd=(long long)(q-1)*(q-1)*(q+1)*gl;long long pi=((long long)(q-1)*(q-1)*q*(q-1)/2)*gl;
 cout<<"q="<<q<<" rank2="<<ranktwo<<" stable="<<stable<<" split="<<split<<" double="<<doub<<" irreducible="<<irred<<" predicted="<<ps<<","<<pd<<","<<pi<<" "<<(split==ps&&doub==pd&&irred==pi?"VERIFY_OK":"FAIL")<<"\n";
}
