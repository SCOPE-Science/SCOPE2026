# Independent mathematical audit

## correctness

PASS

Directly summing the payoff difference at j A-neighbors gives j-(N-1) times the threshold in the sense j-(N-1)*threshold. In a count-k state j is k for a focal B and k-1 for a focal A. This distinction gives q_(m+1)=(m+1)/N, twice the interior value, and its reflected counterpart. At k<=m, upward moves are impossible and q_k=k/N; reflection gives the right cleanup corridor. A positive-probability path to a corridor exists from every interior state and the corridors reach unanimity, giving finite mean time on this finite chain; symmetry gives equal winner probabilities. At the balanced start the exit-time first-step equation has p_r=q_r=1/4, hence d_r=2. For m+2<=k<r, multiply q_k*d_k=1+p_k*d_(k+1) by binomial(N,k) and telescope using detailed balance. This gives the exact half-central-mass numerator and the separate doubled-death-rate endpoint equation gives D_(m+1). Adding the corridor mean NH_m works also at m=0, and m=r-2 uses the valid central condition directly. The lower bound retains the central coefficient in D_(m+2); the upper bound is 2^N/binomial(N,m+2) times polynomial factors plus O(N log N). Stirling along allowable sizes yields the strictly positive rate log 2-H(eta). Independently, I enumerated both payoff matrices and the focal player on one representative labeling per count, then solved the full rational system (u+d)T_k-u*T_(k+1)-d*T_(k-1)=2N with zero unanimous boundary values, where u,d count the upward and downward updates out of 2N equally likely choices. At (N,eta)=(4,1/4),(6,3/10),(20,1/5) this gives means 9, 13 and 20759/21 updates, respectively. The frozen verifier was inspected, not executed; these finite checks do not establish the rate.

## originality

PASS

The supported distinct claim is the boundary-corrected exact finite consensus time for the tie-free, opposed-threshold, full-overlap clique model. The entropy rate is not an independent originality claim: it coincides with the symmetric specialization of a broader indexed rate and follows from the same binomial barrier mechanism. The explicitly compared finite theorem for integer thresholds and tie retention has a different endpoint transition, so it does not state or specialize to the finite identity under review.

## value

PASS

This supplies an exact, reproducible lifetime benchmark for the apparently mixed state of the published coordination mechanism in its natural full-overlap clique limit. It distinguishes eventual absorption from long-lived coexistence, and exactly quantifies the finite-clock effect lost by treating the whole mixed corridor as an ordinary heat bath. The change in the boundary contribution is substantial at a fixed finite threshold and is invisible in the exponent alone; the claim is useful for measuring finite-size consensus, without asserting the same behavior on sparse layers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
