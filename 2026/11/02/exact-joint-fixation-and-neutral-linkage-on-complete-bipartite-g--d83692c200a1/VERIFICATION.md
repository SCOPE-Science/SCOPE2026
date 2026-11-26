---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A prescribed sequence of copies along an oriented spanning tree gives consensus of each coordinate with state-independent positive block probability; consensus in that coordinate is absorbing. With initial vertex markers, this also gives the ordered terminal ancestor pair. Backward maps at a fixed vertex have the stated two-coordinate law by independence of the time steps. Moving only one coordinate along any neighboring edge has positive probability even on the diagonal, yielding irreducibility; holding gives aperiodicity. Independently checked stationarity per ordered vertex pair. With d_i the degree, the proposed off-diagonal weight is d_i*d_j/(abD). Every one-coordinate move between distinct-position pairs satisfies detailed balance with these weights, since a moving lineage chooses its neighbor with transition probability 1/(2n*d_i). For a mixed ordered pair (i,j) in A x B, the remaining flux from the two diagonals balances exactly: after multiplying rates by 4n, pi_ii/b + pi_jj/a = (2/a+2/b)/D. At (i,i) for i in A the incident diagonal and mixed fluxes give 3*pi_ii=(b/a)*pi_jj+4b/(aD) with j in B, and the swapped identity holds at B. These identities follow by substitution and include a=1 or b=1. Summing the masses gives 1, with nonexistent classes empty. The unique stationary weights therefore give the limiting marker pair and their pushforward under arbitrary initial labels. The diagonal sum 2(a+b)/D decreases with ab at fixed n, giving the stated extrema and limits. On the star the center's two marginals are 1/2, and its diagonal weight tends to 3/10, giving correlation 1/5; the separate K_n calculation uses exit probability 1/(2n) from the diagonal and entry probability 1/[n(n-1)] from off it. The argument is exact for all positive a,b. Frozen verify.py and VERIFICATION.md describe 3,648 forward numerical outcome checks and 196 rational size pairs as bounded corroboration; they were inspected, not executed. The cited original Sadekar v1 model equations are (4)–(5), not (10)–(11); this locator error does not alter the defined kernel or proof.

## originality

PASS

No exact or stronger covering law was found in the indexed and primary passages checked. The core is an ordered two-coordinate stationary ancestor distribution with splitting and shared-neighbor moves, not the one-lineage voter law, the initiating update rule, or an equilibrium correlation in a pinned system. The comparison is limited to these retrieved results, not a historical-priority claim.

## value

PASS

The full ordered ancestor law controls terminal covariance for arbitrary initial labels and is useful as an exact zero-selection baseline for a specified coevolution model. The contrast between persistent star linkage and vanishing balanced linkage separates an effect of topology and common-neighbor copying from selective advantage. This is not a consequence of either marginal fixation law, and applies to the whole biclique family, including sharp fixed-size extremes rather than a choice of isolated graph examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
