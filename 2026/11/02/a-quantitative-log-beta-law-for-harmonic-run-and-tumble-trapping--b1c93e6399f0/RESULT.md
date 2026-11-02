# A quantitative log-Beta law for harmonic run-and-tumble trapping times

## Finding

The time required for a run-and-tumble particle launched far outside its harmonically confined stationary support has an explicit nondegenerate limiting **fluctuation law**, not just a logarithmically growing mean. The result also has a finite-launch-distance stochastic sandwich.

Let \(\mu,v,q>0\), let \(\sigma_t\in\{-1,+1\}\) switch sign at rate \(q\), and start the sign process in its fair stationary law. From a deterministic \(x_0>v/\mu\), evolve
\[
\dot X_t=-\mu X_t+v\sigma_t,\qquad X_0=x_0.
\]
Write \(b=v/\mu\) for the rightmost edge of the stationary positional support, and \(T=\inf\{t\geq0:X_t\leq b\}\) for the **first entry time** into that support. Set
\[
C=\frac{\mu(x_0-b)}{2v},\qquad \alpha=\frac q\mu,
\qquad R_C=T-\frac{\log C}{\mu}.
\]
For every \(C\geq1\), let \(B\sim\operatorname{Beta}(\alpha,\alpha)\), let \(Z=-\mu^{-1}\log B\), and set \(\delta_C=\mu^{-1}\log(1+C^{-1})\). Then, **for every real \(s\)**,
\[
\boxed{\Pr(Z>s)\leq\Pr(R_C>s)\leq\Pr(Z+\delta_C>s).}
\]
Equivalently, their quantile functions satisfy
\[
Q_Z(u)\leq Q_{R_C}(u)\leq Q_Z(u)+\delta_C,
\qquad 0<u<1.
\]
Thus the infinity-Wasserstein distance between the distributions of \(R_C\) and \(Z\) is at most \(\delta_C\), and \(R_C\Rightarrow Z\) as \(x_0\to\infty\) with the rates fixed.

The limiting density, Laplace transform and first two cumulants are
\[
\begin{aligned}
f_Z(s)&=\frac{\mu}{\mathrm B(\alpha,\alpha)}e^{-\mu\alpha s}(1-e^{-\mu s})^{\alpha-1},\qquad s>0,\\
\mathbb E[e^{-zZ}]&=\frac{\Gamma(2\alpha)\Gamma(\alpha+z/\mu)}{\Gamma(\alpha)\Gamma(2\alpha+z/\mu)},\quad z\geq0,\\
m_Z&=\frac{\psi(2\alpha)-\psi(\alpha)}{\mu},\\
v_Z&=\frac{\psi_1(\alpha)-\psi_1(2\alpha)}{\mu^2},
\end{aligned}
\]
where \(\psi\) and \(\psi_1\) are the di- and trigamma functions. In particular,
\[
0\leq\mathbb ET-\frac{\log C}{\mu}-m_Z\leq\delta_C,
\]
and
\[
|\operatorname{Var}(T)-v_Z|\leq2m_Z\delta_C+\delta_C^2.
\]
For the resonant switching rate \(q=\mu\), the limiting fluctuation is **exactly exponential** of rate \(\mu\). The fastest possible entry time \(\mu^{-1}\log(1+C)\) carries an exact atom of mass \(\tfrac12(1+C)^{-q/\mu}\); this atom vanishes in the far-launch limit.

## Assumptions and scope

All parameters \(\mu,v,q\) are strictly positive. Switching is symmetric, memoryless and independent of the initial position; the initial sign is fair, which is essential to the stated finite-distance comparison. There is no translational thermal noise. The launch condition \(C\geq1\) is equivalent to \(x_0\geq3v/\mu\). The process is observed until its **first** entry into \([-b,b]\) through the right edge; this is not a first passage to the origin.

The limit fixes \(\mu,v,q\) and sends \(x_0\) to infinity; it is not a fast-tumbling or weak-trap double limit. The notation \(\mathrm B\) is Euler's beta function, distinct from the beta random variable \(B\). All the displayed distributional and moment bounds are uniform for every \(C\geq1\), at fixed positive parameters.

## Proof

