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

# Exact verification of the translation character

Run the supplied `verify_latin_translation.py` with a standard Python 3 interpreter. The verifier independently forms each graph from coordinate equality rules, enumerates maximal cliques via a Bron–Kerbosch recursion, checks the complete line-plus-mixed-triangle description, reconstructs every nonempty face, and sums signed fixed-simplex contributions to every translation's Lefschetz number. A finite discrete Fourier transform checks the resulting multiplicities and dimension.

The program was executed on \(n=3,5,7\) and ended in `VERIFY_OK_CYCLIC_LATIN_CLIQUE_TRANSLATION_CHARACTER`. Its standard-output transcript is included as `verification_output.txt`. For \(n=3\), the face vector is \((9,27,27)\); for \(n=5\), \((25,150,250,75,15)\); for \(n=7\), \((49,441,1029,735,441,147,21)\). All translation traces match the exact formula. These experiments establish only the tested cases: the separate mathematical proof classifies arbitrary odd integer orders, including odd composite \(n\).

The checker computes finite Fourier transforms with floating-point roots, testing discrepancies below \(10^{-7}\); the character multiplicity formula itself follows rigorously from exact finite-group orthogonality, independent of this numerical check.

Self-review was passed; no independent audit or independent validation was performed.
