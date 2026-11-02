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

# Finite reproducibility certificate

Execute the two complete standalone Python standard-library programs embedded beside this document:

```
python verify_projective_exact_cover.py
python verify_fano_cosets.py
```

`verify_projective_exact_cover.py` enumerates all 35 coordinate lines as triples of binary vectors, all 56 exact point-covering spreads, all 240 exact line-covering packings, and every unordered pair of different packings. Assertions check the exact common-spread histogram, nonexistence of trades smaller than three, 7-regularity, 840 edges, the absence of 4-cycles, graph bipartiteness and the all-root distance census. Its success lines are:

```
PROJECTIVE_EXACT_COVER_ALL_240_PACKINGS_PASS
MINIMUM_TRADE_3_DEGREE_7_EDGES_840_GIRTH_6_DIAMETER_5_PASS
ALL_ROOT_DISTANCE_DISTRIBUTION (1, 7, 42, 105, 77, 8)
```

`verify_fano_cosets.py` uses an independent eight-symbol construction via complementary four-subsets. It enumerates the 30 distinct labelled Steiner systems on each seven-of-eight symbol set, constructs their 56 canonical five-line spreads, verifies each exact packing, computes every three-spread replacement, and checks equality with the missing-label star-transposition image for all unordered pairs. It exhausts all 40,320 permutations for the parity split and performs BFS from all 240 packings. Its success lines are:

```
EIGHT_SYMBOL_FANO_COSSET_240_PACKINGS_PASS
ALL_STAR_TRANSPOSITION_TRADES_AND_TWO_CHIRALITIES_PASS
ALL_ROOTS_DIAMETER_5_DISTANCE_DISTRIBUTION_PASS (1, 7, 42, 105, 77, 8)
```

No external dependencies, archive files, random seeds, downloaded papers, or network services are needed for reproduction. Successful execution certifies only the exact finite claim for this one space. It does not certify publication novelty, any infinite-family generalization, or independent external audit.
