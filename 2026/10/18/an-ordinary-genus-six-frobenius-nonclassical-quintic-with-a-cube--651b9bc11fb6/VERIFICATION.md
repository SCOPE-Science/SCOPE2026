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
Exact reproducibility instructions and scientific limits.

From the containing directory, compile `checks/count.cpp` with `g++ -O2 -std=c++17` and run it. It counts \(N_1\) through \(N_7\) by rank reduction of the \(\mathbf F_2\)-linearized affine equation, plus exact infinity roots. Expected values: 5, 35, 65, 395, 1025, 3395, 16385. It verifies its finite-field representation by locating a primitive multiplicative generator.

Independently compile and run `checks/direct.cpp`. It enumerates all affine pairs over extensions of degrees one through six by direct polynomial-basis field arithmetic and explicitly counts infinity roots. Expected values: 5, 35, 65, 395, 1025, 3395. This exhaustive independent calculation uses a different root-counting method. `python checks/verify.py` checks the complete algebraic singularity-candidate list, reconstructs the degree-twelve Weil numerator from the six counts, checks irreducibility of the quartic factor and maximal \(2\)-rank, and confirms the seventh-extension prediction.

The geometric singularity reduction is justified analytically in `RESULT.md`; the finite list is complete because all cube roots of unity already lie in \(\mathbf F_4\). The functional equation is used only after geometric smoothness and genus six are proved. The isogeny claims invoke the standard Honda–Tate and Tate theorems, not a computational test for isomorphism of polarized abelian varieties. The priority comparison is literature-based, not a uniqueness certification.
