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

# Verification and scope

The standalone `VERIFY.py` file contains no dependencies outside the Python standard library. Run it with `python VERIFY.py` in the same directory. The actual execution returned `VERIFICATION_OK 529 exact-rational assertions`.

The program enumerates each open/closed bond pattern, constructs all resulting connected components, and for a uniformly chosen vertex accumulates a source-weighted final outbreak-size distribution. All probabilities use exact rational arithmetic. It checks the closed threshold formula for path lengths through ten, verifies the expected-size pair-connectivity formula, and independently searches all one-vaccine positions for \(M\in\{2,\ldots,10\}\), thresholds through \(M+2\), and three rational transmission probabilities. It verifies the strict two-infection risk gap and the five-vertex numerical fractions.

The mathematical proof, not finite enumeration, establishes all values of \(n\), \(s\) and real \(p\in(0,1)\). The test does not verify independent publication priority, finite-size external data, transmission mechanisms outside Reed–Frost, or results for arbitrary graphs. No independent audit is claimed.
