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

# Verification record

The package contains \`check.py\` and \`checker_output.txt\`. Execute \`python3 check.py\` in this directory. The checker enumerates actual delayed recursion indices for several integer delay factors, tests exact plateau-end weighted sums and reverse-discount bounds in rational arithmetic, and independently enumerates all finite Bernoulli words to check the first two moment identities. The observed output is:

\`PLATEAU_AND_DISCOUNT_IDENTITY_PASS 108\`

\`EXACT_BERNOULLI_FINITE_MOMENT_PASS 84\`

\`INFINITE_LIMIT_THEOREMS_REQUIRE_ANALYTIC_PROOF\`

The infinite almost-sure claims, weak convergence, and limit-set descriptions are established analytically in \`RESULT.md\` by applying Birkhoff's theorem, recurrence of cylinders, the strong law, a vanishing-increment argument, and standard open-set-condition dimension theory. They are not certified by a finite enumeration. The latter dimension theorem is used as a known external theorem and not reproved in full here.

No independent mathematical audit or external replication is asserted.
