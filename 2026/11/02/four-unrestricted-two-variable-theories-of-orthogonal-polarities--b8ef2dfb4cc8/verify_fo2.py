"""Independent non-counting two-pebble color-refinement check.
Uses only adjacency matrices from verify_geometry; no geometric types or formulas.
"""
from verify_geometry import PRIME, graph

QS=tuple(PRIME)
Adj={q:graph(q)[1] for q in QS}
color_id={}
def code(m,key):
    if key not in m:m[key]=len(m)
    return m[key]

colors={}
for q in QS:
    A=Adj[q];n=len(A)
    colors[q]=[[code(color_id,(i==j,A[i][i],A[j][j],A[i][j])) for j in range(n)] for i in range(n)]

for depth in range(20):
    next_id={}
    new={}
    for q in QS:
        a=colors[q];n=len(a)
        row=[tuple(sorted(set(a[i]))) for i in range(n)]
        col=[tuple(sorted(set(a[i][j] for i in range(n)))) for j in range(n)]
        new[q]=[[code(next_id,(a[i][j],row[i],col[j])) for j in range(n)] for i in range(n)]
    size=len(next_id)
    print('FO2_STEP',depth+1,'global_colors',size)
    if size==len(color_id):
        colors=new
        break
    colors=new
    color_id=next_id
else:
    raise AssertionError('No fixed point within 20 rounds')

spectra={q:frozenset(c for row in colors[q] for c in row) for q in QS}
for q in QS:
    print('FO2_SPECTRUM',q,'size',len(spectra[q]),'class',('even_small' if q==2 else 'even_large' if q%2==0 else 'odd_small' if q==3 else 'odd_large'))

for q in QS:
    for r in QS:
        got=(spectra[q]==spectra[r])
        want=((q==2 and r==2) or (q==3 and r==3) or (q%2==0 and r%2==0 and q>=4 and r>=4) or (q%2==1 and r%2==1 and q>=5 and r>=5))
        assert got==want,(q,r,got,want)
print('FO2_ALL_PASS','instances',len(QS),'ordered_pairs',len(QS)**2,'depth',depth+1)
