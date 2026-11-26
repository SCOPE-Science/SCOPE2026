# Independent mathematical audit

## correctness

PASS

This verdict applies to the corrected files under /workspace/repairs/5. The frozen mathematical identities themselves check out: greedily completed arches end at the first available disjoint unequal pair, or equivalently arbitrary disjoint pairs supply successive rich blocks. The two transfer states give P=1+zP+zyuE and E=1+z(1+y)P, yielding the frozen rational and binomial forms. Independently, letting each of the n-t gaps contain 2a_i+epsilon_i present edges shows that the same counts equal 2*binom(n-t,2k-t)*binom(n-k-1,t-k) on their support. In the repair the indicator vectors of weight t are uniform, hence so are their weak compositions of t separated by the fixed number m-t of zeros. The tail of a specified part at r is binom(m-r,t-r)/binom(m,t); summing its odd tails gives ceil(part/2) in expectation, with the correct boundary values. For the concentration proof, after conditioning on a fixed sample prefix, two different next labels can be coupled by their transposition in the completion. Whether the sampled labels are present edges or absent edges, the resulting graphs differ by at most one exchange, and the matching sizes differ by at most one as both have the same graph after removing their exceptional edge. This gives at most d=min(t,m-t) martingale steps of absolute increment at most one, so Azuma gives 2 exp(-s^2/(2d)); d=0 is deterministic. For 0<rho<1 the odd-tail sum is dominated geometrically, giving the normalized expectation rho/(1+rho), and the same bound at deviations proportional to n gives convergence in probability. At rho=0 use 0<=K<=t; at rho=1 use ceil(t/2)<=K<=floor(n/2). `python3 /workspace/reviews/replay_finite.py 5` checked the original histograms and means through length 11 directly by subsequence membership; `python3 /workspace/repairs/5/verify.py` gave 77 exact conditional means and 5,630 exact ordered swap checks. Neither finite check establishes the analytic limit. The frozen verification script was inspected, not executed.

## originality

PASS

For the repaired conditional-density claim only. The original framing does not pass originality: 412ee9869e0f explicitly gives the linear path-matching identity, and its displayed reset-at-zero transfer matrix mechanically gives the entire frozen joint law by changing cycle closure to free path boundary conditions. The repair removes both as claims of novelty and explicitly credits this implication. Its distinct focus is the fixed-budget conditional concentration and density limit, with the hypergeometric mean as a starting point, not a claim of new enumeration by coefficient extraction. Inspected unrefined, circular and general run-counting results do not state this exact-budget probability theorem or give the uniform minority-set deviation bound. The narrowed catalogue and primary search supports the distinction, not global priority.

## value

PASS

For a prescribed transition budget, the ordinary unrefined 1/3 law is not predictive at arbitrary densities, and the edge indicators are dependent. The repaired result answers the natural fixed-budget question for every density including both endpoints, expresses the finite center exactly, and gives a uniform deviation scale tied to the minority indicators rather than the full length. This is useful even for near-full and sparse budgets, where a length-based bound misses that scale. It is a substantive probability statement, not a repackaging of the already covered word counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
