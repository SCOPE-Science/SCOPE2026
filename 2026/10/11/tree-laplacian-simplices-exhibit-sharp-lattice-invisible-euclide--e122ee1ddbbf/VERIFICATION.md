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
The complete proof for every finite tree on \(n\ge2\) vertices is in `RESULT.md`.

Check the exact affine identities
\[
LL^\dagger=I-\mathbf1\mathbf1^{\mathsf T}/n,
\qquad
\lambda_i(x)=1/n+\langle L^\dagger e_i,x\rangle.
\]
Each facet is the zero set of one barycentric coordinate. A radius-\(\rho\) inscribed ball requires
\[
\lambda_i(c)\ge\rho\|L^\dagger e_i\|,
\]
so summing yields a global radius bound attained by the displayed unique barycentric center.

For the two tree inequalities, verify the chain
\[
S_T\le\sqrt{n\operatorname{tr}((L^\dagger)^2)}
\le\sqrt n\operatorname{tr}(L^\dagger)
=\frac{W(T)}{\sqrt n}
\le\frac{(n^2-1)\sqrt n}{6}
\]
and the branch-current bound for each vertex of degree at most two
\[
\|L^\dagger e_i\|\ge\frac{n-1}{2\sqrt2\,n}.
\]
The number of such vertices is at least \((n+2)/2\).

For the exact witnesses, check the pseudoinverse zero-sum column solutions in equations (19)--(21) of `RESULT.md`, the quartic squared norm and the positive Riemann-sum limit. The finite verification file `verify.py` uses only the Python standard library, performs exact rational matrix inversion for labeled trees, checks all labeled tree graphs on up to six vertices, tests larger deterministic trees, and checks the star and path formulas through order 40. It does **not** establish the all-order theorem by enumeration and is not an originality or independent-audit certificate.
