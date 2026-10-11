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
# Reproducibility and proof boundary

The Python 3 standard-library scripts `verify_direct.py` and `verify_cellular.py` were executed from their actual package paths. Both completed without assertion errors and printed their respective PASS lines.

`verify_direct.py` independently enumerates the ordinary independence-complex faces for \(8\le m\le12\), checks every induced dihedral permutation, computes the oriented alternating fixed-simplex trace, subtracts the connected degree-zero contribution, and compares against the claimed character. It checks exactly 100 group elements across these five polygon sizes. The observed nonempty-simplex totals are \(244,570,1285,2838,6190\).

`verify_cellular.py` separately builds the complement-cycle chord graph and all admissible polygon triples for \(8\le m\le20\), checking the character on all 364 dihedral elements. For \(8\le m\le13\), it also verifies that the triangle boundary has maximal rank over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). This checks low-degree homology in those finite cases without assuming the first script's face lists.

The infinite theorem relies on the explicit uniform equivariant poset reduction, a complete classification of the fixed cells for every dihedral symmetry, and the published nonequivariant homology-concentration theorem. Finite numerical experiments alone could not justify the claim for all \(m\ge8\). No independent external scientific audit has been performed.
