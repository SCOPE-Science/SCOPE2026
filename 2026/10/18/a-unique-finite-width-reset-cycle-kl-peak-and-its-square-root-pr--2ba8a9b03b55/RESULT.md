# A unique finite-width reset-cycle KL peak and its square-root protocol gap

## Finding
For a one-dimensional overdamped harmonic Langevin process that is repeatedly returned to a fixed centered Gaussian of strictly positive cold temperature, the **per-time symmetrized endpoint Kullback–Leibler divergence** has a unique positive optimal reset frequency for each of two protocols: deterministic periodic resetting and independent Poisson resetting. As the ratio of equilibrium to cold temperature diverges, the two optimal frequencies differ at leading order by a factor of \(\sqrt{2}\), and the periodic protocol's maximal KL rate exceeds the Poisson protocol's maximal KL rate by a sharp positive square-root term.

Put \(\lambda=2k/\gamma>0\), \(a=T/T_c-1>0\), and \(q=r/\lambda\). Define the maximal dimensionless KL rates \(M_{\mathrm{per}}(a)=\sup_{q>0}\mathcal R_{\mathrm{per}}(\lambda q)/\lambda\) and \(M_{\mathrm{pois}}(a)=\sup_{q>0}\mathcal R_{\mathrm{pois}}(\lambda q)/\lambda\). Each supremum has precisely one maximizer, denoted \(q_{\mathrm{per}}(a)\) and \(q_{\mathrm{pois}}(a)\). As \(a\to\infty\),

\[
\frac{q_{\mathrm{per}}(a)}{\sqrt a}\longrightarrow\frac{1}{\sqrt2},\qquad
\frac{q_{\mathrm{pois}}(a)}{\sqrt a}\longrightarrow1,
\]

\[
M_{\mathrm{per}}(a)=\frac a2-\sqrt{\frac a2}+o(\sqrt a),\qquad
M_{\mathrm{pois}}(a)=\frac a2-\sqrt a+o(\sqrt a),
\]

and hence

\[
\boxed{M_{\mathrm{per}}(a)-M_{\mathrm{pois}}(a)=\left(1-\frac1{\sqrt2}\right)\sqrt a+o(\sqrt a).}
\]

In particular, the periodic protocol has the larger *optimized endpoint-KL rate* for all sufficiently large \(a\). The claim makes no assertion that this endpoint quantity is the full implementation-dependent physical entropy-production rate.

## Assumptions and scope
Fix \(k,\gamma,T,T_c>0\) with \(T>T_c\). Between resets the overdamped Ornstein–Uhlenbeck process obeys \(\gamma\,dX_t=-kX_t\,dt+\sqrt{2\gamma k_B T}\,dW_t\). Each reset independently redraws the position from the centered Gaussian of variance \(k_B T_c/k\); a fresh cycle therefore starts from precisely that distribution. Reset epochs are either \(1/r\) apart (periodic) or form an independent homogeneous Poisson process of rate \(r>0\). No delta-distribution reset, vanishing-width state, or stochastic-trajectory entropy-production identity is assumed.

For a cycle of age \(t\), write \(P_c=N(0,k_B T_c/k)\) and \(P_t\) for its unreset distribution. The dimensionless per-cycle observable is the Jeffreys divergence \(J(t)=D_{\mathrm{KL}}(P_c\Vert P_t)+D_{\mathrm{KL}}(P_t\Vert P_c)\). The average *reward per physical time* is the mean Jeffreys divergence per cycle divided by the mean cycle length; multiply by \(k_B\) to give it entropy units. It is an endpoint-information quantity and, depending on the thermodynamic implementation, a lower-bound component rather than the complete dissipation.

The variance solves \(\sigma^2(t)=(k_B/k)[T_c+(T-T_c)(1-e^{-\lambda t})]\); consequently its ratio to the cold variance is \(\rho(t)=1+a(1-e^{-\lambda t})\). The centered-Gaussian divergence formula gives \(J(t)=\frac12(\rho(t)+\rho(t)^{-1}-2)\).

## Proof
**Exact reduction.** Write \(z(x)=1-e^{-x}\) and define \(f_a(x)=a^2z(x)^2/[2(1+az(x))]\). Then \(J(t)=f_a(\lambda t)\). With \(q=r/\lambda\), renewal reward averaging and the exponential holding-time density give

