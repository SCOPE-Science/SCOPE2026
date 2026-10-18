# Exact short-chord/crossing transfer and independent Poisson–Gaussian limits

## Finding

For a uniform perfect matching of the cyclically ordered labeled points \(1,\ldots,2n\), let \(S_n\) count chords joining cyclically consecutive endpoints and let \(X_n\) count pairs of crossing chords. For every integer \(n\ge2\) and \(0\le k\le n\), write \((x)_{\underline k}=x(x-1)\cdots(x-k+1)\), with the empty product equal to one, and set
\[
 a_{n,k}=\frac{2n}{2n-k}\frac{2^k(n)_{\underline k}}{(2n)_{\underline k}},\qquad
 F_m(z)=\mathbb E[z^{X_m}],\quad F_0(z)=F_1(z)=1.
\]
Then, **as an identity of polynomials in the complex variable \(z\)**,
\[
 \boxed{\mathbb E[(S_n)_{\underline k}z^{X_n}]=a_{n,k}F_{n-k}(z).}
\]
Equivalently, the complete bivariate probability-generating polynomial is
\[
 \boxed{\mathbb E[u^{S_n}z^{X_n}]=\sum_{k=0}^{n}\frac{a_{n,k}}{k!}(u-1)^k F_{n-k}(z).}
\]
In particular, the crossing-count generating polynomial for diagrams with no simple chords is
\[
 \mathbb E[\mathbf1_{\{S_n=0\}}z^{X_n}]
 =\sum_{k=0}^{n}\frac{(-1)^k a_{n,k}}{k!}F_{n-k}(z).
\]
More generally, for every \(0\le s\le n\), the exact joint crossing-count polynomial for \(S_n=s\) equals
\[
 \mathbb E[\mathbf1_{\{S_n=s\}}z^{X_n}]
 =\frac1{s!}\sum_{j=0}^{n-s}\frac{(-1)^j a_{n,s+j}}{j!}F_{n-s-j}(z).
\]
Thus the entire joint distribution is determined by the one-variable crossing enumerators at smaller matching sizes. No limiting approximation is needed for these finite-size assertions.

A distributional consequence is **independent mixed-scale fluctuations**:
\[
 \boxed{\left(S_n,\frac{X_n-\mu_n}{\sigma_n}\right)
 \xrightarrow{d}(P,Z),\qquad
 P\sim\operatorname{Poisson}(1),\quad Z\sim N(0,1),\quad P\perp Z,}
\]
where \(\mu_n=n(n-1)/6\), \(\sigma_n^2=n(n-1)(n+3)/45\). The separate marginal crossing limit is classical; the statement here is their joint asymptotic independence.

The transfer identity also yields, exactly for every \(n\ge2\),
\[
 \mathbb ES_n=\frac{2n}{2n-1},\quad
 \operatorname{Var}(S_n)=\frac{4n(n-1)}{(2n-1)^2},\quad
 \operatorname{Cov}(S_n,X_n)=-\frac{2n(n-1)}{3(2n-1)},\quad
 \operatorname{Corr}(S_n,X_n)=-\sqrt{\frac5{n+3}}.
\]
The covariance is included as a consistency consequence, **not claimed as a new covariance formula**.

## Assumptions and scope

The \(2n\) endpoints are fixed distinct labeled positions in one cyclic order; every perfect matching occurs with probability \(1/(2n-1)!!\). A chord is *simple* precisely when its endpoints are adjacent in that cyclic order, including \(\{1,2n\}\). Two chords cross precisely when their four distinct endpoints alternate around the circle. Crossings are unordered pairs of chords. The finite transfer applies for every complex \(u,z\) without convergence issues. The integer range \(n\ge2\) is essential to avoid identifying the two parallel cyclic adjacencies in the two-vertex boundary; zero and one chord are used only as residual base cases.

## Proof

**1. Count prescribed simple chords.** The potential simple chords form the edge set of the cycle \(C_{2n}\). Choosing \(k\) that can simultaneously occur means choosing a matching of size \(k\) in this boundary cycle. There are
\[
 M_{n,k}=\frac{2n}{2n-k}\binom{2n-k}{k},\qquad 0\le k\le n.
\]
For \(k=0\), both sides equal one. For \(k\ge1\), orient the boundary clockwise and cyclically list selected edges; the \(k\) positive gaps of nonselected edges sum to \(2n-k\). There are \(\binom{2n-k-1}{k-1}\) such positive gap compositions, and \(2n/k\) choices of anchored starting edge, yielding the expression above. This includes the two alternating perfect matchings when \(k=n\).

**2. Delete the marked chords.** Fix any feasible set \(D\) of \(k\) selected consecutive-endpoint chords. Its occurrence probability is
\[
 \Pr(D\subseteq\mathcal M_n)=\frac{(2n-2k-1)!!}{(2n-1)!!},
\]
with \((-1)!!=1\) for the empty residual diagram. Conditional on that event, the remaining matching is uniform on the remaining \(2(n-k)\) endpoints. Each selected simple chord has zero crossings with every chord, and deleting it preserves the cyclic alternation relation between all surviving chord pairs. The conditional crossing-count law is therefore **exactly** that of \(X_{n-k}\), including the case of two or more boundary chords that are adjacent to each other.

