"""Independent finite checks of the fork-frame IK4 normal form.
The root is index 0 and the remaining elements are incomparable maximal worlds.
Only the standard library is required.
"""

def all_relations(n):
    for mask in range(1 << (n*n)):
        rows=tuple((mask >> (n*i)) & ((1<<n)-1) for i in range(n))
        yield rows

def transitive(rows):
    n=len(rows)
    return all(not((rows[i] >> j)&1) or not(rows[j] & ~rows[i])
               for i in range(n) for j in range(n))

def confluences(rows):
    n=len(rows)
    # Forth-up condition.
    for w in range(n):
        for u in range(n):
            if w!=u and w!=0: continue
            for v in range(n):
                if not (rows[w] >> v)&1: continue
                if not any(((rows[u] >> vp)&1) and (v==vp or v==0)
                           for vp in range(n)):
                    return False
    # Back-up condition.
    for w in range(n):
        for v in range(n):
            if not((rows[w] >> v)&1): continue
            for vp in range(n):
                if v!=vp and v!=0: continue
                if not any(((rows[wp] >> vp)&1) and (w==wp or w==0)
                           for wp in range(n)):
                    return False
    return True

def normal_form(rows):
    n=len(rows)
    T=tuple(sum(((rows[i] >> j)&1) << (j-1) for j in range(1,n))
            for i in range(1,n))
    if not transitive(T):return False
    leaves=range(1,n)
    U={j for j in leaves if all((rows[i] >> j)&1 for i in leaves)}
    V={i for i in leaves if all((rows[i] >> j)&1 for j in leaves)}
    S={j for j in leaves if (rows[0] >> j)&1}
    B={i for i in leaves if (rows[i]&1)}
    c=rows[0]&1
    if S and S!=U:return False
    if B and B!=V:return False
    if S & B and not c:return False
    if c and (any(not T[i] for i in range(n-1)) or
              any(not any(T[i] >> j&1 for i in range(n-1)) for j in range(n-1))):
        return False
    return True

def predicted_count(k):
    N=0
    for T in all_relations(k):
        if not transitive(T):continue
        full=(1<<k)-1
        U={j for j in range(k) if all(T[i]>>j&1 for i in range(k))}
        V={i for i in range(k) if T[i]==full}
        both= bool(U) and bool(V) and bool(U & V)
        C=all(T[i]!=0 for i in range(k)) and all(any(T[i]>>j&1 for i in range(k)) for j in range(k))
        # all choices of S and B, with c allowed if C and needed when S cap B.
        for s in (False,True) if U else (False,):
            for b in (False,True) if V else (False,):
                need = bool(s and b and both)
                if not need:N+=1 # c=0
                if C:N+=1 # c=1
    return N
def statistics(maxk):
    t=[];r=[];b=[]
    for k in range(maxk+1):
        Tj=Rj=Bj=0
        for rows in all_relations(k):
            if not transitive(rows): continue
            Tj+=1
            row_complete=all(rows[i] for i in range(k))
            col_complete=all(any(rows[i]>>j&1 for i in range(k)) for j in range(k))
            Rj+=row_complete
            Bj+=row_complete and col_complete
        t.append(Tj);r.append(Rj);b.append(Bj)
    return t,r,b

def cardinality_formula(k,t,r,b):
    from math import comb
    no_root_loop=sum(comb(k,j)*2**(k-j)*t[j] for j in range(k+1))
    root_loop=(b[k]+2*sum(comb(k,j)*r[j] for j in range(k))
      +sum(comb(k,j)*(2**(k-j)-2)*t[j] for j in range(k-1))+1)
    return no_root_loop,root_loop

if __name__=='__main__':
    t,r,b=statistics(4)
    assert (t,r,b)==([1,2,13,171,3994],[1,1,6,68,1387],
                       [1,1,4,35,583]),(t,r,b)
    expected=((4,4),(25,13),(281,98),(5754,1428))
    for k in (1,2,3):
        n=k+1
        got=[0,0]
        for rows in all_relations(n):
            actual=transitive(rows) and confluences(rows)
            predicted=normal_form(rows)
            assert actual==predicted,(k,rows,actual,predicted)
            got[bool(rows[0]&1)]+=actual
        assert tuple(got)==expected[k-1],(k,got)
        assert cardinality_formula(k,t,r,b)==tuple(got)
        print('direct',k,'relations_tested',2**(n*n),
              'root_irreflexive',got[0],'root_reflexive',got[1])
    assert cardinality_formula(4,t,r,b)==expected[3]
    assert predicted_count(4)==sum(expected[3])
    print('weighted',4,'transitive_leaf_relations',t[4],
          'root_irreflexive',expected[3][0],
          'root_reflexive',expected[3][1])
    print('VERIFY_OK')
