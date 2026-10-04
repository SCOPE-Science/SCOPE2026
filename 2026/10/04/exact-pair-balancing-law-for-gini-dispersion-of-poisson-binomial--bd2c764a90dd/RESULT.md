# Exact pair-balancing law for Gini dispersion of Poisson-binomial sums

## Finding

Let
\[
W=\sum_{i=1}^nX_i
\]
be a sum of independent Bernoulli variables with success probabilities \(p_1,\ldots,p_n\), and let \(W'\) be an independent copy. Define
\[
\Delta(W)=\mathbb E|W-W'|.
\]
Fix all parameters except \(p,q\), put
\[
s=p+q,\qquad r=pq,
\]
and replace them by a feasible pair \(\tilde p,\tilde q\) with the same sum and product \(\tilde r=\tilde p\tilde q\). If \(A\) is the sum of the remaining trials, \(A'\) an independent copy, and
\[
c_0=\Pr(A-A'=0),\qquad c_1=\Pr(A-A'=1),
\]
then
\[
\boxed{\Delta(\tilde W)-\Delta(W)
=
4(\tilde r-r)\left[(c_0-c_1)(s-r-\tilde r)+c_1\right].}
\tag{1}
\]
Every nontrivial balancing step has \(\tilde r>r\), and (1) is strictly positive. Hence \(\Delta\) is strictly Schur-concave on each fixed-mean parameter slice.

If
\[
\mu=\sum_i p_i,\qquad m=\lfloor\mu\rfloor,\qquad \delta=\mu-m,
\]
then the complete attainable range is
\[
\boxed{
2\delta(1-\delta)
\le\Delta(W)\le
\Delta\!\left(\operatorname{Bin}\!\left(n,\frac{\mu}{n}\right)\right).
}
\tag{2}
\]
The lower endpoint is attained by \(m\) deterministic successes, one Bernoulli(\(\delta\)) trial when \(\delta>0\), and deterministic failures. The upper endpoint is attained by equal probabilities \(\mu/n\).

For the upper endpoint,
\[
\Delta(\operatorname{Bin}(n,p))
=
2\sum_{k=0}^{n-1}F_{n,p}(k)\bigl(1-F_{n,p}(k)\bigr),
\tag{3}
\]
where \(F_{n,p}\) is the binomial distribution function. Every value between the two endpoints in (2) is attained.

## Assumptions and scope

The summands are mutually independent Bernoulli variables. Their parameters may be unequal, but the total mean is held fixed.

The functional is Gini's mean difference, equivalently twice the second \(L\)-moment. No analogous exact transfer law is asserted for arbitrary dispersion functionals.

## Proof

Let \(U=B_p+B_q\), and let \(U'\) be an independent copy. For fixed \(s=p+q\) and \(r=pq\),
\[
\Pr(U=0)=1-s+r,\qquad \Pr(U=1)=s-2r,\qquad \Pr(U=2)=r.
\]
For \(V=U-U'\),
\[
\Pr(V=\pm2)=r(r-s+1),
\]
\[
\Pr(V=\pm1)=-(2r-s)(2r-s+1),
\]
and
\[
\Pr(V=0)=1-2s+2s^2+2r-6rs+6r^2.
\tag{4}
\]

Set \(Z=A-A'\), which is symmetric and integer-valued, and \(H_0=\mathbb E|Z|\). For every integer \(z\),
\[
|z+1|+|z-1|=2|z|+2\mathbf 1_{\{z=0\}},
\]
and
\[
|z+2|+|z-2|
=
2|z|+4\mathbf 1_{\{z=0\}}+2\mathbf 1_{\{|z|=1\}}.
\]
Therefore
\[
\mathbb E(|Z+1|+|Z-1|)=2H_0+2c_0,
\]
and
\[
\mathbb E(|Z+2|+|Z-2|)=2H_0+4c_0+4c_1.
\]
Substitution into \(\mathbb E|Z+V|\) gives, for fixed \(s\),
\[
\frac{d}{dr}\Delta
=
4\left[(c_0-c_1)(s-2r)+c_1\right].
\tag{5}
\]
Integrating (5) from \(r\) to \(\tilde r\) proves (1).

If \(a_k=\Pr(A=k)\), then
\[
c_0=\sum_k a_k^2,\qquad c_1=\sum_k a_ka_{k+1}.
\]
Cauchy--Schwarz gives \(c_1\le c_0\). Also each feasible product is at most \(s^2/4\), so
\[
r+\tilde r\le\frac{s^2}{2}\le s.
\]
Thus the bracket in (1) is nonnegative and is strictly positive for a genuine balancing step. Iterating pair-balancing transformations gives strict Schur-concavity.

The equal vector gives the maximum in (2). The most unequal feasible vector has \(m\) ones, one \(\delta\), and zeros; its sum is a deterministic shift of a Bernoulli(\(\delta\)) variable, whose two-copy absolute difference has expectation \(2\delta(1-\delta)\). This gives the minimum.

The fixed-mean parameter polytope is connected and \(\Delta\) is continuous, so its image is the full interval between its extrema.

For any integer-valued \(Y\) with distribution function \(F\),
\[
\mathbb E|Y-Y'|=2\sum_{k\in\mathbb Z}F(k)(1-F(k)).
\]
Applied to the binomial law, this yields (3).

## Verification

An exact-rational checker accompanies the theorem. It computes Poisson-binomial mass functions by convolution, evaluates \(\Delta\) directly, checks (1) under rational fixed-sum pair balancing, verifies \(c_1\le c_0\) and strict monotonicity, replays (3), and tests the endpoint theorem on exhaustive small rational grids.

Finite enumeration is supplementary; the universal result follows from the symbolic proof.

## Relationship to prior work

Hoeffding's fixed-mean theory for the number of successes gives extrema for expectations of a fixed scalar function of the sum. Wang later showed, among other Poisson-binomial results, that variance increases as success probabilities become more homogeneous.

Gini's mean difference is a standard robust scale functional. Čiginas and Pumputis analyze it in finite-population sampling, and work on discrete Gini mean differences gives formulas for several named one-parameter laws.

The present theorem concerns the two-copy functional \(\mathbb E|W-W'|\). Formula (1) gives the exact gain from every pair-balancing step through two adjacent autocorrelations of the remaining sum, and yields the full fixed-mean interval. Targeted searches did not locate this identity.

## Limitations

The theorem assumes mutual independence of the Bernoulli summands.

No quantitative global stability remainder, beyond the exact local transfer identity, is claimed.

The originality search was targeted; an equivalent identity may exist in older stochastic-order or reliability literature under different terminology.

## References

1. A. Čiginas and D. Pumputis, “Gini's mean difference and variance as measures of finite populations scales,” arXiv:1406.2275, first submitted 2014-06-09.
2. W. Hoeffding, “On the Distribution of the Number of Successes in Independent Trials,” *The Annals of Mathematical Statistics* 27 (1956), 713--721. DOI: 10.1214/aoms/1177728178.
3. Y. H. Wang, “On the Number of Successes in Independent Trials,” *Statistica Sinica* 3 (1993), 295--312.
4. G. Manca, A. M. D'Uggento, and S. Girone, “The mean difference of discrete distribution models,” 2015.
