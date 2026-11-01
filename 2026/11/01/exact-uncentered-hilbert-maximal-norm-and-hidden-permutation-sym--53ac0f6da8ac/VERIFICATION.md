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

# Reproducible mathematical verification

Execute `python3 verify_c4_uncentered.py` using the Python 3 standard library. The checker recomputes all three strict Sylvester certificates for the losing uncentered averaging choices, the full characteristic polynomial of the surviving Gram matrix, the rational root isolation and eigenvector identities, and **all 81 centered averaging selections**. These are exact rational computations and do not depend on floating-point tolerance.

The analytic proof in `RESULT.md` proves that these finite matrices exactly represent all graph-distance ball choices, that the winning Perron eigenvector lies in the active sorted region, and that every equality case arises by permutation, input signs and scaling. The code corroborates precisely the finite computations used in that proof. The graph has four vertices; there is no assertion that an enumeration over this graph proves a statement about arbitrary graph orders. Independent external audit has not been performed.
