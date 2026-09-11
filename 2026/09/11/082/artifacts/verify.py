"""Verifier for lane-1042 real AB transfer at fixed class (2,2)/(2E+4F)/(E+4F).
Asserts: complex AB 12=10+2*1; full Delta3 real table [8,6,4,2,0] with per-shape
rows; target real rows W_F0=(8,6,4,2), W_F2=(6,6,4,2), W_corr=(1,1,1,1);
defect D=(0,-2,-2,-2): transfer holds iff r=0.
Run: python3 verify.py  (needs enumerate.py importable; reruns census live)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enumerate import Diagram, census, E

def row(c, rmax):
    return [c[f'W_r{r}'] for r in range(rmax+1)]

fails = []
def check(name, got, want):
    print(f"{name}: got {got}, want {want} -> {'OK' if got==want else 'FAIL'}")
    if got != want: fails.append(name)

# --- complex + small calibrations ---
c = census(Diagram("F0(2,1)", {'A':0,'B':0},
    [E('e0','A','B',1,'bounded'),E('bA','B','A',1,'bottom'),E('tB','B','B',1,'top')]), 0)
check("cplx F0(2,1)", c['complex_total'], 1)
c = census(Diagram("F0(1,2)", {'A':0},
    [E('b1','B','A',1,'bottom'),E('b2','B','A',1,'bottom'),
     E('t1','A','A',1,'top'),E('t2','A','A',1,'top')]), 0)
check("cplx F0(1,2)", c['complex_total'], 1)
c = census(Diagram("D2", {'A':0,'B':0},
    [E('e0','A','B',1,'bounded'),E('b1','B','A',1,'bottom'),E('b2','B','A',1,'bottom')]), 0)
check("cplx Delta2", c['complex_total'], 1)

# --- Delta3 full real table ---
def chain(bottoms, ws, tag):
    vs=['A','B','C']; es=[E('e1','A','B',ws[0],'bounded'),E('e2','B','C',ws[1],'bounded')]
    n=0
    for i,v in enumerate(vs):
        for _ in range(bottoms[i]):
            n+=1; es.append(E(f'b{n}','B',v,1,'bottom'))
    return Diagram(tag, {'A':0,'B':0,'C':0}, es)
s1 = census(chain((2,1,0),(1,1),"s1"),4)
s2 = census(chain((3,0,0),(2,1),"s2"),4)
fk = census(Diagram("fork", {'A':0,'B':0,'C':0},
    [E('e1','A','C' if False else 'B',1,'bounded'),E('e2','A','C',1,'bounded'),
     E('b1','B','A',1,'bottom'),E('b2','B','A',1,'bottom'),E('b3','B','A',1,'bottom')]),4)
check("D3 s1 complex", s1['complex_total'], 5)
check("D3 s2 complex", s2['complex_total'], 4)
check("D3 fork complex", fk['complex_total'], 3)
check("D3 s1 real row", row(s1,4), [5,5,5,3,1])
check("D3 s2 real row", row(s2,4), [0,0,0,0,0])
check("D3 fork real row", row(fk,4), [3,1,-1,-1,-1])
check("D3 total real row", [s1[f'W_r{r}']+s2[f'W_r{r}']+fk[f'W_r{r}'] for r in range(5)], [8,6,4,2,0])

# --- target classes ---
A = census(Diagram("F0-A", {'A':0,'B':0},
    [E('e0','A','B',1,'bounded'),E('bA','B','A',1,'bottom'),E('bB','B','B',1,'bottom'),
     E('t1','B','B',1,'top'),E('t2','B','B',1,'top')]),3)
B = census(Diagram("F0-B", {'A':0,'B':0},
    [E('e0','A','B',1,'bounded'),E('bA1','B','A',1,'bottom'),E('bA2','B','A',1,'bottom'),
     E('tA','A','A',1,'top'),E('tB','B','B',1,'top')]),3)
Cc = census(Diagram("F0-C", {'A':0,'B':0},
    [E('e0','A','B',2,'bounded'),E('bA1','B','A',1,'bottom'),E('bA2','B','A',1,'bottom'),
     E('t1','B','B',1,'top'),E('t2','B','B',1,'top')]),3)
D = census(Diagram("F2-D", {'A':0,'B':0},
    [E('e0','A','B',1,'bounded'),E('b1','B','A',1,'bottom'),E('b2','B','A',1,'bottom'),
     E('b3','B','A',1,'bottom'),E('b4','B','B',1,'bottom')]),3)
Ee = census(Diagram("F2-E", {'A':0,'B':0},
    [E('e0','A','B',2,'bounded'),E('b1','B','A',1,'bottom'),E('b2','B','A',1,'bottom'),
     E('b3','B','A',1,'bottom'),E('b4','B','A',1,'bottom')]),3)
K = census(Diagram("F2corr", {'A':0},
    [E('b1','B','A',1,'bottom'),E('b2','B','A',1,'bottom'),
     E('b3','B','A',1,'bottom'),E('b4','B','A',1,'bottom'),
     E('t1','A','A',1,'top'),E('t2','A','A',1,'top')]),3)
check("cplx F0", A['complex_total']+B['complex_total']+Cc['complex_total'], 12)
check("cplx F2", D['complex_total']+Ee['complex_total'], 10)
check("cplx corr", K['complex_total'], 1)
WF0 = [A[f'W_r{r}']+B[f'W_r{r}']+Cc[f'W_r{r}'] for r in range(4)]
WF2 = [D[f'W_r{r}']+Ee[f'W_r{r}'] for r in range(4)]
WK = row(K,3)
check("W_F0", WF0, [8,6,4,2])
check("W_F2", WF2, [6,6,4,2])
check("W_corr", WK, [1,1,1,1])
Ddef = [WF0[r]-WF2[r]-2*WK[r] for r in range(4)]
check("defect D(r)", Ddef, [0,-2,-2,-2])
print("TRANSFER holds at r=0 (8 = 6 + 2x1); DIVERGES by -2 for r = 1,2,3" if not fails else "FAILURES PRESENT")
print("VERIFY_" + ("OK" if not fails else "FAILED"))
sys.exit(1 if fails else 0)
