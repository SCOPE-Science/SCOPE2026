# Four count windows identify background-adjusted Omori decay sharply

## Finding

Consider the four-parameter, background-adjusted modified Omori intensity
\[
\lambda_\theta(t)=\mu+K(t+c)^{-p},\qquad
\theta=(\mu,K,c,p)\in(0,\infty)^4,\quad t\ge0.
\]
For **every** choice of four positive-length, chronologically disjoint observation windows \(I_i=[a_i,b_i]\), with
\(0\le a_1<b_1\le a_2<b_2\le a_3<b_3\le a_4<b_4\),
the map
\[
\theta\longmapsto\left(\int_{a_i}^{b_i}\lambda_\theta(t)\,dt\right)_{i=1}^{4}
\]
is globally injective and has a nonsingular Jacobian everywhere. These observations are *expected seismic event counts*, not realized random counts.

The number four is sharp: for any three ordered positive-length disjoint windows and every interior parameter point, a nonconstant one-parameter family of positive parameter quadruples gives exactly the same three expected counts, locally. If the constant background \(\mu\) is independently known, the sharp number becomes **three** windows: any three suffice globally, whereas two leave a nonconstant local family. The same four-versus-three and three-versus-two conclusions hold for exact *intensity evaluations* at distinct nonnegative times.

The underlying crossing theorem is sharp: two different admissible intensities can agree at at most **three** distinct times, and three intersections can really occur; with a common known background, the limit drops to **two** intersections, again sharp.

## Assumptions and scope

All parameters \(\mu,K,c,p\) are strictly positive. The mainshock clock origin, bin boundaries, exact expected bin counts, and validity of the single Omori-plus-constant intensity throughout the chosen windows are assumed known. The windows need not be equal width, adjacent, or regularly spaced; touching endpoints are allowed. With known background, only \(K,c,p\) are unknown. Claims concern deterministic structural identifiability of the intensity and its expectation integrals, **not** recovery of parameters from four noisy realized Poisson counts or four observed earthquake times.

The expected count in \([a,b]\) is explicit:
\[
M_\theta[a,b]=\mu(b-a)+K\begin{cases}
\displaystyle\frac{(b+c)^{1-p}-(a+c)^{1-p}}{1-p},&p\ne1,\\[4pt]
\displaystyle\log\frac{b+c}{a+c},&p=1.
\end{cases}
\]

## Proof

