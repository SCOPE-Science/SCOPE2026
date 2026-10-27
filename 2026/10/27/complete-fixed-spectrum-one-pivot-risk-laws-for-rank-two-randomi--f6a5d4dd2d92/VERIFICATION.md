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

The finite checks in `check.py` use Python's standard library, with exact fractions for integer-Gram instances and floating arithmetic only for the general three-atom construction checks. The exact tests reconstruct the diagonal-weighted one-pivot probability and Schur-complement residual trace, verify the spectrum-determined mean and the variance envelope on 1,116 full-rank integer Gram cases, and confirm three distinct laws sharing spectrum \((20,2)\). One hundred numerical three-atom construction checks test off-diagonal cancellation, the eigenvalue constraints and the target pivot probabilities. Executable invocation: `python3 check.py`.

The finite verifier does not establish the theorem for every finite-support law or for arbitrary real inputs. Those quantified claims rest on the explicit paired-row Gram construction, Jensen/chord bounds and the elementary sharp tail inequality in `RESULT.md`. The exact expectation identity is prior work, and independent review has not been performed.
