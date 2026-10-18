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

# Reproducibility

Run `python3 verify_paley17.py` with Python 3; no third-party packages or external data are required. It enumerates the \(3468\) faces from seventeen eight-element open neighborhoods, constructs \(1711\) discrete-Morse pairs, checks all directed incidences are acyclic by a full topological sort, computes the signed \(5\)-by-\(40\) Morse boundary, and checks the determinant and prime-field rank certificates for integral \(\mathbb Z/3\) torsion and \(35\) free third-homology generators.

Next it computes a mod-\(3\) cycle/cocycle pairing for the one-dimensional second-homology group, and verifies that all \(136\) affine maps induce scalar \(+1\). It independently enumerates all signed simplicial cell traces and verifies the displayed four-case rational character and its equality to the \(2W\oplus E\) character on all \(136\) elements.

The expected final line is `All exact finite checks passed.` The check is exhaustive for this explicitly finite complex; no integral third-homology group-ring lattice identification or analogous computation for other Paley graphs is supplied. The mathematical argument and assumptions are in `RESULT.md`.
