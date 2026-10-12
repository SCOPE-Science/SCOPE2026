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

## Reproduction

Run `python3 verify.py` with Python 3.9 or later from the extracted package directory. No third-party libraries, downloads, network access, or external datasets are required. The script uses exact integers and `fractions.Fraction` to reconstruct the characteristic polynomial of each tested tree via its matching expansion, and prints its summary only after all assertions succeed.

Expected output:

```
VERIFY_OK tree_cases=34 parity_probes=2788 derivative_and_endpoint_identities=102
```

## What was checked

Thirty-four constructed even-order trees from four structural families were used. In each case, the generalized characteristic determinant is zero at eigenvalues \(0\) and \(2\); the integer coefficient of its linear term is exactly \(-2(n-1)\), and no evaluated reduced even-numerator/odd-denominator rational interior candidate is an eigenvalue. A total of 2,788 exact interior rational evaluations were performed.

## Boundary of verification

This code does not exhaust arbitrary tree orders or possible rational eigenvalues, and does not numerically simulate perfect state transfer over unbounded time. The unrestricted no-transfer result follows from the independent analytical chain in `RESULT.md`: matrix-tree derivative, rational-root and bipartition symmetry, integer-vector congruence via leaf stripping, and the strong-cospectrality phase contradiction. Verification is an aid to detecting arithmetic mistakes, not an independent audit or an infinite proof.
