---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For Cr_n=K_{n,n} minus a perfect matching, the complement I of a double outer-independent dominating set is independent. It is either contained in one bipartition side or exactly the unmatched pair {a_i,b_i}. In a one-sided complement case the selected opposite side is complete, and at least two vertices must also be selected on the first side (one cannot defend its unmatched b_i); every choice of two suffices. Thus |D|≥n+2, and there are 2*C(n,2) such equality sets. A two-sided independent complement yields |D|=2n−2 and is feasible for n≥3. Comparing gives γ_d^{oi}=min(n+2,2n−2)=n+2 for n≥4; n=4 has four additional optimum unmatched-pair complements (total 16), n≥5 has precisely n(n−1). A separately written direct all-subsets checker verifies the complete minimizer set for n=4,5,6. This finite check is corroboration, not the all-n argument.

## originality

PASS

The introducing result establishes the complete bipartite value and isolated-edge perturbation bound, and later work establishes a broader parameter equivalence on minimum-degree≥2 graphs; neither implies the simultaneous perfect-matching deletion value or classifies all minimum sets, including the n=4 boundary.

## value

PASS

A crown graph is a standard highly symmetric perfect-matching deletion from a complete bipartite graph. The theorem resolves the exact increase of the double outer-independent domination number and gives every optimal set, with a genuinely distinct equality geometry at n=4. This is a natural infinite-family equality classification, beyond an edge-removal bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
