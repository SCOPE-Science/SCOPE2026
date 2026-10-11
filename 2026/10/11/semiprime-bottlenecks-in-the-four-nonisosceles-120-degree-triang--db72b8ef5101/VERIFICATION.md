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

The nonstandard inputs are the following published statements for coprime positive integer tile sides \((a,b,c)\):
\[
c^2=a^2+ab+b^2,
\qquad
\Omega(a+b)\ge2,
\]
and the four necessary tile-count formulas
\[
N=3\lambda^2(a+2b)(a+b),
\]
\[
N=\lambda^2(2a+b)(a+b),
\]
\[
N=\frac{\lambda^2(a+b)}{b},
\qquad
\frac{\lambda^2}{b}\in\mathbb Z_{>0},
\]
and
\[
N=\lambda^2(a+2b)(2a+b).
\]

Because \(\Omega(xy)=\Omega(x)+\Omega(y)\), the first two bounds are exact consequences of the displayed factors and compositeness of \(a+b\).

For the third case, writing
\[
m=\frac{\lambda^2}{b}
\]
gives
\[
\Omega(N)=\Omega(m)+\Omega(a+b).
\]
Thus \(\Omega(N)=2\) exactly when \(m=1\) and \(\Omega(a+b)=2\).

For the fourth case, each linear factor exceeds \(1\), hence \(\Omega(N)=2\) exactly when \(\lambda=1\) and both linear factors are prime. Equality of those primes would force \(a=b\), incompatible with \(c^2=3a^2\). A factor equal to \(3\) would force \(a=b=1\), incompatible with \(c^2=3\).

The bundled checker enumerates primitive integral solutions in a finite range and verifies these implications for multiple \(\lambda\). This is only a stress test. The general proof is the exact factor argument above.

The two arithmetic examples are verified by direct substitution:
\[
19^2=5^2+5\cdot16+16^2,
\qquad
\frac{4^2(5+16)}{16}=21,
\]
and
\[
7^2=3^2+3\cdot5+5^2,
\qquad
(3+2\cdot5)(2\cdot3+5)=143.
\]
They are not existence certificates for tilings.
