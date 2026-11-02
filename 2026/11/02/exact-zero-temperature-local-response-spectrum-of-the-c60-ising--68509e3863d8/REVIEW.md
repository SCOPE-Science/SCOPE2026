# Scientific assessment: exact zero-temperature local-response spectrum of the C60 Ising antiferromagnet

## Correctness — PASS

The graph is constructed explicitly as the truncation of the icosahedral graph; no external coordinate conventions are assumed. Each of its 12 disjoint pentagons must contain an unsatisfied bond. Equality at the sharp lower bound \(-66J\) forces precisely one such bond in each pentagon and none on the 30 cross-pentagon edges. Hexagonal-face parity gives a bijection between minimum-frustration patterns and an icosahedral perfect matching with six independent binary face choices. A complete 125-matching recursion yields exactly 8,000 patterns, or 16,000 spin states after global inversion. Each matched pair of pentagons contributes opposite net spins, proving total magnetization exactly zero state by state.

The integer covariance reduction \(B=X^TX/32\) and \(U^TU=2I\) are explicit. The standalone exact checker establishes the square-free annihilating polynomial and five exact rational kernel dimensions \(11,5,4,4,6\), which completely determine the 30 positive eigenvalues; the remaining 30 are zero. It also checks all 1,770 unordered site-pair correlations. Finite enumeration is exhaustive **only because the preceding matching/parity proof establishes coverage**; the numerical outputs alone do not prove that coverage. No finite-precision fitted eigenvalues are used.

## Originality — PASS on examined evidence, provisional

The 16,000-state degeneracy and the C60 Ising model were established well before this calculation. Rasetti and Regge (1981), Samuel (1993), and Dai and Xu (2024) are acknowledged specifically. Dai and Xu's accessible main text addresses entropy and reports the known 16,000 count; it does not present the 60-by-60 covariance eigenvalue factorization. Konstantinidis (2006) and Rausch, Plorin and Peschke (2020) study continuous classical-vector or quantum Heisenberg models, not the two-valued zero-field Ising covariance operator. Searches of scholarly and indexed research claims found no matching exact 30-nonzero-mode Ising covariance spectrum.

The most important remaining priority risk is the unavailable full text of Samuel's exact 1993 Ising solution and Rasetti–Regge's earlier Pfaffian analysis. Their exact partition-function work might, with a more general local-source formulation, imply the spectrum. Metadata and accessible descriptions alone cannot prove absence of an implicit derivation. The novelty assessment is therefore limited to the inspected claims and material; it is not a claim of independent historical certification.

## Mathematical value — PASS

For a physically motivated 60-spin frustrated cluster, the *full local-field susceptibility* is a natural response invariant, not a contrived statistic. The theorem determines exactly which 30 field combinations have nonzero leading Curie response and which 30 are silent. It gives a nontrivial algebraic spectrum with golden-ratio splitting, shows why the uniform-field response is silent despite extensive entropy, and supplies exact spatial correlations against which numerical and quantum-approximation methods can be benchmarked. These results are not a routine reading of the pre-existing degeneracy count. No thermodynamic-limit or experimental prediction is claimed.

## Scientific limitations and prior comparisons

All assertions require a homogeneous, zero-field, classical, nearest-neighbor Ising model on the finite C60 truncated-icosahedral graph. Local response is the derivative at zero field *before* the zero-temperature limit. Graph disorder, extra interactions, quantum spins, finite-temperature corrections and large-size limits remain unproved. The result provides eigenvalue multiplicities and exact arithmetic certificate, not an explicit closed-form real-space eigenbasis. Source priority remains provisional in view of inaccessible early Ising texts.

Self-review: passed. Independent audit: not yet performed.
