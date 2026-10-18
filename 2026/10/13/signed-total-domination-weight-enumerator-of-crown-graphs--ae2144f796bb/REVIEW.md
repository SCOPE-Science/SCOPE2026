# Independent mathematical audit

## correctness

PASS

PASS: For Cr_n (n>=3), the open neighborhood of a_i is B minus b_i and of b_i is A minus a_i. For each side, the label sum must be at least 2, because at least one +1 occurs and its complementary neighborhood tests side_sum-1>=1; conversely a side sum >=2 implies all its neighborhoods meet the bound. Parity of a length-n ±1 sum upgrades 2 to 2 for even n and 3 for odd n. Therefore h=(n+epsilon_n)/2 plus vertices per part is necessary and sufficient. Independent choices of the two parts yield E_n(u,v)=P_n(u)P_n(v) where P_n(z)=sum_{k=h}^n binom(n,k)z^k; W_n(t)=(sum binom(n,k)t^{2k-n})^2, gamma_st=2epsilon_n and min layer binom(n,h)^2, total counts by binomial symmetry. My independent brute-force open-neighborhood classification for n=3,4,5,6 reproduced totals 1,25,36,484 and minimum multiplicities 1,16,25,225; the parity algebra proves arbitrary n. No n<3 connected-crown claim.

## originality

PASS

PASS best-of-knowledge: Zelinka (2001) proves signed-total-domination numbers for complete bipartite graphs, not crown graphs or all feasible-function weight distributions. Liang (2012/2016) classifies scalar domination numbers of complete multipartite graphs. Cr_n is not complete multipartite for n>=3, because between its two given classes each vertex has a distinct non-neighbor; the neighborhood sum loses a coordinate. Published-record matches for signed total domination of complete multipartite and other crown domination variants concern different invariants. The full crown weight enumerator and parity-sensitive deletion are not mechanically implied by the known scalar minima.

## value

PASS

PASS with appropriately modest scope: The family of all signed total dominating labelings of a standard naturally defined near-complete bipartite graph is a natural enumerative invariant, not an arbitrary small numeric slice. The exact bivariate count yields every weight coefficient, minimum-layer multiplicity, total number and a parity-sensitive classification of which labelings are destroyed by deleting a perfect matching. The derivation is elementary, so no deep technique or generalization beyond crowns is claimed; the whole feasible-function distribution is more informative than the previously known scalar parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
