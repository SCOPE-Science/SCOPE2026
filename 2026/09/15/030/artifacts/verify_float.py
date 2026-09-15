"""Independent float verification of S(g) for the three suspect classes + all classes."""
import re, math
def E(n,k=1): return complex(math.cos(2*math.pi*k/n), math.sin(2*math.pi*k/n))
def ev(expr):
    expr=expr.replace(' ','').replace('\n','')
    if expr=='': return 0j
    tot=0j
    for term in expr.replace('-','+-').split('+'):
        if term=='': continue
        m=re.fullmatch(r'(-?\d*)\*?E\((\d+)\)(?:\^(\d+))?',term)
        if m:
            cs,ns,ks=m.groups()
            coef=1 if cs in ('',None) else (-1 if cs=='-' else int(cs))
            tot+=coef*E(int(ns),int(ks) if ks else 1)
        else: tot+=complex(float(term),0)
    return tot
def split_top(s):
    inner=s[1:-1]; parts,depth,cur=[],0,''
    for c in inner:
        if c=='(': depth+=1;cur+=c
        elif c==')': depth-=1;cur+=c
        elif c==',' and depth==0: parts.append(cur);cur=''
        else: cur+=c
    parts.append(cur); return parts
blk=open('output/irr_S63.txt').read()
rows=[];depth=0;start=None
for idx,c in enumerate(blk):
    if c=='[':
        if depth==1: start=idx
        depth+=1
    elif c==']':
        depth-=1
        if depth==1 and start is not None: rows.append(blk[start:idx+1]);start=None
full=[];prev=None
for r in rows:
    if r.startswith('[GALOIS'):
        # conjugate of prev; handle E(13) pair via k->2k
        er=prev
        if any('E(13)' in p for p in er):
            def gal(p):
                # apply k->2k to E(13) terms only: re-eval by string transform is messy; do numeric via ev on rewritten expr
                import re as _re
                def sub(m):
                    coef,n,k=m.group(1),int(m.group(2)),int(m.group(3) or 1)
                    if n==13: k=(2*k)%13 or 13
                    return f'{coef}E({n})^{k}'
                return ev(_re.sub(r'(-?\d*)\*?E\((\d+)\)(?:\^(\d+))?',lambda m: (m.group(1) or '')+'E('+m.group(2)+')^'+str(((2*int(m.group(3) or 1))%13) or 13) if int(m.group(2))==13 else m.group(0), p))
            full.append([gal(p) for p in er]); prev=er
        else:
            full.append([ev(p).conjugate() for p in er])
    else:
        er=split_top(r); full.append([ev(p) for p in er]); prev=er
print('rows',len(full))
degs=[round(r[0].real) for r in full]
for g in range(74):
    S=sum(r[g]**3/r[0].real for r in full)
    if abs(S)<1e-6:
        print(f'class {g+1}: S={S}  ZERO')
print('done; extrema:')
Ss=[sum(r[g]**3/r[0].real for r in full) for g in range(74)]
for g in sorted(range(74),key=lambda g:abs(Ss[g]))[:8]:
    print(f'class {g+1}: |S|={abs(Ss[g]):.4g} S={Ss[g]}')
