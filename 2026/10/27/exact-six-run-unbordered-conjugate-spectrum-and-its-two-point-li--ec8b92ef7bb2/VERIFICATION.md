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

# Verification and reproducibility

The proof in `RESULT.md` derives the six-run border reduction and all-length weak-order generating functions. The standalone Python 3 program `verify.py` independently checks the border definition against every run-length sextuple in \(\{1,2,3,4\}^6\), evaluates the \(169\) order-pattern products by exact integer-polynomial arithmetic, and cross-checks all fixed-length coefficients for \(6\le n\le18\) by explicit compositions.

Command: `python3 verify.py`.

Expected success line: `VERIFY_OK rotations=4096 weak_order_pairs=169 generating_functions=5 fixed_lengths=6..18`.

The finite checks are not a proof for arbitrarily large lengths. The all-length conclusion follows from the border lemma and the exact weight-generating function for every weak-order pattern. No independent audit has been performed.
