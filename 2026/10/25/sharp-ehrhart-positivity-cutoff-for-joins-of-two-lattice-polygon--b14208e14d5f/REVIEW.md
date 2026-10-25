# Scientific review: joins of lattice polygons

## Correctness — PASS

The domain is the height-one standard lattice join of full-dimensional rank-two lattice polygons. Pick's theorem yields the factor numerators \(1+az+bz^2\) with \(a-b=B_P-3\ge0\), and likewise for the second factor. Multiplying known Ehrhart series and expanding the five-dimensional binomial basis gives the exact linear and quadratic sign numerators \(U,V\). The remaining nonconstant coefficients have manifestly positive expressions. The normalized volume is \(NM=(a+b+1)(c+d+1)\). Bounding all admissible polygon Pick-data within an explicitly larger integer domain allows an exhaustive **finite** check, not a statistical sample: exact minima of \(U,V\) over \(NM<168\) are \(5,45\), and the unique nonpositive state through \(168\) occurs at \((12,14,0,0)\). The latter has explicit realizations, and the separate quadratic-only example has been checked independently by convolution. The standalone checker was executed successfully from its actual supplied source.

## Originality — PASS under inspected evidence

The June 2026 Liu–Tao–Xin article already proves the generic Ehrhart-series product and shows non-preservation for joins, including a large-cube/interval example; none of those identities is claimed original. Its inspected Proposition 1.2, Theorem 2.3 and Example 2.4 do not give the two-polygon coefficient criterion, normalized-volume cutoff or first-failure uniqueness. The October 2026 article on operations also gives generic join laws and recites the same counterexample; its Section 3 does not provide this quantitative all-two-polygon classification. Historical overlap searches for polygon joins, sharp normalized area, first counterexamples and the value \(168\) found no equivalent result. The algebraic criterion follows by specialization and expansion of prior generic formulas; the new contribution is particularly the sharp integer optimization, its realized equality case and independent sign-pattern realization. Remaining priority risk: an equivalent small-volume calculation could be published under alternative language or in an unindexed table.

## Mathematical value — PASS

The natural question is how far Ehrhart positivity persists for the **smallest equal-dimensional nonscalar factors** in the join operation after its general failure was established in 2026. The result gives an exact all-parameter sign criterion and a finite, sharp geometric-size cutoff with a first counterexample and unique Ehrhart data. The quadratic-only construction shows there are two independent failure mechanisms, providing more information than a generic non-preservation observation. The exact volume threshold is specific to this naturally motivated class, and no unwarranted global minimality claim is made.

## Closest literature and limitations

The principal comparator is Liu–Tao–Xin, arXiv:2606.18794v1, Proposition 1.2 and Section 2. The next closest is Liu et al., arXiv:2610.06338v1, Section 3, which summarizes the prior counterexample. Both articles provide essential known input; neither inspected portion supplies the cutoff. The proof requires the standard lattice join and full-dimensional lattice polygons. The finite bound was verified on a superset of realizable polygon data, so neither arbitrary higher-dimensional joins nor nonstandard lattice structures are covered. Independent evaluation and historical priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
