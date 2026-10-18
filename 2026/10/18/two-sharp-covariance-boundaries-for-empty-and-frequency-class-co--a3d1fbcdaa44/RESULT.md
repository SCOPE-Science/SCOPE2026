# Two sharp covariance boundaries for empty and frequency-class counts in symmetric Pólya sampling

## Finding

Take a symmetric unit-reinforcement Pólya urn with \(d\ge3\) colors, initially one ball of each color. After \(n\ge1\) draws, let \(X_i\) count draws of color \(i\). For every integer \(1\le r\le n\), put
\[
Z_i=\mathbf{1}_{\{X_i=0\}},\qquad R_{i,r}=\mathbf{1}_{\{X_i=r\}},\qquad K_0=\sum_{i=1}^d Z_i,\qquad K_r=\sum_{i=1}^d R_{i,r}.
\]
Thus \(K_0\) is the number of unobserved colors and \(K_r\) is the number observed exactly \(r\) times. Write
\[
u=\frac{d-1}{n+d-1},\qquad v_r=\frac{\binom{n-r+d-2}{d-2}}{\binom{n+d-1}{d-1}}.
\]
These are respectively \(\Pr(X_i=0)\) and \(\Pr(X_j=r)\). For distinct colors \(i\ne j\), the **local** covariance has the exact expression
\[
\boxed{\operatorname{Cov}(Z_i,R_{j,r})
=uv_r\frac{(d-1)r-n}{(d-1)(d+n-r-2)}.}\tag{1}
\]
The **aggregate** covariance is instead
\[
\boxed{\operatorname{Cov}(K_0,K_r)
=d\,uv_r\frac{d(r-1)-2(n-1)}{d+n-r-2}.}\tag{2}
\]
All factors outside the displayed linear numerators are positive. Thus (1) is negative, zero, or positive exactly as \((d-1)r\) is less than, equal to, or greater than \(n\); (2) is negative, zero, or positive exactly as \(d(r-1)\) is less than, equal to, or greater than \(2(n-1)\). Both statements include equality cases.

The two sign boundaries are strictly ordered:
\[
\boxed{\frac{n}{d-1}<1+\frac{2(n-1)}d,\qquad
1+\frac{2(n-1)}d-\frac{n}{d-1}=\frac{(d-2)(d+n-1)}{d(d-1)}.}\tag{3}
\]
In particular, positive aggregate covariance forces positive local covariance, but the reverse implication fails. For \((d,n,r)=(5,4,2)\), the local covariance is \(1/70\) while the aggregate covariance is \(-1/14\). For \((4,3,2)\), the local covariance is \(1/40\) while the aggregate covariance vanishes; for \((3,4,2)\), the local covariance vanishes while the aggregate covariance is \(-1/5\). There are infinitely many exact aggregate-zero cases: take any \(d\ge3\), \(r\ge2\) with \(d(r-1)\) even and \(n=1+d(r-1)/2\).

## Assumptions and scope

Each draw returns the selected ball together with one additional ball of the selected color. The initial ball count equals one for each of \(d\) colors, and the sampling stops after the fixed integer \(n\). The random variables refer to draw counts, not to the final urn inventory. The theorem covers all integers \(d\ge3\), \(n\ge1\), \(1\le r\le n\), with \(i\ne j\) in (1). There is no large-sample or asymptotic hypothesis.

The distinction between *local* and *aggregate* covariance is essential: because an empty color cannot simultaneously belong to a positive-frequency class, the diagonal terms in the aggregate contribute a negative covariance absent from (1). A zero covariance is not asserted to imply independence.

## Proof

For any vector \((x_1,\ldots,x_d)\) of nonnegative integers totaling \(n\), every particular draw sequence with those counts has probability
\[
\frac{\prod_{i=1}^d (1)_{x_i}}{(d)_n}=\frac{\prod_{i=1}^d x_i!}{(d)_n},
\]
where \((a)_k=a(a+1)\cdots(a+k-1)\) is the rising factorial (and \((a)_0=1\)). There are \(n!/\prod_i x_i!\) such sequences, so the vector has probability \(n!/(d)_n=\binom{n+d-1}{d-1}^{-1}\). Consequently \((X_1,\ldots,X_d)\) is uniform among the weak compositions of \(n\) into \(d\) ordered parts.

