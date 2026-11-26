# Exact finite-amplitude resonance boundary for alternating survival

## Finding

Fix a reproductive coefficient \(R>0\) and two alternating survival fractions \(s_0,s_1\in(0,1]\). Set \(a=Rs_0\), \(b=Rs_1\), \(h=(a+b)/2\), \(d=(a-b)/2\), and \(Q=\sqrt{1+d^2}\). Let a positive initial abundance follow
\[
x_{t+1}=\frac{Rs_{t\bmod2}\,x_t}{1+x_t^2}.
\]
All positive trajectories tend to extinction if \(ab\le1\). If \(ab>1\), every positive trajectory converges in the two seasonal phases to the unique positive seasonal orbit \((u,v)\). The long-run arithmetic mean \(\bar x=(u+v)/2\) and the equilibrium \(x_*=\sqrt{h-1}\) for constant survival \((s_0+s_1)/2\) satisfy
\[
\boxed{\bar x^{\,2}-x_*^2=\frac{(Q-1)(h-Q-2)}{2}.}
\]
For unequal seasons in the persistent regime, alternating survival enhances the mean when \(h>Q+2\), suppresses it when \(Q<h<Q+2\), and ties at \(h=Q+2\). Equal seasons tie.

**Fixed-mean contrast threshold.** For fixed feasible \(R,h\) with \(h>1\), the nonzero persistent amplitudes \(\delta=|d|\) satisfy exactly
\[
0<\delta<\sqrt{h^2-1},\qquad \delta\le R-h .
\]
If \(1<h\le3\), all such amplitudes suppress the mean. If \(h>3\), define
\[
\boxed{\delta_c=\sqrt{(h-2)^2-1}.}
\]
Among feasible persistent contrasts the effect is enhancement for \(\delta<\delta_c\), equality at \(\delta=\delta_c\), and suppression for \(\delta>\delta_c\). The tie at nonzero contrast is accessible exactly when \(R-h\ge\delta_c\); both enhancement and suppression are accessible exactly when \(R-h>\delta_c\). If \(R-h<\delta_c\), all feasible nonzero persistent contrasts enhance the mean (there are no such contrasts when \(R=h\)).

For an exact same-mean comparison, take \(R=10\) and average survival \(1/2\), so \(h=5\) and \(x_*=2\). Alternating survival \((7/10,3/10)\) gives \(\bar x^2=2\sqrt5>4\), whereas \((8/10,2/10)\) gives \(\bar x^2=2\sqrt{10}-5/2<4\). Both are feasible and persistent. In contrast, with \(R=6\) and \(h=5\), the cap \(\delta\le1\) prevents reaching \(\delta_c=\sqrt8\).

## Assumptions and scope

Abundance is a positive real variable. Seasonal survival multiplies density-limited recruitment with the same quadratic denominator in both seasons; reproduction, survival fractions, and the density scale are otherwise fixed as specified. There is no demographic or environmental stochasticity, immigration, age structure, density-dependent harvest, time-varying baseline fecundity, or adaptive harvesting. Comparisons hold the arithmetic mean of the survival fractions fixed, not harvested biomass, effort cost, or the mean of seasonal carrying capacities. The statistic is long-run arithmetic mean census abundance, not yield or profit.

## Proof

Write \(f_c(x)=cx/(1+x^2)\). First let \(ab>1\). Since \(ab=h^2-d^2\) and \(h>0\), this is equivalent to \(h>Q\). Put \(r=d+Q>0\), so \(r^{-1}=Q-d\), \(r-r^{-1}=a-b\), and \(r+r^{-1}=2Q\). The positive numbers
\[
u^2=(h-Q)/r,\qquad v^2=r(h-Q)
\]
satisfy \(v=ru\), \(1+u^2=a/r\), and \(1+v^2=br\); hence \(f_a(u)=v\) and \(f_b(v)=u\). Conversely, the two transition equations for a positive seasonal orbit, with \(\rho=v/u\), imply \(1+u^2=a/\rho\) and \(1+v^2=b\rho\). Substituting \(v^2=\rho^2u^2\) gives \(\rho^2-(a-b)\rho-1=0\), with the unique positive root \(r\). The orbit has minimal period two when \(a\ne b\) and is a fixed point when \(a=b\).