**1. An exact monotone passage functional.** Put \(I_t=\mathbf1_{\{\sigma_t=-1\}}\). The deterministic variation-of-constants formula gives
\[
X_t-b=e^{-\mu t}(x_0-b)-2v\int_0^t e^{-\mu(t-s)}I_s\,ds.
\]
Multiplying by \(e^{\mu t}\), define the nondecreasing continuous functional \(A_t=\mu\int_0^t e^{\mu s}I_s\,ds\). Then
\[
e^{\mu t}(X_t-b)=\frac{2v}{\mu}(C-A_t).
\]
Consequently the first entry time is the first time \(A_t\) reaches \(C\), and
\[
\Pr(T>t)=\Pr(U_t<Ce^{-\mu t}),\qquad
U_t=\mu\int_0^t e^{-\mu(t-s)}I_s\,ds.
\]
The nondecreasing representation proves that being outside at time \(t\) is exactly equivalent to never having entered by that time. It also shows that the particle cannot leave \([-b,b]\) once entered: at the right boundary the largest possible drift is zero, and at the left boundary the smallest possible drift is zero.

**2. Stationary exponentially weighted occupation and its law.** Extend the stationary two-state sign chain to all real times, and set
\[
B_t=\mu\int_{-\infty}^t e^{-\mu(t-s)}I_s\,ds.
\]
Almost surely \(0<B_t<1\), and \((B_t,\sigma_t)\) is stationary. With \(\sigma=+1\) the occupation coordinate drifts as \(\dot B=-\mu B\), while with \(\sigma=-1\) it drifts as \(\dot B=\mu(1-B)\). If \(f\) is its marginal stationary density, zero total spatial flux forces state-resolved densities \(f_+(u)=(1-u)f(u)\) and \(f_-(u)=uf(u)\). The stationary switching equation reduces to
\[
u(1-u)f'(u)=(\alpha-1)(1-2u)f(u).
\]
The normalizable solution on \((0,1)\) is \(f(u)=u^{\alpha-1}(1-u)^{\alpha-1}/\mathrm B(\alpha,\alpha)\). This invariant law is also unique because the integral from the infinite past is the pullback limit of every solution with the same sign path. Thus \(B_t\sim\operatorname{Beta}(\alpha,\alpha)\) for every real \(t\).

**3. A deterministic past-memory bound.** The same two-sided realization supplies the exact identity
\[
B_t=U_t+e^{-\mu t}B_0,
\qquad0\leq B_t-U_t\leq e^{-\mu t},\quad t\geq0.
\]
In particular, for every \(u>0\),
\[
\Pr(B_t<u)\leq\Pr(U_t<u)\leq\Pr(B_t<u+e^{-\mu t}).
\]
This uses no independence between \(B_0\) and \(B_t\), and hence has no hidden renewal or decorrelation assumption.

**4. Sharp-scale stochastic comparison.** For \(C\geq1\), put \(t=(\log C)/\mu+s\) and \(s\geq0\), so that \(t\geq0\). With \(u=e^{-\mu s}\), the threshold in Step 1 is exactly \(u\), whereas the correction in Step 3 is \(u/C\). Therefore
\[
\Pr(B<u)\leq\Pr(R_C>s)\leq\Pr(B<u(1+C^{-1})),
\]
with a beta CDF above its support interpreted as one. Since \(Z=-\mu^{-1}\log B\), these two probabilities are \(\Pr(Z>s)\) and \(\Pr(Z>s-\delta_C)\). For \(s<0\), the inequality is automatic from the deterministic bound \(T\geq\mu^{-1}\log(1+C)\), obtained by replacing \(I_s\) by its maximum one in \(A_t\). This proves the stated stochastic sandwich for all real \(s\). Standard inverse-CDF coupling provides the quantile and infinity-Wasserstein bound.

**5. Fluctuation distribution and moment estimates.** The transformation \(Z=-\mu^{-1}\log B\) produces the stated density and beta-function Laplace transform by an ordinary change of variables and the beta integral. Differentiating the logarithm of the Laplace transform at zero gives the digamma mean and trigamma variance. Stochastic ordering implies, for every positive integer \(n\),
\[
\mathbb E[Z^n]\leq\mathbb E[R_C^n]\leq\mathbb E[(Z+\delta_C)^n]<\infty.
\]
For \(n=1,2\) these inequalities yield the mean error. If \(\theta=\mathbb E R_C-m_Z\in[0,\delta_C]\) and \(\eta=\mathbb E R_C^2-\mathbb E Z^2\in[0,2m_Z\delta_C+\delta_C^2]\), then the variance error is \(\eta-2m_Z\theta-\theta^2\); its absolute value is at most \(2m_Z\delta_C+\delta_C^2\). Because \(\delta_C\to0\), the complete distribution and all fixed positive integer moments converge. The beta density at \(\alpha=1\) is uniform, so its negative logarithm is exponential.

