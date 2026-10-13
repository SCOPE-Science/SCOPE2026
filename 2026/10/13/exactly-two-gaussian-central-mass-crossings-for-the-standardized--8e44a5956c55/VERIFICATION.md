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

For \(0<c\le1\),
\[
D(c)=\frac{2}{e}\sinh c-\bigl(2\Phi(c)-1\bigr),
\qquad
D'(c)=2\left(e^{-1}\cosh c-\phi(c)\right).
\]
The ratio
\[
R_-(c)=\frac{e^{-1}\cosh c}{\phi(c)}
\]
has
\[
(\log R_-)'=c+\tanh c>0.
\]
Since \(R_-(0)<1<R_-(1)\), the derivative changes sign once. Together with \(D(0)=0\) and \(D(1)>0\), this gives exactly one positive root below one.

For \(c\ge1\),
\[
D(c)=2\overline\Phi(c)-e^{-1-c},
\qquad
D'(c)=e^{-1-c}-2\phi(c).
\]
The ratio
\[
R_+(c)=\frac{e^{-1-c}}{2\phi(c)}
\]
has
\[
(\log R_+)'=c-1>0
\]
for \(c>1\). It starts below one and tends to infinity, so the derivative changes sign once. The Mills upper bound gives \(D(c)<0\) for all sufficiently large \(c\), while \(D(1)>0\), hence there is exactly one root above one and no later recrossing.

The standalone script `verify.py` uses standard-library arithmetic to bisect the two roots, verify the stated narrow brackets, and replay representative signs. These computations are not used to prove uniqueness.

Expected successful terminal line:
`VERIFY_OK c_minus=0.496168549596 c_plus=1.932987287529 D1=0.181975224626`.
