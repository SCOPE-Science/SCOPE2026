# Independent Audit — Exact self-decomposability threshold for Gaussian compound-Poisson perturbations of symmetric variance-gamma laws

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `7eed4aee937bd888091e6ef6a10ba6aeb39496f5`  
**Audited current source tree:** `7eed4aee937bd888091e6ef6a10ba6aeb39496f5`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used read-only as evidence. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. The Lévy density is beta exp(-|x|/b)/|x| plus lambda phi_sigma(x), so the canonical function is k(x)=beta exp(-x/b)+lambda x phi_sigma(x). The classical one-dimensional class-L criterion reduces self-decomposability exactly to k'<=0. For x>=sigma this is automatic; for 0<x<sigma it gives the submitted one-variable infimum. The logarithmic derivative of F_r(y)=exp(-ry+y^2/2)/(1-y^2) is -r+y(3-y^2)/(1-y^2), whose increasing second term has derivative (y^4+3)/(1-y^2)^2, so the minimizer y_r is unique. Envelope differentiation gives the unique scale optimum r*=sqrt(2+sqrt(3)); an independent numerical evaluation reproduces y*=0.517638090205..., r*=1.931851652578..., and lambda_max/beta=2.782354289570.... The small- and large-r expansions, weak-perturbation fragility, and the inverse-Fourier background-driving density all agree with direct recomputation.

## Originality — PASSED

PASS, narrowly scoped. The canonical-density monotonicity criterion for self-decomposability and the variance-gamma Lévy density are classical, while Wang--Yin's 2026 work gives a recent characteristic-function criterion in a different alpha-Cauchy application. Targeted searches for a symmetric variance-gamma law perturbed by centered Gaussian compound-Poisson jumps did not locate the submitted exact activity boundary, optimal jump-scale ratio, or background-driving density. The originality credit is therefore for the explicit phase diagram and its consequences, not for the underlying class-L criterion.

## Scientific value — PASSED

PASS. The result gives a closed exact robustness boundary for a natural finite-activity perturbation of a standard self-decomposable family, identifies the unique scale maximizing admissible jump activity, and exhibits a concrete weak perturbation that destroys class L. The explicit background-driving law provides an independent certificate and makes the threshold operational.

## Independent checks

- Re-derived the combined Lévy density and canonical self-decomposability profile.
- Differentiated the canonical profile and rederived the exact infimum over y in (0,1) and uniqueness equation r=y(3-y^2)/(1-y^2).
- Recomputed the envelope derivative, solved the stationary system, and numerically reproduced r*=sqrt(2+sqrt(3)) and lambda_max/beta=2.782354289570....
- Rechecked the small-r and large-r asymptotics and the fixed-lambda weak-perturbation conclusion.
- Fourier-inverted the background-driving characteristic expression and verified nonnegativity is exactly the same threshold inequality.
- Searched for prior Gaussian compound-Poisson/variance-gamma self-decomposability thresholds and found no covering result.
- Verified that the assigned record path did not change between the dispatcher source-check commit and current main and that the dated audit markers are absent.

## Limitations

- The explicit phase diagram is one-dimensional, symmetric, and specialized to centered Gaussian compound-Poisson jumps.
- The general derivative identity is a direct specialization of the classical class-L characterization and is not credited as a new theorem.
- The literature search cannot exclude an older equivalent perturbation calculation phrased in different Lévy-process terminology.

## Evidence and references

- https://arxiv.org/abs/2609.18536
- https://arxiv.org/abs/2303.05615
- https://doi.org/10.1016/j.jmaa.2013.09.041
- https://doi.org/10.1016/j.spa.2019.02.012
- https://arxiv.org/abs/math/0205316
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/variance-gamma-gaussian-jump-selfdecomposability--69b2cf5f0f2e

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
