---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For n>=2 and -1/(n-1)<rho<1, the entrywise independent relative symmetric perturbation set is universally PD exactly when 0<=u<tau_n(rho). For a fixed test x the worst perturbation aligns signs of x, giving G-u S|G|S, so checking all sign vertices is sufficient and necessary. Negative rho is minimized by a coherent sign pattern and the 1-direction eigenvalue, giving tau=(1+(n-1)rho)/(1-(n-1)rho). At rho=0 only diagonal entries vary and tau=1. For positive rho the 2-block eigenspace determinant is positive iff u<(K_r-rho)/(K_r+rho), with K_r^2=rho^2+(1-rho)(1+(n-1)rho)/(r(n-r)); balanced group sizes minimize K_r. The other eigenspaces stay positive. Explicit boundary null vectors and indefinite vertices above threshold show sharpness. Even n gives tau=1/cond_2(G); odd n gives a strictly larger radius with the stated n²/(n²-1) limiting ratio. Fresh independent finite sign-vertex calculations checked dimensions 2..8 and correlations of both signs; they corroborate, not prove, the unrestricted symbolic result.

## originality

PASS

Best-of-knowledge original explicit sign-sensitive complete closed-form robustness radius and odd/even parity effect. Rohn interval-matrix vertex theory, Demmel/Rump componentwise distance theory, Roustant–Deville compound-symmetry block methods, and Balabanov–Melnichenko–Mahoney error context are established antecedents rather than new elements. The full texts of some older plausible sources were inaccessible, so precise old-formula coverage cannot be excluded.

## value

PASS

The universally sharp componentwise definiteness radius, worst-case perturbations, and dimension-parity loss against condition-number-only estimates are motivated conditioning invariants for a canonical Gram family. Their exact boundary can benchmark relative-entry robustness budgets without claiming applicability to a specific correlated rounding-error model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
