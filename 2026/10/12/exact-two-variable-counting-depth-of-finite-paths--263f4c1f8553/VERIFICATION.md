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

# Verification

The proof has two independently checkable parts.

1. **Structural reduction.** After one color-refinement round, any same-order rival of \(P_n\) that remains indistinguishable must have degree multiset \(1^2 2^{n-2}\). Hence it is exactly one path component \(P_m\) plus cycle components. Cycles stay monochromatic under refinement, so all delaying behavior is controlled by the length \(m\) of the path component.

2. **Round count.** Endpoint information propagates one layer per refinement round. The two graphs have equal color histograms through round \(\lfloor m/2\rfloor\), and the short path's endpoint waves meet in round \(\lfloor m/2\rfloor+1\), producing the first mismatch. Since a nonisomorphic rival needs at least three vertices in a cycle, \(m\le n-3\), yielding the maximum first-separation round \(\lfloor(n-1)/2\rfloor\).

The included `artifacts/verify.py` implements joint canonical color refinement directly and enumerates every partition of the cycle remainder for every order \(5\le n\le30\). It verifies the per-rival formula and the global maximum over 6,699 decompositions. Running it with Python 3 produces:

`VERIFY_OK rival_decompositions=6699 n_range=5..30 max_cases=26 formula=D2#(P_n)=1,2,2,2 then floor((n+1)/2)`

The verifier is finite evidence only; correctness for all \(n\) comes from the structural proof.
