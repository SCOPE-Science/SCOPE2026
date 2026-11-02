# The unique reinforcement threshold for pairwise singleton dependence in symmetric Pólya urns

## Finding

For every integer \(m\ge2\), take a symmetric \(m\)-colour Pólya urn with initial mass \(\alpha>0\) per colour and draw \(N=m+1\) times, restoring and reinforcing by one unit after each draw. Let \(C_i\) count draws of colour \(i\) and \(I_i=\mathbf1_{\{C_i=1\}}\) indicate a colour occurring exactly once. For distinct colours \(i,j\):

* If \(m=2,3,4\), then \(\operatorname{Cov}(I_i,I_j)<0\) for every \(\alpha>0\).
* If \(m\ge5\), there is precisely one \(\alpha_m>0\) such that \(\operatorname{Cov}(I_i,I_j)<0\) for \(0<\alpha<\alpha_m\), equals zero at \(\alpha_m\), and is positive for \(\alpha>\alpha_m\).

The ratio of their joint singleton probability to the product of singleton probabilities is **strictly increasing in reinforcement starting mass** \(\alpha\) for all \(m\ge3\). Its exact endpoints are
\[
R_m(0+)=\frac{m^3(m-2)}{(m+1)(m-1)^3}<1,
\qquad
R_m(\infty)=\frac{m^3}{(m+1)(m-1)^2}
\left(1-\frac1{(m-1)^2}\right)^{m-1}.
\]
The last endpoint is below one for \(m=3,4\) and above one for every \(m\ge5\).

For example, with five colours and six draws the covariance at \(\alpha=1/4\) is \(-417706/13461800625\), while at \(\alpha=1\) it is \(1/3150\). The unique threshold for five colours is approximately \(0.316881273819332\).

## Assumptions and scope

The urn has \(m\) named colours, all with equal strictly positive initial mass \(\alpha\), and unit linear reinforcement; its successive colours have the exchangeable Dirichlet-mixture representation. The sample length is **exactly** \(N=m+1\), the first sample length exceeding the number of available categories, where singleton co-occurrence and repeated categories necessarily compete. The indicators refer to two distinct *named* colours, rather than to the total number of singleton colours. No asymptotic in sample size, asymmetry in starting masses or non-unit reinforcement is asserted. Write \((x)_{\overline r}=\prod_{k=0}^{r-1}(x+k)\) with \((x)_{\overline0}=1\).

## Proof

**1. Exact pair probabilities.** The Dirichlet–multinomial count law (equivalently the classical Pólya-urn formula) gives, with \(N=m+1\),
\[
p_m:=\Pr(C_i=1)=\frac{N\alpha\,((m-1)\alpha)_{\overline{N-1}}}{(m\alpha)_{\overline N}},
\]
\[
q_m:=\Pr(C_i=C_j=1)=\frac{N(N-1)\alpha^2\,((m-2)\alpha)_{\overline{N-2}}}{(m\alpha)_{\overline N}}
\quad (m\ge3).
\]
For \(m=2\), \(N=3\) forces \(q_2=0\) and \(p_2>0\), so the covariance is negative. For \(m\ge3\), \(p_m>0\) and
\[
\operatorname{Cov}(I_i,I_j)=q_m-p_m^2
=p_m^2(R_m(\alpha)-1),
\]
where
\[
R_m(\alpha)=\frac{m}{m+1}
\frac{(m\alpha)_{\overline{m+1}}\,((m-2)\alpha)_{\overline{m-1}}}
{\big(((m-1)\alpha)_{\overline m}\big)^2}.
\]

**2. Strict monotonicity.** Differentiate the logarithm of the above positive product. The \(k=0\) summands cancel exactly, leaving
\[
\frac{d}{d\alpha}\log R_m(\alpha)
=F_m(\alpha)+F_{m-2}(\alpha)-2F_{m-1}(\alpha),
\quad F_s(\alpha):=\sum_{k=1}^{s}\frac1{\alpha+k/s}.
\]
For integer \(s\ge1\), Laplace integration gives
\[
F_s(\alpha)=\int_0^\infty e^{-\alpha u}
\frac{1-e^{-u}}{e^{u/s}-1}\,du.
\]
For fixed \(u>0\), define \(g_u(s)=(e^{u/s}-1)^{-1}\) for real \(s>0\). With \(x=u/s\), direct differentiation yields
\[
g_u''(s)=\frac{x e^x}{s^2(e^x-1)^3}
\left[x(e^x+1)-2(e^x-1)\right]>0.
\]
Indeed \(B(x):=x(e^x+1)-2(e^x-1)\) has \(B(0)=B'(0)=0\) and \(B''(x)=xe^x>0\) for \(x>0\). Hence strict convexity of \(s\mapsto g_u(s)\) makes its discrete second difference at \(m-1\) positive, and the positive Laplace integral proves \(R_m'(\alpha)>0\) for every \(m\ge3\) and \(\alpha>0\).

