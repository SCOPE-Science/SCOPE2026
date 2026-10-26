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

Run `python3 verify.py` with Python 3 and no third-party packages. The successful final line is `VERIFY_OK: 8 exhaustive finite-field/quiver cases`. The program exhaustively enumerates every arrow-scalar assignment for four stated finite quivers over \(\mathbb F_2\) and \(\mathbb F_3\), rejects assignments violating length-two zero relations, computes orbits under all vertex scalings, and checks the formula support-by-support. It also directly counts endomorphisms and automorphisms for each valid assignment. These tests validate only the listed finite cases. The general result is proved symbolically in `RESULT.md`; independent mathematical audit and independent validation have not been performed.
