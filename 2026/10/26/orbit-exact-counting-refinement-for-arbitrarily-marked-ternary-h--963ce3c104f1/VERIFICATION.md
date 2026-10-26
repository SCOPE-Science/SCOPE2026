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
# Verification and limits

`python3 verify_ternary.py` uses only Python 3's standard library to construct ternary Hamming graphs, run exact simultaneous 1-WL from distinct singleton marker colours, construct coordinate equality-pattern status histograms independently, and compare partitions by mutual functional consistency. It also checks the exact generating multiset of neighbour distance displacements for each tested vertex. The program checks 985 marker configurations for dimensions one to four and markers one to four. All tests passed on the supplied run, documented in `verification_output.txt`. Cases up to dimension two are exhaustive among marker sets containing the all-zero word (a harmless automorphism normalization); larger cases use deterministic bounded samples.

The universal theorem rests on the written combinatorial proof and is not an inference from finite tests. No Lean or external certification is claimed. Scientific independent audit has not been performed.
