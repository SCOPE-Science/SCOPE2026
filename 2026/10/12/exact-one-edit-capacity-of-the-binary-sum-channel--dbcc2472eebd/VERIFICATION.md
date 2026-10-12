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

Extract the accompanying `verify.py` and execute `python3 verify.py` in the same directory. Python 3 standard-library facilities suffice. The observed terminal output was:

```
EDIT_BALLS 2 3 16 496
EDIT_BALLS 3 4 1024 52224
EDIT_BALLS 4 2 32 1216
NONLINEAR_GAIN 20 versus 16
VERIFY_OK
```

The generated code families use classical seeds of lengths \(2\), \(3\), and \(4\), with brute-force output-ball disjointness checked for substitutions, insertions, deletions, and the no-error output. The separate column-distance test exhausts lengths from \(2\) through \(8\). Classical seed optimality is exhaustively confirmed by an independent maximum-independent-set calculation for lengths \(2\), \(3\), and \(4\). For length \(8\), the verifier checks the distinctness and pairwise minimum distance of the known twenty-word seed from Östergård–Baicheva–Kolev's electronic listing; optimality of size \(20\) is an established result cited in the mathematical references, not certified by this finite program.

The all-parameter equality rests on the proof's fiberwise upper bound and decoder argument; the program cannot independently certify the theorem for arbitrary \(\ell,n\). Only one total edit is addressed. A published exact match in unindexed or inaccessible work is a residual originality risk. Independent external audit has not been performed.
