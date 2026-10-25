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

# Reproducibility and limits

Run `python3 CHECK.py` using Python 3 and only its standard library. It performs symbolic polynomial arithmetic over \(\mathbb F_2\). Its output on the reviewed package is:

`VERIFY_OK: char2 determinant derivatives, S-pair Groebner proof, six nilpotent products, degree-eight CI Hilbert function 0..20`

The critical infinite proof is given in `RESULT.md`: the three affine charts identify the nonreduced scheme, the nilpotent generator transitions identify \(\mathcal O(-3)\), and the complete-intersection resolution supplies the Hilbert series. Testing finitely many coefficients is only a consistency check. Source comparison is a bounded literature review, not an exhaustive proof of novelty. Independent auditing and external validation have not occurred.
