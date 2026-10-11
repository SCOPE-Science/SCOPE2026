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

# Reproduction and proof checks

From this directory, run `python3 verify.py`. The expected last line is `VERIFY_OK`. The verifier is Python-standard-library-only, enumerates all simplices from the closed radius-one graph neighborhoods, checks graph parameters and the local nonisomorphism witness, constructs the deterministic face matching from scratch, validates that it is an actual matching, builds every codimension-one incidence and exhaustively confirms that the reversed matched Hasse orientation is acyclic.

For the Shrikhande graph the checks return \(1512\) nonempty simplices, \(744\) matched pairs, \(5952\) directed Hasse incidences, one critical vertex and \(23\) critical two-simplices. The comparison rook graph returns \(1600\) nonempty simplices, \(768\) matched pairs, \(6240\) incidences, one critical vertex and \(63\) critical two-simplices. Independent mod-two boundary ranks are reported for every positive dimension.

The mathematical implication uses Forman's acyclic-matching theorem: with no critical one-cells or higher cells, a CW complex with a single vertex and only two-cells is a wedge of two-spheres. This proves the integral homotopy statement; mod-two ranks alone would not. The classification of the two strongly regular graph isomorphism types is taken from the cited graph-theory literature. No generalization to other parameter sets or scales, no canonical choice of spherical generators and no independent external certification are asserted.
