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
The exact identity checked is
\[
h_S(x)=h_0(x)\frac{\pi S(x)}{2}\cot\!\left(\frac{\pi S(x)}{4}\right).
\]
Writing \(y=\pi S/4\), differentiation gives
\[
\frac{d}{dy}(2y\cot y)=\frac{2(\sin y\cos y-y)}{\sin^2y}<0,
\]
so the multiplier rises along any strictly decreasing survival function.

For the New X–Lindley baseline, with \(t=\xi z\),
\[
h_0(z)=\xi\frac{1+t}{2+t},\qquad h_0'(z)=\frac{\xi^2}{(2+t)^2}>0.
\]
Thus the SNXL hazard is strictly increasing. The endpoint multiplier values are \(\pi/2\) and \(2\).

For the terminal gap,
\[
2-\Phi(s)=\frac{\pi^2}{24}s^2+O(s^4),
\qquad s=e^{-t}(1+t/2),
\]
and therefore
\[
z(2\xi-h_\xi(z))\to2.
\]

The included checker tests the closed formulas at multiple scales and confirms the terminal constant numerically. Those finite checks are not used as proof. The older Sin-G result \(h_S\sim2h_0\) is treated as prior coverage of the zeroth-order terminal level, not as new evidence.
