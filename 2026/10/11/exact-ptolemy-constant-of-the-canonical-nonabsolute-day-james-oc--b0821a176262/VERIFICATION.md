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

The independent half of the unit-ball boundary has vertices
\[
(0,-1),\quad(1,-1),\quad\left(1,\frac17\right),\quad
\left(\frac23,\frac23\right),\quad(0,1).
\]
For
\[
q(a,b)=a^2+\frac{10}{13}ab+b^2,
\]
the four consecutive edge minima are
\[
\frac{144}{169},\qquad\frac{144}{169},\qquad
\frac{72}{65},\qquad\frac{64}{65},
\]
and the five vertex values are
\[
1,\qquad\frac{16}{13},\qquad\frac{720}{637},\qquad
\frac{16}{13},\qquad1.
\]
Therefore
\[
m=\frac{144}{169},\qquad M=\frac{16}{13},\qquad\frac Mm=\frac{13}{9}.
\]

For
\[
x=\left(-\frac23,-\frac23\right),\quad
y=\left(\frac32,-\frac32\right),\quad
z=\left(\frac56,-\frac{13}{6}\right),
\]
direct evaluation gives
\[
N(x)=1,\quad N(y)=\frac32,\quad N(z)=\frac{13}{6},
\]
\[
N(x-y)=\frac{13}{6},\quad N(x-z)=\frac32,\quad N(z-y)=1,
\]
so the exact Ptolemy ratio is \(13/9\).

The accompanying checker repeats these computations with exact rational arithmetic. No finite grid, floating-point optimization, timeout, or partial enumeration is used to establish a continuous claim.
