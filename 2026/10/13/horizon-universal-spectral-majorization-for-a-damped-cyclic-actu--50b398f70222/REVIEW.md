# Scientific assessment

## Correctness — PASS

The stated domain is every \(n\ge2\), every \(0<r<1\), every unit real actuator and every finite \(H\ge n\) or infinite horizon. Cyclic grouping supplies the exact Gramian factorization. The matrix with the same eigenvalues has diagonal equal to the strictly decreasing phase weights, and the Ky Fan variational principle gives majorization; equality is certified by the nonnegative sum-of-squares identity for its Frobenius norm. The determinant follows from Hadamard, the strict worst-case bound from the last orbit column, the inverse-trace minimum from dual-column Cauchy–Schwarz, and the conditioning bound from the two extreme Rayleigh estimates. The Fourier and nonnegative-input characterizations are proved from cyclic autocorrelations. The standalone standard-library rational checker reproduces 108 instances. There is no infinite-case inference from finite enumeration.

## Originality — PASS, qualified

Prior control literature establishes the Gramian, energy objectives, trace modularity, and inequalities used in the proof. The inspected primary sources concern finite subsets of actuated nodes, symmetric/Laplacian circulant networks, or general Gramian bounds. Their claims do not imply the universal spectrum-majorization and **identical optimizer set for all finite/infinite horizons** over the freely oriented unit actuator of a damped one-way cyclic permutation. The closest plausible historical circular-control thesis chapter was not available in full text, so an older equivalent special-case classification remains a documented risk, not a claim of exclusion. The searchable published-result records did not disclose a covering result; search nonappearance is not treated as mathematical novelty proof.

## Value — PASS

This is a natural complete actuator-design classification, not an arbitrary numerical slice: it simultaneously solves exact worst-case energy, average energy, reachable-volume and conditioning criteria for a directed propagation network at **every** horizon. The fixed Fourier autocorrelation condition is a constructive design test, and the explicit optimal energy scaling quantifies the damping cost. The trace objective is provably blind to a singular actuator that fails controllability. Negative distributed actuation offers nonlocal ties, whereas nonnegative optimal actuation must be concentrated at one node. These are practical distinctions among natural controllability objectives.

## Literature and limitations

The first day-resolved supporting source is Summers and Lygeros, arXiv:1306.2491v1 (June 11, 2013). Further comparisons include Pasqualetti–Zampieri–Bullo's full 2014 circulant-control analysis; Tzoumas et al.'s finite candidate actuator selection; the circulant-network thesis/IEEE literature by Nabi-Abdolyousefi and Mesbahi; and the symmetric continuous-time actuator design of Chen and Belabbas. The proof covers no general network beyond an exactly damped cyclic permutation. The uninspected full thesis chapter presents residual originality uncertainty; this review does not assert coverage has been excluded from it.

Self-review: passed. Independent audit: not yet performed.
