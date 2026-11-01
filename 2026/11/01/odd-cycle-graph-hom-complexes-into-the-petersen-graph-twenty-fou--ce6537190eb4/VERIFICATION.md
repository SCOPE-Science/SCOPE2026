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
# Reproducing the finite checks

Run `python3 verify.py` from the directory containing this file. No network access or third-party packages are required. The program constructs the Petersen graph directly as the disjointness graph of the two-element subsets of five points.

It checks independently the count of length-five, length-seven, and length-nine graph homomorphisms using (a) actual DFS over closed walks and (b) the exact known Petersen adjacency spectrum. It builds the graph-Hom one-skeleton by all one-coordinate recolorings, computes all connected components, and then enumerates all higher product cells by exhaustive admissible insertion. Separately, it constructs a 50-state transfer matrix of nonempty neighborhood subsets and counts all cells again in each dimension, with complete agreement.

The expected component-size spectra are 120 isolated maps in source length five; 24 components of 70 maps in length seven; and 24 components of 720 maps plus 360 isolated maps in length nine. Component-wise Euler characteristics are zero for all nontrivial components and one for the isolated maps. The program checks the action of all 120 point permutations on the 24 nontrivial components, the cyclic order-five stabilizers, and the interpretation of the 360 isolated maps as oriented based nine-cycles.

The geometric inference from component Euler characteristic to a point-or-circle homotopy type uses the external published theorem of Matsushita (Theorem 1.2 and Corollary 5.9, arXiv:2412.19144), not a numerical approximation. No independent human or external audit has been performed. Only the three stated finite source lengths are checked.
