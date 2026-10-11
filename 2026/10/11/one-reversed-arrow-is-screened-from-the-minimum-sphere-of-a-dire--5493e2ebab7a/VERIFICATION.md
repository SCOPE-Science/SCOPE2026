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
The complete proof is in `RESULT.md`; it applies for all integer \(m\ge3\) and every reversal position. The essential facts are the signed Gram tridiagonal identity, the exact quadratic-block difference equation, the cubic sum identity for normalization, the weighted squared-distance optimality certificate, and the exact flipped-vertex gap \(\lambda(m-3)\).

`verify.py` uses Python exact `fractions.Fraction` arithmetic to reconstruct every incidence vector, center, squared norm, and vertex distance for all \(3\le m\le25\) and every flip position (322 exact instances). It checks every weight sum and the position dependence. An independent nonlinear constrained minimax solver examines 52 full-ball problems for \(3\le m\le10\). Neither finite enumeration nor solver termination is used as the proof of the infinite theorem, and neither assesses literature novelty.
