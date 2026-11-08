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
# Finite verification

Execute `python3 verify.py` beside `triple_orbits.tsv`. The table contains exactly 35 translation-orbit representatives for each graph, 70 data rows total; every triple belongs to one of these orbits of cardinality 16. Every representative has an eight-bit complete trace mask, with `ff` exactly when shattered. The script recomputes every representative, each mask, and each translation orbit directly, then compares the entire table. It separately traverses all \(560\) vertex triples and all \(1820\) four-element supports per graph using two trace-calculation implementations; the larger support obstruction is proved in `RESULT.md`.

Expected final output marker: `SRG16_CLOSED_SHATTER_PASS 2 graphs 70 triple orbit rows 1120 triples 2*1820 four-supports`.

No randomized checks, undocumented external software, or infinite extrapolation are involved. The certificate establishes finite computation correctness conditional on execution and exact graph definitions; an external independent audit has not been performed.
