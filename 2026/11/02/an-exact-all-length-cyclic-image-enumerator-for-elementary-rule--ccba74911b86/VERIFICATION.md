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

# Reproducible checks and limits

Run `python3 verify_rule73.py` with a standard Python 3 interpreter. No dependencies, external dataset, network connection, nonstandard arithmetic packages, or third-party files are required. The program regenerates the four-state Boolean matrices from the decimal local rule code `73`, enumerates all 735 reachable relation matrices and their two outgoing transitions, and constructs the degree-34 denominator as a product of six integer polynomials. It checks all 735 components of the all-length recurrence certificate
\[
\sum_{j=0}^{34}q_j T^{40-j}h=0,
\]
where \(T\), \(h\), and the coefficients \(q_j\) are defined in `RESULT.md`. It also generates and compares forty exact formal-power-series coefficients, checks the recurrence to degree 100 as a diagnostic, and directly enumerates every input ring through length fourteen. A successful run prints `VERIFY_OK`.

These comparisons are not claimed to establish an all-length theorem merely by extrapolation: the infinite conclusion uses the exact finite-dimensional vector identity and common-denominator argument in `RESULT.md`. The mathematical conclusion is limited to counts of distinct one-step images on binary synchronous periodic rings. No multi-step inverse reachability, floating-point root-isolation or historical-priority certification is included.
