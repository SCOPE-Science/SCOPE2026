---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Rebuilt rooted subtree feasible-state induction S_v(0) nonempty, S_v(1) subset {0}, and S_v(1) empty implies S_v(0)={0,1}; contiguous child-sum interval and exclusion {0,q} prove existence and allow linear backtracking. Triangle double-hub case split (a,b)=(00,01,10,11) rules out all profiles for q>=3. For sharp q3 finite bound, independent Prüfer enumeration enumerated exactly 1,15,222,3660 distinct labeled connected unicyclic graphs for n=3,4,5,6, and brute-force checked every binary profile; each admits equilibrium. Witnesss q3 has seven vertices. Uniform q proof does not rely on small enumeration.

## originality

PASS

Klimm–Stahlberg full primary arXiv 2301.11849 establishes NP-complete unrestricted equilibrium existence for exactly picky pattern T=10^k10*; its Theorem 5.11 and related work address algorithmic complexity, not universal forest existence or sharp minimal unicyclic obstruction. General treewidth decision algorithms cannot guarantee that every input tree is a yes instance. The exact seven-vertex census may be covered by an old specialized small-game table, risk explicitly retained.

## value

PASS

The forest-vs-one-cycle existence boundary is a structural theorem with constructive linear algorithm and a sharp small obstruction for the first nontrivial picky threshold. It identifies a meaningful tractability/existence frontier even though NP-hardness on unrestricted graphs is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
