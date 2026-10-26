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

The mathematical proof treats every integer \(m\ge4\). The auxiliary program `verify.py` is an independent finite enumeration rather than a proof of the general theorem. It enumerates the gap-subsets of the semigroup, filters those stable under addition, computes colon ideals and bidual closures directly, and compares the resulting fixed points to the binary-word description. The tested range is \(4\le m\le12\), comprising 4,133 normalized ideals, and the expected terminal line is `VERIFY_OK normalized_ideals_examined=4133 multiplicities=9`.

The count and lattice conclusions rely on the general dual calculation and the path-cover bijection in `RESULT.md`; no untested large-m claim is inferred from the finite enumeration. No independent audit is reported.