Stars-and-bars counting gives
\[
\Pr(X_i=0)=\frac{\binom{n+d-2}{d-2}}{\binom{n+d-1}{d-1}}=u,
\quad \Pr(X_j=r)=v_r,
\]
and for two distinct colors,
\[
w_r:=\Pr(X_i=0,X_j=r)
=\frac{\binom{n-r+d-3}{d-3}}{\binom{n+d-1}{d-1}}.
\]
All binomial coefficients have nonnegative upper arguments under the hypotheses. Direct cancellation yields
\[
\frac{w_r}{uv_r}=
\frac{(d-2)(n+d-1)}{(d-1)(d+n-r-2)}.
\]
Subtracting one from this ratio gives
\[
\frac{w_r}{uv_r}-1
=\frac{(d-1)r-n}{(d-1)(d+n-r-2)},
\]
proving (1).

For each color \(i\), \(Z_iR_{i,r}=0\) because \(r\ge1\). For \(i\ne j\), \(\mathbb E[Z_iR_{j,r}]=w_r\). Exchangeability therefore gives
\[
\mathbb E[K_0K_r]=d(d-1)w_r,
\quad \mathbb E K_0=du,
\quad \mathbb E K_r=dv_r.
\]
It follows that
\[
\begin{aligned}
\operatorname{Cov}(K_0,K_r)
&=d(d-1)w_r-d^2uv_r\\
&=d\,uv_r\left(\frac{(d-2)(d+n-1)}{d+n-r-2}-d\right)\\
&=d\,uv_r\frac{d(r-1)-2(n-1)}{d+n-r-2},
\end{aligned}
\]
which is (2). Since \(d+n-r-2\ge d-2>0\), all asserted signs follow without approximation. Equation (3) is an exact subtraction. The stated rational examples follow by substitution; the infinite equality family follows from the numerator of (2) and satisfies \(r\le n\) automatically.

## Verification

The accompanying standard-library-only `verify.py` independently enumerates all uniform weak compositions for \(3\le d\le8\) and \(1\le n\le10\). It computes both covariances as exact rational numbers for every \(1\le r\le n\) and checks (1) and (2), including their zero cases. It additionally verifies the Pólya-to-uniform-compositions correspondence through exact probability recursion for small urns and checks the displayed rational witnesses. The checker reports 330 all-parameter covariance comparisons. This finite verification supports reproducibility; the general theorem is the combinatorial proof above.

## Relationship to prior work

The uniform weak-composition probability law and empty-urn marginal moments are established background, not claimed as new. Shuldiner and Oldford explicitly treat indistinguishable balls allocated uniformly among labeled urns and derive joint empty-urn indicators and moments of the number empty. Their accessible Section 4.4 does not give a joint event \(\{X_i=0,X_j=r\}\) for positive \(r\), or the two sharp sign boundaries and contradictory-sign examples (1)–(3).

For independent balls allocated uniformly to boxes, the published result *A one-switch covariance law for occupancy richness and frequency counts* gives a different complete sign rule for \(\operatorname{Cov}(K,K_r)\) with \(K\) counting occupied boxes. That model assigns equal probability to ball-by-ball placements, whereas the present Pólya urn assigns equal probability to weak-composition vectors. Its strict no-zero sign theorem therefore does not imply the present equality-permitting rule; conversely, neither result covers the other's probability law.

The general Dirichlet-multinomial/Pólya urn probability formula is classical. The claim here is only the exact local-versus-aggregate covariance comparison and its exhaustive finite-parameter sign classification under unit symmetric reinforcement.

## Limitations

The simple linear boundaries rely on one initial ball per color and unit reinforcement. They do not assert the same thresholds for other Dirichlet concentration vectors, unequal initial colors, or independent-ball occupancy. These covariance signs do not provide monotone stochastic association or independence. The count identities and underlying distribution are classical; novelty is assessed for the two simultaneous sign classifications and their strict ordering. A historically equivalent identity under other occupancy terminology could remain undiscovered.

## References

1. P. Shuldiner and R. W. Oldford, “Bernoulli Sums: The only random variables that count,” arXiv:2110.02363, first public version 2021-10-05; Section 4.4, “The empty urns problem.” https://arxiv.org/html/2110.02363v2
2. “A one-switch covariance law for occupancy richness and frequency counts,” publicly available mathematical record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813
3. “Rigorous decorrelation of part count and maximum in uniform compositions,” publicly available mathematical record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-rigorous-decorrelation-of-part-count-and-maximum-in-uniform-comp--0ee24a72cd31
