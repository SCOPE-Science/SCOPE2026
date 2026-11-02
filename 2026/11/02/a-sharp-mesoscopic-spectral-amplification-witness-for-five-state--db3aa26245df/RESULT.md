# A sharp mesoscopic spectral-amplification witness for five-state Markov oscillators

## Finding

**Theorem.** Fix any real triple \((x,y,z)\ne(0,0,0)\). For each \(0<\varepsilon<1\), let \(X_t\) be the irreducible continuous-time Markov chain on states \(0,1,2,3,4\), with **only** the directed transitions \(i\to i+1\pmod 5\), at successive rates
\[
(\varepsilon,1,\varepsilon,1,1).
\]
Observe \(g(X_t)\), where \(g=(0,x,0,y,z)\). With \(\pi_\varepsilon\) its stationary law, put \(f=g-\pi_\varepsilon(g)\) and define the two-sided stationary power spectrum
\[
G_\varepsilon(\omega)=\int_{-\infty}^{\infty}
\operatorname{Cov}(g(X_0),g(X_t))e^{-i\omega t}\,dt,
\qquad \omega\ge0.
\]
For **every** positive frequency scale satisfying \(\varepsilon/\omega_\varepsilon\to0\) and \(\omega_\varepsilon\to0\),
\[
\lim_{\varepsilon\downarrow0}\frac{G_\varepsilon(\omega_\varepsilon)}{\varepsilon}
=A(x,y,z):=x^2+y^2+z^2+yz,
\]
and
\[
\lim_{\varepsilon\downarrow0}\frac{G_\varepsilon(0)}{\varepsilon}
=B(x,y,z):=\frac{x^2+y^2+z^2}{2}+\frac{(x+y+z)^2}{4}.
\]
These limits yield the **sharp restricted-class enhancement law**
\[
\frac{A(x,y,z)}{B(x,y,z)}\le\frac{12}{5},
\]
with equality if and only if \((x,y,z)\) is a nonzero real multiple of \((-3,2,2)\). Thus, for the global oscillation efficiency of five-state irreducible continuous-time Markov networks in the sense of Jia (2026),
\[
\boxed{\eta_5^*\ge\frac7{12}>\frac12.}
\]
The bound \(7/12\) is a *rigorously attained supremum witness in the singular limit*, **not** a claim that the unknown global optimum \(\eta_5^*\) equals \(7/12\).

## Assumptions and scope

Time is continuous. The generator acts on column observables by
\[
Q_\varepsilon=\begin{pmatrix}
-\varepsilon&\varepsilon&0&0&0\\
0&-1&1&0&0\\
0&0&-\varepsilon&\varepsilon&0\\
0&0&0&-1&1\\
1&0&0&0&-1
\end{pmatrix}.
\]
Every \(\varepsilon>0\) gives a finite irreducible stationary chain, even though backward transition rates vanish. This is a *dynamical* spectral problem; the one-way model has formally infinite stochastic-thermodynamic entropy production, so finite-entropy-production inequalities are **not** asserted. The experimental observable is supported on the three short-residence intermediate states, which measures the relative signatures of a one-step excursion and a two-step excursion between two long-lived states. This is a motivated restriction, not the collection of all five-state observables or all rate assignments.

For any nonconstant centered real observable, write \(G_{\max}=\max_{\omega\ge0}G_\varepsilon(\omega)\), and
\[
\eta_f=1-\frac{G_\varepsilon(0)}{G_{\max}}.
\]
The maximum exists because the spectrum is continuous, nonnegative, and tends to zero as \(\omega\to\infty\). The global \(\eta_5^*\) is the supremum over irreducible five-state generators and nonconstant real state observables.

## Proof

**1. Stationary law.** The constant stationary flux through the directed cycle gives
\[
\pi_\varepsilon=\frac{(1,\varepsilon,1,\varepsilon,\varepsilon)}{2+3\varepsilon},
\qquad m_\varepsilon:=\pi_\varepsilon(g)
=\frac{\varepsilon M}{2+3\varepsilon},\quad M:=x+y+z.
\]

