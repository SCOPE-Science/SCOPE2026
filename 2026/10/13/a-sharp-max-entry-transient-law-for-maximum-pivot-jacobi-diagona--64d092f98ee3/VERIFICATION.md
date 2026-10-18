---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

A pivot Jacobi step acts by a plane orthogonal matrix on each nonpivot pair (a_pk,a_qk). Both entries start <=s in magnitude; hence each new component <=sqrt(2)*s, the pivot is zero, and unaffected entries stay <=s. The explicit symmetric offdiagonal template (1,tau,-tau) has equal pivot diagonals and 45-degree rotation realizing sqrt(2)*tau. The eigenvalues 1 and (-1±sqrt(1+8tau²))/2, and c=(1-kappa*beta_minus)/(kappa-1), make the shift SPD of exactly condition number kappa. Check n=2 and tau=0 separately; strict spikes need tau>1/sqrt(2). This is a complete elementary proof, not an inference from the packaged numerical log.

## originality

PASS

Classic Jacobi sources contain orthogonal two-entry updates and decrease of offdiagonal Frobenius energy; these statements do not themselves quantify the sharp max-entry nonincrease criterion in terms of the second-largest element or realize it at arbitrary SPD condition number. Published nearby result on weighted Jacobi Euclidean iteration is a distinct stationary iterative method; Resultary complete-pivot ACA monitors a different matrix-approximation residual. Best-of-knowledge no exact prior coverage found; older Jacobi max-norm treatments remain a priority risk. Weighted Jacobi stationary iteration and ACA max-pivot Frobenius growth are distinct from two-sided symmetric Jacobi eigenvalue rotation, despite shared words; no matching second-largest-gap statement retrieved.

## value

PASS

Max-entry Jacobi actively pivots by an individual-entry diagnostic, unlike the standard decreasing offdiagonal Frobenius norm. An exact condition-independent maximal transient and sharp second-largest-entry gap provide a motivated pivot-local safety boundary; the three-dimensional SPD witness rules out explaining the spike by poor spectral conditioning. It is a narrow but mathematically natural sharp result rather than a general sweep or convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
