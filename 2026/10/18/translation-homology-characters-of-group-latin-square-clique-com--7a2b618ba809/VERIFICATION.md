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

`verify.py` is standalone Python 3 standard-library code that enumerates actual cliques from the graph adjacency relation, computes signed traces by explicit vertex permutations, and compares them with the theorem. It also enumerates cyclic and two-generated translation subgroups and the full group, and checks quotient-rank formulas for the resulting distinct subgroups.

The groups tested are \(\mathbb Z/5\mathbb Z\), \(\mathbb Z/6\mathbb Z\), \(\mathbb Z/7\mathbb Z\), \(\mathbb Z/8\mathbb Z\), \(\mathbb Z/2\mathbb Z\times\mathbb Z/4\mathbb Z\), \((\mathbb Z/2\mathbb Z)^3\), and \((\mathbb Z/3\mathbb Z)^2\). In particular, the three nonisomorphic groups of order eight are compared. For cyclic orders five and six, the code additionally constructs all simplicial boundary matrices over \(\mathbb F_2\) and computes complete reduced Betti vectors by exact bitset elimination.

To run: `python3 verify.py`. Expected exact stdout is embedded as `verify_output.txt`. These finite checks are independent of the all-parameter algebraic argument but cannot prove its universal quantifier. The proof of the universal quantifier is in `RESULT.md` and depends on the established nonequivariant homology concentration in the cited 2026 primary paper. No integral or unstable homotopy claims are verified.
