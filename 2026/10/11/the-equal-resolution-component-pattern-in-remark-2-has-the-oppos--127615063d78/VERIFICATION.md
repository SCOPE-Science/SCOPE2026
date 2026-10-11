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

The proof has two independent checks. First, the three local closures are exactly the three perfect matchings of four boundary points. Holding the outside pairing fixed, one local matching equals it and gives two through-ball components, while each of the other two gives one four-cycle. This is an exhaustive symbolic classification, not a finite sample.

Second, after localization and then scalar extension to a field, a link with \(d\) components has rank \(2^{d-1}\) by Hendricks--Lipshitz--Sarkar Proposition 6.3. The printed plus-one hypothesis would make Huang's exact sequence have ranks \(r,2r,2r,r\). If its middle map is zero as Remark 2 states, exactness requires a rank-\(r\) map to surject onto rank \(2r\) and a rank-\(2r\) map to inject into rank \(r\), both impossible.

The verification does not assert that replacing \(+1\) with \(-1\) is sufficient to recover every localized cobordism-map formula in the remark.
