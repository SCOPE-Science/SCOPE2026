from math import comb,factorial

def multiply(x,y,n):
    out=[]
    for r in x:
      z=0
      for i in range(n):
        if r>>i&1:z|=y[i]
      out.append(z)
    return tuple(out)

def verify(n):
    v=[]
    for a in range(1,1<<n):
      for b in range(1,1<<n):
        if a&b:
          v.append((a,b,tuple(b if a>>i&1 else 0 for i in range(n))))
    assert len({x[2] for x in v})==len(v)
    g=[set() for _ in v]
    for i in range(len(v)):
      for j in range(i+1,len(v)):
        if multiply(v[i][2],v[j][2],n)==multiply(v[j][2],v[i][2],n):
          g[i].add(j);g[j].add(i)
    counted=[1]+[0]*n
    maxcount=[0]*(n+1)
    def rec(prefix,candidates):
      if prefix:
        counted[len(prefix)]+=1
        # Direct maximality check, not just formula.
        maximal=not any(all(j in g[i] for i in prefix) for j in range(len(v)) if j not in prefix)
        cover=0
        for i in prefix:
            cover|=v[i][0]|v[i][1]
        assert maximal==(cover==(1<<n)-1), (n,prefix)
        if maximal:maxcount[len(prefix)]+=1
      for j,i in enumerate(candidates):
        rec(prefix+[i],[l for l in candidates[j+1:] if l in g[i]])
    rec([],list(range(len(v))))
    expected=[sum((-1)**j*comb(k,j)*(2**(k+1)+k-1-j)**n for j in range(k+1))//factorial(k) for k in range(n+1)]
    max_expected=[0]+[sum((-1)**j*comb(k,j)*(2**(k+1)+k-2-j)**n for j in range(k+1))//factorial(k) for k in range(1,n+1)]
    assert counted==expected,(n,counted,expected)
    assert maxcount==max_expected,(n,maxcount,max_expected)
    assert maxcount[-1]==1
    print('VERIFY_N',n,'vertices',len(v),'cliques',counted,'maximal',maxcount)

if __name__=='__main__':
    for n in range(1,5):verify(n)
    print('VERIFY_OK')
