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

# Reproduction and proof verification

Run `python -m pip install -r requirements.txt` if needed, then `python verify.py` from the folder containing these files. The program was executed with 110-decimal-digit mpmath arithmetic and returned:

`PASS: 382 independent finite and high-precision assertions`

The code independently computes the two-dimensional environmental density-matrix spectrum, verifies the entropy variational envelope against 200 random finite-support photon-number distributions, locates and checks strict finite-energy stationary optima, reproduces the two exact endpoint thermal identities, and tests successive small-\(r\) essential-singularity ratios. The program is a finite numerical corroboration, not a proof of the universal energy-constrained quantum/private capacity theorem or the asymptotic limits. Those rely on the analytic reductions, standard degradable-channel coding theorem, entropy inequalities, concavity, and uniform small-\(q\) derivative expansion in `RESULT.md`.

In the exact theorem, \(E>0\) is fixed as \(r\downarrow0\); the phase noise consists of independent binary kicks only. Independent mathematical or priority audit has not been performed.
