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

# Verification of the cycle-prism two-total-domatic formula

Run `python3 verify.py` using standard Python 3 in the extracted standalone file directory. The script itself constructs the exact transfer matrix, and `verification_output.txt` is the resulting ordinary output of the code executed on this package's `verify.py` file.

The independent brute-force search directly inspects all \(2^{2n}\) named colourings of the specified \(2n\)-vertex prism at each integer \(3\le n\le9\). Its counts are \(20,36,122,400,842,2116,5780\). This separately verifies the local transfer predicate and the global label convention. Matrix-power traces and the closed formula agree at all integers \(3\le n\le30\).

For the critical all-orders algebra, the script computes the \(16\)-degree characteristic polynomial by exact Faddeev–LeVerrier operations. It compares the coefficient vector to the displayed factored product and checks that the resulting polynomial annihilates the transfer matrix. The full unrestricted theorem then follows algebraically from this polynomial factorization, the spectral trace formula, and elementary trigonometric evaluations. The script does not constitute a machine-checked external formal proof; its finite tests do not stand in for the analytic implication.

Remaining scientific limitation: the result is for two total dominating classes on simple prisms \(C_n\square K_2\) only. The accessible abstract of an older work on cubic-graph two-class partitions did not permit a conclusive historical priority check. No independent audit has occurred.
