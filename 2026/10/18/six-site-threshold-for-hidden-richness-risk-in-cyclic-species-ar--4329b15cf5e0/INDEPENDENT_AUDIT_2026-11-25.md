# Independent mathematical audit

## correctness

PASS

The endpoint mean gives total species S. Windows of length 1 and N have a point mass, length 2 is binary, and length N−1 can lose at most one species. The only remaining depth for N≤5 is N=5,m=3. Its law is binary unless S=3 with a species occupying three sites. When S=3, the mean at depth 4 distinguishes (2,2,1) from (3,1,1), via singleton losses. In (3,1,1) the depth-2 mean distinguishes adjacent from nonadjacent singleton sites; in each case the pattern is unique up to symmetry and relabeling. For N≥6 with nonadjacent B,C, every window of length at least two detects A, and the singletons each have detection probability m/N. Among the N starts, those with both rare sites split by the first rare site in the linear window, giving exactly (m−s)_+ + (m−(N−s))_+, also at m=N. Thus at m≥2 the law is that of one plus two indicators with those marginals and intersection. The variable part of the variance is twice the joint probability. At floor(N/2) the two summands cannot both be positive, the count ranges from 0 to floor(N/2)−2, and the stated separations attain the endpoints, including odd N. At N=6,m=3 the histograms are (1,4,1) and (0,6,0) by direct count, with variances 1/3 and 0. Independent replay: python3 /workspace/branches/check_3.py checks all n^n site colorings for each n≤5, the labelled witness detection counts and histograms, and all eligible starts/separations through N=40. The unbounded claim follows analytically, not from the replay.

## originality

PASS

Mean richness as an aggregate of detection statistics and the importance of spatial variability are not new. On the evidence inspected, the new part is the sharp full-law threshold in the cyclic one-label model and the exact size-dependent variance ambiguity even with identical labelled detection curves.

## value

PASS

For a standard spatial summary, this fixes the minimum size at which compressing windows to a mean loses the entire local richness law, and shows that even retaining all labelled marginal detections does not recover the missing joint behavior. The exact half-window gap makes the effect interpretable at arbitrary size, including deterministic versus fluctuating landscapes at the same mean. This is a sharp, identifiable boundary and witness in the stated design, not an ecological prediction or a universal variance bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
