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

The proof is symbolic and valid for arbitrary positive part sizes. The finite computation below is an independent consistency check, not an infinite certificate.

`verify.py` enumerates every nondecreasing complete-multipartite part profile of total order at most \(9\) with at least two parts. For every nonempty subset it constructs closed neighborhoods directly and tests the literal private-vertex condition \(N[w]\cap D=\{v\}\) for every selected vertex \(v\). It compares that predicate against the claimed two-shape classification, compares the resulting size counts against the closed irredundance-polynomial formula, reconstructs maximal irredundant sets from the literal predicate, and checks the maximal-polynomial, lower-irredundance, and upper-irredundance consequences.

Replaying the packaged file produced:

`VERIFY_OK profiles=87 subset_checks=22845 irredundant_sets=2975 maximal_sets=995 max_order=9`

The check is exhaustive only through order \(9\). It does not substitute for the general proof. The originality comparison is bibliographic rather than computational, and older incompletely indexed literature remains the stated residual risk.
