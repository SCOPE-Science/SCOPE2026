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

The unit ball is the centrally symmetric octagon with vertices
\[
(0,1),\ \left(\frac23,\frac23\right),\ \left(1,\frac17\right),\ (1,-1)
\]
and their negatives. These points follow directly from the three breakpoints of the source function \(\psi\) together with the \(\ell_\infty\) branch.

For every positive-definite quadratic form \(q\), let \(M\) and \(m\) be its maximum and minimum on the norm unit sphere. The exact matrix identity
\[
\frac4{13}v_1v_1^{\mathsf T}+\frac9{13}v_2v_2^{\mathsf T}=\frac{13}{9}\cdot\frac12(z_1z_1^{\mathsf T}+z_2z_2^{\mathsf T})
\]
with \(v_1=(2/3,2/3)\), \(v_2=(1,-1)\), \(z_1=(1,-5/13)\), and \(z_2=(5/13,-1)\) proves \(M/m\ge13/9\) for every Euclidean pullback.

For \(q_*(x,y)=x^2+(10/13)xy+y^2\), exact evaluation gives \(M=16/13\). Exact minimization on the four right-half edges gives
\[
\frac{64}{65},\quad\frac{72}{65},\quad\frac{144}{169},\quad\frac{144}{169},
\]
and central symmetry repeats these values on the remaining edges. Hence \(m=144/169\), so \(M/m=13/9\).

`verify.py` uses only Python standard-library rational arithmetic and replays these identities directly from the embedded vertex data. Its success condition is `VERIFY_OK d2=13/9`.

Limits: the checker verifies the finite exact algebra after the polygon has been derived from the published norm definition; it does not establish literature originality. The theorem does not classify all optimal pullback forms.
