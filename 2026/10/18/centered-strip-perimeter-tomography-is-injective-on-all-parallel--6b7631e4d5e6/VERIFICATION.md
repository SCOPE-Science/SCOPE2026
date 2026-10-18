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

# Mathematical verification

The formulas apply to \(K=\{sa+rb:|s|,|r|\le1\}\) with \(0<t<\min\{C/A,C/B\}\), using \(A=\|a\|_2\), \(B=\|b\|_2\), \(C=|\det(a,b)|\), \(U=|u\cdot a|\), and \(V=|u\cdot b|\). The three strict chambers are \(U+t<V\), \(V+t<U\), and \(|U-V|<t<U+V\); wall cases follow by continuity.

**Hand-verifiable symbolic identity.** Substituting signed linear forms \(X,Y\) in the mixed formula and expanding gives
\[
\frac{XY}{4}(M(u)+M(-u))
=(X-Y)(AY-BX)-Ct.
\]
The right side equals \(-Ct\ne0\) on any direction where \(X=Y\ne0\), which exists by independence. If mixed and pure germs agreed on any open arc, multiplication by their three linear denominators would create a trigonometric-polynomial identity, hence equality on every direction. Such equality would force the mixed germ to be odd under \(u\mapsto-u\), contradicting the displayed identity. This argument is an exact proof, not a numerical certificate.

**Geometric cross-check.** Run `python3 verify_formula.py`. It constructs polygons, clips them successively against \(\langle u,x\rangle\le t\) and \(-\langle u,x\rangle\le t\) using exact Euclidean segment interpolation in floating arithmetic, and compares the perimeter of each clipped polygon to the case-formula perimeter. Its pseudorandom sample and tolerance are reproducible, but a finite experiment cannot verify an all-direction or all-parallelogram conclusion.

**Scope of verification.** No independent audit, formal-proof environment, or universal computational search was performed. Originality risks are discussed in REVIEW.md; the comparison with the inaccessible full text of *Thick Sections of Convex Bodies* was limited to its abstract and the explicit description in the 2026 source.
