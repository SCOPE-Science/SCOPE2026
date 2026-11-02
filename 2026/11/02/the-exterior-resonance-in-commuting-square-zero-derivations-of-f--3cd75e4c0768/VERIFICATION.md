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

# Verification details

Run `python3 check.py` and compare its standard output with `verify_output.txt`.

For \(Q=3,5,7\) at the exterior parameter, the checker traverses every possible image of \(x,y\) in the Jacobson radical, tests the derivation identity against all original basis products, tests the square of the resulting four-by-four operator, then tests every ordered pair for commutation, ranks, neighborhood cardinality, and zero product. The outcomes are respectively \(33,145,385\) square-zero derivations and \(369,4225,21217\) commuting ordered pairs. The checker also tests three nonresonant/commutative parameter configurations over odd prime fields.

The \(\mathbb F_9\) test uses the irreducible polynomial \(t^2+1\) over \(\mathbb F_3\), checks all structurally possible square-zero parameters and confirms 801 solutions using the original algebra multiplication. It does not independently brute-force all linear endomorphisms of the four-dimensional vector space; the exhaustion of all derivations uses the proved normal form.

The geometry for arbitrary tuple lengths, the all-arity polynomial and the exact number of maximal compatible planes are established by symbolic algebra and incidence geometry, not by computation. The checker is corroboration only. No independent mathematical audit has been performed.
