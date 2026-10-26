# Sharp contact-mass loss under strong harmonic binding with finite run-and-tumble duration

## Finding
Consider two noncrossing run-and-tumble particles in one dimension whose relative distance \(X\geq0\) is driven by harmonic attraction and a six-state relative propulsion process with finite tumbling periods. For every fixed \(\alpha,\beta,v>0\), let \(\mu\to\infty\) denote increasing harmonic attraction strength. Then the stationary *atom at exact contact* has the sharp expansion
\[
\boxed{\Pr_\mu\{X=0\}=\frac12-\frac{K(\alpha,\beta)}{\mu^2}+o(\mu^{-2}),}\qquad
K(\alpha,\beta)=\frac{\pi^2\alpha^2\beta^2}{32(\alpha+\beta)^2}
\left(1+\frac{\beta}{4\alpha}+\frac{\alpha}{2\beta}\right)>0.
\]
For all \(\mu>0\), the stationary support obeys \(0\leq X\leq v/\mu\), hence \(X\) converges weakly to a point mass at zero even though its probability of **exactly** being zero converges only to one half. The coefficient is independent of propulsion speed \(v\). The order \(\mu^{-2}\) is caused by rapid *two-switch* passages from positive propulsion through a zero-velocity tumbling state into negative propulsion, and by subsequent missed contacts that persist during zero-velocity intervals.

## Assumptions and scope
The relative velocity state is \(\sigma\in\{2,1,0_s,0_t,-1,-2\}\), with zero labels distinct, and follows the autonomous irreducible Markov chain in the ordered basis above with generator
\[
Q=\begin{pmatrix}
-2\alpha&2\alpha&0&0&0&0\\
\beta/2&-\alpha-\beta&\beta/2&\alpha&0&0\\
0&\alpha&-2\alpha&0&\alpha&0\\
0&\beta&0&-2\beta&\beta&0\\
0&0&\beta/2&\alpha&-\alpha-\beta&\beta/2\\
0&0&0&0&2\alpha&-2\alpha
\end{pmatrix}.
\]
The propulsion values for \(0_s,0_t\) are both zero. Between velocity jumps, \(\dot X=-2\mu X+v\sigma\) for \(X>0\). At the reflecting/jamming boundary \(X=0\), outward (negative) deterministic drift is suppressed, and nonnegative drift is unchanged. No translational Brownian noise is included. Holding-time clocks are independent exponentials with the rates in \(Q\). This is precisely the finite-tumble/harmonic-interaction specialization of the interacting-particle setup in Hahn, arXiv:2501.11379, Section 1.1. All claims are for fixed strictly positive \(\alpha,\beta,v\), and \(\mu\to\infty\).

## Proof
**Existence and compact support.** For any interval with constant \(\sigma\), the deterministic flow is a contracting affine map, clipped at zero. Since \(-2\mu X+v\sigma\leq-2\mu X+2v\), the interval \([0,v/\mu]\) is forward-invariant and globally attracting. A negative-velocity interval of sufficiently long duration takes the entire interval to zero. Such intervals occur almost surely for the irreducible finite-state velocity chain; coupling at the first such episode yields the unique stationary law in the compact interval. The same bound gives weak convergence of its \(X\)-marginal to \(\delta_0\).

**An idealized contact indicator.** In a bi-infinite stationary velocity path, let \(C^*\in\{0,1\}\) be one if the most recent *nonzero* propulsion has negative sign, zero if its sign is positive; the state is propagated unchanged through \(0_s\) and \(0_t\). Under sign reversal \(\sigma\mapsto-\sigma\), the generator is unchanged, with both zero labels fixed. Therefore \(\Pr(C^*=1)=1/2\). The true indicator \(C=1_{\{X=0\}}\) satisfies \(C\leq C^*\): positive propulsion immediately separates the particles; zero propulsion preserves contact or noncontact; negative propulsion can only create contact, possibly after a finite delay. Hence
\[
\frac12-\Pr_\mu\{X=0\}=\Pr(C^*=1,C=0)=:\Delta_\mu.
\]

**Finite recovery time.** If \(\sigma=-1\) and the distance is \(x>0\), then, absent a velocity switch, the exact time until contact is
\[
\tau_\mu(x)=\frac{1}{2\mu}\log\left(1+\frac{2\mu x}{v}\right).
\]
Let \(F_\mu(x)\) be the expected total future time spent in \(\{C^*=1,C=0\}\), starting immediately after a switch into \(-1\) at distance \(x\), and terminating when contact is made or positive propulsion next appears. For \(0<x\leq v/\mu\), a first-jump decomposition gives, uniformly in \(x\),
\[
F_\mu(x)=B\tau_\mu(x)+O_{\alpha,\beta}(\tau_\mu(x)/\mu),\qquad
B=1+\frac{\beta}{4\alpha}+\frac{\alpha}{2\beta}.
\]
Indeed, uninterrupted travel contributes \(\tau_\mu(x)+O(\tau_\mu(x)^2)\). A switch from \(-1\) to \(0_s\) occurs at rate \(\beta/2\) and, before positive propulsion resumes or contact is later reached, contributes the zero-state mean holding time \(1/(2\alpha)\) to first order; a switch to \(0_t\) occurs at rate \(\alpha\) and contributes \(1/(2\beta)\). A switch to \(-2\) contributes only \(O(\tau_\mu(x)^2)\). After a zero holding period \(H\sim\operatorname{Exp}(\rho)\), the remaining distance is multiplied by \(e^{-2\mu H}\). Any later negative-velocity recovery therefore costs an expected \(O(\tau_\mu(x)\rho/(\rho+2\mu))\); further switches are bounded by the finite-state geometric renewal estimate. These observations establish the uniform remainder above. All constants may depend on the fixed rates, never on \(x\) or \(\mu\).

