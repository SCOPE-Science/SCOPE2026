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

PASS: Reconstructed all 1771 pattern monomials (a,b,c,e) for (u,v)∈C×C⊥, the 85 base equations (63 marginals, one normalization, 21 MacWilliams), 1771 Hadamard invariance identities, and 686 nonnegative admissible pattern variables after e-even orthogonality, 1<=c+e<7 distance, and LCD intersection exclusions. Independently fetched the actual 13,393-byte CERTIFICATE.json Git blob; using an independently coded full degree-by-degree 4-variable Hadamard coefficient transform and BigInt exact rational common denominators, checked each of 74 base multipliers and 427 joint multipliers, plus uniform 1/10000 positive coefficient slack. Every one of 686 admissible coefficients is strictly positive; exact right-hand side equals −999899898449/10^12. The Farkas contradiction is rigorous for the LP relaxation, so d(C)<=6 for every actual binary LCD [20,8] code. It does NOT construct an LCD [20,8,6] code nor prove D_M=6 is feasible.

## originality

PASS

PASS (best of knowledge): Kang–Xiong 2026 studies Gauss-phase LP and compares against mixed joint-enumerator LP; its numerical D_M(20,8)=6 benchmark is described as screening in the submitted comparison, whereas the current independently validated all-rational dual inequality supplies a missing exact obstruction. Alahmadi et al 2015 developed joint-LP theory and tables through n=16, not an exact (20,8,7) certificate in accessible material. A published exact Gauss-phase bound or numerical JWE report does not itself prove infeasibility in the distinct JWE relaxation. Full highly relevant 2026 appendix unavailable; preserve risk that an independently verifiable JWE certificate might already appear there.

## value

PASS

PASS: Exact certification at a concrete coding-theoretic boundary resolves a natural gap between numerical LP screening and rigorous joint-enumerator exclusion; 686-variable 501-row rational Farkas verification supplies a reusable benchmark. It is not merely a verifier log or an assertion of optimal LCD code existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
