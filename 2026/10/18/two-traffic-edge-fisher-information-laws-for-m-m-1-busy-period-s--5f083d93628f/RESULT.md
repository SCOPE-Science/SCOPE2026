# Two traffic-edge Fisher-information laws for M/M/1 busy-period surveillance

## Finding

Fix a service rate \(\mu>0\), and consider the busy period \(Y\) of an \(M/M/1\) queue initiated by one arrival, with Poisson arrival rate \(0<\lambda<\mu\). The Fisher information \(\mathcal I_Y(\lambda,\mu)\) in one observed busy-period duration about the arrival-rate parameter, holding \(\mu\) fixed, obeys both endpoint laws

\[
\lim_{\lambda\downarrow0}\mathcal I_Y(\lambda,\mu)=\frac{2}{\mu^2},\qquad
\mathcal I_Y(\lambda,\mu)=\frac{1}{2\mu(\mu-\lambda)}+O_\mu(1)\quad(\lambda\uparrow\mu).
\]

Let \(K_X\) and \(K_Y\) denote the previously defined KL-covertness square-root constants for observing, respectively, the number of services and the duration in each busy period. For fixed \(\mu\), their complete leading endpoint behavior is

\[
\begin{array}{lll}
\lambda\downarrow0:&K_X\sim\sqrt{2\mu/\lambda},&K_Y\sim\mu/\lambda,\\
\lambda\uparrow\mu:&K_X\sim2\sqrt{\mu/(\mu-\lambda)},&K_Y\sim2\sqrt{\mu/(\mu-\lambda)}.
\end{array}
\]

In particular, writing \(\rho=\lambda/\mu\),
\[
\frac{K_Y}{K_X}\sim\frac1{\sqrt{2\rho}}\quad(\rho\downarrow0),\qquad
\frac{K_Y}{K_X}=1+O(1-\rho)\quad(\rho\uparrow1).
\]

Thus the statistical cost of revealing the service count rather than the busy-period duration diverges in light traffic, but the two covert constants become asymptotically equivalent in heavy traffic. The asymptotics are sequential limits: the square-root-law observation horizon is sent to infinity for each fixed \(0<\lambda<\mu\), then \(\lambda\) approaches the indicated endpoint. No uniform joint horizon/traffic-limit assertion is made.

## Assumptions and scope

The queue has one work-conserving exponential server of rate \(\mu\), independent Poisson inputs of rate \(\lambda\), and no service interruption. Busy periods start from one customer and end at the next empty state. The parameter \(\mu\) is known and fixed when differentiating likelihoods. The density of the busy-period duration, with \(I_\nu\) the modified Bessel function, is
\[
g_{\lambda,\mu}(y)=e^{-(\lambda+\mu)y}\sqrt{\frac\mu\lambda}\,\frac{I_1(2y\sqrt{\lambda\mu})}{y},\qquad y>0.
\]

We define \(\mathcal I_Y=\int_0^\infty g_{\lambda,\mu}(y)[\partial_\lambda\log g_{\lambda,\mu}(y)]^2dy\). The earlier square-root constants are normalized by expected inserted jobs divided by \(\sqrt{n\delta}\) under asymptotic total KL budget \(\delta\). Their established fixed-parameter representations are
\[
K_X=\sqrt{\frac{2\mu(\mu+\lambda)}{\lambda(\mu-\lambda)}},\qquad
K_Y=\frac{\mu}{\lambda(\mu-\lambda)}\sqrt{\frac2{\mathcal I_Y}}.
\]

Only the endpoint evaluations of these previously given formulas, and the supporting Fisher-information estimates, are asserted as new.

## Proof

