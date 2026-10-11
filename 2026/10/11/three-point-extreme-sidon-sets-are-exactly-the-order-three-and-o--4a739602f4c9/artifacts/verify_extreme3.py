from collections import Counter
import cmath, itertools, math

# Finite regression over product groups Z_m x Z_n.  The proof in RESULT.md is algebraic;
# this finite check only tests the support classification and explicit witnesses.

def add(x,y,mods): return tuple((a+b)%m for a,b,m in zip(x,y,mods))
def neg(x,mods): return tuple((-a)%m for a,m in zip(x,mods))
def sub(x,y,mods): return add(x,neg(y,mods),mods)
def mul(k,x,mods): return tuple((k*a)%m for a,m in zip(x,mods))
def order(x,mods):
    y=tuple(0 for _ in mods)
    for k in range(1, 4*max(mods)+5):
        y=add(y,x,mods)
        if all(v==0 for v in y): return k
    raise AssertionError

def translate_norm(E,mods):
    base=E[0]
    return [sub(x,base,mods) for x in E]

def structural_type(E,mods):
    E0=translate_norm(E,mods)
    a,b=E0[1],E0[2]
    # order-3 coset: translated support is {0,d,2d}
    for d in (a,b):
        if order(d,mods)==3 and set(E0)=={tuple(0 for _ in mods), d, mul(2,d,mods)}:
            return 'C3'
    # three of a cyclic order-4 coset
    for d in (a,b,sub(b,a,mods)):
        if order(d,mods)==4:
            H={tuple(0 for _ in mods),d,mul(2,d,mods),mul(3,d,mods)}
            if set(E0).issubset(H) and len(E0)==3:
                return 'C4'
    # Klein-four candidate
    nonzero=[x for x in E0 if any(x)]
    if len(nonzero)==2 and all(order(x,mods)==2 for x in nonzero):
        return 'V4'
    return None

def repeated_difference_candidate(E,mods):
    c=Counter(sub(x,y,mods) for x in E for y in E if x!=y)
    return all(v>=2 for v in c.values())

def characters(mods):
    for idx in itertools.product(*[range(m) for m in mods]):
        yield idx

def char(idx,x,mods):
    angle=2*math.pi*sum(i*a/m for i,a,m in zip(idx,x,mods))
    return cmath.exp(1j*angle)

def flat_for_witness(E,mods,typ):
    # reorder/translate support to {0,d,2d}; translation only contributes a character factor.
    base=E[0]
    E0=translate_norm(E,mods)
    zero=tuple(0 for _ in mods)
    if typ=='C3':
        d=next(x for x in E0 if any(x) and order(x,mods)==3)
        ordered=[zero,d,mul(2,d,mods)]
        omega=cmath.exp(2j*math.pi/3)
        coeff=[1,1,omega]
    elif typ=='C4':
        d=None
        for x in [y for y in E0 if any(y)]+[sub(E0[2],E0[1],mods)]:
            if order(x,mods)==4 and set(E0).issubset({zero,x,mul(2,x,mods),mul(3,x,mods)}):
                # choose orientation/translate among the 3 points to realize {0,d,2d}
                for t in E:
                    F=[sub(y,t,mods) for y in E]
                    if set(F)=={zero,x,mul(2,x,mods)}:
                        ordered=[zero,x,mul(2,x,mods)]; d=x; break
                if d is not None: break
                xn=neg(x,mods)
                for t in E:
                    F=[sub(y,t,mods) for y in E]
                    if set(F)=={zero,xn,mul(2,xn,mods)}:
                        ordered=[zero,xn,mul(2,xn,mods)]; d=xn; break
            if d is not None: break
        if d is None: return False
        p=cmath.exp(-1j*math.pi/4)
        coeff=[1,p,1j]
    else:
        return False
    vals=[]
    for chi in characters(mods):
        vals.append(abs(sum(c*char(chi,x,mods) for c,x in zip(coeff,ordered))))
    return max(vals)-min(vals) < 2e-10 and abs(vals[0]-math.sqrt(3))<2e-10

triples=0
candidates=0
good=0
v4=0
for m in range(2,9):
  for n in range(1,7):
    mods=(m,n)
    G=list(itertools.product(range(m),range(n)))
    if len(G)>48: continue
    zero=(0,0)
    # normalize one point to zero to avoid translation duplicates
    for a,b in itertools.combinations([x for x in G if x!=zero],2):
        E=[zero,a,b]; triples+=1
        if repeated_difference_candidate(E,mods):
            candidates+=1
            typ=structural_type(E,mods)
            assert typ in ('C3','C4','V4'), (mods,E,typ)
            if typ in ('C3','C4'):
                assert flat_for_witness(E,mods,typ), (mods,E,typ)
                good+=1
            else:
                # The analytic contradiction is Re p = Re q = Re(p qbar)=0.
                v4+=1

assert good>0 and v4>0
print(f'VERIFY_OK triples={triples} multiplicity_candidates={candidates} good_C3_C4={good} V4_obstructions={v4}')
