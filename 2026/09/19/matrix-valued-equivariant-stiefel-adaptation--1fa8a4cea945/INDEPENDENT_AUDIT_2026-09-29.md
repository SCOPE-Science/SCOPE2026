# Independent Audit — Matrix-valued adaptive moments preserve Stiefel equivariance

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `9ed03f5aeca8fb9b7d01769b04529a6eb1f55526`  
**Audited current source tree:** `9ed03f5aeca8fb9b7d01769b04529a6eb1f55526`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used only as read-only evidence. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. For the left O(d)-action on R^{d×r}, the commutant is exactly right multiplication X↦XB: writing the map columnwise and using the standard irreducibility/commutant argument forces every d×d block to be a scalar multiple of I_d, while an arbitrary r×r matrix of those scalars remains. Thus O(d)-equivariance does not force a single scalar moment. Self-adjoint positive definite equivariant operators correspond exactly to symmetric positive definite B, and the entrywise-diagonal subclass is precisely right multiplication by a diagonal B. The proposed column-covariance state C_t=βC_{t-1}+(1-β)ξ_t^Tξ_t transforms by C↦R^TCR under right O(r), so its inverse square root transforms covariantly; the Stiefel tangent projector and polar retraction then give the stated O(d)×O(r) biequivariance. I independently checked the non-scalar/non-diagonal commutant identity numerically to machine precision.

## Originality — PASS

PASS, narrowly scoped and chronological. Matrix-valued adaptive statistics on matrix manifolds are established prior art (e.g. RASA), and Adam-style Stiefel optimization also predates the motivating preprint, so no novelty is credited to those ideas. The September 19 record instead corrects the source-specific uniqueness/prior-art claim and identifies the full right-matrix commutant. The current arXiv v2 of Guerrero's paper, posted after this record, now explicitly concedes that per-column scaling is O(d)-equivariant; that later revision is consistent with the correction and does not erase the record's earlier priority. The record's full XB commutant classification remains stronger than the v2 entrywise-diagonal statement.

## Scientific value — PASS

PASS. The correction separates three notions that the optimizer discussion otherwise conflates: O(d)-equivariance, entrywise-diagonal adaptivity, and collinearity/steepest-direction preservation. It also gives a concrete matrix-valued equivariant adaptive family and a precise condition under which scalar uniqueness really is true. Because the current source revision has already narrowed its equivariance claim, the principal value is conceptual correction and reusable representation-theoretic guidance rather than a new benchmark optimizer.

## Independent checks

- Reproved the commutant classification for the left O(d) representation on d×r matrices and the self-adjoint/SPD specialization.
- Checked explicitly that arbitrary non-diagonal right multiplication XB commutes with left orthogonal changes of basis; an independent random d=7,r=3 test gave residual below 1e-15.
- Re-derived covariance transformation, functional-calculus transformation of (C+eps^2 I)^(-1/2), tangent-projection equivariance, and polar-retraction equivariance.
- Compared against RASA (ICML 2019), which already adapts row/column subspaces of matrix-manifold gradients, and against earlier Stiefel adaptive optimization literature.
- After open-access full-text retrieval failed, authorized retrieval was used for arXiv:2609.19363. The current v2 explicitly allows per-column moments in Proposition 5 and is dated after the September 19 SCOPE record.
- Verified the current repository tree SHA exactly matches the assigned source-tree SHA and that the September 30 independent-audit marker files are absent.

## Limitations

- The audit does not claim that matrix-valued manifold adaptation or Adam-on-Stiefel is new.
- The archived v1 wording was not independently recovered as a stable historical PDF; the audit relies on the dated SCOPE record for the v1-targeted wording and independently verifies that the later current v2 now contains the per-column concession.
- No empirical superiority is claimed for the proposed full matrix-valued moment; the validated contribution is structural.

## Evidence and references

- https://arxiv.org/abs/2609.19363
- https://arxiv.org/abs/1902.01144
- https://proceedings.mlr.press/v97/kasai19a.html
- https://arxiv.org/abs/2205.14173
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/matrix-valued-equivariant-stiefel-adaptation--1fa8a4cea945

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
