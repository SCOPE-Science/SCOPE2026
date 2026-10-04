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

The theorem is verified by an exact analytic reduction and a supplementary exact-arithmetic replay.

1. In orthogonal coordinates \(u=(x+y)/\sqrt2\), \(v=(x-y)/\sqrt2\), the norm is invariant under independent sign changes. Averaging any candidate positive-definite quadratic form over these isometries preserves its two comparison constants and removes the mixed term. Therefore no nonsymmetric Euclidean pullback can improve on a form \(u^2+t v^2\).
2. On \(0\le v/u\le1\), the exact squared-norm ratio is \((1+s)^2/[2(1+t s^2)]\), whose derivative has the sign of \(1-ts\). On the complementary sector it is \(2/(t+r^2)\), which is decreasing.
3. These extrema yield \(D(t)=4/t\) for \(0<t\le3\) and \(D(t)=(t+1)^2/(4t)\) for \(t\ge3\). Hence the exact minimum is \(D(3)=4/3\).
4. Since \(u^2+3v^2=2(x^2-xy+y^2)\), the rescaled optimal form is \(|(x,y)|_*^2=x^2-xy+y^2\). Its matrix has eigenvalues \(1/2\) and \(3/2\), so it is positive definite.
5. The lower comparison equality is attained at \((1,1)\) and \((1,0)\); the upper comparison equality is attained at \((1,-1)\).

The bundled `verify.py` checks the coordinate identity and equality-witness ratios using exact rational arithmetic. It is not used to infer the global theorem from finite sampling. The only unproved external statement used in the comparison section is the published Yang–Wang value \(C_{\mathrm{NJ}}=(3+\sqrt5)/4\); it is not needed for the Banach–Mazur proof itself.
