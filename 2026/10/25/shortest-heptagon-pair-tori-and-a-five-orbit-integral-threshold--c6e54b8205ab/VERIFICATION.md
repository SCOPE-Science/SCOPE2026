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

# Computational verification

Run `python verify_mcgee.py` with `requirements.txt` in the same directory. An actual replay was performed using Python 3.13.5, NumPy 2.3.5, NetworkX 3.6.1, and SymPy 1.14.0. The executable reconstructs all chains and certificates rather than reading a precomputed log.

Checks include cubicity, biconnectivity, absence of cycles of lengths \(3\)–\(6\), full seven-cycle and disjoint-pair enumeration, cellular boundary composition, zero boundaries of all \(152\) torus chains, the rank-\(504\) modular certificate, an exact signed integral \(54\)-by-\(54\) determinant equal to \(+1\), all \(32\) graph automorphisms and seven torus orbits, all combinations of up to four orbits over \(\mathbb F_2\), and Smith normal forms of the asserted three- and five-orbit lattices.

The observed success marker was `VERIFY_OK_MCGEE_SHORTEST_CYCLE_TORI_FIVE_ORBIT_THRESHOLD`. The computed Smith counts were \(1^{51},2,2,4\) for orbits \(\{1,3,4\}\) and \(1^{54}\) for \(\{0,1,2,3,5\}\). The maximal rank modulo two from any four orbits was \(53\).

The finite checks are exhaustive for the explicitly defined graph and specified orbit family, not a statement about other graphs. The topological interpretation relies on the published equivariant deformation-retraction theorem for two-point graph configurations. Independent audit remains unperformed.
