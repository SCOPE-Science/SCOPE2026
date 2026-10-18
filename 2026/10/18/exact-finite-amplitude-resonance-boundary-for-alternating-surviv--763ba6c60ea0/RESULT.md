# Exact finite-amplitude resonance boundary for alternating survival in a quadratic population map

## Finding

**Theorem.** Fix a reproductive coefficient \(R>0\) and two alternating survival fractions \(s_0,s_1\in(0,1]\). Define \(a=Rs_0\), \(b=Rs_1\), \(h=(a+b)/2\), \(d=(a-b)/2\), and \(Q=\sqrt{1+d^2}\). Let every positive initial abundance evolve by
\[
 x_{t+1}=\frac{Rs_{t\bmod2}\,x_t}{1+x_t^2}\quad(t=0,1,2,\ldots).
\]

If \(ab\le1\), all such trajectories tend to extinction. If \(ab>1\), they converge to the unique positive two-season orbit \((u,v)\) described explicitly below. The corresponding long-run arithmetic mean \(\overline{x}=(u+v)/2\) and the positive equilibrium \(x_*=\sqrt{h-1}\) of the **constant survival** map with survival \((s_0+s_1)/2\) satisfy
\[
\boxed{\overline{x}^{\,2}-x_*^2=\frac{(Q-1)(h-Q-2)}{2}.}
\]
Consequently, when \(a\ne b\) and \(ab>1\), alternating survival increases mean census population precisely when \(h>Q+2\), decreases it precisely when \(Q<h<Q+2\), and ties precisely at \(h=Q+2\). When \(a=b\) there is equality.

**Fixed-mean contrast threshold.** For fixed \(h>3\), write the amplitude \(\delta=|d|\). Within the exact persistence range \(0<\delta<\sqrt{h^2-1}\), increasing contrast crosses once from enhancement to suppression, at
\[
\boxed{\delta_c=\sqrt{(h-2)^2-1}.}
\]
If \(1<h\le3\), every nontrivial persistent contrast suppresses the mean relative to constant survival. Thus a small-contrast resonant regime does not imply resonance at all finite contrasts.

For an exact same-mean comparison, choose \(R=10\) and average survival \(1/2\), so \(h=5\) and \(x_*=2\). Alternating survival \((7/10,3/10)\) gives \(\overline{x}^{\,2}=2\sqrt5>4\), whereas the more uneven \((8/10,2/10)\) gives \(\overline{x}^{\,2}=2\sqrt{10}-5/2<4\). Both alternate between survival fractions strictly between zero and one and have positive globally attracting cycles.

## Assumptions and scope

Abundance is a positive real variable; reproduction is density-limited by the quadratic denominator, and the seasonal survival fraction multiplies recruitment. There is no demographic or environmental stochasticity, immigration, age structure, density-dependent harvest, time-varying baseline fecundity, or adaptive harvesting. Survival is applied after density-limited recruitment. Comparisons hold the **arithmetic mean of the survival fractions**, not harvested biomass, effort cost, or the mean of seasonal carrying capacities, fixed. The result is about long-run **mean census abundance**, not sustainable yield or profit. All claims quantify over every \(R>0\), all allowed survival fractions, and every positive initial population.

## Proof

Write \(f_c(x)=cx/(1+x^2)\). Suppose first \(ab>1\), equivalently \(h>Q\). Put \(r=d+Q>0\). As \(r^{-1}=Q-d\), the identities \(r-r^{-1}=2d=a-b\) and \(r+r^{-1}=2Q\) hold. Set
\[
 u^2=\frac{h-Q}{r},\qquad v^2=r(h-Q),\qquad u,v>0.
\]
We have \(v=ru\). Since \(1+u^2=(r+h-Q)/r=a/r\) and \(1+v^2=1+r(h-Q)=br\), direct substitution yields \(f_a(u)=v\) and \(f_b(v)=u\). Conversely, if a positive two-season orbit exists and \(v/u=\rho>0\), the two transition equations imply
\[
 1+u^2=\frac a\rho,\quad 1+v^2=b\rho,
 \quad \rho^2-(a-b)\rho-1=0.
\]
The last quadratic has exactly one positive root \(\rho=r\), so the positive orbit is unique. It has minimal period two when \(a\ne b\); for \(a=b\) it is a fixed point.

