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

The symbolic proof enumerates all four primitive normal-ray families, uses an explicit pairing argument for each and invokes Nill's complete-toric group theorem. No external certificate or independent validation is asserted.

The bundled checker uses Python 3 standard library, with no network, no nondeterministic steps and no external packages. Run `python3 three_tier_roots_check.py` alongside its companion output file. It brute-forces all characters in the displayed bounded integer box for ten selected parameter triples; agreement with the theorem is a finite regression, not an exhaustive test for arbitrary parameters. The saved check output records each exact case and its group-dimension prediction.

The literature inspection covers the relevant root-theoretic statements and the cited full-text Hibi/poset-toric constructions. The possible existence of an equivalent unindexed result remains unverified. The disconnected automorphism group and finite central isogenies are outside the theorem.
