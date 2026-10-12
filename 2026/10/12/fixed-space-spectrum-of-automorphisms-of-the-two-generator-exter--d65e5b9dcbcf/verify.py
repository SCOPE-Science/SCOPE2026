from collections import Counter, deque

def inv(a,q): return pow(a,-1,q)

def rank(M,q):
    A=[row[:] for row in M]; m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]%q),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=inv(A[r][c]%q,q)
        A[r]=[(z*x)%q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%q:
                z=A[i][c]%q
                A[i]=[(A[i][j]-z*A[r][j])%q for j in range(n)]
        r+=1
    return r

def automorphisms(q):
    for a in range(q):
      for b in range(q):
       for c in range(q):
        for d in range(q):
         det=(a*d-b*c)%q
         if det==0: continue
         for r in range(q):
          for s in range(q):
           # columns are images of x,y,z on radical basis x,y,z
           yield ((a,c,r),(b,d,s),(0,0,det))

def matvec_cols(cols,v,q):
    return tuple(sum(cols[j][i]*v[j] for j in range(3))%q for i in range(3))

def spectrum(q):
    C=Counter(); autos=[]
    for cols in automorphisms(q):
        # phi-I matrix as rows for rank calculation
        M=[[cols[j][i]-(1 if i==j else 0) for j in range(3)] for i in range(3)]
        drad=3-rank([[x%q for x in row] for row in M],q)
        C[1+drad]+=1
        autos.append(cols)
    return C,autos

def formula(q):
    return {1:q**3*(q+1)*(q-2)**2,
            2:2*q**5-q**4-4*q**3-q**2+q,
            3:(q+1)*(q**2-1),
            4:1}

for q in (3,5,7):
    C,autos=spectrum(q)
    F=formula(q)
    assert {d:C.get(d,0) for d in range(1,5)}==F,(q,C,F)
    total=q**3*(q-1)**2*(q+1)
    assert sum(C.values())==len(autos)==total
    burn=sum(C[d]*(q**d) for d in C)//total
    assert burn==3*q
    print(f'q={q} total={total} spectrum={dict(sorted(C.items()))} burnside_orbits={burn}')

# Direct orbit enumeration for q=3 on all algebra elements (scalar, radical triple).
q=3
C,autos=spectrum(q)
unseen={(c,x,y,z) for c in range(q) for x in range(q) for y in range(q) for z in range(q)}
orbits=[]
while unseen:
    e=next(iter(unseen)); c=e[0]; v=e[1:]
    orb={(c,)+matvec_cols(g,v,q) for g in autos}
    unseen-=orb; orbits.append(orb)
assert len(orbits)==9
sizes=sorted(len(o) for o in orbits)
print('q=3 direct_orbits=9 sizes=',sizes)
print('VERIFY_OK')
