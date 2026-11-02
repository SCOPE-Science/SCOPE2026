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

# Verification evidence and limits

The executable `checks.py` is a standalone Python 3 standard-library program. Running `python3 checks.py` produced the exact output stored in `checks.txt`, ending with `PASS: 4382 exact and numerical assertions`.

For small path sizes, the program enumerates every composition of a fixed half-order among the odd and even block classes and checks the unique cone-flow recursion against a separately coded integral maximum-flow algorithm for the complete bipartite block support. It also checks necessary nonnegative partial sums, evaluates exact rational conditional multinomial cone probabilities, and prints several scaled finite-order probabilities. The exact integer and rational checks validate finite combinatorics; the displayed floating-point values are exploratory diagnostics only.

The infinite-limit proof is not delegated to this program. Its substantive ingredients are the fixed-block deterministic cycle-cover theorem and blow-up lemma, a direct Chernoff/union-bound high-probability verification for strictly positive fixed edge probabilities, the balanced binomial local central limit estimate, the conditional multinomial central limit theorem, the polyhedral tangent-cone boundary argument, and the cyclic-exchangeability identity for a continuous Gaussian bridge. The last five steps, hypotheses, and normalizations are stated in `RESULT.md`.

Scientific limits: no proof is given for varying block count, vanishing supported probabilities, or a second-order expansion. Checks do not establish novelty or constitute independent validation.
