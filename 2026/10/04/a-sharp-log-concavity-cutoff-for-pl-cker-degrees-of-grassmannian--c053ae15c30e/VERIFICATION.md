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
The bundled `verify.py` uses exact Python integers and rational arithmetic. It recomputes the factorial Plücker degree, checks symmetry and strict central growth for \(2\le n\le100\), exhaustively checks every log-concavity inequality for \(2\le n\le11\), confirms the first failure at \((n,k)=(12,2)\), and verifies \(Q_{11}=437/442\) and \(Q_{12}=3795/2584\). It also checks the algebraic polynomial identity controlling the monotonicity of \(Q_n\) through \(n=1000\).

The infinite conclusion does not rely on the finite loop: the written proof shows that \(Q_{n+1}/Q_n-1\) has positive numerator \(11(n-5)^3+94(n-5)^2+199(n-5)+56\) for every integer \(n\ge5\). Thus \(Q_n>1\) for all \(n\ge12\).

The finite range \(2\le n\le11\) is exhaustive and exact, so no numerical tolerance or floating-point decision is involved. The checker does not claim to certify novelty or literature completeness.
