# A nonfactorizing four-time aging law for fractional run-and-tumble motion

## Finding

Let \(0<\nu<1\), \(\alpha>0\) and \(0<a<b<c<d\). Consider the one-dimensional fractional run-and-tumble process of Angelani, De Gregorio, Garra and Iafrate [1]. The normalized heading is
\[
\Sigma(t)=\sigma(E_\nu(t))\in\{-1,+1\},
\]
where \(\sigma\) is a symmetric stationary telegraph chain flipping at rate \(\alpha/2\) and the clock is independent. For \(0<x<y\), write
\[
p_\nu(x,y)=I_{x/y}(\nu,1-\nu)=\frac{\sin(\pi\nu)}{\pi}\int_{(y-x)/x}^{\infty}\frac{u^{-\nu}}{1+u}\,du.
\]
The four-time aging correlation has the exact, \(\alpha\)-independent limit
\[
\begin{aligned}
Q_\nu(a,b,c,d)&:=\lim_{T\to\infty}\mathbb E[\Sigma(aT)\Sigma(bT)\Sigma(cT)\Sigma(dT)]\\
&=p_\nu(a,d)+\frac{\sin(\pi\nu)}{\pi}\int_{b-a}^{c-a}\frac{a^\nu}{z^\nu(a+z)}p_\nu(c-a-z,d-a-z)\,dz.
\end{aligned}
\]
The two-time aging moment is \(\lim_{T\to\infty}\mathbb E[\Sigma(aT)\Sigma(bT)]=p_\nu(a,b)\). Consequently the two disjoint signed-persistence measurements do not generally become independent. In particular, for \(\nu=1/2\) and \((a,b,c,d)=(1,2,3,4)\),
\[
\begin{aligned}
\lim_{T\to\infty}\operatorname{Cov}(\Sigma(T)\Sigma(2T),\Sigma(3T)\Sigma(4T))
&=Q_{1/2}(1,2,3,4)-\frac13\\
&=\frac1\pi\int_1^2\frac{p_{1/2}(2-z,3-z)}{\sqrt z(1+z)}\,dz>0.
\end{aligned}
\]
This positive residual arises from configurations where the first observation pair occupies one long trapping plateau and the second pair occupies another. It is a joint four-time effect, not a claim about ordinary equilibrium correlations or the displacement process.

## Assumptions and scope

The forward stable subordinator \(D_\nu(u)\) is characterized by \(\mathbb E[e^{-sD_\nu(u)}]=e^{-us^\nu}\) for \(s,u>0\), and \(E_\nu(t)=\inf\{u>0:D_\nu(u)>t\}\). Its paths are nondecreasing and its inverse is continuous. The chain starts at a fair independent sign; at each event of a Poisson process of rate \(\alpha/2\) its sign reverses. All four observation times are strictly positive and strictly increasing. Every expectation integrates both random drivers. Only the normalized sign, not the particle position or a physical-time derivative, is studied.

## Proof

**1. Conditional four-time reduction.** For four ordered operational times \(u_1\le u_2\le u_3\le u_4\), Poisson parity and independent disjoint increments give
\[
\mathbb E[\sigma(u_1)\sigma(u_2)\sigma(u_3)\sigma(u_4)]
=e^{-\alpha[(u_2-u_1)+(u_4-u_3)]}.
\]
Indeed the two odd-parity contributions in the product are precisely the flips in the disjoint intervals \((u_1,u_2]\) and \((u_3,u_4]\). Conditioning on the independent inverse clock therefore yields
\[
\mathbb E[\Sigma(aT)\Sigma(bT)\Sigma(cT)\Sigma(dT)]
=\mathbb E[e^{-\alpha(\Delta_{ab}(T)+\Delta_{cd}(T))}],
\]
where \(\Delta_{ab}(T)=E_\nu(bT)-E_\nu(aT)\) and similarly for \(\Delta_{cd}(T)\).

**2. Clock scaling and the zero-increment limit.** Stability implies joint self-similarity \((E_\nu(Tt))_{t\ge0}\overset{d}=(T^\nu E_\nu(t))_{t\ge0}\). Since both increments are nonnegative, dominated convergence gives
\[
Q_\nu(a,b,c,d)=\Pr(E_\nu(b)=E_\nu(a),\ E_\nu(d)=E_\nu(c)).
\]
For a single pair the same argument gives \(p_\nu(a,b)=\Pr(E_\nu(b)=E_\nu(a))\), once the overshoot law below is applied.

**3. Overshoot density, with normalization.** Define \(O_a=D_\nu(E_\nu(a))-a\). The potential density of the stable subordinator is \(y^{\nu-1}/\Gamma(\nu)\), and its jump measure has density \(\nu x^{-1-\nu}/\Gamma(1-\nu)\). Summing the unique crossing jump over all possible pre-crossing positions yields, for \(z>0\),
\[
\begin{aligned}
f_a(z)&=\frac{\nu}{\Gamma(\nu)\Gamma(1-\nu)}
\int_0^a\frac{y^{\nu-1}}{(a-y+z)^{1+\nu}}\,dy\\
&=\frac{\sin(\pi\nu)}{\pi}\frac{a^\nu}{z^\nu(a+z)}.
\end{aligned}
\]
The equality uses the explicit antiderivative of the integrand and Euler's reflection formula. The density integrates to one; changing variables \(x=a/(a+z)\) identifies the beta distribution and gives
\[
\Pr(O_a>y-a)=\int_{y-a}^\infty f_a(z)\,dz=p_\nu(a,y),\qquad y>a.
\]
For deterministic positive \(a\), stable subordinators cross \(a\) by a jump almost surely, so endpoint equalities carry zero probability.

