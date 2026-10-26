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

# Reproducibility and verification

Execute `python3 verify_poset_threshold.py` using Python 3.10 or newer. This enumerates all naturally labeled transitive posets through six vertices. The exact Littlestone recurrence is applied to the computed lower-ideal families and does not use the analytic chain-bound proof. Its output is in `verification_output.txt`; the terminal marker is `ALL_POSET_WIDTH_THRESHOLD_CHECKS_PASS`.

The program checks each small poset's width, hypothesis count, exact Littlestone dimension, the predicted universal order lower bound, and the exact structure in every minimum-order equality case. It also verifies the integer threshold construction algebra on \(1\le w\le10\) and \(w\le K<30\). The enumeration is finite and does not certify every order size. The unrestricted theorem rests on the complete mathematical proof in `RESULT.md`, including the product additivity, chain-decomposition inequality, rigidity, connected construction, and padding argument. No independent scientific audit has been performed.
