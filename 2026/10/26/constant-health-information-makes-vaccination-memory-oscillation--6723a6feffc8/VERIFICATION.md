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

For positive I, averaging d log I gives mean S=delta/beta. Averaging dI and dS yields mean I=(mu/delta)(q-mean p). Averaging d log[p/(1-p)] yields mean I=alpha mean p-eta E(1/p), since normalized delay preserves stationary mean p. The unique interior equilibrium satisfies analogous I*=alpha p*-eta/p* and I*=(mu/delta)(q-p*). Subtraction gives (alpha+mu/delta+eta/(p* mean p))(mean p-p*)=eta(E1/p-1/mean p). The last term equals E[(p-mean p)^2/p]/(mean p)^2>0 for nonconstant p, proving discount; at eta=0 means coincide. Stationary measure extension follows by bounded observables and invariance, not numerical periodic orbit existence. Sympy identity and a rational formula check independently passed.

## originality

PASS

Best-of-knowledge original on the stated restricted theorem after comparison of exact implications; no exhaustive priority claim and specified inspection limits remain.

## value

PASS

A finite-amplitude invariant mean identity identifies a strict campaign-dependent reduction in average prevalence independent of delay-kernel shape. It explains a qualitative distinction between oscillatory and endemic burden beyond local linear stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
