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

The standalone `verify.py` uses exact integer recurrences to enumerate labeled diagonal maps by image size, then counts all allowed off-diagonal output pairs. Brute-force table enumeration gives exactly 14 regular operations of 16 for two labels and 14,619 of 19,683 for three labels. Directly searching all possible two-element inner inverses independently confirms the criterion for all 16 operations. For dimensions 5, 10, 20, 40, 80, 160, and 320, exact rational probabilities converge to the stated leading asymptotic, and exact conditional image-deficiency means and variances approach the proposed constants. The most stringent numerical ratio at dimension 320 is 0.999926864225.

Command: `python3 verify.py`. Expected completion marker: `CHECK_OK`.

All finite tests were run successfully on the packaged source. They are evidence against implementation and normalization errors, not a substitute for the general proof. The proof's noncomputational inputs are Stirling's asymptotic formula and standard one- and two-dimensional lattice local central limit theorems, whose aperiodicity and nondegeneracy hypotheses are explicitly checked in the result.
