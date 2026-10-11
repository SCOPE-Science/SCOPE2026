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

For
\[
\gamma_m=[0;2,m,1,\overline2],
\]
the periodic tail gives
\[
\gamma_m=\frac12-\frac{1}{2(2m+1+\sqrt2)}.
\]
Thus
\[
h_m=\frac{\pi}{2(2m+1+\sqrt2)},
\qquad
R_m=\csc h_m,
\qquad
A_m=\frac{4\pi}{3}\cot^3h_m.
\]

The convergent denominators needed by the source theorem are
\[
q_2=2m+1,\qquad q_3=2m+3,\qquad q_4=6m+7.
\]
For \(m\ge2\), the proof gives a uniform strict bound for the source's bounded-tail criterion at \(j_0=3\), so the source theorem certifies all conditions with
\[
k\ge m+2.
\]

For \(2\le k\le m+1\),
\[
\alpha_k=\frac\pi2-(2k-1)h,
\qquad
\beta_k=\frac\pi2-(2k-3)h.
\]
Direct substitution into the source definitions gives
\[
F_-(\alpha_k)
=
\arcsin\!\left(\frac{\sin h}{\sin((2k-1)h)}\right)-h,
\]
and
\[
F_+(\alpha_k,\beta_k)
=
h-\arcsin\!\left(\tan h\,\sin(2(k-1)h)\right).
\]

For \(2\le k\le m\), the plus inequality follows from \(F_+<h<\delta_{k+1}\), while the minus inequality is equivalent to
\[
3\sin h<\sin((4k-1)h).
\]
The proof bounds the right side from below at the two endpoints of its possible angular interval.

At the transition \(k=m+1\),
\[
\alpha_{m+1}=\sqrt2h,\quad
\beta_{m+1}=(2+\sqrt2)h,\quad
\delta_{m+2}=(2-\sqrt2)h.
\]
The two source inequalities reduce respectively to
\[
2\sin h<\sin(3h)+\sin((3-2\sqrt2)h)
\]
and
\[
\sin(2h)>\tan(\sqrt2h),
\]
both proved uniformly from \(h<1/4\).

The bundled checker independently evaluates the source functions and verifies the entire finite prefix for \(2\le m\le100\), together with thousands of later indices for representative values. Those computations are stress tests only; the analytic proof establishes every \(m\ge2\) and every required \(k\).

Unproved limits: no positive-measure-at-infinity theorem, no density estimate for the admissible set, no classification of all quadratic admissible rotations, and no extension beyond the geometric hypotheses of the cited rigidity theorem.
