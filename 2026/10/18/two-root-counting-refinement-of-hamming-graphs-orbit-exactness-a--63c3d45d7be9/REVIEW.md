# Review of the two-root Hamming graph classification

## Correctness — PASS

The claim is uniform in integers \(q\ge2\), \(d\ge1\), and \(1\le t\le d\). The explicit coordinate-permutation and letter-permutation subgroup is transitive on each proposed tuple. The three intrinsic invariants \(u\), \(v\), and \(f\) distinguish every tuple: \(f=\delta\) by the unique simultaneous two-distance-decreasing moves, and the reconstruction formulas recover the other entries. Stable equitable colour classes are homogeneous for distances to the two individually coloured singleton roots and hence for \(f\). Automorphism invariance supplies the reverse refinement inclusion. The metric-pair criterion follows by elementary inversion in the three exact cases and two feasible counterprofiles in every other case. Finite checks were executed from the three supplied scripts: direct graphs, independent quotient transition matrices, and parameter arithmetic. These corroborate but do not replace the all-order proof.

## Originality — PASS, with residual literature risk

Krotov (arXiv:0907.0001) treats perfect colourings and weight distributions, the survey by van Dam–Koolen–Tanaka (arXiv:1410.6294) places equitable two-root distance partitions into the distance-regular context, and Mirafzal–Ziaee (arXiv:1901.07784) derive the Hamming automorphism group. Relevant text was inspected; the inspected statements do not give the two-individualization stable-partition theorem or sharp \(q,d,t\) distance-pair obstruction. Additional claim/alias searches did not reveal an implication from a stronger statement. A specialized earlier description of Hamming two-root equitable partitions remains possible, so no absolute priority claim is made. An earlier classification for **one** distinguished vertex in general Cartesian products does not imply the two-root statement: the second root changes pointwise-stabilizer orbit types and metric pairs.

## Value — PASS

The theorem connects the finite-model-theoretic counting-refinement partition and the group-theoretic pointwise-stabilizer orbit partition for an infinite natural distance-regular family. Its sharp trichotomy separates when two distance measurements suffice from when local equitable refinement genuinely adds information. The explicit orbit counts and sizes are useful quantitative invariants, and the parameter-wide non-equitability witness identifies a structural boundary rather than a routine isolated example.

## Scientific limits

Only uniform Hamming graphs with two distinctly individualised vertices are covered. No optimal round complexity is asserted; experimental checks are finite, and the literature search cannot certify unique publication priority.

Self-review: passed. Independent audit: not yet performed.
