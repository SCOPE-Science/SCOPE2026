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

For every integer g>=3 and k>=1, n in E1 requires n=1+b with b in the odd- or even-supported digit class. In odd class the nonoverlapping mixed sum forces 1; an even+even representation is possible exactly when all odd-position digits of b are <=1, by carrying one from each adjacent even digit, with both summands positive. For even class splitting base-g columns classifies 2,3 and 1+g^{2j} (j>=1) as unique essential cases; g=3 and carry boundary handled explicitly. Thus the three stated families are disjoint and the odd-digit family has g^k-2^k vectors, plus k-1 powers and 2 exceptions, proving exact count g^k-2^k+k+1 for all g,k. Independent code enumerates all admissible positive summands and ALL unordered representations below g^{2k}, checking equality of full essentiality sets (not just totals) for (g,k)=(3,1),(3,2),(3,3),(4,2),(5,2),(6,2), giving counts 3,8,23,15,24,35. Finite checks supplement unlimited carry proof.

## originality

PASS

Tang 2026 Theorem 1.1 proves general minimality for every infinite digit partition when g>h, Corollaries 1.4/1.5 give lower bounds for E_a but not exact single-element fiber; earlier Tang-Ling treats minimality conditions and counterexamples, not explicit all-n classifications. Same objects and parameters were compared, not titles alone. Best-of-knowledge PASS subject to unindexed exact digit analysis risk.

## value

PASS

The fiber E_1 is a natural refined invariant of minimality, and its full digit classification, sharp leading sqrt-scale coefficient 1 and precise correction -2^k+k+1 are not recoverable from the old generic lower bound. A natural evenly split 2-class g-adic basis provides mathematical motivation for this exact cutoff census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
