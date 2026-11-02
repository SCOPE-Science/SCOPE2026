# Likelihood-ratio ordering of singleton abundance in uniform set partitions

## Finding

**Theorem (finite-sample total positivity).** Fix an integer \(n\ge2\). Choose uniformly a set partition \(\Pi\) of \([n]=\{1,\ldots,n\}\). Let \(K\) be its total number of blocks and \(S\) its number of singleton blocks. For \(0\le k,s\le n\), let \(w_n(k,s)\) denote the number of partitions with \((K,S)=(k,s)\), including the value zero for infeasible pairs. Then the entire joint count array is TP\(_2\):

\[
 w_n(k,s)w_n(\ell,t)\ \ge\ w_n(k,t)w_n(\ell,s)
 \quad\text{whenever }k<\ell\text{ and }s<t.
\]

Consequently, for every \(1\le k<\ell\le n\), the conditional distribution of \(S\) given \(K=\ell\) dominates that given \(K=k\) in **monotone likelihood-ratio order**. It strictly dominates in ordinary stochastic order. In particular, every pair of real-valued, strictly increasing functions \(f,g\) on the respective supports satisfies

\[
 \operatorname{Cov}(f(K),g(S))>0.
\]

The same conclusions hold when a partition receives any positive weight \(h(K)\) depending only on its total block count, because this rescales rows of the joint count array by positive factors. No claim is made about conditioning on the number of blocks of a different fixed size.

## Assumptions and scope

All partitions are of a *labeled* finite set; their blocks are unlabeled. Write \(A(N,r)\) for the number of partitions of \([N]\) into exactly \(r\) blocks of size at least two. Use \(A(0,0)=1\), \(A(N,r)=0\) for infeasible indices, and \(A(1,r)=0\) for all \(r\). Write \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) for Stirling numbers of the second kind, and \(B_n\) for the Bell number. The exact joint and conditional laws are

\[
 w_n(k,s)=\binom ns A(n-s,k-s),\qquad
 \Pr\{K=k,S=s\}=\frac{w_n(k,s)}{B_n},
\]

\[
 \Pr\{S=s\mid K=k\}=
 \frac{\binom ns A(n-s,k-s)}{\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}}.
\]

An equivalent bivariate exponential generating function, useful for independent coefficient checks, is

\[
\sum_{n\ge0}\sum_{k,s\ge0}w_n(k,s)u^k v^s\frac{z^n}{n!}
=\exp\!\bigl(uvz+u(e^z-1-z)\bigr).
\]

For \(1\le k<n\), the feasible singleton support is the complete integer interval \(\max(0,2k-n)\le s\le k-1\); for \(k=n\) it consists of \(s=n\). All \(K\)-strata \(1,\ldots,n\) have positive probability.

## Proof

**1. Exact coefficients.** Choose the \(s\) singleton elements and partition the other \(n-s\) elements into \(k-s\) nonsingleton blocks. This gives the formula for \(w_n(k,s)\). In particular, its nonzero support has precisely the stated intervals.

**2. An interlacing-to-likelihood-ratio lemma.** Define \(P_N(x)=\sum_{r\ge0}A(N,r)x^r\). For each \(N\ge2\), Bóna and Mező [1, Theorem 1] proved that \(P_N\) has simple nonpositive real zeros, and the negative zeros of \(P_N\) lie strictly to the right of the corresponding zeros of \(P_{N-1}\), with an additional more-negative zero when its degree rises. Both polynomials have a zero at the origin for \(N\ge2\). The base cases \(P_2(x)=P_3(x)=x\) are immediate.

For a nonzero polynomial \(P_N\), its normalized coefficients are the distribution of \(1+\sum_j Z_j\), where the \(Z_j\) are independent Bernoulli variables with parameters \(1/(1+\lambda_j)\) and the \(-\lambda_j\) are its negative roots. Matching roots by descending order thus increases each Bernoulli parameter as \(N\) increases, and a degree increase adds one Bernoulli variable with a positive parameter.

Increasing one Bernoulli parameter \(p\) to \(q\), with \(q\ge p\), increases the resulting Poisson-binomial sum in likelihood-ratio order. Indeed, if \(h_j\) is the mass function of the sum of all *other* Bernoullis, then the old and new mass functions \(F_p,F_q\) satisfy

\[
 F_q(j+1)F_p(j)-F_q(j)F_p(j+1)
 =(q-p)(h_j^2-h_{j-1}h_{j+1})\ge0,
\]

because every Poisson-binomial mass function is log-concave. Adding a new Bernoulli is the same comparison against parameter zero. Repeated replacement, and transitivity of likelihood-ratio order, show that for \(N\ge4\) and every integer \(r\),

\[
 A(N-1,r)A(N-2,r-1)
 \ge A(N-1,r-1)A(N-2,r).
 \tag{1}
\]

The cases \(N=2,3\), in which one relevant polynomial is zero, are treated directly below. The coefficients also obey Newton's inequalities: with \(a_r=A(N-1,r)\),

\[
 r a_r^2\ge(r+1)a_{r-1}a_{r+1}
 \quad (r\ge0).
 \tag{2}
\]

Here coefficients outside the range vanish; for interior indices, (2) is weaker than the usual ultra-log-concavity inequality for the coefficients of a real-rooted polynomial.

**3. Every adjacent minor.** Fix \(0\le k,s<n\) and put \(N=n-s\) and \(r=k-s\). For \(N\ge2\), divide the adjacent \((k,s)\)-minor by its positive factor \(\binom ns\binom n{s+1}\). What remains is

