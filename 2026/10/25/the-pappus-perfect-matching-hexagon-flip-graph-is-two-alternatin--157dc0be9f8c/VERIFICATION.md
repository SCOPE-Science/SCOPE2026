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

# Computational verification and limits

Run `python3 verify_incidence.py` and `python3 verify_lcf.py` in the same directory as this file. Their complete standard outputs must match `incidence_output.json` and `lcf_output.json` byte for byte. Both scripts use only the Python standard library and contain exact assertions; the second starts from an independently specified LCF graph and generic perfect-matching recursion, rather than from the nine-line incidence configuration.

The incidence search visits every admissible injective assignment of one line to each of the nine points, so reaching depth nine is equivalent to a perfect matching. Testing both cyclic rotations on all point triples is necessary and sufficient for a symmetric difference of one alternating six-cycle. Per-component structural assertions prove the precise hub/hexagon isomorphism. Exhaustive breadth-first searches give radius and diameter, not merely lower bounds. The LCF check independently constructs and enumerates all simple six-cycles of an eighteen-vertex graph.

The finite scope of the computation is the fixed eighteen-vertex Pappus graph. These exact checks do not prove statements for other graphs or establish independent scientific review or publication priority.
