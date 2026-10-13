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

# Reproduction

Run `python verify.py` using Python 3 and its standard library. The source code is included alongside this document.

The script independently builds and solves the discrete cycle Poisson equation in rational arithmetic, checks the centered-potential closed form for integer cycle sizes \(4\le n\le43\) and all distances \(1\le d\le\lfloor n/2\rfloor\), and checks the exact first-order threshold ratio. A second group evaluates actual finite-graph Kirchhoff indices by rational inversion of shifted Laplacians, at prices immediately below and above the predicted boundary, for sizes \(4\le n\le10\). The observed output is:

`VERIFY_OK 460 exact cycle-Poisson/threshold identities; 32 exact objective-side comparisons`

The finite tests check formulas and example directions; the infinite theorem, strict convexity, uniqueness, and the full price classification rest on the displayed symbolic proof. They do not amount to independent audit or external certification.
