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

The proof was reconstructed from the definitions and checked independently of the literature search.

**Centralization.** If a rectangle in a centrally symmetric convex body has center \(c\) and vertices \(c\pm u\pm v\), then for each sign choice the centered vertex \(\pm u\pm v\) is the midpoint of \(c\pm u\pm v\) and the reflection of \(c\mp u\mp v\). Both points lie in the body, so convexity puts the midpoint in the body. The new rectangle has the same side vectors and area.

**Diagonal coordinates.** With half-diagonals \(p=u+v\) and \(q=u-v\), orthogonality \(u\perp v\) gives \(|p|=|q|=r\), and the rectangle area is exactly
\[
2r^2\sin\delta,
\]
where \(\delta\) is the acute angle between the two diagonal lines.

**Regular-polygon radial function.** For \(\alpha=\pi/n\), a ray at angular distance \(s\in[0,\alpha]\) from a nearest vertex ray reaches radius
\[
\rho(s)=R\frac{\cos\alpha}{\cos(\alpha-s)}.
\]
This follows from the apothem \(R\cos\alpha\).

**Case \(4\mid n\).** The inequalities \(r\le R\) and \(\sin\delta\le1\) give area at most \(2R^2\), attained by orthogonal vertex lines.

**Case \(n\equiv2\pmod4\).** The vertex lines form an odd cyclic lattice whose largest acute separation is \(\delta_0=\pi/2-\alpha\). For \(\delta\le\delta_0\), the area is at most \(2R^2\cos\alpha\). For \(\delta=\delta_0+t\), the nearest-vertex-line distances satisfy \(s_1+s_2\ge t\), so
\[
r\le R\frac{\cos\alpha}{\cos(\alpha-t/2)}.
\]
Substitution reduces the desired bound to
\[
\cos\alpha\cos(\alpha-t)
\le
\cos^2\!\left(\alpha-\frac t2\right),
\]
and the difference of the two sides is exactly \((1-\cos t)/2\). Strictness for \(t>0\) gives the equality classification among centered rectangles.

A dense angular sweep for \(n\in\{6,10,14,18\}\) independently reproduced the predicted maxima to grid precision. That computation was only a sanity check; the theorem is proved analytically.

No statement is verified here for odd regular polygons or for maximum perimeter.
