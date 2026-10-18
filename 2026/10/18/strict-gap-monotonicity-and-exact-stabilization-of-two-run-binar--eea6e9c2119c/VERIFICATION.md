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

# Verification of the mathematical claim

Run `python3 verify.py` alongside this file, using only Python 3 and its standard library. The exact arithmetic checker computes the density from the two-state carry process using `fractions.Fraction`, then compares each increment against the displayed finite-convolution formula for all \(1\le r,s\le9\) and all gaps up to \(r+s+3\). It makes 972 transition comparisons, including positivity and stabilization. Independently it enumerates every low-bit residue of the shift for 45 smaller triples \(1\le r,s\le3\), exactly averaging over the geometric high-bit carry tail. Four illustrative fractions are checked explicitly.

Observed output: `VERIFY_OK: exact increment identities 972 ; independent residue-class enumerations 45`.

The proof of the infinite theorem is in RESULT.md, Sections 3–4. The finite verification does not certify originality and is not substituted for the universal proof. No independent audit has been performed.
