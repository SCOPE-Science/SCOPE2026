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

# Verification protocol

Unpack `verify.py` beside the manuscript and run `python3 verify.py`. The code uses only exact standard-library integer/fraction arithmetic for its recurrence, binary-matrix counts, character calculations, and small finite unit groups. It checks the exact finite-field matrix rank identity, complete independence of the first five quadratic sign-coordinate maps on their reduced residue rings, and the inequality between the quadratic obstruction cutoff and the full-generator cutoff on eight small squarefree moduli. The last four sample-frequency comparisons use a fixed deterministic pseudorandom seed and are illustrations, not proofs.

Observed execution: `EXACT_CHECKS 130` and final marker `VERIFY_OK`. Four finite sample rates were \(0.36500,0.65820,0.33460,0.62400\), compared against the exact matrix-model rates \(0.37500,0.65625,0.328125,0.615234375\).

The analytic step is the standard Siegel--Walfisz theorem uniformly up to a fixed power of \(\log X\). The proof explicitly ensures this conductor bound by the stated restriction on the growth of \(r\). The code does not attempt to certify that theorem or the asymptotic limits by enumeration. No independent review has been performed.
