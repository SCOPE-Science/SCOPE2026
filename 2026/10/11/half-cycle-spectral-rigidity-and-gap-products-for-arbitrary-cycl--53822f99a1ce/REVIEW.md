# Scientific review: half-cycle Fourier concentration

**Correctness — PASS.** The unitary Fourier normalization gives a diagonal half-mass kernel, zero same-parity off-diagonal entries, and a rectangular Cauchy cross-parity matrix. Every maximal square Cauchy minor is nonzero, proving the exact \(1/2\)-eigenspace dimension without relying on numerics. Cauchy--Binet proves the gap product for all masks, including both degenerate boundaries. The separate finite checker passed 696 masks/cases; it is corroborative only.

**Originality — PASS, with an explicitly retained literature risk.** Jaming addresses the cyclic Fourier transform and not finite time/frequency concentration. The inspected periodic-prolate framework in Matthysen--Huybrechs uses contiguous band masks and does not state the arbitrary-mask half-energy multiplicity or all-noncentral-gap product. Zhu and coauthors prove nonasymptotic eigenvalue distribution bounds for contiguous symmetric bands, not this exact product or parity classification. Searches of equivalent Cauchy/Toeplitz, Slepian, cyclic-concentration, and determinant language did not locate a covering statement; absence from a search is not itself a novelty proof. Xu--Chamzas (1984) is close but access-limited: its full text could not be compared. An equivalent result under historical special-function terminology remains a residual risk.

**Mathematical value — PASS.** A half-cycle is the canonical equal-time partition of an even periodic signal. The result supplies an exact, mask-independent count of transition modes for every band layout and an explicit algebraic invariant measuring the entire collection of departures from half-energy concentration. Neither quantity requires numerical diagonalization, and the nullity is controlled only by the even/odd frequency imbalance. This is a natural structural classification, not an arbitrary finite parameter census.

**Scope.** The theorem neither gives each individual noncentral eigenvalue nor extends to unequal time windows; it is not a claim of independent validation.

Same-model review: passed. Independent audit: not yet performed.
