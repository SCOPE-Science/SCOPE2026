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
# Verification and reproducibility

Run `python3 verify.py` with a standard Python installation from the directory containing this document and the checker. The checker independently builds the labeled bridge graph and computes the expected eventual bridge use and vacant-site count by recursively sampling all eligible edges with their rates. A separate two-integer tagged-endpoint recursion is compared exactly using rational arithmetic.

The executed checker reports 144 exact bridge-use comparisons, 144 exact terminal-vacancy comparisons, four independent rational benchmarks and four finite-parameter monotonicity checks. Its state spaces are finite and it does not purport to prove the all-order or scaling assertions. Those statements require the full generator, coupling, martingale and dominated-convergence arguments in RESULT.md.

The exact-clock normalization is unit rate per internal unordered edge and bridge rate \(\beta>0\). The finite-state checker uses these same rates and checks all clique orders between two and seven for four distinct positive rational bridge rates. A singular right limit as \(\beta\downarrow0\) is mathematically distinct from the exactly zero bridge-rate model.

No independent audit or validation has been performed.
