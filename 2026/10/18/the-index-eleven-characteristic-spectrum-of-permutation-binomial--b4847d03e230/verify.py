"""Exact certificate for index-eleven permutation-binomial characteristics.
Run with Python 3: python verify.py. No third-party packages.
"""
from collections import defaultdict
from math import comb


def wendt11():
    # Resultant of f=X^11-1 and g=(X+1)^11-1, via Sylvester/Bareiss.
    f=[-1]+[0]*10+[1]
    g=[comb(11,k) for k in range(12)]
    g[0]-=1
    n=11
    mat=[]
    for i in range(n):
        mat.append([0]*i+list(reversed(f))+[0]*(n-1-i))
    for i in range(n):
        mat.append([0]*i+list(reversed(g))+[0]*(n-1-i))
    d=1
    sign=1
    for k in range(2*n-1):
        if mat[k][k]==0:
            loc=next((j for j in range(k+1,2*n) if mat[j][k]),None)
            assert loc is not None
            mat[k],mat[loc]=mat[loc],mat[k]
            sign=-sign
        pivot=mat[k][k]
        for i in range(k+1,2*n):
            for j in range(k+1,2*n):
                v=mat[i][j]*pivot-mat[i][k]*mat[k][j]
                assert v%d==0
                mat[i][j]=v//d
            mat[i][k]=0
        d=pivot
    return sign*mat[-1][-1]


def pk(p, kmax=22):
    # P1=1, P{k+1}=[(X-k)(Y-1)-k*T*Y] Pk+T*Y*(Y-1)*partial_Y Pk
    tau=-pow(11,-1,p)%p
    pol={(0,0):1}
    out={1:pol}
    for k in range(1,kmax):
        tmp=defaultdict(int)
        for (i,j),v in pol.items():
            tmp[i+1,j+1]+=v
            tmp[i+1,j]-=v
            tmp[i,j+1]-=k*(1+tau)*v
            tmp[i,j]+=k*v
            tmp[i,j+1]+=tau*j*v
            tmp[i,j]-=tau*j*v
        pol={ij:v%p for ij,v in tmp.items() if v%p}
        out[k+1]=pol
    return out


def eval_poly(poly,x,z,p):
    return sum(v*pow(x,i,p)*pow(z,j,p) for (i,j),v in poly.items())%p


def main():
    W=wendt11()
    assert abs(W)==23**5*67**2*89*199**2
    assert all(n%k for n in (23,67,89,199) for k in range(2,int(n**.5)+1))
    expected={
      67:{9:[27,34],15:[50,57],25:[19],59:[65]},
      89:{2:[43],45:[65]},
      199:{61:[69,180],62:[48,159],63:[],139:[]}
    }
    for p,rootmap in expected.items():
        Q=pk(p)
        zs=[z for z in range(1,p) if z!=1 and pow(z,11,p)==1 and pow(z-1,11,p) in (1,p-1)]
        assert zs==sorted(rootmap)
        total=0
        for z in zs:
            us=[u for u in range(p) if eval_poly(Q[11],u,z,p)==0]
            assert us==rootmap[z],(p,z,us)
            for u in us:
                for c in (0,1):
                    v=(2*u+(1-c)*pow(11,-1,p))%p
                    residue=eval_poly(Q[22],v,z,p)
                    assert residue!=0,(p,z,u,c,v)
                    total+=1
        print('ELIMINATED',p,'zeta_candidates',len(zs),'joint_cases',total)
    f=[(pow(x,12,23)+2*x)%23 for x in range(23)]
    assert len(set(f))==23
    print('RESULTANT',abs(W))
    print('WITNESS F23',f)
    print('CERTIFICATE_OK')

if __name__=='__main__':main()