In log coordinates \(z=\log x\) a season has map \(g_c(z)=\log c+z-\log(1+e^{2z})\) with derivative \(-\tanh z\). Thus \(G=g_b\circ g_a\) satisfies \(|G'(z)|<1\) for every finite \(z\). With the fixed point \(z_*=\log u\) established above, the mean-value theorem shows that the even-season log iterates stay in the closed interval centered at \(z_*\) of radius \(|z_0-z_*|\). On this compact interval \(\sup |G'|<1\), proving geometric convergence to \(z_*\). The odd-season iterates converge to \(\log v\). In particular, the arithmetic time average converges to \((u+v)/2\).

For \(ab\le1\),
\[
\frac{x_{t+2}}{x_t}=\frac{ab}{(1+x_t^2)(1+x_{t+1}^2)}<1
\]
for each positive state. The even subsequence decreases to a limit \(L\ge0\). If \(L>0\), continuity of \(f_a\) makes the displayed ratio eventually bounded away from one, a contradiction. Thus \(L=0\) and \(x_{2t+1}=f_a(x_{2t})\to0\).

For the positive orbit, \(uv=h-Q\) and \(u^2+v^2=2Q(h-Q)\), so \(\bar x^2=(Q+1)(h-Q)/2\). The constant multiplier is \(h\) and its positive equilibrium satisfies \(x_*^2=h-1\). Subtracting gives the displayed factorization. Both means are positive, so their difference has the sign of the difference of their squares. When \(\delta>0\), \(Q>1\); the sign is the sign of \(h-Q-2\).

At fixed \(h>1\), persistence is equivalent to \(h^2-\delta^2>1\), which also ensures \(h-\delta>0\). Since the two multipliers are \(h\pm\delta\), the remaining feasibility condition is \(h+\delta\le R\), inclusive because full survival is allowed. The increasing function \(Q=\sqrt{1+\delta^2}\) gives the stated sign rule, and if \(h>3\), its unique threshold \(Q=h-2\) occurs strictly below the extinction amplitude. The survival cap can therefore exclude the tie, include it as an endpoint, or allow contrasts on both sides, as stated.

## Verification

Run `python3 verify.py` from the source package. The unchanged standard-library verifier checks exact rational phase and mean identities at seven triples, iterates 33 independent positive initial conditions in persistent, extinct and critical regimes with high-precision decimal arithmetic, and checks the signs in the two fixed-mean examples at \(R=10\). These finite checks do not establish global convergence or the feasibility restriction at fixed \(R,h\). The proof gives both analytically, including the equality endpoint when \(h+\delta=R\).

## Relationship to prior work

Franke and Yakubu (2006) developed a local small-amplitude signature for resonant versus attenuant population cycles. Their Smith model (§5.5) contains the present map when both multipliers exceed one and the seasonal carrying capacities obey \(k_t^2=r_t-1\) with \(r_t=Rs_t\). Their local signature compares with mean seasonal carrying capacity, not the equilibrium for the arithmetic mean survival fraction. Here the result gives the exact crossover and its accessibility at finite forcing for the constant-mean-survival benchmark. The small-amplitude results do not in themselves give this crossover.

Franke and Yakubu (2005) studied recruitment with additive survivors, not survival multiplying the quadratic recruitment function used here. Brauer and Sánchez (2003) considered periodic environmental and harvesting effects in continuous-time equations. The result is not a general statement of harvesting optimality.

## Limitations

The mean census population is not harvested biomass, reproductive value, conservation welfare, or a policy objective. Equal mean survival fractions do not imply equal effort or catch. The model assumes a deterministic period of two and a fixed quadratic density scale. No claim is made about more general density dependence, longer schedules, or stochastic environments.

## References

1. J. E. Franke and A.-A. Yakubu (2006), *Signature Function for Predicting Resonant and Attenuant Population 2-cycles*, Bulletin of Mathematical Biology 68, 2069–2104, DOI: 10.1007/s11538-006-9086-8. https://franke.math.ncsu.edu/Research/sigrevc.pdf
2. J. E. Franke and A.-A. Yakubu (2005), *Population models with periodic recruitment functions and survival rates*, Journal of Difference Equations and Applications 11, 1169–1184, DOI: 10.1080/10236190500386275. https://franke.math.ncsu.edu/Research/SurvivalFinal05.pdf
3. F. Brauer and D. A. Sánchez (2003), *Periodic Environments and Periodic Harvesting*, Natural Resource Modeling 16, 233–244, DOI: 10.1111/j.1939-7445.2003.tb00113.x.
4. S. M. Henson and J. M. Cushing (1997), *The effect of periodic habitat fluctuations on a nonlinear insect population model*, Journal of Mathematical Biology 36, 201–226.
