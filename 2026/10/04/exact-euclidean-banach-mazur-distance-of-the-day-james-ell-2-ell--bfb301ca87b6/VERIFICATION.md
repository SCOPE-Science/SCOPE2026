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

The claim is proved analytically. Write \(u=(x+y)/\sqrt2\) and \(v=(x-y)/\sqrt2\). Then
\[
N^2=\begin{cases}u^2+v^2,&|u|\ge|v|,\\2v^2,&|v|\ge|u|.\end{cases}
\]
For an arbitrary Euclidean pullback quadratic form \(q\), averaging \(q\) with its image under the coordinate swap preserves any bounds \(mN^2\le q\le MN^2\) and therefore cannot worsen distortion. The averaged form is diagonal in \((u,v)\), so after scaling it is \(q_t=u^2+tv^2\) with \(t>0\).

The complete ratio extrema are
\[
\left\{1,\frac t2,\frac{1+t}{2}\right\}.
\]
Hence the squared distortion is \(2/t\) for \(0<t\le1\), \(1+1/t\) for \(1\le t\le2\), and \((1+t)/2\) for \(t\ge2\). Its minimum is exactly \(3/2\) at \(t=2\). This verifies the claimed Banach--Mazur distance over all invertible linear maps.

For \(C_{\mathrm{NJ}}\), the pair \((1,0),(0,1)\) attains \(3/2\). The parallelogram law for every Euclidean pullback gives the upper bound \(C_{\mathrm{NJ}}\le d_{\mathrm{BM}}^2\), so equality follows from the exact distance.

Limits: the verification is specific to the real two-dimensional Day--James \(\ell_2-\ell_1\) norm. It neither proves a general Day--James formula nor classifies every optimal isomorphism.
