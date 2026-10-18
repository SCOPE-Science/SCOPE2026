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

# Reproducibility

Using Python 3 standard library, run `python3 verify.py`. It checks the original forth-up, forth-down, reflexivity, and transitivity clauses on every generated relation through level sizes \((3,3)\), verifies uniqueness, computes automorphism-orbits by explicit canonical relabelling for level sizes up to \((3,2)\), and independently checks Burnside fixed-point averages through \((3,3)\). Expected output:

```
labelled/unlabelled 2 2 89 38
labelled/unlabelled 2 3 762 135
labelled/unlabelled 3 2 762 135
labelled/unlabelled 3 3 5922 452
VERIFY_OK
```

For an independent check *without using the normal form*, compile and run `cc -O3 -o exhaust_orbits exhaust_orbits.c && ./exhaust_orbits`. This enumerates every reflexive binary relation on the specified world set, checks relational transitivity and both original confluences, and canonically relabels each surviving frame; expected output:

```
EXHAUSTIVE 2 2 89 38
EXHAUSTIVE 2 3 762 135
EXHAUSTIVE 3 2 762 135
VERIFY_OK
```

Run `python3 calcstats.py` to reproduce the \(n=4\) unlabelled component statistics by averaging all permutation fixed-point statistics imported from `verify.py`: \((a_4,b_4,c_4,d_4)=(33,14,173,59)\). The full arbitrary-size theorem is a proof of group-action classification; finite runs are sanity checks, not exhaustive proofs for unbounded parameters.
