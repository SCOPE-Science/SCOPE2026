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

# Finite verification and mathematical scope

Run `python3 verify_folded_cube_cut.py` from the directory containing the script. The complete recorded output is in `verification_output.txt`.

For the Clebsch graph \(d=5\), the checker constructs \(336\) nonempty faces of the Alexander dual and verifies every one of \(80\) elementary collapse pairs. It directly checks all \(65,536\) vertex subsets against the complement-of-disconnected-triples definition; the \(400\) disconnected triples give \(337\) dual faces including the empty face. The signed square-boundary ranks are \(24\) modulo \(2\) and \(25\) modulo \(3\) and \(5\). A separate element matching verifies the entire directed Hasse graph acyclic and gives Morse critical counts \((1,1,16,0)\) and an integer degree vector with gcd exactly two.

For \(d=6\), the dual contains \(1,128\) nonempty faces and \(120\) squares; all \(240\) local collapses are checked. The square boundary has ranks \(64\) modulo \(2\) and \(65\) modulo \(3\) and \(5\), agreeing with a free \(H_2\) rank \(55\) and one nontrivial \(\mathbb F_2\) torsion contribution. The \(160\) distant edges are counted directly.

The proof for all \(d\ge5\) follows from the short-word relations, elementary collapses, free cubical covering, Euler characteristic, universal coefficient theorem and Alexander duality. Tests of two values do not themselves establish an infinite theorem, and modular ranks alone do not determine integral torsion orders. The two-fold simply-connected covering supplies the exact order of the torsion.
