# Independent Audit — Gaussian local limits and exact constants for weighted-representation partitions

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `8b25c3ddf1dc747b880874effbcb2fcf7994f31b`  
**Audited current source tree:** `8b25c3ddf1dc747b880874effbcb2fcf7994f31b`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit files were absent when this guarded plan was prepared.

## Correctness — PASS

PASS. Li--Xu--Yan's recurrence reduces every eventual discrepancy condition to k boundary equations in T+k signs. After converting signs to independent Bernoulli bits, the coefficient matrix B_T has T^{-1}B_TB_T^T→G_k=(1/k)I+(k+2)J/k^2, with det(G_k)=(k+3)/k^k and inverse kI-(k+2)J/(k+3). Each residue class supplies Θ(T) columns equal to e_s, so the lattice is exactly Z^k and there are no secondary modulus-one Fourier saddles. The multivariate lattice local CLT therefore gives the stated Gaussian factor and constant; multiplying the local probability (2/pi)^{k/2}T^{-k/2}/sqrt(det G_k) by 2^{T+k} yields (8k/pi)^{k/2}/sqrt(k+3)·2^T/T^{k/2}. Independent dynamic-programming counts for k=2,3 converge to the claimed constants and shifted profile.

## Originality — PASS

PASS, with an access qualification. The complete September 2026 Li--Xu--Yan preprint proves only two-sided order f_k(T) asymp_k 2^T/T^{k/2}; its introduction says Yang--Chen (2012) proved finiteness and only lim log f_k(t)/t=log 2. The submitted local limit therefore sharpens the new order theorem to an exact constant and Gaussian moderate boundary profile. Open-access searches for the 2012 paper did not expose full text, and authorized Oxford retrieval stopped at a human-verification gate, so that paper was not claimed as read; the priority assessment relies on the explicit historical summary in the 2026 primary source plus targeted searches of the intervening representation-function literature, which found no matching exact asymptotic.

## Scientific value — PASS

PASS. An exact multivariate local limit supplies the previously missing leading constants, answers quantitative comparisons between different weights, and handles sqrt(T)-scale boundary discrepancies with a nontrivial Gaussian profile. This is a substantive refinement of a just-proved order-of-magnitude theorem.

## Independent checks

- Read all ten pages of the lawful-open Li--Xu--Yan preprint; Theorem 1.2/Corollary 1.3 give only asymptotic comparability, while the proof provides the finite boundary sign system used here.
- Re-derived the boundary coefficient matrix, its covariance limit G_k, determinant, and inverse.
- Checked the aperiodicity/lattice issue using the Θ(T) copies of each standard basis column e_s.
- Independently evaluated exact counts by dynamic programming; for k=2 the actual/predicted ratios at T=40,80,120 were about 0.9264,0.9619,0.9743 and a shifted T=200 test gave about 0.9929.
- Searched the 2012 Yang--Chen paper through arXiv/open-access channels first; authorized institutional retrieval then reached a human-verification gate, so no inaccessible text is represented as read.
- Checked 2024/2025 follow-up abstracts and the 2026 source's literature account; no exact large-T constant or Gaussian local-limit statement was located.
- Verified the assigned record tree is unchanged from the dispatcher source-check commit to current main and that the dated audit markers are absent.

## Limitations

- The asymptotic is for fixed k; no uniformity for growing k is established.
- The Oxford attempt for Yang--Chen (2012) required human verification and therefore did not yield readable full text during this run; the audit does not claim otherwise.
- The local-CLT proof uses standard Fourier/lattice machinery; novelty is in identifying and exploiting the exact boundary matrix, not in the general theorem itself.

## Evidence and references

- https://arxiv.org/abs/2609.20385
- https://doi.org/10.1016/j.jnt.2012.06.005
- https://doi.org/10.1007/s11139-025-01113-7
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/exact-weighted-representation-counts--1c7512f9deb9

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