**2. Zero-frequency spectrum from a regenerative cycle.** Regenerate each time the chain enters state \(0\). One complete tour has independent holding times \(T_0,T_2\sim\operatorname{Exp}(\varepsilon)\) and \(T_1,T_3,T_4\sim\operatorname{Exp}(1)\). Its duration and raw integrated reward are
\[
\tau=T_0+T_1+T_2+T_3+T_4,
\qquad R=xT_1+yT_3+zT_4.
\]
Since successive tours are independent, the standard renewal-reward variance identity (or its direct proof by centering completed tours and controlling the two boundary tours) gives
\[
G_\varepsilon(0)=\frac{\operatorname{Var}(R-m_\varepsilon\tau)}{\mathbb E\tau}
=\frac{\varepsilon}{2+3\varepsilon}
\left[(x-m_\varepsilon)^2+(y-m_\varepsilon)^2
+(z-m_\varepsilon)^2+2\left(\frac{m_\varepsilon}{\varepsilon}\right)^2\right].
\]
All holding times have exponential moments, ensuring integrable stationary covariances and the requisite regeneration limits. Substituting \(m_\varepsilon\) proves
\(G_\varepsilon(0)/\varepsilon\to B(x,y,z)\).

**3. Intermediate-frequency spectrum from the exact resolvent.** For \(\omega>0\), solve
\[
(i\omega I-Q_\varepsilon)u=f,
\qquad f=(-m_\varepsilon,x-m_\varepsilon,-m_\varepsilon,
 y-m_\varepsilon,z-m_\varepsilon).
\]
The stationary spectral identity is
\[
G_\varepsilon(\omega)=2\operatorname{Re}
\sum_{j=0}^{4}\pi_{\varepsilon,j}f_j u_j.
\]
Set \(\alpha=\varepsilon/(\varepsilon+i\omega)\) and \(\beta=1/(1+i\omega)\). The five scalar resolvent equations become
\[
\begin{aligned}
u_0&=\alpha u_1-\frac{m_\varepsilon}{\varepsilon+i\omega},
&u_1&=\beta(u_2+x-m_\varepsilon),\\
u_2&=\alpha u_3-\frac{m_\varepsilon}{\varepsilon+i\omega},
&u_3&=\beta(u_4+y-m_\varepsilon),\\
&&u_4&=\beta(u_0+z-m_\varepsilon).
\end{aligned}
\]
If \(\varepsilon\ll\omega_\varepsilon\ll1\), then \(\alpha\to0\), \(\beta\to1\), and \(m_\varepsilon/(\varepsilon+i\omega_\varepsilon)\to0\). Substitution closes after one directed tour with feedback multiplier \(\alpha^2\beta^3\to0\); hence all five resolvent entries are uniformly bounded, and
\[
(u_0,u_1,u_2,u_3,u_4)\to(0,x,0,y+z,z).
\]
The slow-state contributions to \(G_\varepsilon(\omega)/\varepsilon\) vanish because \(f_0=f_2=-m_\varepsilon=O(\varepsilon)\), while \(\pi_1/\varepsilon=\pi_3/\varepsilon=\pi_4/\varepsilon\to1/2\). Therefore
\[
\frac{G_\varepsilon(\omega_\varepsilon)}{\varepsilon}
\longrightarrow x^2+y(y+z)+z^2=A(x,y,z).
\]
No eigenvalue-oscillation hypothesis is required: this is an observable-spectrum statement for a nonnormal chain.

**4. Sharp optimization over the three observable amplitudes.** The direct sum-of-squares identity
\[
12B-5A=
\frac{(4x+3y+3z)^2+7(y-z)^2}{4}\ge0
\]
proves \(A/B\le12/5\), since \(B>0\) for every nonzero triple. Equality forces \(y=z\) and \(4x+6y=0\), exactly \((x,y,z)=t(-3,2,2)\) with \(t\ne0\). For this triple, \(A=21\) and \(B=35/4\), so the ratio tends to \(12/5\).

**5. Implication for network-wide efficiency.** Choose the concrete scale \(\omega_\varepsilon=\sqrt\varepsilon\). Since \(G_{\max}\ge G_\varepsilon(\sqrt\varepsilon)\), for all sufficiently small \(\varepsilon>0\) the spectrum peaks away from zero, and
\[
\liminf_{\varepsilon\downarrow0}\eta_{(-3,2,2)}(Q_\varepsilon)
\ge1-\lim_{\varepsilon\downarrow0}
\frac{G_\varepsilon(0)}{G_\varepsilon(\sqrt\varepsilon)}
=1-\frac5{12}=\frac7{12}.
\]
Taking the supremum over admissible five-state networks proves the global lower bound. The argument establishes no global upper bound better than the known one.

## Verification

