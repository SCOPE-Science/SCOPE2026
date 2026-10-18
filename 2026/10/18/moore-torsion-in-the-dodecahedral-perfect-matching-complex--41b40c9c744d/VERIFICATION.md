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
# Verification procedure

The graph, simplicial complex and claim are stated in `RESULT.md`; both checkers independently generate the same 36 ten-edge perfect matchings and 30,504 faces (including the empty face).

`python3 verify_dodeca_pm.py` (Python standard library only) checks every incidence of the full face poset and constructs the ordered sequential toggle matching. It checks that all 30,503 nonempty faces admit an acyclic Hasse orientation, reports 15,238 pairs and critical counts 1 in dimension 0, 3 in dimension 2 and 23 in dimension 3. It computes the signed integral Morse boundary recursively by gradient-path elimination, then computes the gcd of all 1x1, 2x2 and 3x3 minors to obtain Smith invariants 1, 1, 2. The complete ordered 3-by-23 boundary matrix is printed in JSON and in `verify_dodeca_pm_output.json`.

`python3 crosscheck_dodeca_pm.py` independently creates graph edges and enumerates perfect matchings by set recursion and faces by combinations. It performs 14,669 genuine elementary free-face collapse pairs, leaving 1,165 simplices, with face counts by dimension (30, 231, 543, 361). Direct boundary-rank elimination on the collapsed simplicial chain complex yields ranks (29, 202, 340) over \(\mathbb F_2\) and (29, 202, 341) over \(\mathbb F_3\), \(\mathbb F_5\) and \(\mathbb F_{101}\). Hence mod-two reduced homology has ranks 1 and 21 in dimensions 2 and 3, while the odd-characteristic ranks are 0 and 20. This independently corroborates, but does not alone prove, the integral classification.

The conclusion about the homotopy type uses Forman's CW theorem and the fact that attaching maps of 3-cells to the simply connected wedge of three two-spheres are classified by integral degrees. The absence of critical one-cells and higher cells is essential. No finite test has been misinterpreted as a theorem for all graphs; the only object is \(GP(10,2)\).

# Integrity and limits

Both checkers should exit with status zero and print one serialized JSON object, byte-for-byte matching their embedded `*_output.json` reference outputs when run with compatible Python 3. The verification is computationally exhaustive for the finite input, not an independent human audit. No conclusions are asserted for larger generalized Petersen graphs or for any other fullerene.
