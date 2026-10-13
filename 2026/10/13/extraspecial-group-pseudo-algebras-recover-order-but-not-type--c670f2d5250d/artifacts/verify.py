def pseudo(p,n):
    assert p >= 2 and n >= 1
    return {1:1, p:p**(2*n)-1, p**(n+1):p-1}

def recover(C):
    nontrivial=sorted(d for d in C if d>1)
    p=nontrivial[0]
    top=nontrivial[-1]
    z=top
    exponent=0
    while z%p==0:
        z//=p
        exponent+=1
    assert z==1
    n=exponent-1
    return p,n,p**(1+2*n)

for p in (2,3,5,7):
    for n in range(1,5):
        C=pseudo(p,n)
        assert sum(C.values())==p**(2*n)+p-1
        assert p**(2*n)+(p-1)*(p**n)**2==p**(1+2*n)
        assert recover(C)==(p,n,p**(1+2*n))
        print({"p":p,"n":n,"order":p**(1+2*n),
               "pseudo_algebra":dict(sorted(C.items()))})

assert pseudo(2,1)=={1:1,2:3,4:1}
assert pseudo(3,1)=={1:1,3:8,9:2}
print("VERIFY_OK")
