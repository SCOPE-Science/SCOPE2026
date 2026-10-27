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

# Reproducible checks and bounds

Run `python verify.py` with Python 3 and its standard library. The program enumerates exactly all monic degree-eleven polynomials over \(\mathbb F_2\) at cutoff \(M=2\) for the four shifts \(1,t,t^2,t+1\). It compares local \(P^2\)-level means with the product of exact rational local factors, and bounds the discrepancy between squarefree-truncated and small-prime-truncated correlations by the elementary large-square union bound. Expected result: `VERIFY_OK`.

These are finite regression checks, not a proof of the universal theorem. The proof uses local enumeration of all residue classes mod \(P^2\), the CRT for \(N\ge D_M\), the polynomial prime counting identity, and a convergent Euler-product estimate. Nothing in this package represents independent auditing or infinite computational certification.
