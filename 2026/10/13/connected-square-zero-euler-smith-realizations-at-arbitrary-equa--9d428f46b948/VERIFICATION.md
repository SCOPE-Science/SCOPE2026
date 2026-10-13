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

The proof is algebraic and uniform in \(k,m\ge1\). The following exact checks establish the claim.

1. The binomial coefficient split gives \(f_m(x)-1=p_+(x)-p_-(x)\) with \(p_+,p_-\in\mathbb Z_{\ge0}[x]\) and zero constant term.
2. The coefficient of \(x^2\) in every off-diagonal entry of \(N_{k,m}(x)\) is \(m>0\), so the vertex graph is complete and the algebra is connected.
3. Direct collection of diagonal and off-diagonal terms gives \(I_r+N_{k,m}=f_m I_r+p_-J_r\).
4. A constant rational basis adapted to the all-ones line and the sum-zero hyperplane reduces this matrix to one factor \(f_m+r p_-\) and \(k\) factors \(f_m\).
5. With \(x=1+t\), \(f_m(1+t)=(-t(2+t))^m\) has exact \(t\)-adic valuation \(m\).
6. The odd-binomial identity gives \(p_-(1)=2^{m-1}\), so \(f_m(1+t)+r p_-(1+t)\) has nonzero constant term \(r2^{m-1}\) and is a unit in \(\mathbb Q\llbracket t\rrbracket\).
7. Hence the local Smith exponents of the Cartan matrix are \((0,m,\ldots,m)\); inversion reverses sign and order, yielding \((-m,\ldots,-m,0)\).

The calculation is performed over \(\mathbb Q\llbracket t\rrbracket\), as required by the graded-dimension definition, so no base-field characteristic exception is introduced. No computation beyond these identities is needed. The result does not claim arbitrary mixed profiles, uniqueness, or minimality.
