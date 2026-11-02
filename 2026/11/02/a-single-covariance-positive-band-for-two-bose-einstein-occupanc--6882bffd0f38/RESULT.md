# A single covariance-positive band for two Bose–Einstein occupancy frequencies

## Finding

Take a uniformly random weak composition \((X_1,\ldots,X_k)\) of an integer \(n\) into \(k\ge2\) ordered nonnegative parts. Write \(N_t=\#\{i:X_i=t\}\) for the number of parts (occupancy categories) with size \(t\). For all integers \(1\le r<s\) with \(r+s\le n\), define the normalized cross-moment
\[
R_{n,r,s}(k)=\frac{\mathbb E[N_rN_s]}{\mathbb E[N_r]\,\mathbb E[N_s]}.
\]
For every integer \(k\ge3\), this quantity has the exact product form
\[
R_{n,r,s}(k)=\frac{k-2}{k}\frac{(n)_{\underline{r+s}}}{(n)_{\underline r}(n)_{\underline s}}
\prod_{j=0}^{r}\frac{n+k-1-j}{n+k-s-2-j},
\]
where \((z)_{\underline m}=z(z-1)\cdots(z-m+1)\). At \(k=2\), its value is \((n+1)/2\) if \(n=r+s\), and zero otherwise.

**Covariance-positive band theorem.** The smooth rational interpolation of \(R_{n,r,s}(k)\) to real \(k>2\) is strictly decreasing when \(n=r+s\). When \(n>r+s\), it strictly increases to exactly one maximum and then strictly decreases. Consequently, for fixed \(n,r,s\), the set of integers \(k\ge2\) for which \(\operatorname{Cov}(N_r,N_s)>0\) is a single finite interval of consecutive integers (possibly empty). The covariance cannot undergo more than two sign reversals as the number of categories grows. The limiting normalized cross-moment is strictly below one:
\[
\lim_{k\to\infty}R_{n,r,s}(k)
=\frac{(n-r)_{\underline s}}{(n)_{\underline s}}<1.
\]
Both sign reversals can occur. At \((n,r,s)=(10,1,6)\), for \(k=2,3,4,5,6,7\) respectively, the exact normalized cross-moments are
\[
0,\quad\frac{22}{25},\quad\frac{26}{25},\quad\frac{26}{25},\quad 1,\quad\frac{20}{21}.
\]
Thus the covariance is negative at \(k=2,3\), positive at \(k=4,5\), zero at \(k=6\), and negative for all \(k\ge7\).

## Assumptions and scope

The integer parameters satisfy \(n\ge3\), \(1\le r<s\), \(r+s\le n\), and \(k\ge2\). Every vector of nonnegative integers summing to \(n\) is sampled with probability \(1/\binom{n+k-1}{k-1}\). Equivalently, the category proportions are drawn from a symmetric \(\operatorname{Dirichlet}(1,\ldots,1)\) law and then \(n\) categorical observations are drawn conditionally independently from those proportions. The term *Bose–Einstein* refers here to the equal-weight weak-composition occupancy law, not to interacting physical bosons. There are no additional independence assumptions on the resulting counts \(X_i\).

The denominator in the definition of \(R_{n,r,s}(k)\) is positive under the stated constraints. For distinct frequencies \(r,s\), its covariance has the same sign as \(R_{n,r,s}(k)-1\). The theorem does not assert monotonicity for each individual covariance magnitude; it is a sign and normalized-cross-moment statement.

## Proof

**1. Exact stars-and-bars moments.** Let \(Z=\binom{n+k-1}{k-1}\). Marking the first part at size \(t\), with \(0\le t\le n\), gives
\[
p_t:=\Pr(X_1=t)=\frac{\binom{n-t+k-2}{k-2}}{Z},
\qquad \mathbb E[N_t]=kp_t.
\]
For \(k\ge3\), marking two distinct parts with sizes \(r,s\) gives
\[
p_{r,s}:=\Pr(X_1=r,X_2=s)
=\frac{\binom{n-r-s+k-3}{k-3}}{Z},
\qquad
\mathbb E[N_rN_s]=k(k-1)p_{r,s}.
\]
Because \(r\ne s\), no diagonal term appears. Substituting and cancelling factorials proves the product formula. For \(k=2\), both sizes can occur only when \(n=r+s\). In that case two ordered compositions contain both sizes, so \(\mathbb E[N_rN_s]=2/(n+1)\), and \(\mathbb E[N_r]=\mathbb E[N_s]=2/(n+1)\). When \(n>r+s\), no two-part composition can contain both sizes, proving the stated boundary values.

**2. An exact derivative certificate.** Fix \(n,r,s\) and regard the product expression as a positive function \(R(x)\) for real \(x>2\). Set
\[
A_j=n-1-j,\qquad B_j=n-s-2-j\qquad(0\le j\le r),
\]
so that \(A_j\ge s-1>0\), \(B_j\ge-2\), and \(A_j-B_j=s+1\). Direct logarithmic differentiation yields
\[
\frac{d}{dx}\log R(x)=\frac{2-(s+1)T(x)}{x(x-2)},\qquad
T(x)=\sum_{j=0}^{r}\frac{x(x-2)}{(x+A_j)(x+B_j)}.
\]
Every summand is a product of the positive functions \(x/(x+A_j)\) and \((x-2)/(x+B_j)\). The first is strictly increasing, while the second is nondecreasing because \(B_j\ge-2\); hence every summand and \(T(x)\) itself are strictly increasing. Furthermore \(T(x)\to r+1\) as \(x\to\infty\). Since \(r\ge1\) and \(s\ge2\), \((s+1)(r+1)>2\).

If \(n>r+s\), then \(B_j>-2\) for every \(j\), so \(T(2+)=0\). Hence the equation \(T(x)=2/(s+1)\) has exactly one solution in \((2,\infty)\), and \(R\) first strictly rises and then strictly falls. If \(n=r+s\), only \(B_r=-2\), and \(A_r=s-1\), giving \(T(2+)=2/(s+1)\). Strict growth makes the logarithmic derivative negative throughout \((2,\infty)\), so \(R\) is strictly decreasing.

**3. From unimodality to a complete sign-band statement.** The prefactor independent of \(x\) equals \((n-r)_{\underline s}/(n)_{\underline s}\), strictly below one. The product tends to one and \((x-2)/x\to1\) as \(x\to\infty\); thus \(R(x)\) approaches a limit below one. The \(k=2\) value agrees with the right-hand limit as \(x\downarrow2\): zero if \(n>r+s\), and \((n+1)/2\) if \(n=r+s\). A strictly decreasing or strictly single-peaked continuous curve has a connected open superlevel set \(\{x\ge2:R(x)>1\}\), and the subunit limit bounds that set above. Intersecting it with the integers gives either the empty set or one finite interval of integers. Since \(\operatorname{Cov}(N_r,N_s)=\mathbb E[N_r]\mathbb E[N_s](R_{n,r,s}(k)-1)\), the covariance classification follows. Substituting \((10,1,6)\) gives the six rational values above; unimodality rules out any further positive values after \(k=7\).

## Verification

The accompanying standard-library Python file `check.py` checks the exact first and mixed moments by independently enumerating all weak compositions for \(3\le n\le10\) and \(2\le k\le7\), across every admissible \(1\le r<s\) with \(r+s\le n\). It independently evaluates the falling-factorial product, tests single-band behavior and discrete unimodality for broader parameters \(3\le n\le50\) and \(2\le k\le40\), and checks the exact six-term example. The script passed 21,041 exact assertions using integer and rational arithmetic. These finite checks corroborate, but do not replace, the all-parameter argument above. Run from a directory containing this file with `python3 check.py`.

## Relationship to prior work

Huillet and Paroissin (2008) describe Dirichlet sampling and the uniform-composition/Bose–Einstein occupancy special case. Huillet and Martínez (2013), especially their general frequency-of-frequencies factorial-moment formulas, supply pre-existing moment-enumeration machinery from which the present stars-and-bars moments follow. Their general formulas are **not** claimed as new here. The substantive assertion assessed is the global single-maximum law and the resulting complete covariance-positive interval in the number of categories, including an explicit two-reversal regime. The inspected works do not explicitly formulate this parameter-shape theorem. Ben-Hamou, Boucheron and Ohannessian (2014) study occupancy-count concentration for iid samples with fixed category probabilities, a different sampling law; their main estimates neither imply nor disprove the Dirichlet-mixture covariance-band property.

## Limitations

This is an exact finite-parameter statement for distinct positive occupancy frequencies in the symmetric Dirichlet concentration-one model. It does not establish the same shape for unequal Dirichlet parameters, repeated frequencies, a nonuniform deterministic categorical law or general occupancy functionals. The covariance magnitude itself is not proved unimodal. Historical-priority risk remains: earlier general multivariate occupancy formulas may encode the same shape through an unrecognized inequality. The work has not undergone independent scientific audit.

## References

- T. Huillet and C. Paroissin, *Sampling from Dirichlet populations: estimating the number of species*, arXiv:0809.4181, first public 2008-09-24, https://arxiv.org/abs/0809.4181.
- T. Huillet and S. Martínez, *Occupancy distributions arising in sampling from Gibbs-Poisson abundance models*, arXiv:1307.3000, first public 2013-07-11, https://arxiv.org/abs/1307.3000.
- A. Ben-Hamou, S. Boucheron and M. I. Ohannessian, *Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications*, arXiv:1412.8652, first public 2014-12-30, https://arxiv.org/abs/1412.8652.
