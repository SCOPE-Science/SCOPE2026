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

The standalone file `verify.py` is a Python 3 program using no dependencies beyond the standard library. Execute `python3 verify.py` to reconstruct all orientations and permitted source/sink flips of complete graphs for \(3\le n\le6\); its successful final line is `VERIFY_OK`. It compares fixed cycle and path components against character formulas for every conjugacy class, checks that each fixed cyclic component acts without orientation reversal, and enumerates component orbits under generators of both \(S_n\) and \(A_n\), checking the quotient path-length profile. It verifies \(26\) permutation cycle types in total and complete component enumerations of sizes \(4\), \(38\), \(728\), and \(26,744\). Computations are finite corroboration only; the infinite theorem relies on the proof and cited component decomposition. Neither independent external validation nor a separate independent audit has been carried out.
