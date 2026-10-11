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
For \(0<\lambda\le1/2\), put
\[
d=1-2\lambda.
\]
Under the supporting-face hypotheses,
\[
\lambda x+(1-\lambda)y=\lambda(x+y)+dy
\]
and
\[
\lambda x-(1-\lambda)y=\lambda(x-y)-dy.
\]
The two support functionals therefore certify the same lower value
\[
\lambda J(X)+d.
\]
The published weighted-James upper comparison gives the identical quantity, proving equality. The parameter symmetry extends the formula to \(1/2\le\lambda<1\).

For the affine-regular hexagon, the linear isometries
\[
Q(s,t)=(t,t-s),
\qquad
R(s,t)=(s,s-t)
\]
reduce the classical James problem to four edge classes. The formulas in `RESULT.md` show their minima never exceed \(3/2\), while
\[
x=\left(1,\frac12\right),
\qquad
y=(0,1)
\]
attains \(3/2\). The functionals
\[
f_+(s,t)=t,
\qquad
f_-(s,t)=s-t
\]
then certify the supporting-face hypotheses.

`verify.py` uses exact rational arithmetic to verify the isometries, reduced edge formulas, the James witness, and the weighted profile on all reduced rational weights with denominator at most \(80\). These finite checks are supplementary; the continuum theorem is proved analytically.

No independent audit or independent validation has been performed.
