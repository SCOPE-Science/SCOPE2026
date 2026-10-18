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

# Verification of the wheel-matching homology character

The exact scope is one wheel with \(n\ge4\) rim vertices, \(n\equiv1,2\pmod3\), and the rational representation of its dihedral group on degree-\(\lfloor n/3\rfloor\) reduced homology. There are no unspecified normalization choices: graph rim-edge indices and spoke indices, including the reflection shifts, are defined in `RESULT.md`.

`verify_wheel.py` enumerates **all** matchings of each wheel with rim length in \(\{4,5,7,8,10,11,13,14,16,17,19,20\}\), constructs the induced permutations on graph edges, and sums the fixed oriented simplicial faces with exact integer permutation signs. The reduced empty face contributes \(-1\). In these cases the independently known one-degree homology concentration converts reduced Lefschetz values to top-character values. The executable asserts equality with the proposed formula for all \(2n\) elements of \(D_n\) and raises an error on any mismatch. Its actual run output is embedded as `verification_output.txt` and ends in `FINITE_CHARACTER_CHECK_OK`.

A second exact check, `verify_mod2.py`, separately generates all matching simplices and reduces the augmented boundary matrices over \(\mathbb F_2\). Its output `verification_mod2_output.txt` verifies reduced Betti numbers \((3,6,6,9,9,12,12)\) in degrees \((1,1,2,2,3,3,4)\) for rim lengths \(n=(4,5,7,8,10,11,13)\), with all other reduced degrees vanishing. The signed character check uses a separate enumeration and tests every group element; neither finite procedure is treated as an infinite proof.

The infinite justification is the equivariant spoke-relative long exact sequence and the exact six-periodic fixed-orbit independence polynomial; details are in the four steps of `RESULT.md`. The manuscript comparison identifies the nonequivariant wheel result as old, and the proof asserts no homotopy classification beyond it. Residual scientific scope: no integral equivariant splitting, no all-graph or all-scale claim, and no independently performed audit.
