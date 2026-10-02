---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Reconstruction from the actual voltage assignment gives a symmetric 6-regular 21-vertex K7 3-cover. Exact integer power traces are Tr(A^k)=(0,126,204,2074,7750,54636) for k=1..6. The old sixth trace is 6^6+6=46662, so Tr_new(A^6)=7974<8000=(2*sqrt(5))^6; since sixth powers are nonnegative, every new eigenvalue satisfies |lambda|<2*sqrt(5). The checked exact expected-trace enumerator yields ETr=(0,126,210,2226,7770,59136), hence ETr_new(A^6)=12474 and the stated existence bound. Newton identities give the listed leading coefficients. The Cheeger lower bound follows from lambda_2<4.5 and 6-regularity.

## originality

PASS

Best-of-knowledge originality passes: the checked covering literature gives general 2-lift/r-covering or asymptotic theory, while the exact 21-vertex non-bipartite K7 3-lift voltage witness and its six-moment table were not located elsewhere.

## value

PASS

A concrete two-sided Ramanujan 3-cover of the non-bipartite base K7 together with an exact low-moment calculation is a natural finite spectral-graph benchmark not mechanically supplied by the standard 2-lift or asymptotic random-lift results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
