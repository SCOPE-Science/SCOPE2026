---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For 0<T<1 an unsecured vertex is safe exactly when its unsecured component has no edges; NE unsecured sets are precisely maximal independent sets, and social optima leave maximum independent sets. Thus BestNE=n-alpha, WorstNE=n-i, Opt=n-alpha. For the two k-leaf hubs bridged at a1b1, a three-edge matching and explicit size-3 vertex cover prove alpha(G_k)=alpha(H_k)=2k-1, so opt/bestNE=3. Hubs form independent dominating set in tree G_k and no universal vertex exists, so i(G_k)=2. With added uv, case split on which hubs are in an independent dominating set forces >=k+1, attained by one hub plus all opposite leaves, so i(H_k)=k+1. n<=5 connected graph has i<=2; if i=1 universal persists; hence six-vertex sharpness. Independently enumerated all vertex subsets for k=2,3,4, confirming (alpha,i)=(3,2)->(3,3),(5,2)->(5,4),(7,2)->(7,5). Finite cases do not establish unbounded k.

## originality

PASS

Best-of-knowledge statement-level comparison identifies no prior theorem implying the final claim at its actual hypotheses; known overlap and residual bibliographic risks are recorded, not erased.

## value

PASS

The addition of one contact to a connected tree produces an arbitrarily large decrease in worst pure-equilibrium protection burden with identical constant social optimum, with an exact six-vertex onset. This is a motivated and counterintuitive strategic comparative static explained by ordinary independent domination, not a trivial equilibrium restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
