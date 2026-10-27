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

The file `icos_influence_certificate.py` uses exact integer coefficient arrays to verify the pivotal-polynomial identity and the complete nine-class coefficient census across \(64\) probability-box corners and \(15\) pairs of voters. Executed with Python 3: checks passed for complementarity, monotonicity, five winning triples per voter, \(960\) polynomial comparisons, signed coefficient counts, and the sharpness witness. No third-party package, randomness, search approximation, or external certificate is required.

The additional mathematical step—multiaffinity of each pivotal-probability difference and consequent attainment of every pairwise extremum at a corner—is proved in RESULT.md. Therefore the exact finite polynomial verification applies to every real-valued parameter in the continuous box. Results do not address correlated votes, different tie-breaking rules, or historical priority.
