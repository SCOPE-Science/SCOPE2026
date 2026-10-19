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

# Reproducibility and limits

Run `python3 verify_paperfolding_maw.py` from the directory containing this document and the source code, using Python 3.9 or later; there are no third-party package requirements.

The verifier constructs the first 2048 symbols from (i) odd-part arithmetic and (ii) the recursive parity definition and checks exact agreement. It checks absence of alternating length-four factors. For every factor length from 7 through 130 it enumerates the observed factor set and checks that its cardinality equals \(4n\). By Allouche's published complexity theorem, these exact counts establish that the enumerated finite sets are the full factor sets for those lengths. It then verifies the full bispecial-extension table at inner lengths 7 through 16, the four-versus-zero minimal absent counts for lengths 9 through 128, the lifting and preservation of extension profiles for source lengths 8 through 63, and the explicit length-nine and length-seventeen minimal absent lists.

Expected success line:

`VERIFY_OK paperfolding two_generators=2048 base_factor_sets_7_18=complete base_bispecial_7_16=checked MAW_lengths_9_128=checked extension_lifts_m_8_63=checked`

**Proof boundaries.** Finite verification does not independently prove the infinite statement, establish uniqueness of a mathematical statement in published literature, or validate Allouche's factor-complexity theorem beyond its cited proof. The infinite assertion is established by the mathematical parity and extension-preserving induction. Source access to the entire 1994 canonical-position article remained incomplete; an earlier equivalent enumeration cannot be ruled out. Independent audit status remains unperformed.
