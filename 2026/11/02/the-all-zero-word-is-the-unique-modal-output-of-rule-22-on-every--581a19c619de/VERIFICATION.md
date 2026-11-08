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

The four pair-state matrices A0,A1 count every indexed cyclic input with fixed one-step Rule22 output by trace product; cyclic rotation allows any nonzero output to end in A1. The coordinatewise envelope of arbitrary A0/A1 row-products reaches (1,1,1,1) after two steps from each unit row and follows (a,a,b,c)->(b,b,c,a+c), bounding every nonzero fiber by u_n=2a_{n-1}+b_{n-1}. The zero-output trace gives P_n(0^n)=1+tr(B^n)=1+t_n with t_0=3,t_1=t_2=1 and t_n=t_{n-1}+t_{n-3}. Both u and t satisfy same recurrence, differences at n=3,4,5 are 1,2,2, so remain >0 for every n>=3. Independently enumerated all inputs for rings n=3..12, maximum fibers 5,6,7,11,16,22,32,47,68,99, unique at zero. The all-length result follows from matrix induction, not this finite census.

## originality

PASS

Jen (1989) gives finite open-block Rule22 predecessor recurrences and maximal growth, not the claimed exact unique all-zero maximal fiber over every indexed periodic ring n>=3; finite-seed Exactly 1 dynamics and de Bruijn studies address other issues. An older combinatorial specialization of general preimage machinery could imply this recurrence, but exact cyclic strict mode was not found in the inspected primary sections.

## value

PASS

The modal output is the exact maximum of a natural finite-volume deterministic CA push-forward distribution, not a random selected pattern. A strict all-n transfer-matrix envelope and explicit predecessor counts make it useful despite leaving the full fiber distribution open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
