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

At the minimum valuation u there are two parity classes inside the common mod-2^u class; exactly two points are in one class. They are the unique closest pair. Dephase at the outsiders to obtain the four entries A=omega^(ac), B=omega^(ad), C=omega^(bc), D=omega^(bd). Rank one occurs iff all four equal 1, i.e. u+s>=m. Otherwise all four differ from 1; conjugating the chord-product equality forces AD=BC, and expansion under that condition gives the stated two factors. One factor vanishes exactly at u+t>=m or v+s>=m, and either inequality also forces AD=BC. This checks necessity, sufficiency and equality boundaries. Count N^2/2^(v+2) closest pairs and N/2^(u+1) outsiders per pair to get B_m; product counts enumerate the ordered row/column roles exactly once. For the event v+s>=m put v=m-h: the contribution to N times the normalized weighted sum tends to (8/3)2^-h and is bounded by that same summable sequence. In the intersection with u+t>=m, summing v and t for fixed u,s gives at most 4/N^2 after multiplying by 2^(-u-s). The intersection therefore contributes o(1/N) and contains all rank-one cases. The two one-sided events give (16/3)/64=1/12 at N^5 scale and hence probability ~3/N. All ranks occur for m>=4, e.g. types (m-2,m-1) on both sides for rank one, (0,m-1) against (1,2) for rank two, and (0,1) on both sides for rank three. Independent exact reduction checks all 316752 pairs at N=4,8,16 plus 18000 seeded pairs each at N=32,64,128, and independently enumerates dyadic type frequencies through N=128.

## originality

PASS

Best-of-knowledge pass for the integrated dyadic census and singularity asymptotic. The collision mechanism is a specialization of general proportional-pair rigidity; do not credit standalone novelty to that mechanism. A later prime-power record genuinely covers the rank law, exact census and leading asymptotic by specialization; its date does not establish earlier coverage. The Delvaux–Van Barel antecedent remains a real access risk for the structural part, not evidence of noncoverage or grounds by itself to fail.

## value

PASS

A natural structured-matrix sampling question asks how often an independently chosen minor is singular and of which rank. The valuation stratification enables a complete count, identifies a concrete leading 3/N probability, and shows rank one is negligible. These quantitative consequences are not supplied by checking a principal or proportional-pair criterion alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
