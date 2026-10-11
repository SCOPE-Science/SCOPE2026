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
The verification target is the source-reduced function
\[
\Phi(t)=\frac{f(t)^2+f(-t)^2}{5g(t)^2}
\]
for the regular-octagonal norm
\[
N_8(s,u)=\max\left\{|s|,|u|,\frac{|s|+|u|}{\sqrt2}\right\}.
\]

For \(0\le t\le1\), exact facet comparison gives breakpoints
\[
d=5\sqrt2-7,
\qquad
a=\sqrt2-1,
\qquad
c=\frac{5\sqrt2-1}{7},
\]
with
\[
0<d<a<c<1.
\]
The four exact pieces are
\[
\frac{t^2+9}{10},
\quad
\frac{3t^2+14t+17}{20},
\quad
\frac{3t^2+14t+17}{10(1+t)^2},
\quad
\frac{5t^2+8t+5}{5(1+t)^2}.
\]
Their derivatives have signs \(+,+,-,-\), so the maximum is at
\[
t=\sqrt2-1.
\]
The exact reciprocal identity
\[
\Phi(t)=\Phi(1/t)
\]
extends the conclusion to \(t\ge0\).

`verify.py` implements arithmetic in \(\mathbb Q(\sqrt2)\), checks the breakpoint order and continuity, reconstructs the norm branches, verifies the equality value, and checks the displayed sharp pair exactly. Rational-grid checks are consistency tests only.

No independent audit or independent validation has been performed.
