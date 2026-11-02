#!/usr/bin/env python3
"""Independent factor-profile enumeration for ternary Cantor substitution lengths."""

def cant(k):
    s = '1'
    for _ in range(k):
        s = ''.join('101' if x == '1' else '000' for x in s)
    return s

def pos(j):
    out, place = 0, 1
    while j:
        out += (j % 2) * 2 * place
        j //= 2
        place *= 3
    return out

def predicted(k):
    n, B = 3**k, 2**k
    all_profiles = {(0, 0)}
    overlap = 0
    P = 0
    for t in range(1, B+1):
        a = pos(t-1) + 1
        b = pos(t) if t < B else n
        X = {t * (m-t)-P for m in range(a, b+1)}
        Y = {t * (n-m)+P for m in range(a, b+1)}
        all_profiles.update((t, q) for q in X|Y)
        overlap += len(X&Y)
        if t < B: P += pos(t)-t
    return all_profiles, overlap

def direct_profiles(s,n):
    f=s[:n];ones=0;zeros=0;p01=0
    for c in f:
        if c=='1':ones+=1;p01+=zeros
        else:zeros+=1
    result={(ones,p01)}
    for i in range(len(s)-n):
        x=int(s[i]);y=int(s[i+n]);
        if x==0:p01-=ones
        ones-=x
        if y==1:p01+=n-1-ones
        ones+=y
        result.add((ones,p01))
    return result

def verify():
    counts=[]
    for k in range(1,8):
        s = cant(k+2)
        pred, ov = predicted(k)
        direct = direct_profiles(s,3**k)
        assert pred==direct,(k,len(pred),len(direct),pred^direct)
        assert len(pred)==2*3**k+1-ov
        counts.append(len(pred))
    assert counts == [5,17,50,154,466,1402,4210],counts
    for k in range(3,8):
        C=cant(k);n=3**k;h=2**(k-2);q=3**(k-2);t=3*h
        a,b=7*q,8*q;F=sum(pos(j) for j in range(t))
        P=F-t*(t-1)//2
        assert (2*P)%t==0
        S=n+t+(2*P)//t
        assert S==46*q//3
        distinct_profiles=set()
        for m in range(22*q//3,8*q+1):
            m2=S-m
            assert a<=m<=b and a<=m2<=b
            A=C[n-m:]+'0'*(n-m)
            B='0'*(n-m2)+C[:m2]
            assert A!=B
            def value(v):
                z=0;p=0
                for x in v:
                    if x=='0':z+=1
                    else:p+=z
                return v.count('1'),p
            va,vb=value(A),value(B)
            assert va==vb and va[0]==t
            assert va not in distinct_profiles
            distinct_profiles.add(va)
        assert len(distinct_profiles)==2*3**(k-3)+1
    print('PASS: all ternary-length profiles k=1..7; exact overlap sum; linear nonidentical collision families k=3..7')
    print('Profile cardinalities:',counts)
if __name__=='__main__':verify()
