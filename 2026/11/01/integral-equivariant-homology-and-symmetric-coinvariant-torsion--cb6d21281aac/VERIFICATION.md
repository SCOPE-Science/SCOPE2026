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

# Reproducibility and limits

- `python check_km_tree_equiv.py` (Python 3 standard library) fully enumerates all faces of ten finite \(K_m\square T\) two-cut complexes, computes oriented signed Lefschetz traces of every specified \(S_m\times\operatorname{Aut}(T)\) action, and checks 148 exact character equalities. Named trees include paths, branching stars and a five-vertex fork.
- `python check_clique_tree_coinvariants.py` (Python 3 and `sympy`) builds integer relation matrices for the untwisted and sign-twisted \(S_m\)-actions on \(B_m\), computes their Smith normal forms for \(2\le m\le8\), and checks 14 independent presentations.

Both programs were executed successfully. The finite computations do not establish an all-tree theorem by themselves. The complete proof uses complementary-face chain duality, the vanishing of higher clique cohomology after contracting clique fibers, the injectivity of the tree incidence matrix, and a presentation calculation of integral coinvariants. No external independent audit has been performed.
