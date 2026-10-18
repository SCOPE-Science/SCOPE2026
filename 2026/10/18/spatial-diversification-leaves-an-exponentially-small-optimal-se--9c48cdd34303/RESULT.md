# Spatial diversification leaves an exponentially small optimal seed reserve

## Finding
Consider an annually reproducing seed population with a fully mixed regional seed bank and \(k\ge1\) equally weighted, environmentally independent habitat patches. Each year a fraction \(g\in[0,1]\) germinates and is divided equally among the patches. Each patch independently permits \(B>0\) new seeds per germinated seed with probability \(p\in(0,1)\), and produces no seeds otherwise. Nongerminating seeds survive with probability \(s\in(0,1]\). Write \(g_k\) for the allocation that maximizes almost-sure long-run logarithmic seed-bank growth.

**Theorem.** If \(Bp\le s\), then \(g_k=0\) uniquely for all \(k\). If \(Bp>s\), then, for every finite \(k\), the maximizer is unique and lies strictly between zero and one; moreover
\[
0<g_1<g_2<\cdots<1,\qquad \lim_{k\to\infty}g_k=1,
\]
and the surviving dormant fraction has the sharp rare-catastrophe asymptotic
\[
\boxed{\displaystyle 1-g_k\sim\frac{Bp}{Bp-s}(1-p)^k.}
\]
The optimal logarithmic growth rate increases strictly with \(k\) and tends to \(\log(Bp)\). These claims concern the specified density-independent, fully remixed stochastic population, not general local seed-bank dynamics.

For the exact example \(p=1/2\), \(s=4/5\), and \(B=16/5\), the unique optima are \(g_1=1/3\) and \(g_2=1/\sqrt3\), while \(1-g_k\sim2^{1-k}\). Thus even arbitrarily extensive but finite spatial diversification does not make complete germination optimal: an exponentially small seed reserve remains because all patches can fail in the same year.

## Assumptions and scope
Time is integer-valued. At the beginning of each year, the regional seed bank contains a nonnegative real quantity of viable seeds. Seeds make the same stationary germination decision independently in the deterministic-proportion (large-population) approximation. Nongerminating seeds contribute a fraction \(s\) to the following year's seed pool; germinated seeds are distributed in equal proportions across exactly \(k\) patches. Patch quality indicators are independent Bernoulli variables of probability \(p\), independently resampled each year, and their favorable-year fecundity is \(B\). All seeds produced are pooled before the next year's decision. There is no density dependence, demographic sampling noise, dispersal mortality, environmental cross-patch correlation, delayed maturation, or age-dependent seed survival. This yields a strictly positive annual multiplier for \(g<1\):
\[
R_{k,g}=s(1-g)+\frac{Bg}{k}K_k,\qquad K_k\sim\operatorname{Binomial}(k,p).
\]
The logarithmic fitness, interpreted as \(-\infty\) at zero multipliers, is
\[
L_k(g)=\mathbb E\log R_{k,g}=\sum_{j=0}^k\binom{k}{j}p^j(1-p)^{k-j}\log\left(s(1-g)+\frac{Bgj}{k}\right).
\]
For a stationary choice of \(g\) and positive initial seed mass, the strong law of large numbers identifies \(L_k(g)\) as the almost-sure long-run logarithmic growth rate whenever \(g<1\). When \(g=1\), an all-unfavorable year occurs almost surely eventually for every finite \(k\); the growth rate is \(-\infty\).

## Proof
**1. Strict concavity and interior optima.** At \(g<1\), differentiation of the finite expectation gives
\[
L'_k(g)=\mathbb E\frac{BX_k-s}{s(1-g)+BgX_k},\qquad X_k=K_k/k,
\]
and
\[
L''_k(g)=-\mathbb E\frac{(BX_k-s)^2}{[s(1-g)+BgX_k]^2}<0.
\]
Strict inequality follows already from the all-unfavorable outcome, which has probability \((1-p)^k>0\). Since \(L'_k(0)=(Bp-s)/s\), the cases \(Bp\le s\) have the unique boundary maximizer \(g_k=0\). If \(Bp>s\), the derivative at zero is positive, whereas \(L'_k(g)\to-\infty\) as \(g\uparrow1\), again because the all-unfavorable event has positive probability. Thus exactly one interior critical point, the unique maximizer, exists.

