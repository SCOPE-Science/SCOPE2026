"""Exact, standalone verification of the Petersen four-color Hom cell character.

Run: python3 verify.py
No external packages are required. All enumeration and arithmetic are integral.
"""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

V=list(itertools.combinations(range(5),2))
assert len(V)==10
VI={p:i for i,p in enumerate(V)}
N=[tuple(j for j,w in enumerate(V) if set(w).isdisjoint(u)) for u in V]
assert all(len(n)==3 for n in N)

colors=[]
assignment=[-1]*10
def rec(i):
    if i==10:
        colors.append(tuple(assignment))
        return
    for c in range(4):
        if all(assignment[j]<0 or assignment[j]!=c for j in N[i]):
            assignment[i]=c
            rec(i+1)
    assignment[i]=-1
rec(0)
assert len(colors)==12960

# Every product-of-simplices cell contains a vertex; start with all vertices
# and successively add every color permitted by its neighbors' complete lists.
seed={tuple(1<<c for c in a) for a in colors}
all_cells=set(seed)
frontier=list(seed)
while frontier:
    following=[]
    for x in frontier:
        for i in range(10):
            forbidden=0
            for j in N[i]:
                forbidden |= x[j]
            for c in range(4):
                bit=1<<c
                if bit&(forbidden|x[i]):
                    continue
                y=x[:i]+(x[i]|bit,)+x[i+1:]
                if y not in all_cells:
                    all_cells.add(y)
                    following.append(y)
    frontier=following
cells=sorted(all_cells)
fvec=dict(sorted(Counter(sum(m.bit_count()-1 for m in x) for x in cells).items()))
assert fvec=={0:12960,1:53280,2:80400,3:54960,4:17400,5:2400,6:120}
assert len(cells)==221520
assert sum((-1)**k*v for k,v in fvec.items())==240

# The recoloring graph is the one-skeleton: every move alters one color.
index={a:i for i,a in enumerate(colors)}
seen={colors[0]}
queue=[colors[0]]
for a in queue:
    for i in range(10):
        forbidden={a[j] for j in N[i]}
        for c in range(4):
            if c==a[i] or c in forbidden:
                continue
            b=a[:i]+(c,)+a[i+1:]
            assert b in index
            if b not in seen:
                seen.add(b)
                queue.append(b)
assert len(seen)==len(colors)

def cycle_rep(part):
    a=list(range(sum(part)))
    j=0
    for length in part:
        for k in range(length):
            a[j+k]=j+(k+1)%length
        j+=length
    return tuple(a)

def cycles(p):
    seen=set()
    result=[]
    for i in range(len(p)):
        if i not in seen:
            cyc=[]
            j=i
            while j not in seen:
                seen.add(j)
                cyc.append(j)
                j=p[j]
            result.append(cyc)
    return result

def power(p,n):
    out=tuple(range(len(p)))
    for _ in range(n):
        out=tuple(p[i] for i in out)
    return out

def restricted_sign(p,mask):
    x=[i for i in range(4) if mask>>i&1]
    y=[p[i] for i in x]
    if set(x)!=set(y):
        return 0
    return 1-2*(sum(y[i]>y[j] for i in range(len(y)) for j in range(i+1,len(y)))%2)

p5=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
p4=((1,1,1,1),(2,1,1),(2,2),(3,1),(4,))
def key(p,q):
    return '/'.join(map(str,p))+';'+'/'.join(map(str,q))

def class_size(p):
    return math.factorial(sum(p))//math.prod(k**n*math.factorial(n) for k,n in Counter(p).items())

published=json.loads(Path(__file__).with_name('class_character.json').read_text(encoding='utf-8'))
assert published['f_vector']=={str(k):v for k,v in fvec.items()}
assert len(published['character'])==35
traces={}
for pa in p5:
    p=cycle_rep(pa)
    pv=tuple(VI[tuple(sorted((p[a],p[b])))] for a,b in V)
    cyc=cycles(pv)
    for pb in p4:
        q=cycle_rep(pb)
        masks=tuple(sum(1<<q[i] for i in range(4) if m>>i&1) for m in range(16))
        parity=[]
        for c in cyc:
            qq=power(q,len(c))
            parity.append({m:(-1)**(m.bit_count()-1)*restricted_sign(qq,m) for m in range(1,16) if masks[m]!=0})
        total=0
        count=0
        for x in cells:
            if any(x[pv[i]]!=masks[x[i]] for i in range(10)):
                continue
            count+=1
            sign=1
            for c,sgn in zip(cyc,parity):
                assert sgn[x[c[0]]]!=0
                sign*=sgn[x[c[0]]]
            total+=sign
        name=key(pa,pb)
        assert published['character'][name]=={'trace':total,'fixed_cells':count,'class_size':class_size(pa)*class_size(pb)}
        traces[(pa,pb)]=total

# Independent Specht projections: for S5, the (3,2) character is the
# permutation character on two-subsets minus that on singletons.
# Its conjugate partition (2,2,1) is the sign twist.
def specht_32(pa):
    f=pa.count(1)
    return f*(f-1)//2+pa.count(2)-f

def sign(pa):
    return (-1)**(sum(pa)-len(pa))

def multiplicity(source_sign,color_sign):
    total=0
    for pa in p5:
        for pb in p4:
            a=specht_32(pa)*(sign(pa) if source_sign else 1)
            b=sign(pb) if color_sign else 1
            total+=(traces[(pa,pb)]-1)*class_size(pa)*class_size(pb)*a*b
    assert total%2880==0
    return total//2880

assert multiplicity(False,False)==1
assert multiplicity(False,True)==1
assert multiplicity(True,False)==1
assert multiplicity(True,True)==-1
assert traces[(p5[0],p4[0])]==240
print('vertices',len(colors),'all_cells',len(cells),'connected',len(seen)==len(colors))
print('face_vector',fvec,'Euler',240,'reduced_Euler',239)
print('classes',len(traces),'source_group',120,'color_group',24)
print('multiplicity_(3,2)_x_trivial',multiplicity(False,False))
print('multiplicity_(2,2,1)_x_sign',multiplicity(True,True))
print('VERIFY_OK')
