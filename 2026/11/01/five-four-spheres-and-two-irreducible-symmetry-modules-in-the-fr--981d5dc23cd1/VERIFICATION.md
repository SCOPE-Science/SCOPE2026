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

# Verification record

The standalone `verify.py` reconstructs the defining graph and checks all 4096 vertex subsets by two equivalent but separately implemented face predicates (induced degrees and forbidden triples). It verifies face vector (12,66,184,264,168,28), an acyclic 358-pair matching on 722 nonempty simplices, 2748 Hasse covering incidences, one critical zero-cell and five critical four-cells. All 48 graph automorphisms are obtained by exhaustive adjacency/nonadjacency-consistent backtracking. Signed face traces from inversions and restricted permutation cycles agree and give the full group character. The central splitting has dimensions three and two, each with squared character norm one, and the full trivial-representation multiplicity is zero. Direct mod-two simplicial boundary ranks corroborate the homology but are not substituted for the integral discrete-Morse proof.

Execute `python3 verify.py`. The full expected standard output is `verify_output.txt`, ending in `ALL_CHECKS_PASS`. No external packages, services or other scientific artifacts are required. The computation proves only the specified finite complex and full symmetry character; it does not imply integral quotient homology, equivariant homotopy equivalences or a classification for other graphs. Independent review is not performed.
