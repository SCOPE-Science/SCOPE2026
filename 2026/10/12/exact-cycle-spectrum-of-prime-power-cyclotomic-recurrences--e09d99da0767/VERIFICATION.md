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

For every prime p, index j>=1, modulus m>=1, free integral module A=Z[X]/Phi_{p^j}(X) is rank p^r over B=Z[Y]/Phi_{p^{j-r}}(Y), Y=X^{p^r}, for 0<=r<j. Multiplication by Y-1 has cokernel B/(Y-1)=Z/p and is nonsingular over Q; hence SNF(C^{p^r}-I) has exactly p^r diagonal p entries, all remaining entries 1. Modulo m fixed points are gcd(p,m)^{p^r}; C^{p^j}=I and Mobius/telescoping gives all cycle counts. This handles p=2,j=1,m=1. Reconstructed exact small cycle decompositions with disjoint cycles, e.g. (p,j,m)=(3,1,6): three fixed points and eleven 3-cycles, (2,2,4): two fixed, one 2-cycle and three 4-cycles. Finite replay is corroboration; universal assertion follows from the integral-module/SNF proof.

## originality

PASS

Published conjectures gave the same prime-power cycle formulas without their integral Smith-form proof. The assessed original contribution is establishing the conjectured spectrum and its SNF certificate, not inventing the conjectured numbers. General periodic-point inversion is prior work and requires the missing fixed-point input. Resultary did not retrieve an equivalent complete cyclotomic proof. A later or unindexed proof remains a best-of-knowledge priority risk.

## value

PASS

The exact all-modulus orbit decomposition of a natural prime-power cyclotomic companion recurrence answers explicitly published recurrence-period conjectures. Its Smith-form lemma is a reusable arithmetic mechanism; this is a motivated complete all-parameter classification, not a finite numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
