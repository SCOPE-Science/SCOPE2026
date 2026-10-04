# Five endpoint laws behind vanishing standardized anti-concentration
## Finding
Fix \(y>0\). Hu, Song and Tan prove that the standardized two-sided tail can be driven to zero for the Gamma, Pareto, Weibull, log-normal and Beta families. Along the same continuous witness paths used in their proofs, the decay has the following sharp form.

For \(G_\alpha\sim\operatorname{Gamma}(\alpha,1)\),
\[
\Pr\{|G_\alpha-\alpha|\ge y\sqrt\alpha\}=\frac{\alpha}{2}\log\frac1\alpha-\alpha(\log y+\gamma)+o(\alpha),\qquad \alpha\downarrow0.
\]
For unit-scale Pareto shape \(2+\varepsilon\),
\[
\Pr\{|P_{2+\varepsilon}-\mathbb EP_{2+\varepsilon}|\ge y\sqrt{\operatorname{Var}(P_{2+\varepsilon})}\}\sim\frac{\varepsilon}{2y^2},\qquad \varepsilon\downarrow0.
\]
For unit-rate Weibull shape \(\alpha\),
\[
-\alpha\log\Pr\{|W_\alpha-\mathbb EW_\alpha|\ge y\sqrt{\operatorname{Var}(W_\alpha)}\}\longrightarrow\frac2e,
\qquad \alpha\downarrow0.
\]
For log-normal log-scale \(\sigma\), independently of log-location,
\[
\Pr\{|L_\sigma-\mathbb EL_\sigma|\ge y\sqrt{\operatorname{Var}(L_\sigma)}\}\sim\frac{e^{-\sigma^2/2}}{y\sigma\sqrt{2\pi}},\qquad \sigma\to\infty.
\]
For \(B_q\sim\operatorname{Beta}(1,q)\),
\[
\Pr\{|B_q-\mathbb EB_q|\ge y\sqrt{\operatorname{Var}(B_q)}\}=\frac q2\log\frac1q-q\log\frac{y}{\sqrt2}+o(q),\qquad q\downarrow0.
\]
Thus the zero anti-concentration results arise through several genuinely different endpoint scales. In the Gamma and Beta cases, the leading coefficient is one half of that suggested by the source's convenient upper bound. In the Weibull case the exact exponential rate is \(2/e\), twice the rate delivered by the source's upper bound.

## Assumptions and scope
The threshold \(y\) is any fixed positive real number. Gamma uses unit scale, Pareto uses unit lower endpoint, Weibull uses unit rate, and log-normal uses arbitrary log-location because the standardized event is location-scale invariant in the relevant parameterization. Beta is restricted to the source's witness path \(\operatorname{Beta}(1,q)\). The claim concerns these endpoint paths; it does not claim an optimal rate after jointly optimizing all parameters of the Beta family, nor a uniform expansion when \(y\) varies with the endpoint parameter.

## Proof
For Gamma, when \(\alpha<y^2\), the lower standardized threshold is negative, hence with \(t_\alpha=\alpha+y\sqrt\alpha\),
\[
P_\Gamma(\alpha;y)=\frac{\Gamma(\alpha,t_\alpha)}{\Gamma(\alpha)}.
\]
On \([t_\alpha,1]\), replacing \(x^{\alpha-1}\) by \(x^{-1}\) changes the numerator by at most \(O(\alpha\log^2(1/t_\alpha))=o(1)\); the contribution on \([1,\infty)\) changes by \(O(\alpha)\). Therefore
\[
\Gamma(\alpha,t_\alpha)=E_1(t_\alpha)+o(1)=-\gamma-\log t_\alpha+o(1).
\]
Since \(t_\alpha=y\sqrt\alpha(1+o(1))\) and \(1/\Gamma(\alpha)=\alpha+O(\alpha^2)\), the stated two-term Gamma expansion follows.

For Pareto, the source's exact tail formula gives, with \(r=2+\varepsilon\),
\[
P_{\rm Par}(\varepsilon;y)=\left(\frac{1+\varepsilon}{2+\varepsilon+y\sqrt{(2+\varepsilon)/\varepsilon}}\right)^{2+\varepsilon}.
\]
The squared base divided by \(\varepsilon\) tends to \(1/(2y^2)\), while the extra power \(\varepsilon\) contributes a factor tending to one because \(\varepsilon\log\varepsilon\to0\).

For Weibull, write
\[
m_\alpha=\Gamma(1+1/\alpha),\qquad s_\alpha^2=\Gamma(1+2/\alpha)-m_\alpha^2.
\]
Stirling's formula shows \(m_\alpha/s_\alpha\to0\). The exact Weibull survival function therefore gives
\[
-\alpha\log P_{\rm W}(\alpha;y)=\alpha(m_\alpha+ys_\alpha)^\alpha.
\]
Moreover,
\[
\frac\alpha2\log\Gamma(1+2/\alpha)=\log(2/\alpha)-1+o(1),
\]
so \((m_\alpha+ys_\alpha)^\alpha=(2/(e\alpha))(1+o(1))\), proving the limit \(2/e\).

