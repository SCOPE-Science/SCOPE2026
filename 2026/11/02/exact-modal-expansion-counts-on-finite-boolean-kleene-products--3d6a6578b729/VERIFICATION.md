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
Run `python checker.py` with Python 3.10 or newer. The checked script prints `ALL_CHECKS_OK filter_masks= 30 independent_full_unary_censuses= 4 n_range=1..4 carrier_sizes=2,3,4,6` upon success.

The first check enumerates, for every labelled support \(H\subseteq[n]\) with \(1\le n\le4\), all principal or inactive Boolean output thresholds and all join-preserving diamond neighborhoods. It tests the two contact and filter-coverage conditions directly on every subset pair; it does not assume the formula when counting admissible choices. The second check exhausts **all** unary functions on the full fixed Kleene carriers of cardinalities \(2,3,4,6\), directly checking (MK), (Pos), and (Con), with no use of the normal-form classification. These computations test boundaries and provide independent small-case evidence only.

The infinite family and all exact counts for larger carriers are proved symbolically in `RESULT.md`; the program does not certify originality or independently validate the general proof. This scientific review is not an independent audit.
