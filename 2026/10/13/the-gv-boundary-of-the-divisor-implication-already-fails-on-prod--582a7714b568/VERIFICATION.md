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

Let \(A=E_1\times\cdots\times E_g\) and \(F_i=\operatorname{pr}_i^*([0_{E_i}])\). The following checks establish the claim.

1. \(\mathcal O_A(H)\cong\boxtimes_i\mathcal O_{E_i}([0_{E_i}])\), so \(H=\sum_iF_i\) is a principal polarization.
2. \(D=2F_1\) is effective and nef.
3. \(2H-D=2\sum_{i\ge2}F_i\) is the pullback of an ample divisor from \(E_2\times\cdots\times E_g\), hence nef. It is not ample because its restriction to the first elliptic factor has degree \(0\).
4. For \(C_1=E_1\times\{q_2\}\times\cdots\times\{q_g\}\), one has \(F_1\cdot C_1=1\) and \(F_i\cdot C_1=0\) for \(i\ge2\). Therefore \((H-D)\cdot C_1=-1\), so \(H-D\) is not nef.
5. Applying the standard line-bundle equivalence on abelian varieties, nefness is equivalent to GV and ampleness to IT of index zero. Thus \(\mathcal O_A(2H-D)\) is GV while \(\mathcal O_A(H-D)\) is not GV.

The numerical polynomial provides a consistency check:
\[
\frac{(tH-D)^g}{g!}=t^{g-1}(t-2).
\]
The root at \(2\) is exactly the boundary excluded when \(2H-D\) is assumed ample/IT.

No computation beyond these exact intersection identities is needed. The verification does not claim anything for indecomposable principally polarized abelian varieties.
