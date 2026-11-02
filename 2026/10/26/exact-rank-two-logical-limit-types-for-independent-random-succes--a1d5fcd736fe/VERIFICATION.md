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

For fixed r independent uniform Hamiltonian paths, any prescribed directed chain collection of s distinct arcs occurs with probability 1/(n)_s. Expanding each fixed mixed factorial moment of the 2*binom(r,2) signed common-adjacency counts, vertex-disjoint motifs contribute 1+O(1/n). Every overlapping connected component has more prescribed coloured arcs than vertices (two motifs on one pair require >=3 arcs; connected >=3-vertex components require >=2(v-1)>v), so its total is O(1/n); all mixed factorial moments tend to 1, identifying independent Poisson(1) limits. In the two-round EF game for loopless binary relations, the set of vertex supports of directed pair-masks is a complete invariant. With high probability all endpoints are distinct, collision motifs are separated and avoid endpoints, and there exist generic vertices. The only support changes are one missing endpoint singleton or the two merged masks from each collision sign, so the support set depends exactly on its positivity bit vector. Each bit is detectable by an existential rank-two sentence, giving precisely 2^K positive limit types and the stated weights. No extension to higher quantifier rank is inferred.

## originality

PASS

Best-of-knowledge distinct statement: combining joint signed adjacency-collision Poisson limits with the complete rank-two theory distribution for multiple independent random order successors is not shown as a corollary of the compared satisfiability and permutation-limit papers. Overlapping-motif Poisson counting and EF games are classical and not claimed as standalone novelties.

## value

PASS

The mathematical object is a natural random multiorder successor structure and the invariant is its complete bounded-quantifier logical limit. The theorem turns sparse signed adjacency coincidences into all 2^K limit-type probabilities, supplying exact probabilities of every rank-two first-order sentence. This is more than a single routine Poisson count or variable renaming: it proves a complete local-logic classification across arbitrary fixed r.

The dated certificate retains the supplied scientific assessment, sources and limitations.
