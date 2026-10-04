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

The verification is symbolic and has two parts.

First, expand the source's three conditional abbreviations:
\[
N(x)=\neg(F(x)>\bot),
\]
\[
x<y=N(x)\wedge N(y)\wedge((F(x)\vee F(y))>\neg F(y)),
\]
\[
x\equiv y=N(x)\wedge N(y)\wedge((F(x)\vee F(y))>(F(x)\wedge F(y))).
\]

No other definition or axiom introduces \(>\). Therefore every translated sentence has conditional depth one and every conditional operand is quantifier-free and conditional-free.

Second, the source's reverse-direction model was checked directly. With
\[
f(X,n)=\{\min(X\cap[n,\infty))\}
\]
when the tail is nonempty and \(f(X,n)=\varnothing\) otherwise, Success, Weak Centering, and Uniqueness are immediate. Uniformity follows because mutual containment of the two selected minima forces those minima to be equal, with the empty-tail case handled symmetrically.

At world \(0\), interpreting \(F\) by
\[
I(F,k)=\{k\}
\]
makes \(N\) universal on the domain, the encoded order ordinary strict order, and encoded equivalence ordinary equality. The source's \(Z,S,A,M\) then become zero, successor, addition, and multiplication, so \(\mathrm{AX}\) holds.

For every arithmetic sentence \(\alpha\), the source's forward interpretation and this checked reverse model give
\[
\mathbb N\models\alpha
\iff
\mathrm{AX}\to\alpha^*
\text{ is weakly Stalnakerian-valid}.
\]

Corollary 1 of the source identifies weakly Stalnakerian and Stalnakerian validity. Since true arithmetic is not arithmetical and the translation is computable, each restricted validity set is non-arithmetical.

## Limits

Only arithmetic sentences are used. No claim about open-form translation is needed.

No finite test substitutes for the semantic proof. The result does not locate the restricted validity set in the analytical hierarchy and does not bound ordinary first-order quantifier depth.
