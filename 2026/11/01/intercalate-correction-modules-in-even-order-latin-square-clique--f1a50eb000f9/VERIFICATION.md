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

# Reproduction

Run `python3 verify.py`. The script uses only the Python standard library and performs genuine finite graph and boundary computations. For each of four abelian groups it enumerates adjacency, graph triangles and tetrahedra, checks the line-plus-rainbow-plus-intercalate face model, calculates every signed simplicial Lefschetz number, verifies all Fourier multiplicities, and checks mod-two second and third boundary ranks. It prints `ALL_CHECKS_PASS` if every check succeeds.

The four cases have orders \(6,8,8,8\), respective second Betti numbers \(116,327,295,231\), and invariant dimensions \(4,6,4,0\). These do not exhaust all finite abelian groups. The infinite result relies on the displayed general proof and on the all-field homology theorem of Cioabă and Mim (arXiv:2606.27328v1, Theorem 3.12). All checks concern ordinary homology and symmetry; no independent validation was performed.