**1. An exact score free of a singular cancellation.** Set \(z=2y\sqrt{\lambda\mu}\) and \(R(z)=I_2(z)/I_1(z)\). The Bessel recurrence \(I_1'(z)=I_2(z)+I_1(z)/z\), together with \(\partial_\lambda z=y\sqrt{\mu/\lambda}\), gives the exact score
\[
S_{\lambda,\mu}(y):=\partial_\lambda\log g_{\lambda,\mu}(y)
=-y+y\sqrt{\frac\mu\lambda}\,R(2y\sqrt{\lambda\mu}).
\]

For all \(z>0\), the power series for \(I_1\) and \(I_2\) give
\[
0<R(z)\le z/4.
\]
Indeed, the term with index \(k\) in \(I_2\) divided by the corresponding positive term in \(I_1\) equals \(z/[2(k+2)]\le z/4\); summing preserves the inequality. Hence, uniformly for \(\lambda>0\),
\[
|S_{\lambda,\mu}(y)|\le y+\frac{\mu y^2}{2}.
\]

**2. The light-traffic boundary.** The series \(I_2(z)/I_1(z)=z/4+O(z^3)\) shows, for fixed \(y>0\),
\[
S_{\lambda,\mu}(y)\longrightarrow\frac{\mu y^2}{2}-y
\quad\text{as }\lambda\downarrow0.
\]
The other Bessel series identity yields
\[
g_{\lambda,\mu}(y)
=\mu e^{-(\lambda+\mu)y}\sum_{k\ge0}\frac{(\lambda\mu y^2)^k}{k!(k+1)!}
\le\mu e^{-(\sqrt\mu-\sqrt\lambda)^2y}.
\]
For example, the last bound follows from the coefficient comparison with \(I_0(z)\le e^z\). Whenever \(0<\lambda\le\mu/4\), the density is thus bounded by \(\mu e^{-\mu y/4}\), uniformly in \(\lambda\). Consequently, the nonnegative integrand \(gS^2\) is dominated by an integrable fixed polynomial times that exponential. The density converges pointwise to \(\mu e^{-\mu y}\). Dominated convergence and the elementary moments of \(\operatorname{Exp}(\mu)\) now give
\[
\begin{aligned}
\lim_{\lambda\downarrow0}\mathcal I_Y
&=\int_0^\infty\mu e^{-\mu y}\left(\frac{\mu y^2}{2}-y\right)^2dy\\
&=\frac{\mu^2}{4}\frac{24}{\mu^4}-\mu\frac6{\mu^3}+\frac2{\mu^2}
=\frac2{\mu^2}.
\end{aligned}
\]

**3. The heavy-traffic boundary.** Standard two-term large-argument Bessel asymptotics give
\[
R(z)=1-\frac3{2z}+O(z^{-2})\qquad(z\to\infty).
\]
Since \(R(z)=z/4+O(z^3)\) at zero and is continuous on \((0,\infty)\), the absolute constant
\[
H=\sup_{z>0}z|R(z)-1|
\]
is finite. Write \(d=\mu-\lambda\) and
\[
a_\lambda=\sqrt{\mu/\lambda}-1=\frac d{\sqrt\lambda(\sqrt\mu+\sqrt\lambda)}.
\]
The exact score decomposes as \(S_{\lambda,\mu}(y)=a_\lambda y+r_\lambda(y)\), where
\[
r_\lambda(y)=y\sqrt{\mu/\lambda}[R(2y\sqrt{\lambda\mu})-1],\qquad
|r_\lambda(y)|\le\frac H{2\lambda}.
\]
For \(\lambda\ge\mu/2\), this remainder is bounded uniformly in both \(y\) and \(\lambda\).

The busy-period Laplace transform is the smaller root of its branching equation:
\[
F(s)=\mathbb E e^{-sY}
=\frac{\lambda+\mu+s-\sqrt{(\lambda+\mu+s)^2-4\lambda\mu}}{2\lambda}.
\]
Differentiating at \(s=0\) gives the exact moment identities
\[
\mathbb E Y=\frac1d,\qquad \mathbb E Y^2=\frac{2\mu}{d^3}.
\]
The cross term in \(\mathbb E(a_\lambda Y+r_\lambda(Y))^2\) has absolute value at most \(a_\lambda H\mathbb E Y/\lambda=O_\mu(1)\), and the remainder square has expectation \(O_\mu(1)\). Therefore
\[
\begin{aligned}
\mathcal I_Y(\lambda,\mu)
&=a_\lambda^2\mathbb EY^2+O_\mu(1)\\
&=\frac{2\mu}{\lambda(\sqrt\mu+\sqrt\lambda)^2}\frac1{\mu-\lambda}+O_\mu(1)\\
&=\frac1{2\mu(\mu-\lambda)}+O_\mu(1).
\end{aligned}
\]
Both appearances of \(O_\mu(1)\) are bounded as \(\lambda\uparrow\mu\); they do not assert an error bound uniform in \(\mu\).

**4. Convert information into covert constants.** The fixed-parameter formulas in the scope section and the light limit give
\[
K_X=\sqrt{\frac{2\mu}{\lambda}}(1+o(1)),\quad
K_Y=\frac\mu\lambda(1+o(1))\qquad(\lambda\downarrow0).
\]
At the heavy endpoint \(d\downarrow0\), the previous step yields
\[
\mathcal I_Y=\frac1{2\mu d}(1+O(d/\mu)),\quad
K_X=2\sqrt{\frac\mu d}(1+O(d/\mu)),\quad
K_Y=2\sqrt{\frac\mu d}(1+O(d/\mu)).
\]
The ratio statements follow. This proves each assertion.

## Verification

The accompanying standalone script `verify.py` uses exponentially scaled modified Bessel functions, independent numerical quadrature, likelihood finite differences, exact busy-period first and second moments, and checks at several traffic ratios and service rates. It passed 275 deterministic assertions in the recorded run. Its tests are finite consistency checks and not proofs of endpoint asymptotics; the proof above supplies the infinite statements. Run with Python 3.10 or newer after installing packages from `requirements.txt`, then execute `python verify.py`.

## Relationship to prior work

Sahithi, Yardi and Ravi (2026, arXiv:2610.13911v1) establish the two KL-covertness square-root constants and provide a numerical comparison for fixed stable parameters. Their discussion and conclusion explicitly leave an analytical characterization of both traffic-endpoint asymptotics as future work. The present contribution evaluates the duration Fisher information at both ends and translates those evaluations into the previously defined constants, including their sharply different ratio behavior. The known busy-period density, Catalan service-count formula, square-root law and fixed-parameter capacity representations are not new claims.

Nazarathy and Palmowski (2022) study critical queue busy-period tails and renewal/BRAVO effects, rather than Fisher information in an observed duration. Denisov and Shneer (2010) study tails of M/G/1 busy periods with subexponential services, and Parker et al. (2015) study Fisher information from sampled queue-state measurements; neither available description covers the particular observation experiment and two-sided constants here. A covering inference from unidentified queueing-information literature cannot be ruled out without independent priority review.

## Limitations

The conclusion is for \(M/M/1\) busy periods, known fixed service rate, and the specified KL covertness normalization. It does not prove the number of covert jobs attainable in a simultaneous limit with traffic intensity varying with observation horizon; order of limits matters. The result does not determine higher-order coefficients or the information relation between complete departure counts and durations for finite interior traffic ratios. No independent mathematical audit or global priority certification has been performed.

## References

1. A. V. S. S. Sahithi, A. Yardi and J. Ravi, *Fundamental Limits of Covert queueing under Busy-Period Observations*, arXiv:2610.13911v1 (first public 2026-10-09), https://arxiv.org/html/2610.13911v1. Relevant: equations (3), (22), (34)-(40), Section IV and Section V.
2. Y. Nazarathy and Z. Palmowski, *On busy periods of the critical GI/G/1 queue and BRAVO*, Queueing Systems 102 (2022), 219-225, https://doi.org/10.1007/s11134-022-09858-4.
3. D. Denisov and S. Shneer, *Global and local asymptotics for the busy period of an M/G/1 queue*, Queueing Systems 64 (2010), 383-393, https://doi.org/10.1007/s11134-010-9167-0.
4. B. M. Parker, S. G. Gilmour, J. A. Schormans and H. Maruri, *Optimal design of measurements on queueing systems*, Queueing Systems 79 (2015), DOI:10.1007/s11134-014-9421-y.
