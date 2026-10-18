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

The accompanying `verify_facets.py` is standalone Python 3 code without third-party dependencies. From the extracted folder run `python3 verify_facets.py`. It checks each entry of the displayed transfer matrix by a separate small union-find reconstruction; verifies the exact row identity that implies the recurrence; compares 63 transfer coefficients with the formal recurrence; and enumerates every normalized integer Lipschitz potential for sizes \(2\le n\le11\), computing saturated-edge connectivity directly. The program printed `PASS 124 exact assertions` on this package. These tests do not enumerate arbitrary real points; their coverage of all real vertices is established separately by the proved integral-height lemma.

Scientific proof checkpoints: (1) the vertex–facet polarity and tight-component rank identity; (2) no omitted tight component when eliminating the older boundary point; (3) exact transition matrix; (4) exact row polynomial identity; (5) base values and rational-series algebra. Beyond the stated graph family, no extension is claimed.

No independent audit or external certification has been performed.
