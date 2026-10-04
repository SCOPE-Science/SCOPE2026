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
# Verification

The exact domain is the binary octahedral group \(2O\), physical representation \(\rho_4\), and the six two-dimensional logical representations listed in Table 3 of arXiv:2609.26660v1.

The critical proof steps are:

1. QEC matrices are equivariant maps from physical error sectors to logical operator space.
2. A physical error sector is forced to act scalarly when it has no irreducible constituent in common with \(\operatorname{End}_0(\lambda)\).
3. Exact character decomposition gives the symmetric powers and mixed sectors through total degree \(4\).
4. Exact tensor-product decomposition gives the traceless logical-operator sectors.
5. Comparing the two lists yields the depth vector \((2,2,2,4,2,2)\).
6. The one-photon Knill–Laflamme products have total degree at most \(2\), so only the depth-\(4\) choice is symmetry-forced to satisfy all of them.

Run `python3 verify.py` in the directory containing this file. The script uses only the Python standard library and exact arithmetic in \(\mathbb Z[\sqrt2]\). It verifies character orthogonality, all decompositions used in the proof, and the final depth vector.

The script does not inspect coherent-state seeds and does not prove that an allowed intertwiner has nonzero coefficient for every seed. Accordingly, the finding does not claim impossibility of one-photon correction for the depth-\(2\) choices. It also does not establish correction of all two-photon errors for any listed representation.
