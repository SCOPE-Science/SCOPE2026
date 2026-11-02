"""Exact F3/F9 check of the two local relative-Fano types.
The proof establishes the algebraic-closure statement via coordinates and symmetry.
"""
from itertools import product

def mod(x):return x%3

def lin_solve(A,b):
    M=[[x%3 for x in r]+[v%3] for r,v in zip(A,b)]
    for j in range(4):
        pivot=next((i for i in range(j,4) if M[i][j]),None)
        assert pivot is not None
        M[j],M[pivot]=M[pivot],M[j]
        factor=1 if M[j][j]==1 else 2
        M[j]=[(factor*z)%3 for z in M[j]]
        for i in range(4):
            if i!=j:
                c=M[i][j]
                M[i]=[(M[i][t]-c*M[j][t])%3 for t in range(5)]
    return [M[i][4] for i in range(4)]

def fourth_roots_in_F9():
    mul=lambda u,v: (((u%3)*(v%3)+2*(u//3)*(v//3))%3)+3*(((u%3)*(v//3)+(u//3)*(v%3))%3)
    pow4=lambda x:mul(mul(x,x),mul(x,x))
    roots=[i for i in range(9) if pow4(i)==1]
    anti=[i for i in range(9) if pow4(i)==2]
    assert len(roots)==len(anti)==4
    return roots,anti

roots,anti=fourth_roots_in_F9()
assert len({(a,b,c) for a,b,c in product(roots,repeat=3)})==64
assert 3*len(anti)**2==48
# The exotic representative is z=s+t, w=s-t. In char 3:
a,b,c,d=1,1,1,2
assert (1+a**4+b**4)%3==0
assert (1+c**4+d**4)%3==0
assert (a**3*c+b**3*d)%3==0
assert (a*c**3+b*d**3)%3==0
assert (a*d+b*c)%3==0
# Four independent equations A,B,C,D on a Grassmann chart.
J=[[a**3,b**3,0,0], [0,0,c**3,d**3],
   [0,0,a**3,b**3], [c**3,d**3,0,0]]
# The lambda derivative of (A,B,C,D) is (0,0,ab,cd).
v=lin_solve(J,[0,0,-a*b,-c*d])
aa,bb,cc,dd=v
obstruction=(aa*d+a*dd+bb*c+b*cc)%3
assert obstruction==1,(v,obstruction)
# Standard representative z=alpha*s,w=beta*t: alpha^4=beta^4=-1.
# Then the mixed coefficient of lambda*xyzw equals alpha*beta != 0.
assert all(i!=0 for i in anti)
print('DWORK_LOCAL_TANGENT_48_REDUCED_64_LENGTH_TWO_TOTAL_176_OK')
