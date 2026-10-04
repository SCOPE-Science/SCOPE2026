# Review

## Correctness
PASS. For each level \(s<1\), the conditional rejection probability is bounded pointwise by a decreasing envelope \(g_s(P)\). Super-uniformity gives stochastic dominance over a uniform variable, so integrating that envelope is a valid worst-case bound. The envelope integral is exactly \(h_1t_1+(h_2-h_1)t_2\), and its three regions are below the diagonal precisely when \(h_1/b_1+(h_2-h_1)/b_2\le1\). Necessity uses an exactly uniform \(P\) and a proxy label chosen as a deterministic function of \(P\) to attain the envelope at a small level. Boundary cases \(s=1\), capped thresholds, and the ordering assumptions are handled explicitly.

## Originality
PASS. The closest primary source, arXiv:2512.01423, writes the exact active-p tail condition but proceeds through a sufficient decomposition and explicitly states that decomposition is not necessary. Its supplement gives only the baseline nondecomposable construction with \(a\equiv b\equiv1\). Full-text searches for finite/two-point/two-value formulations and parameter aliases did not reveal the two-bin necessary-and-sufficient multiplier frontier. arXiv:2502.05715 proves a particular arbitrary-dependence active-p construction but does not characterize the two-bin nonquery-one family. Targeted database and web searches returned no equivalent formula or implication. The residual risk is an equivalent robust-randomization result under different terminology.

## Value
PASS. Two bins are the smallest nonconstant discretization of an auxiliary proxy and are directly usable when side information is binned for budget allocation. The theorem replaces a conservative sufficient rule with an exact power frontier under the same harsh arbitrary-dependence regime. The boundary example \((1/5,4/5,1/2,1)\) proves the improvement is substantive: it permits halving queried p-values in the low-query bin while no common split parameter can certify the construction. This is a structural validity budget, not a routine reparameterization or a numerical table entry.

## Closest literature and limitations
The primary comparison is Qi Kuang, Bowen Gang, and Yin Xia, arXiv:2512.01423, especially Definition 2, equation (3), Remark 3, Theorems 2--3, and Supplement F. A second comparison is Ziyu Xu et al., arXiv:2502.05715, especially its arbitrary-dependence active p-value construction and Proposition 2. The result does not claim a full functional characterization, more than two bins, or a new FDR theorem. An equivalent statement hidden under unrelated randomized-test terminology remains the main residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
