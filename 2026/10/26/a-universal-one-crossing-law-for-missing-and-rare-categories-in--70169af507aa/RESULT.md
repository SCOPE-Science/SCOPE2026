# A universal one-crossing law for missing and rare categories in Dirichlet-multinomial sampling

## Finding

Take a finite set of \(m\ge3\) categories with arbitrary positive Dirichlet concentrations \(\alpha_1,\ldots,\alpha_m\). Draw one probability vector from this Dirichlet distribution and then take \(n\) conditionally independent categorical observations. Write \(X_{n,i}\) for the count in category \(i\). Fix distinct categories \(i,j\) and an integer \(r\ge1\), and vary the sample size \(n\ge r\) without changing the concentration parameters. Define
\[
Q_n=\frac{\Pr(X_{n,i}=0,\ X_{n,j}=r)}{\Pr(X_{n,i}=0)\Pr(X_{n,j}=r)}.
\]
Set \(T=\sum_{h=1}^m\alpha_h\), \(a=\alpha_i\), \(b=\alpha_j\), and \(c=T-a-b>0\). With the rising factorial \((x)_k=x(x+1)\cdots(x+k-1)\), \((x)_0=1\), the exact formula and adjacent ratio are
\[
\boxed{Q_n=\frac{(c)_{n-r}(T)_n}{(T-b)_{n-r}(T-a)_n}},\qquad
\boxed{\frac{Q_{n+1}}{Q_n}=1-\frac{a(b+r)}{(T-b+n-r)(T-a+n)}<1.}
\]
Moreover \(Q_r>1\) while
\[
\lim_{n\to\infty}Q_n=\frac{\Gamma(T-b)\Gamma(T-a)}{\Gamma(c)\Gamma(T)}<1.
\]
Consequently **the covariance of the two indicators** \(\mathbf1_{\{X_{n,i}=0\}}\) and \(\mathbf1_{\{X_{n,j}=r\}}\) has precisely one transition, from positive to negative as the sample size increases, with at most one zero at the crossing. More precisely, the Gamma-interpolated function \(Q_x\) has a unique real root \(\rho>r\) of \(Q_\rho=1\); the covariance is positive for integer \(r\le n<\rho\), zero if \(n=\rho\) is an integer, and negative for \(n>\rho\).

For symmetric concentrations \(\alpha_1=\cdots=\alpha_m=\alpha>0\), fixed \(r\) and fixed \(\alpha\), the crossing has the refined large-category expansion
\[
\boxed{\rho_{m,r,\alpha}=rm-\frac{r(\alpha+1)}{2\alpha}+O(m^{-1})\qquad(m\to\infty).}
\]
The leading threshold \(n\sim rm\) is universal in \(\alpha\), while the order-one shift detects Dirichlet reinforcement. For unit concentration the crossing is **exactly** \(\rho_{m,r,1}=r(m-1)\) for every \(m\ge3\).

## Assumptions and scope

The Dirichlet vector is drawn once per sample; conditional on it, all \(n\) observations use that same vector. This is a single Dirichlet-multinomial component, not a mixture of components or a multinomial model with independent probability redraws per observation. All concentrations are strictly positive and fixed while \(n\) varies. The separate sampled categories satisfy \(i\ne j\); the assumption \(m\ge3\) ensures \(c>0\). The indicator covariance is \(\Pr(X_{n,i}=0)\Pr(X_{n,j}=r)(Q_n-1)\), so its sign is exactly the sign of \(Q_n-1\).

The symbols \(\Gamma\) and \(\psi\) are the Euler Gamma and digamma functions. The real interpolation is defined by replacing rising factorials with their Gamma ratios at real \(x\ge r\); it is a comparison device, not a claim that noninteger sample sizes are observable. No assertion concerns covariance between the untransformed counts \(X_{n,i}\) and \(X_{n,j}\), or the aggregate numbers of missing and rare categories.

## Proof

**Exact joint moments.** Integration of the multinomial likelihood against the Dirichlet density gives, for \(n\ge r\),
\[
\begin{aligned}
\Pr(X_{n,i}=0)&=\frac{(T-a)_n}{(T)_n},\\
\Pr(X_{n,j}=r)&=\binom nr\frac{(b)_r(T-b)_{n-r}}{(T)_n},\\
\Pr(X_{n,i}=0,X_{n,j}=r)&=\binom nr\frac{(b)_r(c)_{n-r}}{(T)_n}.
\end{aligned}
\]
Cancellation proves the displayed formula for \(Q_n\). Its adjacent ratio has numerator \((c+n-r)(T+n)\) and denominator \((T-b+n-r)(T-a+n)\). The denominator exceeds the numerator by exactly \(a(b+r)>0\), proving strict decrease in integer \(n\).

At \(n=r\), \(Q_r=(T)_r/(T-a)_r>1\). Gamma-ratio asymptotics give the displayed limiting constant. Its strict inequality follows from strict convexity of \(\log\Gamma\): for \(c,a,b>0\),
\[
\log\Gamma(c)+\log\Gamma(c+a+b)>
\log\Gamma(c+a)+\log\Gamma(c+b).
\]
Thus the integer sign sequence crosses once (with a possible equality).

