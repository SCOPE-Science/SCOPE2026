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

The accompanying `verify_odd_cycle.py` contains exact integer arithmetic (including a Bareiss determinant routine), with no external dependencies. Run `python3 verify_odd_cycle.py` from the directory containing the file. The recorded standard output is `verify_output.txt`.

Checks: all independent sets and active facet normals for odd cycle sizes 5, 7, 9, 11, 13, and 15; unimodular subbases and torsion-free class-rank predictions; pairing with the canonical character; all pairs of special maximal-size faces, and their normal-lattice relation. The size-5 case is a deliberate Gorenstein boundary test and not part of the theorem, which starts at size 7.

The non-\(\mathbb Q\)-Gorenstein support argument for arbitrary sizes is a proof using the cited 2022 Theorem 3.4 and primitive toric class calculations. The checker covers only finitely many small cases and does not establish the general theorem, uniqueness in the literature, or any independent validation. No separate audit has been conducted.
