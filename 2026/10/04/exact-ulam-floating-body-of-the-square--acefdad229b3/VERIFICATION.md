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

For \(0<\delta\le2\), normals are reduced by square symmetry to directions proportional to \((1,m)\) with \(0\le m\le1\).

If \(m\le\delta/2\), the cap is the trapezoid
\[
-1\le y\le1,
\qquad
1-\frac\delta2-my\le x\le1.
\]
Its area is \(\delta\), and direct integration gives
\[
\bar x=1-\frac\delta4-\frac{m^2}{3\delta},
\qquad
\bar y=\frac{2m}{3\delta}.
\]
Eliminating \(m\) gives the parabolic boundary equation.

If \(m\ge\delta/2\), the cap is a right triangle at \((1,1)\). With \(d=\sqrt{2\delta m}\), its side intercepts yield centroid
\[
\bar x=1-\frac d3,
\qquad
\bar y=1-\frac{d}{3m},
\]
and therefore
\[
(1-\bar x)(1-\bar y)=\frac{2\delta}{9}.
\]

Green integration over one octant gives
\[
I_1=\frac13-\frac{2\delta}{27},
\qquad
I_2=\frac23-\frac\delta3+\frac{2\delta}{9}\log\!\left(\frac\delta2\right),
\]
so the full area is \(4(I_1+I_2)\).

For \(\delta>2\), complementary caps in a zero-centroid centrally symmetric square give
\[
M_\delta(Q)=\frac{4-\delta}{\delta}M_{4-\delta}(Q).
\]

The decoded package's `verify.py` was replayed before packaging and returned:

`VERIFY_OK square Ulam body boundary and area`

The numerical replay is a consistency check and is not used to prove the continuum of normal directions or levels.
