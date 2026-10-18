# Mathematical assessment: finite-return tomography

## Correctness — PASS

The theorem is quantified over every integer dimension \(d\ge2\) and every strictly positive probability vector of coordinate step weights. The exact Fourier–Bessel product generates all even return probabilities; its logarithm produces nonzero coefficients multiplying the power sums of squared weights. Newton identities leave only the constant term of \(\prod_j(t+h_j^2)\) undetermined. The beta-integral representation of \(\sum_j h_j\) is strictly monotone in that constant term, so the normalization fixes it uniquely. Descartes' rule and the implicit-function theorem yield a one-dimensional local ambiguity with one fewer observed return. The first-return decomposition is triangular at every finite horizon, including transient walks.

Exact-rational diagnostics passed 249 checks across dimensions \(2\) through \(8\), including return-generating coefficients, Bessel-log inversion, Newton reconstruction, generic Jacobian ranks and renewal relations. The explicit \(d=3\) witness has equal two-step return but unequal four-step return. These finite checks are supporting diagnostics; the proof is the infinite-dimensional-range argument in `RESULT.md`. No noisy-data stability claim is made.

## Originality — PASS, qualified

The inspected September 2026 primary work of Hsiau–Tsai–Yao studies the exact same walk class and proves **forward stochastic ordering** of first-return times under majorization, not identification from a finite number of return observations. Belmans–Galkin–Mukhopadhyay (October 2026) consider recovery from **all** returns for much more general finite-range supports, proving counterexamples there; even their symmetric square-support weight counterexample does not lie in the present nearest-neighbor cross-polytope family. Zhou (2015) establishes all-return uniqueness on \(\mathbb Z\), not a sharp higher-dimensional finite cutoff. Comparisons of relevant published mathematical records and inverse-spectral aliases did not identify the same finite identifiability and generic optimality theorem. An unindexed earlier implication through symmetric-function identities or inverse spectral moment theory remains a real priority risk. Searches do not certify novelty.

## Mathematical value — PASS

There is an explicit current motivation: finite return observations are natural invariants in the 2026 studies of nearest-neighbor first returns and lattice-walk inverse problems. A known dimension entails \(d-1\) free unordered probabilities; the theorem gives a complete sharp **finite observation threshold**, with an explicit algebraic recovery route and a rigorous impossibility statement for fewer exact observations near generic parameter points. The proof's monotone last-coefficient step is needed: the first \(d-1\) squared-weight power sums alone do not determine \(d\) arbitrary positive numbers until the probability normalization is used. Thus this is neither a restatement of the existing majorization theorem nor a routine numerical recomputation of a table.

## Closest primary literature, limitations, and risks

- Hsiau, Tsai, Yao, *Stochastic dominance of first return times for nearest-neighbor random walks on \(\mathbb Z^d\)*, arXiv:2609.36728, §§1–4: same stochastic process, different forward comparison result.
- Belmans, Galkin, Mukhopadhyay, *Can one hear the shape of a lattice random walk?*, arXiv:2610.08348, §6: larger finite-range models and counterexamples; source's strong symmetric weight non-identifiability has square rather than cross-polytope support.
- Zhou, *Return Probabilities of Random Walks*, arXiv:1512.04142, Theorem 1.1: infinite sequence on the one-dimensional lattice.

Strictly positive weights, known dimension and nearest-neighbor support are essential declared hypotheses. The method does not guarantee numerical robustness near equal weights, detect an unknown support or prove priority against unindexed older material. Independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
