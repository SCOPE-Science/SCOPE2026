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

The verification is analytic.

At the primary extremizer,
\[
H(z)=z-\overline c-\frac{1}{\overline{p_0(z)}}
\]
and
\[
F_0(z)=p_0(z)\overline{(z-\overline c)}-1
\]
satisfy
\[
F_0(z)=p_0(z)\overline{H(z)}.
\]
At a zero \(z_0\) of \(H\),
\[
dF_0(z_0)=p_0(z_0)d\overline H(z_0),
\]
so
\[
\det dF_0(z_0)
=-|p_0(z_0)|^2\det dH(z_0).
\]
The primary source proves every zero of \(H\) is nonsingular and that the orientation counts for \(H\) are \(n\) positive and \(2n-1\) negative. Hence the logharmonic equation has \(2n-1\) positive and \(n\) negative Jacobian roots.

Treat all complex coefficients of \(p\) and \(q\) as real parameters. The real-analytic implicit-function theorem applies independently at all \(3n-1\) simple roots. After intersecting the finitely many parameter neighborhoods, all branches persist and remain distinct, and their Jacobian signs cannot change without passing through zero.

The independent global theorem gives at most
\[
3n-1
\]
solutions for every degree-\(n\) polynomial paired with a linear factor and every target. Therefore the \(3n-1\) continued branches exhaust all solutions throughout the small coefficient neighborhood.

No finite computation, root solver, or numerical perturbation experiment is used as evidence.
