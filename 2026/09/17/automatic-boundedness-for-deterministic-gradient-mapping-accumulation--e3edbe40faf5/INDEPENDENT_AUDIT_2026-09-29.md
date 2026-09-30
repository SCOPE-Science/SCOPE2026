# Independent audit — 2026-09-29

**Record:** `2026/09/17/automatic-boundedness-for-deterministic-gradient-mapping-accumulation--e3edbe40faf5`  
**Audited source tree:** `503e1dd1363b9f794ec4bfd0dd3ba447ecd50c97`  
**Repository:** `SCOPE-Science/SCOPE2026` at checked commit `253a0fe5d0217455660a277f9adb940030e567ad`  
**Overall independent-audit verdict:** **PASS**

## Correctness — PASS

The accumulator dichotomy is noncircular.  If S_k is bounded, its exact multiplicative update directly makes the squared increments summable.  If S_k is unbounded, monotonicity forces a finite index after which alpha_k<=1/L; the standard deterministic proximal-gradient descent inequality then bounds all tail increments, and only a finite prefix remains.  In the convex case, proximal optimality and monotonicity of partial h give the stated cross-term inequality; Baillon--Haddad cocoercivity and exact maximization of the resulting quadratic yield ||e_{k+1}||^2-||e_k||^2 <= (alpha_k L/2-1)||d_k||^2.  Square summability controls the bounded-S branch, while eventual alpha_k<=1/L makes the distance Fejer-decreasing in the unbounded-S branch.  Thus both components of the cited Assumption 1 are indeed automatic in the deterministic smooth regimes claimed.

## Originality — PASS

The inspected Wang--Yurtsever v1 explicitly assumes bounded increments in its deterministic smooth theorem and optimizer-distance boundedness in the convex smooth corollary.  Nearby adaptive proximal methods avoid boundedness assumptions by different update mechanisms; no located source made these two bounds automatic for this exact gradient-mapping-accumulation recursion.  The observation is concise, but it is algorithm-specific and not merely a restatement of fixed-stepsize forward--backward theory.

## Scientific value — PASS

Removing a named boundedness assumption from two deterministic guarantees of a recent adaptive proximal-gradient method is a substantive structural improvement even though it does not improve the first-order complexity exponent.  The dichotomy also explains why this accumulator self-corrects from potentially oversized early steps.

## Sources used in the independent comparison

- https://arxiv.org/abs/2605.05944 — Wang--Yurtsever source; Algorithm 1 and Assumption 1 are the exact objects audited.
- https://arxiv.org/abs/2510.06079 — Nearby adaptive proximal-gradient work that avoids boundedness through a different curvature-based mechanism.
- https://arxiv.org/abs/2606.29893 — Related 2026 discussion of AdaGrad/composite objectives and gradient-mapping accumulation, without the audited automatic-boundedness theorem.

## Limitations and residual uncertainty

- The proof is deterministic and smooth; it does not remove boundedness requirements in the stochastic, convex nonsmooth, inexact-proximal, or accelerated regimes.
- The resulting bound can depend on the finite pre-threshold trajectory and is not a small a priori problem-data constant.

This independent audit is scoped to correctness, originality, and scientific value.  Repository material was used as evidence only; no GitHub modification was made during the audit.
