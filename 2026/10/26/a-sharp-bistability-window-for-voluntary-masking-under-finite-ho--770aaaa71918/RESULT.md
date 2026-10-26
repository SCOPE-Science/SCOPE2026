# A sharp bistability window for voluntary masking under finite-horizon Poisson exposure

## Finding

A single-population mask game with no conformity rewards, mandates, heterogeneous risk types, or behavioral response in disease prevalence can have **two distinct interior symmetric Nash equilibria** and two locally attracting states under replicator adjustment. The sole nonlinearity needed is the probability of at least one successful infectious contact during a fixed observation horizon.

**Theorem.** Fix mask attenuation \(0<q<1\), effective Poisson exposure \(\lambda>0\), infection-loss severity \(\ell>0\), and mask cost \(c>0\). Put
\[
m(p)=1-(1-q)p,\qquad
H(m)=e^{-\lambda q m}-e^{-\lambda m},\qquad 0\le p\le1.
\]
For the game defined below, there are two distinct interior symmetric Nash masking fractions if and only if
\[
\frac{\log(1/q)}{1-q}<\lambda<\frac{\log(1/q)}{q(1-q)}
\quad\text{and}\quad
\ell\max\{H(q),H(1)\}<c<\ell H(m_*),
\qquad m_*:=\frac{\log(1/q)}{\lambda(1-q)}.
\]
In that case there are exactly two interior fractions \(0<p_-<p_+<1\). For the replicator dynamics
\[
\dot p=p(1-p)\bigl[\ell H(m(p))-c\bigr],
\]
\(p=0\) and \(p=p_+\) are locally asymptotically stable, while \(p=p_-\) and \(p=1\) are unstable. The symmetric Nash equilibria are precisely \(p=0,p_-,p_+\). For **every** choice of parameters, there are at most two interior symmetric Nash equilibria; outside the strict exposure interval above there is at most one.

There is a fully explicit instance: with \(q=1/2\), \(\lambda=2\), \(\ell=1\), and \(c=63/256\), the two interior symmetric Nash fractions are
\[
p_-=2\left(1+\log\frac7{16}\right)\approx0.3466428536,\qquad
p_+=2\left(1+\log\frac9{16}\right)\approx0.8492717102.
\]
Thus voluntary nonmasking and sustained partial masking are both locally attracting, separated by an unstable adoption threshold.

## Assumptions and scope

A continuum of identical agents independently chooses either an unmasked action of contact attenuation \(1\), at zero private cost, or a masked action of attenuation \(q\), incurring fixed private cost \(c\). Against population masking share \(p\), the mean attenuation of contacts is \(m(p)\). Over a fixed horizon, successful infectious contacts for a tagged susceptible are Poisson with mean \(\lambda a m(p)\), where \(a=1\) or \(a=q\) is the tagged agent's attenuation. The expected infection loss is \(\ell\) times the probability of at least one such contact. Infection prevalence and exposure rates are frozen over this behavioral adjustment horizon; agents are negligible, so a unilateral deviation does not alter \(p\).

Consequently the unmasked and masked payoffs, respectively, are
\[
U_N(p)=-\ell\bigl(1-e^{-\lambda m(p)}\bigr),\qquad
U_M(p)=-c-\ell\bigl(1-e^{-\lambda q m(p)}\bigr).
\]
The masked-minus-unmasked payoff is
\[
G(p)=U_M(p)-U_N(p)=\ell H(m(p))-c.
\]
An interior symmetric Nash fraction is exactly a zero of \(G\). The pure endpoints are Nash if and only if \(G(0)\le0\), respectively \(G(1)\ge0\). Replicator adjustment is an explicitly specified behavioral rule, not a prediction that the epidemic itself follows replicator dynamics.

## Proof