**3. Factorial-weighted distribution identity.** Expand \((S_n)_{\underline k}\) as the number of ordered distinct simple chords present. Sum the conditional crossing generating polynomial over each ordered feasible selection:
\[
 \mathbb E[(S_n)_{\underline k}z^{X_n}]
 = k!M_{n,k}\frac{(2n-2k-1)!!}{(2n-1)!!}F_{n-k}(z).
\]
Using \((2m-1)!!=(2m)!/(2^m m!)\), the leading factor simplifies to the stated \(a_{n,k}\). Expanding \(u^{S_n}=(1+(u-1))^{S_n}\) in falling factorials proves the entire bivariate identity. Coefficient extraction in \(u\) proves the conditional-mass and zero-simple-chord formulas.

**4. Finite covariance consequences.** From the first two factorial moments, \(a_{n,1}=a_{n,2}=2n/(2n-1)\), giving the stated mean and variance of \(S_n\). Differentiating the transfer at \(z=1\) for \(k=1\) gives
\[
 \mathbb E[S_nX_n]=a_{n,1}\mu_{n-1}.
\]
Since \(\mu_n=n(n-1)/6\), subtraction yields \(\operatorname{Cov}(S_n,X_n)=a_{n,1}(\mu_{n-1}-\mu_n)\). The classical variance \(\sigma_n^2=n(n-1)(n+3)/45\) then yields the stated correlation. This calculation recovers a known exact covariance; the new object in this result is the whole joint polynomial and its limiting consequence.

**5. Joint limit.** Write \(\phi_n(s,t)\) for the joint characteristic function of \(S_n\) and \((X_n-\mu_n)/\sigma_n\). Substitution into the finite identity gives
\[
 \phi_n(s,t)=\sum_{k=0}^{n}\frac{a_{n,k}}{k!}(e^{is}-1)^k
 \mathbb E\left[e^{it(X_{n-k}-\mu_n)/\sigma_n}\right].
\]
For fixed \(k\), \(a_{n,k}\to1\). The established one-dimensional crossing central limit theorem and the relations \((\mu_{n-k}-\mu_n)/\sigma_n\to0\), \(\sigma_{n-k}/\sigma_n\to1\) show that the expectation in the summand tends to \(e^{-t^2/2}\). Uniformly in \(0\le k\le n\),
\[
 0\le a_{n,k}=\frac{2n}{2n-k}\prod_{j=0}^{k-1}\frac{2(n-j)}{2n-j}\le2.
\]
The absolute value of the \(k\)-th summand is therefore bounded by \(2|e^{is}-1|^k/k!\), a summable sequence independent of \(n\). Dominated convergence for series gives
\[
 \lim_{n\to\infty}\phi_n(s,t)
 =e^{-t^2/2}\sum_{k\ge0}\frac{(e^{is}-1)^k}{k!}
 =\exp(e^{is}-1-t^2/2).
\]
This is the joint characteristic function of independent \(\operatorname{Poisson}(1)\) and standard Gaussian variables. Lévy's continuity theorem completes the proof.

## Verification

Run `python verify_chord_joint.py` with standard Python 3. The independent enumeration routine covers every perfect matching for each size from two through seven chords and verifies all factorial-weighted crossing-distribution identities coefficient by coefficient, all second moments and the exact squared correlation. It reports `PASS: 487 exact-rational/equality assertions; all perfect matchings through n=7 checked.` This finite calculation is not used as a substitute for the all-size counting proof or for the classical crossing central limit theorem.

## Relationship to prior work

Flajolet and Noy established the crossing-count mean, variance and Gaussian limit and studied asymptotic simple-chord counts. Acan studied simple chords and Poisson limits for short-chord length statistics using factorial moments. Paguyo provided quantitative rates for the **separate** crossing and simple-chord marginal limits. The Touchard–Riordan crossing enumerators supply the univariate polynomial \(F_m\). The present exact transfer refines these separate marginal results to a complete bivariate law and proves independence of differently scaled limiting fluctuations. The elementary joint finite covariance displayed above can also be derived by direct conditioning and is **not** asserted to be novel.

## Limitations

The exact transfer depends on selected chords being cyclically consecutive: a prescribed longer chord may cross residual chords, so identical deletion reasoning does not directly apply. The independence statement concerns the stated Poisson-count/Gaussian-count limiting pair, not exact finite independence or independence of the full matching. The joint limit relies on the established marginal crossing central limit theorem. The identity does not establish historical priority against every possible implicit bivariate enumeration in the literature. No independent scientific validation has been performed.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, author manuscript (2000), https://algo.inria.fr/flajolet/Publications/FlNo00.pdf; especially Theorem 3 on crossing counts.
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489 (first posted 2015-01-07), https://arxiv.org/abs/1501.01489; especially Section 3 and Lemma 3.3.
3. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134 (first posted 2021-04-02), https://arxiv.org/abs/2104.01134; especially Theorems 1.1–1.2.
4. V. Pilaud and J. Rué, *Analytic Combinatorics of Chord and Hyperchord Diagrams with k Crossings*, arXiv:1307.6440, https://arxiv.org/abs/1307.6440; crossing-number enumeration with fixed crossing count.
