---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The exact proof is analytic. `verify.py` is a finite corroboration tool: it recomputes the degree-two kernel average and the closed boundary formula with exact rational arithmetic for \(2\le N\le400\), then compares the lattice-phase approximation with the exact boundary formula numerically for \(100\le N\le20000\).

The finite computation does not prove the identities for all \(N\), does not prove the uniform Stirling remainder, and is not an independence certificate. Those parts are established in the written proof by the binomial second-difference identity and uniform Stirling expansion.
