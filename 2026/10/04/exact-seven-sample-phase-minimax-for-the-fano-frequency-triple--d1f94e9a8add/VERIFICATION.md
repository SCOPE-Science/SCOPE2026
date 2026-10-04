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

The proof is analytic. The checker performs the following corroborative checks from exact algebraic data:

- expands the sampled Laurent polynomial \(q_k=|1+u\zeta^k+v\zeta^{3k}|^2\) in the group algebra of \(\mathbb Z_7\);
- verifies exactly \(m_1=3\) and \(m_2=15\);
- verifies the exact Laurent formula \(m_3-84=3(3+X+X^{-1}+Y+Y^{-1}+XY+(XY)^{-1})\), whose bracket is \(|1+X+Y^{-1}|^2\);
- verifies exactly \(m_4=(52/3)m_3-973\);
- verifies the coefficient reduction of the quartic certificate \(x(A-x)(x-B)^2\) to \(-(41+3\sqrt{21})(m_3-84)/6\);
- evaluates the displayed cubic-root phase witness on all seven roots to confirm one zero and two three-point levels equal to the two roots of \(x^2-7x+7\).

Run `python3 artifacts/verify.py`. A successful replay prints `VERIFY_OK`.

The numerical witness evaluation is not used to prove the lower bound; it only checks the explicitly derived extremizer values. No statement for other frequency triples or moduli is verified.
