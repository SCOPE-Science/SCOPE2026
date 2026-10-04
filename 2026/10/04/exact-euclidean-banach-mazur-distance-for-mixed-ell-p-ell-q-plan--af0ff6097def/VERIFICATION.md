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

Let \(G\) be the eight signed coordinate permutations. For an arbitrary isomorphism \(T\), put \(Q=T^\mathsf{T}T\). If \(m\) and \(M\) are the minimum and maximum of \(x^\mathsf{T}Qx\) on the norm unit sphere, then the squared distortion of \(T\) is \(M/m\).

Averaging \(g^\mathsf{T}Qg\) over \(G\) gives \(cI\). Since every \(gx\) remains on the norm unit sphere, \(m\le c\|x\|_2^2\le M\) for every unit vector of the given norm. At points of smallest and largest Euclidean radius this forces
\[
M/m\ge (r_+/r_-)^2.
\]
The identity map attains equality, so the Euclidean Banach--Mazur distance is exactly \(r_+/r_-\).

For a Euclidean unit vector \(u\),
\[
2^{2/r-1}\le \|u\|_r^2\le1
\]
when \(2\le r\le\infty\), with diagonal and axial equality respectively; for \(1\le r\le2\), the inequalities reverse. Therefore the mixed norm has squared radial ratio
\[
\frac{2(1+\lambda)}{2^{2/p}+\lambda2^{2/q}}
\]
in the upper regime and
\[
\frac{2^{2/p}+\lambda2^{2/q}}{2(1+\lambda)}
\]
in the lower regime.

The exact-family source's Example 4.2 gives these same two expressions for the von Neumann--Jordan constant. Endpoint sanity checks give \(1\) for \(p=q=2\) and \(2\) for \(p=q=1\) or \(p=q=\infty\).

No numerical sampling or finite enumeration is used to justify the universal parameter claim. The unproved region is \(p<2<q\).
