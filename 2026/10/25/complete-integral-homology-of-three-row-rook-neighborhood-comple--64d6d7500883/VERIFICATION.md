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
# Verification of the three-row rook homology theorem

The proof uses a complete three-subcomplex simplicial cover and its **integral** Mayer–Vietoris spectral sequence. The nonstandard finite combinatorial facts are the nerve of each row-centered cover, the crown-plus-isolates structure of each pair intersection, and the absence of edges in the triple intersection. The signed projection of the degree-zero Čech boundary onto the isolated pair components is a unimodular permutation matrix. These facts prove the theorem for every integer \(n\ge5\) without assuming that binary computations establish integral homology.

Run `python verify_rook3n.py` using only the Python standard library. The program enumerates the complete open-neighborhood simplicial complex for \(n=5,6,7,8\), checks all stated facet intersections, computes every reduced binary boundary rank, and explicitly reconstructs the signed isolated-component projection. The corresponding face vectors and nonzero binary Betti ranks are in `verification_output.txt`, ending with `ROOK3N_MV_FINITE_CHECKS_OK`.

The finite computations do **not** verify the nerve theorem, Mayer–Vietoris convergence or the infinite quantifier by enumeration. The proof of split integrality is mathematical: in every parameter, each triple vertex has a unique isolated-component coordinate with coefficient \(\pm1\), so the projection is an integral signed permutation matrix. No independent audit is claimed.
