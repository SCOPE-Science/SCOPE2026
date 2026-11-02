# A sharp finite-sample sign phase diagram for two-scale uniform spacing exceedances

## Finding

Let \(n\ge2\) points be independently uniform on a circle of circumference one. Enumerate their \(n\) clockwise spacings as \(G_1,\ldots,G_n\), and for \(0<t<1\) put
\[
N_n(t)=\sum_{i=1}^n\mathbf1\{G_i>t\}.
\]
For every pair \(0<r\le s<1\), the complete two-threshold covariance is
\[
\operatorname{Cov}(N_n(r),N_n(s))=
 n\left[(1-s)^{n-1}+(n-1)(1-r-s)_+^{n-1}
 -n(1-r)^{n-1}(1-s)^{n-1}\right], \tag{1}
\]
where \(z_+=\max\{z,0\}\). Define the critical lower threshold
\[
r_c(n)=1-n^{-1/(n-1)}. \tag{2}
\]
The following **sharp, all-size sign classification** holds, including its zero sets.

1. If \(r>r_c(n)\), the covariance in (1) is strictly positive for every \(s\in[r,1)\).
2. If \(r=r_c(n)\), it is strictly positive for \(r\le s<1-r\) and exactly zero for \(1-r\le s<1\). The strictly positive interval is empty when \(n=2\).
3. If \(0<r<r_c(n)\), put
\[
Q_n(r)=\frac{n(1-r)^{n-1}-1}{n-1},\qquad
s_*(n,r)=1-\frac{r}{1-Q_n(r)^{1/(n-1)}}. \tag{3}
\]
Then \(r<s_*(n,r)<1-r\), and the covariance is strictly positive for \(r\le s<s_*(n,r)\), zero at \(s=s_*(n,r)\), and strictly negative for \(s_*(n,r)<s<1\).

There is also an exact polynomial encoding of the entire joint count law:
\[
\mathbb E[u^{N_n(r)}v^{N_n(s)}]
=\sum_{a+b\le n}\frac{n!}{a!\,b!\,(n-a-b)!}
 (u-1)^a\,[u(v-1)]^b\,(1-ar-bs)_+^{n-1}, \tag{4}
\]
where the sum is over nonnegative integers \(a,b\).

For example, at \(n=3\), \(r=1/10\), and \(s=3/5\), the exact covariance is \(-183/1250\), despite the almost-sure nesting \(N_n(r)\ge N_n(s)\). A nested pair of exceedance counts thus need not be positively correlated.

## Assumptions and scope

All randomness is solely from independent uniform points on a unit circle; equivalently, after rotating one of those points to the origin, the clockwise gaps have the \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution. The strict inequalities in the definition of \(N_n(t)\) cause no atom or boundary complication because all individual spacings have continuous distributions. The statements hold for every integer \(n\ge2\) and all real thresholds \(0<r\le s<1\), without asymptotic assumptions. In particular, the \(n=2\), \(r=1/2\) case is retained: \(N_2(1/2)=1\) almost surely and its covariance with every higher-threshold count is zero.

## Proof

**Step 1: simplex volume.** Fix a distinguished sampled circle point and rotate it to the origin. The remaining \(n-1\) points are independent uniform samples on \((0,1)\). The vector of the \(n\) gaps between successive order statistics and the two endpoints is uniform on the standard \((n-1)\)-simplex. For any \(k\) distinct coordinates and nonnegative thresholds \(t_1,\ldots,t_k\), translation of the constrained simplex gives
\[
\Pr\{G_{i_1}>t_1,\ldots,G_{i_k}>t_k\}
=\left(1-\sum_{j=1}^k t_j\right)_+^{n-1}. \tag{5}
\]
The formula also holds at equality of the threshold sum to one, since the corresponding boundary has zero \((n-1)\)-dimensional measure for \(n\ge2\).

**Step 2: all finite mixed moments.** Expand the identity
\[
u^{\mathbf1\{G_i>r\}}v^{\mathbf1\{G_i>s\}}
=1+(u-1)\mathbf1\{G_i>r\}
  +u(v-1)\mathbf1\{G_i>s\}. \tag{6}
\]
Taking the product over the gap indices, selecting disjoint sets of cardinalities \(a,b\), and applying (5) produces (4). Alternatively, the one- and two-coordinate instances of (5) yield
\[
\mathbb E[N_n(t)]=n(1-t)^{n-1},\quad
\mathbb E[N_n(r)N_n(s)]
=n(1-s)^{n-1}+n(n-1)(1-r-s)_+^{n-1}, \tag{7}
\]
which imply (1).

**Step 3: the unique sign crossing.** Factor (1) as
\[
\operatorname{Cov}(N_n(r),N_n(s))
=n(1-s)^{n-1}B_{n,r}(s),\tag{8}
\]
where
\[
B_{n,r}(s)=1-n(1-r)^{n-1}
+(n-1)\left(1-\frac{r}{1-s}\right)_+^{n-1}.\tag{9}
\]
The prefactor is strictly positive because \(s<1\). On \(r\le s<1-r\), the last term in (9) is strictly decreasing in \(s\); on \(s\ge1-r\), it is zero. Thus \(B_{n,r}\) is strictly decreasing up to \(1-r\) and constant thereafter. Its final value is
\[
B_{n,r}(1-r)=1-n(1-r)^{n-1},\tag{10}
\]
whose unique zero as a function of \(r\) is (2).

