# A single covariance sign transition among block sizes at fixed partition richness

## Finding

Fix integers \(n\ge4\) and \(2\le k\le n-2\). Choose a partition of the labeled set \([n]\) uniformly among partitions into exactly \(k\) nonempty blocks. Write \(N_s\) for the number of blocks of size \(s\), and \(J=N_1\) for the number of singleton blocks. Let \(S(m,r)\) denote a Stirling number of the second kind and put

\[
\mu(m,r)=\frac{mS(m-1,r-1)}{S(m,r)}\qquad(m\ge r\ge1).
\]

For every integer \(2\le s\le n-k+1\), the expectation \(\mathbb E[N_s\mid K=k]\) is strictly positive, and

\[
\boxed{\frac{\operatorname{Cov}(J,N_s\mid K=k)}{\mathbb E[N_s\mid K=k]}=\mu(n-s,k-1)-\mu(n,k).}
\]

For \(k\ge3\), this normalized covariance is **strictly increasing as \(s\) increases**, is strictly negative at \(s=2\), and is strictly positive at \(s=n-k+1\). Thus the covariance has exactly one negative-to-positive transition (possibly with a single zero at the boundary between the two signs). For \(k=2\), all sizes \(2\le s\le n-2\) have the same strictly negative normalized covariance, and the size \(s=n-1\) has strictly positive covariance. In particular, at \((n,k)=(6,3)\), the signs at \(s=2,3,4\) are respectively negative, zero, positive.

The same theorem holds, without dependence on the total number of boxes, for the frequency-of-frequencies statistics of \(n\) independent uniform throws into \(q\) labeled boxes, conditional on exactly \(k\) boxes being occupied, whenever \(q\ge k\).

## Assumptions and scope

All set partitions are of a labeled finite set, blocks themselves are unlabeled, and the conditional measure with \(K=k\) is uniform. The nontrivial range \(n-k\ge2\) guarantees at least two feasible nonsingleton sizes. The Stirling conventions are \(S(0,0)=1\), \(S(m,0)=0\) for \(m>0\), and \(S(m,r)=0\) outside \(0\le r\le m\). The theorem concerns all feasible integer sizes \(s\in\{2,\ldots,n-k+1\}\), with no asymptotic limit or assumption about proportions.

## Proof

**1. Exact marked-block identity.** Given a partition with \(k\) blocks, count the ordered choices of one of its \(s\)-blocks. Choosing its \(s\) labels and partitioning the other labels into \(k-1\) blocks yields

\[
\mathbb E[N_s\mid K=k]=\binom ns\frac{S(n-s,k-1)}{S(n,k)}>0.
\]

After an \(s\)-block is marked with \(s\ge2\), removing it leaves a uniform partition of the remaining \(n-s\) labels into \(k-1\) blocks, without changing the singleton count. Also, marking a singleton shows

\[
\mathbb E[J\mid K=k]=\mu(n,k)=\frac{nS(n-1,k-1)}{S(n,k)}.
\]

Consequently, by the marked-block size-bias identity,

\[
\mathbb E[JN_s\mid K=k]=\mathbb E[N_s\mid K=k]\mu(n-s,k-1),
\]

which proves the boxed formula and every normalization, including \(s=n-k+1\).

**2. A strictly decreasing singleton-mean lemma.** For each fixed integer \(r\ge2\), the function \(m\mapsto\mu(m,r)\) is strictly decreasing on integers \(m\ge r\). Here is a self-contained proof. Define

\[
G(z)=\frac{e^z-1}{z}=\sum_{j\ge0}g_jz^j,
\qquad g_j=\frac1{(j+1)!},
\]

and let \(q_t=[z^t]G(z)^{r-1}\), \(p_t=[z^t]G(z)^r\). The coefficient form of the Stirling generating function gives, for \(m=r+t\),

\[
\mu(r+t,r)=r\frac{q_t}{p_t}.
\]

The positive sequence \((g_j)_{j\ge0}\) is strictly log-concave, since \(g_j^2>g_{j-1}g_{j+1}\) for every \(j\ge1\). Positive log-concave sequences remain log-concave under convolution, and strictness is preserved here: the upper-triangular Toeplitz matrix \(T(a)_{i,j}=a_{j-i}\) has nonnegative two-by-two minors for a log-concave sequence with no internal zeros; its product corresponds to convolution. For adjacent row indices and columns \(t,t+1\), the Cauchy–Binet expansion includes the strictly positive term formed by the same two intermediate columns, namely \((a_t^2-a_{t-1}a_{t+1})b_0^2\). Induction therefore shows that every \((q_t)\) is strictly log-concave at positive indices.

