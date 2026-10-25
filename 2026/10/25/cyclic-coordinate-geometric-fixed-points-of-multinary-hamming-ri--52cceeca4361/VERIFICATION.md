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

# Reproducible verification

Run `python3 verify.py` with Python 3 and no third-party packages. It enumerates all three-letter words for alphabet sizes 2 through 6, computes cyclic orbits directly from coordinate rotation, discards orbits that fail the original Hamming-distance Rips-simplex test, and independently computes raw orbit compatibilities from every underlying word pair. It compares the complete raw adjacency to the claimed constant/two-equal orbit-block formulas, enumerates their simplices, and computes reduced mod-two homology from boundary matrices.

At sizes 2, 3, 4, 5 and 6 it finds respectively 1, 4, 9, 16 and 25 reduced first-homology classes, with no others. For every letter permutation at sizes 2 through 5 (152 group elements total) it computes a signed simplicial reduced Lefschetz trace and checks that it equals the negative of the stated first-homology character. The signed trace computation is independent of the cellular multigraph representation formula.

The size-two run is a boundary control; the theorem's new domain begins at three. These are complete finite checks for the listed alphabet sizes, not exhaustive verification of every alphabet size. The infinite-family result follows from the explicit orbit and chain proof in RESULT.md. No independent scientific audit or formal proof certification is claimed.
