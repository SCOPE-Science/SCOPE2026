# Independent mathematical audit

## correctness

PASS

For each reported round total demand is at least three. If some demand is unmet, reported PE forces total capped utility to be three, so no allocation can exceed its report or leave unused supply; if all demands are met, the total constraint gives the same conclusion. CF2 sets the lower increment bound 1−a when a<1; CF1 gives it when a≥1, and CF3 forces equality since the bounds sum to zero. In truthful profile A, CF4 fixes the unit to agent 1 initially; their second-round quantity cannot exceed one without CF5 requiring two for agent 3. Two demand-saturated rounds leave credits (2,0,−2), so CF4–CF5 bound agent 2's final quantity to exactly one. Thus agent 1 has payoff four. Independently exchanging the labels in the forcing inequalities proves the analogous payoff in B, not symmetry of a mechanism. Both altered histories have the same fixed-label reports (0,3,0),(2,0,2) through round two, so the same x∈[1,2] is used for agent 1 by onlineness. In each altered branch the final credit of agent 2 is −1 and that of the relevant deviator at least 2. Any positive final quantity for 2 would force all three units to the deviator by CF5, a contradiction. The payoff gains are therefore x−1 and 2−x, with sum one including the endpoints. No assumption about anonymity or future truthful demands enters the mechanism's observed state. A separate exhaustive 1/16-quantity-grid history search (python3 /workspace/review_evidence/reproduce.py 1) found the two unique truthful histories, all 17 common splits and minimum maximum gain 1/2 on that grid; the real-valued proof is analytical.

## originality

PASS

The published impossibility requires anonymity and explicitly asks whether that requirement can be removed. Removing it is a genuine change in quantifier; the original fixed-profile proof cannot force a half split for a biased mechanism, whereas the common altered prefix makes two opposite gains unavoidable. The frozen result's cited comparison is substantively correct. For precision the fixed-version PDFs label the prior result v1 Theorem 2, v2 Theorem 3, and conference Theorem 2; theorem numbers quoted in portions of the frozen self-audit are not the fixed-version PDF locators.

## value

PASS

The result resolves a stated open question about a natural allocation desideratum, removing a meaningful assumption without weakening PE, CF or the incentive requirement. The identical-report-history construction works even with fixed label preferences and gives a quantitative lower bound on manipulation for the two-profile witness. This is not a mere re-evaluation of the original symmetric split.

The dated certificate retains the supplied scientific assessment, sources and limitations.
