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

Run `python3 verify.py` beside `certificate.json`.

The verifier computes \(E_N=3D_N\) directly from the definition through \(N=4^9\). It checks the four local \(01\)-occurrence identities and all four residue recurrences on every complete four-block.

A separate evaluator reads the base-\(4\) expansion of \(N\) and updates only the pair \((E,t)\) using the claimed recurrence. Its value is compared with the direct prefix count for every tested index.

For \(1\le k\le9\), direct enumeration verifies the exact maximum, minimum, and the explicit witnesses. Finally, an independent two-state dynamic program checks the closed max-plus and min-plus formulas through depth \(100\).

These computations verify the implementation and algebra on large finite ranges. The theorem for all \(k\) and the asymptotic constants are proved symbolically by the recurrences and induction in `RESULT.md`.

Independent audit has not been performed.
