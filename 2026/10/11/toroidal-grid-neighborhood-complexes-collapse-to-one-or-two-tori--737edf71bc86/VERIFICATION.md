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

# Reproduction and verification limits

Execute `python3 verify_toroidal_neighborhoods.py` using a standard Python 3 installation, from the directory containing the extracted file. Its output is reproduced in `verification_output.txt`.

The checker builds the open neighborhoods and their downward-closed simplicial complex for \(5\leq m,n\leq8\), \(0\leq k<m\), and checks \(104\) graphs. It confirms the correct number of four-neighbor maximal tetrahedra, uniqueness of each triangle's owner, and tests each local elementary-collapse pair by enumerating all cofaces in the current complex before deletion. After the \(9,048\) collapses it checks the predicted face vector; every vertex link is a connected six-cycle, every edge has exactly two incident triangles, every component has Euler characteristic zero, and the component count matches the period parity. For the five twists of \(m=n=5\), it additionally computes mod-two simplicial boundary ranks and homology ranks.

The reproduction tests are finite and are not a proof for all periods or all lattices. The unlimited-domain proof instead uses the minimum-period hypothesis, the uniqueness of common neighbors in the square grid, elementary simplicial collapses, and the translation quotient of two diamond-triangulated Euclidean planes. There is no independent mathematical audit or formal infinite certificate.
