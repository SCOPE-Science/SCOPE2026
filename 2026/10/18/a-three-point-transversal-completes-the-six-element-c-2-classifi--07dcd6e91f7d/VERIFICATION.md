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

# Reproducibility and verification

With Python 3 and the standard library, in the directory containing the supplied files, execute `python3 verify_triple_equivalences.py 6`, `python3 crosscheck_triple_equivalences.py`, and `python3 triangle_witnesses.py`.

The first enumerates every isomorphism type of three named equivalences through six elements and computes globally synchronized vertex colour-refinement histograms from all eight binary atomic masks. Its key six-element outputs are **21,205** isomorphism types, **21,197** counting-logic classes and **eight** doubletons. The second independently checks all isomorphism totals by a Burnside fixed-partition sum, separately checks the nonisomorphism and counting-logic indistinguishability of all sixteen exceptional structures, and checks four symmetry orbits of sizes **1, 3, 3, 1**. The third exhausts twenty unordered three-vertex subsets per exceptional structure; every ambiguous pair has common-transversal counts **0** and **2**. It reproduces the machine-readable `COLLISIONS.json` witness catalogue.

All three checks were executed successfully from the supplied program files. Enumeration, not a log alone, constitutes the finite verification. The underlying standard finite-model-theoretic correspondence between counting logic and colour refinement is cited to Kiefer--Schweitzer--Selman (2015). The result is restricted to structures of at most six elements. No third-party or independent audit has been performed.
