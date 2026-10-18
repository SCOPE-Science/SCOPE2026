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

# Verification
The source `verify_centered_square.py` is standalone Python 3 and uses only the standard library. Running `python3 verify_centered_square.py` reported `VERIFY_OK: 79 Apéry calculations; pairwise gcd, minimality, exceptional gluing and symmetry bounds`.

For each integer \(2\le n\le80\), the script computes Apéry residues by Dijkstra shortest paths modulo the least generator; from those distances it obtains \(F(S_n)\) and \(g(S_n)\) and checks \(2g(S_n)=F(S_n)+1\) exactly if \(n=2\). It also directly checks the gcd formulas, minimality, and finite-range impossibility of exceptional normalized gluing relations. The integer inequalities, congruences, and Watanabe–Herzog three-generator criterion supply the infinite argument; exhaustive checking through \(80\) is not an infinite certificate.

Independent audit: not performed.
