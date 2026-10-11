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
The verification target is the fixed-separation maximum
\[
M(\epsilon)
=
\sup\left\{
N_{12}(x+y):
x,y\in S_{X_{12}},\
N_{12}(x-y)=\epsilon
\right\}.
\]

The analytic upper certificate is
\[
M(\epsilon)
\le
\min\left\{
2,\
4-\sqrt3\,\epsilon,\
\frac{4-\epsilon}{\sqrt3}
\right\}.
\]
The two nontrivial bounds follow from exact dual-facet inequalities. `verify.py` reconstructs all twelve signed facet functionals and all twelve primal vertices and checks every cyclic separation. The exact weighted dual sums are
\[
2\sqrt3,\ 
2+\sqrt3,\ 
4,\ 
4,\ 
4,\ 
2+\sqrt3,\ 
2\sqrt3,
\]
so both weighted estimates are globally valid.

The checker then verifies five explicit witness families covering
\[
[0,4-2\sqrt3],\
[4-2\sqrt3,1],\
[1,2(\sqrt3-1)],\
[2(\sqrt3-1),\sqrt3],\
[\sqrt3,2].
\]
Every relevant signed-facet evaluation is affine in \(\epsilon\). The checker proves each required norm inequality at both endpoints of its interval and verifies an identically active facet, which establishes the claimed norm exactly throughout the full interval.

Finally,
\[
\delta_{X_{12}}^a(\epsilon)
=
1-\frac12M(\epsilon)^2
\]
is the defining transformation. No finite sampling or timeout inference is used as proof.

No independent audit or independent validation has been performed.
