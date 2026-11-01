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

Run `python oct.py`, `python characters.py`, `python verify_equiv.py`, and `python independent_trace.py` with NumPy installed. The programs require only the companion `octchars.json`, which `characters.py` also reproduces, and their own included source files. Expected exact records appear in the companion `.out` outputs.

`oct.py` enumerates the complete reduced weight-three chain basis of sizes \((364,1404,1620,540)\), checks all boundary compositions, and verifies differential ranks \((363,1033,540)\) modulo \(32003\). The first/last ranks are rationally maximal by connectedness and source dimension, while the Ko–Park planar three-connected theorem independently fixes first homology at rank eight, making the middle bound sharp. Direct mod-prime ranks alone would not prove rational ranks.

`characters.py` enumerates the complete \(48\)-element octahedral automorphism group, calculates all ten signed-cycle Euler characters via the local-cycle polynomial, and uses exact integer character inner products to determine the two graded representations. `verify_equiv.py` computes the induced action on actual first-homology quotient cycles over \(\mathbb F_{32003}\) for all \(48\) automorphisms and agrees with the geometric first-homology character. `independent_trace.py` explicitly enumerates \(9704\) weight-three full-chain states and independently verifies every supertrace, rather than merely reusing the closed form.

All four recorded program runs passed. The calculations leave open integral torsion and depend for topological interpretation on the published graph-homology chain-model theorem. This is not an independent mathematical audit.
