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

The universal claim is verified by a symbolic induction, not by finite enumeration.

The checked dependency chain is:

1. conjugation by \(N_G(\langle x\rangle)\cap K\) preserves the generated-pair set;
2. the maximal admissible normal subgroup \(T\) exists because \(T=1\) is admissible;
3. any nontrivial subgroup of \((H/T)\cap Z(K/T)\) lifts to an admissible larger normal subgroup because its quotient contribution is finite abelian and therefore lies in \(\mathcal C\);
4. right multiplication by \(T\) preserves the generated-pair set, so quotient cardinalities are integral;
5. a nonidentity element of \(H/T\) has a proper centralizer preimage in \(K\), allowing induction;
6. fixed points in the quotient are exactly the relevant intersections divided by \(T\);
7. each nonidentity conjugacy-class contribution to Burnside's sum is divisible by \(|H/T|\), forcing the identity contribution to be divisible as well;
8. intersecting and splicing normal series verifies the hypotheses for \(\pi\)-separable groups.

The proof does not establish necessity of the closure axioms, a profinite extension, or a bounded-derived-length analogue. No computational experiment is used as evidence for the infinite statement.
