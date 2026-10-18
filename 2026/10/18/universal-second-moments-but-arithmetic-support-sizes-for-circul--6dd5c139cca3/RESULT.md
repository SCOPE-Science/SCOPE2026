# Universal second moments but arithmetic support sizes for circular permutation correlograms

## Finding

For a fixed sample of \(n\ge4\) real observations, randomly permute the observations onto an \(n\)-cycle and form the unordered-product sum \(C_d\) over all position pairs at cyclic separation \(d\). Every non-antipodal lag has exactly the same variance, and every two distinct non-antipodal lags have a universal negative correlation, independent of the observed numbers. Nevertheless, for a sample in generic real position, the exact number of attainable permutation-statistic values can vary by enormous factors across those lags, determined explicitly by \(\gcd(n,d)\).

**Exact covariance and spectra.** Let \(a_0,\ldots,a_{n-1}\in\mathbb R\) be fixed (repetitions permitted), let \(\pi\) be uniformly distributed on all \(n!\) permutations, and write \(Y_i=a_{\pi(i)}\), with position subscripts understood modulo \(n\). For every integer \(1\le d\le m=\lfloor n/2\rfloor\), put
\[
 C_d=\begin{cases}
 \sum_{i=0}^{n-1}Y_iY_{i+d},&2d<n,\\[2mm]
 \frac12\sum_{i=0}^{n-1}Y_iY_{i+d},&2d=n.
 \end{cases}
\]
The factor \(1/2\) is essential: it counts each antipodal unordered pair once. Define \(\bar a=n^{-1}\sum_i a_i\), \(Q=\sum_i(a_i-\bar a)^2\), \(R=\sum_i(a_i-\bar a)^4\), and
\[
 \Lambda=\frac{(n^2-3n+3)Q^2-n(n-1)R}{(n-1)(n-2)(n-3)}.
\]
For any two non-antipodal lags \(d,e\),
\[
 \operatorname{Cov}(C_d,C_e)=
 \begin{cases}
 \frac{n-3}{n-1}\Lambda,&d=e,\\[2mm]
 -\frac2{n-1}\Lambda,&d\ne e.
 \end{cases}
\]
When \(n\) is even, also
\[
 \operatorname{Cov}(C_d,C_{n/2})=-\frac{\Lambda}{n-1}\quad(d<n/2),\qquad
 \operatorname{Var}(C_{n/2})=\frac{n-2}{2(n-1)}\Lambda.
\]
These are all the entries of the full covariance matrix \(\Sigma\). It follows that if \(\Lambda>0\), the Pearson correlation of any two distinct non-antipodal lag sums is exactly
\[
 \operatorname{Corr}(C_d,C_e)=-\frac2{n-3}.
\]
For odd \(n\), the spectrum is \(\Lambda\) with multiplicity \((n-3)/2\), and zero once. For even \(n\), the spectrum is \(\Lambda\) with multiplicity \((n-4)/2\), \(\frac{n}{2(n-1)}\Lambda\) once, and zero once. Zero is forced by the deterministic relation \(\sum_{d=1}^m C_d=\frac12[(\sum_i a_i)^2-\sum_i a_i^2]\). The covariance rank is therefore \(m-1\) whenever \(\Lambda>0\).

The scale is nonnegative for **every** real sample:
\[
 \Lambda=\frac n4\,\mathbb E\big[(Y_1-Y_2)^2(Y_3-Y_4)^2\big]\ge0,
\]
where the four positions are distinct. Equality occurs exactly when at least \(n-1\) sample values coincide. In particular, the nonzero even-length covariance condition number is exactly \(2(n-1)/n<2\) for even \(n\ge6\), and the odd-length nonzero covariance is a scalar multiple of an orthogonal projection.

**Exact generic permutation support.** Assume in addition that the \(a_i\) are algebraically independent over \(\mathbb Q\). This holds with probability one for a sample having an absolutely continuous joint distribution. Given a lag \(d\), put \(g=\gcd(n,d)\) and \(\ell=n/g\). The distribution of \(C_d\) under uniform random permutation is *uniform on precisely*
\[
 s(n,d)=\begin{cases}
 \displaystyle\frac{n!}{(2\ell)^g g!},&\ell\ge3,\\[3mm]
 \displaystyle\frac{n!}{2^g g!},&\ell=2
 \end{cases}
\]
distinct real values, each with mass \(1/s(n,d)\). The joint vector \((C_1,\ldots,C_m)\) is uniform on precisely \(n!/(2n)\) distinct vectors. These counts and uniform atom masses hold for every algebraically independent sample, without approximation.

Thus **identical marginal variances can conceal strikingly different exact randomization supports**. At \(n=9\), the ordinary lags \(d=1\) and \(d=3\) have the same variance and correlation with other ordinary lags, but their separate permutation null distributions respectively have \(20{,}160\) and \(280\) equiprobable atoms. For a one-sided unrandomized upper-tail test based on a single lag statistic, the smallest possible generic permutation \(p\)-value is respectively \(1/20160\) and \(1/280\).

