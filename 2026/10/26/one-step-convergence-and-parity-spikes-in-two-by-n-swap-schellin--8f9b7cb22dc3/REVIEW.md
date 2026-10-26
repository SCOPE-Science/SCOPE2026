# Mathematical review

## Correctness
**PASS.** The classification is proved by an exhaustive partition into the three possible red counts on the two-vertex side. A profitable move from either monochromatic small side exists precisely when the large side has at least two agents of the opposite color and its composition is not exactly half-and-half. The destination payoff of each participant is explicitly recomputed; every such move makes the small side mixed, ruling out further improvements. Disjoint binomial cases establish the full polynomial; elementary factorial identities and Stirling's formula give the two sharp stability spikes and parity asymptotics. Independent finite enumeration in `verify.py` matches the full claim for all colorings through ten large-side vertices and separately checks rational identities for even sizes through 98. No finite check is invoked to prove the general statement.

## Originality
**PASS, with stated uncertainty.** The inspected 2022 single-peaked swap paper uses closed neighborhoods, while the present theorem requires open neighborhoods; its existence and welfare theorems do not entail the enumerator, one-step convergence, or conditional population stability spikes here. The inspected 2019 swap paper uses open neighborhoods but monotone preferences. Literature and mathematical-record searches under alternative formulations identified no directly covering theorem. The closest own result concerns balanced \(K_{m,m}\), including the small \(K_{2,2}\) boundary; it cannot imply the asymmetric \(K_{2,n}\), \(n\ge3\), population spike or one-step classification. Equivalence with a less-indexed formulation remains an open bibliographic risk.

## Mathematical value
**PASS.** This is a complete equilibrium and improvement-dynamics classification for an infinite, structurally natural network with two small-side hubs interacting with a large population. The conditional equilibrium fraction has two macroscopic one-agent imbalance peaks (limit \(3/4\)) straddling a lower perfectly balanced fraction (limit \(1/2\)), a sharp nonmonotonic comparative-statics phenomenon invisible in existence-only and worst-case integration results. The parity-sensitive unconditional correction and the exact fixed-composition enumerator support quantitative studies of randomly mixed residential assignments.

## Scope and residual risk
The classification applies to strict bilateral swaps, identical symmetric peak-half utility, fully occupied and labeled \(K_{2,n}\) graphs, open neighborhoods, and \(n\ge3\). It does not claim convergence under non-strict swaps, asymmetrical utility shapes, other network classes, or independent verification. Search coverage cannot certify global bibliographic uniqueness.

Self-review: passed. Independent audit: not yet performed.
