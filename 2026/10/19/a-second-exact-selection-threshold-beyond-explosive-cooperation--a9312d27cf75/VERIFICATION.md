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

`python3 VERIFY.py` runs with only the Python standard library. The final test run reported `PASS: 787 exact and numeric assertions`. It checks rational polynomial identities, multiple independent parameter examples, boundary and interior potential conditions, finite-state birth–death probability normalization and detailed balance, and a finite-size progression toward the stated stationary limits.

## Analytic checks not replaced by the finite tests

The proof establishes the fold by an exact discriminant/tangency calculation; it establishes uniqueness of the potential crossing via the strictly positive derivative \(\int_0^{r_+}t(1-t)\,dt\). It obtains stationary weights directly from detailed balance and bounds the remaining prefactor uniformly for fixed parameters. The critical equal-height case requires the separate \(O(N^{-1})+O(N^{-3/2})\) comparison to the defection-boundary weight; its validity does not follow from a generic numerical fit or from large deviations alone.

## Scope and unverified statements

No transfer to a random higher-order network with spatial correlations is proved. No mixing time, finite-population practical observability or universal behavior under different mutation scalings is asserted. The equality-point selection relies specifically on \(\mu_N=N^{-2}\). The attached tests do not independently audit the proof, scientific value or publication priority.