For the optimizing observable \(g=(0,-3,0,2,2)\), direct rational solution of the same five-state resolvent gives the additional finite-rate identities
\[
G_\varepsilon(0)=
\frac{10\varepsilon(15\varepsilon^2+20\varepsilon+7)}{(3\varepsilon+2)^3},
\]
\[
G_\varepsilon(\sqrt\varepsilon)=
\frac{2\varepsilon(25\varepsilon^4+133\varepsilon^3+224\varepsilon^2+129\varepsilon+21)}{(3\varepsilon+2)(\varepsilon^5+5\varepsilon^4+12\varepsilon^3+15\varepsilon^2+7\varepsilon+1)}.
\]
These yield \(G_\varepsilon(0)/\varepsilon\to35/4\) and \(G_\varepsilon(\sqrt\varepsilon)/\varepsilon\to21\), independently corroborating the regenerative and intermediate-frequency calculations. At \(\varepsilon=1/100\), the resulting *witness* efficiency \(1-G_\varepsilon(0)/G_\varepsilon(\sqrt\varepsilon)\) is approximately \(0.5803868669\); this is not claimed to equal the true frequency-optimized finite-rate efficiency.

The companion `verify.py` uses only the Python standard library. It independently evaluates resolvents using exact-rational Gaussian elimination (including the doubled real system for complex frequency), checks the finite-rate expressions, the regenerative formula, and the quadratic identity on many rational inputs. Run `python verify.py` in the directory containing that file. These finite checks support, but do not replace, the analytical proof.

## Relationship to prior work

Jia's October 2026 study, *Fundamental Bounds on the Oscillation Efficiency of Markov Networks* [1], defines the same observable-efficiency invariant, proves \(\eta_N^*\le\cos^2(\pi/N)\), proves the bound sharp for \(N=3,4\), and explicitly leaves its sharpness for \(N\ge5\) without proof. Its constructions are one-way three- and four-state rings. The present claim supplies a new five-state two-time-scale construction and a sharp, restricted-class three-amplitude analysis, giving
\[
\frac7{12}\le\eta_5^*\le\cos^2(\pi/5)=\frac{3+\sqrt5}{8}.
\]
The lower bound strictly exceeds the four-state benchmark \(1/2\) and the normal-network five-state maximum \((3-\sqrt5)/2\) already proved in [1]; it does **not** settle the remaining global gap.

Xu and Meng [2] constrain *generator eigenvalue imaginary parts* by cycle rate products and winding; those spectral-localization statements do not supply this specific real-observable power-spectrum ratio. Gupta and Khammash [3] provide general power-spectrum methodology, not the five-state sharp mesoscopic ratio. Jia, Qian and Zhang [4] compute an exact spectrum for a distinct hybrid gene-feedback model, rather than this five-state Markov ring. Searches against those statements and available related research records did not locate the \(12/5\) enhancement or the \(7/12\) global lower-bound witness. General resolvent theory makes the computations possible but does not, without this new optimization, imply the claimed sharp restricted-class value.

## Limitations

The exact sharpness applies **only** to the stated two-slow-state rate family, observables supported on its three fast states, and the specified mesoscopic-frequency scaling. No assertion is made that \(7/12\) is the five-state global optimum, that the finite-rate peak has a particular unique location, or that the Markov generator has nonreal eigenvalues. Backward jumps are absent, so entropy production is formally infinite and finite-dissipation bounds are inapplicable. A larger unknown family of generators or general results on nonnormal resolvent amplification could supersede the novelty of this explicit witness. The scientific argument and source comparisons have not undergone an independent audit.

## References

[1] C. Jia, *Fundamental Bounds on the Oscillation Efficiency of Markov Networks*, arXiv:2610.23310, first submitted 2026-10-16, https://arxiv.org/abs/2610.23310.

[2] R. Xu and C. Meng, *Coarse-grained kinetic scale tightens thermodynamic spectral bounds of Markov cycles*, arXiv:2608.22934, first submitted 2026-08-24, https://arxiv.org/abs/2608.22934.

[3] A. Gupta and M. Khammash, *Frequency spectra and the color of cellular noise*, Nature Communications **13**, 4305 (2022), https://doi.org/10.1038/s41467-022-31263-x.

[4] C. Jia, H. Qian and M. Q. Zhang, *Exact power spectrum in a minimal hybrid model of stochastic gene expression oscillations*, arXiv:1909.09769, https://arxiv.org/abs/1909.09769; SIAM Journal on Applied Mathematics **84** (2024), 1204–1226.
