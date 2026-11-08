# Independent mathematical audit

## correctness

PASS

From block multiplication, g(X,Y,Z)^2=g(0,0,XY) in characteristic two; therefore g^2=1 iff XY=0. A rank-r map X:F_q^b→F_q^a has [a r]_q[b r]_q|GL_r(q)| choices, and for each X the rank-s maps Y:F_q^c→ker X have [b−r s]_q[c s]_q|GL_s(q)| choices, exactly N_{r,s} with r+s≤b. Conjugation fixes X,Y and translates Z by A Y−X B. AY spans the a*s-dimensional space of maps killing ker Y; XB spans the c*r-dimensional space of maps with image in im X; the intersection has r*s dimensions. So each orbit has q^(as+cr−rs) elements and q^(ac−d) distinct classes for each (X,Y), yielding K(T). Since d=ac−(a−r)(c−s), d≤ac with equality iff r=a or s=c, feasible exactly for b≥min(a,c); otherwise d≤max(a,c)(r+s)−rs≤b max(a,c), with equality only at (0,b) or (b,0) as described. g^4=1, so the complementary element count is the order-four count. Independently enumerated literal multiplication, inverse, square-one elements and actual conjugacy orbits for 9 complete small groups over F2/F4; every class-size histogram agreed, e.g. (2,1,2,2) has 16 classes of size 1 and 24 of size 4, 112 square-one elements. These finite cases are corroboration, not proof for arbitrary dimensions/fields. The proof explicitly assumes all a,b,c>0, q=2^f≥2 and conjugacy inside G. No missing pole/normalization issue found.

## originality

PASS

Best-of-knowledge originality of the full class-size enumerator on the square-one locus survives a statement-level comparison. Diaconis–Thiem (2006), Example 3 and Corollary 5.1, already gives precisely the same three-block group and affine corner-block orbit; the submitted orbit mechanism by itself is not new. Goodwin–Röhrle (2009/2010) treats total parabolic-radical conjugacy classes and centralizers. Neither inspected primary result gives the Gaussian compatible-rank multiplicity of conjugacy classes of EACH size subject to XY=0 or its sharp b=min(a,c) saturation threshold. The published UT_3(F_{2^f}) order-count is an existing (1,1,1) boundary case, and is excluded from the general novelty claim. Searching does not establish uniqueness, and the implicit-consequence risk from the older orbit description is material.

## value

PASS

A natural finite class-two unipotent family contains elements of order 1,2 and 4 when q is even. Conditional centralizer-index/class-size statistics for the full square-one locus are independent of a total conjugacy-class count and are useful in finite p-group, orbit and representation statistics. The formula is a complete all-parameter size-resolved invariant and the exact b=min(a,c) saturation threshold is structurally motivated by the middle layer bottleneck; extremal multiplicities refine it. The work is short and uses known affine orbit machinery but is not simply a title/parameter renaming, arbitrary finite slice, or known-table recomputation under the inspected sources. It does not claim new orbit theory, general p-group classification, or a larger downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
