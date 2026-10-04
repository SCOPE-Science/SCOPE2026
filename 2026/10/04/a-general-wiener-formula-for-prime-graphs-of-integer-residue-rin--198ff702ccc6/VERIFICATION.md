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
The proof was reconstructed from the ring-prime-graph definition and checked independently.

Exact symbolic points checked:
- in a commutative unital ring, prime-graph adjacency is equivalent to zero product;
- the zero vertex makes every nonedge a distance-two pair;
- for fixed \(x\bmod n\), exactly \(\gcd(x,n)\) residues \(y\) satisfy \(xy\equiv0\pmod n\);
- grouping by gcd gives \(T(n)=n\sum_{d\mid n}\varphi(d)/d\);
- multiplicativity gives \(T(n)=\prod p^{a-1}((a+1)p-a)\);
- square-zero residues number \(S(n)=\prod p^{\lfloor a/2\rfloor}\);
- deleting the diagonal and quotienting ordered pairs by symmetry gives \(|E|=(T-S)/2\);
- the Hosoya and Wiener formulas then follow from the distance-one/distance-two partition.

`artifacts/verify.py` constructs the graph directly for every \(2\le n\le300\), compares the exact edge count and Wiener index with the formulas, and separately checks many specializations against the six formulas printed in the 2024 paper. It returns `VERIFY_OK`.

Finite computation is corroboration only and is not used as a proof of the all-\(n\) theorem.
