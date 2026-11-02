# Sharp one-crossing law for the fourth cumulant of stationary asymmetric telegraph transport

## Finding

Let a particle alternate between constant velocities \(v_0<v_1\) as a continuous-time, two-state Markov chain, with switching rates \(a>0\) from state \(0\) to state \(1\) and \(b>0\) in the reverse direction. Start the internal chain in its stationary distribution. Define \(r=a+b\), \(\Delta=v_1-v_0>0\), \(P=ab/r^2\), \(\eta=(b-a)/r\), and \(u=rt\). The fourth displacement cumulant \(\kappa_4(t)\), for every \(t>0\), obeys the complete and strict classification:

- If \(0\le\eta^2\le1/5\), then \(\kappa_4(t)<0\) at every finite positive time.
- If \(1/5<\eta^2<1/3\), there is exactly one simple positive zero \(t_*\), with \(\kappa_4(t)<0\) before it and \(\kappa_4(t)>0\) afterward.
- If \(1/3\le\eta^2<1\), then \(\kappa_4(t)>0\) at every finite positive time.

Here \(\kappa_4(t)=\mathbb E[(X_t-\mathbb EX_t)^4]-3\operatorname{Var}(X_t)^2\), for \(X_t=\int_0^t v_{S_s}\,ds\). All assertions continue to hold for \(X_t+\sqrt{2D}B_t\) with any independent standard Brownian motion and \(D\ge0\). The zero in the middle regime is the unique positive solution of
\[
\frac{B((a+b)t_*)}{A((a+b)t_*)}=\frac{4\eta^2}{1-\eta^2},
\]
where
\[
A(u)=u-3+\tfrac12(u^2+4u+6)e^{-u},\qquad
B(u)=u-\tfrac52+2(u+1)e^{-u}+\tfrac12e^{-2u}.
\]

This is a classification of a time-dependent, directly measurable transport statistic, not merely a moment evaluation at selected parameters.

## Assumptions and scope

Take the row generator and invariant probabilities
\[
Q=\begin{pmatrix}-a&a\\ b&-b\end{pmatrix},\qquad
\pi=\left(\frac b{a+b},\frac a{a+b}\right).
\]
The chain is initialized with law \(\pi\), the velocities are real and constant, and \(a,b>0\), \(v_0<v_1\). Observation time \(t\) ranges over all positive real numbers. A translation of both velocities affects only the first cumulant, not the fourth. An independent Gaussian displacement affects only the first two cumulants. The sign of excess kurtosis equals the sign of \(\kappa_4\), because the displacement variance is positive for \(t>0\).

## Proof

**1. Exact resolvent.** Let \(\bar v=(bv_0+av_1)/r\) and \(Y_t=X_t-\bar vt\). The centered velocities are \(-a\Delta/r\) and \(b\Delta/r\). By the finite-state Feynman–Kac formula, the time-Laplace transform of the moment-generating function \(M(z,t)=\mathbb E[e^{zY_t}]\), initially for sufficiently large positive Laplace variable \(s\), is
\[
\widetilde M(z,s)
=\pi\big(sI-Q-z\operatorname{diag}(-a\Delta/r,b\Delta/r)\big)^{-1}\mathbf1
=\frac{s+r-\eta\Delta z}{s(s+r-\eta\Delta z)-P\Delta^2z^2}.
\]
Equivalently, with \(w=\Delta z\), expansion through order four gives
\[
\widetilde M(z,s)=\frac1s+
\frac{Pw^2}{s^2(s+r)}+
\frac{P\eta w^3}{s^2(s+r)^2}+
 w^4\left(\frac{P\eta^2}{s^2(s+r)^3}+\frac{P^2}{s^3(s+r)^2}\right)+O(w^5).
\]
These rational coefficients uniquely determine all moments up to order four. Inverting their Laplace transforms and using the zero mean of \(Y_t\) yields
\[
\mathbb E[Y_t^2]=\frac{2P\Delta^2}{r^2}(u-1+e^{-u}),\quad
\mathbb E[Y_t^4]=\frac{24\Delta^4}{r^4}\big(P\eta^2 A(u)+P^2C(u)\big),
\]
where \(C(u)=\tfrac12(u^2-4u+6)-(u+3)e^{-u}\). Subtracting three times the squared variance and simplifying gives the identity
\[
\boxed{\kappa_4(t)=\frac{24P\Delta^4}{r^4}\left(\eta^2A(u)-PB(u)\right)}.
\]

