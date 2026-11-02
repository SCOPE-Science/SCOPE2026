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

# Verification of the cycle optimal-function support census

`verify.py` requires only a standard Python 3 installation and no external data files. Run `python3 verify.py` from the same directory. It evaluates the original constraints \(f(i-1)+f(i+1)\ge k\) over all labelled assignments in the stated small ranges; this checks both the minimum and each support-count coefficient. Separately a cyclic dynamic program over consecutive original labels independently counts minimum-weight solutions without employing the step-two-chain proof reduction.

Observed output when the verifier was executed:

```
ORIGINAL_NEIGHBORHOOD_EXHAUSTIVE_OK 18
INDEPENDENT_CYCLIC_DYNAMIC_PROGRAM_OK 112
VERIFY_OK
```

The exhaustive loop covers \(3\le n\le8\) and \(1\le k\le3\), testing the support formula for \(k\ge2\). The independent dynamic-programming comparison covers \(3\le n\le30\) and \(1\le k\le4\); values with \(k=1\) are boundary consistency checks and are not claimed new. The infinite theorem is established by the step-two constraint decomposition and the cyclic-chain lemma in `RESULT.md`; finite tests are supplemental. Computation does not establish historical priority. No external independent audit has been performed.
