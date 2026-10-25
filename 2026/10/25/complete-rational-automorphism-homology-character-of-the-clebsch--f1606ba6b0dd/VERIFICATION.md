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

Run `python3 verify_clebsch_module.py`. No downloaded resources or external packages are required. The verifier checks the graph presentation and simplex counts, exhaustively certifies a 191-pair acyclic discrete-Morse matching on the full 392-element nonempty face poset and all 1200 Hasse incidences, evaluates all 1920 signed simplicial automorphism traces, then performs exact 16-point Walsh–Fourier character extraction on the translation subgroup.

The successful direct replay produced all four completion markers: `MORSE_191_PAIRS_ONE_VERTEX_NINE_3CELLS_ACYCLIC 392 1200`, `ALL_1920_FULL_AUTOMORPHISM_CHARACTERS_VERIFIED 1920`, `TRANSLATION_MODULE_FOUR_TRIVIAL_PLUS_FIVE_DISTINCT_LINES_VERIFIED`, and `CLEBSCH_FULL_RATIONAL_HOMOLOGY_MODULE_VERIFIED`.

The certificate is exhaustive only for this finite complex and finite group. The noncomputational deductions use Forman's acyclic matching theorem, the reduced Euler–Poincaré Lefschetz trace identity, and rational character uniqueness. The certificate is not an independent mathematical audit or an integral representation classification.
