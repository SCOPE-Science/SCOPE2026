#!/usr/bin/env python3
"""Reproduce full stable point-line color classes after a projective quadrangle."""
from collections import Counter, defaultdict
from field_plane_verify import plane, refine
for p in (2,3,5):
    q=p*p
    F,P,adj=plane(q);n=len(P)
    frame=[P.index(a) for a in ((1,0,0),(0,1,0),(0,0,1),(1,1,1))]
    nc,iterations,color=refine(adj,frame)
    cells=defaultdict(list)
    for i,c in enumerate(color):cells[c].append(i)
    spectrum=Counter(len(v) for v in cells.values())
    expected={1:2*(p*p+p+1),p*(p-1):2*(p*p+p+1)}
    if p==2: expected={1:14,2:14}
    assert dict(spectrum)==expected,(p,spectrum,expected)
    assert nc==4*(p*p+p+1)
    # The rational point-line subplane is characterized by canonical coordinates in F_p.
    rational={i for i,x in enumerate(P) if all(a<p for a in x)}
    assert len(rational)==p*p+p+1
    for i in range(n):
        rational_incident=[j-n for j in adj[i] if j-n in rational]
        assert (len(rational_incident)==p+1 if i in rational else len(rational_incident)==1)
        if i not in rational:
            L=rational_incident[0]
            class_external=[x for x in range(n) if x not in rational and n+L in adj[x]]
            assert len(class_external)==p*(p-1)
            assert {color[x] for x in class_external}=={color[i]}
    print(f'p={p} q={q} vertices={2*n} colors={nc} singleton={spectrum[1]} nonsingleton={spectrum[p*(p-1)]} external_class_size={p*(p-1)} rounds={iterations}')
print('VERIFY_OK')
