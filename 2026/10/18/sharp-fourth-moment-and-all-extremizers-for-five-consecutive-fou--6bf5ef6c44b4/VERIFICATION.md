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

# Verification details
The self-contained Python 3 / SymPy checker `verify.py` was executed against its actual local file and completed successfully. It reconstructs all five aperiodic autocorrelations, the normalized fourth-moment polynomial, both stationary numerators, the elimination of the inner coefficient ratio, the rational expression for the optimum, and the coordinate-boundary rational identities, using exact symbolic polynomial arithmetic. It verifies the unique positive root and displayed numerical values at high precision. It additionally verifies the no-aliasing difference argument on representative cyclic sizes; the proof establishes that condition universally for all \(N\ge9\), independently of sample tests.

The scientific proof is in `RESULT.md`. Finite numerical or computational checks alone are not asserted to certify all frequencies; symbolic identities plus positivity, compactness and Fourier orthogonality supply the unrestricted proof. Independent external audit has not been performed. Literature novelty remains subject to older unindexed results.