For log-normal, after standardizing the logarithm the upper-tail normal threshold is
\[
z_\sigma=\frac\sigma2+\frac1\sigma\log\left(1+y\sqrt{e^{\sigma^2}-1}\right)=\sigma+\frac{\log y}{\sigma}+o(\sigma^{-1}).
\]
Thus \(z_\sigma^2=\sigma^2+2\log y+o(1)\), and Mills' ratio \(1-\Phi(z)\sim e^{-z^2/2}/(z\sqrt{2\pi})\) gives the stated asymptotic.

For \(B_q\sim\operatorname{Beta}(1,q)\), the upper standardized threshold exceeds one for small \(q\), and the lower threshold gives exactly
\[
P_\Beta(q;y)=1-c_q^q,\qquad c_q=\frac{q+y\sqrt{q/(q+2)}}{1+q}.
\]
Now \(\log c_q=\frac12\log q+\log(y/\sqrt2)+o(1)\) and \(q\log c_q\to0\). Expanding \(1-e^{q\log c_q}\) yields the claimed two-term formula.

For comparison with the simplifying bounds in the source, its Gamma bound is
\[
1-e^{-\alpha}\frac{\alpha^{\alpha}}{\Gamma(1+\alpha)}=\alpha\log(1/\alpha)(1+o(1)),
\]
while the exact Gamma probability has leading coefficient \(1/2\). Its Beta bound is \(1-(q/(1+q))^q=q\log(1/q)(1+o(1))\), again twice the exact leading coefficient. Its Weibull bound is \(\exp[-m_\alpha^\alpha]\), and Stirling gives \(-\alpha\log \exp[-m_\alpha^\alpha]\to1/e\), whereas the exact standardized event has limit \(2/e\).

## Verification
The accompanying script `verify_endpoint_rates.py` evaluates the exact formulas at three fixed values of \(y\) and endpoint parameters deep in the asymptotic regime. It checks that the exact-to-asymptotic ratios for Gamma, Beta, Pareto and log-normal are close to one, and that the normalized Weibull logarithmic rate is close to \(2/e\). These finite evaluations are consistency checks only; the proof above establishes the limits.

The derivations were also checked against the exact formulas in Propositions 3.5--3.9 of Hu, Song and Tan. Their Gamma and Beta proofs use upper bounds whose first-order sizes are respectively \(\alpha\log(1/\alpha)\) and \(q\log(1/q)\), whereas the exact probabilities above have one-half those leading coefficients. Their Weibull upper bound has normalized exponent tending to \(1/e\), whereas the exact standardized threshold has exponent tending to \(2/e\).

## Relationship to prior work
Hu, Song and Tan prove that the anti-concentration infimum is zero for all five families and display the exact witness probabilities or inequalities sufficient to take the endpoint limit. Their stated results are qualitative at these endpoints: the Gamma and Beta arguments deliberately replace the standardized threshold by a simpler one, the Weibull argument uses the mean as a lower threshold, and the log-normal argument only sends a normal threshold to infinity. The present claim extracts the sharp endpoint laws for the standardized events themselves and shows that the simplifying bounds can lose leading constants.

Targeted searches for the five-family standardized endpoint laws, the individual Gamma and Beta logarithmic terms, the Pareto variance-boundary rate, the Weibull constant \(2/e\), and the log-normal normal-tail equivalent found the motivating paper but no source stating this collection of sharp standardized asymptotics. Nearby published results on Gamma endpoint localization, Gamma-sum quantiles, and block-product anti-concentration concern different objects and do not imply these formulas.

## Limitations
The originality search cannot exclude an equivalent calculation under different distribution-asymptotic terminology. The Beta statement is path-specific, not a joint two-parameter optimization theorem. The expansions are pointwise in each fixed \(y>0\); no uniformity as \(y\downarrow0\) or \(y\to\infty\) is asserted. The numerical script is not a proof and is not used to certify an infinite asymptotic statement.

## References
1. Z.-C. Hu, R. Song and Y. Tan, *On the anti-concentration functions of some familiar families of distributions*, arXiv:2401.09998, first posted 2024-01-18; *Mathematical Theory and Applications* 44 (2024), 1--15, DOI: 10.3969/j.issn.1006-8074.2024.01.001.
2. NIST Digital Library of Mathematical Functions, standard asymptotic expansions for the Gamma function, exponential integral, complementary error function, and normal tail.
