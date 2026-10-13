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

# Verification checks

Execute \(\texttt{python3 verify.py}\) with Python 3 and no third-party dependencies. The checker enumerates all nonzero symmetric binary forms over the prime fields \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\) and the explicitly implemented quadratic field \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). For each form, it checks the invertible similarities and their multipliers; it computes all radical orbits by union-find on the \(q^3\) elements, collapsing socle coordinates when the vector part is nonzero because every linear shift \(\tau:V\to J^2\) is available. It then matches the **complete** orbit-size multiset, not merely its count, with the formula in RESULT.md. The program reports the numbers of tested forms as \(7,26,63,124\), ends in \(\texttt{VERIFY_OK}\), and raises an assertion on disagreement.

All arbitrary-prime-power cases rely on the algebraic proof: the similarity classification of symmetric bilinear planes over finite fields, the square-class multiplier description for rank-one forms, norm surjectivity in the anisotropic case, and explicit transitivity in the characteristic-two nonalternating case. No finite enumeration certifies universal correctness or independent originality.
