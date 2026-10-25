# Independent mathematical audit

## correctness

PASS

For Cr_n=K2 x Kn with named layers and n>=2, a_i sees b_j iff j !=i. The total Roman conditions are: every zero has an opposite-layer label-two defender at a different index, and every positive has a positive opposite-layer neighbour at a different index. Disjointly partition assignments by counts of twos in A and B (0,1,>=2); after swapping layers the seven cases in RESULT.md give exactly F_n^2, 2 n z^2 Q_n(F_n-F_(n-1)), 2 U_n V_n, n z^4 Q_n^2, n(n-1)z^6(1+z)^(2n-4), 2n z^(n+2)Q_n and z^(2n), with Q,F,U,V as defined there. Each case necessity/sufficiency was checked against the local neighborhoods; no disjointness or zero-label defect found, including special n=2 where the graph is 2 K2. An independently written direct graph-neighborhood brute evaluator compared all 3^(2n) labelled functions and all coefficients to the 7-term formula for n=2..6: totals 16,259,3232,35769,371270 feasible functions, minima (4,1),(6,31),(6,48),(6,100),(6,180). Extraction gives n^2(n-1) optimal functions for n>=4 (not just the known minimum 6); no numerical finite check is claimed to establish the infinite formula, which follows from the exhaustive seven-case symbolic proof.

## originality

PASS

The minimum total Roman domination number of K2 x Kn is established in published direct-product work. The new statement is the entire integer-weight enumerator, not ordinary Roman or Roman{2} variants, and it is not mechanically implied by known minimum weight alone. The Resultary complete-multipartite enumerator is a different graph family since Cr_n is not complete multipartite for n>=3.

## value

PASS

Crown graphs form a classic natural direct-product family; enumerating every total Roman function by weight is a mathematically meaningful refinement of an established extremal domination invariant and gives exact multiplicities of every weight. The seven-case description works uniformly for arbitrary n and is neither a trivial minimum-value restatement nor a known complete-multipartite table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
