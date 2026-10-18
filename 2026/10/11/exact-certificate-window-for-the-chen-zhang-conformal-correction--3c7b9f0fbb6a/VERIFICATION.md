---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read actual RESULT.md blob 0e4da01a07100502bcc52430319c4ef3672ed0a8 and the source-used hypotheses explicitly stated: k_g≥ε⁴(1−s)/8−ε⁶/2 and Δ_g(z²)=(1+ε²)(2−6s). With e=ε², a=ε⁴/(1+ε²), s=z²∈[0,1], u=1+aτs, the conformal certificate reduces exactly to B(s)=(1−s)/8−τ(1−3s)/(1+aτs)−e/2. Independently differentiated B in SymPy: B′=−1/8+τ(3+aτ)/(1+aτs)^2 and B′′=−2aτ²(3+aτ)/(1+aτs)^3<0. Thus its minimum lies at s=0 or 1, with B(0)=1/8−τ−e/2 and B(1)=2τ/(1+aτ)−e/2, giving the claimed necessary-and-sufficient strict window for THIS LOWER BOUND, not actual curvature. u∈[1,1+aτ] gives uniform certified k_hat≥ε⁴min(B0,B1)/(1+aτ)^2. The two branches cross at 1+(a−24)τ−8aτ²=0; checked closed positive root and small-a expansion τ*=1/24+a/864+a²/62208+O(a³) symbolically. Below crossing, derivative of lower branch has positive numerator 2+a e+a² e τ−4aτ on allowed range; above crossing first branch decreases while denominator grows. The source coefficient τ=1/24 is interior for every 0<ε≤1/4. Numerical samples at ε²=1/16 and 1/100 corroborate order; the inequalities are analytic.

## originality

PASS

Best-of-knowledge: the primary cited construction fixes τ=1/24 and introduces the geometric conformal correction. Its available statement does not identify a global open robustness window for that precise lower-bound proof or optimize its finite-ε certificate. The external primary full text remained inaccessible; exact formulas are compared from the inspected source package with explicit residual risks.

## value

PASS

The source’s conformal coefficient 1/24 is motivated by a difficult geometric positivity construction. Determining the exact robustness interval of the actual published certificate and its unique finite-ε optimal coefficient is a natural stability question; a reader reusing the construction can choose an admissible coefficient and a rigorous numerical lower bound. The value claim is explicitly limited to the certificate, not inflated to a new manifold classification or a sharp curvature positivity criterion. This narrowly useful non-implied coefficient fact meets the common structural/value threshold despite elementary endpoint calculus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
