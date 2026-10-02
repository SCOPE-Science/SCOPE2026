# Independent Audit — Quadratic anisotropy slaving in diffusive simplex covariance dynamics

**Audit date:** 2026-10-01 (UTC) (UTC)  
**Disposition:** passed

## Correctness — PASS

The primary source gives the exact covariance eigenvalue ODE, the pairwise-difference identity, exponential convergence, and the sharp rates \(\alpha_\perp\) and \(\alpha_\parallel\). Because the coefficient in the pairwise exponent approaches its limit exponentially, each nonzero eigenvalue gap has a finite nonzero asymptotic amplitude, producing a nonzero traceless limit. Expanding \(e_n\) about the mean cancels the linear traceless term and gives \(-\tfrac12\binom{d-2}{n-2}\lambda_*^{n-2}\|A\|_F^2\). The mean equation is therefore forced at rate \(2\alpha_\perp\). Since \(\alpha_\parallel-2\alpha_\perp>0\) for \(2\le n<d\), variation of constants yields the displayed \(C_{d,n}\); direct binomial simplification also gives the displayed \(K_{d,n}\). The symbolic verifier agrees with these identities but is not proof by itself.

## Originality — PASS

The source paper stops at first-order exponential covariance rates. Its proof explicitly bounds the centered elementary-symmetric remainder by \(O(D(t)^2)\) and uses that only to obtain an upper decay estimate for the mean; it does not identify the quadratic forcing coefficient, a limiting recoil ratio, eventual positive recoil, or the interaction-energy coefficient. Resultary and targeted literature searches found no equivalent source-specific second-order law.

## Scientific value — PASS

This is a structural nonlinear asymptotic law: it identifies how the slow symmetry-breaking traceless mode forces the faster scalar mode and the interaction energy, including universal sign and exact coefficients. It sharpens the source’s rate theorem in a way that can distinguish genuinely multipoint interactions from the pairwise regime.

## Source inspections

- Full arXiv HTML was read through the covariance ODE, pairwise differences, subcritical convergence proof, and sharp covariance-rate corollary.
- Assigned proof and verifier were inspected from the frozen Git blobs.
- Resultary and related-source searches were compared for aliases of slaving/recoil/second-order asymptotics.

## Residual risks

- Very recent concurrent work may be incompletely indexed.
