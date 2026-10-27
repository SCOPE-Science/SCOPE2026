# Exact mixed chord statistics and independent Poisson–Gaussian limits

## Finding

Let a chord diagram be a uniformly chosen perfect matching of the linearly ordered sites \(1,\ldots,2n\). Write \(S_n\) for its number of short chords \((i,i+1)\), for \(1\le i<2n\), and \(C_n\) for its number of crossing pairs, where \((a,c)\) and \((b,d)\) cross when \(a<b<c<d\). For \(n\ge0\), define the univariate crossing polynomial

\[
T_n(q)=\sum_{M\in\mathcal M_{2n}}q^{C(M)},\qquad T_0(q)=1.
\]

**Theorem.** For every integer \(n\ge0\), the complete joint enumerator is

\[
\sum_{M\in\mathcal M_{2n}}z^{S(M)}q^{C(M)}
=\sum_{r=0}^{n}\binom{2n-r}{r}(z-1)^rT_{n-r}(q).
\tag{1}
\]

For \(0\le r\le n\), each bounded function \(f\) on the crossing-count range satisfies the exact mixed-factorial-moment identity

\[
\mathbb E[(S_n)_r f(C_n)]
=a_{n,r}\mathbb E[f(C_{n-r})],\qquad
 a_{n,r}=\frac{r!\binom{2n-r}{r}(2n-2r-1)!!}{(2n-1)!!},
\tag{2}
\]

where \((s)_r=s(s-1)\cdots(s-r+1)\), \((s)_0=1\), \((-1)!!=1\), and \(C_0=0\). In particular, for \(n\ge2\),

\[
\operatorname{Cov}(S_n,C_n)=-\frac{n-1}{3},\qquad
\operatorname{Corr}(S_n,C_n)
=-\sqrt{\frac{5(2n-1)}{2n(n+3)}}.
\tag{3}
\]

For **every nondecreasing real function** \(f\) on the crossing-count range, \(\operatorname{Cov}(S_n,f(C_n))\le0\). Finally, let \(\mu_n=n(n-1)/6\), \(\sigma_n^2=n(n-1)(n+3)/45\), and \(Z_n=(C_n-\mu_n)/\sigma_n\) for \(n\ge2\). Then

\[
(S_n,Z_n)\ \xrightarrow[n\to\infty]{\mathrm{d}}\ (P,Z),
\qquad P\sim\mathrm{Poisson}(1),\quad Z\sim N(0,1),\quad P\perp Z.
\tag{4}
\]

The local short-chord count and the centered global crossing count thus have a negative finite-size dependence, but become **jointly independent after their natural limit scalings**.

## Assumptions and scope

All \((2n-1)!!\) perfect matchings on the \(2n\) ordered sites are equiprobable. Adjacency is **linear**: the sites \(2n\) and \(1\) are not adjacent. Intersections refer to pairs whose endpoints alternate. In (2), the \(C_{n-r}\) distribution belongs to a fresh uniform matching on \(2(n-r)\) sites; there is no assertion that the original \(C_n\) is independent of \(S_n\). The covariance inequality also applies to nondecreasing functions that are unbounded outside the finite support, provided their values are finite on that support. Equation (3) requires \(n\ge2\) so that both variances are nonzero. Equation (4) concerns the entire joint law; it makes no rate-of-convergence assertion.

## Proof

**1. Forced short chords preserve every crossing.** Fix \(r\) pairwise disjoint adjacent edges in the original ordered sites, and require all of them to be matching edges. They cannot cross any other chord: their endpoints have no intervening site. Delete their endpoints and relabel the remaining sites in order. Every crossing among remaining chords is preserved, and every matching of the remaining sites arises uniquely. Thus the sum of \(q^{C(M)}\) over diagrams containing that forced set is precisely \(T_{n-r}(q)\), independently of which adjacent edges were forced. There are \(\binom{2n-r}{r}\) sets of \(r\) nonoverlapping adjacent edges on a \(2n\)-vertex path: if their left endpoints are \(1\le i_1<\cdots<i_r\le2n-1\) with \(i_{j+1}\ge i_j+2\), shifting \(i_j\mapsto i_j-(j-1)\) gives a choice of \(r\) integers from \(1,\ldots,2n-r\).

