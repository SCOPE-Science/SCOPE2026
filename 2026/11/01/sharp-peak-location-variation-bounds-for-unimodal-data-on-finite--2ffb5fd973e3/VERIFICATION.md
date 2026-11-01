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

The analytical derivation is contained in `RESULT.md`. Its central step compares the summed excess above any real threshold on two centered graph balls with the same clipped right endpoint; terms removed on the left are nonpositive. Reflection gives the other side. This proves the unimodality-preservation assertion for every path size and all nonnegative real data.

The two endpoint ball averages are explicit and give the variation deficit without limiting or approximation. For zero-endpoint data the unique equality class is forced by nonnegativity of all surplus coordinates. These arguments are not consequences of the finite consistency test.

The accompanying `check_unimodal.py` uses exact Python `fractions.Fraction` arithmetic to enumerate nonnegative weakly unimodal inputs with integer values in the set `{0,1,2,3}` on each path from three through eight vertices. It checks unimodality of the maximal function, the telescoping identity, the peak-sensitive inequality, the sharp zero-endpoint remainder and equality restrictions, and explicit singleton and endpoint-baseline equality cases. The documented execution returned `EXACT_CHECK_OK 4365`. This finite enumeration is not exhaustive over arbitrary real sequences or arbitrary path lengths.

No independent audit, publication-priority certification, or higher-variation extension is claimed.
