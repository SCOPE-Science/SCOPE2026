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

The source premise checked in the primary full text is that the Fermat cubic has exactly \(72\) type-\(9\) points and that their ideal is \((F,Q(x,y))\), with the displayed factorization of \(Q\) into degrees \(6,9,9\).

The accompanying exact checker verifies the polynomial factorization, \(q(1)=-243\), the two primitive-cube-root projective triples and their exact \(C_3\) permutation stabilizers, the order \(9\) kernel of coordinatewise cubing on the projective torus, and the orbit arithmetic. A fresh run used the inspected SymPy \(1.14.0\) installation and returned:

`VERIFY_OK group_order=54 orbit_sizes=18,54 small_stabilizer=C3 small_locus=x9=y9=z9 sextic_factor=exact`

The script does not infer an infinite or geometric statement from sampling. The proof in `RESULT.md` supplies the exhaustive Hessian and stabilizer argument. The verification is specific to characteristic zero and does not address analogous orbit structures for other plane cubics.
