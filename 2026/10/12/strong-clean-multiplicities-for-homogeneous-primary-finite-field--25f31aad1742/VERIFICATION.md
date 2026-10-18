---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Commuting E and U=A-E equivalent to E in centralizer of A. Primary decomposition is canonical; for f=t nilpotent A forces ker E=0, and f=t-1 nilpotent A-I forces im E=0. Neutral factors make both A and A-I units on every direct summand so every centralizing idempotent is valid. For homogeneous blocks centralizer M_k(R), a finite chain ring with residue field F_Q, rank-r idempotents form GL_k(R)/(GL_r(R)xGL_(k-r)(R)); |GL_j(R)|=Q^((m-1)j^2)|GL_j(F_Q)|. This gives exponent (2m-1)r(k-r) exactly. Two valid choices on any neutral primary prove uniqueness criterion; condition A-A^2 nilpotent equivalent to only 0,1 primary factors. Independent direct local ring idempotent enumeration yields 26 in M2(F2[u]/u²) and 110 in M2(F3[u]/u²), matching H. Finite tests supplement, not replace proof.

## originality

PASS

Prior sources characterize existence of strongly clean decompositions and ring-wide properties; centralizer/module and idempotent counting tools are classical and explicitly not individually claimed as original. No inspected primary result tabulates the number of decompositions for each fixed homogeneous-primary finite-field matrix, nor the exact nilpotent-thickness multiplier as a strongly clean multiplicity. Risk of an equivalent old idempotent count under modular-lattice wording remains.

## value

PASS

A fixed matrix’s number of strongly clean decompositions is a natural exact invariant, and homogeneous primary blocks are canonical nonsemisimple rational-canonical strata. The formula quantifies effect of nilpotent thickness on a qualitative existence theory, with a sharp unrestricted elementwise uniqueness characterization. The necessary orbit-stabilizer algebra is elementary but the end-to-end exact formula covers arbitrary degrees, ranks and lengths and is practically usable without ad hoc enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
