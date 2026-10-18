---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: For positive-overlap Venn signature (a,b,c), J=1/(1+u) and Ochiai²=1/(1+u+v), where u=(b+c)/a and v=bc/a². Two pairs strictly reverse iff (u-U)(u+v-U-V)<0. Exact independent rational enumeration of all b<=c triples a>=1 and a+b+c<=N gives no strict reversal for N<=4 and precisely ((1,0,4),(1,1,2)) at N=5; the first weak mismatch is ((1,0,2),(1,1,1)) at N=3. The family ((1,0,r+2),(1,1,r)) is a strict reversal for every r>=2 by positive algebraic difference.

## originality

PASS

PASS qualified: Pavoine–Ricotta discusses both coefficients and pointwise Jaccard<=Ochiai and empirical ranking, and Jackson–Somers–Harvey compares occurrences and coefficient behavior; these do not give the exact two-pair sign criterion, earliest weak split and uniquely sharp N=5 threshold. The arithmetic key identity is elementary and itself receives little novelty credit; the exhaustive minimum counterexample plus infinite family constitute the surviving claim.

## value

PASS

The cutoff has a specific scientific motivation: established ecological presence–absence similarities can reorder comparisons despite high empirical agreement. The exact minimal five-species witness and infinite extension give compact adversarial test cases for ecological similarity ranking. This is a sharply motivated counterexample and boundary, not an arbitrary tiny parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
