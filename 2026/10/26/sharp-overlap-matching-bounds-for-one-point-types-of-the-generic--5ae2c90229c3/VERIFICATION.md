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
# Reproduction and limits

Run \`python3 verify.py\` using Python 3.8 or later, with no external packages or network dependencies. Its output should match \`verification_output.txt\` and begin with \`ALL_CHECKS_PASS\`.

The program independently enumerates every tetrahedron-free labelled parameter 3-hypergraph on 3, 4, and 5 vertices. For each it constructs the overlap graph, finds the maximum matching by recursive exhaustive search, counts legal one-point link assignments by direct enumeration, and verifies the sharp probability bound plus its equality condition for probabilities \(1/3,1/2,2/3\) as exact rational numbers. Additional seeded, admissible six-vertex bases test the theorem at probability \(1/2\), and the eight pencil checks confirm the closed normalization formula.

The complete finite census tests 785 admissible labelled bases (99 equality cases, 686 strict cases); the six-vertex tests are 35 sampled bases and are not exhaustive. The infinite result, the full equality classification, and the realizability for arbitrary numbers of constraints are proved in the mathematical argument, not inferred from the checker. The program is a corroborating verification, not an independent scientific audit.
