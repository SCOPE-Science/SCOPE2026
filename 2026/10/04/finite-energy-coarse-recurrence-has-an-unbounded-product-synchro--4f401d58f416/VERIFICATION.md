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

The proof was checked directly from the positive \(\varepsilon\)-\(\ell^p\) chain definitions. Projection gives the lower bound for every \(p\). For \(p=\infty\), concatenating a chain does not change its error norm, so factor chains can always be synchronized to a common length.

For the finite examples, all distinct metric distances are either \(1\) or \(D\). Below \(D\), the transition graph has only exact orbit edges and one unit reset per factor. A factor return therefore has exactly one unit reset per \(L\)-step block. In the product, the unit-error times in one least common multiple block are the union of multiples of \(L\) and \(M\), whose cardinality is \(M/g+L/g-1\), with \(g=\gcd(L,M)\). This proves the exact finite-\(p\) threshold after choosing \(D\) larger than that norm.

The included checker recomputes shortest finite-state return energies for representative \((L,M,p)\) values and verifies the counting formula. It is a consistency check only; the all-parameter conclusion is established by the symbolic argument above.

The motivating coarse-chain paper and the closest classical product-recurrence paper were inspected in full at the relevant definitions and theorems. No positive-threshold synchronization theorem was found. Independent audit was not performed.
