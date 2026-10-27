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

The proof reduces the general theorem to the finite-tree covering-walk lemma, classical Munn-tree class equivalences, and the published logspace normal form theorem for fixed free groups. These steps are explicit in RESULT.md. The logspace complexity itself is not inferred from finite experiments.

Run `python3 green_geodesic_check.py` with the standard library. It enumerates every word of length zero through six on a symmetric two-generator alphabet: 5461 words. The program groups independently by the exact H/R/L/D classes of the Munn prefix trees, computes each class's shortest represented length from all words in the search range, and compares that length with the four geometric formulas for every word. It completed with `VERIFY_OK words=5461 rank=2 lengths=0..6 types=H,R,L,D`, and class-profile totals `H:4099 R:2725 L:2725 D:986`.

The finite range is exhaustive only within its stated word bound and is not a proof of deterministic logspace for unbounded inputs. The theoretical complexity claim uses the established logspace free-group normal form construction. Independent mathematical audit: not performed.
