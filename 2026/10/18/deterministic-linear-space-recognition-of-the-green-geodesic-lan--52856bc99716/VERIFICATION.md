---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Munn coordinates (T,t) encode the prefix-visited subtree. R fixes rooted T, L fixes its translation to the terminal-rooted copy, and D fixes the unrooted edge-labeled tree up to group left translation; free terminal/start vertices correspond to endpoints to optimize. Any tree walk from s to u covering all e edges has length ≥2e−dist(s,u): each on-path edge is required odd and ≥1 crossing, each off-path edge even and ≥2; branch excursions attain equality. Thus optimizing one/both endpoints gives eccentricities/diameter and all Green shortest lengths, including empty word. For O(n) work space, re-free-reduce individual prefixes as needed, keeping at most two O(n)-length stacks and O(log n) counters for pairwise equality/distance and uniqueness scans; polynomial repeated scans avoid storing O(n²) prefix strings. Complement uses the same deterministic total decider. An independent exhaustive rank-one length≤9 and rank-two length≤5 short-word census (1023 and 1365 words) grouped true Munn Green invariants and matched all four formulas; not an unbounded proof.

## originality

PASS

Best-of-knowledge PASS despite elementary tree-tour ingredients. Bodart–Carvalho–Monteiro 2026 define these languages, obtain geometric descriptions and prove R/L/D neither context-free nor co-context-free in rank≥2, while Section 11 publicly asks whether they are context-sensitive (explicitly quoted in the discoverable open-question record). Their publication therefore does not claim the new linear-space conclusion in its accessible description. Growth work on free inverse monoids counts objects rather than testing shortest Green-class representatives. A prior implicit algorithm or unindexed result could nevertheless imply deterministic linear space; full 2026 manuscript was not read here.

## value

PASS

The bound answers a concrete published formal-language classification question for three natural Green relations with a uniform algorithm, also establishing context-sensitive complements. It is independently worthwhile even though the tree-walk lemma is standard and indexed-language status remains open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
