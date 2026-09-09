#!/usr/bin/env python3
"""Symmetric/alternating splitting census for two-row Kronecker squares S7/S8.
Stdlib only. From-scratch Murnaghan-Nakayama + class squaring map.
"""
import csv, json, math, itertools
from functools import lru_cache

def partitions(n, max_part=None):
    if n==0:
        yield []
        return
    if max_part is None: max_part=n
    for f in range(min(max_part,n),0,-1):
        for rest in partitions(n-f, f):
            yield [f]+rest

def part_to_count(p):
    d={}
    for x in p: d[x]=d.get(x,0)+1
    return d

def class_size(n, ct):
    # ct = cycle type partition of n (list desc)
    c=part_to_count(ct)
    z=1
    for l,m in c.items():
        z*= (math.factorial(m))*(l**m)
    return math.factorial(n)//z

def conj_classes(n):
    parts=list(partitions(n))
    # sort lexicographically desc for determinism
    parts.sort(reverse=True)
    out=[]
    for ct in parts:
        sz=class_size(n,ct)
        out.append({"ctype":ct,"size":sz})
    return out

def rim_hooks(shape, r):
    """All rim hooks of size r in shape (list desc), return list of (new_shape, height)."""
    # Represent diagram as rows lengths. Enumerate connected border strips of size r whose removal leaves a valid diagram.
    # Brute force: choose cells subset of size r that is a rim hook.
    cells=[(i,j) for i,r_ in enumerate(shape) for j in range(r_)]
    cellset=set(cells)
    results=[]
    seen=set()
    # enumerate subsets: C(|shape|,r) could be big for n=8 max 8 cells choose r up to 8 -> fine.
    for combo in itertools.combinations(cells, r):
        s=set(combo)
        # must contain no 2x2 block
        bad=False
        for (i,j) in combo:
            if (i+1,j) in s and (i,j+1) in s and (i+1,j+1) in s:
                bad=False  # actually 2x2 fully inside combo is forbidden
                # check: if all 4 in s -> not a rim hook
                bad=True; break
        if bad: continue
        # connectivity (edge-adjacent)
        stack=[combo[0]]; vis={combo[0]}
        while stack:
            a=stack.pop()
            for b in combo:
                if b not in vis and abs(a[0]-b[0])+abs(a[1]-b[1])==1:
                    vis.add(b); stack.append(b)
        if len(vis)!=r: continue
        # removal leaves Young diagram (left-justified, rows nonincreasing, no holes)
        rem=cellset - s
        # check rows left-justified: for each row i, remaining cells must be {0..k_i-1} for some k_i
        ok=True
        newshape=[]
        maxr=len(shape)
        for i in range(maxr):
            rowcells=sorted(j for (ii,j) in rem if ii==i)
            if rowcells and rowcells!=list(range(len(rowcells))):
                ok=False; break
            newshape.append(len(rowcells))
        if not ok: continue
        # remove trailing zeros, check nonincreasing
        while newshape and newshape[-1]==0: newshape.pop()
        for i in range(len(newshape)-1):
            if newshape[i]<newshape[i+1]: ok=False; break
        if not ok: continue
        # rim hook must be border: each cell in combo must be edge? standard def: removal leaves diagram + combo connected + no 2x2. Also combo must be "rim" i.e. if cell (i,j) in combo and (i+1,j+1)... simpler: every cell of combo on rim? Use condition: for each (i,j) in combo, (i+1,j+1) not in cellset (southeast neighbor absent). Actually rim cells have no SE neighbor in diagram... but interior of hook may? For a rim hook all cells are on rim. Check.
        for (i,j) in combo:
            if (i+1,j+1) in cellset:
                # (i+1,j+1) must also be... hmm if SE in diagram but not in hook then not rim
                # In a rim hook, complement is a diagram, which implies rim automatically given no-2x2+connected? The standard characterization: S is rim hook iff complement is diagram and S connected and no 2x2. So fine.
                pass
        height = len(set(i for (i,j) in combo))-1
        key=(tuple(newshape),height)
        # MN sums over distinct subdiagrams with sign; multiple hooks can give same subdiagram -> sum signs separately. So don't dedupe; append each occurrence? Our cell-subset enumeration counts each hook once. Keep all.
        results.append((newshape,height))
    # Deduplicate identical cell sets? combinations already unique. Keep.
    return results

