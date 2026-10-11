// Exact finite-field certificate for principal Fourier minors of order 15 in characteristic 7.
// C++17, standard library only. No floating point, probabilistic tests, or external input.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
constexpr int P=7, Q=2401, N=15;
using Coeff = array<int,4>;
Coeff unpack(int u) {Coeff a{};for(int i=0;i<4;i++){a[i]=u%P;u/=P;}return a;}
int pack(const Coeff& a) {return a[0]+P*a[1]+P*P*a[2]+P*P*P*a[3];}
int residue(int x) {x%=P;return x<0?x+P:x;}
int product(int a,int b,const Coeff& c) {
    const auto u=unpack(a),v=unpack(b);int w[7]={};
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)w[i+j]+=u[i]*v[j];
    for(int i=6;i>=4;i--){int t=residue(w[i]);
        for(int j=0;j<4;j++)w[i-4+j]-=t*c[j];}
    Coeff out{};for(int i=0;i<4;i++)out[i]=residue(w[i]);return pack(out);
}
int subtract(int a,int b){auto u=unpack(a),v=unpack(b);Coeff w{};
    for(int i=0;i<4;i++)w[i]=residue(u[i]-v[i]);
    return pack(w);
}
void require(bool b,const char* s){if(!b)throw runtime_error(s);}
struct Field {
    vector<uint16_t> mult,inv;array<int,N> roots{};
    Field(Coeff c):mult(Q*Q),inv(Q) {
        for(int a=0;a<Q;a++)for(int b=0;b<Q;b++)mult[a*Q+b]=product(a,b,c);
        roots[0]=1;for(int k=1;k<N;k++)roots[k]=times(roots[k-1],7);
        require(times(roots[14],7)==1,"X^15 is not 1");
        require(roots[3]!=1 && roots[5]!=1,"X is not primitive order 15");
        for(int a=1;a<Q;a++){
            int b=1,t=a,e=Q-2;while(e){if(e&1)b=times(b,t);t=times(t,t);e>>=1;}
            require(times(a,b)==1,"quotient polynomial not irreducible");inv[a]=b;
        }
    }
    int times(int a,int b) const{return mult[a*Q+b];}
    int rank_principal(int mask) const {
        int idx[N],n=0;for(int i=0;i<N;i++)if((mask>>i)&1)idx[n++]=i;
        int a[N][N]{};for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i][j]=roots[(idx[i]*idx[j])%N];
        int rank=0;
        for(int col=0;col<n && rank<n;col++){
            int pivot=rank;while(pivot<n && a[pivot][col]==0)pivot++;
            if(pivot==n)continue;
            if(pivot!=rank)for(int j=col;j<n;j++)swap(a[pivot][j],a[rank][j]);
            int reciprocal=inv[a[rank][col]];
            for(int row=rank+1;row<n;row++)if(a[row][col]){
                int factor=times(a[row][col],reciprocal);a[row][col]=0;
                for(int j=col+1;j<n;j++)a[row][j]=subtract(a[row][j],times(factor,a[rank][j]));
            }
            rank++;
        }
        return rank;
    }
};
int translate_mask(int mask,int step){
    int b=0;
    for(int k=0;k<N;k++) {
        if((mask>>k)&1)b|=1<<((k+step)%N);
    }
    return b;
}
int main(){
    // The two monic irreducible quartics in Phi_15(X) modulo 7:
    // X^4+2X^3+4X^2+X+2 and X^4+4X^3+2X^2+X+4.
    const Coeff factors[2]={Coeff{2,1,4,2},Coeff{4,1,2,4}};
    constexpr int ALL=(1<<N)-1;
    // S={0,2,3,6,7,9}; its 15 translates and their complements.
    int seed=0;for(int a:{0,2,3,6,7,9})seed|=1<<a;
    vector<int> expected(1<<N,0);
    for(int t=0;t<N;t++){
        int a=translate_mask(seed,t);
        require(!expected[a] && !expected[ALL^a],"duplicated orbit member");
        expected[a]=1;expected[ALL^a]=1;
    }
    for(int orbit=0;orbit<2;orbit++){
        Field f(factors[orbit]);int defects=0,six=0,nine=0,normal=0,rank_defects=0;
        for(int mask=1;mask<=ALL;mask++){
            int n=__builtin_popcount((unsigned)mask);
            int rank=f.rank_principal(mask);
            bool singular=rank<n;
            require(singular==bool(expected[mask]),"classification failed");
            if(singular){
                defects++;rank_defects+=(n-rank);
                require(rank==n-1,"higher-dimensional singular kernel");
                if(n==6)six++;else if(n==9)nine++;else require(false,"bad singular size");
            }else normal++;
        }
        require(defects==30 && six==15 && nine==15 && normal==32737 && rank_defects==30,"wrong counts");
        cout<<"root_orbit="<<orbit<<" nonzero_principal=32737 singular_six=15 singular_nine=15 "
            <<"nullity_one=30 total=32767 PASS\n";
    }
    cout<<"VERIFY_OK\n";
}
