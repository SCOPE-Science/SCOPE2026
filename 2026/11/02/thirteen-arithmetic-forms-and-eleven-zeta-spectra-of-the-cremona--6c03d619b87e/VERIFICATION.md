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

The standalone `verify.py` reconstructs all duads, synthemes, thirty component vertices, forty-five nodes and ninety normalization branches. It exhaustively enumerates 1440 graph automorphisms via exact graph isomorphism, constructs the same 1440 elements independently as 720 label permutations and 720 transforms by an explicit side-swapping involution, and computes 13 conjugacy classes and 11 distinct zeta function signatures. It checks the point counts obtained directly from normalized branches against the logarithmic derivatives of the stated zeta functions for all elements, over extension degrees 1 through 24 with the symbolic finite-field cardinality specialized to 3 for this check. The exact class/edge/branch orbit census is exhaustive, hence not extrapolated from field experiments.

Command: `python verify.py` in the package directory with `networkx` available. Output: `verification_output.txt`. Full representative permutations and orbit tables: `classification.json`. The checked executions end with `VERIFY_OK`.

The infinite-field correctness argument is algebraic: stable three-pointed projective-line descent and the finite-field normalization zeta identity; no finite test by itself proves an infinite statement. The results do not classify other stable curves or other base fields. The mathematical originality comparison is qualified by residual historical-literature risk, and no independent scientific audit or certification is claimed.
