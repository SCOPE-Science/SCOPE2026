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

# Verification and limitations

The exact proof is in `RESULT.md`; execute `python3 CHECK.py` in a directory containing the delivered package files. `CHECK.py` requires no external dependencies. The saved output in `CHECK_OUTPUT.txt` records 54,000 exact polynomial identities, 855 exact rational branch identities, and 143 high-precision numerical phase checks.

The key verifiable algebra is the equality between the stage-sum leader cost and the normalized quartic \(G_{A,\eta}\); the shifted-quartic identity; the cubic first-order equation; and the factorization of its derivative at \(\eta=1\). These are reconstructed directly in the proof. The uniqueness of the selected global minimum rests on the one-positive-root argument for the derivative on the favored half-line. Exact branch minima, Schur thresholds, and the critical asymptotics are proved symbolically in `RESULT.md`.

Finite checks are consistency tests, not exhaustive verification of arbitrary real parameters or proof of priority. The theorem excludes constraints on incentive magnitude, nonzero reference, extra state terminal penalties, horizons other than two, and asymptotic-stability constraints imposed at the design stage. Self-review has been performed; no independent audit or external certification has been performed.
