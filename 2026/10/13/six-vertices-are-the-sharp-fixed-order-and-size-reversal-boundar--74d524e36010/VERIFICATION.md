---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Regenerated all graph relabeling orbits from edge masks and independently found 1, 2, 6, 21 connected classes at orders 2–5. Compared all 32 same-(n,m) pairs of distinct classes, using exact matrix characteristic polynomials and joint real-root isolation, including exact ties. In contrast to the supplied proof, the replay formed the full directed-edge Hashimoto matrix rather than the Ihara–Bass auxiliary polynomial. Perron–Frobenius makes the largest real root the spectral radius for each nonnegative matrix, including the nilpotent tree case. For the specified connected six-vertex seven-edge witnesses, the adjacency factors match the proof and the largest roots lie respectively in (2.709275359436922, 2.709275359436923) and (2.705586727307843, 2.705586727307844). For the actual Hashimoto matrices the largest roots are the positive roots of x^3−3 and x^3−x−2, with disjoint exact intervals in the opposite order. Thus the lower bound and witness hold. Replay: python /workspace/replay_frozen_graphs.py 2 (SymPy 1.14.0); output /workspace/replay_2.log.

## originality

PASS

The evidence supports a distinct exact fixed-(n,m) strict-order reversal boundary, not novelty of the spectral quantities, threshold surrogates, or qualitative observation that their optima can differ. The closest checked catalogue and primary-literature statements do not supply or imply the two opposite strict inequalities in a common (n,m) layer together with the lower-order exclusion.

## value

PASS

Comparing ordinary walk growth with nonbacktracking walk growth at fixed vertex and edge counts removes changes in average degree as an explanation. The two small networks provide a sharp diagnostic: adjacency is sensitive to the placement of the pendant edges and hub while the nonbacktracking radius sees the cyclic core. This is an informative controlled benchmark for the two spectral proxies, not a claim that either inverse is an exact threshold for every spreading process.

The dated certificate retains the supplied scientific assessment, sources and limitations.
