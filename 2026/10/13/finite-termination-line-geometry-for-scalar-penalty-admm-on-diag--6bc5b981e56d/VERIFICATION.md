---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Exact scaled error updates give the rank-one 2×2 block M with det M=0 and trace 1-alpha*rho*(a+b)/((rho+a)*(rho+b)). Cayley–Hamilton yields M²=(tr M) M; any nonzero trace creates a persistent eigenmode, whereas zero traces annihilate all modes in at most two cycles. Solving tr=0 is exactly ab=tau(a+b)-rho² with tau=rho(alpha-1) and 0<tau<=rho. The KKT z-optimality gives rho u^+=B z^+ in error coordinates. Independently recomputed exact Fraction modal matrices for (a,b)=(1,5),(2,6), rho=4, alpha=15/8: [[5/18,-2/9],[25/72,-5/18]] and [[3/20,-1/10],[9/40,-3/20]], both square to zero.

## originality

PASS

Complete common-line geometric criterion for arbitrary heterogeneous commuting diagonal pairs under scalar-Euclidean penalty is not covered by known isotropic spectral annihilation or metric-selection rate bounds inspected; best-of-knowledge only.

## value

PASS

The result identifies exactly when one practical scalar penalty and over-relaxation parameter annihilate every heterogeneous quadratic coordinate, with sharp necessary and sufficient geometric conditions and two-step termination; useful for algorithm design and tests without requiring an arbitrary new algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