**2. Strict monotone-ratio lemma.** The functions \(A,B\), and their first derivatives, vanish at zero, while
\[
A''(u)=\tfrac12u^2e^{-u}>0,\qquad
B''(u)=2e^{-u}(u-1+e^{-u})>0\qquad(u>0).
\]
Consequently \(A(u),B(u)>0\) at every positive argument. Furthermore
\[
\frac{B''(u)}{A''(u)}=\frac{4(u-1+e^{-u})}{u^2}.
\]
The derivative of this ratio has the sign of \(2-u-(u+2)e^{-u}\), which is strictly negative for \(u>0\): its negative is \(u-2+(u+2)e^{-u}\), whose derivative is \(1-(u+1)e^{-u}>0\) and whose value at zero is zero. Thus \(B''/A''\) is strictly decreasing. Since \(A'(0)=B'(0)=0\) and \(A''>0\), the quotient \(B'/A'\) is a strictly decreasing \(A''\)-weighted running average of \(B''/A''\). Since \(A(0)=B(0)=0\), another weighted-average step makes \(R(u)=B(u)/A(u)\) strictly decreasing on \((0,\infty)\). Direct Taylor and large-argument expansions give
\[
\lim_{u\downarrow0}R(u)=2,\qquad
\lim_{u\to\infty}R(u)=1.
\]
In particular \(1<R(u)<2\) and \(R'(u)<0\) for all \(u>0\).

**3. All rates, times, and endpoint cases.** Because \(P=(1-\eta^2)/4\), the sign of the exact cumulant is the sign of
\[
\frac{4\eta^2}{1-\eta^2}-R(u).
\]
The strictly decreasing function \(R\) covers exactly \((1,2)\). Its horizontal level lies below or at \(1\) precisely when \(\eta^2\le1/5\), between \(1\) and \(2\) precisely when \(1/5<\eta^2<1/3\), and above or at \(2\) precisely when \(\eta^2\ge1/3\). Thus the claimed signs, uniqueness, simplicity, and strict endpoint cases all follow. The local and long-time coefficients independently corroborate the thresholds:
\[
\kappa_4(t)=\frac{P\Delta^4}{2}(3\eta^2-1)t^4+O(t^5),\qquad
\lim_{t\to\infty}\frac{\kappa_4(t)}t=\frac{6P\Delta^4}{r^3}(5\eta^2-1).
\]
Finally, the fourth cumulant of the sum of independent variables is the sum of their fourth cumulants, and a Gaussian variable has zero fourth cumulant. Therefore independent Brownian displacement cannot change the classification.

## Verification

The standalone `check.py` constructs a 10-dimensional block moment-generator from the original two-state Markov chain, computes its matrix exponential, reconstructs the fourth cumulant, and compares it with the exact closed form. It also checks the signs in the three regimes using 70-digit precision and locates the intermediate root. Running `python check.py` with NumPy, SciPy and mpmath produced 333 successful assertions; maximal absolute discrepancy for the matrix/closed-form comparisons was \(2.73\times10^{-12}\). For \(a=1\), \(b=3\) the unique root has \(rt_*=3.0464755666632222\ldots\), hence \(t_*=0.7616188916658056\ldots\). These numerical tests reproduce representative finite computations; the all-parameter classification is established by the exact resolvent and strict monotonicity argument above.

## Relationship to prior work

López and Ratanov (2014) analyze precisely the asymmetric two-velocity Markov telegraph model, including general moment-generating functions and formulae for moments of arbitrary order (Section 4, notably Theorem 4.1). Those general tools are established prior work and imply, in principle, that the fourth cumulant can be calculated. The specific result here is the all-time sign-and-zero classification with two sharp imbalance thresholds, a strict one-crossing theorem, and its stationary-transport interpretation; the inspected paper does not explicitly formulate these assertions. Classical symmetric telegraph analyses are recovered in the negative-sign region. Any undiscovered equivalent classification in earlier moment or telegraph literature would supersede the originality claim; priority is not independently established.

## Limitations

Stationary initialization is essential. The theorem is not asserted for deterministic initial velocity, time-varying rates, hidden additional velocity states, state-dependent diffusion, or correlated Brownian forcing. It classifies fourth-cumulant signs, not complete displacement distributions or the size of normalized excess kurtosis. Historical-priority checking is finite and cannot prove uniqueness in the literature. Independent scientific validation has not been performed.

## References

1. O. López and N. Ratanov, *On the Asymmetric Telegraph Processes*, Journal of Applied Probability 51 (2014), 569–589. https://doi.org/10.1239/jap/1402578644 ; accessible full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AF791584BC527BA17D7E23A7060053BC/S0021900200011438a.pdf/on-the-asymmetric-telegraph-processes.pdf
2. S. K. Foong and S. Kanno, *Properties of the telegrapher's random process with or without a trap*, Stochastic Processes and their Applications 53 (1994), 147–173 (referenced and compared in López and Ratanov).
3. A. D. Kolesnik, *Moment analysis of the telegraph random process*, Bulletin of the Academy of Sciences of Moldova, Mathematics 68 (2012), 90–107 (symmetric moments, cited in López and Ratanov).
4. American Mathematical Society, MSC2020 category `82C70`: transport processes in time-dependent statistical mechanics. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C05
