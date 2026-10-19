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

# Reproduction

Invoke `python3 verify.py` from the artifact directory. No data files, external packages or internet connection are required. The complete printed output is embedded as `verify-output.txt`.

The program verifies the ten canonical reverse-complement orbits; enumerates all 1023 nonempty orbit-subsets; computes optimal lengths by oriented Hamiltonian-path dynamic programming; computes longest possible direct greedy output using exhaustive recursive maximization over all ties and orientations; and asserts the full cardinality table, an additive excess of at most one, 282 one-character-loss instances, and ratio \(5/4\).

Independent direct permutation/orientation checks are included for inputs with at most four reads, while an uncached, separately expressed enumeration of greedy transition trees is included for inputs with at most three. Both cover all such small inputs. The finite verification covers the complete stated domain; it does not certify results about longer reads or larger alphabets.
