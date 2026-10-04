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

The exact source parameters are
\[
a=-\frac{10}{11},
\qquad
b=\frac1{44},
\]
\[
A=-\frac{9890884608}{9139543205},
\qquad
B=-\frac{251761689}{562995861428},
\]
\[
C=\frac{41190732}{12795360487},
\qquad
D=\frac{1373955264}{9139543205}.
\]

With
\[
S_r(x)=\frac{x(2-rx)}{(1-rx)^2},
\]
the self-convolution derivatives are reconstructed as
\[
p'(x)
=
1+A^2S_{a^2}(x)+2ABS_{ab}(x)+B^2S_{b^2}(x),
\]
\[
q'(x)
=
D^2S_{a^2}(x)+2DCS_{ab}(x)+C^2S_{b^2}(x).
\]

Exact simplification gives
\[
p'-q'
=
-\frac{3748096P_4(x)}
{24606462475(x-1936)^2(100x-121)^2}
\]
and
\[
p'+q'
=
-\frac{3748096P_6(x)}
{818606249961404385845
(x-1936)^2(5x+242)^2(100x-121)^2}.
\]

The packaged exact-arithmetic checker verifies:
\[
\#\{P_4=0\text{ in }(-1,1)\}=0,
\]
\[
\#\{P_6=0\text{ in }(-1,1)\}=1,
\]
and
\[
P_6(-0.961916078016036)>0,
\qquad
P_6(-0.961916078016035)<0.
\]

It also checks
\[
J_F(0)=1
\]
and
\[
J_F(-99/100)<0.
\]

Therefore the real-axis zero is unique and the Jacobian is negative exactly to its left.
