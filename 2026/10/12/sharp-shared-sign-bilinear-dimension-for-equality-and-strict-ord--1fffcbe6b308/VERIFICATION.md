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

## Reproducible arithmetic check

Run `python3 verify.py 100` using Python 3 without external libraries. Expected output:

```
VERIFY_OK max_domain=100 domain_sizes=100 pairs=338350 standalone_3point_relation_checks=18
```

The integer algorithm evaluates all pairs \((i,j)\) on the indicated domain sizes and checks that every equality/strict-order score is strictly positive or strictly negative in accordance with its atomic truth value. It also tests two-dimensional *separate* witnesses for each relation on the three-element domain. The \(338350\) reported domain pairs each receive two relational sign tests; the separate-witness checks contribute 18 more tests.

## Symbolic check and limits

The equations \(h_i^{\mathsf T}B_{\mathrm{eq}}h_j=1-2(i-j)^2\) and \(h_i^{\mathsf T}B_{\mathrm{lt}}h_j=2(j-i)-1\) give the full upper-bound proof over all finite domain sizes; the finite program merely catches transcription errors. The impossibility of dimension two on a domain of at least three elements uses the positive-dependence lemma in `RESULT.md`, not numerical optimization or finite enumeration. It assumes strict sign semantics with no zero scores and shared vectors for both argument positions.

Independent audit: not performed. The mathematical checks described here are not independent validation.
