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

The package contains a complete deletion certificate and an independent replay script for the finite claim. Run `python verify.py` beside `DELETION_CERTIFICATE.json`.

The replay performs these checks from the encoded source and target orders:

1. It exhaustively considers all \(6^8\) set maps and keeps exactly the order-preserving maps, obtaining \(738\).
2. It reconstructs the entire pointwise mapping-poset relation.
3. It replays every one of the \(732\) deletions against the current surviving subposet. For an up-beat deletion, the recorded witness must be the minimum of the current strict upper set; for a down-beat deletion, it must be the maximum of the current strict lower set.
4. It checks the deletion totals \(128\) up-beat and \(604\) down-beat.
5. It checks that the six survivors are exactly the constant maps and that their inherited order is precisely the order of \(X_2\).
6. It checks directly that the six-point terminal subposet has no beat points.

Actual replay result from the packaged files:

`VERIFY_OK maps=738 deletions=732 up=128 down=604 core=6`

The computation proves only this finite mapping-space claim. It is not an exhaustive proof of any statement over arbitrary dimensions, and no such extrapolation is made.