**Unique real crossing.** For \(x\ge r\) put \(z=c+x-r\). The logarithmic derivative of the interpolated ratio is
\[
\frac{d}{dx}\log Q_x=
\bigl[\psi(z)-\psi(z+a)\bigr]
+\bigl[\psi(z+a+b+r)-\psi(z+b+r)\bigr].
\]
Since the trigamma function \(\psi'\) is strictly decreasing on positive arguments, the integral of \(\psi'\) over \([z+b+r,z+a+b+r]\) is strictly smaller than the integral over \([z,z+a]\). Hence this derivative is negative. Continuity, \(Q_r>1\), and \(\lim_{x\to\infty}Q_x<1\) give a unique real \(\rho>r\).

**Symmetric threshold and correction.** If all concentrations equal \(\alpha\), then
\[
Q_r=\prod_{j=0}^{r-1}\frac{m\alpha+j}{(m-1)\alpha+j},\qquad
\frac{Q_{h+1}}{Q_h}=1-\frac{\alpha(\alpha+r)}{((m-1)\alpha+h-r)((m-1)\alpha+h)}.
\]
Fix a bounded real offset \(u\) and set \(x=rm+u\). Expanding the first display yields
\[
\log Q_r=\frac r m+\frac{r/2-r(r-1)/(2\alpha)}{m^2}+O(m^{-3}).
\]
For integer \(h\), use
\[
\frac1{(z+h-r)(z+h)}=\frac1r\left(\frac1{z+h-r}-\frac1{z+h}\right),
\]
with \(z=(m-1)\alpha\); the sum telescopes to differences of \(r\) boundary terms. Since there are \(O(m)\) summands each of order \(m^{-2}\), the sum of quadratic logarithmic errors is \(O(m^{-3})\). For the real interpolation, the same digamma-integral formula used above yields, uniformly when \(x=rm+O(1)\),
\[
\frac{d}{dx}\log Q_x=-\frac{\alpha}{(\alpha+r)m^2}+O(m^{-3}).
\]
Integrating between neighboring integers extends the integer expansion to every bounded real offset \(u\), giving
\[
\log Q_{rm+u}=-\frac{\alpha u+r(\alpha+1)/2}{(\alpha+r)m^2}+O(m^{-3}).
\]
Uniformity on bounded \(u\)-intervals and the negative derivative of order \(m^{-2}\) locate the unique real zero at
\[
\rho_{m,r,\alpha}=rm-\frac{r(\alpha+1)}{2\alpha}+O(m^{-1}).
\]
For \(\alpha=1\) all rising-factorial ratios telescope **exactly** to
\[
Q_n-1=\frac{r(m-1)-n}{(m-1)(m+n-r-2)},
\]
which proves the finite exact crossing without any asymptotic approximation.

## Verification

The self-contained `verify.py` checks the Dirichlet-multinomial mass by independently enumerating finite weak compositions with exact rational arithmetic. It independently checks the three event probabilities, the normalized ratio, its adjacent recurrence, and the exact unit-concentration crossing. High-precision Gamma calculations test the second-order expansion at large category counts. Running `python verify.py` yields `PASS 29784 exact or high-precision assertions` with the stated dependencies. No finite computation is used as a proof of the unrestricted sign law or of the asymptotic remainder.

## Relationship to prior work

Gnedin, Hansen and Pitman (2007) develop moments and occupancy frequency counts for the classical fixed-frequency balls-in-boxes problem. Their full text treats deterministic sampling probabilities and infinite-box asymptotics, not the finite Dirichlet-mixed, fixed-pair vacancy/rare-frequency one-crossing theorem. Holmes, Harris and Quince (2012) give a single Dirichlet component and its multinomial sampling law as the building block for Dirichlet-multinomial mixtures in microbial species counts; their method concerns model inference and clustering, not covariance-sign transitions with sample size.

A published one-switch result for covariance of **total occupied richness** with a frequency count under uniform independent occupancy has a different variable, different changing parameter, and different sampling law. The present result fixes two labeled categories, varies \(n\), and allows arbitrary unequal positive Dirichlet concentrations. The joint probabilities themselves follow from the classical Dirichlet-multinomial mass, but the global monotonicity, unique crossing, and finite reinforcement-sensitive offset require the ratio and asymptotic arguments above.

## Limitations

The result is a theoretical statement for a single Dirichlet component and for one missing-versus-fixed-positive-frequency pair; mixtures of Dirichlet components need not preserve its one-crossing property. The Gamma root may coincide with an integer, so a zero covariance is allowed and occurs in the unit-concentration model. The expansion keeps \(r\) and \(\alpha\) fixed as \(m\to\infty\); it is not uniform in them. A broader historical theory of Dirichlet-multinomial association might imply the crossing theorem implicitly, and some older application papers could not be inspected in full; priority is therefore provisional.

## References

1. A. Gnedin, B. Hansen, J. Pitman, *Notes on the occupancy problem with infinitely many boxes: general asymptotics and power laws*, arXiv:math/0701718v1, first public 2007-01-24; *Probability Surveys* 4 (2007), 146–171.
2. I. Holmes, K. Harris, C. Quince, *Dirichlet Multinomial Mixtures: Generative Models for Microbial Metagenomics*, *PLoS ONE* 7 (2012), e30126; published 2012-02-03; DOI 10.1371/journal.pone.0030126.
3. P. de Valpine, A. N. Harmon-Threatt, *General models for resource use or other compositional count data using the Dirichlet-multinomial distribution*, *Ecology* 94 (2013), 2678–2687; DOI 10.1890/12-0416.1.
