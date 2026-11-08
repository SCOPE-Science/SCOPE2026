---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For all a,b>=1 and exactly three synchronous cyclic colors, the update factors through 49 nonempty shore-support pairs (A,B), with each color transformed by the opposite shore successor-support test. I independently computed all 49 support transitions, obtaining only diagonal singleton fixed supports, full/full fixed support, and three two-cycles ((3,5),(3,6),(5,6) and their reverses); every other support enters within <=2 steps. Applying the exact labelled update shows the support two-cycles induce four-step labelled, not two-step, periods. Surjective-coloring counts on a labelled shore are S1=1, S2=2^m-2=U_m, S3=3^m-3*2^m+3=R_m. The six table populations are respectively 3, R_a R_b, 6 U_a U_b, 6+3(U_a+U_b+U_a U_b), 3(U_a R_b+R_a U_b), and 6(U_a+U_b)+3(R_a+R_b); they sum to 3^(a+b), giving F^14=F^2 and orbit counts by division by primitive periods. An independently coded brute-force labelled update checked all six (T,p) classes for 16 shore pairs a,b=1..4, each up to 3^8 configurations; the complete finite support classification and surjection identity—not a finite-size extrapolation—prove all dimensions. The stated exceptional conditional probability follows from the exact complement identity and min(a,b)->infinity estimates.

## originality

PASS

Best-of-knowledge originality after primary-literature reading and Resultary queries. The explicitly identified prior statements and implication gaps are documented under the four checks. A failed search is not proof of priority, and inaccessible literature was not treated as automatic failure.

## value

PASS

This is a complete exact recurrent/transient census for a natural canonical nontrivial graph family under a widely studied cyclic excitation rule, not just a verification of graph-diameter synchronization. The primitive period-three and period-four orbit counts and asymptotically dominant one-step exceptional transient quantify phenomena left undecided by general qualitative criteria. The 49-support factorization provides a reusable finite-state method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