**2. Strict increase of germination with patch number.** For each fixed \(g\in(0,1)\), define
\[
\phi_g(x)=\frac{Bx-s}{s(1-g)+Bgx},\qquad
\phi_g''(x)=-\frac{2B^2sg}{[s(1-g)+Bgx]^3}<0.
\]
For \(k+1\) Bernoulli observations, let \(Y_i\) be the average after deleting observation \(i\), so that \(X_{k+1}=\frac1{k+1}\sum_iY_i\). Strict Jensen gives \(\phi_g(X_{k+1})\ge\frac1{k+1}\sum_i\phi_g(Y_i)\), with strict inequality whenever not all Bernoulli observations agree, an event of strictly positive probability. Every \(Y_i\) has the law of \(X_k\). Consequently
\[
L'_{k+1}(g)>L'_k(g)\quad(0<g<1).
\]
Evaluating this inequality at the unique zero \(g_k\) of \(L'_k\), then using that \(L'_{k+1}\) is strictly decreasing, proves \(g_{k+1}>g_k\). The same deletion/Jensen argument applied to the strictly concave function \(x\mapsto\log[s(1-g)+Bgx]\) yields \(L_{k+1}(g)>L_k(g)\) for every \(g>0\), so optimized logarithmic growth improves strictly.

**3. Convergence to complete germination.** Fix any \(g\in(0,1)\). By the law of large numbers and bounded continuity,
\[
\lim_{k\to\infty}L'_k(g)=\frac{Bp-s}{s(1-g)+Bpg}>0.
\]
The unique critical point eventually exceeds each fixed \(g<1\); therefore \(g_k\to1\). Jensen's inequality gives \(L_k(g)\le\log[s(1-g)+Bpg]\le\log(Bp)\). Taking the admissible trial choice \(g=1-1/k\) for \(k\ge2\), the multipliers converge in probability to \(Bp\). Their logarithms have expectations tending to \(\log(Bp)\): on \(X_k\ge p/2\) the logs are uniformly bounded and converge in probability; on the complementary event a Chernoff bound yields exponentially small probability and the logs have magnitude at most \(O(\log k)\) below. Hence \(L_k(g_k)\to\log(Bp)\).

**4. Sharp dormant reserve.** Put \(\delta_k=1-g_k\). The identity
\[
gL'_k(g)=1-s\mathbb E\left[\frac1{R_{k,g}}\right]
\]
shows that at the interior optimum, \(s\mathbb E[1/R_{k,g_k}]=1\). Separate the outcome \(K_k=0\):
\[
\frac1s=\frac{(1-p)^k}{s\delta_k}+
\mathbb E\left[\frac{\mathbf1_{\{K_k>0\}}}{s\delta_k+B(1-\delta_k)K_k/k}\right].
\]
The second term tends to \(1/(Bp)\). Indeed on \(K_k/k\ge p/2\) it is uniformly bounded for sufficiently large \(k\), and convergence in probability to \(1/(Bp)\) applies. On \(0<K_k/k<p/2\), the integrand is at most \(k/[B(1-\delta_k)]\), and the event's probability is exponentially small by a binomial Chernoff bound. Since \(\delta_k\to0\), this remainder is negligible. Thus
\[
\frac{(1-p)^k}{\delta_k}\longrightarrow 1-\frac{s}{Bp}=\frac{Bp-s}{Bp},
\]
which gives the stated asymptotic with a strictly positive prefactor.

**5. Exact example.** For \(p=1/2,s=4/5,B=16/5\), multiplication by the positive constant \(s\) does not change the optimizer. At one patch, the reduced fitness is \(\tfrac12\log(1-g)+\tfrac12\log(1+3g)\), so the critical point is \(1/3\). At two patches, the derivative is
\[
\frac14\left[-\frac1{1-g}+\frac2{1+g}+\frac3{1+3g}\right]
=\frac{1-3g^2}{(1-g)(1+g)(1+3g)},
\]
whose unique zero in \((0,1)\) is \(1/\sqrt3\). Here \(Bp/(Bp-s)=2\) and \(1-p=1/2\), yielding \(1-g_k\sim2^{1-k}\).

