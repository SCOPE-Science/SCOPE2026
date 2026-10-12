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

# Verification of the delay-spread extinction criterion

The finite checker `verify.py` uses only the Python standard library to verify the *rational input certificate*: the positive and ordered fitness bounds, triangular row-stochastic mutation matrix, absence of backward mutation, positive unequal delays, and \(NM(b-a)=21/50\). It also checks the exact strict bound \(e^{-21/50}\geq29/50>2/5\) via \(e^{-u}\geq1-u\).

Run `python3 verify.py` in the same directory. Output must be `VERIFY_OK`.

The **infinite-time theorem** is proved in RESULT.md by invariant-simplex dynamics, a differential-inequality comparison across asynchronous delays, and a scalar retarded supersolution. The checker does not certify that analysis automatically. The scalar decay rate is mathematically the unique positive root of \(\lambda=m(c-qe^{\lambda b})\), since its defining function is continuous, strictly decreasing, initially positive and eventually negative. Equality in the criterion, backward mutation into the master, and models lacking a uniform lower fitness bound are outside the claimed result. An independent audit has not been performed.
