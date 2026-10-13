from fractions import Fraction

def table(limit):
    spf=list(range(limit+1))
    for p in range(2,int(limit**.5)+1):
        if spf[p]==p:
            for j in range(p*p,limit+1,p):
                if spf[j]==j: spf[j]=p
    beta=[0]*(limit+1); omega=[0]*(limit+1); beta[1]=1
    for n in range(2,limit+1):
        p=spf[n]; a=0; u=n
        while u%p==0: u//=p; a+=1
        beta[n]=beta[u]*((p**(a+1)+(-1)**a)//(p+1))
        omega[n]=omega[u]+a
    return beta,omega

def main():
    bound=1000000
    beta,omega=table(bound+1)
    assert beta[194]==beta[195]==96
    hits=[n for n in range(2,bound+1,4) if omega[n+1]<=3 and beta[n]==beta[n+1]]
    assert hits==[194],hits
    assert Fraction(8,15)>Fraction(1,2)
    assert Fraction(4,5)*Fraction(6,7)*Fraction(10,11)>Fraction(1,2)
    assert Fraction(2,3)*Fraction(6,7)*Fraction(10,11)>Fraction(1,2)
    assert Fraction(2,3)*Fraction(4,5)*Fraction(16,17)>Fraction(1,2)
    assert [(15*r-1)//2 for r in [7,11,13]]==[52,82,97]
    print('EXACT_REGRESSION_OK hits=[194] scanned=2..1000000 residue=2mod4')

if __name__=='__main__':main()