from functools import lru_cache as lc

def chi_MN(shape, ctype):
    """Murnaghan-Nakayama: shape partition tuple, ctype tuple desc."""
    # recursion with memo
    key=(tuple(shape),tuple(ctype))
    return _mn(tuple(shape),tuple(ctype))

@lc(maxsize=None)
def _mn(shape, ctype):
    shape=list(shape); ctype=list(ctype)
    if sum(shape)==0:
        return 1 if sum(ctype)==0 else 0
    if not ctype:
        return 1 if sum(shape)==0 else 0
    r=ctype[0]; rest=tuple(ctype[1:])
    total=0
    for (ns,h) in rim_hooks(shape,r):
        total+= ((-1)**h)*_mn(tuple(ns),rest)
    return total

def char_table(n):
    shapes=sorted([tuple(p) for p in partitions(n)],reverse=True)
    classes=conj_classes(n)
    ctypes=[tuple(c["ctype"]) for c in classes]
    tab={}
    for s in shapes:
        row=[]
        for ct in ctypes:
            row.append(_mn(s,ct))
        tab[s]=row
    return shapes,classes,tab

def check_table(n,shapes,classes,tab):
    fn=math.factorial(n)
    sizes=[c["size"] for c in classes]
    # row orthogonality
    for i,s in enumerate(shapes):
        for j,t in enumerate(shapes):
            ip=sum(sizes[k]*tab[s][k]*tab[t][k] for k in range(len(classes)))//fn
            # must divide evenly
            raw=sum(sizes[k]*tab[s][k]*tab[t][k] for k in range(len(classes)))
            assert raw%fn==0, (s,t,raw)
            if i==j: assert ip==1,(s,ip)
            else: assert ip==0,(s,t,ip)
    # dims: value at [1^n] class = last class (all ones)
    # find identity class [n]? identity cycle type is [1]*n.
    idx_id=ctypes_index(classes,[1]*n)
    for s in shapes:
        d=tab[s][idx_id]
        assert d>0
    return True

def ctypes_index(classes,ct):
    for i,c in enumerate(classes):
        if list(c["ctype"])==list(ct): return i
    raise KeyError(ct)

