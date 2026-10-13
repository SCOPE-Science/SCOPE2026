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

# Verification of the mathematical claim

The claim is an exact symbolic statement for every two-positive-integer parameter pair over \(\mathbb C\). Reproduce the finite consistency experiment by running `python3 hibi_bipartite_checker.py` and comparing its JSON output to `hibi_bipartite_checks.json`. The checker enumerates \(1,815\) nonzero tensor/zero-factor representatives for the nine specified parameter pairs and evaluates all Hibi straightening quadrics and their Jacobian ranks modulo the two primes \(1000003\) and \(1000033\). All evaluated Jacobian rank decisions match the all-parameter singularity criterion. The script implements the equations independently of the geometric reasoning and is included with its output, but the selection of test points is not exhaustive even for arbitrary complex points of an individual variety.

Proof-level checks requiring no code are: the two Boolean sublattices have exactly one shared order ideal; the Jacobian criterion for the equation equating their Segre corner coordinates; the one-zero-cone tangent excess \(2^m-m-1\); the irreducible projective divisor faces and mixed joins; and analytic normal forms after localizing at a general point. Multiplicity \(m!\) comes from the Segre degree. The corner derivatives are analyzed on rank-one tensor charts rather than relying on a finite experiment. The reduced singular locus is proved complete; the nonreduced singular scheme and nongeneric completed local rings are explicitly outside the claim. The analogous arbitrary-characteristic analytic statement and exhaustive equivalence searches are not claimed. Independent mathematical audit has not been performed.
