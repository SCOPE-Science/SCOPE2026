---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

An interleaving is exactly one length-eight binary word with four A and four B, so there are 70 distinct concept masks and the 16 available queries compare the i-th A and j-th B. Independent complete exhaustive Python computation generated all 70 masks and evaluated every query and the full memoized minimax shattering recurrence (Ldim C = 1+max_q min(Ldim C0,Ldim C1) where both children nonempty). It obtained Ldim on square profiles n=1,2,3,4 equal to 1,2,4,5; all four diagonal queries 4x4 split 35/35. The package provides an exact finite integer-exhaustion certificate: only those four roots could support 2^5=32 witnesses per child, endpoints fail because S_{3,4} best first split is 15/20, and for the middle q22 a unique 17/18 split branches into 9/9 children lacking any 4/4 split. A constructive first-elements deletion argument supplies depth5. The finite exhaustion here is exhaustive for the EXACT finite 70-concept domain, not an extrapolation to larger chains.

## originality

PASS

Best-of-knowledge first symmetric four-by-four online shattering entropy deficit for this ordered-interleaving concept class. Previously studied worst-case number of MERGE comparisons is a different minimax quantity; general Littlestone theory does not state the exact 70-concept calculation. Earlier exact tables or a general poset-order-ideal Ldim result remain a risk.

## value

PASS

The two-ordered-chain interleaving lattice is a canonical finite concept family. The first balanced symmetric failure of the cardinality ceiling despite all four perfectly balanced root comparisons, requiring a nested obstruction, is a motivated exact online-learning invariant not reducible to a toy one-step count. An exact complete finite case has value without a general asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
