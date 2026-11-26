# Independent mathematical audit

## correctness

PASS

The incidence operator is projectively equivariant, so the displayed rotation and reflection give the full visible subgroup of order 24. An independent exact reconstruction confirms 66 distinct starting points, 49 rich lines, the stated census, and the six line orbits with singleton z=0. It also gives an alternative upper bound over C: the unique twelvefold point is the origin P, and the twelve sevenfold points lie on the smooth conic x²+y²=(2+√3)z². Any stabilizer preserves this conic (two distinct conics cannot share twelve points on a smooth conic) and fixes P, so it preserves the polar of P, namely z=0. In affine coordinates it is therefore linear and preserves x²+y². A chosen sevenfold point has at most twelve images; fixing its nonisotropic vector leaves only the two possible signs on its one-dimensional orthogonal complement. Thus there are at most 24 projectivities, with no restriction to real or rational projectivities. Replay: python3 /workspace/replay/dodecagon.py (SymPy, exact quadratic field); it derives incidence multiplicities from pair counts and computes the orbits under the two generators, not by executing the submitted checker. No claim about abstract lattice automorphisms.

## originality

PASS

The construction, census, rigidity and inherited dihedral action are inputs, not the distinct claim. The inspected comparisons do not establish the upper bound on the complex projective stabilizer or the exact line orbits for this realization.

## value

PASS

For a rigid free arrangement built from a regular polygon it is natural to ask whether the construction has projectivities not inherited from the polygon. The upper bound answers exactly that question over C, and the orbit list gives the precise equivariant decomposition of its components, not simply the order of a visible subgroup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
