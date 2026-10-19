# Scientific review: circular Hermite Fock sampling

## Correctness — PASS

The proof is self-contained after standard classical identities. In the normalized monomial basis, ordinary derivative evaluation differs from the Euler row only by a unimodular row factor. The confluent Vandermonde determinant yields the precise eighth power of angular chord products; Hadamard's inequality and Newton identities force a regular polygon. Both radial stationarity equations are solved uniquely because truncated exponential-family means are strictly increasing. Fourier reduction produces explicit two-by-two Gram blocks. Exponential Poisson-tail control at radius parameter near \(n\), followed by a second-order log-determinant expansion, proves the limiting squared-determinant ratio \(e4^{-n}\). The included independently assembled matrix calculations pass 45 numerical tests; these are supplemental checks, not the proof.

## Originality — PASS (best-knowledge comparison)

Escudero–Haimi–Romero, arXiv:2004.12922 (first posted 2020-04-27), studies multiple Fock sampling through infinite-dimensional density conditions. Gröchenig–Ortega-Cerdà, arXiv:2109.11825 (first posted 2021-09-24), compares polynomial Fock sampling with infinite-dimensional interpolation families. Inspection of their accessible full articles, including main results and the relevant methodological discussions, did not identify the exact finite common-circle Hermite determinant, its complete Fourier-block spectrum, or the sharp normalized volume comparison. Classical confluent Vandermonde and Fekete facts explain the angular factor but not by themselves the finite-space normalization and the asymptotic constant. The value-only circular optimum is prior related content and is rederived solely as a comparator, not claimed anew. Remaining risk: a comparable derivation may exist in less-indexed Hermite optimal-design literature.

## Mathematical value — PASS

The problem is an intrinsically normalized, fixed-measurement-budget comparison of two natural Gaussian polynomial sampling schemes. Co-locating first derivatives with values does not merely produce a different interpolation basis: the best possible Gram determinant is asymptotically reduced by \(e4^{-n}\), giving an exponentially sharp quantitative cost with exact optimizer geometry, unique radial choices and the entire spectrum. The result informs experimental design and conditioning diagnostics for finite Fock/coherent-state subspaces without claiming stronger noise guarantees.

## Limitations and literature risk

The theorem concerns one common circle and individually normalized derivative-evaluation functionals on a **finite-dimensional** Fock polynomial subspace; it does not classify unrestricted planar configurations, infinite-dimensional sampling, or optimal condition numbers. A classical confluent-interpolation treatment could contain an equivalent formula; this remains a residual originality risk. No independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.
