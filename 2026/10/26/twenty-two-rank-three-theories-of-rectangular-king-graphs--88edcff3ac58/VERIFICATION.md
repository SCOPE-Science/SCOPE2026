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
# Verification and reproducibility

`king_rank3_verifier.py` uses only Python 3's standard library. Run `python3 king_rank3_verifier.py` in an empty writable directory to regenerate `classification.json` and reproduce the verification messages.

The first algorithm explicitly constructs the complete equality/adjacency diagram of every ordered triple (including repeated vertices), then computes all one-variable extensions at ranks one, two, and three. The second independently computes the four possible adjacency masks of a third vertex distinct from an ordered pair. The two produce exactly the same partition of all twenty-eight canonical parameter pairs into twenty-two classes. Every class is given with all its canonical members and a least-order representative in `classification.json`.

The recorded output in `verification_output.txt` is:

```
CANONICAL_OK pairs=28 classes=22 independent_algorithms=2
PATH_CHECK_OK n=7..30
EXTERNAL_PARAMS_OK unordered_pairs_m_n_1_to_12=78
CROSS_SHAPE_EQUIVALENCE_OK 3x7=4x6 5x6=7x7
SHARP_BOUND_OK minimum_maximum_representative_order=30
VERIFY_OK
```

The explicit checks for parameter pairs through twelve and for paths up to thirty are corroborative only. The unlimited-domain reduction to parameters at most seven follows from the path extension-pattern lemma and the coordinatewise Ehrenfeucht–Fraïssé product strategy in `RESULT.md`. Neither the empirical checks nor the output log alone proves the infinite assertion. No external formal certification or independent validation is claimed.
