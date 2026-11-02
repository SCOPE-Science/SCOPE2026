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

# Reproduction and limits

Execute from the directory containing this file and the two included scripts:

```sh
python3 checker.py
python3 numeric_example.py
```

`checker.py` requires only the Python 3 standard library. It enumerates all connected undirected graphs on three, four, and five labelled vertices, compares the first two nonzero killed-generator Taylor coefficients with an independent first-hit path enumeration for every source and target with distance at least two, tests additional randomly sampled weighted and asymmetric finite graphs including multiple farthest targets, and checks the two pendant-tree coefficients. Its observed output was `PASS: 6807 exact rational assertions`.

`numeric_example.py` uses only the Python 3 standard library and evaluates the small-tree cover-time survival functions through the nonnegative uniformization expansion of killed generators, followed by composite Simpson quadrature. Its output for \(N=10000\) was approximately \(1.34879037\) without the pendant leaf and \(1.69337030\) with it, after subtracting the leading \(N^{-1/2}\) term and multiplying by \(N\). The theorem predicts limits \(4/3\) and \(5/3\). Finite quadrature is diagnostic; numerical tolerance and truncation cannot certify an asymptotic statement.

The general theorem follows from the analytic first-hit expansion, finite inclusion-exclusion, uniform integrability on the extreme-time scale, and near-target comparison in RESULT.md. No external formal proof, third-party audit, or independent validation is asserted. Historical novelty cannot be guaranteed by a finite search.
