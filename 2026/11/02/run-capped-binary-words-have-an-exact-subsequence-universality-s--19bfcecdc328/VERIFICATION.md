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
# Reproducibility and verification

Execute `python3 verify.py` with the standard library. The program independently enumerates binary hosts under caps \(h=1,\ldots,5\) through length sixteen, counts greedy completed arches, and matches all formula coefficients. A second labeled-state transfer recurrence checks the same table; for short words it additionally constructs the set of all binary target strings and performs literal greedy subsequence tests. It checks the exact two longest hosts and shortest-host multiplicities for \(k=1,\ldots,9\) at every tested cap.

Observed terminal output:

`VERIFY_OK caps=1..5 lengths=0..16 exhaustive_host_checks=249399 literal_subsequence_checks=2777 boundary_k=1..9`

The mathematical proof does not depend on floating-point calculations. Exhaustive enumeration is finite evidence only; the all-parameter count and limit theorem are established by the symbolic state equations and aperiodic dominant-pole argument in the result. No external or independent scientific audit is recorded.
