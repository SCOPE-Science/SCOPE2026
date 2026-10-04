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

The proof is symbolic. It uses the valuation vectors of all factorials that can occur when the largest prime divisor is \(13\), namely \(2!,\ldots,16!\), and an exact unimodular coordinate change. In those coordinates the semigroup is \(\mathbb N^6+\mathbb N u+\mathbb N v\), with \(u\) and \(v\) the vectors of \(14!\) and \(15!\). Eliminating their nonnegative coefficients gives the closed criterion in `RESULT.md`; the displayed canonical exponents are obtained by the explicit feasible choice \(r=r_0\), \(t=m\).

`verify.py` independently reconstructs the factorial valuation vectors and checks the coordinate identities. It then compares the closed criterion against direct bounded coefficient search on \(3,198,720\) coordinate vectors and checks \(18,225\) generated cases by rebuilding the canonical representation. Fresh replay output:

`VERIFY_OK`

`factorials_checked=2..16`

`box_equivalence_checks=3198720`

`generated_canonical_checks=18225`

These finite checks are regression evidence only. The unrestricted theorem follows from the exact semigroup reduction and integer-inequality elimination, not from finite enumeration. The literature comparison does not remove the residual risk of an unindexed older equivalent formulation.
