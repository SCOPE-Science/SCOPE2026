---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For p odd, p∤a, b>a, p|(b−a), d=a+b is a unit and v=(aα+bβ)/d is recovered from the degree-(d−1) coefficient. The invertible change α=v+bw, β=v−aw gives F(T)=(U−bw)^a(U+aw)^b. In characteristic p, b−a=p^e c and b≡a yield (1−bz)^a(1+az)^b=(1−a²z²)^a(1+az^{p^e})^c. Exactly w² and w^h (h=p^e odd) are recovered by nonzero coefficients −a³ and ac; all other exponents lie in <2,h>. Hence each finite-roots chart is k[v,w²,w^h]=k[v,x,y]/(y²−x^h), reduced and irreducible. Normalization k[v,w] is same fraction field, proper finite/birational globally; all forms in locus fit some linear-coordinate finite-root chart. Numerical-semigroup gaps 1,3,...,h−2 imply defect (h−1)/2 and conductor w^{h−1}; characteristic-p Jacobian of y²−x^h gives (2y,−h x^{h−1},y²−x^h)=(y,x^h), transverse singular length h. Independently recalculated examples (p,a,b)=(5,2,27), h=25, delta=12, and (3,2,11), h=9, delta=4; finite tests support rather than prove unrestricted result.

## originality

PASS

Best-of-knowledge PASS: characteristic-zero coincident-root loci have established normalization and pure-power singular support, but the inspected theorems assume characteristic zero, so they do not imply wild exponent h=p^e or characteristic-p Jacobian length; the exact positive-characteristic coefficient identity is substantive. A different unindexed characteristic-p treatment remains plausible.

## value

PASS

A natural positive-characteristic boundary of classical coincident-root surfaces is the collision of two distinct multiplicities congruent mod p. Determining its actual local algebra, normalization conductor, Jacobian thickening and unbounded cusp defect separates wild characteristic behavior from characteristic-zero cusp theory; the exact invariant and growth can inform local singularity and intersection calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
