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

# Reproduction and scope

Run the bundled `VERIFY.py` with Python 3 standard library: `python3 VERIFY.py`.

The program uses exact rational arithmetic in \(\mathbb Q(\sqrt5)\) for the explicitly displayed two-patch witness. It independently evaluates the common-marginal, fixed-point, isolated-capacity and optimal rank-one identities. In 245 further randomly selected rational-parameter cases with two through eight patches, 65-decimal-digit arithmetic compares the symbolic envelope formula against a separate bisection-based marginal-allocation calculation at five population scales and tests convergence over 120 generations. Fixed deterministic seeds make the checks reproducible. Executing the file produced `PASS: 2701 independent exact/algebraic and high precision comparisons`.

For the infinite-parameter result, reproduction consists of checking the six analytic steps in `RESULT.md`: uniqueness of the strictly concave maximizer; monotonicity of its scalar envelope and strict decrease of the envelope/population ratio; the exact balancing identity at \(K_*\); induction controlling all adaptive paths; global convergence of the rank-one policy; and the marginal derivative and strong-concavity arguments. Numerical samples alone do not certify an infinite claim. No independent external audit has been performed.
