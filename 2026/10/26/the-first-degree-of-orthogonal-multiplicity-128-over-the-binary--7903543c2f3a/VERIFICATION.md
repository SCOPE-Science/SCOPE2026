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

# Exact replay

Compile `verify.c` using `cc -O2 -std=c11 -Wall -Wextra verify.c -o verify`; execute `./verify` from the same folder. The verifier independently tests monic irreducibles of degrees 2–6 using trial monic division, constructs all 6 degree-25 and 66 degree-26 candidates, and exhaustively enumerates all 2^25 and 2^26 words with degree-one polynomial continuants. A successful run prints `VERIFY_OK` with 0 positives in degree 25, one degree-26 positive at coefficient mask `123935485`, and multiplicity `128`.

# Actual run

Compiler and program executed successfully with `-O2 -std=c11 -Wall -Wextra`. Output:

```
irreducibles_degree_2=1
irreducibles_degree_3=2
irreducibles_degree_4=3
irreducibles_degree_5=6
irreducibles_degree_6=9
degree_25_candidates=6 positive=0
positive_degree_26: 123935485
degree_26_candidates=66 positive=1
witness_word_mask=52109888 witness_multiplicity=128
VERIFY_OK
```

# Limits

The finite counts are exhaustive, not probabilistic. The inference that orthogonal multiplicity at least 128 requires seven distinct nonlinear irreducible factors uses Blackburn's published theorem. The procedure does not certify an infinite family, an independent audit, or originality against inaccessible literature.