\[
\Delta=A(N,r)A(N-1,r)-A(N,r+1)A(N-1,r-1).
\]

The associated Stirling recurrence [1, equation (4)] is

\[
 A(N,r)=rA(N-1,r)+(N-1)A(N-2,r-1).
\]

For \(N\ge4\), set \(a_j=A(N-1,j)\) and \(b_j=A(N-2,j)\). Substitution gives the **exact decomposition**

\[
\Delta=
\underbrace{r a_r^2-(r+1)a_{r-1}a_{r+1}}_{\ge0\text{ by (2)}}
+(N-1)\underbrace{(b_{r-1}a_r-b_ra_{r-1})}_{\ge0\text{ by (1)}}.
\]

Thus \(\Delta\ge0\). For \(N=2\), the factor \(A(N-1,\cdot)\) is identically zero; for \(N=3\), the second term vanishes and Newton's term is nonnegative. If \(N=1\), the first row's relevant coefficients vanish; if \(N=0\), the only possibly nonzero entry is \((k,s)=(n,n)\), so adjacent minors are again nonnegative. This covers every boundary and every infeasible index without division by zero.

**4. All minors and strict consequences.** For each \(k<n\), the nonzero \(s\)-support of \(w_n(k,s)\) is an interval, and both endpoints are nondecreasing with \(k\). Adjacent-minor nonnegativity therefore makes \(w_n(k+1,s)/w_n(k,s)\) nondecreasing over common support, with the prescribed zero/infinity behavior at the moving endpoints. The adjacent row laws are in likelihood-ratio order. Transitivity extends the order to arbitrary \(k<\ell\), equivalently giving every displayed TP\(_2\) minor.

Strict ordinary stochastic ordering follows because the largest feasible singleton count is \(k-1\) for \(k<n\), and \(n\) for \(k=n\): each larger stratum puts positive mass strictly above the previous stratum's upper endpoint. Consequently \(\mathbb E[g(S)\mid K=k]\) increases *strictly* with \(k\) for strictly increasing \(g\). The covariance identity

\[
\operatorname{Cov}(f(K),g(S))
=\operatorname{Cov}\bigl(f(K),\mathbb E[g(S)\mid K]\bigr)
\]

is then positive by the pairwise-difference expression for covariance, since \(K\) is nondegenerate. Multiplying every row of \(w_n\) by any positive \(h(k)\) leaves all minor signs unchanged, which proves the weighted extension. \(\square\)

## Verification

The accompanying standalone \(\texttt{verify.py}\) independently enumerates all labeled set partitions for \(0\le n\le8\), checks exact coefficients and Stirling marginals, verifies all adjacent TP\(_2\) minors for \(n\le75\), and tests all (not merely adjacent) minors for \(n\le22\), using exact integers. It completed **467,463 exact assertions**. The verification program needs only Python's standard library; run it as \(\texttt{python3 verify.py}\). The infinite statements are proved above using the stated published interlacing theorem and elementary probabilistic inequalities, not inferred from the finite tests.

For illustration at \(n=6\), the unnormalized singleton-count rows are \((w_6(2,0),w_6(2,1))=(25,6)\) and \((w_6(3,0),w_6(3,1),w_6(3,2))=(15,60,15)\). Their common-support adjacent minor is \(25\cdot60-6\cdot15=1410>0\).

## Relationship to prior work

Timashev [2] studied the count of blocks of fixed size in a uniformly sampled partition conditional on the total block count. His exact-count framework and asymptotic Poisson/normal laws address the same two observables, but do not assert finite-sample TP\(_2\) or likelihood-ratio comparisons **between** distinct conditioned block counts. Bóna and Mező [1] proved the recurrence, real-rootedness and precise root interlacing of the *nonsingleton* block-count polynomial. These are explicitly used as known inputs; neither real-rootedness alone nor Timashev's count formulas state the joint singleton-versus-total-block TP\(_2\) conclusion. Pitman [3] studies probabilistic representations of uniform set partitions, providing broader background rather than this conditional ordering. The contribution claimed here is the bivariate TP\(_2\) synthesis and its distributional consequences, **not** the underlying counting formula, recurrence, real-rootedness, or generic Newton inequalities.

## Limitations

Originality is assessed against the inspected literature and searched mathematical records, not established as global uniqueness; implicit coverage in other work on total positivity or conditional occupancies remains possible. The argument is restricted to singleton blocks and distributions whose weights depend only on the total number of blocks; it does not assert the analogous statement for arbitrary fixed-size block counts or nonexchangeable element weights. The underlying interlacing theorem [1] is invoked as an established, published theorem, not independently re-proved. The exhaustive checks cover only the finite sizes stated and provide corroboration rather than certification of the infinite theorem.

## References

[1] M. Bóna and I. Mező, *Real Zeros and Partitions without singleton blocks*, arXiv:0705.2734, first public version May 18, 2007, Theorem 1 and equation (4). https://arxiv.org/abs/0705.2734 ; https://arxiv.org/pdf/0705.2734.

[2] A. N. Timashev, *Random partitions of sets with a known number of blocks*, Diskretnaya Matematika 15 (2003), 138–148; English translation in Discrete Mathematics and Applications 13 (2003), 307–317. https://www.mathnet.ru/eng/dm201 ; DOI:10.4213/dm201.

[3] J. Pitman, *Some Probabilistic Aspects of Set Partitions*, American Mathematical Monthly 104 (1997), 201–209. https://www.stat.berkeley.edu/~pitman/452.pdf.
