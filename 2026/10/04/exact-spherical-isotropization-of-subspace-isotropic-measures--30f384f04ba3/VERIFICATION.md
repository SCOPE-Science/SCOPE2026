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

The claim is verified analytically rather than by finite enumeration.

For the lower bound, any admissible coupling \((X,Y)\) satisfies \(\|X\|=\|Y\|=1\), \(X\in U\), and \(\mathbb E[YY^{\mathsf T}]=I_d/d\). Therefore
\[
\mathbb E\|X-Y\|^2=2-2\mathbb E\langle X,P_UY\rangle
\ge 2-2\sqrt{\mathbb E\|X\|^2\,\mathbb E\|P_UY\|^2}
=2-2\sqrt{r/d}.
\]

For attainment when \(r<d\), choose a centered spherical tight \(Z\) in \(U^\perp\), independent of \(X\), and set
\[
Y=\sqrt{r/d}\,X+\sqrt{(d-r)/d}\,Z.
\]
Orthogonality gives \(\|Y\|=1\), and direct second-moment expansion gives \(\mathbb E[YY^{\mathsf T}]=I_d/d\). The achieved correlation is \(\sqrt{r/d}\).

For the equality case, equality in Hilbert-space Cauchy--Schwarz is equivalent to \(P_UY=cX\) almost surely with \(c\ge0\). Its \(L^2\) norm fixes \(c=\sqrt{r/d}\). Decomposing the remaining orthogonal component and comparing the diagonal and mixed blocks of \(I_d/d\) yields exactly the two stated moment conditions on \(Z\).

No numerical experiment, timeout result, or partial enumeration is used to justify the universal statement. The theorem does not address sources whose second moment is not \(P_U/r\).
