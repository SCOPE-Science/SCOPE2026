"""Finite checks of singleton classes in marked affine incidence graphs.
Standard library only; fields represented in polynomial bases over prime fields.
"""
from collections import Counter

CASES = [
    (2, (0, 1)), (3, (0, 1)), (5, (0, 1)), (7, (0, 1)),
    (2, (1, 1, 1)),     # 4 = GF(2)[x]/(x^2+x+1)
    (2, (1, 1, 0, 1)),  # 8 = GF(2)[x]/(x^3+x+1)
    (3, (1, 0, 1)),     # 9 = GF(3)[x]/(x^2+1)
    (2, (1, 1, 0, 0, 1)), # 16 = GF(2)[x]/(x^4+x+1)
    (5, (2, 0, 1)),     # 25 = GF(5)[x]/(x^2+2)
]
class Field:
    def __init__(self, p, modulus):
        assert modulus[-1] == 1
        self.p, self.n = p, len(modulus)-1
        self.q = p**self.n
        self.modulus = modulus
        self.digits = []
        for x in range(self.q):
            ds=[]; y=x
            for i in range(self.n):ds.append(y%p);y//=p
            self.digits.append(ds)
        self.sum = [[0]*self.q for _ in range(self.q)]
        self.mul = [[0]*self.q for _ in range(self.q)]
        for a in range(self.q):
            for b in range(self.q):
                c=[(x+y)%p for x,y in zip(self.digits[a],self.digits[b])]
                self.sum[a][b]=sum(x*p**i for i,x in enumerate(c))
                d=[0]*(2*self.n-1)
                for i,x in enumerate(self.digits[a]):
                    for j,y in enumerate(self.digits[b]):d[i+j]=(d[i+j]+x*y)%p
                for k in range(len(d)-1,self.n-1,-1):
                    lead=d[k]
                    for j in range(self.n):
                        d[k-self.n+j]=(d[k-self.n+j]-lead*modulus[j])%p
                self.mul[a][b]=sum(d[i]*p**i for i in range(self.n))
        assert all(self.mul[a][b]!=0 for a in range(1,self.q) for b in range(1,self.q))
        self.neg=[next(y for y in range(self.q) if self.sum[x][y]==0) for x in range(self.q)]

    def add(self,x,y):return self.sum[x][y]
    def multiply(self,x,y):return self.mul[x][y]
    def sub(self,x,y):return self.sum[x][self.neg[y]]


def affine_graph(F):
    q=F.q
    pts=[(x,y) for x in range(q) for y in range(q)]
    lines=[('v',c) for c in range(q)]+[('n',a,b) for a in range(q) for b in range(q)]
    nb=[[] for _ in range(len(pts)+len(lines))]
    for i,(x,y) in enumerate(pts):
        for j,line in enumerate(lines):
            if (line[0]=='v' and x==line[1]) or (line[0]=='n' and y==F.add(F.multiply(line[1],x),line[2])):
                nb[i].append(len(pts)+j)
                nb[len(pts)+j].append(i)
    assert all(len(nb[i])==q+1 for i in range(q*q))
    assert all(len(nb[i])==q for i in range(q*q,len(nb)))
    return pts,lines,nb


def color_refinement(nb, npoints, marks):
    colors=[0]*npoints+[1]*(len(nb)-npoints)
    for k,i in enumerate(marks):colors[i]=2+k
    for step in range(len(nb)+2):
        signature=[(colors[i],tuple(sorted(Counter(colors[j] for j in nb[i]).items()))) for i in range(len(nb))]
        kind={sig:k for k,sig in enumerate(sorted(set(signature)))}
        fresh=[kind[s] for s in signature]
        if len(set(fresh)) == len(set(colors)):
            colors=fresh
            return colors,step+1
        colors=fresh
    raise AssertionError('No stabilization')

def check_case(F):
    pts,lines,nb=affine_graph(F)
    frame=[pts.index(v) for v in [(0,0),(1,0),(0,1)]]
    colors,r=color_refinement(nb,len(pts),frame)
    cs=Counter(colors)
    ps={pt for i,pt in enumerate(pts) if cs[colors[i]]==1}
    ls={ln for j,ln in enumerate(lines) if cs[colors[len(pts)+j]]==1}
    p=F.p
    required={(x,y) for x in range(p) for y in range(p)}
    required_lines={('v',c) for c in range(p)}|{('n',a,b) for a in range(p) for b in range(p)}
    assert ps==required,(F.q,'point',ps,required)
    assert ls==required_lines,(F.q,'line',ls,required_lines)
    print('q',F.q,'three_marks','singleton_points',len(ps),'singleton_lines',len(ls),'rounds',r)
    if F.n>1:
        t=p # polynomial indeterminate x
        index=pts.index((t,0))
        colors,r=color_refinement(nb,len(pts),frame+[index])
        assert len(set(colors))==len(colors),(F.q,'four marks non-discrete')
        print('q',F.q,'four_marks','discrete',len(colors),'rounds',r)
    else:
        assert len(set(colors))==len(colors)

if __name__=='__main__':
    for p,mod in CASES:
        check_case(Field(p,mod))
    # Nontrivial intermediate subfield: GF(4) contained in GF(16).
    F=Field(2,(1,1,0,0,1))
    pts,lines,nb=affine_graph(F)
    K={z for z in range(F.q) if F.multiply(F.multiply(z,z), F.multiply(z,z))==z}
    assert len(K)==4 and K=={0,1,6,7}
    t=next(z for z in K if z not in (0,1))
    for fourth in [(t,0),(t,F.multiply(t,t))]:
        marks=[pts.index(a) for a in [(0,0),(1,0),(0,1),fourth]]
        c,r=color_refinement(nb,len(pts),marks)
        ct=Counter(c)
        point_singletons={a for i,a in enumerate(pts) if ct[c[i]]==1}
        line_singletons={a for i,a in enumerate(lines) if ct[c[len(pts)+i]]==1}
        assert point_singletons=={(a,b) for a in K for b in K}
        assert line_singletons=={('v',a) for a in K}|{('n',a,b) for a in K for b in K}
        print('q 16 GF4_fourth_mark', fourth, 'singleton_points',len(point_singletons),'singleton_lines',len(line_singletons),'rounds',r)
    print('ALL_CASES_PASS')
