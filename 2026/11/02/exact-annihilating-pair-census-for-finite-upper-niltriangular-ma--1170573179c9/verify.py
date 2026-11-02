from itertools import product

def formula(q,n):
    state={0:1}
    for k in range(2,n+1):
        out={}
        for r in range(k):
            val=(q**(k-1)*state.get(r,0))
            if r>0: val+=q**(k-r)*(q**(k-1)-q**(r-1))*state.get(r-1,0)
            out[r]=val
        state=out
    return sum(state.values())

def brute(q,n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    mats=list(product(range(q),repeat=len(pairs)))
    def idxmat(x):
        a=[[0]*n for _ in range(n)]
        for (i,j),v in zip(pairs,x): a[i][j]=v
        return a
    dense=[idxmat(x) for x in mats]
    count=0
    for a in dense:
        for b in dense:
            if all(sum(a[i][k]*b[k][j] for k in range(i+1,j))%q==0 for i,j in pairs): count+=1
    return count

for q,n in [(2,2),(3,2),(2,3),(3,3),(2,4)]:
    a=formula(q,n);b=brute(q,n)
    print(q,n,a,b,'PASS' if a==b else 'FAIL')
    assert a==b
print('VERIFY_OK')
