---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

In any connected triangle-free graph, a dismantlable dominated vertex is a leaf, so the nonempty induced cop-win subgraphs are exactly trees. The selected nonempty ladder columns form a contiguous interval in symbols top,bottom,double; connectivity and acyclicity are equivalent to excluding TB, BT and DD as adjacent pairs. Transfer recurrences U_{ell+1}=z(U_ell+2V_ell), V_{ell+1}=z^2 U_ell and placement factor n-ell+1 yield the claimed t z(2+z+3t z^2)/((1-t)^2(1-tz-2t²z³)). A second singleton-gap count verifies the coefficient binomial formula; reliability follows from p/(1-p) substitution and first moment by derivative. Independently enumerated all nonempty graph vertex subsets n=1..8, tested acyclicity/connectivity and transfer coefficients, including n=4 counts 8,10,16,18,16,10 and moment identity; unrestricted theorem rests on the complete forbidden-word bijection.

## originality

PASS

The unweighted induced-tree counts C_n(1) and maximum-tree cardinalities/multiplicities occur in OEIS A360202/A360920/A360918; they are expressly prior art. Vince studies all connected induced vertex subsets and their mean density 3/4, not necessarily induced trees. Ahmed–Cameron defines node cop-win reliability and handles unicyclic/bicyclic host graphs; L_n has n-1 independent cycles. Its all-size, all-n cardinality distribution is not implied by those scalar results. Both relevant historical full texts were inaccessible (Oxford VPN disconnected), so equivalent specialized formulas remain risk.

## value

PASS

The two-row ladder is a canonical graph family, and the full cop-win induced-subset size polynomial is the natural reliability invariant under vertex failure. It yields all survival probabilities, every coefficient, and the limiting conditional density 2/3; this is stronger than a known total and not a mechanistic re-tabulation of it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
