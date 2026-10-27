# Review: sharp boundary profiles for clipped quadratic dynamics

## Correctness — PASS
The domain is exactly \(0<\alpha<1\), \(0<\varepsilon<1/2\), with state \(p\in[\varepsilon,1-\varepsilon]\). The logarithmic-radius identity reduces escape to the atomless random binary sum. The two prefix events are proved by binary lexicographic order, including null dyadic-boundary events. The all-one/all-zero feedback paths saturate at explicit finite indices, giving the exact renormalization identities. Two-sided radial bounds and optimality of the exponent follow with constants uniform in the initial state. The rational witness \(H_{1/2,1/4}(3/4)=27/32\) is proved by the first two symbols; standard-library exhaustive cylinder checks reproduce the corresponding finite identities. No numerical experiment is used as an infinite proof.

## Originality — PASS within checked sources
The closest primary source is Endo, arXiv:2603.20653, Section 4 Example 4.2. Its proved assertion for this model is continuity of the escape probability, including its value at radius \(2\); it does not present either the exact finite-level dyadic profile or the sharp endpoint exponent and oscillation witness. Arcozzi's arXiv:2607.07344 and Okamura's arXiv:1507.05829 study different de Rham equations and singular measures. Searches of related mathematical records and accessible prior claims did not locate an equivalent assertion or a stronger statement implying the pair of exact feedback profiles. This is a bounded evidence-based assessment, not a claim of exhaustive mathematical priority.

## Mathematical value — PASS
Quantifying the boundary regularity of the published example fills a specific gap left by a continuity theorem. The model has a nontrivial state-feedback process, yet finite clipping creates a common exact profile at both escape boundaries, a uniform exponent independent of feedback strength, and explicit discrete-scale non-power behavior. These identify structural rather than merely numerical features and offer a precise benchmark for other state-dependent random-iteration systems.

## Limitations and residual priority risk
The result does not control interior moduli, global Hölder regularity, arbitrary random polynomial systems, or the entire parameter set for profile nonconstancy. Earlier general work on binary-cylinder local dimensions may contain a broader abstract formulation of the exponent, although no checked source gives the finite-state-saturation identities for Endo's particular model. Independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
