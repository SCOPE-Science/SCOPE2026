from itertools import product

def brute(m,n):
    N=m+n+2;u,v=m+n,m+n+1
    neighbors=[[] for _ in range(N)]
    for i in range(m):neighbors[i].append(u);neighbors[u].append(i)
    for i in range(m,m+n):neighbors[i].append(v);neighbors[v].append(i)
    neighbors[u].append(v);neighbors[v].append(u)
    out=[0,0,0]
    for leaves in product(range(3),repeat=m+n):
      for center in product(range(4),repeat=2):
        c=list(leaves)+list(center)
        # 3 represents uncoloured
        if any(c[x]==c[y]!=3 for x in range(N) for y in neighbors[x]):continue
        initial=sum(x!=3 for x in center)
        while True:
          forced=[]
          for i in range(N):
            if c[i]!=3:continue
            used={c[j] for j in neighbors[i] if c[j]!=3}
            if len(used)==2:forced.append((i,({0,1,2}-used).pop()))
          if not forced:break
          # Simultaneously forced vertices can conflict; sequentially apply one
          i,x=forced[0]
          c[i]=x
        if all(x!=3 for x in c) and all(c[x]!=c[y] for x in range(N) for y in neighbors[x]):out[initial]+=1
    return out
for m in range(1,5):
 for n in range(1,5):
    b=brute(m,n)
    t=[6*(2**(m+n)-2**m-2**n),6*(2**(m+n+1)-2**m-2**n),6*2**(m+n)]
    assert b==t,(m,n,b,t)
    print(f'm={m},n={n}: {b} == {t}')
print('ALL_DOUBLE_STARS_PASS')
