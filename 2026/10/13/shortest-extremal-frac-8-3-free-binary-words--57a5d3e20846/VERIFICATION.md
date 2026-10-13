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

Compile and run `verify.cpp` beside `certificate.json`.

The checker enumerates every binary \(\frac{8}{3}\)-free word through length \(30\) by exact suffix pruning. For every retained word it directly tests all insertion positions and both inserted letters. It confirms zero extremal words through length \(29\), exactly two at length \(30\), and the complete population vector recorded in `certificate.json`.

For the two final witnesses, an independent routine computes the least period of every factor from the definition rather than using the suffix-pruning criterion. It confirms both original words are free and all \(124\) inserted extensions are not free.

Expected output:

`VERIFY_OK shortest=30 free30=66102 extremal30=2 symmetry_orbits=1`

The claim is finite and exhaustive. No claim is made about longer lengths or thresholds above \(\frac{8}{3}\).
