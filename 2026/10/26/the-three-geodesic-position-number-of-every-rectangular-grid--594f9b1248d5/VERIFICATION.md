---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every 2x2 rectangular tile has gp_3 at most 2; every 3x2/2x3 tile at most 3, with only alternating 3-vertex masks (101,010) or (010,101); every 3x3 tile at most 5 by the adjacent-column constraints. Tiling m=2a+3epsilon, n=2b+3delta yields upper (mn+epsilon*delta)/2; coordinate checkerboard meets geodesics length<=3 in at most two points and attains it. Equality on a three-row strip forces each 3x2 tile to be one of two phases, while adjoining mismatched phases form a forbidden triple; odd final column selects the unique larger parity class. Independently recomputed small tile forbidden triples and 3xn maximizers; finite tests corroborate the complete tiling/propagation proof.

## originality

PASS

Klavžar–Rall–Yero study general d-position sets and already cover half-order grid bounds in even-even cases; Cody–Moore solve 2-row grids and leave wider grids as open. The result supplies the remaining mixed/odd-parity rectangular grid values for gp_3 and full three-row optimizer rigidity.

## value

PASS

Settles an explicit natural geometric graph invariant for every two-dimensional rectangular grid and classifies 3-row optimizers; not merely a finite grid census or previously established even-even case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