For each matching expand \(z^{S(M)}=\sum_{r=0}^{S(M)}\binom{S(M)}r(z-1)^r\), sum over matching diagrams and interchange sums over short-chord subsets. This proves (1), including \(n=0\).

**2. Factorial Palm identities.** Differentiating (1) \(r\) times in \(z\) at \(z=1\), then comparing coefficients of \(q\), gives the enumeration identity for \((S_n)_r\) at every crossing count. Division by \((2n-1)!!\), using \(T_{n-r}(1)=(2n-2r-1)!!\), yields (2) for every \(f\). In particular \(a_{n,1}=1\) for \(n\ge1\), \(a_{n,2}=2(n-1)/(2n-1)\) for \(n\ge2\), and

\[
\mathbb ES_n=1,\qquad
\operatorname{Var}(S_n)=\frac{2(n-1)}{2n-1}.
\tag{5}
\]

The cases \(r=0\) and \(n=0\) follow directly under the empty-product conventions.

**3. Negativity and precise covariance.** The \(r=1\) identity is

\[
\mathbb E[S_n f(C_n)]=\mathbb E[f(C_{n-1})].
\tag{6}
\]

To compare the two crossing-count distributions, sample a uniform matching on \(2n\) sites, choose one of its \(n\) chords uniformly and delete it. Conditional on the remaining \(2n-2\) sites, every matching of those sites is equally likely; after increasing relabeling the remainder has the distribution of a uniform \((n-1)\)-chord matching. Its crossings are a subset of the original crossing pairs. This constructs a coupling \(\widetilde C_{n-1}\le C_n\) almost surely. Since \(\mathbb ES_n=1\), (6) proves \(\operatorname{Cov}(S_n,f(C_n))=\mathbb Ef(C_{n-1})-\mathbb Ef(C_n)\le0\) for every nondecreasing \(f\). For strictly increasing \(f\) and \(n\ge2\), this inequality is strict, because crossing chords exist with positive probability.

The classical crossing mean and variance (Flajolet–Noy, Theorem 3) are

\[
\mathbb EC_n=\frac{n(n-1)}6,\qquad
\operatorname{Var}(C_n)=\frac{n(n-1)(n+3)}{45}.
\tag{7}
\]

Consequently (6) at \(f(c)=c\) gives \(\operatorname{Cov}(S_n,C_n)=\mu_{n-1}-\mu_n=-(n-1)/3\). Combining with (5) and (7) yields (3).

**4. Joint limit.** First, for every \(0\le r\le n\), the factorial coefficient satisfies \(0\le a_{n,r}\le1\). To see the upper bound, write \(a_{n,r}\) as the sum, over ordered lists of \(r\) disjoint original adjacent bonds, of the probability that all listed bonds are present. At the stage when \(j\) bonds are selected, at most \(2(n-j)-1\) admissible **original** adjacent bonds remain, since these are among the neighboring pairs of the compressed remaining ordered sites. Thus the number of ordered lists is at most \(\prod_{j=0}^{r-1}(2(n-j)-1)\), the reciprocal of the joint inclusion probability for each list. For each fixed \(r\), the explicit factorial expression also shows \(a_{n,r}\to1\) as \(n\to\infty\).

The crossing central limit theorem of Flajolet–Noy states \(Z_n\Rightarrow N(0,1)\). With \(r\) fixed,

\[
\frac{C_{n-r}-\mu_n}{\sigma_n}
=\frac{\sigma_{n-r}}{\sigma_n}Z_{n-r}
+\frac{\mu_{n-r}-\mu_n}{\sigma_n}
\ \Rightarrow\ N(0,1),
\tag{8}
\]

because the standard-deviation ratio tends to one and the mean shift is \(O(n)/\Theta(n^{3/2})=o(1)\). The formula is interpreted directly when the finite initial values have zero variance; asymptotically \(n-r\ge2\).

