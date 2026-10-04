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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

For each tested pair \((n,k)\), it forms
\[
a=\frac{k-1}{n-1},
\qquad
b=\frac{k}{n-1},
\]
and verifies:

- the exact tangent identities at every non-endpoint tangent point;
- the left and right line-majorant inequalities on rational grids;
- the central second-derivative quadratic certificate;
- normalization and mean constraints for every endpoint directing measure;
- exact agreement between the endpoint mixtures and the stated upper envelope;
- the zero lower endpoint from the directing law on \(\{0,1\}\).

A finite two-atom stress test enumerates many rational support pairs and weights
with prescribed rational mean. No enumerated law exceeds the closed-form
upper envelope.

These checks do not replace the continuous concave-envelope proof.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK tangent_checks=3422 majorant_checks=178770 concavity_checks=143370 construction_checks=357540 two_atom_checks=30030`.
