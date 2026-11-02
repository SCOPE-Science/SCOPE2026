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

# Mathematical verification

The formula for the focal payoff difference is derived from the one-coplayer pivotal event. The derivative and turning-point theorem are proved analytically in `RESULT.md`, including the endpoint cases, roots and basin boundaries. A finite checker cannot prove the universal result.

Run `python3 checks/verify.py` in the extracted package; it requires only Python 3 standard library. The reference run completed 4,795 assertions successfully, including rational pivotal-event enumeration, exact factorization and stability signs, exact group-size observation weighting, and 500 reproducible numerical stress tests of the strict three-root parameter window.

The statement excludes the equality bifurcation surfaces; it does not prove the same phenomena for finite-population Markov chains, changing group-size laws or different public-good benefit functions. Publication priority remains provisional where original full texts were inaccessible. Independent mathematical or literature review has not been conducted.
