# Independent mathematical audit

## correctness

PASS

Independently checked the finite result by deleting the marked leaf, rather than by the frozen recursion. All parent arrays have equal mass. Deleting j when it is a final leaf and order-preservingly relabeling gives a bijection with pairs consisting of an arbitrary recursive tree of size n−1 and an attachment label in {1,…,j−1}; reversal inserts j as a leaf. Thus the event probability is (j−1)/(n−1), the residual tree is uniform, and all other depths are unchanged. The marked depth has its ordinary mean H_(j−1), since its parent law and the earlier tree are unaltered by the later exclusions. Using E[T_k]=k(H_k−1), obtained by the usual depth recursion, the conditional mean is (n−1)(H_(n−1)−1)+H_(j−1), which yields the stated covariance. For m=j−1 and N=n−1, the absolute covariance times N is F_N(m)=m(H_N−H_m), with forward difference H_N−H_m−1, strictly decreasing wherever two differences exist. Integral comparison gives a uniform error at most 1/N from (m/N)log(N/m), including the zero-age endpoint. This profile has a unique maximum at e⁻¹, so all maximizing sequences and the maximum converge as claimed. Exchanging the harmonic sums gives sum_m F_N(m)=N(N−1)/4. The cases j=n and n=2 (always a leaf) give zero covariance as required.

## originality

PASS

The supported distinct claim is the exact final-leaf covariance and conditional mean at a specified birth rank, and hence the age profile. The aggregate formula is already covered. A later-dated Resultary record materially matches the marked theorem, but was not established to be earlier evidence.

## value

PASS

Final leaf status and total path length are natural recursive-tree observables. The birth-specific law resolves which age contributes most strongly and yields covariance for any chosen deterministic age window or weighting. In particular, it locates the strongest dependence at an interior age fraction rather than at either endpoint. Those are precise uses of the marked formula, not of the already known total covariance. A short deletion proof does not make the observed age-dependent invariant an automatic reading of the unmarked law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