**Lemma 1 (sharp crossing bound).** For two parameter quadruples \(\theta_1\ne\theta_2\), let \(F(t)=\lambda_{\theta_1}(t)-\lambda_{\theta_2}(t)\). Unless \(F\) is a nonzero constant, its derivative is
\[
F'(t)=-K_1p_1(t+c_1)^{-p_1-1}+K_2p_2(t+c_2)^{-p_2-1}.
\]
Zeros of this derivative solve
\[
R(t):=\frac{(t+c_2)^{p_2+1}}{(t+c_1)^{p_1+1}}=\frac{K_2p_2}{K_1p_1}.
\]
But
\[
\frac{R'(t)}{R(t)}=
\frac{(p_2-p_1)t+(p_2+1)c_1-(p_1+1)c_2}
{(t+c_1)(t+c_2)}.
\]
Its numerator is affine, so a nonconstant \(R\) is monotone or has one turning point. Every horizontal level therefore occurs at most twice. If \(R\) is constant, the powers and shifts coincide; \(F'\) is either identically zero or nowhere zero. By Rolle's theorem, a nonzero \(F\) has at most three distinct zeros on \([0,\infty)\). When \(F\equiv0\), taking the limit at infinity gives \(\mu_1=\mu_2\); comparing the negative logarithmic derivative of \(\lambda-\mu\), namely \(p/(t+c)\), forces \(p_1=p_2\), \(c_1=c_2\), and finally \(K_1=K_2\). Hence four distinct agreements imply identical quadruples.

For fixed common \(\mu\), agreement of the two aftershock contributions is equivalently
\[
\frac{(t+c_2)^{p_2}}{(t+c_1)^{p_1}}=\frac{K_2}{K_1}.
\]
Its logarithmic derivative has affine numerator \((p_2-p_1)t+p_2c_1-p_1c_2\). Therefore two different, equal-background curves have at most two agreements; three force the remaining three parameters to coincide.

Both bounds are attained. With distinct positive backgrounds, set
\[
\lambda_1(t)=1+\frac1{t+1},\qquad
\lambda_2(t)=\frac{111}{100}+\frac{7}{2(t+2)^2}.
\]
Their difference, after multiplication by \(100(t+1)(t+2)^2\), is exactly
\[
-(t-3)(11t^2-12t+2),
\]
with three positive roots \((6-\sqrt{14})/11\), \((6+\sqrt{14})/11\), and \(3\). For a common background \(\mu=1\), the two distinct curves \(1+(t+1)^{-1}\) and \(1+17/[2(t+3)^2]\) meet at the two positive roots \((5\pm\sqrt{17})/4\).

**Lemma 2 (ordered-bin transfer).** If the integral of a continuous function \(g\) over a positive-length interval is zero, \(g\) must vanish at a point of that interval's interior, unless it vanishes identically on the interval. For intervals with disjoint interiors, zero integrals produce distinct roots, except when an interval is identically zero. All functions considered here are real analytic on \([0,\infty)\), so a function vanishing identically on one interval vanishes globally. Therefore equality of expected counts on four ordered windows gives four distinct roots of \(F\), and Lemma 1 yields identical parameters. With background known, three windows suffice by the two-crossing bound. The same proofs apply directly to distinct intensity evaluations.

**Lemma 3 (nonsingular Jacobians and sharp lower counts).** At a parameter point, the Jacobian columns of the continuous-time intensity with respect to \((\mu,K,c,p)\) are proportional (by nonzero scalar factors) to
\[
1,\quad z^{-p},\quad z^{-p-1},\quad z^{-p}\log z,\qquad z=t+c>0.
\]
No nontrivial linear combination of these four functions has four distinct zeros. Indeed, after multiplication by \(z^{p+1}\), it becomes
\[
h(z)=Az^{p+1}+Bz+C+Dz\log z.
\]
Then \(zh''(z)=Ap(p+1)z^p+D\), which either is identically zero (in which case \(h\) is affine) or has at most one zero. Twice applying Rolle's theorem bounds the number of distinct roots of \(h\) by three. Hence evaluations at four distinct times have nonsingular parameter Jacobian. The corresponding four-window integral Jacobian is also nonsingular: a null vector would give zero integrals of the associated nontrivial linear combination over four disjoint windows and thus four roots, a contradiction.

At fixed \(p\), the three derivative columns for \((\mu,K,c)\) are proportional to \(1,z^{-p},z^{-p-1}\). Multiplication by \(z^{p+1}\) gives \(Az^{p+1}+Bz+C\), whose second derivative has a constant strict sign when \(A\ne0\); otherwise it is affine. Thus a nonzero combination has at most two distinct roots, and three-window integrals (or three point evaluations) have rank three in these variables. The implicit function theorem now permits \(p\) to vary in an interval while \((\mu,K,c)\) vary smoothly to preserve all three observations. Every sufficiently nearby parameter remains strictly positive.

When \(\mu\) is known and \(p\) is fixed, the two derivative columns for \((K,c)\) are proportional to \(z^{-p},z^{-p-1}\). Multiplication by \(z^{p+1}\) gives an affine function, with at most one root. Hence any two-window integral Jacobian has rank two in \((K,c)\), and varying \(p\) gives an admissible one-parameter family preserving two observations. These establish both sharp sample-count statements.

## Verification

Run `python verify.py` in an environment with Python 3, SymPy, NumPy, and SciPy. It checks the exact cubic factorization, three positive crossings, the exact known-background two-crossing polynomial, and 150 independent positive parameter sets with four irregular disjoint windows. The program compares closed-form bin integrals with numerical quadrature and checks the full and reduced Jacobian ranks, for 1,050 numerical checks. The zero-count, universal injectivity and implicit-function arguments above are the infinite-domain proofs; numerical checks alone are not evidence of universal validity.

## Relationship to prior work

Holschneider et al. (2012) treat Bayesian uncertainty and dependence among the three modified-Omori parameters \((K,c,p)\) using stochastic earthquake times and observation cutoffs, not a four-parameter, exact finite-bin injectivity theorem. Gardonio et al. (2015) explicitly use a constant-background Omori-Utsu rate \(\mu+K/(t+c)^p\) when modeling post-Tohoku seismicity in Kanto, but their likelihood fits and geological conclusions do not state a globally sharp number of arbitrary disjoint *expected-count* windows sufficient to determine all four parameters. Here the exact crossing-number argument proves sufficiency and the implicit-function argument proves necessity, including the known-background contrast. Standard Rolle/Chebyshev arguments are an important mathematical antecedent; historical priority of this exact specialization is not independently certified.

## Limitations

The result assumes a single smooth aftershock component plus a constant background with fixed, known mainshock clock origin. It does not identify multiple mainshock sources, triggering cascades, time-varying backgrounds, catalogue incompleteness, or unmodeled aftershock-rate fluctuations. In real Poisson or ETAS observations, four realized counts are random and typically insufficient for reliable estimation despite structural injectivity of their four expectation parameters. A globally nonzero Jacobian is not a uniform lower singular-value bound: ill conditioning remains possible as parameters approach limiting models or windows cluster. No confidence interval or estimation accuracy is claimed.

## References

1. M. Holschneider, C. Narteau, P. Shebalin, Z. Peng, and D. Schorlemmer (2012), "Bayesian analysis of the modified Omori law," *Journal of Geophysical Research: Solid Earth* 117(B6), DOI: https://doi.org/10.1029/2011JB009054, publicly available 2012-06-30.
2. B. Gardonio, D. Marsan, O. Lengliné, B. Enescu, M. Bouchon, and J.-L. Got (2015), "Changes in seismicity and stress loading on subduction faults in the Kanto region, Japan, 2011–2014," *Journal of Geophysical Research: Solid Earth* 120, 2616–2626, DOI: https://doi.org/10.1002/2014JB011798, publicly available 2015-03-25.