## Verification
The standalone `verification/check_seedbank.py` uses Python standard-library exact rationals to establish the one-patch optimum, the reduced two-patch derivative identity, and 1,012 derivative inequalities spanning multiple admissible parameter choices. Arbitrary-precision decimal bisection checks the unique critical points for patch counts 1 through 60 and the approach of the rescaled reserve toward the proven constant 2. These are finite checks, not replacements for the strict Jensen argument or the rare-event asymptotic proof. Running `python verification/check_seedbank.py` from the document directory reproduces the output. The source package was reread and the program run successfully.

## Relationship to prior work
Cohen (1966) established the ecological logic of delayed germination in a fluctuating environment; in particular, the one-environment bet-hedging optimization is classical. Bascompte, Possingham, and Roughgarden (2002) established a spatially averaged geometric-mean growth criterion and the benefit of more uncorrelated patches under full dispersal. Klinkhamer and colleagues (1987), and Cohen and Levin (1987), studied interactions between dormancy and dispersal; their qualitative risk-substitution mechanism is not claimed as new. Mathias and Kisdi (1999) studied germination evolution with spatially heterogeneous, density-dependent population dynamics. Snyder (2006) demonstrated that environmental temporal autocorrelation can reverse intuitive dispersal/dormancy relationships. The present theorem instead fixes complete spatial mixing and independent binary patch outcomes and optimizes the temporal reserve **as the integer number of independent patches changes**. Its claimed added content is the strict all-integer optimizer ordering, finite-patch interiority and sharp \((1-p)^k\) reserve prefactor, which do not follow merely from the cited qualitative dispersal conclusions or from a geometric-mean persistence criterion. One close historical paper (Bascompte et al.) and portions of the 1987 full texts could not be read in full; a hidden equivalent specialization remains possible.

## Limitations
This is a theorem for an explicit simplified stochastic growth model, not a field-validated recommendation. It does not incorporate carrying capacities, local seed banks, demographic sampling, finite-population extinction, non-independent patches, correlation across years, density-dependence, dormancy age structure, or dispersal costs. Positive optimized logarithmic growth is not guaranteed when \(Bp>s\) (for instance, \(Bp\) could still be less than 1). Stronger coverage in incompletely accessible historical dispersal/dormancy literature remains a novelty risk; no independent external audit has been performed.

## References
1. Cohen, D. (1966). *Optimizing reproduction in a randomly varying environment*. Journal of Theoretical Biology. DOI: 10.1016/0022-5193(66)90188-3.
2. Klinkhamer, P. G. L., de Jong, T. J., Metz, J. A. J., and Val, J. (1987). *Life history tactics of annual organisms: The joint effects of dispersal and delayed germination*. Theoretical Population Biology 32, 127–156. DOI: 10.1016/0040-5809(87)90044-X.
3. Cohen, D., and Levin, S. A. (1987). *The interaction between dispersal and dormancy strategies in varying and heterogeneous environments*. Lecture Notes in Biomathematics 71, 110–122. DOI: 10.1007/978-3-642-93360-8_11.
4. Mathias, A., and Kisdi, É. (1999). *Evolutionary branching and coexistence of germination strategies*. IIASA Interim Report IR-99-014. https://pure.iiasa.ac.at/id/eprint/5925/1/IR-99-014.pdf.
5. Mathias, A., Kisdi, É., and Olivieri, I. (2001). *Divergent evolution of dispersal in a heterogeneous landscape*. Evolution 55, 246–259. DOI: 10.1111/j.0014-3820.2001.tb01290.x.
6. Bascompte, J., Possingham, H., and Roughgarden, J. (2002). *Patchy populations in stochastic environments: Critical number of patches for persistence*. The American Naturalist 159, 128–137. DOI: 10.1086/324793.
7. Snyder, R. E. (2006). *Multiple risk reduction mechanisms: Can dormancy substitute for dispersal?* Ecology Letters 9, 1106–1114. DOI: 10.1111/j.1461-0248.2006.00962.x.
