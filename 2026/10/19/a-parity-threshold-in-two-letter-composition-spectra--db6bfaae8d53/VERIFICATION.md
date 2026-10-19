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

# Reproduction and scope of verification

Run `python3 verify.py` using Python 3 and only its standard library. No input files, network access or external services are needed.

The checker regenerates simple-graph degree-parity polynomials and partition-lattice Möbius sums; tests four symbolic rational equalities by multiplying both sides to integer polynomials; tests the combined quaternary generating-function numerator; expands coefficients to eleven edges; independently enumerates connected parity-valid undirected multigraph profiles for alphabets of sizes two, three and four through eight edges; and also directly enumerates words whenever the search space is at most 65536 words.

All tests completed and reported `ALL EXACT POLYNOMIAL AND INDEPENDENT FINITE CHECKS PASSED`.

The all-alphabet formula and asymptotic are mathematical deductions. The finite searches cover only the explicitly stated ranges, and no claim of external or independent audit is made.
