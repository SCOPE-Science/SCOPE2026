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

# Verification of the chain theorem

The associated \(\texttt{verify.py}\) uses only Python's standard library and constructs each tested relation as a set of integer pairs. It checks the original definition, not solely the proposed formula. Specifically, exhaustive filtering of all reflexive relations on \(C_n\) for \(1\le n\le4\) compares exact counts, prefix reconstruction, rank-generating coefficients, and congruence counts. A separately generated family of all prefix-code pairs checks closure, code recovery, and coefficients for \(2\le n\le5\).

The observed counts of diagonal subsemigroups for \(n=1,2,3,4,5\) were respectively \(1,4,36,576,14400\). The brute-force congruence counts for \(n=1,2,3,4\) were respectively \(1,2,4,8\). The actual test run ended with \(\texttt{VERIFY\_OK}\).

Only finite orders specified in the script were checked computationally. The uniform theorem and asymptotics depend on the explicit mathematical proof in \(\texttt{RESULT.md}\), including the mixed-product case and the convexity argument. No independent or formal certification was performed.
