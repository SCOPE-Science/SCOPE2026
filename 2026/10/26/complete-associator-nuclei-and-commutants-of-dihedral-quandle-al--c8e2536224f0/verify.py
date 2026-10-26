"""Direct modular-linear-algebra check of dihedral quandle associator nuclei.

Every constraint is generated from the defining basis multiplication, not from
any purported cyclic-polynomial simplification.
"""

from itertools import product


def product_index(i, j, n):
    return (2*j-i) % n


def rref_rank(rows, p, n):
    a = [[x % p for x in row] for row in rows]
    pivot = 0
    for col in range(n):
        k = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        inverse = pow(a[pivot][col], -1, p)
        a[pivot] = [(inverse*x) % p for x in a[pivot]]
        for i in range(pivot + 1, len(a)):
            factor = a[i][col]
            if factor:
                a[i] = [(x-factor*y) % p for x,y in zip(a[i],a[pivot])]
        pivot += 1
        if pivot == n:
            break
    return pivot


def constraint_matrices(n):
    matrices = [[] for _ in range(4)]
    op = lambda i,j: product_index(i,j,n)
    for i, j in product(range(n), repeat=2):
        block = [[[0]*n for _ in range(n)] for _ in range(4)]
        for t in range(n):
            pairs = (
                (op(op(t,i),j), op(t,op(i,j))),
                (op(op(i,t),j), op(i,op(t,j))),
                (op(op(i,j),t), op(i,op(j,t))),
                (op(t,i), op(i,t)),
            )
            for which,(plus,minus) in enumerate(pairs):
                block[which][plus][t] += 1
                block[which][minus][t] -= 1
        for which in range(4):
            matrices[which].extend(block[which])
    return matrices


def predicted(n,p):
    if n%2:
        return (1,1,1,3 if n%3==0 else 1,1,1)
    m=n//2
    return (2, m+1, m+1 if m%2 else m,
            0, 2 if m%2 or p==2 else 0, 0)


def kernel_member(rows, vector, p):
    return all(sum(a*b for a,b in zip(row,vector))%p==0 for row in rows)


def multiply(u,v,n,p):
    result=[0]*n
    for i,x in enumerate(u):
        if not x:continue
        for j,y in enumerate(v):
            if y: result[product_index(i,j,n)] = (result[product_index(i,j,n)]+x*y)%p
    return result


def check(n,p):
    spaces=constraint_matrices(n)
    dims=tuple(n-rref_rank(M,p,n) for M in spaces)
    all_nuc=[row for M in spaces[:3] for row in M]
    both=[row for M in spaces for row in M]
    got=dims+(n-rref_rank(all_nuc,p,n), n-rref_rank(both,p,n))
    want=predicted(n,p)
    assert got==want, (n,p,got,want)

    if n%2:
        omega=[1]*n
        assert kernel_member(all_nuc,omega,p)
        assert kernel_member(both,omega,p)
        assert multiply(omega,omega,n,p)==[n%p]*n
        d=3 if n%3==0 else 1
        for k in range(d):
            vec=[int(i%d==k) for i in range(n)]
            assert kernel_member(spaces[3],vec,p)
    else:
        m=n//2
        basis=[[int(i%2==k) for i in range(n)] for k in range(2)]
        for x in basis:
            assert kernel_member(spaces[0],x,p)
            if want[4]==2:
                assert kernel_member(all_nuc,x,p)
            else:
                assert not kernel_member(all_nuc,x,p)
        for i,j in product(range(2),repeat=2):
            assert multiply(basis[i],basis[j],n,p)==[(m*x)%p for x in basis[i]]
        for j in range(m):
            pair=[0]*n
            pair[j]=1;pair[j+m]=-1
            assert kernel_member(spaces[1],pair,p)
            if m%2==0:
                assert kernel_member(spaces[2],pair,p)
    return got


if __name__=='__main__':
    for prime in (2,3,5):
        for order in range(2,15):
            result=check(order,prime)
            print('n=',order,'characteristic=',prime,'dimensions=',result)
    print('ALL_NUCLEUS_CHECKS_OK')
