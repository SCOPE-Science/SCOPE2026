---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Set y=|u_prime|^(p-2)u_prime. The equation at gamma=0 gives y(t)=c-A(t), so both Neumann and periodic derivative endpoint conditions require A(T)=0. The two-step primitive traverses [0,M] once in each direction; Neumann fixes c=0 and yields a unique derivative up to an additive solution constant. Periodicity of position requires integral phi_q(c-A)=0, equivalently |c|^q=|c-M|^q, hence c=M/2 uniquely. Integrating absolute derivative on both branches gives Delta_N=(T/q)M^(q-1), Delta_P=(T/q)M^(q-1)/2^q; q=p/(p-1). Independent exact substitutions p=2,3,4 at T=3,M=2 reproduced ratios 1/4,2^(-3/2),2^(-4/3). Any sufficiently large additive shift is positive; no false uniqueness of absolute level claimed.

## originality

PASS

The closest Cagnetta 2026 paper explicitly excludes gamma=0, with Remark 4 giving only degeneracy and zero mean for scalar closure. Its full main result treats gamma outside {0,p-1}; it does not compute Neumann and periodic solution shapes or exact universal oscillation ratio. Nondegenerate Boscaggin–Feltrin–Zanolin time-map estimates have a different premise.

## value

PASS

The omitted gamma=0 boundary regime is a natural structural endpoint of an active uniqueness theorem. Classifying both boundary conditions modulo the correct symmetry and giving a sharp universal oscillation ratio is a useful exact completion, despite elementary solvability once the degeneracy is isolated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
