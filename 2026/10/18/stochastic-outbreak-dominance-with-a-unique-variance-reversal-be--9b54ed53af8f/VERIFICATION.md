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

# Reproducible verification

Execute `python3 verify.py` with Python 3.8 or later (standard library only). The script constructs the two exact nine-edge graphs, enumerates every one of their \(512\) open-edge subsets with each of six seed vertices, and independently computes the rooted component size by breadth-first search and union-find. It confirms vertex-transitivity at the level of all component-size distributions, equality of the first three tail probabilities, and the exact three nontrivial tail-difference polynomials.

It independently constructs the first and second moments and checks the complete degree-12 variance factorization by integer-polynomial arithmetic. It computes all 13 coefficients of the rationally transformed polynomial, verifies the single sign change, and checks the signs at the two rational endpoints \(479/1000\) and \(480/1000\). It also enumerates every labeled simple 3-regular six-vertex graph: exactly ten labeled copies of \(K_{3,3}\) and sixty labeled copies of the triangular prism appear. The analytical proof explains why these are the only isomorphism types.

The exact \(p=1/2\) moments, including variances \(847367/262144\) and \(213327/65536\), are independently reconstructed. The successful run prints five `PASS` lines; a failure raises a Python assertion. The exact tail and moment formulas can be reproduced without probabilistic simulation, floating-point decisions, or external packages.

**Limits:** Finite enumeration does not prove claims about networks of other sizes. All-parameter inequality signs and root uniqueness follow from polynomial factorization, positivity and Descartes' rule. The script is a computational verifier of the mathematical argument, not an independent external audit. Related epidemic literature remains potentially incomplete.
