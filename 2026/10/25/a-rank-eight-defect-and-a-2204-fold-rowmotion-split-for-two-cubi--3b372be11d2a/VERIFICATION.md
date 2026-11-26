---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

An ideal is uniquely a vertex subset U and any subset of its induced edges, giving H=F(t,1+t). Equal cubic triangle-free counts agree through triples, and m(U)=12-3|V\U|+m(V\U) handles sizes at least five. For four-sets, the independent-set counts are 2 and 0, and the induced squares number 6 and 4. In the Wagner graph a square must use two disjoint opposite chords and parallel cycle edges (0 or 1 chord cannot close in four steps, three or four cannot lie in a four-cycle because the chords are a matching); the cube squares are its faces. Counting all four-sets and occurrences of single edges and pairs of edges gives the three common equations for the intervening coefficients, hence difference (2,-8,12,-8,2). Independently ran an exhaustive Python enumeration, different from the supplied checker: scan all 2^20 subsets for each graph, dropping any that include an edge but omit an endpoint; map each valid I to P minus the upset of max(I), which is inverse rowmotion because maximal elements of the generated ideal are exactly its complement-minimal generators. Verify the inverse images give exactly the ideal set; traverse the cycles and count ranks directly. This reproduced both complete histograms in RESULT.md, all ideal/orbit/max-length counts and both automorphism orders (also independently enumerated over 8! permutations). The computed LCMs are 110880 and 244379520, ratio 2204, and the directly enumerated rank defect is (8,+2).

## originality

PASS

The distinct contribution is the induced-edge and rank defect paired with the full classical rowmotion cycle contrast on these two precise labelled incidence posets. The strongest same-object archive hit studies a different dynamics; closest same-dynamics sources do not include the two posets. No exact table overlap was found by the bounded checks.

## value

PASS

The cube and Wagner graph are standard, comparably small connected vertex-transitive cubic graphs; the shared parameters force almost all of their incidence-ideal rank data to match. The contrast between a single two-ideal discrepancy and a 2204-fold order change is a concrete test of how little those near-equal static statistics constrain the order of the dynamics. The exact census is a usable benchmark for methods computing classical rowmotion on graph incidence posets, where full rather than sampled profiles matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
