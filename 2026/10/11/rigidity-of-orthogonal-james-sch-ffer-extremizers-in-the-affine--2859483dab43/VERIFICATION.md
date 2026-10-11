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

The norm is
\[
N(u,v)=\max\{|u|,|v|,|u-v|\}.
\]
The maps
\[
R(u,v)=(u-v,u),
\qquad
S(u,v)=(v,u)
\]
preserve \(N\) and reduce every unit-sphere point to one of two strata.

For an open-edge point
\[
x=(1,t),\qquad0<t<1,
\]
the unique norming functional is \(f(u,v)=u\), so every unit Birkhoff direction is \(y=(0,\pm1)\). Thus the two chord lengths are
\[
1+t,\qquad2-t.
\]

At the vertex \(x=(1,0)\), the complete norming-functional set is
\[
f_a(u,v)=u-av,\qquad0\le a\le1.
\]
Every unit Birkhoff direction is therefore \(y=\pm(a,1)\), and the two chord lengths are
\[
1+a,\qquad2-a.
\]

For \(s\in[0,1]\),
\[
\min\{1+s,2-s\}\le\frac32
\quad\text{and}\quad
\max\{1+s,2-s\}\ge\frac32,
\]
with equality in either statement if and only if \(s=1/2\). Hence every extremizer of either orthogonal constant has both chord lengths equal to \(3/2\), and the explicit isometries reduce every such pair to the representative
\[
\left((1,0),\left(\frac12,1\right)\right)
\]
up to the stated sign and order operations.

No numerical sampling or external certificate is used in the proof.