Let \(t\in\mathbb R\) and \(0\le z\le1\). The finite binomial expansion and (2) give

\[
\mathbb E[z^{S_n}e^{it Z_n}]
=\sum_{r=0}^{n}\frac{(z-1)^r}{r!}
 a_{n,r}\,
\mathbb E\left[\exp\left(it\frac{C_{n-r}-\mu_n}{\sigma_n}\right)\right].
\tag{9}
\]

Each summand is bounded in modulus by \(1/r!\), uniformly in \(n\). Hence (8), \(a_{n,r}\to1\), and dominated convergence for series imply

\[
\mathbb E[z^{S_n}e^{it Z_n}]
\longrightarrow e^{z-1}e^{-t^2/2}.
\]

The limit is the joint probability-generating/characteristic transform of an independent Poisson(1) and standard Gaussian pair. Its uniqueness and the continuity theorem (or extracting the \(z\)-coefficients then applying characteristic-function convergence) give (4). No finite numerical experiment is invoked in this infinite-dimensional step.

## Verification

A self-contained Python 3 standard-library program, `verify.py`, exhaustively enumerates all perfect matchings for \(1\le n\le6\), independently builds the joint crossing/short-chord count table, and reconstructs it coefficient-by-coefficient from (1). It also checks (2) for all factorial orders and every possible crossing value, the exact means/variances/covariance, and nonpositive indicator-threshold covariances. It separately checks \(0\le a_{n,r}\le1\) for \(1\le n\le200\) and \(r\le\min(n,12)\). On execution the program returned `PASS 2945 exact assertions`. These are finite checks only; the all-size proof and joint convergence are the deductions above.

## Relationship to prior work

The Touchard–Riordan crossing polynomial and the marginal Gaussian limit are classical; Flajolet and Noy give a modern full proof and exact variance. The marginal distribution of the number of linear short chords has classical enumerations, discussed explicitly by Cameron and Killpatrick and by Marmor (including the Bessel-polynomial identity of McSorley and Feinsilver). Paguyo obtains **separate** Gaussian and Poisson convergence with quantitative bounds for crossings and **circularly** adjacent simple chords. Marmor further proves that matching families with a prescribed number of crossing pairs have Schur-positive short-chord quasisymmetric functions. Pilaud and Rué give a core decomposition and enumerative asymptotics in the fixed-small-crossing regime, distinct from typical crossings of order \(n^2\). That framework may encode some joint finite statistics, but the inspected statements do not present the exact short-edge-deletion transform (1), the universal covariance inequality (6), or the joint independent limit (4). These are statements about different properties and are not consequences of Schur positivity alone. The proof here builds directly on the published marginal crossing central limit theorem.

## Limitations

The definition of short chord is linear and excludes the wrap-around pair; modifying it requires a different edge-subset count in (1). No quantitative bound on distance to the product limit is proved. Joint asymptotic independence does **not** mean finite-size independence: the finite-size covariance is strictly negative. Historical priority is provisional: older combinatorial encodings or unpublished extensions of existing formulas might imply part or all of the identities. The inspected literature does not exhaust every possible prior derivation; independent assessment has not occurred.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report RR-3914 (March 2000), Section 2 and Theorem 3. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
2. N. Cameron and K. Killpatrick, *Statistics on Linear Chord Diagrams*, arXiv:1902.09021 (initial release 26 February 2019), on the marginal linear-short-chord law. https://arxiv.org/abs/1902.09021
3. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134 (initial release 2 April 2021), separate crossings and circular-simple-chord limit theorems. https://arxiv.org/abs/2104.01134
4. A. Marmor, *Schur-Positivity of Short Chords in Matchings*, arXiv:2307.09894 (initial release 19 July 2023), Sections 4 and 5. https://arxiv.org/abs/2307.09894
5. V. Pilaud and J. Rué, *Analytic combinatorics of chord and hyperchord diagrams with \(k\) crossings*, arXiv:1307.6440 (initial release 24 July 2013), crossing-enumeration background. https://arxiv.org/abs/1307.6440
