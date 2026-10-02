# Independent audit evidence — 2026-10-01 UTC

## Final claim

Every strictly positive submultiplicative sequence \((a_n)_{n\ge 0}\) with \(a_0=1\) is simultaneously the operator-norm and essential-norm power profile of an irreducible unilateral weighted shift. Consequently every positive nonincreasing sequence \((\rho_n)\) is realized exactly as both \(\|W^n\|^{1/n}\) and \(\|W^n\|_e^{1/n}\).

## Correctness — PASS

Set \(\beta_k=a_{k+1}/a_k\). Submultiplicativity gives \(\beta_j\cdots\beta_{j+n-1}=a_{j+n}/a_j\le a_n\). Construct the weights by concatenating longer prefixes of \((\beta_k)\), separated by positive bridges. At each finite stage every new crossing product contains the newly chosen bridge, and there are only finitely many such new constraints; choosing the bridge sufficiently small preserves all upper bounds. Each prefix reappears at arbitrarily large indices, so the product of the first \(n\) ratios equals \(a_n\) infinitely often. Hence \(\|W^n\|=a_n\).

For block-start basis vectors \(e_{s_m}\), one has \(\|W^n e_{s_m}\|=a_n\) for all sufficiently large \(m\). The sequence is orthonormal and weakly null, so every compact \(K\) satisfies \(Ke_{s_m}\to0\). Therefore \(\|W^n-K\|\ge a_n\) for every compact \(K\), proving \(\|W^n\|_e=a_n\). All weights are positive, and the standard unilateral-shift reducing-subspace argument then gives irreducibility.

If \(a_n=\rho_n^n\) and \((\rho_n)\) is nonincreasing, then \(a_{m+n}\le a_ma_n\), so the construction applies and both root-norm sequences equal \(\rho_n\) exactly.

## Originality — PASS, with residual risk

The ordinary power-norm characterization is classical Wallen and is expressly excluded from the originality claim. A Resultary semantic search for prescribed ordinary and essential weighted-shift power profiles returned no earlier covering record. Targeted searches of the classical weighted-shift and spectral-radius-rate literature likewise found no inspected source stating simultaneous equality \(\|W^n\|=\|W^n\|_e=a_n\) for every \(n\) with an irreducible unilateral shift.

The most relevant classical survey is Allen L. Shields, *Weighted shift operators and analytic function theory* (DOI:10.1090/surv/013/02). Complete text was not available for inspection in this audit. That access limitation is retained as a genuine residual risk; it is not used as evidence of novelty. Young's 1980 result (DOI:10.1017/S0305004100057406) gives broad spectral-radius-rate context but does not imply the exact simultaneous realization here.

## Value — PASS

The theorem supplies a natural exact Calkin-norm strengthening of a classical arbitrary-profile realization while preserving irreducibility. The exact-rate corollary gives controlled examples in a narrow and important operator class, including irreducible quasinilpotent Riesz shifts with no compact positive power.

## Residual risks

The complete Shields 1974 survey was not inspected. Because the recurrent-prefix argument is elementary once Wallen's ratios are known, equivalent older coverage under different terminology remains possible.
