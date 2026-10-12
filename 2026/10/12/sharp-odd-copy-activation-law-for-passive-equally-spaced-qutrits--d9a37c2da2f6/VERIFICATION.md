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

# Mathematical verification

Run `python3 verify.py` with a standard Python 3 interpreter. No nonstandard modules, data files, network requests, or external binaries are necessary.

The executed command completed with `VERIFY_OK 2574 exact product-spectrum tests; 120 shell-extremum tests`. For each of 2,574 combinations of copy number \(1\le n\le9\) and ordered positive integer populations bounded by 11, the verifier enumerates all \(3^n\) computational-basis strings and compares their exact integer weights across every consecutive energy shell. The answer agrees with an independently evaluated exact-integer version of the analytic formula. The verifier also checks both discrete shell-extremum identities for \(1\le n\le120\), two explicit first-activation cases, and Gibbs examples.

The verifier is a finite consistency check. The analytic proof in `RESULT.md` establishes the claim for every \(n\ge1\) and every strictly positive ordered triple of real populations; no finite test is treated as an exhaustive proof of those quantified statements. There has been no independent external audit or independent validation.
