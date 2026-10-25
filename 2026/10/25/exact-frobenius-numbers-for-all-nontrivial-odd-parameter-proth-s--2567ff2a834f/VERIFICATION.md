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
# Verification notes

The argument proves an infinite parameter family using the cited full-family Apéry reduction and greedy minimality, together with the internal binary expansion and plateau lemmas. The checker's role is independent finite confirmation of the resulting Frobenius number and unique maximal Apéry residue for admissible pairs, not a substitute for infinite reasoning.

From the package root execute:

```sh
python3 verification/check_proth.py
```

The program recomputes the greedy formula and independently computes the shortest nonnegative representative of every residue class modulo \(M+1\) using Dijkstra's algorithm on the semigroup's original generators. It checks 161 parameter pairs with 1,072,169 residue vertices, three further previously untreated examples, and exact local greedy-weight identities up to index 25. It signals disagreement by failed assertions and prints `VERIFIED` only on success.

For the concrete case \(n=7\), \(m=127\), the calculated values are \(M=16256\), \(h=7\), \(c=1\), \(t=3\), and \(F=264371337\). The statement does not certify unspecified parameters by computation alone.
