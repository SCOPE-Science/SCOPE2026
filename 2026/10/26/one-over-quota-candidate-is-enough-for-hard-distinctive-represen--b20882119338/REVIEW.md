# Independent mathematical audit

## correctness

PASS

DR means JR plus every elected candidate has exactly q=ceil(n/k) supporters. When all supports <=q and at least k candidates have q supports, greedily maximize pairwise disjoint q-support hyperedges: size <= floor(n/q)<=k. Padding with distinct q candidates preserves JR because every nonselected q-support intersects the maximal packing and hence a represented voter, and smaller supports cannot cause JR failure. For NP-hardness from X3C |U|=3t, make four copies of U and common d; n=12t+1, k=4t, q=4. Each ordinary candidate is T_j union {d}, exception e all 12t element voters without d. Every selected DR member ordinary; d represented, so only e blocks and requires >=4 uncovered element voters. YES exact covers in each copy cover all. In NO X3C, any allocation s_1+...+s_4=4t leaves >=4 uncovered: deficit B=0 has four copies with t sets each missing >=1, B=1 has one t-1 copy missing >=3 plus two t copies missing >=1, B>=2 has >=3B>=6. Thus exact iff, NP membership straightforward. Independent exact direct-JR committee enumeration tests on YES/NO instances; infinite hardness from reduction.

## originality

PASS

Compared exact statements and implications with same-object original papers, published related mathematical records, and alternatives. The exact one-exception promise is not inherited from the source result and its sharp separation is a substantive new combinatorial construction. Residual historical priority and access risk explicitly retained.

## value

PASS

A sharply motivated computational-complexity boundary: without oversized support, DR is always constructible when enough candidates meet quota, but one almost-universal overquota candidate suffices for NP-completeness even with all others 4-supported sharing a voter. This is structurally restricted hardness, not routine unrestricted NP-completeness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