It follows that, for each \(a\ge1\), the ratio \(q_{t-a}/q_t\) is nondecreasing in \(t\) where defined; for \(a=1\) it is strictly increasing, with the ratio interpreted as zero when \(t<a\). Thus

\[
\frac{p_t}{q_t}=\sum_{a=0}^{t}g_a\frac{q_{t-a}}{q_t}
\]

is strictly increasing for \(t\ge0\), because the \(a=1\) term increases strictly and all coefficients \(g_a\) are positive. Its reciprocal, multiplied by \(r\), strictly decreases. This proves the lemma.

**3. The unique sign transition.** For \(k\ge3\), apply the lemma with \(r=k-1\): as \(s\) increases, \(n-s\) decreases, so \(\mu(n-s,k-1)-\mu(n,k)\) increases strictly. The deterministic excess identity

\[
\sum_{s=2}^{n-k+1}(s-1)N_s=n-k
\]

implies, after taking covariance with \(J\) at fixed \(K=k\),

\[
\sum_{s=2}^{n-k+1}(s-1)\mathbb E[N_s\mid K=k]
\bigl(\mu(n-s,k-1)-\mu(n,k)\bigr)=0.
\]

Every weight in this sum is positive. Since there are at least two terms and the parenthesized quantities increase strictly, the first must be negative and the last positive; at most one can be zero. The explicit value \(\mu(3,2)=\mu(6,3)=1\) establishes the attainable zero example.

For \(k=2\), \(\mu(m,1)=0\) for \(m\ge2\), while \(\mu(1,1)=1\). Moreover \(0<\mu(n,2)=n/(2^{n-1}-1)<1\) for \(n\ge4\). This yields the asserted negative plateau and positive final value.

**4. Uniform occupancy correspondence.** For \(n\) independent throws into \(q\) equally likely labeled boxes, each unlabeled partition of the \(n\) throw-indices into exactly \(k\) nonempty collision classes can be assigned injectively to occupied boxes in precisely \((q)_{\underline k}\) ways. The number does not depend on the partition. Conditional on \(k\) occupied boxes, the induced collision partition is therefore uniform, and its frequency counts agree with the block-size counts above.

## Verification

The included standard-library Python program `verify.py` checks the exact Stirling and marked-block formulas, strict normalized-covariance ordering, both endpoint signs, weighted covariance cancellation, and the two-block boundary across all integers \(4\le n\le100\). Separate restricted-growth-word enumeration of every labeled set partition through \(n=9\) independently verifies the covariance values. Enumeration of uniform labeled-box allocations through \(n=6\) independently checks the occupancy interpretation. All **499,367** assertions passed. The all-size conclusion rests on the proof, not these finite checks.

## Relationship to prior work

The Stirling counting framework and nonsingleton-block generating functions are classical. Bóna and Mező establish real-rootedness and related enumeration for partitions without singleton blocks; that statement does not establish a conditional covariance profile as the block size varies. Johnson and Goldschmidt discuss preservation of log-concavity on summation, a general mechanism compatible with the strict coefficient argument above. Barbour and Gnedin study joint asymptotics and covariance structures of occupancy counts for potentially nonuniform infinite box schemes; their regime and conclusions differ from the exact finite uniform-occupancy conditioning here. Existing unconditional relationships between richness and frequency counts do not determine conditional \(\operatorname{Cov}(N_1,N_s\mid K=k)\), and exact results for noncrossing partitions concern a different sampling measure. The contribution asserted here is the complete strict conditional normalized-covariance sign profile, with its exact tie allowance and uniform-box corollary, not the underlying Stirling enumeration or general log-concavity lemma.

## Limitations

The precise threshold size, although determined by exact Stirling ratios, need not have a simpler closed formula in \(n\) and \(k\). The theorem does not claim that an actual covariance's magnitude increases with block size; only the covariance divided by the strictly positive expected block count does. It does not cover nonuniform box probabilities, arbitrary weighted set partitions, or unconditional covariance signs. Historical priority, including possibly implicit coverage in older joint-moment literature, remains a risk.

## References

- M. Bóna and I. Mező, *Real Zeros and Partitions without singleton blocks*, arXiv:0705.2734v1 (first public 2007-05-18). https://arxiv.org/abs/0705.2734
- A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387v1 (first public 2008-09-25). https://arxiv.org/abs/0809.4387
- O. Johnson and C. Goldschmidt, *Preservation of log-concavity on summation*, ESAIM: Probability and Statistics (online publication 2006-05-03). https://www.cambridge.org/core/journals/esaim-probability-and-statistics/article/preservation-of-logconcavity-on-summation/91F47E323792C6CC5F1FFD89BED8E207
- W. M. Y. Goh and E. Schmutz, *Random Set Partitions*, SIAM Journal on Discrete Mathematics (1994). https://doi.org/10.1137/S0895480190186974
