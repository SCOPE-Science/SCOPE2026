---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For M_(2n), n≥3, a maximal matching has exactly one nine-letter per-rung state (V,V) or (U/L/R,U/L/R)≠(U,U). Rail transitions (a_j=R)⇔(b_j=L), together with exclusion of adjacent U symbols, encode matched rail edges consistently and prevent adjacent unmatched vertices. The boundary flip is the rail-transposition matrix S, producing P_n(z)=tr(T(z)^n S). Splitting the commuting transfer T into symmetric and antisymmetric S eigenspaces gives Q_+=1−2zt−z²t³+z³t³−z³t⁴−z⁴t⁵ and Q_−=1+zt−z²t³. Formal log determinants yield the displayed generating series with terms n=1,2 removed. The substitution t=u/w²,z=w³ cancels zero-excess terms, proving 3|F|−2n>0. Exact w^1,w^2,w^3 coefficient calculations give minimum size floor(2n/3)+1 and all three residue-class multiplicity formulas, including n=3 six. I independently constructed ladder edges, exhaustively enumerated every maximal matching for n=3..8 and compared every cardinality coefficient against a separate exact polynomial log-derivative recurrence; e.g. P_4=16z³+7z⁴. Symbolic excess identities were separately checked. The infinite claim rests on the state bijection and formal identity, not finite extrapolation.

## originality

PASS

The new content is the refinement by size and exact twist-induced zero-excess law; scalar total matching count and ordinary matching polynomial are acknowledged old. Best-of-knowledge originality follows from actual semantic published-record searches and the specifically inspected primary theorem material; unsuccessful searching alone is not proof of novelty.

## value

PASS

The Möbius ladder is a canonical cubic cyclic family. Twisted boundary conditions alter the smallest maximal matching size; the theorem supplies the complete size-profile polynomial, a sharp saturation threshold, and explicit minimum multiplicities for every size class. This is a meaningful graph-family invariant beyond ungraded counts and transfer-matrix methodology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
