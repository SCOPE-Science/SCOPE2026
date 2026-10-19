# Rank-one co-clustering covariance and a sharp size threshold for Ewens–Pitman partitions

## Finding

Let \(n\ge 2\), \(0\le\alpha<1\), and \(\theta> -\alpha\). Let \(\Pi_n\) have the two-parameter Ewens–Pitman exchangeable partition law. For an integer \(1\le r\le n\), let \(T_r\) be its number of blocks of size \(r\), and let \(Y_{ij}=\mathbf 1\{i,j\text{ belong to the same block}\}\) for distinct labels \(i,j\). For arbitrary fixed real edge weights \(w_{ij}\) on unordered label pairs, put \(C_w=\sum_{i<j}w_{ij}Y_{ij}\), and write \(W=\sum_{i<j}w_{ij}\).

Define
\[
p=\frac{1-\alpha}{\theta+1},\qquad q=\frac{1-\alpha}{\theta+\alpha+1},\qquad
F_{n}(r)=r(r-1)+q(n-r)(n-r-1)-p n(n-1).
\]
Then for every such \(n,\alpha,\theta,r\) and every deterministic weight array,
\[
\boxed{\operatorname{Cov}(C_w,T_r)=\frac{W\,\mathbb E T_r}{n(n-1)}F_n(r)},\qquad
\mathbb E T_r=\binom nr\frac{(1-\alpha)_{r-1}(\theta+\alpha)_{n-r}}{(\theta+1)_{n-1}}.
\]
Here \((x)_j=x(x+1)\cdots(x+j-1)\), with \((x)_0=1\). Thus the entire cross-covariance matrix between the pair co-clustering indicators and the block-size frequency vector has rank one for \(n\ge2\): all pair rows coincide, and they are not all zero. In particular, all zero-sum edge contrasts are uncorrelated with every block-size count.

There is exactly one real threshold \(R_n\in(1,n)\) such that, for every integer \(r\in[1,n]\), \(F_n(r)<0\) below \(R_n\), \(F_n(r)=0\) at \(R_n\), and \(F_n(r)>0\) above \(R_n\). The threshold is
\[
\boxed{R_n=\frac{1+(2n-1)q+\sqrt{[1+(2n-1)q]^2+4(1+q)n(n-1)(p-q)}}{2(1+q)}}.
\]
For positive total edge weight \(W\), these are exactly the covariance signs; for negative \(W\), the signs reverse. For fixed \(\alpha,\theta\),
\[
\frac{R_n}{n}\longrightarrow\frac{q+\sqrt{p(1+q)-q}}{1+q}.
\]
In the Ewens case \(\alpha=0\), the threshold simplifies to \(R_n=(2n+\theta)/(\theta+2)\). In particular, the uniform-random-permutation-cycle case \(\theta=1\) has exact threshold \((2n+1)/3\).

## Assumptions and scope

The pair indices are distinct and unordered, the weights deterministic real numbers, and the partition is exchangeable with EPPF
\[
\mathbb P\{\Pi_n=\{B_1,\ldots,B_k\}\}=
\frac{(\theta+\alpha)_{k-1;\alpha}}{(\theta+1)_{n-1}}
\prod_{j=1}^{k}(1-\alpha)_{|B_j|-1},
\qquad (x)_{j;\alpha}=\prod_{h=0}^{j-1}(x+h\alpha).
\]
The parameter domain guarantees strict positivity of all block-size probabilities and \(0<q\le p<1\). The statement concerns mixed *covariances* only; it does not claim independence between weighted graph scores and block counts, nor a distribution for either statistic. For an empty graph or a signed weight array with \(W=0\), the stated mixed covariances all vanish.

## Proof

**Pair probability.** Sampling consistency of the EPPF on two labels gives \(\mathbb EY_{ij}=p=(1-\alpha)/(\theta+1)\).

**Mark one block.** Fix an \(r\)-subset \(B\) of the labels. By summing the EPPF over all partitions of its complement, the event that \(B\) is *exactly one block* has probability
\[
Q_{n,r}=\frac{(1-\alpha)_{r-1}(\theta+\alpha)_{n-r}}{(\theta+1)_{n-1}}.
\]
Conditional on this event, the partition of the \(n-r\) remaining labels has the Ewens–Pitman law with parameters \((\alpha,\theta+\alpha)\). This follows directly by factoring the EPPF: if the remainder has \(k\) blocks, the numerator factor \((\theta+\alpha)_{k;\alpha}\) divides into \(\theta+\alpha\) times \((\theta+2\alpha)_{k-1;\alpha}\), yielding the EPPF for the shifted parameter. The statement is also valid for a remainder of size zero or one, for which the relevant pair probability is never used.

