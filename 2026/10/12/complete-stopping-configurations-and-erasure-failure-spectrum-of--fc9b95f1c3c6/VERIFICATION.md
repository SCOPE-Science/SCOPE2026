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

# Reproducible verification

From the same directory as the supplied standalone source files, run `python3 verify.py`. Compile the independent implementation with `g++ -O2 -std=c++17 verify_independent.cpp -o verifier` and run `./verifier`. The checks require no third-party libraries.

The Python program constructs the 13 dual-point coordinates and 13 check rows, exhaustively tests all 8192 possible column subsets, and compares every direct stopping-set result with the geometric nine-class description. It confirms exactly 769 stopping sets, including one empty set, with coefficients \(e_0=1\), \(e_6=78\), \(e_8=117\), \(e_9=247\), \(e_{10}=234\), \(e_{11}=78\), \(e_{12}=13\), and \(e_{13}=1\); unlisted coefficients vanish. It reconstructs all 5616 projective collineations, checks the nine orbit representatives stored in `orbits.csv`, and verifies every nonempty stopping set contains a size-six member.

Direct peeling and the independent geometric covering test agree for every erasure pattern. Exactly 3004 patterns fail, with coefficients \(B_6=78\), \(B_7=546\), \(B_8=1287\), \(B_9=715\), \(B_{10}=286\), \(B_{11}=78\), \(B_{12}=13\), and \(B_{13}=1\). The independently written C++ program separately constructs the finite plane and checks all 8192 patterns by checking row intersection sizes and explicitly iterating the peeling rule; it reproduces the two totals and every coefficient.

The geometric proof in `RESULT.md` supplies the argument for completeness, rather than extrapolating from a finite experiment. Verification does not extend the theorem to planes of other orders, other parity-check matrices, or maximum-likelihood decoding. The mathematical analysis and executable checks are not an independent mathematical audit.
