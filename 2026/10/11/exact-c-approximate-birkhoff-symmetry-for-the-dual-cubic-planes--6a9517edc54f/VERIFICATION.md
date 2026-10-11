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
For unit vectors in the real cubic plane, all ordered Birkhoff--James pairs can be reduced to
\[
x(t)=\frac{(1,t)}{(1+t^3)^{1/3}},\qquad y(t)=\pm\frac{(-t^2,1)}{(1+t^6)^{1/3}}.
\]
The reverse norming-functional value equals
\[
D(t)=\frac{|t-t^4|}{(1+t^3)^{1/3}(1+t^6)^{2/3}}.
\]
After setting \(u=t^3\) and \(k=(1-u)/(1+u)\) on \(0\le u\le1\),
\[
D^3=\frac{k^3(1-k^2)}{(1+k^2)^2},\qquad
\frac{d}{dk}D^3=\frac{k^2(3-6k^2-k^4)}{(1+k^2)^3}.
\]
The unique interior maximum has \(k^2=2\sqrt3-3\) and
\[
D_{\max}^6=\frac{78\sqrt3-135}{16}.
\]
The attached `verify.py` uses exact symbolic differentiation and radical simplification, then independently checks representative primal/dual norming-functional identities and numerical samples. The continuum theorem follows from the displayed derivative sign and all-parameter support-functional classification, not from samples.

The same-model assessment concerns the mathematical claim above; independent audit and validation have not been performed.
