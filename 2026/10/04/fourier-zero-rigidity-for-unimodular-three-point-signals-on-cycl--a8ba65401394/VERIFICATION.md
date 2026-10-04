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
The analytic proof is independent of finite enumeration. It uses three exact ingredients: equilateral rigidity for three unit summands, the kernel size of the character-pair homomorphism, and a congruence criterion for whether the two cancellation orientations lie in one image coset.

The bundled `verify.py` uses integer modular arithmetic only. For every normalized support \(\{0,a,b\}\) with \(3\le N\le180\), it compares the closed-form modulo-\(3\) criterion against direct image membership, checks that the kernel has cardinality \(g\), and verifies that the explicit phase construction has exactly the predicted number of zeros. It also checks that no paired case occurs for primes greater than \(3\) in the tested range.

Replay output:

`VERIFY_OK triples=955860 paired=76776 single=879084 primes_gt3=39 N_max=180`

The finite replay is corroborative and does not establish the universal quantifier by itself. No claim is made for supports with four or more points, approximate zeros, or noncyclic groups.
