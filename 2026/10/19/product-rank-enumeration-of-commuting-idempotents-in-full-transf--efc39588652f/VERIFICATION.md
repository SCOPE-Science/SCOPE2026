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

# Reproducibility and scope

Run `python3 verify.py` with Python 3.9 or later, no third-party modules. It derives the rooted-fiber numbers by factorial/multinomial counting and the product-rank coefficients independently using labeled convolution. It separately enumerates all idempotent functions on sets of sizes one through six and checks commuting pairs and product ranks directly. The test asserts the row distributions and the induced commuting-graph edge counts. A successful execution prints `VERIFY_OK`.

The program uses exact nonnegative integers, never floating approximations. Direct exhaustive verification covers only sizes at most six. All-size correctness follows from the explicit bijection and labeled SET proof in `RESULT.md`, not from observing finite agreement. Originality rests on scientific comparison rather than numerical experiment. No independent mathematical audit has been performed.
