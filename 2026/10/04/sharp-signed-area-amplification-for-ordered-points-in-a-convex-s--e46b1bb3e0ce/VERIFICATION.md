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

The proof is exact and analytic.

Checks performed:

- Base cases: the full text of arXiv:2609.21968v1, Lemma 3.3, proves \(F(P)\le\operatorname{area}(H)\) for arbitrary ordered lists with \(3\le m\le5\); applying it to the reversed list gives the absolute-value form.
- Deletion identity: replacing the chain \(P_0,P_1,P_2,P_3,P_4\) by the chord \(P_0,P_4\) changes the shoelace sum by
  \[
  \frac12\bigl(P_0\times P_1+P_1\times P_2+P_2\times P_3+P_3\times P_4+P_4\times P_0\bigr),
  \]
  exactly the five-point shoelace expression.
- Induction: for \(m\ge6\), the deletion identity and the five-point bound give \(C_m\le C_{m-3}+1\). With \(C_3=C_4=C_5=1\), this yields \(C_m\le\lfloor m/3\rfloor\).
- Sign: reversal of the cyclic order negates the shoelace expression without changing the containing set.
- Sharpness: a nondegenerate triangle traversed \(q=\lfloor m/3\rfloor\) times has signed area \(q\operatorname{area}(H)\); inserting repeated copies of a vertex pads the list by one or two entries without changing the shoelace sum.
- Boundary cases: zero-area convex sets are collinear, so every closed shoelace expression vanishes.

Unproved limits and risks:

- The theorem is about signed area, not unsigned lobe area.
- Exact equality outside multiples of three uses repeated point locations; distinct-point exact attainment is not asserted.
- The bibliographic search did not locate a prior equivalent all-length coefficient, but an older result under different terminology cannot be excluded.
