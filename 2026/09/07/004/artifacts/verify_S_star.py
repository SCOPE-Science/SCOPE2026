"""Independent verifier (second code path): brute-force triple loop with sorting + cross-check.
Usage: python3 verify2.py coords.txt
Coords file: one 'x y' per line.
"""
import sys, itertools

def read_pts(path):
    pts=[]
    with open(path) as f:
        for ln in f:
            ln=ln.strip()
            if not ln or ln.startswith('#'): continue
            a=ln.replace(',',' ').split()
            pts.append((int(a[0]),int(a[1])))
    return pts

def main(path):
    pts=read_pts(path)
    n=len(pts)
    assert n==20, f"expected 20 points, got {n}"
    for (x,y) in pts:
        assert 0<=x<=11 and 0<=y<=11, f"point {(x,y)} outside G12"
    assert len(set(pts))==n, "duplicate points"
    n0=n1=0; dmin=None; c2=c3=0
    bad1=[]
    # different order: sorted triple enumeration via indices, det via shoelace form
    for i in range(n):
        xi,yi=pts[i]
        for j in range(i+1,n):
            xj,yj=pts[j]
            for k in range(j+1,n):
                xk,yk=pts[k]
                # shoelace doubled area, different expression order than verify.py
                d=(xj-xi)*(yk-yi)-(xk-xi)*(yj-yi)
                a=d if d>=0 else -d
                if a==0: n0+=1
                elif a==1:
                    n1+=1; bad1.append((pts[i],pts[j],pts[k]))
                elif a==2: c2+=1
                elif a==3: c3+=1
                if dmin is None or a<dmin: dmin=a
    total=n*(n-1)*(n-2)//6
    print(f"n={n} total_triples={total} D={dmin} A={dmin/2} n0={n0} n1={n1} c2={c2} c3={c3}")
    if dmin is not None and dmin>=2:
        print("PASS: D>=2 (no collinear, no unimodular triple)")
    else:
        print("FAIL: D<2")
        for t in bad1[:10]:
            print("  det=1:",t)
    # histogram of small dets
    hist={}
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                xi,yi=pts[i]; xj,yj=pts[j]; xk,yk=pts[k]
                a=abs((xj-xi)*(yk-yi)-(xk-xi)*(yj-yi))
                hist[a]=hist.get(a,0)+1
    small={k:hist.get(k,0) for k in range(0,11)}
    print("hist_0_10:",small)
    assert total==1140
    return 0 if dmin>=2 else 1

if __name__=="__main__":
    sys.exit(main(sys.argv[1]))
