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

Run `python3 verify.py` with Python 3.8 or later. No third-party packages or network access are required. The script directly generates every generator-image Lie homomorphism in \((n,q)=(2,2),(2,3),(3,2)\), filters idempotents, computes full matrix composition to enumerate commuting pairs and triangles, and compares the resulting arity-one, -two, and -three tuple counts with the closed weak-composition formula. It also performs direct maximal-clique enumeration for the two rank-two examples. A successful run prints `VERIFY_OK`.

The checked results are \((14,88,452,12)\) for \((n,q)=(2,2)\), \((38,292,1664,54)\) for \((n,q)=(2,3)\), and \((1122,66532,1386792)\) for \((n,q)=(3,2)\), with the last case omitting exhaustive maximal-clique enumeration. For \(q=3\), only the prime field is exercised; the abstract proof covers all prime powers.

Computer enumeration does not certify formulas beyond those small cases; the unrestricted theorem is established by the proof in `RESULT.md`. No independent mathematical audit has been performed.