**4. Two-gap classification.** The first equality \(E_\nu(b)=E_\nu(a)\) holds precisely when \(O_a\ge b-a\). If \(O_a\ge d-a\), the same jump covers both observation intervals; its probability is \(p_\nu(a,d)\). If \(b-a\le O_a<c-a\), the first interval is entirely covered but the plateau ends before the third observation. By the strong Markov property of \(D_\nu\) at its first crossing of \(a\), the residual process is an independent stable subordinator. Given \(O_a=z\), the probability that the second interval is entirely contained in a subsequent plateau is \(p_\nu(c-a-z,d-a-z)\). Finally, if \(c-a\le O_a<d-a\), the clock remains frozen at time \(c\) but advances before \(d\); this contributes zero. If \(O_a<b-a\), the first equality fails. Integrating these mutually exclusive cases against \(f_a\) gives the stated \(Q_\nu\) formula for all strictly ordered positive observation times.

**5. A provably positive connected four-time limit.** For \(\nu=1/2\), the beta distribution is the classical arcsine law, so \(p_{1/2}(1,2)=1/2\), \(p_{1/2}(3,4)=2/3\), and \(p_{1/2}(1,4)=1/3\). Therefore the covariance limit is exactly the strictly positive integral printed in the Finding. Its integrand is positive for \(1<z<2\) and integrable at both endpoints, which proves strict positivity without appealing to a numerical approximation.

## Verification

The accompanying `verify.py` independently recomputes incomplete-beta values and the quadrature, checks the exact three pair probabilities, and compares the predicted simultaneous-gap probability against inverse-\(1/2\)-stable path simulations based on the exact stable-increment identity \(D_{1/2}(\delta)\overset{d}=\delta^2/(2G^2)\) for a standard normal \(G\). Simulations are diagnostics only, while the preceding probabilistic argument proves the infinite-time statements. Execute `python verify.py` after installing the packages in `requirements.txt`.

## Relationship to prior work

Angelani et al. [1] establish the time-fractional random-flight model, its inverse-stable-clock construction, and one-time telegraph probabilities; those are not claimed new. Classical high-order telegraph moments [2] use the untime-changed clock. Leonenko and Papić [3], and the fractional-Pearson literature, derive two-time correlations of other processes with the same clock and hence imply the two-time expression here; we credit that as prior and do not claim that two-time formula new. The aging arcsine law of Akimoto et al. [4] treats a single observation window. Stable-regenerative partition theory [5] supplies the clock's foundational gap laws. The contribution isolated here is the four-time velocity correlation, its explicit two-gap formula, and a strict disjoint-window connected-memory example for the specified fractional run-and-tumble model. Broader regenerative-partition formulae could potentially subsume this particular two-gap integral and remain a publication-priority qualification.

## Limitations

The result is asymptotic in a *common* large physical-time scale, with four distinct positive time ratios held fixed. It assumes an independent inverse strictly stable clock and symmetric one-dimensional velocity reversals; it does not apply unchanged to integrated-orientation walks, more general renewal distributions, correlated clock/velocity forcing, or finite sampling accuracy. No claim of a positive four-time connected covariance for every exponent and every timing configuration is made. The named beta and stable-overshoot laws have long-standing prior provenance.

## References

[1] L. Angelani, A. De Gregorio, R. Garra and F. Iafrate, *Anomalous Random Flights and Time-Fractional Run-and-Tumble Equations*, arXiv:2404.15941v1 (first public 2024-04-24), https://arxiv.org/abs/2404.15941; *Journal of Statistical Physics* 191, 129 (2024), https://doi.org/10.1007/s10955-024-03344-2.

[2] E. Renshaw, *The high-order autocovariance structure of the telegraph wave*, *Journal of Applied Probability* 25 (1988), 744–751, https://doi.org/10.2307/3214295.

[3] N. N. Leonenko and I. Papić, *Correlation properties of continuous-time autoregressive processes delayed by the inverse of the stable subordinator*, *Communications in Statistics — Theory and Methods* 49 (2020), 5091–5113, https://doi.org/10.1080/03610926.2019.1612918; lawful repository text https://orca.cardiff.ac.uk/id/eprint/121914/1/dCAR_19_03_20.pdf.

[4] T. Akimoto, T. Sera, K. Yamato and K. Yano, *Aging arcsine law in Brownian motion and its generalization*, arXiv:2004.00808, https://arxiv.org/abs/2004.00808.

[5] J. Pitman and M. Yor, *Arcsine Laws and Interval Partitions Derived from a Stable Subordinator*, *Proceedings of the London Mathematical Society* s3-65 (1992), 326–356, https://doi.org/10.1112/plms/s3-65.2.326.

[6] M. M. Meerschaert, E. Nane and P. Vellaisamy, *The fractional Poisson process and the inverse stable subordinator*, arXiv:1007.5051, https://arxiv.org/abs/1007.5051.
