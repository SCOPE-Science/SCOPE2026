"""Direct subset-sum relation verifier for cyclic three-chain orders."""
from itertools import product


def closure(t, signs):
    N=3*(2*t+1)
    reach=[[0]*N for _ in range(N)]
    for a in range(2*t):
        for z in range(3): reach[3*a+z][3*(a+1)+z]=1
    for j,s in enumerate(signs):
        for z in range(3): reach[3*(2*j)+z][3*(2*j+2)+(z+s)%3]=1
    for k in range(N):
        for a in range(N):
            if reach[a][k]:
                for b in range(N):
                    reach[a][b] |= reach[k][b]
    return reach


def direct_relation(t, signs, a, x, b, y):
    if a>=b: return False
    offsets={0}
    for j,s in enumerate(signs):
        if a<=2*j and 2*j+2<=b:
            offsets |= {(v+s)%3 for v in tuple(offsets)}
    return (y-x)%3 in offsets


def main():
    checked=0
    for t in range(1,8):
        for signs in product((1,-1),repeat=t):
            R=closure(t,signs)
            for a in range(2*t+1):
                for b in range(2*t+1):
                    for x in range(3):
                        for y in range(3):
                            assert bool(R[3*a+x][3*b+y])==direct_relation(t,signs,a,x,b,y)
                            checked+=1
        print(f'checked subset-sum formula for t={t}, {2**t} sign choices')
    print(f'PASS: {checked} ordered pair relations equal the independent subset-sum formula')

if __name__=='__main__':main()
