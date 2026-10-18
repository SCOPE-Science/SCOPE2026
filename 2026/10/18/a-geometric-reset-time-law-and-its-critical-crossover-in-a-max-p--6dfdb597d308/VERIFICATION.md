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

# Reproduction and limits

Run `python3 check_capture.py` with Python 3 and no third-party packages. It executes exact rational transformations at \(D=6/5,3/2,2,3,7\), checks the four-cycle at \(T=0\) and \(T=10^{-6}\), compares the parity formula with 1,600 rational initial-state pairs, and checks truncated sums of the independent-geometric law against its analytically derived mean. The expected final message is `EXACT_RESET_CYCLE_AND_GEOMETRIC_MOMENT_CHECK_OK 1600`.

The analytical proof, not finite enumeration, establishes the geometric distribution, exact expectation, weak critical limit, and total-variation convergence. Finite tests do not prove any of those assertions. The set of exceptional initial states is of zero Lebesgue area but not asserted empty. The theorem does not determine the distribution of first arrival to any of the four cycle phases, and it does not guarantee finite positive-parameter reset times for every initial state.
