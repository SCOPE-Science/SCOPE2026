---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Partial transpose on the first qubit of the explicit 8x8 density operator factors into two zero eigenvalues, 2eta/3, (1-eta)/2, [3(1-eta) +/- sqrt(41eta^2-18eta+9)]/12 and [eta +/- sqrt(eta^2+9(1-eta)^2 s^2)]/6. Independently constructed symbolic partial transpose and exactly factored the characteristic polynomial into these four factors (2 zeros). First minus root is negative precisely eta>0, second minus root negative when s>0 and eta<1, giving stated negativity. Derivative 3(1-eta)^2 s/(2 sqrt(eta^2+9(1-eta)^2s^2)) positive away from endpoints. eta=0,1 and s=0 correctly handled; all three cuts identical by permutation symmetry.

## originality

PASS

Best-of-knowledge PASS with residual equivalence risk: Ali arXiv:1609.01031 defines the exact GHZ/W state and discusses numerical genuine multipartite negativity, while this result analytically computes ordinary bipartition cut negativity, a different entanglement monotone. Ali follow-up and Carnio framework do not supply the inspected partial-transpose spectrum. A later unindexed exact formula is possible.

## value

PASS

The distinction between freezing genuine multipartite entanglement and strict decay of bipartite cut negativity on the SAME physically motivated decoherence family is a substantive analytic boundary: exact monotonicity and positive asymptotic floor clarify what time invariance does or does not mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
