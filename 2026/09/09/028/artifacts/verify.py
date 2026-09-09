"""Independent verifier for the d4 non-lift certificate.
Recomputes d4(n) = coeffs of (q^2;q^2)^4/(q;q)^13 from scratch by an
independent code path (series inverse via schoolbook long division on
directly multiplied products), checks generating-function identity,
then checks every witness in witness_table.json and the headline claims.
Usage: python3 output/artifacts/verify.py  (stdlib only, ~60-120s)
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
SER = os.path.join(HERE, "d4_series.json")
WIT = os.path.join(HERE, "witness_table.json")

def products(N):
    A=[1]*(N+1); A=[0]*(N+1); A[0]=1
    for k in range(1,N+1):
        for n in range(N,k-1,-1):
            A[n]-=A[n-k]
    B=[0]*(N+1); B[0]=1
    for k in range(1,N//2+1):
        kk=2*k
        for n in range(N,kk-1,-1):
            B[n]-=B[n-kk]
    return A,B

def mul(X,Y,N):
    Z=[0]*(N+1)
    for i,a in enumerate(X):
        if a:
            for j in range(N-i+1):
                if Y[j]: Z[i+j]+=a*Y[j]
    return Z

def main():
    W=json.load(open(WIT)); N=W["N"]
    NV=min(N,1000)  # witnesses all have n<=970, so N=1000 suffices for headline
    A,B=products(NV)
    B2=mul(B,B,NV); B4=mul(B2,B2,NV)
    A2=mul(A,A,NV); A4=mul(A2,A2,NV); A8=mul(A4,A4,NV)
    A12=mul(A8,A4,NV); P=mul(A12,A,NV)
    D=[0]*(NV+1)
    for n in range(NV+1):
        s=B4[n]
        for j in range(1,n+1):
            s-=P[j]*D[n-j]
        D[n]=s
    # identity check
    assert mul(D,P,NV)==B4, "generating-function identity FAILED"
    # spot values
    assert D[:5]==[1,13,100,585,2862], f"spot values FAILED: {D[:5]}"
    # check stored series agreement on overlap
    S=json.load(open(SER))["d4"]
    assert S[:NV+1]==D, "stored series mismatch"
    # check every witness row
    bad=0
    for row in W["rows"]:
        r,n,v,m=row["B"],row["n"],row["d4"],row["mod49"]
        if D[n]%49==0 or D[n]!=v or (D[n]%49)!=m:
            print("WITNESS FAIL",row,"recomputed",D[n]); bad+=1
    assert bad==0, f"{bad} witness rows failed"
    # headline: no 343-class vanishes mod49; none of {39,235,284} lifts
    for r in range(343):
        assert any(D[n]%49!=0 for n in range(r,NV+1,343)), r
    # no 49-class vanishes mod7
    for r in range(49):
        assert any(D[n]%7!=0 for n in range(r,NV+1,49)), r
    print(f"VERIFY_OK N={NV} rows={len(W['rows'])} identity=D*P=B4 spot=D[:5]={D[:5]}")
if __name__=="__main__":
    main()
