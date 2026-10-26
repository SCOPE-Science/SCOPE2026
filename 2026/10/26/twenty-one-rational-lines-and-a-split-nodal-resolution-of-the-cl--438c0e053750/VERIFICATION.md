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

# Reproducibility and scientific limits

The complete standalone Python 3 program is `verify.py`. Invoke `python3 verify.py` in the directory containing that file. It uses only the Python standard library and exact finite-field arithmetic. Successful output includes the projective-point counts for \(q=5,25\), the six directions and full conic counts, the exhaustive \(806\)-candidate line enumeration over \(\mathbb F_5\), the \(21=6+15\) line split, the \(15\) diagonal lines, and the \(120\) distinct ordered triples in the \(S_5\) action, ending in `VERIFY_OK`.

The program enumerates **rational** lines and points only over the two explicitly implemented finite fields; it does not enumerate all extensions or certify geometric lines over an algebraic closure. Those stronger statements are proved in `RESULT.md` by the gradient, Bézout, blowup, adjunction and arithmetic arguments. No external or independent audit has been performed.
