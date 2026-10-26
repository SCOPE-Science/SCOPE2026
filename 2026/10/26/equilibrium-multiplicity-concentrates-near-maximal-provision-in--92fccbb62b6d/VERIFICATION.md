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

The equilibrium characterization was reconstructed from the stated payoffs. The exact count was derived by inclusion-exclusion over nonbuyers receiving no nomination. The included Python script was executed from its saved package path and compared the formula with direct enumeration for every \(2\le n\le5\) and \(1\le k<n\). These finite checks do not prove the asymptotic claim. The asymptotic proof uses a union-bound lower estimate at \(q=\lfloor n/\log n\rfloor\), the upper bound \(N_{n,k}(q)\le\binom nq\binom qk^{n-q}\), and strict concavity of the associated logarithmic envelope. No independent audit or external certification has been performed.
