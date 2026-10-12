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

# Reproducibility of the six-season result

The embedded `verify.py` is a standalone scientific checker. It requires Python 3 and SymPy 1.12 or newer as listed in `requirements.txt`. Run `python verify.py` in the extracted directory. It reports `VERIFY_OK` after evaluating symbolic identities and exact-rational comparisons.

The checker constructs \(J=L\operatorname{diag}(u,1)\), \(A=L\operatorname{diag}(1,v)\), enumerates all twenty balanced six-character words, partitions them into exactly four cyclic necklaces of sizes \(6,6,6,2\), and verifies the traces of two mixed classes agree. It checks one determinant common to all classes, the two exact factored trace-gap identities, and the correspondence of every balanced word to its trace representative. An independent arithmetic path implements \(2\times2\) matrix multiplication with `fractions.Fraction` and checks 192 rational parameter tuples plus one exact growth/decline witness.

The polynomial identities establish algebraic equality over all real parameter values; finite numerical tests are supporting checks only and are not an exhaustive proof of an infinite-domain theorem. Symbolic computations and the written sign/Perron argument do not constitute external certification or independent review. Positive-matrix assumptions, six-season three-plus-three scope, and the inaccessible full text of one relevant ecological article limit the evidence.
