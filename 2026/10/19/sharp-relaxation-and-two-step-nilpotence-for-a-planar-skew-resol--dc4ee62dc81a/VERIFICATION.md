---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The KKT matrix is invertible with determinant c² and zero satisfies the saddle inequalities. Inverting I+τS gives D=(I−K)/ρ=[(s²+h,−s);(s(1−h),s²)]/(1+s²). Its trace is t and its determinant is s²/(1+s²)=d. Real roots μ± are positive, so the exact Schur limit is ρ<2/μ+, and the maximum modulus is minimized uniquely by balancing the opposed endpoints at ρ=2/t. For conjugate roots the squared radius is 1−ρt+ρ²d, giving the strict interval and the unique minimizer t/(2d). At the repeated root the strict limit is 4/t and the radius is zero only at 2/t; at each extreme stability boundary at least one eigenvalue has modulus one. A fixed K terminates universally in finite time iff both eigenvalues vanish, requiring Δ=0; factoring the discriminant numerator gives τ²[q²+4c²(τq−1)], with exactly one positive root iff q<2c. At that root the positive (1,2) entry prevents index one, and Cayley–Hamilton gives index two. Exact alternate replay: with ζ=q/(2c) at the terminating tuning, K=(2ζ/(1+ζ²))(1,ζ)ᵀ(−ζ,1), whose square vanishes since the row and column pair to zero. At ζ=3/4 this produces all four rational entries in the finding exactly. Solving ρ*>2 gives ζ>1/√3. These checks apply to all deterministic starts, not only eigenvector starts or monotonic norm decay. Supplied code and run description were inspected and not executed.

## originality

PASS

The method is established relaxed forward–backward splitting, also expressible as preconditioned Richardson, and its generic spectral minimization is standard. The supported distinct contribution is the sharp behavior in this motivated monotone-plus-skew model, especially the exact curvature/coupling feasibility of a unique positive, nontrivial nilpotent tuning and a region of such tuning beyond relaxation two. No inspected stronger convergence or different splitting theorem supplies that condition or tuning.

## value

PASS

The spectral formulas alone are standard two-eigenvalue analysis. The smallest curved bilinear saddle model gives an exact separation between generic sufficient relaxation rules and what a fixed natural splitting can achieve: there is a precise curvature threshold for hitting the saddle from every start in two steps, and it can occur for relaxation greater than two. At the nilpotent tuning the displayed rank-one factorization gives ‖K‖₂=2ζ=q/c, which can exceed one despite exact termination. This is a precise witness distinguishing spectral behavior from per-step contraction, not a claim that extrapolation is generally numerically safe.

The dated certificate retains the supplied scientific assessment, sources and limitations.
