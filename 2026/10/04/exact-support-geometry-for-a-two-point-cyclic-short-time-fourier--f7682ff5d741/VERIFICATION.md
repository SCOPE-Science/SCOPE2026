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

`verify_two_point_stft.py` uses integer combinatorics only. For every \(3\le N\le12\), every nonzero \(a\in\mathbb Z_N\), and every nonempty \(S\subseteq\mathbb Z_N\), it computes \(A_a(S)\), \(E_a(S)\), and \(Q_a(S)\), constructs coefficients with the predicted maximum number of good internal edges, and checks that the resulting STFT support count equals the theorem's formula. This covers \(81{,}855\) support cases.

The script also evaluates the proved component minima for every \(3\le N\le5000\) and every nonzero \(a\), covering \(12{,}497{,}499\) parameter pairs and confirming the global dichotomy. A successful replay prints `VERIFY_OK`.

The finite replay corroborates the implementation and boundary cases. The infinite theorem rests on the root-of-unity slice calculation and the cycle argument in `RESULT.md`; finite enumeration is not used as a substitute for that proof.
