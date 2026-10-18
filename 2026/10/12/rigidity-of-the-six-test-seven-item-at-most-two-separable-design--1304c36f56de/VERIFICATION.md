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

Every valid nonzero six-bit family is visited uniquely by strictly increasing bitmask DFS with exact checks for singleton and pair-OR outcome collisions; independently implemented enumeration finds precisely 30 families of 7, and no extension of any such family to 8. All smaller family growth cannot avoid a valid size-7 prefix if 8 exists. Each family has three disjoint 2-subsets and four 3-subset parity transversals, and direct six-row permutation orbit has size 30. Its extension yields a 2-(7,3,1) block system. Independent code at /mnt/data/scope09_check_1334.py uses no SAT solvers or saved logs.

## originality

PASS

The exact optimal size appears in Chen 2010 via Fano construction and parameter obstruction, but an equality-case uniqueness/orbit enumeration was not established in the inspected main theorem. Claim is therefore narrowly the complete extremal classification and count.

## value

PASS

Exact extremizer rigidity and symmetry/orbit counts fill the equality structure of a natural seven-item optimum; it is not just another seven-item witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
