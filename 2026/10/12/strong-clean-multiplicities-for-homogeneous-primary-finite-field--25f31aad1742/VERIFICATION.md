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
# Verification

Run `python3 verify.py` from the extracted package directory.

The checker uses only the Python standard library. It performs the following independent finite tests:

- exact strong-clean counts for neutral scalar and Jordan examples over \(\mathbb F_3\) and \(\mathbb F_5\);
- a mixed \(0\)-, \(1\)-, and neutral-primary example over \(\mathbb F_3\);
- a mixed linear and irreducible-quadratic example over \(\mathbb F_3\);
- two copies of the irreducible quadratic primary module over \(\mathbb F_2\), giving \(22\) decompositions;
- every \(2\times2\) matrix over \(\mathbb F_2\) and \(\mathbb F_3\) for the equivalence between unique strong cleanness and nilpotence of \(A-A^2\);
- every idempotent in \(M_2(\mathbb F_3[u]/(u^2))\), yielding \(110\);
- every idempotent in \(M_2(\mathbb F_2[u]/(u^3))\), yielding \(98\).

A successful replay ends with `VERIFY_OK`.

These are finite consistency checks. They do not certify all finite fields or dimensions; the universal claim is proved symbolically in `RESULT.md`.
