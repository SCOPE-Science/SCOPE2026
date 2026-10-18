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

# Reproducible checks

Run `python3 verify_squared_path_reversal.py` in the directory containing the verifier. Only the Python standard library is required. The program independently enumerates facets from disconnected induced \(k\)-sets in the squared path; enumerates every face by inclusion; computes the action of vertex reversal on each oriented face with exact signs; and compares the resulting alternating Lefschetz character to the proposed all-parameter formula. It also enumerates symmetric connected \(k\)-sets without using the proposed composition-count formula.

Actual execution passed all **45** parameter pairs with \(5\le n\le13\), \(2\le k\le n-3\). For all **21** such pairs with \(n\le10\), separate exact \(\mathbb F_2\)-boundary Gaussian elimination computed every reduced Betti number and agreed with the known integral homology ranks. Five explicit rational \(C_2\) eigenspace examples are printed. The exact captured stdout is in `verification_output.txt`; regenerate it by redirecting the script's stdout.

Scientific bounds: The finite verifier checks, but cannot establish, the symbolic infinite-family theorem. The proof's general steps use the published full complementary-face classification, known shellability and the proved centered-gap enumeration. Computation over \(\mathbb F_2\) is not by itself a certificate of integral torsion-freeness or of rational character formulas, which come from the cited topology and signed rational chain argument. Neither finite computation nor literature-search failure certifies global originality.
