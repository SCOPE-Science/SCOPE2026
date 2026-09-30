# Independent Audit — Sharp SSPRK(3,3) CFL for piecewise-constant sparse-grid DG

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `57bf7a7f3697ebc675d2eeb044796f2adbbee263`  
**Audited current source tree:** `57bf7a7f3697ebc675d2eeb044796f2adbbee263`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence; this file is a guarded publication-plan payload and is not claimed to be already present in the repository.

## Correctness — PASSED

PASS. Huang's Corollary 4.4 supplies exactly the needed contraction H=I-B_c/m with ||H||_2<=1 and endpoint eigenvalues +1 and -1. Complexifying the finite-dimensional real Hilbert space and applying von Neumann's polynomial inequality therefore gives the submitted disk upper bound, while the constant and alternating modes give the two scalar lower witnesses. For SSPRK(3,3), the independent symbolic check reproduces 1-|R_3(mu(w-1))|^2=(mu x/9)F_mu(x) and the stated Bernstein coefficients. Their signs are nonnegative exactly through the unique positive root mu*=1.256372663309164... of 2mu^3-3mu^2+3mu-3=0; immediately above it the alternating mode has |R_3(-2mu)|>1. This establishes the iff CFL threshold, not merely a sufficient bound.

## Originality — PASSED

PASS, narrowly scoped. The scalar origin-tangent stability-disk problem for Runge–Kutta methods is classical and is not new. Huang's September 2026 paper, however, states only the SSP-coefficient sufficient extension for higher-order SSP RK and explicitly says its sharpness is not guaranteed. Targeted searches did not locate the combination of Huang's sparse-grid contraction/end-point modes with the SSPRK(3,3) stability disk yielding the exact 1.2563726633... multiplier. The originality credit is therefore only for this sparse-grid sharp application and reduction.

## Scientific value — PASSED

PASS. The theorem closes an explicit sharpness gap in the motivating preprint and enlarges the rigorously admissible SSPRK(3,3) step by about 25.64% over the SSP-coefficient-one bound, uniformly in dimension for the standard sparse-grid construction. The general contraction-to-polynomial-disk reduction is also reusable for other RK stability polynomials on the same spatial operator.

## Independent checks

- Read Huang's open arXiv full text at Lemma 3.9, Corollary 3.10, Corollary 4.4, and Remark 3.11; the paper supplies ||H||<=1 and eigenvalues ±1 and explicitly says the high-order SSP sufficient condition need not be sharp.
- Independently expanded the SSPRK(3,3) boundary polynomial and verified the Bernstein identity and coefficient factorization.
- Independently solved the cubic and reproduced mu*=1.2563726633091643; P'(mu)=-3(2mu^2-2mu+1)<0 verifies uniqueness.
- Checked that the alternating endpoint gives the necessary instability for every mu>mu*.
- Inspected the repository verification artifact as corroboration, including its finite two-dimensional Haar sparse-grid matrix check.
- Verified the assigned record path is unchanged from the dispatcher source-check commit to current main and that both dated independent-audit marker files are absent.

## Limitations

- The theorem is for linear constant-coefficient periodic transport, piecewise-constant standard total-level sparse-grid upwind DG, and one-step L2 stability.
- Classical stability-disk theory and von Neumann's inequality are prior work; no novelty is claimed for them.
- The motivating preprint is very recent, leaving a residual risk of simultaneous unindexed follow-up work.

## Evidence and references

- https://arxiv.org/abs/2609.17312
- https://arxiv.org/html/2609.17312v1
- https://ntrs.nasa.gov/citations/19790024769
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/ssprk3-sharp-sparse-grid-cfl--3609313351c2

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