## Assumptions and scope

The covariance, positivity, rank, and spectral results apply to every deterministic real sample of length \(n\ge4\), including samples with ties; no moment or distributional assumption is placed on those fixed numbers. The atom-count statement additionally assumes algebraic independence and is an almost-sure statement for absolutely continuously sampled data. The permutation is uniform on all position assignments and the lag statistic uses *circular* wrapping, not the usual endpoint-truncated sample autocorrelation. The exceptional diameter lag is counted once rather than twice. This is an exact finite-sample result, not an asymptotic normality or independence theorem.

## Proof

**1. Four finite-population edge moments.** Under the random permutation, for pairwise distinct positions let
\[
 u=\mathbb E[Y_1Y_2],\quad v=\mathbb E[Y_1^2Y_2^2],\quad
 w=\mathbb E[Y_1^2Y_2Y_3],\quad z=\mathbb E[Y_1Y_2Y_3Y_4].
\]
For unordered-position edges, products associated with the same edge, two different incident edges, and two disjoint edges have respective second moments \(v,w,z\). By translation invariance of a product sum under adding a constant to every sample value, its covariance does not change if the values are first centered. For centered values, direct counting of distinct indices gives
\[
 v=\frac{Q^2-R}{n(n-1)},\qquad
 w=\frac{2R-Q^2}{n(n-1)(n-2)},\qquad
 z=\frac{3Q^2-6R}{n(n-1)(n-2)(n-3)}.
\]
Consequently, \(n(v-2w+z)=\Lambda\). Expanding four squared differences gives \(4(v-2w+z)=\mathbb E[(Y_1-Y_2)^2(Y_3-Y_4)^2]\).

**2. Overlap geometry of cyclic lag edge classes.** For \(2d<n\), the position-edge set
\(E_d=\{\{i,i+d\}:i\in\mathbb Z/n\mathbb Z\}\)
has exactly \(n\) distinct edges and degree two at every position, regardless of whether \(\gcd(n,d)>1\). A fixed edge of \(E_d\) overlaps exactly two *other* edges of \(E_d\), giving \(2n\) ordered distinct incident pairs. For two distinct ordinary lags, the edge sets are disjoint, but exactly \(4n\) ordered edge pairs share one endpoint. Hence, writing \(V\) for any ordinary diagonal covariance and \(B\) for any distinct ordinary off-diagonal covariance,
\[
\begin{aligned}
V&=n(v-u^2)+2n(w-u^2)+n(n-3)(z-u^2),\\
B&=4n(w-u^2)+n(n-4)(z-u^2),
\end{aligned}
\]
and therefore \(V-B=n(v-2w+z)=\Lambda\).

For even \(n\), the antipodal edges form a perfect matching with \(n/2\) edges and degree one at each position. Relative to any ordinary lag there are \(2n\) ordered incident edge pairs, exactly half the number for two ordinary lags. The total pair count is also half, so the ordinary–antipodal covariance \(D\) is precisely \(B/2\).

**3. Sum constraint and full diagonalization.** Every unordered pair of positions belongs to exactly one distance class; hence \(\sum_d C_d\) is deterministic, and every covariance row sums to zero. If \(n\) is odd, there are \(m=(n-1)/2\) ordinary classes, giving \(V+(m-1)B=0\). Together with \(V-B=\Lambda\), this yields \(V=(n-3)\Lambda/(n-1)\) and \(B=-2\Lambda/(n-1)\). The covariance is \(\Lambda(I_m-\mathbf1\mathbf1^{\mathsf T}/m)\), proving its spectrum.

If \(n\) is even, there are \(r=n/2-1\) ordinary classes and one antipodal class. The ordinary row condition is \(V+(r-1)B+D=0\), with \(D=B/2\). Solving again yields \(B=-2\Lambda/(n-1)\), \(V=(n-3)\Lambda/(n-1)\), and \(D=-\Lambda/(n-1)\). The antipodal row condition gives \(\operatorname{Var}(C_{n/2})=-rD=r\Lambda/(n-1)\). The subspace of ordinary coordinates summing to zero is an eigenspace of eigenvalue \(\Lambda\) and dimension \(r-1\). The all-ones vector is a null mode; the remaining direction \((1,\ldots,1,-r)\) has eigenvalue \(n\Lambda/[2(n-1)]\). This proves all covariance and spectral assertions.

The formula for \(\Lambda\) is nonnegative by the squared-difference identity. It vanishes precisely when there do not exist two vertex-disjoint pairs of unequal sample values. For \(n\ge4\), this means that at least \(n-1\) of the values agree: if the largest equal-value class has at most \(n-2\) members, either two members of that class and two outside it form two unequal pairs, or all class sizes are one and four distinct values can be paired. This proves the exact degeneracy criterion.

