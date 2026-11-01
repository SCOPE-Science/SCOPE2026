# Self-review

## Correctness — PASS

The theorem quantifies over every integer complex dimension \(d\ge1\), every positive integer shell count \(q\), and all strictly ordered positive finite shell endpoints. The Gamma\((n+d,1)\) diagonal integral and its integration-by-parts first difference are exact, including factorial normalization and homogeneous-degree multiplicities. A self-contained generalized Descartes induction gives at most \(2q-1\) zeros of the endpoint exponential sum. The sign sequence starts positive at exponent zero and ends negative, which limits positive-to-negative crossings to \(q\), including any one-sided peak at degree zero. The fixed-mass sharpness argument uses a finite base interval and \(q-1\) widely separated large-radius intervals; each distant logarithmic mean lies strictly between consecutive integers, with Stirling-based domination of cross-shell contributions. This proves strict peaks rather than numerical or nonstrict ones. A standalone SciPy checker passed 422 finite comparisons; finite tests do not replace the theorem.

## Originality — PASS with historical-priority risk

Dewage and Ólafsson (arXiv:2107.01465), Section 2, supply radial Gaussian-Fock Toeplitz diagonalization, but not the fixed-mass sharp multiring peak count. Rozenblum and Vasilevski (arXiv:2203.04170), Section 3, give Bergman radial spectral transforms rather than an all-dimension Fock shell-count law. The classical variation-diminishing/Descartes principle already implies the *upper bound* once combined with known radial diagonalization; originality therefore rests particularly on the complete sharp Fock-geometric interpretation and its constructive attainment at **every prescribed positive Gaussian mass**, which was not found in compared works. The closest separate spectral staircase result concerns a harmonic Bergman trace on one circle, not analytic Fock localization on multiple annuli. Exact prior coverage in older total-positivity applications remains possible and needs independent priority review.

## Mathematical value — PASS

The number of disjoint radial observation components is an exact upper bound on spectral complexity by angular momentum, regardless of complex dimension or total observation probability. The fixed-mass saturating construction makes the invariant sharp under a natural resource constraint, distinguishing geometric spectral complexity from total mass and giving a precise design limit for multimodal radial localization. This is not a reparameterization of a single special example: it settles all finite shell counts and all nontrivial masses. It does not assert a general theorem for arbitrary observation geometries.

## Literature and limitations

Primary scientific sources: V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols* (arXiv:2107.01465), and G. Rozenblum and N. Vasilevski, *Commutative algebras of Toeplitz operators on the Bergman space revisited* (arXiv:2203.04170). The kernel and spectral formulas are prior art; the exact sharp finite-shell profile is the evaluated contribution. Related radial harmonic-Fock work was not fully available for inspection, although its underlying space is different. Remaining risks include historical-priority overlap and the absence of independent proof review. The proof is restricted to positive indicator masks of finitely many separated radial shells.

Self-review: passed. Independent audit: not yet performed.
