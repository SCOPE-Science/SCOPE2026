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

The exact checker is `verify_genus6_alexander.py`.

Run:

`python3 verify_genus6_alexander.py`

Expected output:

`VERIFY_OK total=16 admissible=11 unique_negative_root_support=6,5,3,2,1 root_count=1`

The script uses only Python's standard library. It constructs every genus-six support pattern allowed by the alternating-coefficient theorem, removes the five support patterns forbidden by Proposition 2.4, and applies Sturm's theorem over exact rational arithmetic to \(Q(t)=t^6\Delta(t)\). The interval is \(( -\infty,-1)\), so no floating-point approximation is used to certify the required negative root.

The mathematical bridge from this finite check to the knot statement uses three published facts: elliptic surgery makes \(K\) an L-space knot; Corollary 3.7 of arXiv:2609.39260v1 forces \(-\lambda<-1\) to be an Alexander root when \(r>21\); and the finite-surgery slope classification reduces the interval \(21<r\le23\) to \(22\) or \(23\) in genus \(6\).

Limit: the checker verifies the finite polynomial classification only. It does not independently prove the cited topology theorems.
