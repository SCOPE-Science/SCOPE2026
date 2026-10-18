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

# Reproducible finite reductions and tests

From the directory containing these files, run `python3 VERIFY.py` using Python 3 and only its standard library. `VERIFY_OUTPUT.txt` is the captured complete expected standard output of the successful execution.

The code evaluates \(4^9=262144\) capped nine-type count vectors and checks exact equality with the 18 hypothesized large-size type patterns. The mathematical reason these finite counts apply to all \(n\ge5\) is the proved clipping invariant: the local singleton tests only subtract at most one from side totals, so all counts at least three remain non-singletons after such subtraction. The finite computation is exhaustive for its reduced state space; it is not just experimental sampling.

An independent direct graph-edge implementation enumerates all \(3^{2n+1}\) colourings when \(n=3,4,5\), and two-colour assignments at those sizes. These check the open edge neighbourhood predicate without the nine-type shortcut. A separate multinomial composition implementation confirms counts for \(5\le n\le12\). These finite size checks do not alone establish the infinite result.

No independent audit, external formal verification, source-priority guarantee, or claim concerning larger palettes is provided.
