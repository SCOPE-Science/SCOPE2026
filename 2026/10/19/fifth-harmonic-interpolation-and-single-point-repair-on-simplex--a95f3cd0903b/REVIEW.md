# Scientific review

## Correctness
PASS. The source-domain normalization and zonal addition formula produce the unit-diagonal degree-five Gram kernel. A Newton-binomial expansion on the Johnson scheme yields all four exact rational sector eigenvalues. Three complete modular residue lists rule out every other integer singularity, not just those checked experimentally. At the exceptional order the Gram nullspace is exactly the constant vector. The harmonic polynomial \(H_{27}\) has zero values on the old sampling orbit and nonzero values on all original simplex vertices, establishing independence of the replacement row. `VERIFY.py` independently rederives the identities and checks small Gram matrices and the singular case. Boundary \(m=6\) is explicitly excluded.

## Originality
PASS under the comparisons recorded in `AUDIT.json`, with residual risk. Dai–Xu's addition theorem and Burcroff's general Johnson-matrix eigenvalue formula provide substantial background and some directly applicable computational ingredients; neither inspected source states the arithmetic \(m=27\) failure, the precise all-integer rank classification, and the single-vertex replacement theorem. The new construction of a degree-five harmonic separating the replacement sample goes beyond the Johnson-scheme orbit spectrum. Related cubic **edge-centroid** results do not imply the quintic **triangle-centroid** classification. Older association-scheme and spherical-design literature may contain an equivalent result, and the general formula makes implicit derivability a material originality caveat.

## Mathematical value
PASS. Identifying the unique high-dimensional failed interpolation order, the exact codimension-one data constraint, and a deterministic one-sample repair addresses sampling identifiability on a natural group orbit. It is not simply one more numerical rank: the conclusion holds uniformly for every integer \(m\ge7\), the exceptional nullspace is explicitly interpreted, and a concrete harmonic separates the replacement vertex from the entire old measurement span. No downstream theorem beyond the stated setting is claimed.

## Limits
The argument proves the listed full-orbit and one-point-replacement conclusions only. Generic Johnson spectral identities are prior art. The oldest foundational design paper was located bibliographically but not inspected in full; an implicit prior version of the exceptional calculation cannot be excluded. Numerical tests are not relied on for infinite claims.

Self-review: passed. Independent audit: not yet performed.
