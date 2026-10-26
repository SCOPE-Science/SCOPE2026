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

# Reproducibility and logical limits

Run `python verify.py` using Python 3 and its standard library in the folder containing the extracted script. The checker first builds adjacency lists of the exact clique-bouquet graph, including the hub. It tests every nonempty subset for connectivity and iteratively applies the original \(k\)-neighbor forcing rule. These predicate results are compared with the independently coded structural characterization; all successful sets are counted by cardinality and compared coefficientwise with a polynomial formed by separate combinatorial convolution.

The performed check returned:

`VERIFIED 671 parameter tuples and 1458592 vertex-subset comparisons`

`Includes heterogeneous blade sizes, all k from 1 to N_blades+1, and connectivity.`

The tested domain comprises \(r\in\{2,3,4\}\), all blade-size tuples with \(m_i\in\{2,3,4\}\) and total blade order at most \(11\), and each integer \(1\le k\le \sum_i m_i+1\). These finite checks catch many boundary and combinatorial errors but cannot prove all infinite parameter cases. The accompanying complete proof supplies the universal quantifiers and necessity/sufficiency arguments. The 2020 prior scalar result is acknowledged. The checks do not establish global originality, and no independent audit has been performed.
