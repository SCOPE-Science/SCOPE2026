#!/usr/bin/env python3
import itertools

def tuple_to_matrix(bits):
    S=[[0]*5 for _ in range(5)]
    k=0
    for i in range(5):
        for j in range(i+1,5):
            a=bits[k]; k+=1
            S[i][j]=a; S[j][i]=-a
    return S

def matrix_to_tuple(S):
    return tuple(S[i][j] for i in range(5) for j in range(i+1,5))

def pf4(a,b,c,d,e,f):
    # pf([[0,a,b,c],[-a,0,d,e],[-b,-d,0,f],[-c,-e,-f,0]])
    return a*f-b*e+c*d

def C_value(bits):
    S=tuple_to_matrix(bits)
    vals=[]
    for drop in range(5):
        I=[i for i in range(5) if i!=drop]
        a=S[I[0]][I[1]]; b=S[I[0]][I[2]]; c=S[I[0]][I[3]]
        d=S[I[1]][I[2]]; e=S[I[1]][I[3]]; f=S[I[2]][I[3]]
        vals.append(pf4(a,b,c,d,e,f))
    return sum(x*x for x in vals)

def normalize_first_row(tail):
    # entries (01,02,03,04) are +1; remaining six use tail
    return (1,1,1,1)+tuple(tail)

def transform(bits, perm, signs):
    S=tuple_to_matrix(bits)
    T=[[0]*5 for _ in range(5)]
    # coordinate transform by signed permutation: T_ab = d_a d_b S_{p(a),p(b)}
    for a in range(5):
        for b in range(5):
            T[a][b]=signs[a]*signs[b]*S[perm[a]][perm[b]]
    return matrix_to_tuple(T)

def main():
    nc={5:0,21:0}
    for tail in itertools.product((-1,1), repeat=6):
        c=C_value(normalize_first_row(tail))
        assert c in nc, c
        nc[c]+=1
    assert nc=={5:24,21:40}, nc

    all_counts={5:0,21:0}
    maxset=set()
    for bits in itertools.product((-1,1), repeat=10):
        c=C_value(bits)
        assert c in all_counts, c
        all_counts[c]+=1
        if c==5: maxset.add(bits)
    assert all_counts=={5:384,21:640}, all_counts

    seed=next(iter(maxset))
    orbit=set()
    for perm in itertools.permutations(range(5)):
        for signs in itertools.product((-1,1), repeat=5):
            orbit.add(transform(seed,perm,signs))
    assert len(orbit)==384, len(orbit)
    assert orbit==maxset

    print('VERIFY_OK normalized_C5=24 normalized_C21=40 all_C5=384 all_C21=640 max_orbit=384')

if __name__=='__main__':
    main()
