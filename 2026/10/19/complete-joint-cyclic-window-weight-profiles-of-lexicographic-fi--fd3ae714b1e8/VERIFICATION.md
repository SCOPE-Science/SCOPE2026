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

The theorem is proved for every integer \(m\ge1\) in `RESULT.md`; this file reports finite consistency checks without claiming independent certification. Run `python3 code/check_profiles.py` using Python 3.10 or newer (standard library only). It builds the affine evaluation vectors in the exact stated index order, directly lists cyclic zero-runs, and compares **full joint signatures** and multiplicities against the theorem for \(1\le m\le8\). It then independently scans individual cyclic windows to verify the marginal enumerator of every window length for \(1\le m\le7\).

Expected complete-profile counts for dimensions \(m=1,2,3,4,5,6,7,8\) are \(3,4,6,10,18,34,66,130\); the histogram is respectively two singleton profiles, one doubleton profile, and \(2^{m-1}-1\) fourfold profiles. Actual integer computations yielded these values for every checked dimension. This finite check does not rule out all possible errors in an infinite proof, and no independent audit has been performed.