For \(r<r_c(n)\), one has \(r<1/2\) (with equality of \(r_c(n)\) and \(1/2\) only at \(n=2\)). On open subsets of the simplex, one can place exactly one large gap above \(r\), or at least two gaps above \(r\), by assigning the remaining gaps sufficiently small positive lengths. Hence \(N_n(r)\) is nonconstant and
\[
B_{n,r}(r)=\frac{\operatorname{Var}(N_n(r))}{n(1-r)^{n-1}}>0.\tag{11}
\]
The terminal value (10) is negative for \(r<r_c(n)\). Strict monotonicity therefore yields exactly one zero between \(r\) and \(1-r\); solving (9) for that zero gives (3). For \(r=r_c(n)\), the terminal value is zero, producing the entire stated zero interval. For \(r>r_c(n)\), the terminal value is positive and monotonicity forces strict positivity throughout. This proves every sign and boundary case.

**Step 4: relation to the classical spacing-process limit.** For fixed \(0<x\le y\), set \(r=x/n\) and \(s=y/n\). Taylor expansion of the exact powers in (1) gives
\[
\lim_{n\to\infty}\frac1n
\operatorname{Cov}(N_n(x/n),N_n(y/n))
=e^{-y}[1-(1+xy)e^{-x}]. \tag{12}
\]
The limiting covariance kernel is already part of the classical Shorack uniform-spacings Gaussian-process theory and is not asserted as a new result. Its unique sign-changing upper threshold is
\[
y_*(x)=\frac{e^x-1}{x},\qquad
n\,s_*(n,x/n)\longrightarrow y_*(x), \tag{13}
\]
where the second conclusion follows by bracketing the unique finite zero between fixed scaled thresholds on either side of \(y_*(x)\), using (12) and the already-proved finite monotonicity.

## Verification

The standalone \`verify.py\` requires only Python's standard library. Running \`python verify.py\` checks the covariance both against a separately inverted exact bivariate distribution and, for two gaps, against direct integration on a uniform interval. It also checks the joint generating polynomial at independent rational evaluation points, all three sign regimes over many sizes and thresholds, the degenerate boundary case, and convergence to the classical limiting kernel. A recorded execution completed **1,640 grouped exact and numerical assertions** successfully, including direct exact examples with negative covariance. Computations corroborate but do not replace the all-parameter proof above.

## Relationship to prior work

Pyke's *Spacings* (1965) introduced systematic spacing distribution theory; Koziol (1977) studied the empirical distribution function of spacings. Lo's 2014 full-text study, *Gaussian Approximations and Related Questions for the Spacings Process*, gives the already-known Gaussian limiting covariance kernel (its Theorem 1, formula (2.1)); that limit covers (12), not the finite \(n\) zero curve (3). Beirlant and van Zuijlen (1985) studied strong laws for this empirical distribution; Roos (1993) studied compound-Poisson approximations for counts of extreme spacings. Mijatović and Vysotsky (2015) treat maximal uniform spacings. The present specific finite two-threshold all-size sign classification and exact zero interval were not found in the available inspected material. Equation (5) itself is classical Dirichlet geometry; neither this elementary ingredient nor the established Gaussian limiting kernel is claimed as an original invention.

## Limitations

The novelty judgment is a best-knowledge comparison, not a claim of exhaustive bibliographic priority. Full text could not be obtained for the broad 1965 Pyke survey, the 1977 Koziol note, and the 1985 Beirlant–van Zuijlen article, leaving a concrete possibility of earlier implicit formulas or equivalent classifications. The theorem applies to uniform circular spacings only; it does not assert the same sign structure for nonuniform point processes, higher-order spacings, or counts of graph components on a circle. The exact joint generating polynomial is a consequence of known uniform-simplex volumes; the claimed addition is the explicit sharp finite-sample sign geometry.

## References

1. Pyke, R., *Spacings*, Journal of the Royal Statistical Society B 27 (1965), 395–436. DOI: 10.1111/j.2517-6161.1965.tb00602.x.
2. Koziol, J. A., *On Goodness of Fit Tests Based on the Empirical Distribution Function for Uniform Spacings*, Journal of the Royal Statistical Society B 39 (1977), 333–336. DOI: 10.1111/j.2517-6161.1977.tb01631.x.
3. Beirlant, J., and van Zuijlen, M. C. A., *The empirical distribution function and strong laws for functions of order statistics of uniform spacings*, Journal of Multivariate Analysis 16 (1985), 300–317.
4. Roos, M., *Compound poisson approximations for the numbers of extreme spacings*, Advances in Applied Probability 25 (1993), 847–874. DOI: 10.2307/1427795.
5. Lo, G. S., *Gaussian Approximations and Related Questions for the Spacings Process*, arXiv:1406.7427v1 (first publicly posted 2014-06-28); especially Section 2, Theorem 1.
6. Mijatović, A., and Vysotsky, V., *On the weak limit law of the maximal uniform k-spacing*, arXiv:1508.00944v1 (first publicly posted 2015-08-05).
