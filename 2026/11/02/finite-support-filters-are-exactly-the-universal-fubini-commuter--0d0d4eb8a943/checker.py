from itertools import product

def filters(n):
    carrier=(1<<n)-1
    sets=range(1<<n)
    for code in range(1<<(1<<n)):
        coll={a for a in sets if (code>>a)&1}
        if 0 in coll or carrier not in coll:continue
        if any(a in coll and any((a&b)==a and b not in coll for b in sets) for a in sets):continue
        if any(a&b not in coll for a in coll for b in coll):continue
        yield frozenset(coll)

def filt_tensor(F,G,n,m,relation):
    leftrows=0
    for i in range(n):
        row=sum(1<<j for j in range(m) if relation>>(i*m+j)&1)
        if row in G: leftrows |= 1<<i
    rightcols=0
    for j in range(m):
        col=sum(1<<i for i in range(n) if relation>>(i*m+j)&1)
        if col in F:rightcols |= 1<<j
    return leftrows in F,rightcols in G

def main():
    q=0; pairs=0;fcounts={n:len(list(filters(n))) for n in range(1,4)}
    for n in range(1,4):
      for m in range(1,4):
        for F in filters(n):
          for G in filters(m):
            pairs+=1
            for R in range(1<<(n*m)):
              l,r=filt_tensor(F,G,n,m,R);q+=1
              assert l==r,(n,m,F,G,R,l,r)
    assert fcounts=={1:1,2:3,3:7}, fcounts
    print('ALL_CHECKS_OK', 'filters_by_carrier='+str(fcounts), 'filter_pairs='+str(pairs),'finite_relations='+str(q))
if __name__=='__main__':main()