For global attraction, use the logarithmic population coordinate \(z=\log x\). A season with multiplier \(c\) becomes
\[
 g_c(z)=\log c+z-\log(1+e^{2z}),\qquad g_c'(z)=-\tanh z.
\]
For every finite real \(z\), \(|g_c'(z)|<1\). Hence the two-season map \(G=g_b\circ g_a\) satisfies \(|G'(z)|<1\) everywhere. The already constructed \(z_*=\log u\) is its fixed point. For any starting \(z_0\), the mean-value theorem gives \(|G(z)-z_*|<|z-z_*|\) unless \(z=z_*\); thus all even-season log iterates remain in the compact interval \([z_*-|z_0-z_*|,z_*+|z_0-z_*|]\). Continuity gives a uniform upper bound strictly below one for \(|G'|\) on this interval, establishing geometric convergence to \(z_*\). The intervening odd-season iterates converge to \(\log v\). This also proves uniqueness of any positive attracting orbit and excludes other long-run behavior for positive initial states.

If \(ab\le1\), then
\[
 \frac{x_{t+2}}{x_t}=\frac{ab}{(1+x_t^2)(1+x_{t+1}^2)}<1
\]
for every positive state. The even subsequence decreases to a limit \(L\ge0\). If \(L>0\), continuity of \(f_a\) makes the displayed ratio eventually bounded away from one, a contradiction. Thus \(L=0\), and \(x_{2t+1}=f_a(x_{2t})\to0\) as well.

For \(ab>1\), the product and sum of the positive orbit are \(uv=h-Q\) and \(u^2+v^2=(r+r^{-1})(h-Q)=2Q(h-Q)\). Therefore
\[
 \overline{x}^{\,2}=\frac{(u+v)^2}{4}
 =\frac{(Q+1)(h-Q)}2.
\]
The fixed survival fraction \((s_0+s_1)/2\) induces multiplier \(h\), so its fixed positive abundance is \(x_*^2=h-1\). Subtraction and factorization give
\[
 \overline{x}^{\,2}-x_*^2
 =\frac{(Q+1)(h-Q)-2(h-1)}2
 =\frac{(Q-1)(h-Q-2)}2.
\]
Since both populations are positive, the sign of the difference of their squares is exactly the sign of the abundance difference. For a genuinely alternating environment, \(Q>1\), and the sign is fixed by \(h-Q-2\). At fixed \(h>3\), \(Q=\sqrt{1+\delta^2}\) increases continuously from one to \(h\) as \(\delta\) spans the full persistence interval, with the unique zero \(\delta_c\) claimed above; when \(1<h\le3\), no positive amplitude meets \(h>Q+2\). This proves every assertion.

## Verification

The accompanying standard-library Python script `verify.py` checks exact rational phase identities at seven parameter triples with rational \(Q\), including positive, negative and zero mean differences, and iterates 33 independent positive initial-value trajectories across persistent, extinct and critical regimes with high-precision decimal arithmetic. The two exact fixed-mean examples are also checked numerically. Run `python3 verify.py` from the directory containing this document. The algebraic identities and global-convergence argument above, not finite experiments, provide the proof for all parameters.

## Relationship to prior work

Franke and Yakubu (2006) developed a local small-amplitude signature function for resonant versus attenuant cycles, including a Smith model with periodically varying carrying capacity and demographic rate (their §5.5 and Table 2). Their population comparison uses the mean of seasonal carrying capacities and their theorem assumes small parameter oscillations. Here survival multiplies density-limited reproduction, comparison is to a *constant mean survival fraction*, and the threshold is exact at arbitrary persistent forcing amplitude; these statements do not follow simply by identifying the local signature. In particular, fixing \(h=5\) and increasing \(|d|\) from two to three reverses its effect, a finite-contrast issue absent from the local signature.

Franke and Yakubu (2005) analyzed periodic survival in additive-survivor recruitment models, with constant or monotone Beverton–Holt recruitment, rather than the nonmonotone quadratic recruitment map here. Brauer and Sánchez (2003) considered periodic environmental and harvesting effects in continuous-time population equations. A relevant published spectral analysis of synchronous Ricker cycles concerns a different nonlinearity and a multispecies Floquet question. The exact finite-amplitude crossover stated here is not claimed to establish general harvesting optimality.

## Limitations

The mean census population is not the mean number harvested, reproductive value, conservation welfare, or a policy-optimality criterion. Constant mean survival fractions do not imply equal effort costs or equal cumulative catch. The result assumes homogeneous density-scale normalization, deterministic seasonal periodicity of length two, and multiplicative survival after recruitment. It does not cover noisy ecosystems, frequency-dependent management or general density-dependence exponents. No independent external scientific audit has been performed. Relevant older periodic-harvesting literature may contain implications not revealed by available full texts; originality is not proved by absence of a search hit.

## References

1. J. E. Franke and A.-A. Yakubu (2006), *Signature Function for Predicting Resonant and Attenuant Population 2-cycles*, Bulletin of Mathematical Biology 68, 2069–2104, DOI: 10.1007/s11538-006-9086-8. Author-posted full article: https://franke.math.ncsu.edu/Research/sigrevc.pdf ; online publication date 2006-07-25 (PubMed PMID 16865608).
2. J. E. Franke and A.-A. Yakubu (2005), *Population models with periodic recruitment functions and survival rates*, Journal of Difference Equations and Applications 11, 1169–1184, DOI: 10.1080/10236190500386275. Author-posted full article: https://franke.math.ncsu.edu/Research/SurvivalFinal05.pdf.
3. F. Brauer and D. A. Sánchez (2003), *Periodic Environments and Periodic Harvesting*, Natural Resource Modeling 16, 233–244, DOI: 10.1111/j.1939-7445.2003.tb00113.x (abstract examined; complete text not inspected).
4. S. M. Henson and J. M. Cushing (1997), *The effect of periodic habitat fluctuations on a nonlinear insect population model*, Journal of Mathematical Biology 36, 201–226 (historical population-resonance context).
