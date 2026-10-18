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

# Verification record
Run `python3 truncated_octahedron_section_checker.py` using Python 3 without third-party modules. The checker constructs 24 signed-permutation vertices and 36 exact squared-length-2 edge pairs; verifies every vertex has degree three and that every edge has squared endpoint norms five and dot product four; verifies all five integer sign-chamber examples and their 6-, 8-, or 10-edge crossing counts; verifies the determinant, norms and dot products of the three extreme rays; and checks the closed expressions for all probabilities and mean. It separately reconstructs 605 central sections directly from all 14 active halfspace constraints, obtaining the same polygon side counts as the combinatorial edge model. Its fixed-seed 120,000-orientation Gaussian simulation observes 59,594 six-sided, 38,158 eight-sided, and 22,248 ten-sided sections and passes a numerical tolerance comparison.

The exact geometric proof, not the finite test run or sampling, establishes the three probabilities for all generic orientations. Full-text inspection and similarity comparisons support a self-review but cannot certify historical novelty; one closely relevant recent preprint was abstract-accessible only. No independent audit was carried out.
