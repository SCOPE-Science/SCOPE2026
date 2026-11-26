# Independent mathematical audit

## correctness

PASS

A rank-five symmetric complex matrix admits C=XBX^T with X of full column rank and B invertible symmetric. For |I|=5, det C[I]=det B (det X_I)^2, so nonzero minors are exactly the bases of the row matroid. Every principal 3-minor is 2c_ij c_ik c_jk≠0, hence there is no row circuit of size ≤3. The dual is rank two; its hyperplanes consist of the loops together with one nonloop parallel class, so all class sizes satisfy a_j≤t−4 for t nonloops. Thus 5≤t≤7, and the number of dual bases is the number of cross-class nonloop pairs. Enumerating bounded partitions gives 1, 4 and 8 patterns for t=5,6,7. Separately verified the supplied integer matrices without running the supplied checker: exact nullspaces gave rank and the dual class data (the kernel is the relation space of X^T); exact principal determinants independently confirmed all thirteen patterns and count set {10,12,13,14,15,16,17,18,19,20,21}. The factor interpretation is the order-five layer of the published product formula, not an ML-degree conclusion.

## originality

PASS

The principal determinant, standard symmetric factorization and rank-two matroid counting are known ingredients. The distinct content is the exhaustive order-five spectrum on the d=7 rank-five locus, including realizability of all thirteen admissible dual patterns by dense hollow symmetric matrices. Inspected papers cover rank-three constructions or stratifications through d≤6, not that realizability issue. A rank-two matroid realized abstractly by vectors need not thereby be the dual of a hollow symmetric scaling of the specified rank.

## value

PASS

On rank five the highest potentially nonzero principal-determinant layer is order five. Its support count is therefore a natural statistic of these scaling strata, not a randomly chosen subset of factors. A sharp hole at eleven and full realization of all compatible dual patterns give useful exact constraints on a dimension just beyond the published d≤6 classification. No claim is made that this computes ML degrees or the whole stratification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
