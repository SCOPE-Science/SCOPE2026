# Self-review

## Correctness
PASS. The maximizing-chain proof was reconstructed with the source's exact domains and monotonicity. The two-round threshold \(d_s\), the positivity-implied upper cutoff, the Fagnani--Ravazzi transition inequality, and the count of uniformly negative intermediate transitions yield the stated integer certificate without numerical extrapolation. The near-GV expansion uses only differentiability of \(h_2\) at \(\delta_*\in(0,1/2)\). The code-level resource statement reserves half the target gap for the source's finite-round distance theorem.

## Originality
PASS. The closest source, arXiv:2610.01277v1, explicitly says that it does not characterize the convergence rate. Its proof invokes an unspecified compactness constant; the new statement replaces that constant by \(\eta_s(\gamma)\) and derives a closed sufficient round count. Classical RMA convergence literature and the Brehm--Resch fast-code/fast-dual construction were inspected and do not imply the quantum parity-outer formula found here.

## Value
PASS. The source's main encoder theorem hides target-gap dependence inside an existential number of rounds. The explicit \(O_s(\Delta^{-2/s})\) certificate converts that hidden dependence into a usable guaranteed depth and gate-count law. The constants are conservative, but the result resolves a mathematical gap named by the source rather than optimizing an arbitrary slice.

## Closest literature and limitations
The nearest literature is Zhang's arXiv:2610.01277v1, Ravazzi--Fagnani on classical RMA spectral convergence, and Brehm--Resch on fast codes with fast duals. The new result is only a sufficient upper bound on rounds. It does not establish sharp convergence, a converse, a finite-blocklength threshold, or a decoding guarantee.

Self-review: passed. Independent audit: not yet performed.
