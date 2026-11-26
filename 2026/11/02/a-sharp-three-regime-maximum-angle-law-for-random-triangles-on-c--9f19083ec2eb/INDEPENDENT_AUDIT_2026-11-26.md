# Independent mathematical audit

## correctness

PASS

For ordered arc positions and successive gaps u,v, the simplex density is 6(L-u-v)/L³ and the angles are u/2, v/2 and (2π-u-v)/2. At fixed r=u+v, the width is r-2(r-h)_++(r-2h)_+; impose r≥a=2π-h. Integration gives exactly the stated CDF, including the lower-cut corrections when a>h. Positive density on the connected open gap triangle and continuity of the maximum give the support, with no atoms (each fixed level lies in a union of lines). Substitution at h=π gives the acute law, including its derivative and quadratic onset. The local integrations give numerators 12Lδ²−16δ³, 12(4π−3L)δ²+64δ³, 64δ³, and 108(L−4π/3)δ² respectively, the last exactly for sufficiently small fixed-L δ. The repair checks the actual realizability at L=4π/3 and above. Independent exact-fraction deficit-coordinate comparisons and symbolic local integrations replay with python3 /workspace/review-evidence/reproduce.py 2 (SymPy). The supplied script and recorded outputs were inspected, not executed; neither a mesh nor Monte Carlo proves the law.

## originality

PASS

The supported distinction is the exact fixed-arc maximum-angle law in both variables and its isolated cubic lower edge, not the full-circle marginal, the uniform-spacing primitive, or the equilateral feasibility threshold alone. The strongest catalogue comparators supply the full-circle joint law and the ordered arc density for an area statistic, respectively, but not the short-arc maximum-angle integration or its transition.

## value

PASS

The largest angle is a natural shape statistic of triangles constrained to an observation aperture. The exact two-variable law gives acute probabilities and resolves a nontrivial boundary change: at the minimum aperture supporting an equilateral triangle the gap-area shrinkage and the vanishing ordering weight combine to produce a cubic onset, whereas on either side it is quadratic. That change and the explicit coefficients are useful beyond a full-circle benchmark or the textbook spacing density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
