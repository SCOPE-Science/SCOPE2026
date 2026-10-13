---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the crown-graph fixed-point calculation

The standalone `checker.py` uses only Python 3's standard library. Run it from the directory containing the file with `python3 checker.py`. The recorded successful output is `checker_output.txt`. For each \(3\le n\le8\), it independently regenerates every edge exponent difference, compares the expected minimal monomial generating set against the actual chart monomials, computes exact rational matrix ranks of the spanning rays and tight facet generators, and checks the all-ones canonical character pairings. For \(3\le n\le5\), it constructively decomposes every integral cone point whose coordinates lie in \(\{0,1,2\}\); exactly \(6{,}933\) such points passed. These finite checks supplement a complete symbolic proof for arbitrary \(n\ge4\).

The cone inequalities and integer decomposition are the main general proof; finite enumeration has not been treated as evidence that no other singular orbit, nontrivial divisor, or novel prior theorem exists. The class-group isomorphism is local at a fixed point and must not be interchanged with the class group of the entire affine cone. No independent external audit was performed.