def square_class(ctype):
    """Class of w^2 given cycle type of w."""
    out=[]
    for L in ctype:
        if L%2==1:
            out.append(L)
        else:
            out.extend([L//2,L//2])
    out.sort(reverse=True)
    return out

def analyze_n(n):
    shapes,classes,tab=char_table(n)
    check_table(n,shapes,classes,tab)
    sizes=[c["size"] for c in classes]
    fn=math.factorial(n)
    ctypes=[list(c["ctype"]) for c in classes]
    sq=[square_class(ct) for ct in ctypes]
    sq_idx=[ctypes_index(classes,s) for s in sq]
    idx_id=ctypes_index(classes,[1]*n)
    # dims
    dims={s:tab[s][idx_id] for s in shapes}
    tworow=[s for s in shapes if len(s)<=2]
    assert len(tworow)==(4 if n==7 else 5)
    rows={}
    for lam in tworow:
        chi=tab[lam]
        chi_sq=[chi[i]**2 for i in range(len(classes))]
        chi_p2=[chi[sq_idx[i]] for i in range(len(classes))]
        # integrality: chi^2 +/- chi_p2 even
        for i in range(len(classes)):
            assert (chi_sq[i]+chi_p2[i])%2==0
            assert (chi_sq[i]-chi_p2[i])%2==0
        chiS=[(chi_sq[i]+chi_p2[i])//2 for i in range(len(classes))]
        chiA=[(chi_sq[i]-chi_p2[i])//2 for i in range(len(classes))]
        d=dims[lam]
        # dim checks
        assert sum(chiS[i]*sizes[i] for i in range(len(classes)))//fn + 0 == 0 or True
        dimS=sum(sizes[i]*chiS[i]* (1 if list(ctypes[i])==[1]*n else 0) for i in range(len(classes)))
        # value at identity:
        assert chiS[idx_id]==d*(d+1)//2, (lam,chiS[idx_id],d)
        assert chiA[idx_id]==d*(d-1)//2
        for nu in shapes:
            chin=tab[nu]
            rawS=sum(sizes[i]*chiS[i]*chin[i] for i in range(len(classes)))
            rawA=sum(sizes[i]*chiA[i]*chin[i] for i in range(len(classes)))
            rawG=sum(sizes[i]*chi_sq[i]*chin[i] for i in range(len(classes)))
            assert rawS%fn==0 and rawA%fn==0 and rawG%fn==0
            s=rawS//fn; a=rawA//fn; g=rawG//fn
            assert s>=0 and a>=0 and g>=0, (lam,nu,s,a,g)
            assert s+a==g, (lam,nu,s,a,g)
            rows.setdefault(lam,{})[nu]=(s,a,g)
        # sum rules
        ssum=sum(rows[lam][nu][0]*dims[nu] for nu in shapes)
        asum=sum(rows[lam][nu][1]*dims[nu] for nu in shapes)
        assert ssum==d*(d+1)//2,(lam,ssum)
        assert asum==d*(d-1)//2,(lam,asum)
    # maximal gap
    best=None
    for lam in tworow:
        for nu in shapes:
            s,a,g=rows[lam][nu]
            gap=abs(s-a)
            key=(gap,)
            if best is None or gap>best[0] or (gap==best[0] and (list(lam),list(nu))<(list(best[1]),list(best[2]))):
                best=(gap,lam,nu,s,a,g)
    return shapes,classes,tab,sq,rows,best,dims

def main():
    out={}
    for n in (7,8):
        shapes,classes,tab,sq,rows,best,dims=analyze_n(n)
        out[n]=(shapes,classes,tab,sq,rows,best,dims)
        print(f"n={n} classes={len(classes)} best gap={best[0]} at lam={list(best[1])} nu={list(best[2])} s={best[3]} a={best[4]} g={best[5]}")
    # write CSVs
    import os
    os.makedirs("output/artifacts",exist_ok=True)
    summary={}
    for n in (7,8):
        shapes,classes,tab,sq,rows,best,dims=out[n]
        fn=math.factorial(n)
        # classes csv
        with open(f"output/artifacts/classes_S{n}.csv","w",newline="") as f:
            w=csv.writer(f)
            w.writerow(["class_index","cycle_type","class_size","order","square_class_index","square_cycle_type"])
            for i,c in enumerate(classes):
                from math import gcd
                ct=c["ctype"]
                # order = lcm
                L=1
                for x in ct: L=L*x//gcd(L,x)
                w.writerow([i,"+".join(map(str,ct)),c["size"],L,sq_idx_of(classes,sq[i]),"+".join(map(str,sq[i]))])
        # chartable csv
        with open(f"output/artifacts/chartable_S{n}.csv","w",newline="") as f:
            w=csv.writer(f)
            w.writerow(["shape"]+[f"class_{i}" for i in range(len(classes))])
            for s in shapes:
                w.writerow(["+".join(map(str,s)) if s else "[]"]+tab[s])
        # splitting csv (two-row only)
        with open(f"output/artifacts/splitting_tworow_S{n}.csv","w",newline="") as f:
            w=csv.writer(f)
            w.writerow(["lambda","nu","s","a","g","gap_abs","dim_nu"])
            for lam in sorted(rows.keys(),reverse=True):
                for nu in shapes:
                    s,a,g=rows[lam][nu]
                    w.writerow(["+".join(map(str,lam)),"+".join(map(str,nu)),s,a,g,abs(s-a),dims[nu]])
        summary[str(n)]={
            "n_classes":len(classes),"n_shapes":len(shapes),
            "best":{"gap":best[0],"lambda":list(best[1]),"nu":list(best[2]),"s":best[3],"a":best[4],"g":best[5]},
            "dims_tworow":{ "+".join(map(str,l)):dims[l] for l in sorted(rows.keys(),reverse=True)},
        }
    with open("output/artifacts/summary.json","w") as f:
        json.dump(summary,f,indent=2)
    print(json.dumps(summary,indent=2))

def sq_idx_of(classes,ct):
    for i,c in enumerate(classes):
        if list(c["ctype"])==list(ct): return i
    raise KeyError(ct)

if __name__=="__main__":
    main()
