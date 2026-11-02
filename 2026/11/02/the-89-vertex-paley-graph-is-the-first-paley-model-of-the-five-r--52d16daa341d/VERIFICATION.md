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

# Replayable finite verification

1. Run `python3 verify_paley89.py`. This constructs every prime-power field of eligible order at most 89; the defining polynomials are explicitly checked for small-degree factors. It checks all affine-square-normalized ordered-pair configurations and all 16 fourth-vertex extension patterns. All thirteen smaller eligible orders return a counterexample. At order 89 all \(7,482\) normalized configurations pass.
2. Compile `verify_paley89_direct.cpp` with a C++17 compiler and run it; it directly inspects all \(\binom{89}{4}=2,441,626\) four-subsets and 16 patterns per subset, without the Python normal-form reduction. Every pattern occurs, with minimum per-four-set coverage exactly 16.
3. The `run_checks.sh` script performs both operations. The two recorded outputs `verify_paley89.stdout.txt` and `verify_paley89_direct.stdout.txt` capture the completed checks; the latter's elapsed seconds depend on the machine.

The finite certificate is exhaustive for the precise first-order threshold claim. It does not establish any assertion for Paley parameters above 89. The reduction from 4-e.c. to agreement with the Rado graph through quantifier rank five is a mathematical proof given in RESULT.md, not a finite experiment. The computations and proof have not been independently audited.