**3. Endpoint signs and unique crossing.** Isolating the zero-index factors from the rising factorials gives
\[
\lim_{\alpha\downarrow0}R_m(\alpha)
=\frac{m^3(m-2)}{(m+1)(m-1)^3}=1-\frac{2m-1}{(m+1)(m-1)^3}<1.
\]
Taking leading powers in \(\alpha\) yields the stated \(R_m(\infty)\). At \(m=3\) it equals \(243/256\); at \(m=4\), \(32768/32805\); both are below one.

For every \(m\ge5\), set \(t=m-1\ge4\). The assertion \(R_m(\infty)>1\) is equivalent to
\[
(t+1)^3(1-t^{-2})^{t}>(t+2)t^2.
\]
By the first four terms of the alternating binomial expansion (a lower Bonferroni bound for \(t\ge4\)),
\[
(1-t^{-2})^t\ge1-\frac1t+\frac{t-1}{2t^3}-\frac{(t-1)(t-2)}{6t^5}.
\]
Multiplying this lower bound by \((t+1)^3\) and subtracting \((t+2)t^2\) gives \(P(t)/(6t^5)\), where
\[
P(t)=3t^6-7t^5-6t^4-2t^3-t^2-3t-2.
\]
Its translation at \(t=u+4\) is
\[
P(u+4)=3u^6+65u^5+574u^4+2622u^3+6439u^2+7829u+3426>0
\quad (u\ge0).
\]
Thus the large-\(\alpha\) endpoint is strictly above one for every \(m\ge5\). Continuity and strict monotonicity establish exactly one crossing. The calculations at \(m=5\) are obtained by substituting \(\alpha=1/4,1\) into \(p_m,q_m\). This finishes the proof.

## Verification

Run `python3 check.py` with standard Python 3. The program independently enumerates all Dirichlet–multinomial count vectors for \(m=2,3,4,5,6\) at the rational starting masses \(\alpha\in\{1/4,1,2\}\); it verifies the probability normalization and closed \(p_m,q_m\) expressions, tests endpoint and rational-inequality identities at finite parameter values, and checks the two exact five-colour covariance examples. It performs 229 exact rational / identity / sign assertions. The infinite-parameter theorem is proved above by convexity and the polynomial positivity identity; finite checks are not substituted for that proof.

## Relationship to prior work

The Dirichlet–multinomial law, its Pólya-urn representation, and ordinary (negative) covariance of *count variables* are classical. Dello Schiavo and Quattrocchi's 2023 polychromatic-partition framework uses these laws; its later open-access revision explicitly records the Dirichlet–multinomial colour counts in Example 5.54 and their moment framework in Section 6. The result here concerns a different nonlinear functional: dependence of two events of *exactly one* occurrence at the first overfull sample size. An ordinary count-covariance formula does not imply its sign, much less the all-category unique phase boundary. Previously published work on independent occupancy indicators likewise concerns at-least-once occupancy under iid sampling, not the events and reinforced law studied here. The claim is restricted to the proved family and is not a claim of a universal dependence property for Pólya urns.

## Limitations

The threshold is specified uniquely but no closed formula in \(m\) or asymptotic expansion of \(\alpha_m\) as \(m\to\infty\) is claimed. Unequal initial masses, other sample sizes and the joint law of all singleton indicators lie outside the theorem. The literature comparison checks accessible mathematical texts and records but cannot establish definitive historical priority; independent mathematical audit is not yet performed.

## References

1. L. Dello Schiavo and F. Quattrocchi, *Polychromatic Partitions, Kingman Theory, and Ewens Sampling Formula*, arXiv:2309.11292, first publicly submitted 2023-09-20. https://arxiv.org/abs/2309.11292 . Relevant open-access revised text: https://arxiv.org/html/2309.11292v2 , Examples 5.53–5.54 and Section 6.
2. K. W. Ng, G.-L. Tian and M.-L. Tang, *Dirichlet–Multinomial Distribution*, in *Dirichlet and Related Distributions*, 2011. https://doi.org/10.1002/9781119995784.ch6 . General distributional reference (abstract accessible, full chapter not read).
3. *Overdispersion models for correlated multinomial data: applications to blinding assessment*, 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6800782/ . General Dirichlet–multinomial modelling and count-covariance background.
