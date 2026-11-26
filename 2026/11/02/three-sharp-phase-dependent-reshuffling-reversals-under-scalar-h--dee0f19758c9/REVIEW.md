# Independent mathematical audit

## correctness

PASS

The companion polynomial r²-(1+beta-t)r+beta is strictly Schur stable on the stated open interval. In the normalized recursion, independent sampling has innovation g=(t,0); reshuffling has end-of-epoch innovation (Ag-g) times the fresh sign, not two independent innovations. The odd covariance uses A S_E A^T+gg^T and its first diagonal entry equals the second diagonal entry of S_E. For an analytic check, set c=1+beta-t, let u and v be normalized even and odd variances, and let z and w be the corresponding lag-one covariances. Then w=c u-beta z and z=c v-beta w-t², with the last term coming from the sign reversal. Adding and subtracting the resulting two variance equations gives u+v=2t²/D and u-v=-2ct²/((1+beta)G); with independent signs the one-step equation gives t(1+beta)/D. Rescaling by U gives the frozen formulas. The independent symbolic replay at /workspace/branches/d4dcdb01-fed6-445e-9eb6-4b86d281b243/independent_phase_covariance.py returned EXACT_REPLAY_OK for all three variances, both comparison factorizations, the phase average and the rational witness (1/3,3/2,5/3) in E,I,O order. D and G are positive, so the even comparison changes sign only at t0, and the odd comparison changes sign at t_-, t0 and t_+; these are distinct and inside the stable interval for positive beta. In particular, the two opposite-phase comparison intervals are (t_-,t0) and (t0,t_+). The stability endpoints are excluded. The supplied checker was inspected, not executed; the replay is exact algebra, not evidence for cases with other losses or sampling schemes.

## originality

PASS

Credit is limited to the positive-momentum, within-epoch stationary pair and its exact comparison thresholds against IID. Phase-averaged heavy-ball variance, related scalar reshuffling reversals at epoch ends, and the general fact that reshuffling is not always better are antecedents, not separate novelty claims. The inspected prior statements do not give or determine the phase-resolved result.

## value

PASS

The exact comparison shows that the recommendation about which sampling rule to use can reverse solely by changing the observation position within the same epoch. The stable scalar model isolates that effect, the open reversal intervals and exact witnesses make it robust, and the average cannot reveal which phase wins. This is a useful boundary case for phase-sensitive stationary-risk analysis, not a general algorithmic recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
