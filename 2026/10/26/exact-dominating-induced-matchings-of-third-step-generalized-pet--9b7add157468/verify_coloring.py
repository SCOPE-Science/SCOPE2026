"""Independent vertex-color formulation and candidate enumeration for GP(n,3).
Enumerates all cyclic outer words avoiding 00 and 111, determines inner bits
from the outer vertex equation, and independently validates inner equations.
"""

def outer_words(n):
    def search(w):
        i=len(w)
        if i==n:
            if w[0]==0 and w[-1]==0:return
            if w[-2]+w[-1]+w[0]==3:return
            if w[-1]+w[0]+w[1]==3:return
            yield tuple(w)
            return
        for val in (0,1):
            if i>=1 and w[-1]==0 and val==0:continue
            if i>=2 and w[-2]==w[-1]==val==1:continue
            yield from search(w+[val])
    yield from search([])


def solution_words(n):
    ans=[]
    for x in outer_words(n):
        y=[3-2*x[i]-x[(i-1)%n]-x[(i+1)%n] for i in range(n)]
        if not all(v in (0,1) for v in y):continue
        if all(x[i]+2*y[i]+y[(i-3)%n]+y[(i+3)%n]==3 for i in range(n)):
            ans.append((x,tuple(y)))
    return ans

if __name__=='__main__':
    for n in range(7,33):
        sol=solution_words(n)
        expected=5 if n%5==0 else 0
        assert len(sol)==expected,(n,len(sol),expected)
        if sol:
            for x,y in sol:
                assert all(x[i]==x[i%5] and y[i]==y[i%5] for i in range(n))
        print(f'n={n} valid_binary_colorings={len(sol)}')
    print('PASS: independent cyclic-vertex-word enumeration, 7<=n<=32')
