"""Independent arithmetic-vs-neighborhood verification for finite path powers.
This code is auxiliary to an entirely symbolic proof, not its substitute.
"""

def closed(n,r,x,y):
    assert 1<=x<y<=n and r>=2
    d=y-x
    adj=(d<=r)
    z11=(d<=2*r)
    z10=(y>=r+2 and not (x==1 and y==r+2))
    z01=(x<=n-r-1 and not (y==n and x==n-r-1))
    z00=(n>4*r+2) # only applies to stable family
    return (adj, z00,z01,z10,z11)

def direct(n,r,x,y):
    others=[z for z in range(1,n+1) if z not in (x,y)]
    have={(abs(x-z)<=r,abs(y-z)<=r) for z in others}
    return (y-x<=r,(False,False) in have,(False,True) in have,(True,False) in have,(True,True) in have)

def pointed(n,r):
    profiles=[]
    for x in range(1,n+1):
        each=set()
        for y in range(1,n+1):
            if x==y:continue
            if x<y:
                a,z00,z01,z10,z11=closed(n,r,x,y)
            else:
                a,z00,z10,z01,z11=closed(n,r,y,x)
            each.add((int(a),int(z00),int(z01),int(z10),int(z11)))
        profiles.append(frozenset(each))
    return profiles

if __name__=='__main__':
    npairs=0; ngraphs=0
    expected_five=None
    for r in range(2,18):
        for n in range(4*r+3,4*r+9):
            ps=pointed(n,r)
            assert len(set(ps))==5,(n,r,len(set(ps)))
            for x in range(1,n+1):
                a=min(x-1,n-x)
                group=0 if a==0 else (1 if a<r else (2 if a==r else (3 if a==r+1 else 4)))
                if expected_five is None: expected_five=[None]*5
                if expected_five[group] is None: expected_five[group]=ps[x-1]
                assert ps[x-1]==expected_five[group],(n,r,x,group,ps[x-1],expected_five[group])
            ngraphs+=1
            for x in range(1,n+1):
                for y in range(x+1,n+1):
                    assert closed(n,r,x,y)==direct(n,r,x,y),(n,r,x,y,closed(n,r,x,y),direct(n,r,x,y))
                    npairs+=1
    print('ARITHMETIC_FORMULA_OK graphs=',ngraphs,'ordered_pairs=',npairs)
    for i,p in enumerate(expected_five):
        print('GROUP',i, sorted(p))