**Step 1: unique possible turning point.** Direct differentiation yields
\[
H'(m)=\lambda\bigl(e^{-\lambda m}-q e^{-\lambda q m}\bigr).
\]
Its zero condition is \(e^{-\lambda(1-q)m}=q\), hence the unique stationary point is \(m_*\) stated in the theorem. Since \(H'(0)=\lambda(1-q)>0\), and the exponential ratio strictly falls with \(m\), \(H\) increases before \(m_*\) and decreases after it. Therefore it has a unique strict maximum at \(m_*\) on its positive domain. Because \(m(p)\) strictly decreases from \(1\) to \(q\), there are at most two solutions of \(G(p)=0\) inside \((0,1)\).

**Step 2: exact two-root criterion.** The maximum lies strictly inside the accessible attenuation interval precisely when \(q<m_*<1\). Solving both inequalities for \(\lambda\) gives the stated strict exposure window. In that window, the composite \(p\mapsto H(m(p))\) strictly increases on \((0,p_*)\) and strictly decreases on \((p_*,1)\), where \(p_*=(1-m_*)/(1-q)\). A horizontal line \(c/\ell\) crosses both monotone branches at points strictly inside \((0,1)\) precisely when it lies strictly above **both endpoint values** and strictly below the peak. This gives the necessary and sufficient cost inequalities and uniqueness of \(p_-,p_+\). Outside the exposure window the composite is monotone, hence has at most one interior root. At equalities or tangent levels, the count of *distinct* interior roots is at most one.

**Step 3: game equilibria and stability.** Under the strict two-root inequalities, \(G(0)<0\), \(G(1)<0\), and its signs along increasing \(p\) are negative, positive, negative. The endpoint Nash test therefore admits \(p=0\) and excludes \(p=1\); both interior zeros are symmetric Nash mixtures. For \(\dot p=p(1-p)G(p)\), the negative-to-positive crossing at \(p_-\) repels, the positive-to-negative crossing at \(p_+\) attracts, \(p=0\) attracts from its right, and \(p=1\) repels toward its left. These are local asymptotic statements on the invariant interval \([0,1]\). No additional equilibria exist.

**Step 4: exact rational example.** For \(q=1/2\), \(\lambda=2\), let \(y=e^{-m(p)}\). Then \(G(p)=y-y^2-63/256\); the exact factorization is
\[
y-y^2-\frac{63}{256}
=-\left(y-\frac7{16}\right)\left(y-\frac9{16}\right).
\]
As \(p\) increases, \(y\) strictly increases from \(e^{-1}\) to \(e^{-1/2}\). The elementary bounds \(e>5/2\) and \(e<3\) give
\[
e^{-1}<\frac25<\frac7{16}<\frac9{16}<\frac1{\sqrt3}<e^{-1/2},
\]
where \(9/16<1/\sqrt3\) follows from \(243<256\). Both roots therefore occur strictly inside the masking interval, yielding the stated logarithmic fractions. The quadratic is positive between the roots and negative outside them, establishing the sign pattern independently of floating-point computation.

## Verification

The standalone Python program `verify_poisson_mask.py` uses exact fractions to check the two rational roots, then checks their interior location, endpoint payoff signs, intermediate payoff sign, and stability-direction signs numerically. It also samples four attenuation values and representative exposure levels on either side of the exact turning-point boundaries, including checks that the predicted bistability window has two crossings. Run `python verify_poisson_mask.py` with the Python standard library. The printed decimal fractions are corroborative; **the proof of the universal parameter classification is analytic, not empirical**.

## Relationship to prior work

Altman, Datar, de Pellegrini, Perlaza and Menasché [1] formulate a Poisson-contact mask game with a *bilinear infection-rate payoff* and analyze its symmetric single- and multiple-risk-type equilibria. Their Appendix A discusses nonlinear infection probabilities under thinning (particularly section A.6's daily Poisson contact-count formulation) but explicitly leaves the resulting games for future analysis. The present theorem analyzes one precisely specified finite-horizon Poisson-count specialization and gives an exact two-interior-equilibrium criterion. It does **not** claim that the distinct spatiotemporal kernel in their Appendix A.5 is solved.

For contrast, the first-order rate approximation to the present finite-horizon payoff gives
\[
G_{\mathrm{lin}}(p)=\ell\lambda(1-q)m(p)-c,
\]
which is strictly decreasing with \(p\) and cannot yield the coexistence of a stable all-unmasked state and a distinct stable interior masking state. The saturation of *probability of at least one infection*, rather than exogenous norm-reward or epidemic feedback, creates the extra turning point.

Kabir, Risa and Tanimoto [2] couple mask behavior to infection prevalence, cost and conformity effects. Yang and colleagues [3] study social-norm and institutional tipping, and Qiu and colleagues [4] study fear/peer-pressure-driven coevolution on multilayer networks. None of those distinct behavioral mechanisms mathematically implies the two-root criterion for a frozen-prevalence Poisson mask game. The subsequent Pei–Xu–Zhang networked voluntary-mask model [5] is thematically close but its available abstract describes coevolving epidemic and strategy ODEs rather than this fixed-horizon root classification; complete text could not be compared.

## Limitations

The result assumes a continuum of symmetric agents, multiplicative contact attenuation, independent Poisson transmission attempts, a frozen infectious-contact environment, risk neutrality, constant severity and mask cost, and the specified replicator adaptation. It is not a theorem for finite stochastic populations, endogenous epidemics, alternative point-process distributions, type heterogeneity, or stochastic evolutionary stability. The apparent behavioral bistability is a property of this particular game and revision dynamic, not an empirical prediction for actual mask adoption. Relevant unindexed research or the inaccessible full text of [5] may contain related special cases; independent literature validation remains outstanding.

## References

[1] E. Altman, M. Datar, F. de Pellegrini, S. Perlaza, and D. S. Menasché, *The Mask Game with Multiple Populations*, Dynamic Games and Applications **12** (2022), 147–167. DOI: 10.1007/s13235-022-00431-5. Preprint HAL: hal-03527522 (submitted 2022-01-16).

[2] K. M. A. Kabir, T. Risa, and J. Tanimoto, *Prosocial behavior of wearing a mask during an epidemic: an evolutionary explanation*, Scientific Reports **11** (2021), 12621. DOI: 10.1038/s41598-021-92094-2.

[3] L. Yang et al., *Sociocultural determinants of global mask-wearing behavior*, Proceedings of the National Academy of Sciences **119** (2022), e2213525119. DOI: 10.1073/pnas.2213525119.

[4] Z. Qiu et al., *Understanding the coevolution of mask wearing and epidemics: A network perspective*, Proceedings of the National Academy of Sciences **119** (2022), e2123355119. DOI: 10.1073/pnas.2123355119.

[5] S. Pei, F. Xu, and B. Zhang, *A Game Theoretical Analysis of Voluntary Mask Wearing for Epidemic Spreading Over Complex Networks*, Dynamic Games and Applications **15** (2025), 1494–1516. DOI: 10.1007/s13235-025-00644-4.
