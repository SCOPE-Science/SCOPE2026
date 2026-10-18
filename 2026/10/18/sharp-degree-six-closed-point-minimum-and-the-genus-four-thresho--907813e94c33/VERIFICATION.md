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

# Exact computational verification

Run `python3 verify_closed_points_genus4.py` with `DATA.b64` in the same directory, using standard Python 3 only. The source table is derived from the initial 620 quadruples of the author's original `ListCurvesGenus4p2.txt`, original Git blob SHA `99610bd76b48b74b1ebf59c2df8052ff74d6e278`. The binary octet encoding corresponds to each of the four point counts for each entry, sorted as in source.

The executed checker asserts 620 distinct ordered entries, applies exact Newton identities and the genus-four Weil functional equation, cross-checks all degree-six counts with an independent real-Weil-polynomial recurrence, verifies the unique minimum and entire histogram, and separately enumerates all 32 elements of \(\mathbf F_{32}\) for the Artin--Schreier witness. It checks positivity for degrees seven and eight-and-above by the cited analytic inequalities.

The observed output was:

```
B6 histogram: [(1, 1), (2, 3), (3, 6), (4, 22), (5, 26), (6, 52), (7, 46), (8, 80), (9, 94), (10, 55), (11, 78), (12, 58), (13, 37), (14, 26), (15, 17), (16, 10), (17, 7), (18, 1), (19, 1)]
Unique sharp N-vector / N6 / Weil L: [(360, (3, 9, 9, 45), 21, 1, (1, 0, 2, 0, 9, 0, 8, 0, 16))]
C(F_2^1): 1
C(F_2^5): 1
VERIFIED: rho(2,4)=6; sharp B6=1 in one isogeny class.
```

This checks arithmetic conditional on the published exhaustive census, not the independent completeness of Xarles's curve classification or absence of equivalent results in unindexed literature. The smooth genus-four property of the Artin--Schreier witness follows from its unique odd pole of order nine and standard genus formula, not finite sampling alone.
