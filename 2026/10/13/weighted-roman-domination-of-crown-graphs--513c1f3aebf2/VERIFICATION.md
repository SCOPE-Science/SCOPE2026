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

The analytic proof reduces every optimum to six possible support types according to the numbers of label-\(2\) vertices on the two shores. The bundled `verify_weighted_roman_crown.py` independently evaluates the definition and the six-term formula.

The checker exhausts every weight vector in \(\{1,2,3\}^{6}\) for \(\operatorname{Cr}_3\), and for each such vector enumerates all \(3^6\) labelings. It also tests deterministic integer-weight profiles on \(\operatorname{Cr}_4\) and \(\operatorname{Cr}_5\) and includes profiles where the asymmetric \((2,1)\), \((1,2)\), and \((2,2)\) regimes are optimal.

These finite computations do not prove the theorem for arbitrary positive real weights or unbounded \(n\). That infinite statement is established by the support-type proof in `RESULT.md`.
