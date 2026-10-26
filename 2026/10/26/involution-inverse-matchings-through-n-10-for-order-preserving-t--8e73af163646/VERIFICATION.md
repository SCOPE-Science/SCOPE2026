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

# Verification record

The certificate `INVOLUTION_MATCHINGS.tsv` has exactly 62,704 two-cycle rows. A full execution of `python verify_involutions.py INVOLUTION_MATCHINGS.tsv` reconstructed every rank from \(n=1\) to \(10\), checked disjointness and mutual-inverse transversal conditions on every paired map, and checked idempotency of every unpaired map. For \(n\le5\), the checker additionally composed all paired maps directly and checked both inverse equations. This is a complete finite-range certificate, not evidence for arbitrary \(n\).

An independent audit has not been performed. The checker uses only the Python standard library and the exact included certificate; no external mathematical package or network call is required. The last case contains \(92{,}378\) transformations. Any claim for larger chain sizes requires new evidence.
