---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

On the frozen RESULT.md, Dirichlet covariance (δ_ij−1/n)/[n(nα+1)] gives K(x,y)=−nα+n(nα+1)Σx_i y_i. K integrates to 1 and reproduces the affine span. Convexity of its negative part in x reduces the L∞ norm and positivity defect to a vertex, and interior-positive Dirichlet density makes nonvertex maxima strict. With Y_1~Beta(α,(n−1)α), the beta recurrence gives C=(nα+1)c^α(1−c)^b/[α B(α,b)]−I_c(α,b), hence both endpoint norms 1+2C and min_{0≤f≤1} Pf=−C. For α=λ/n, expanding the beta tail after splitting at c=λ/[n(1+λ)] proves λ−C=(λ²/n)[log n+1+log((1+λ)/λ)−ψ(λ)−γ]+o_λ(1/n). Fixed-α n→∞ uses gamma convergence and uniform integrability, fixed-n α→∞ Gaussian convergence; these regimes are distinct. Independently evaluated high-precision beta values for λ=.5,1,3 and n=300,3000; the claimed second-term errors decreased, but numerical checks are not proofs. Source check.py was inspected as exact-rational finite checker, not relied upon for the limiting theorem.

## originality

PASS

Best-of-knowledge PASS for weighted endpoint norm and double scaling, expressly excluding the already published α=1 result. The 2010 primary canonical-correlation/Jacobi kernel article supplies the kernel framework; its inspected portions did not establish the present beta negative-part norm or fixed-total-mass logarithmic coefficient. Literature under orthogonal-polynomial Lebesgue constants may contain a disguised equivalent.

## value

PASS

Symmetric Dirichlet concentration is a natural deformation of simplex affine least squares; endpoint loss of positivity matters for projection stability. The singular fixed-total-mass scaling α=λ/n produces a genuine logarithmic correction that cannot be recovered from the unweighted α=1 case. The exact all-n beta law and distinct linear-growth fixed-α limit are reusable operator invariants, not a cosmetic parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
