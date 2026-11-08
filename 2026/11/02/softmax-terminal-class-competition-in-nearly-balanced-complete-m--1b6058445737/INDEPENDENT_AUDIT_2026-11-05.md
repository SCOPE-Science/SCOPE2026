# Independent mathematical audit

## correctness

PASS

For fixed k>=3, the embedded part chain has P(i,j)=m_j/(N-m_i), reversible stationary pi_i=m_i(N-m_i)/(N^2-sum_j m_j^2). A two-step Doeblin lower bound is uniform for nearly equal parts and yields E V_i(t)=pi_i t+O(1), Var V_i(t)=O(t); at t=O(n log n), clocks deviate o_p(n). Independent uniform coupon streams are an exact within-part construction; the preseen initial vertex affects completion with probability <=1/m_i. Coupon missing-count factorial moments imply independent Gumbel limits. Expanding pi_i to 1/log n, and centering at kn(log n + (k-2)Theta/[k(k-1)]), gives shifted G_i+theta_i/(k-1) jointly. The exponential-race identity gives softmax exp(theta_i/(k-1)); S(log x)/(N-x) mean-value derivative gives the one-sided unique-part domination when all pairwise size gaps are >>n/log n. Checks of formula normalization and finite exact-state package checker show no boundary mismatch; finite simulations do not prove convergence.

## originality

PASS

Best-of-knowledge new joint part-labeled near-balance Gumbel limit and softmax law for fixed nonbipartite complete multipartite walks. Existing global cover-time and exact hitting-time results are weaker/different; fixed k>=3 prevents direct use of known bipartite logistic law.

## value

PASS

The part label of the final unseen vertex is a natural localized cover-time extreme statistic. The theorem identifies the critical n/log n imbalance, joint fluctuations and a k-dependent sensitivity distinct from the bipartite alternating process; these are quantitative, reusable facts not implied by a scalar cover-time law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
