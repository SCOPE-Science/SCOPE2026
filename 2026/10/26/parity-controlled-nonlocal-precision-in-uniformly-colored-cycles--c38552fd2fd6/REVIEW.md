# Scientific review: Parity-controlled nonlocal precision in uniformly colored cycles

## Correctness
**PASS.** The claim is for every integer \(n\ge3\), \(q\ge3\), with one precisely named singular case. The color-transition matrix \(J_q-I_q\) gives exact marked first and second moments; the cyclic Green-kernel identity and the Sherman–Morrison formula give the inverse. The proof independently checks the unique singularity and strict signs of both adjacent and nonadjacent entries, including the small exceptional boundaries. A standalone exact-arithmetic checker independently enumerated finite samples and verified all claimed finite instances: 6,605 assertions passed. Finite testing is corroboration, not the proof of the infinite quantifier.

## Originality
**PASS, with historical-priority uncertainty.** The earliest motivating source is Chen–Liu–Mani–Moitra, arXiv:2304.01954 (first public 2023-04-04), concerning spatial mixing and influence of random proper colorings; it neither states the present finite-cycle, one-color covariance inverse nor determines its parity signs. Turban, arXiv:1701.09058, computes different Potts-chain two-point functions but not the inverse covariance or this zero-temperature proper-coloring model. Chang–Shrock, arXiv:cond-mat/0404373, gives cyclic-strip chromatic transfer matrices rather than the one-color precision classification. Prior mathematical-result searches found related precision calculations in random permutations, occupancy, and restricted graph orientations, none of which implies this cycle-coloring result. Standard transfer-matrix and circulant identities are fully credited. An older implicit inversion or unindexed graphical-model calculation remains possible.

## Mathematical value
**PASS.** Collapsing a categorical proper coloring to the occupancy indicator for one color is a natural observation model in statistical mechanics and statistics. The precision matrix, unlike the original local color constraint, has weak but nonzero interactions between all nonneighbors. Their signs are completely determined by cycle parity, with a unique rank-deficient boundary and an exact exponential magnitude. This supplies a full all-parameter conditional-linear-dependence classification rather than a single numerical moment or a routine finite table. Partial correlations are explicitly distinguished from conditional independence.

## Evidence and limitations
The exact formula and proof are in RESULT.md, the self-contained rational checker is `verify.py`, and all checks and boundaries are explained in VERIFICATION.md. This is a finite-cycle theorem for uniform proper colorings and does not address weighted color classes, non-Gaussian conditional independence, or general host graphs. Priority is not guaranteed by search results, and the scientific review is not independent.

Self-review: passed. Independent audit: not yet performed.
