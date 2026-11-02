# Self-review

## Correctness

**PASS.** The theorem concerns arbitrary real reports in \(\mathbb R^2\), including coincident locations. The proof separately handles zero-optimum profiles; for even sizes the \(\ell_1\) comparison gives factor \(2\); for odd sizes a four-quadrant nonnegative dual-certificate argument proves the sharper \(2n/(n+1)\). The certificate correctly counts strictly positive coordinates separately, at most \((n-1)/2\) each, and handles \(t=0,1\) and reports on both axes. Three-location examples attain every bound. The proof is analytic, and exact-rational verification reproduces its small cases; exhaustive finite tests are not used as an infinite proof.

## Originality

**PASS, with residual unindexed-priority risk.** Hastings, arXiv:2606.12187, proves the sharp asymptotic/population-uniform factor \(2\), with explicit limiting lower-bound examples. That result is compatible with—and does not imply—the sharp strict improvement for each fixed odd population. The published Euclidean \(n\)-dependent formula of Goel and Hann-Caruthers concerns a different per-agent norm, so it does not cover the Chebyshev-plane claim. Lin, arXiv:2610.36613, treats exact optimization and the uniform Chebyshev factor \(2\), without stating the finite odd-case constant in the inspected full text. Semantic and phrase searches found no exact equivalent, but absence of a match is not proof of priority. Earlier records on randomized multility facility mechanisms have different objects.

## Mathematical value

**PASS.** The new exact \(n\)-dependent guarantee resolves a structural ambiguity in the known sharp \(2\) benchmark. In particular, it shows a parity discontinuity: doubling an odd population preserves the same reported data ratio and makes even-population factor \(2\) attainable, while at fixed odd size the barrier is strictly below \(2\). Exact attainment, the real-domain proof and a closed-form optimal cost checker make this useful as a benchmark for deterministic strategyproof facility rules and finite-population guarantees.

## Closest literature and limitations

The sources are Hastings (arXiv:2606.12187), Goel–Hann-Caruthers (arXiv:2007.00903), and Lin (arXiv:2610.36613). The result is not a general lower bound for all strategyproof mechanisms, and does not extend by this proof to higher dimensions, nonunit weights, or multiple facilities. The latter Lin source was released after the initiating-source cutoff and was used for comparison only. An independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
