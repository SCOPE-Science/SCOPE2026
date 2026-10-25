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

Run `python3 verify.py` using Python 3.9 or later; no dependencies are required. The script enumerates every edge and 2-cell of the unordered deleted-product cubical complex for n=4 through 8, constructs signed boundary matrices, checks primitive four-cycle chains, obtains the sharp 24-square support for the generated minimizers, and reports modular ranks for primes 2, 3 and 5. Rank at prime 2 is intentionally one less than the characteristic-odd boundary rank; no false integral-torsion conclusion is drawn from modular calculations. The exact, all-parameter integral kernel and lattice-generation arguments are mathematical proofs in RESULT.md and are not replaced by these finite checks. Output is recorded in verify_output.txt.

No independent audit was performed.

Supplementary exact integer-check: install the listed SymPy dependency with `python3 -m pip install -r requirements.txt`, then run `python3 saturation_check.py`. Smith factors for the primitive alternating-four-cycle generator matrices are all unity for n=4,5,6; see saturation_output.txt. Integer saturation for every n is instead proved by the elimination induction in RESULT.md.
