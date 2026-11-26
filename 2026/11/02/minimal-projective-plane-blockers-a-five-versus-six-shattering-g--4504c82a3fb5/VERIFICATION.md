---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The class consists of all inclusion-minimal hitting sets, including the lines. Hitting every line and giving each chosen point a line it hits alone are necessary and sufficient. A separately written checker reconstructs PG(2,3) from an affine plane with points at infinity, tests all 8192 subsets, and obtains 13 four-point lines and 234 six-point open-side triangles and no other blockers. For support sizes 3,4,5,6 it reproduces respectively {8:286}, {15:13,16:702}, {29:117,31:468,32:702}, and {56:468,57:78,60:936,61:234}. It compares the actual five-support sets, not just counts, with all triangle deletions and checks multiplicity two. No six-support is shattered, excluding all larger ones by restriction. Reconstructing incidence separately for certificate.json and following positive and negative branches verified all 63 internal nodes and 64 distinct terminal witnesses; a separate exact version-space recurrence also gave depth 6. No depth-seven tree is possible: along an all-positive path every query must be different (a repeated query has an inconsistent sibling), and maximum concept size is six. In the control PG(2,2) all seven blockers are lines and all 21 pairs are shattered; seven concepts rule out depth or cardinality three. Minimality factors over disjoint components. For VC, restriction to each component must shatter there, and component witnesses can be combined independently. For Littlestone, concatenate trees for the lower bound; for the upper bound, a query only splits one component and at least one child decreases that component rank for every nontrivial split. Iteration gives the sum bound. The disjoint unions are linear, four-uniform, four-regular and point-transitive by the projectivity action and component permutations. Independent finite replay: /workspace/branches/a13dbeae-9d2b-41bc-9a59-c82f6e10a7d4/check_record2.py (pass the frozen certificate.json path; see adjoining check_record2.out). Frozen scripts were read, not executed.

## originality

PASS

The supported distinct claim is the query-learning result for the entire minimal-blocker class, especially the exact trace spectra, characterization of which supports are shattered by blockers, and adaptive depth six versus static dimension five. The underlying small-plane blocker geometry is prior work. Moreover, a distinct earlier indexed exchange-graph record directly implies the two-completion property and the count of candidate five-sets, and a separate two-line-union theorem shatters precisely the same five-sets for a different concept class. Neither establishes their shattering by minimal blockers, the trace spectra, or the adaptive rank. The amplification is a direct product consequence of the new base gap, not a separate novel dimension-additivity theorem.

## value

PASS

Minimal transversals of a classical symmetric incidence structure give a natural test of how static and adaptive membership-query capacities differ. The trace spectra answer more than just the VC maximum, and the verifiable depth-six tree establishes a strict gap not implied by the geometric count or exchange graph. Repeating the plane makes the gap unbounded within a point-transitive linear uniform regular class; this construction makes no connected amplification claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
