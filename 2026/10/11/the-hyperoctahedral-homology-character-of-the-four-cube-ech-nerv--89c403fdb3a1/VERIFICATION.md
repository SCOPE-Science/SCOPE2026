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
# Reproducibility of finite certificates

Execute `python3 verify.py` from the directory containing this document, using only Python's standard library. It emits the 20 signed-cycle-class trace rows and irreducible multiplicities, independent exact mod-two boundary ranks and `VERIFY_OK`. No downloaded files, internet services, other scripts, or undocumented paths are required.

The certified finite universe consists of 16 binary vertices, 32 graph edges and Čech facets, 3,944 nonempty faces and 384 signed-permutation automorphisms; it includes all faces of dimension zero through seven. The verifier recomputes all group actions on all invariant faces with orientation signs, the 20 conjugacy classes and the complete 20-character orthogonality matrix. Binary chain reduction independently gives reduced homology ranks 1 and 24 in degrees three and four. The rational nonvanishing and decomposition then follow from the negativity obstruction in the Lefschetz inner product, the Euler characteristic, and character nonnegativity, not from a floating-point approximation.

Boundaries: This is a rational representation certificate only; mod-two ranks do not establish integral torsion absence or integral representation lattices. It neither tests nor proves any analogous statement for higher-dimensional cubes. No independent audit has been performed.
