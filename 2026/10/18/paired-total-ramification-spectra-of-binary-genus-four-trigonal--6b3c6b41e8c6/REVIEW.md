# Mathematical assessment

## Correctness — PASS

The total-ramification criterion is exact: a rational fibre of a degree-three projection is triple at one geometric point exactly when its restricted binary cubic is a cube of a rational linear form; the only three nonzero cubes over \(\mathbf F_2\) have coefficient masks \(1,8,15\). The universal sharp bound has a separate exhaustive obstruction: \(1128\) candidate masks with at least four total fibres, \(1110\) singular at rational points, and the remaining orbit of \(18\) singular at an explicit \(\mathbf F_4\)-point. The full table follows from exhaustive enumeration, \(49515\) independently rechecked singular witnesses and \(1008\) exact Gröbner unit ideals on four charts of all \(252\) orbits. Direct coefficient counts equal the orbit-size-weighted totals. Both equal-zeta forms pass the geometric checks and have verified point counts. Risks are implementation error and finite certificate replay; all scripts and certificates are included. Limited-extension negative tests alone are not used to certify smoothness.

## Originality — PASS (with priority risk)

Xarles (arXiv:2007.07822) completely enumerates all genus-four curves over \(\mathbf F_2\), but the inspected full paper and public Magma code address isomorphism classes and point-count data, not simultaneous total ramification of the two trigonal pencils. Looijenga (arXiv:2211.09941) studies genus-four trigonal discriminants over the complex numbers and identifies the two pencils, without finite binary ramification-profile counts. Meaning-based published-record searches for paired trigonal ramification, all six numerical classes, and stronger classifications found no equivalent claim. Importantly, absence of a hit is not proof of novelty. The unindexed or unpublished postprocessing of known curve equations remains a priority risk. The accepted contribution is **only** the paired ramification theorem and its six-stratum profile and sharp obstruction, not a reclassification of the curves already counted by Xarles.

## Value — PASS

Two intrinsic degree-three maps arise from the canonical split quadric, so simultaneous ramification is a natural geometric invariant, directly tied to ramification divisors and trigonal discriminants. The sharp inequality \(t_1+t_2\le3\) cuts the naive maximum of six rational fibres in half, and the complete six-profile classification resolves which patterns actually occur; counts are given both by equations and by abstract isomorphism classes. Moreover, two smooth curves with identical Weil numerator have different paired profiles, proving this is genuinely finer than the published zeta-point-count classifications, not merely a reformatting of them. The classification is specialized to \(\mathbf F_2\); no broad characteristic theorem is asserted.

Self-review: passed. Independent audit: not yet performed.
