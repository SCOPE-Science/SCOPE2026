# Self-review

## Correctness — PASS

For every positive coupling tuple, direct multiplication of the stated hopping operator gives a half-line Jacobi matrix with boundary diagonal \(u\), interior diagonal \(u+v\), and neighbor coupling \(q\). The square-summable root is forced to \(r=-\overline q/v\), and the boundary eigenvalue is forced to \(\mu=u-c^2/v\). The proof explicitly separates the \(\mu=0\) case, handles \(c=0\) and the critical non-decaying root \(c=v\), and establishes no additional bright surface eigenvalue by rank-one perturbation. For finite \(N\), the resolvent endpoint entry at the infinite-volume lower band edge is exactly \(N/[c(N+1)]\), providing an if-and-only-if *strict* threshold rather than an unproven numerical pattern. The exact small-flux Taylor computation yields a cubic energy gap. An independently assembled physical hopping matrix was tested in 2310 cases, and for small sizes direct full-matrix spectral comparisons agreed. Remaining risk: independent proof review has not occurred.

## Originality — PASS

The source's exact three-arm Hamiltonian and bulk caging bands are established in Brosco–Pilozzi–Conti (2021), and so are **not** claimed as new. The checked original analysis discusses Bloch modes, caging, and finite propagation, whereas the new claim is a complete open-boundary spectral theorem: four-coupling/two-flux existence criteria, an \(N\)-dependent sharp detachment cutoff, a zero-mode collision, and a cubic small-flux energy scale. Kremer et al. (2018) and Mukherjee et al. (2018) already cover relevant two-arm cage edge modes, which are recognized but do not imply the stated three-arm parameter classification. Literature and published research-record searches also considered terminology such as rhombic cages, surface/Tamm/edge states, square-root Hamiltonians, and rank-one Jacobi perturbations. No matching stronger three-arm theorem was found among inspected sources; this is a bounded originality assessment, not a claim that every possible publication was searched. Priority review remains an external risk.

## Value — PASS

The two independent synthetic fluxes were introduced to control interference and caging. Whether finite arrays also support modes outside their propagating bands and how large an array must be for a weak-flux surface signature are natural spectroscopic questions. A sharp \(N\)-dependent critical flux separates finite samples with and without detached surface modes, while a diverging penetration length \(\asymp\phi^{-2}\) combined with a cubic energy separation answers how demanding weak-flux detection becomes. The special zero-eigenvalue collision distinguishes a physically important boundary of the parameter region. These exact finite-size and critical-scale facts have specific value beyond textbook Jacobi computations.

## Closest literature and limits

Brosco, Pilozzi, Conti, arXiv:2102.06682v1, Sections II–IV, is the direct original model; Kremer et al. arXiv:1805.05209 and Mukherjee et al. arXiv:1805.03564 discuss known rhombic-cage boundary modes. The theorem is about linear Hermitian single-particle spectra at the specified cut. No assertion is made about disorder, many-body phases, alternative terminations, or independent novelty certification.

Self-review: passed. Independent audit: not yet performed.
