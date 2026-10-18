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
# Reproducibility

Run `python3 verify.py` with Python 3.9 or newer; no external packages or data files are needed. Expected final line: `VERIFY_OK exact_checks= 1065`.

The program performs exact rational inversion of \(I-\theta hQ\) on 1,008 combinations (six sizes, three positive rate patterns, seven theta parameters, eight timesteps), verifies row sums, all off-diagonal signs, all theta-step diagonals, and the exact positivity equivalence. It additionally performs 55 strict Karamata-consistent product comparisons for fixed-sum rate vectors and checks an exact three-state finite crossing on each side.

These are finite algebraic consistency checks, not an enumeration of arbitrary real rates, arbitrary sizes, or the continuum of timesteps. The universal assertions follow instead from the explicit resolvent product identity, the strict diagonal logarithmic derivative and the strict concavity argument in `RESULT.md`. Independent mathematical audit has not been performed.
