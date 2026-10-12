#!/usr/bin/env python3
def delta(w):
    return "".join("01" if c=="0" else "00" for c in w)

def pd_prefix(N):
    w="0"
    while len(w)<N:
        w=delta(w)
    return w[:N]

def rotations(w):
    return {w[i:]+w[:i] for i in range(len(w))}

def canon(w):
    return min(rotations(w))

def lie_classes(F,n):
    out=set()
    for w in F:
        R=rotations(w)
        if R.issubset(F):
            out.add(min(R))
    return out

def expected_classes(n):
    # Returns canonical representatives predicted by the theorem.
    # n=2^k or 3*2^k.
    m=n
    k=0
    while m%2==0:
        m//=2; k+=1
    if m==1:
        a,b="0","1"
    elif m==3:
        a,b="000","001"
    else:
        return set()
    for _ in range(k):
        a,b=delta(a),delta(b)
    return {canon(a),canon(b)}

N=1<<15
d=pd_prefix(N)
d2=pd_prefix(1<<14)

# Structural identities used in the proof.
assert all(d[i]=="0" for i in range(0,len(d),2))
assert "11" not in d
assert "0000" not in d

# Factor sets from two long prefixes stabilize for the entire checked range.
# This is finite regression evidence only, not the infinite proof.
for n in range(1,65):
    F={d[i:i+n] for i in range(len(d)-n+1)}
    G={d2[i:i+n] for i in range(len(d2)-n+1)}
    assert F==G, ("factor-set-not-stable",n,len(F),len(G))
    C=lie_classes(F,n)
    E=expected_classes(n)
    assert C==E, ("lie-classes",n,C,E)
    assert len(C)==(2 if ((n & (n-1))==0 or ((n//3)>0 and n%3==0 and ((n//3)&((n//3)-1))==0)) else 0)

# Explicit base classes.
F1={d[i:i+1] for i in range(len(d))}
F3={d[i:i+3] for i in range(len(d)-2)}
assert lie_classes(F1,1)=={"0","1"}
assert lie_classes(F3,3)=={"000","001"}

# Directly check the doubling bijection on all classes in a substantial range.
for m in range(1,33):
    Fm={d[i:i+m] for i in range(len(d)-m+1)}
    F2={d[i:i+2*m] for i in range(len(d)-2*m+1)}
    C1=lie_classes(Fm,m)
    C2=lie_classes(F2,2*m)
    image={canon(delta(w)) for w in C1}
    assert image==C2, ("doubling",m,C1,C2,image)

print(
    "VERIFY_OK "
    "prefix=2^15 "
    "factor_sets_stable_n<=64 "
    "exact_classes_n<=64 "
    "doubling_bijection_m<=32 "
    "bases_n=1,3 "
    "no_11_no_0000"
)
