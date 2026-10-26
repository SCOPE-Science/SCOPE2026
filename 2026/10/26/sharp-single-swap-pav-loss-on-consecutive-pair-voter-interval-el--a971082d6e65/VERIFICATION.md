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

The exact combinatorial proof is in `RESULT.md`. The accompanying `verify_path_pav.py` independently computes adjacent-pair counts for every \(k\)-element subset of a path with \(2k-1\) candidate positions, for each integer \(1\le k\le10\), and directly tries all one-for-one replacements. It checks the claimed sharp bound and explicit extremizers using integer operations only. The checks cover finite \(k\) and do not establish the infinite theorem; the proof does.

A successful local run of the supplied file prints ten `k=...` records. For \(k=1,\dots,10\), the exact worst adjacent-pair counts are `0,0,1,1,1,2,2,2,3,3`, respectively. No publisher or third-party paper is embedded in this package.
