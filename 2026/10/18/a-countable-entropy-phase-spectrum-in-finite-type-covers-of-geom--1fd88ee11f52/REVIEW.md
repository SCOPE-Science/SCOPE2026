# Scientific review: finite-cover entropy phases of geometric gap shifts

## Correctness (C): PASS
The mathematical object is fully specified: binary two-sided geometric return-distance shift, canonical length-\(n\) SFT covers, natural logarithmic entropy, fixed integer base \(b\ge2\), and all integers \(n\ge1\). A word-level characterization shows that the covers permit precisely the power returns shorter than \(n\), plus every return at least \(n\). The finite-state first-return graph yields the exact renewal equation. Subtracting the infinite return series, bounding the next geometric power by at least \(2n\), and Taylor expanding around the simple entropy root prove a uniform \(O_b(n\lambda_b^{-n})\) normalized error. All subsequential phases are proved exhaustive; a periodic witness distinguishes successive covers at every non-power. The supplied checker matched 96 matrix/root cases and separately compared all short languages for \(n\le9\). Finite tests do not establish the general theorem; the analytic argument does.

## Originality (O): PASS, subject to the stated residual risk
The motivating 2026 article [1] introduces and studies SFT cover entropy stability but does not give a geometric-gap exact entropy spectrum. The established general renewal formulas [2,3,4,7] are openly credited. An inspected published result [5] uses the same geometric-gap system but studies constrained measure entropy at small marker density, a distinct invariant/limit. An inspected published result [6] does study canonical covers, but of the Fibonacci Sturmian shift with zero limiting entropy, yielding an interval-valued rescaling; it does not imply the positive-entropy lacunary-gap countable spectrum. Searches for geometric-gap Markov approximations, return-length lacunarity, exponential entropy errors, cover plateaux, and countable accumulation found no same-claim or stronger covering statement. The publication record cannot guarantee global uniqueness: an alternative earlier renewal-asymptotic formulation is a real residual bibliographic risk.

## Mathematical value (V): PASS
Canonical finite-type covers are natural, finitely computable resolutions of a given symbolic system, and their entropy convergence is the subject of [1]. A mere convergence statement hides a sharp \(\lambda_b^{-n}\) boundary layer: its normalized errors do not settle to a constant or fill an interval but form an explicit countable set of asymptotic phases with one limit point. The exact sparse equality stages provide a structural explanation for those phases and contrast with known cover staircases on zero-entropy languages. This is a precise finite-resolution law across all bases and all cover lengths, rather than an isolated parameter evaluation or table recomputation.

## Scope, closest literature, and risks
The claim concerns fixed integer powers as allowed marker distances, not all gap shifts, and does not address invariant measures or other cover constructions. A known renewal formula is the starting point, not a new entropy identity. A possible equivalent formulation in older coding/renewal perturbation literature remains unverified; no independent validation is asserted.

[1] Coles, Cyr, Kra, Pavlov, *Stable covers of subshifts*, arXiv:2602.04097v1 (2026-02-04), §§2.2, 3.3.  
[2] Dillon, *Dynamics and entropy of S-graph shifts*, arXiv:2010.06031v3, §§1, 4.  
[3] Ahmadi Dastjerdi and Jangjoo, *Computations on Sofic S-gap Shifts*, arXiv:1108.3414v5.  
[4] Ahmadi Dastjerdi and Jangjoo, *Dynamics and Topology of S-gap Shifts*, arXiv:1108.3242v4.  
[5] *Log-periodic second-order entropy law for geometric gap shifts*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-log-periodic-second-order-entropy-law-for-geometric-gap-shifts--166969f68799 .  
[6] *A Fibonacci entropy staircase and its full scaled accumulation interval*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-fibonacci-entropy-staircase-and-its-full-scaled-accumulation-i--be7c0c99809f .

[7] Ramirez and Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438v1, Theorems 1.1 and 3.3.

Self-review: passed. Independent audit: not yet performed.
