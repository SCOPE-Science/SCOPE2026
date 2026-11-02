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

# Verification record

The package's `verify.py` is a standalone Python 3 script with no third-party dependencies. Run `python3 verify.py` from a directory containing that file. Its recorded successful finite output is:

`VERIFY_OK N=30000 least_prime_memberships=29999 rough_cutoffs=9 exact_moments=PASS exact_inclusion_exclusion=PASS nice_count=15574 finite_only=YES`

The script recomputes \(\omega(n)\), smallest prime factors, truncated prime-factor counts, the exact first and second moment identities, and inclusion–exclusion counts for nine prime thresholds. For every \(2\le n\le30000\) it checks the algebraic equivalence between removing the smallest prime and updating the distinct-prime-factor count. It does **not** enumerate residue-assignment witnesses, prove Mertens' theorem, or establish an infinite asymptotic by finite experiments.

The infinite proof in `RESULT.md` independently details: the concentration estimate from divisibility moments, both threshold implications of the published niceness characterization, the uniform small-cutoff inclusion–exclusion estimate, and three cases for the limiting tail. All uses of external theorems are named. Publication priority and independent mathematical audit remain open.
