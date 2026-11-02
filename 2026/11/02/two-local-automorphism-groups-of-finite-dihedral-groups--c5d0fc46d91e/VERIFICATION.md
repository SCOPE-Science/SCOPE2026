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
# Verification of two-local automorphisms of dihedral groups

The symbolic proof in `RESULT.md` gives an all-dimensional theorem. The accompanying `check.py` is a standalone exact-arithmetic corroboration and requires only Python's standard library. From the directory containing both files, run `python check.py`.

The checker directly generates dihedral automorphisms from the presentation and, for every \(n=3,4,5,6,7,8\), checks each proposed map against the set of attainable images of each unordered pair of distinct domain elements. Since ordered pairs have the same condition after reversal, this exhausts the required interpolation tests. Every candidate is also checked to be distinct, and its total number is compared with the independent prime-factorial product calculation. The results are:

| \(n\) | Ordinary automorphisms | Two-local maps |
| ---: | ---: | ---: |
| 3 | 6 | 12 |
| 4 | 8 | 16 |
| 5 | 20 | 480 |
| 6 | 12 | 24 |
| 7 | 42 | 30240 |
| 8 | 32 | 512 |

The checker separately enumerates every permutation of the entire underlying set for \(n=1,2,3\), testing the original group-product equation to identify automorphisms and the original pair-image condition to identify two-local maps. Their respective counts are \((1,1)\), \((6,6)\), and \((6,12)\). The checker ends with `VERIFY_OK`.

The infinite family is **not** established by computational exhaustion; the key prime-power unit-congruence lemma, Chinese remainder reduction, and rooted-tree count are mathematical arguments in `RESULT.md`. All input integers used in the checker are exact. The checker assumes the dihedral group presentation stated in `RESULT.md` and does not analyze arbitrary groups or two-local endomorphisms.
