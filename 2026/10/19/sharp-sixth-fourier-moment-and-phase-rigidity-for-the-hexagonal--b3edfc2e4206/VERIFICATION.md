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

Run `python3 checker.py` beside this file, using Python 3 and no third-party dependencies. The included `checker_output.txt` contains the recorded output of that exact package file. The checker independently constructs all \(6^3=216\) ordered sums, the 37 convolution fibers, and the complete balanced sixth-moment polynomial; it verifies the exact identity
\[
F=20s^3+120s e_2+420e_3
\]
and the ratio \(2040/6^3=85/9\). It also tests 350 bounded complex Gaussian-integer coefficient arrays and 216 nonnegative balanced integer triples, and checks nonaliased finite-grid Fourier averages at orders 7, 8, and 9. The size-six boundary witness yields the exact flat sixth moment 2046.

The global upper bound for arbitrary complex coefficients is **not** inferred from finite testing. It is derived by strict coefficient symmetrization, exact fiber enumeration, and sharp symmetric-polynomial inequalities. Likewise, the phase classification is deduced from the relevant triple fibers, not sampled from a finite phase alphabet. The self-review is complete; no independent audit is claimed.