**6. First-entry atom.** The inequality \(A_t\leq e^{\mu t}-1\) forces \(T\geq\mu^{-1}\log(1+C)\). Equality occurs precisely when the sign starts at \(-1\) and stays there until this time. The fair initial sign and exponential flip law give probability \(\tfrac12e^{-q\log(1+C)/\mu}=\tfrac12(1+C)^{-\alpha}\). This proves the exact front atom, including its decay.

## Verification

The standalone `verify.py` uses the exact integrated occupation over every simulated telegraph holding interval: no Euler approximation to the particle motion is used. It checks the stationary beta-density differential equation at multiple parameter values, its normalization, the stochastic mean bounds against the independently published hypergeometric mean formula, and Monte Carlo diagnostics of the limiting law at three rates and a large launch distance. Run in the directory containing the two standalone artifacts:

```bash
python -m pip install -r requirements.txt
python verify.py
```

In the recorded execution the script returned `PASS: 22808 analytic and exact-clock diagnostic assertions`. Exact-clock samples at \(\mu=1\), \(C=1000\), with 7,500 paths per tested switching rate, had means approximately \(1.37573\), \(1.00713\), and \(0.82939\) for \(\alpha=0.5,1,2\), against limits \(1.38629\), \(1\), and \(0.83333\). Their variances were approximately \(3.10433\), \(0.99080\), and \(0.36777\), against \(3.28987\), \(1\), and \(0.36111\). Simulations and finite algebraic evaluations are diagnostics only; the uniform-in-time probability bounds and asymptotic assertions are proved in the preceding steps.

## Relationship to prior work

Guéneau, Majumdar and Schehr (2024, arXiv:2409.16951v1) introduced the harmonic-trap **mean** entry-time calculation and derived an explicit generalized hypergeometric expression, including logarithmic growth at large launch distance (Section V.2, Eq. (63)). Its Appendix B presents a higher-moment recursion but does not solve the full harmonic trapping-time distribution. That exact mean was used here only as an independent finite-parameter consistency check, not as a newly discovered formula.

The stationary beta law of a symmetric, harmonically confined one-dimensional run-and-tumble particle is established prior mathematics and is explicitly recalled in Guéneau, Majumdar and Schehr (2026, arXiv:2602.08436v1, Section IV.1). Their velocity-redraw rate is twice the sign-flip rate used here. The new component is the exact **inverse weighted-occupation first-entry identity**, the finite-distance stochastic/quantile comparison, and the resulting limiting log-beta *hitting-time* law and moment-error estimates. A stationary position density alone does not state a first-entry fluctuation distribution or control its approach.

Bogachev and Ratanov (2010, arXiv:1007.3139) study occupation of the positive half-line by an integrated telegraph process. The functional here instead discounts the **negative sign state** exponentially and inverts its weighted occupation to obtain a first-entry time. Its abstract and introduction were compared as a plausible general occupation-time antecedent; the theorem sections and appendices were not materially inspected in this review.

## Limitations

This is a symmetric two-sign, athermal, harmonic-confinement theorem with a fair initial orientation. It does not address biased switching, nonlinear traps, thermal diffusion, random initial launches or fixed-orientation finite-distance stochastic bounds. The quantitative comparison is stated for \(C\geq1\); the far-launch limit is within that domain. The result determines distributional and moment asymptotics but does not assert a pointwise density approximation for finite \(C\), nor an exact finite-distance variance formula. Prior general exponential-functional theory could contain a broader implicit version, and independent publication-priority verification has not been performed.

## References

1. Mathis Guéneau, Satya N. Majumdar, Grégory Schehr, *Run-and-tumble particle in one-dimensional potentials: mean first-passage time and applications*, arXiv:2409.16951v1, first submitted 25 September 2024, https://arxiv.org/html/2409.16951v1 (especially Sections II.1, V.2 and Appendix B).
2. Mathis Guéneau, Satya N. Majumdar, Grégory Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1, 9 February 2026, https://arxiv.org/html/2602.08436v1 (Section IV.1 and the explicitly noted factor-two flip-rate conversion).
3. Leonid Bogachev, Nikita Ratanov, *Occupation time distributions for the telegraph process*, arXiv:1007.3139, 19 July 2010, https://arxiv.org/abs/1007.3139 (abstract-and-introduction comparison only).