**4. Arithmetic orbit sizes.** Regard \(C_d\) as a polynomial in \(n\) independent indeterminates indexed by the observation labels. Under algebraic independence of their realized values, two such quadratic polynomials agree numerically if and only if they have identical coefficients. Each coefficient of \(a_i a_j\) identifies whether the unordered pair \(\{i,j\}\) appears as an edge at distance \(d\) after assignment. Thus two permutations give equal \(C_d\) precisely when they differ by an automorphism of the undirected distance-\(d\) position graph.

That graph is a disjoint union of \(g=\gcd(n,d)\) cycles of length \(\ell=n/g\). For \(\ell\ge3\), each cycle has \(2\ell\) dihedral automorphisms and the \(g\) cycles can be permuted, giving automorphism order \((2\ell)^g g!\). When \(\ell=2\), it is a perfect matching and has automorphism order \(2^g g!\). Every orbit has the indicated stabilizer size, proving both the support formula and equal masses. Finally, equality of the entire lag vector implies equality of \(C_1\). The distance-one graph is a Hamilton cycle, whose automorphism group is precisely the dihedral group of order \(2n\), and every such dihedral symmetry preserves all unordered circular distance classes. Therefore the full vector has \(n!/(2n)\) equiprobable values.

## Verification

The standalone `verify.py` performs exact-arithmetic checks of all covariance entries and deterministic row sums by exhaustive enumeration of all position permutations for lengths \(4\) through \(8\), on four different samples per length (including tie-heavy and degenerate cases). It checks the zero-scale classification on all multisets over three distinct values up to length \(12\). For lengths \(4\) through \(8\), it also enumerates every distinct single-lag and joint score, checking both predicted support counts and exact equal atom multiplicities. The injective arithmetic test sample uses values \(2^{2^i}\): every unordered pair product occupies a unique binary digit, so distinct edge sets are guaranteed different sums. The verifier returned `VERIFY_OK 737 exact assertions`. Finite verification is supporting evidence; the proof above establishes the arbitrary-length theorem.

## Relationship to prior work

Romano and Tirlea, *Permutation Testing for Dependence in Time Series* (first public preprint 2020-09-07, arXiv:2009.03170), establish a framework for exact permutation inference under exchangeability and asymptotic behavior of ordinary, endpoint-truncated autocorrelations. Their accessible full preprint discusses simultaneous lag tests, but does not establish the circular finite-sample covariance spectrum or the gcd-dependent count of exact permutation atoms.

Zhou, Mayhew, Sun, Xu, Zou and Wright, *Space–time clustering and the permutation moments of quadratic forms* (2013), provide exact moments of arbitrary quadratic forms under permutation. By polarization their general method can recover individual cyclic-lag covariances in principle. Accordingly, no novelty is claimed for the existence of those individual moments or the underlying edge-type bookkeeping. The specific structural classification here couples a universal all-lag covariance eigensystem with the exact graph-automorphism orbit spectrum of randomization supports; fourth-moment formulas alone cannot determine the latter. The older Wald–Wolfowitz serial-correlation literature and Hallin–Puri multivariate rank tests are also relevant to permutation-test methodology, but their accessible summaries do not establish the combined finite-support classification. This literature comparison is not an independent historical-priority certification.

## Limitations

The exact atom counts require algebraic independence; ties and algebraic relations among observed values can cause extra collisions and larger atom masses. Uniform atom masses are proved only for the generic fixed-sample random-permutation null, not for time-series alternatives or arbitrary dependent observations. The ordinary-pair negative correlation is a second-moment statement, not pairwise independence, and the theorem does not provide an asymptotic joint distribution. Generic quadratic-form moment theory covers raw moments broadly and remains an originality risk for the covariance part; older treatments of generic orbit stabilizers could potentially cover the support part. No independent mathematical or historical-priority audit has been performed.

## References

1. J. P. Romano and M. A. Tirlea, *Permutation Testing for Dependence in Time Series*, arXiv:2009.03170 (initial public version 2020-09-07), DOI: 10.1111/jtsa.12638. The publication lists MSC 62G10 and 62M10.
2. Y.-H. Zhou, G. Mayhew, Z. Sun, X. Xu, F. Zou and F. A. Wright, *Space–time clustering and the permutation moments of quadratic forms*, Stat 2 (2013), 292–302, DOI: 10.1002/sta4.37.
3. A. Wald and J. Wolfowitz, *An Exact Test for Randomness in the Non-Parametric Case Based on Serial Correlation*, Annals of Mathematical Statistics 14 (1943), 378–388, DOI: 10.1214/aoms/1177731358.
4. M. Hallin and M. L. Puri, *A multivariate Wald–Wolfowitz rank test against serial dependence*, Canadian Journal of Statistics 23 (1995), 55–65, DOI: 10.2307/3315547.
