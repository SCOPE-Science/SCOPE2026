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
# Verification of the band-projection defect threshold

The theorem is analytic. The required computations are the exact factorization
\[
2GG''-(G')^2=4(1+r^p)^{2/p-2}(1+(p-1)r^p)(H_p(r^p)-c),
\]
where \(G(r)=(1+r^p)^{2/p}-cr^2\) and
\[
H_p(z)=\frac{(p-1)z^{(p-2)/p}(1+z)^{2/p}}{1+(p-1)z}.
\]
A separate symbolic differentiation and simplification in SymPy returned identically zero for the difference between both sides (assuming positive parameters), and independently returned the exact logarithmic derivative
\[
-\frac{(p-2)(z-1)}{p z(1+z)(1+(p-1)z)}.
\]
The sign calculation, the limiting values at zero, and the perspective convexity proof supply the infinite-parameter proof. Numerical crosschecks used \(p=5/4,3/2,7/4,2,5/2,3,10\), and confirmed the prescribed balanced minimum or zero-infimum patterns. Such finite checks do not establish the theorem by themselves.

The construction \(f_\pm=(r\pm\varepsilon)u+v\) with disjoint unit vectors is the independently checkable triangle-inequality obstruction whenever \(g''(r)<0\). The admissible boundary is included by nonnegative curvature and separate coordinate monotonicity; the endpoints \(p=1\), \(p=2\) and \(t=0\) are assessed separately. The only claimed domain is finite \(p\), two nonzero bands, and \(0\le t<1\); no claims of independent audit or external mathematical certification are made.
