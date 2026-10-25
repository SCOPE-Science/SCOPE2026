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

The independently implemented `checker.py` enumerates quiver arrow-coordinate assignments and calculates commutator ranks directly from length-two path multiplication using row reduction over prime fields. This is not the graph component proof in executable form. It also enumerates ordered pairs of arrow vectors directly and confirms the commuting-pair count against both the graph expression and rank histogram. The checker includes loops, parallel arrows, oriented paths and cycles, forks, and disconnected composability cases. Its recorded output is stored in `checker_output.txt`.

The exhaustive ranges are 55 quiver/field configurations, 3,889 single-element arrow assignments, and 30,946 ordered-pair assignments; path recurrence tests extend through seven arrows and cyclic formula tests through eight arrows for fields of orders 2, 3, and 5. Full enumeration does not certify the infinite parameter range or general finite field extensions. The proof's basis-coordinate computation does that work. Reproduce with `python3 checker.py` from this directory.
