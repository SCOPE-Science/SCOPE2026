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

Run `python3 verify.py` with the two bundled files in the same directory. The checker uses only the Python standard library and reconstructs (i) all Euler circuits from local successor permutations in six small instances, (ii) the distinct contracted-graph matrix-tree minors in eight instances, and (iii) sharp-bound minima/maxima and the entire equality sets for nonbinary orders in 21 alphabet/order instances. The actual run output is included verbatim in `verification_output.txt`.

The path contraction identifies Euler circuits with a single prescribed two-arc adjacency. The finite cases do not amount to a proof for arbitrary alphabets or orders. The infinite theorem is proved in `RESULT.md`. None of these checks is an independent scientific audit.
