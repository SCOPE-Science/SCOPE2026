---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For finite connected simple G of n>=3 with m edges, M=m+binom(n,2), verify D_i(C^2(G);z)=sum_{s=0}^{alpha(G)}a_s(G) z^{M-(n-1)s+binom(s+1,2)} + m z^{M-1}+2m z^{M-n+2}. In C(H), the old-vertex part of each independent dominating set is a clique X and subdivision choices are forced exactly for edges of H-X; nonselected old v is undominated iff N_H(v)=X. In H=C(G), every open neighborhood is nonclique (old vertices have an isolated subdivision neighbor; subdivision vertices have nonadjacent endpoints), so all intermediate cliques are admissible. Their exhaustive types are original independent sets, m subdivision singletons, 2m incident pairs; degree count yields the formula. Difference e_{s+1}-e_s=s+2-n proves the n>=4 complete/star/other minimum multiplicity trichotomy and nonstar recovery. Independently enumerated all maximal independent sets of C^2(G) for four selected small hosts, including P3, K3, K1,3, P4; full claimed finite verifier was inspected but its entire 870-host run not repeated. Infinite proof is structural.

## originality

PASS

Theorem 2.12 in the directly relevant September 2026 central-graph paper already establishes the minimum independent domination NUMBER for C^2(G); this part is not new. Its Theorems 2.1 and 2.12 were examined in all 13 pages and do not give a full independent-domination polynomial or multiplicities. The new claim is the complete cardinality enumerator, constructive bijection of all sets, total count, minimum multiplicities, and coefficient recovery. General independent-domination polynomial theory and a higher-central-iterate minimum-number record were also compared. No matching stronger enumerator found in the checked material; priority remains contingent.

## value

PASS

The independent-domination polynomial is a natural graph invariant refining a known minimum-number theorem. The exact closed formula for every connected input, its bijective explanation, and recovery of the original independent-set counts for nonstars would be useful for extremal enumeration and distinguishing iterated central graphs; the classification handles nontrivial complete/star degeneracies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
