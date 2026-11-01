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

# Verification

The exact integer transfer operator acts on 256 pair-symbol states from sixteen possible four-bit rung symbols. Its accepted middle transitions are precisely the four simultaneous majority equalities in `RESULT.md`, evaluated exhaustively by `verify.py`; the first and last rungs use their own bit for endpoint tie retention.

The verifier enumerated all 4096 symbol triples; 400 satisfy the middle condition. It found 36 admissible start pairs, and 36 admissible end pairs. It tested all 256 coordinates of the two annihilator-vector identities, a total of 512 exact integer residuals, and every one vanished. Exact transfer initial values for periodic states at lengths 2–6 and fixed states at lengths 2–4 also agree with the stated formulas. These checks constitute a finite algebraic certificate of the recurrences for all lengths.

An independent bit-mask implementation of the original vertex update was run on every binary configuration at lengths 2–8, totaling 87,376 states. For each it compared the first and second iterates to the input, validating both enumerators directly in these seven finite cases. Recorded output: `verification-output.txt`.

The proof of eventual period at most two uses a finite-valued strict Lyapunov decrease, not the finite simulations. Neither basin enumeration nor independent review is claimed.