\[
H_a(q):=\frac{\mathcal R_{\mathrm{per}}(r)}\lambda=q f_a(1/q),\qquad
G_a(q):=\frac{\mathcal R_{\mathrm{pois}}(r)}\lambda=q^2\int_0^\infty e^{-qx}f_a(x)\,dx.
\]

Integration by parts (using \(f_a(0)=0\) and boundedness at infinity) yields \(G_a(q)=q\int_0^\infty e^{-qx} f_a'(x)\,dx=\mathbb E[f_a'(Y/q)]\), where \(Y\) is unit exponential. Direct differentiation gives

\[
f_a'(x)=\frac{a^2e^{-x}z(x)[2+az(x)]}{2[1+az(x)]^2}>0\quad(x>0).
\]

**Periodic uniqueness.** For \(x>0\), its elasticity is

\[
h_a(x):=\frac{x f_a'(x)}{f_a(x)}=\frac{x}{e^x-1}\frac{2+az(x)}{1+az(x)}.
\]

Both positive factors decrease strictly with \(x\), and \(h_a(0+)=2\), \(h_a(\infty)=0\). Since \(H_a'(q)=f_a(1/q)-q^{-1}f_a'(1/q)=f_a(1/q)[1-h_a(1/q)]\), the derivative changes sign exactly once, from positive to negative. Since \(H_a(q)\to0\) at both endpoints \(q\downarrow0\) and \(q\uparrow\infty\), the unique critical point is the unique global maximum.

**Poisson uniqueness.** Let \(g(w)=w(2+w)/(1+w)^2=1-(1+w)^{-2}\). Then \(f_a'(x)=(a/2)e^{-x}g(az(x))\). The function \(A(u)=\log z(e^u)\) is increasing and strictly concave: its derivative is \(e^u/(e^{e^u}-1)\), which decreases strictly from one to zero. The function \(B(v)=\log g(ae^v)\) is increasing and concave, because \(B'(v)=2/[(1+ae^v)(2+ae^v)]\) is positive and strictly decreasing. Thus \(F(u)=\log f_a'(e^u)=\log(a/2)-e^u+B(A(u))\) is concave.

Putting \(s=\log q\) and writing the unit-exponential random variable as \(Y=e^v\), the density of \(v\) is \(\exp(v-e^v)\). Hence

\[
G_a(e^s)=\int_{\mathbb R}\exp\{v-e^v+F(v-s)\}\,dv.
\]

The integrand is jointly log-concave in \((s,v)\). Prékopa's marginal log-concavity theorem therefore implies that \(s\mapsto G_a(e^s)\) is log-concave. This function is positive, real analytic (a Laplace transform evaluated at \(e^s>0\)), and tends to zero as \(s\to\pm\infty\) by bounded convergence and the two vanishing endpoint limits of \(f_a'\). A positive log-concave function has a convex set of maximizers. Two distinct maximizers would force a nontrivial constant interval, contradicting real analyticity and the vanishing endpoint limits. Thus the Poisson maximum exists and is unique.

**Sharp large-temperature-ratio scaling.** Use the identity

\[
f_a(x)=\frac a2z(x)-\frac12+\frac1{2[1+az(x)]}.
\]

Writing \(J_a(q)=\mathbb E[(1+a z(Y/q))^{-1}]\), this gives

\[
G_a(q)=\frac a2\frac q{q+1}-\frac q2+\frac q2J_a(q).
\]

For \(q=c\sqrt a\) and fixed \(c>0\), split the expectation at \(Y=q\). Since \(z(x)\ge x/2\) for \(0\le x\le1\),

\[
0\le J_a(q)\le\frac{2q}{a}\log(1+a/2)+e^{-q}=O(a^{-1/2}\log a).
\]

Differentiating the integrand of \(J_a\) and using \(xe^{-x}\le1-e^{-x}\) shows \(0\le qJ_a'(q)\le J_a(q)\). Therefore, uniformly for \(c\) in compact subintervals of \((0,\infty)\),

\[
G_a'(c\sqrt a)=\frac1{2c^2}-\frac12+o(1).
\]

The derivative is eventually positive at every \(c<1\) and negative at every \(c>1\). Log-concavity and uniqueness already established guarantee that the unique maximizer lies between these test points, yielding \(q_{\mathrm{pois}}(a)/\sqrt a\to1\). Substitution in the displayed formula for \(G_a\), with the bound on \(J_a\), gives \(M_{\mathrm{pois}}(a)=a/2-\sqrt a+o(\sqrt a)\).

For the periodic protocol the same identity gives

\[
H_a(q)=\frac a2q(1-e^{-1/q})-\frac q2+\frac q{2[1+a(1-e^{-1/q})]}.
\]

At \(q=c\sqrt a\), direct differentiation and the expansion \(1-(1+1/q)e^{-1/q}=1/(2q^2)+O(q^{-3})\) yield

\[
H_a'(c\sqrt a)=\frac1{4c^2}-\frac12+o(1).
\]

By periodic uniqueness its maximizer therefore satisfies \(q_{\mathrm{per}}(a)/\sqrt a\to 1/\sqrt2\). Expanding \(q(1-e^{-1/q})=1-(2q)^{-1}+O(q^{-2})\) at that maximizing scale gives \(M_{\mathrm{per}}(a)=a/2-\sqrt{a/2}+o(\sqrt a)\). Subtracting the two expansions proves the claimed protocol gap.

## Verification
A standalone numerical consistency script, `check.py`, implements the exact Gaussian formulas, differentiates them by independent finite differences, compares the two equivalent Poisson renewal integrals, and numerically finds both optimizers over finite parameter ranges. It passed 230 assertions. At \(a=10^6\), it returned \(q_{\mathrm{pois}}/\sqrt a\approx1.004917\), \(q_{\mathrm{per}}/\sqrt a\approx0.707274\), and the normalized optimized gap \((M_{\mathrm{per}}-M_{\mathrm{pois}})/\sqrt a\approx0.289629\), approaching the proved value \(1-1/\sqrt2\approx0.292893\). These computations are not substitutes for the analytic uniqueness and asymptotic proofs.

Reproduce with Python and the packages in `requirements.txt`: `python check.py`.

## Relationship to prior work
Farago (arXiv:2605.28445v1) establishes the harmonic Gaussian endpoint-KL construction and obtains approximate Poisson and periodic rates in the sharp-reset regime, including qualitative behavior at slow and extremely fast resetting. The exact, strictly positive cold-variance renewal objective analyzed here is a finite-width specialization compatible with that endpoint framework. The new claim is the *global uniqueness* of both optima for every finite width, the sharp asymptotics of their locations and values, and the positive leading optimized protocol gap. The Gaussian relative-entropy formula, renewal averaging, and Prékopa's marginal log-concavity theorem are prior standard ingredients, not claimed as discoveries.

Fuchs, Goldt and Seifert (arXiv:1603.01141v1) analyze resetting entropy and thermodynamic work through stationary currents and Shannon-information balances. Their entropy observable is distinct from the present Jeffreys-divergence reward of a single finite-width harmonic cycle. General renewal-reward formulas likewise do not automatically imply the two uniqueness assertions or the sharp temperature-ratio coefficients.

## Limitations
This is a precise theorem about per-time *symmetrized endpoint KL divergence*, not a claim about the full physical entropy generated by resetting hardware, path-space dissipation, heat-engine efficiency, or arbitrary reset distributions. A physical reset implementation could add strictly positive entropy production whose dependence on \(r\) changes the optimal rate. The Gaussian distribution is independently redrawn at every reset; no carry-over memory is allowed. The optimal-location asymptotics hold as \(T/T_c\to\infty\) with other parameters fixed and do not imply uniform validity of teleportation or continuum physical approximations in that limit. Periodic and Poisson reset protocols are not compared at every fixed rate; the strictly positive optimized gap is proved asymptotically.

## References
1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445v1 (first posted 2026-05-27), https://arxiv.org/abs/2605.28445.
2. J. Fuchs, S. Goldt and U. Seifert, *Stochastic thermodynamics of resetting*, Europhysics Letters 113 (2016), 60009; arXiv:1603.01141v1, https://arxiv.org/html/1603.01141v1.
3. A. Prékopa, *On logarithmic concave measures and functions*, Acta Sci. Math. (Szeged) 34 (1973), 335–343, https://acta.bibl.u-szeged.hu/14411/.
