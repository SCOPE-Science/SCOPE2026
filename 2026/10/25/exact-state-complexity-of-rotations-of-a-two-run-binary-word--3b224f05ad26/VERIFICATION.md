---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For a,b>=1, every mixed proper circular factor of 0^a1^b identifies its rotation via the oriented run boundary; pure-prefix sets and pure-suffix singleton completions must be separated, with the two run-boundary overlaps subtracted. Reconstructing this disjoint Myhill–Nerode quotient count gives q_0=q_n=1, q_d=2 min(a,b,d,n-d) for 0<d<n, and one dead quotient, so sc=2ab+3. The depth sum equals ab and balancing a+b maximizes ab. Independently recomputed all right-language quotients for each of 81 ordered pairs a,b=1..9, including a=b=1 and other boundary cases, and every profile matched. This finite confirmation is distinct from the all-a,b combinatorial proof. Git tree 9ca006a29e997775aa5bcb975803717467c0ab90 was independently reconstructed from the seven real blob IDs.

## originality

PASS

Best-of-knowledge PASS for the exact two-run singleton profile, excluding the already-known cyclic-shift operation, state-complexity theory and greedy universal-cycle constructions. Inspected primary statements and published Resultary records do not logically imply the exact formula. Historical priority is not certified.

## value

PASS

The binary two-run necklace is a canonical restricted cyclic-closure family; the full quotient profile and exact quadratic recognition blow-up relative to a single n-letter word are natural, useful finite-language state-complexity invariants. The sharp fixed-length composition maximizing recognition cost is structural information, not an arbitrary numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
