"""Independent unreduced exact rank-four FO-type recurrence for two ladder families.
Usage: python research03_prism_direct.py [exclusive_max_width]. Pure Python 3.
"""
import sys

TABLES=[{}, {}, {}, {}]
def intern(level,sig):
    table=TABLES[level]
    if sig not in table:table[sig]=len(table)
    return table[sig]

def build(kind,n):
    N=2*n;edges=[set() for _ in range(N)]
    def add(u,v):edges[u].add(v);edges[v].add(u)
    if kind=='P':
        for i in range(n):
            add(2*i,2*i+1)
            for row in (0,1):add(2*i+row,2*((i+1)%n)+row)
    else:
        for i in range(N):
            add(i,(i+1)%N)
            add(i,(i+n)%N)
    return edges

def atom(E,t):
    return tuple(0 if t[i]==t[j] else 1 if t[j] in E[t[i]] else 2
                 for j in range(1,len(t)) for i in range(j))

def rank4(E):
    N=len(E)
    # Here all ordered triples are computed, including repetitions,
    # without any graph automorphism reduction.
    T3={}
    for a in range(N):
      for b in range(N):
       for c in range(N):
        sig=tuple(sorted({atom(E,(a,b,c,d)) for d in range(N)}))
        T3[a,b,c]=intern(0,sig)
    T2={}
    for a in range(N):
      for b in range(N):
        sig=tuple(sorted({T3[a,b,c] for c in range(N)}))
        T2[a,b]=intern(1,sig)
    T1={}
    for a in range(N):
        sig=tuple(sorted({T2[a,b] for b in range(N)}))
        T1[a]=intern(2,sig)
    return intern(3,tuple(sorted(set(T1.values()))))

if __name__=='__main__':
    stop=int(sys.argv[1]) if len(sys.argv)>1 else 13
    for n in range(3,stop):
        p=rank4(build('P',n));m=rank4(build('M',n))
        print(n,p,m,'equiv' if p==m else 'distinct',flush=True)
