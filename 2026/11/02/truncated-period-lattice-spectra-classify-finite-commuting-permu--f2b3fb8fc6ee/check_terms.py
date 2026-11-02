"""Direct verification of quantifier-free stabilizer and orbit tests.
Usage: python check_terms.py
No external modules.
"""

def torus(a,b,s):
    f={}; g={}
    for i in range(a):
        for j in range(b):
            f[(i,j)]=((i+1)%a,j)
            g[(i,j)]=(i,j+1) if j<b-1 else ((i-s)%a,0)
    return f,g


def power(z,op,n):
    for _ in range(n):z=op[z]
    return z


def word(z,f,g,i,j):return power(power(z,g,j),f,i)


def has_type(z,f,g,H):
    a,b,s=H
    if power(z,f,a)!=z or word(z,f,g,s,b)!=z:return False
    terms={word(z,f,g,i,j) for i in range(a) for j in range(b)}
    return len(terms)==a*b


def main():
    orbit_types=[(a,b,s) for a in range(1,11) for b in range(1,11)
                 if a*b<=10 for s in range(a)]
    tests=0
    for h in orbit_types:
        for j in orbit_types:
            f,g=torus(*j)
            for z in f:
                assert has_type(z,f,g,h)==(h==j),(h,j,z)
                tests+=1
    print('HNF subgroups with index <= 10:',len(orbit_types))
    print('cross-subgroup point-type tests:',tests)
    print('every quantifier-free stabilizer formula exact: PASS')
if __name__=='__main__':main()
