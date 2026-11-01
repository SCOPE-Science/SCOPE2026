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

Execute `python verify.py` with Python 3. The program uses only built-in modules. It enumerates all product-of-simplices cells for \(\operatorname{Hom}(C_5,K_5)\), selects canonical orbits under rotations and reflections, builds the integer quotient cellular boundary matrices with orientation signs, and checks that consecutive boundaries compose to zero. For each matrix it performs a full sequence of unimodular unit-pivot eliminations, then confirms that the remaining block vanishes or has one-dimensional rational rank and an exact nonunit Smith factor. The Smith factors fully determine integral homology; finite-prime experiments alone would not.

The output in `verification_output.txt` was produced by executing the embedded `verify.py`. The quotient chain ranks in dimensions zero through five are \(102,570,1300,1500,875,207\); the boundary ranks are \(101,469,831,668,207\). The nonunit factors are \(2\) in the second boundary, \(5\) in the fourth, and \(2\) in the fifth. A separate four-colour control reconstructs the known order-four first-homology torsion.

The code verifies exact finite incidence and integer algebra, not a general formula for every number of colours. No external or independent audit is claimed.

An independently executed finite-field calculation in `modular_crosscheck.py` obtains boundary ranks over prime 2 of \(101,468,831,668,206\), over prime 5 of \(101,469,831,667,207\), and over prime 7 of \(101,469,831,668,207\). These are consistent with precisely the two- and five-primary Smith factors. The auxiliary script and its captured results in `modular_output.txt` are included; finite-field ranks alone would not establish the complete integral result.
