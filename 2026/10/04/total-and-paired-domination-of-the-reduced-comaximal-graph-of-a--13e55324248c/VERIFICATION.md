---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

CRT gives a vertex u_i whose neighborhood is exactly the exclusive cell T_i, forcing every total set to meet each T_i. Conversely one chosen vertex per T_i forms a clique and dominates every vertex outside the Jacobson radical. Parity plus this clique gives the paired minimum, with an extra CRT vertex in the odd case. The polynomial is the direct generating function of the all-set classification. Fresh support-union enumeration reproduces the minima through n=5.

## originality

PASS

The 2015 primary paper on exactly this reduced comaximal graph constructs a size-n clique and notes it is total dominating, but gives no lower bound for total domination and no all-set classification, paired parameter, or total-domination polynomial. The 2024 Boolean-blow-up paper gives compatible Artinian structure but studies other invariants. The submitted CRT forcing-cell argument supplies the missing lower bound and works for all semilocal rings.

## value

PASS

This closes the exact-minimum gap left by the known total-dominating construction and strengthens it to every total set, a full polynomial for finite graphs, a paired formula, and semilocal rather than merely Artinian scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
