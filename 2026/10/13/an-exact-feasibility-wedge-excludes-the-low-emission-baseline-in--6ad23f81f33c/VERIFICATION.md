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

Let
\[
A=m+(1-\alpha)\delta,
\quad
L=\frac{A(\delta\theta+\varphi)}{2\theta\varphi},
\quad
U=\frac{A^2}{4m\theta-2(1-\alpha)\varphi}.
\]
Since \(A>0\) and \(L>0\), the interval \(L<k<U\) can contain a positive \(k\) only if
\[
4m\theta-2(1-\alpha)\varphi>0.
\]
This gives
\[
m\theta>\frac{(1-\alpha)\varphi}{2}.
\]
On that region,
\[
U-L=
-\frac{(2\delta\theta+\varphi)A
(m\theta+\alpha\varphi-\varphi)}
{2\theta\varphi[2m\theta-(1-\alpha)\varphi]},
\]
so \(U>L\) exactly when
\[
m\theta+\alpha\varphi<\varphi.
\]
Therefore
\[
\frac{(1-\alpha)\varphi}{2}<m\theta<(1-\alpha)\varphi.
\]

At the source baseline
\[
m=\frac25,\qquad
\alpha=\frac15,\qquad
\delta=\frac{17}{20},
\]
the bundled checker evaluates all four combinations of
\[
\theta\in\left\{\frac7{10},\frac{29}{20}\right\},
\qquad
\varphi\in\left\{\frac34,\frac9{10}\right\},
\]
using exact rational arithmetic.

The two low-emission cases have negative upper endpoints and hence no positive feasible \(k\). The high-emission, \(\varphi=3/4\) interval ends at \(729/700<11/10\), excluding both listed baseline \(k\)-values. The high-emission, \(\varphi=9/10\) interval contains both \(11/10\) and \(13/10\).

The result does not compute the constrained Stackelberg optimum outside the stated domain.
