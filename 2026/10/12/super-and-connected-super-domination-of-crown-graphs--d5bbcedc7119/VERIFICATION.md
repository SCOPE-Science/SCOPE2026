---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For Cr_n=K_n,n minus a perfect matching, each omitted a_i requires a selected b_j adjacent to a_i but to no other omitted A vertex; because b_j is adjacent to all A except a_j, at most two A can be omitted, and symmetrically at most two B. Hence |S|>=2n-4. Equality forces two omitted A indices I={i,j} and two omitted B indices J={k,l}; the unique possible private witnesses b_j,b_i and a_l,a_k must all remain selected, exactly when I∩J=empty. Every such S is super dominating. Its induced subgraph is K_2,2 for n=4; for n>=5, each part has >=3 selected vertices and any missing cross-pair has a selected alternating length-three path, proving connectedness. Counting disjoint index pairs gives binom(n,2)binom(n-2,2). Boundary n=3 is C6 with 15 ordinary vs 6 connected minimum sets. An independent exhaustive definition-based enumerator checks 3<=n<=7.

## originality

PASS

Best-of-knowledge implication comparison of assigned exact claim against primary literature and semantic Resultary search. Super domination is not ordinary, restrained, perfect Roman, majority, or upper domination; such formulas cannot be equated with the private-neighbor condition. Neither complete-bipartite result nor connected super domination on general graph products gives the exact crown lower bound or disjoint-pair equality classification; no direct stronger coverage identified.

## value

PASS

Crown graphs are natural regular bipartite graph families obtained by removing a perfect matching. Exact minimum super- and connected-super-domination numbers, complete rigidity of extremal sets and their count are motivated graph invariants; the difference from K_n,n establishes nonmonotone edge-deletion behavior. This is a self-contained all-n exact extremal classification, not an arbitrary small case or general paper-sized claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