**Stationary crossing flux.** The velocity chain's invariant probabilities at \(+1,-1,0_s,0_t,\pm2\) are
\[
\pi_{+1}=\pi_{-1}=\frac{\alpha\beta}{(\alpha+\beta)^2},\quad
\pi_{0_s}=\frac{\beta^2}{2(\alpha+\beta)^2},\quad
\pi_{0_t}=\frac{\alpha^2}{(\alpha+\beta)^2},\quad
\pi_{\pm2}=\frac{\beta^2}{4(\alpha+\beta)^2}.
\]
The ideal indicator changes from zero to one only on a passage \(+1\to0_j\to-1\) with \(j=s,t\). Such passages form disjoint mismatch episodes. Conditional on leaving \(+1\) for \(0_j\), the residence time \(S_j\) in the zero state is exponential with rate \(\rho_s=2\alpha\) or \(\rho_t=2\beta\). If the distance at the \(+1\)-departure is \(Y_\mu\), then the distance at the negative entry is \(Y_\mu e^{-2\mu S_j}\). Palm occupation / renewal reward therefore gives exactly
\[
\Delta_\mu=\pi_{+1}\sum_{j=s,t}q_{+1,0_j}q_{0_j,-1}
\int_0^\infty e^{-\rho_j s}
\mathbb E\big[F_\mu(Y_\mu e^{-2\mu s})\mid(+1\to0_j)\big]ds.
\]
The exponential holding time in \(+1\), of rate \(\alpha+\beta\), is independent of the entry distance and the identity of the following jump. In that holding time the dimensionless distance \(U_\mu=2\mu Y_\mu/v\) relaxes to one. Since \(0\leq U_\mu\leq2\),
\[
\mathbb E|U_\mu-1|\leq\frac{\alpha+\beta}{\alpha+\beta+2\mu}\longrightarrow0.
\]

**Sharp limit.** Substitute the uniform recovery estimate and change variables \(u=2\mu s\). Dominated convergence is valid because \(U_\mu\leq2\) and \(\log(1+U_\mu e^{-u})\leq2e^{-u}\). Thus
\[
\lim_{\mu\to\infty}\mu^2\int_0^\infty e^{-\rho_j s}
\mathbb E\left[\tau_\mu(Y_\mu e^{-2\mu s})\right]ds
=\frac14\int_0^\infty\log(1+e^{-u})du=\frac{\pi^2}{48}.
\]
The last equality follows by integrating the alternating logarithmic series; its sum is \(\sum_{n\ge1}(-1)^{n+1}/n^2=\pi^2/12\). Since
\[
\sum_{j=s,t}q_{+1,0_j}q_{0_j,-1}=(\beta/2)\alpha+\alpha\beta=\frac{3\alpha\beta}{2},
\]
we obtain \(\mu^2\Delta_\mu\to (\alpha\beta/(\alpha+\beta)^2)(3\alpha\beta/2)(\pi^2/48)B=K(\alpha,\beta)\). This proves the theorem.

## Verification
The accompanying `verify_contact.py` reconstructs \(Q\), checks the exact rational stationary vector for 100 positive rational parameter pairs, independently compares the flux and simplified coefficients, and verifies the logarithmic integral numerically. On its recorded execution it passed 502 checks. Separate event-driven Monte Carlo tests of the exact clipped affine flow at \(\alpha=\beta=v=1\) and \(\mu\in\{2,4,8,16,32,64\}\) showed the scaled deficit tending toward \(K(1,1)\approx0.134936\); the finite simulation is corroboration, not a proof of the limiting asymptotic.

## Relationship to prior work
Hahn, arXiv:2501.11379v1, supplies the six-state generator, the hard-jamming harmonic flow, and exact invariant measures for other combinations of finite tumbling and interaction potentials. Its Section 1.1 expressly identifies the finite-tumble harmonic invariant measure as analytically challenging. The present result obtains a sharp contact-atom asymptotic for exactly that unsolved combination without claiming the full stationary measure. Le Doussal–Majumdar–Schehr, arXiv:2105.11838, solve harmonically interacting two-state (instantaneous-tumble) particles without the same finite-duration hard-jamming dynamics. Slowman–Evans–Blythe, arXiv:1705.04812, solve finite-tumble exclusion on a periodic lattice, not the strongly harmonically bound continuum pair. These precedents supply context but do not state or imply this six-state strong-binding coefficient without further analysis.

## Limitations
The formula is pointwise for fixed positive tumbling rates and no thermal diffusion; it is not uniform if \(\alpha\) or \(\beta\) tend to zero or infinity with \(\mu\). It only characterizes the exact-contact atom, not the full bulk stationary density nor finite-\(\mu\) convergence rates. The distinction between weak convergence to \(\delta_0\) and convergence of the atom must not be conflated. The limit is analytically proved; numerical checks are supplementary. Independent mathematical assessment of originality and proof details has not been performed.

## References
1. L. Hahn, *Steady state and mixing of two run-and-tumble particles interacting through jamming and attractive forces*, arXiv:2501.11379v1 (first posted 2025-01-20), especially Sections 1.1 and 2.
2. P. Le Doussal, S. N. Majumdar and G. Schehr, *Stationary nonequilibrium bound state of a pair of run and tumble particles*, arXiv:2105.11838v1 (2021), Section IV.3.
3. A. B. Slowman, M. R. Evans and R. A. Blythe, *Exact Solution of Two Interacting Run-and-Tumble Random Walkers with Finite Tumble Duration*, arXiv:1705.04812v1 (2017).
