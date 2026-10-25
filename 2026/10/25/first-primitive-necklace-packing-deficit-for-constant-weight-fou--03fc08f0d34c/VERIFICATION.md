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
Place `certificate.json` and `verify.py` in the same directory and execute `python verify.py` using a Python 3 interpreter. No packages or network access are needed.

The program enumerates all binary words of weight four at lengths \(5\)–\(12\), computes primitive rotation orbits, verifies the supplied codebook at each length by checking every nonempty proper prefix against every suffix in both directions, and tests all self-borders. It then independently enumerates the length-twelve unbordered universe and establishes that the supplied \(39\) groups are a disjoint complete partition of its \(128\) words and that every group is a pairwise-conflict clique.

The checked lower witnesses and upper partition give the exact values reported in RESULT.md. The computation is finite and exhaustive in the asserted finite range; it does not establish any statement for larger blocklengths or independently establish historical novelty.