**Mixed moment.** Since \(T_r=\sum_{|B|=r}\mathbf1\{B\text{ is a block}\}\), its expectation is \(\binom nr Q_{n,r}\). In the size-biased marking induced by this sum, the marked vertex set is uniform among the \(r\)-subsets. For any fixed pair \(\{i,j\}\), the chance that both labels lie in the marked block is \(r(r-1)/(n(n-1))\); the chance both lie outside is \((n-r)(n-r-1)/(n(n-1))\). The within-remainder co-block probability is \(q\); a pair split between marked block and remainder cannot co-cluster. Consequently,
\[
\mathbb E[Y_{ij}T_r]=\frac{\mathbb ET_r}{n(n-1)}\left[r(r-1)+q(n-r)(n-r-1)\right].
\]
Subtracting \(p\,\mathbb ET_r\) and summing with arbitrary weights proves the covariance formula. Because every row of the pair-by-size mixed-covariance matrix is identical, its rank is at most one. It is exactly one since its \(r=1\) entry is strictly negative and \(\mathbb ET_1>0\).

**Unique sign change.** The polynomial \(F_n(r)\) is quadratic with leading coefficient \(1+q>0\). Its value at zero is \(n(n-1)(q-p)\le0\), at one it equals \((n-1)[(n-2)q-np]<0\), and at \(n\) it equals \(n(n-1)(1-p)>0\). Hence it has exactly one positive root in \((1,n)\); any other root is nonpositive. The quadratic formula gives \(R_n\) above. Taking \(r=nx\), dividing \(F_n(nx)\) by \(n^2\), and solving \(x^2+q(1-x)^2=p\) proves the limit. Setting \(q=p=1/(\theta+1)\) yields the Ewens simplification.

## Verification

Run `python3 check.py` using only the Python standard library. The checker enumerates every set partition for \(2\le n\le8\), evaluates exact rational EPPF probabilities for five parameter pairs, and checks normalization, all block-frequency means, and all mixed covariance formulas for path, star, cycle, and complete graph edge sets. It reports 1,015 exact comparisons over 35 complete finite probability laws. Exact symbolic expansion separately verifies the quadratic coefficient, endpoint signs, and the first difference \(F_n(r+1)-F_n(r)=2[(1+q)r-q(n-1)]\). The proof, not finite enumeration, establishes the theorem for all admitted parameters and sizes.

## Relationship to prior work

The two-parameter EPPF and the use of block-size frequencies are classical; Gnedin and Pitman (2004) provide the EPPF and broader Gibbs-partition theory. Chern, Diaconis, Kane, and Rhoades (2013, 2015) examine levels and pattern statistics of **uniform Bell-distributed set partitions**, not the size-frequency mixed covariances of the Ewens–Pitman law. The present calculation evaluates the cross-covariance of every co-clustering edge statistic with every block-size frequency and extracts the exact unique sign transition. It does not claim a new exchangeable partition distribution or deletion principle.

## Limitations

The result covers \(0\le\alpha<1\) and \(\theta>-\alpha\), not arbitrary exchangeable Gibbs partitions, nonexchangeable partitions, or partition-dependent edge weights. It proves covariance identities and signs only, not stochastic monotonicity or conditional independence. Broad EPPF machinery makes implicit prior coverage a genuine historical-priority risk; the literature comparison has not been independently audited. All cited sources are prior to the archival cutoff.

## References

1. J. Pitman and M. Yor, *The two-parameter Poisson–Dirichlet distribution derived from a stable subordinator*, University of California, Berkeley Technical Report 433 (1995), https://statistics.berkeley.edu/tech-reports/433 .
2. A. Gnedin and J. Pitman, *Exchangeable Gibbs partitions and Stirling triangles*, arXiv:math/0412494 (first submitted 2004-12-25), https://arxiv.org/abs/math/0412494 .
3. B. Chern, P. Diaconis, D. M. Kane, and R. C. Rhoades, *Closed expressions for averages of set partition statistics*, arXiv:1304.4309 (first submitted 2013-04-16), https://arxiv.org/abs/1304.4309 .
4. B. Chern, P. Diaconis, D. M. Kane, and R. C. Rhoades, *Central Limit Theorems for some Set Partition Statistics*, arXiv:1502.00938 (first submitted 2015-02-03), https://arxiv.org/abs/1502.00938 .
