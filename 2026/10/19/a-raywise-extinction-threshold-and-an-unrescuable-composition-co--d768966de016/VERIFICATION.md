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

# Verification and reproducibility

Run `python3 CHECK.py` with Python 3.10 or later. Its standard-library-only exact rational loop checks the normalized three-species identities in 153 strictly positive grid configurations; its floating-point checks illustrate the two real symmetric biomass equilibria for \(d=1/20\), \(\gamma=1\), and validate the stated no-rescue cone aperture formula. The actual checker was run successfully from the provided package.

The full logical proof is in `RESULT.md`: the derivative of the normalized product, scalar order and convergence, uniqueness of the threshold orbit, and exponential transformation in the no-rescue cone. Finite sampling and numerical root finding are diagnostic checks only, not certification of the infinite assertions.

The 2012 historical open-cycle reference was available only in indexed abstract/excerpt form; the absence of complete full text limits originality review. Independent scientific audit: not performed.
