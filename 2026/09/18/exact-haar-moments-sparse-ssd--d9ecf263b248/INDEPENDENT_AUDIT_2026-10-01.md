# Independent audit — SCOPE-20260918-d9ecf263b248

Audit date (UTC): 2026-10-01

## Final claim

For exact-gradient classical stochastic subspace descent on \(f(x)=g(Rx)\) with Haar rank-\(d\) projectors, the compressed-projector second moment is exactly scalar with coefficient \(\theta_{n,s,d}\), yielding the stated unrestricted optimal expected-descent stepsize, stationarity rate, PL contraction, and rank-one constant-stepsize sharpness.

## Correctness

**PASS** — The projector moment was re-derived from the beta second moment of a diagonal Haar projector entry, idempotence for off-diagonal squares, and orthogonal invariance of the compressed block. Exact rational recomputation reproduced \(\theta_{1000,512,32}=264307/500499\) and the rate constant about 33.0054. Substitution into the smoothness inequality gives a concave quadratic in the stepsize whose maximizer is exactly the claimed value; telescoping yields the stationarity bound. The PL step follows immediately, and for a rank-one quadratic the one-step expectation is the same quadratic exactly, proving constant-stepsize sharpness. The source full HTML was inspected and confirms its Theorem 6/8 uses the same intrinsic-dimension model but imposes the logarithmic lower bound, \(d\le s/16\), and coefficient \(36Ls/d\).

## Originality

**PASS** — The beta/projector moments themselves are classical and are not novel. The 2021 stochastic-subspace paper gives general ambient-dimensional convergence theory, while the 2026 source explicitly describes its restricted theorem as the first sparse classical-SSD analysis. No prior source located states the exact compressed second-moment coefficient for this active-subspace descent calculation, the resulting all-\(d\) intrinsic-dimensional rate, or the rank-one sharpness statement. The new theorem is not mechanically implied by the source concentration proof because it replaces its bad-event bound with an exact second moment.

### Equivalent formulations

Aliases, parameter normalizations, and source-specific formulations were compared by implication rather than by title similarity. Exact-title, exact-claim, alias, and primary-literature searches found no equivalent stronger statement beyond the qualifications below.

### Broader coverage

The closest general results and source theorems were inspected directly. General machinery that is prior art is excluded from the novelty claim; none of the inspected broader statements implies the final claim at the stated strength.

### Exact database or table

Finite computations and tables were treated as corroborative evidence only. They were not used to infer an infinite theorem or to establish novelty.

### Claim versus prior implication

The beta/projector moments themselves are classical and are not novel. The 2021 stochastic-subspace paper gives general ambient-dimensional convergence theory, while the 2026 source explicitly describes its restricted theorem as the first sparse classical-SSD analysis. No prior source located states the exact compressed second-moment coefficient for this active-subspace descent calculation, the resulting all-\(d\) intrinsic-dimensional rate, or the rank-one sharpness statement. The new theorem is not mechanically implied by the source concentration proof because it replaces its bad-event bound with an exact second moment.

## Value

**PASS** — The result removes every sampling-dimension restriction from a newly motivated sparse-SSD theorem without changing the algorithm, permits one-dimensional subspaces, improves the source guarantee by at least a factor of sixteen in its own regime, adds a PL rate, and proves a sharpness statement on a natural rank-one family. Those are substantive algorithmic guarantees rather than a known-moment recomputation in isolation.

## Sources inspected

- Gradient Descent with Stochastic Subspaces via Persistence of Memory — https://arxiv.org/html/2609.18416v1 — NOT_COVERING: same sparse classical SSD setting, but uses concentration and imposes the stated lower/logarithmic and upper sampling-dimension restrictions with the weaker coefficient.
- A stochastic subspace approach to gradient-free optimization in high dimensions — https://arxiv.org/abs/2003.02684 — BROADER ALGORITHM BACKGROUND but not covering: gives general random-subspace convergence with ambient-dimensional behavior, not this intrinsic active-subspace exact-moment rate.
- Some geometric applications of the beta distribution — https://doi.org/10.1007/BF00049302 — BACKGROUND: supplies classical beta-distribution geometry; the moment itself is not claimed novel.

## Residual risks and limitations

- The guarantee is in expectation for exact projected gradients with independent Haar subspaces; finite-difference error, stochastic gradient noise, non-Haar sketches, and changing active subspaces are outside scope.
- Originality is best-of-knowledge; exact random-projector moments are classical and a differently phrased active-subspace optimization theorem could reduce novelty.

## Disposition

**PASSED**
