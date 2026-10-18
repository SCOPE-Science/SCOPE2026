# Reentrant discount-rate stability and a universal sampling barrier in exact one-step receding-horizon control

## Finding
For the scalar plant \(\dot x=u\), a receding-horizon controller that *exactly* minimizes the discounted continuous-time quadratic running cost over one zero-order-held sampling interval can be asymptotically stable at small and at large discount rates but unstable between them. There is a **sharp universal sampling threshold** for this reentrant behavior. With \(h>0\) the hold length, \(r>0\) the control penalty, and \(\rho\ge0\) the within-hold exponential discount, introduce, for \(z>0\),
\[
\psi(z)=\frac{z-4}{2z^2}+\frac{z+4}{2z(e^z-1)}.
\]
Let \(z_\dagger\) be the unique positive root of
\[
K(z)=(8-z)(e^z-1)^2-4z(e^z-1)-z^2(z+4)e^z=0
\]
and set \(M=\psi(z_\dagger)\) and \(H_*=M^{-1/2}\). Numerically,
\[
z_\dagger=7.6636051835440198508\ldots,\quad M=0.031547317895875515727\ldots,\quad H_*=5.6301346164001932383\ldots.
\]
For \(h/\sqrt r<H_*\), the repeated one-step feedback is asymptotically stable for **every** \(\rho\ge0\). At equality, the only non-asymptotically-stable discount is \(\rho=z_\dagger/h\), where the sampled multiplier equals \(-1\). When \(h/\sqrt r>H_*\), there are exactly two positive rates \(\rho_-<\rho_+\), defined by \(\psi(\rho_\pm h)=r/h^2\), and the sampled loop is asymptotically stable precisely for \(\rho\in[0,\rho_-)\cup(\rho_+,\infty)\). At the two endpoints the multiplier is \(-1\); inside the intervening interval it is below \(-1\).

Complementarily, for every fixed \(r>0\) and \(\rho>0\), there is exactly one positive sampling-length stability boundary \(h_*(r,\rho)=z_\beta/\rho\), where \(\beta=r\rho^2\) and \(z_\beta\) is the unique positive solution of \(\phi(z)=\beta\), with
\[
\phi(z)=\frac{z-4}{2}+\frac{z(z+4)}{2(e^z-1)}.
\]
The sampled loop is stable for \(h<h_*\), neutral at \(h=h_*\), and unstable for \(h>h_*\). At \(\rho=0\) the sampled loop is stable for every finite \(h>0\).

## Assumptions and scope
Fix \(h>0\), \(r>0\), and \(\rho\ge0\). The scalar real integrator obeys \(\dot x(t)=u(t)\). At each sample \(kh\), its current state \(x_k\) is measured exactly, and a constant control \(u_k\) on that entire interval minimizes
\[
J_{h,\rho,r}(x_k,u)=\int_0^h e^{-\rho t}\bigl((x_k+tu)^2+ru^2\bigr)\,dt.
\]
There is no terminal cost or terminal constraint, and the minimization is repeated afresh at the next sample. All calculations are in exact real arithmetic. "Asymptotically stable" means the sampled scalar multiplier has modulus strictly less than one, equivalently exponential convergence of every sampled trajectory to zero. Neutral endpoints have multiplier \(-1\), giving nondecaying sign alternation. This is the specific one-step receding-horizon feedback, not general finite-horizon MPC or continuous-time infinite-horizon LQR.

## Proof
**1. Exact first-step feedback.** The coefficient of \(u^2\) in \(J\) is \(\int_0^h e^{-\rho t}(t^2+r)\,dt>0\), hence the minimizer is unique. For \(\rho>0\) put \(z=\rho h\), \(\beta=r\rho^2\), and
\[
A=1-e^{-z},\quad B=1-(1+z)e^{-z},\quad C=2-(z^2+2z+2)e^{-z}.
\]
Direct integration gives \(\int e^{-\rho t}\,dt=A/\rho\), \(\int te^{-\rho t}\,dt=B/\rho^2\), and \(\int t^2e^{-\rho t}\,dt=C/\rho^3\), all over \([0,h]\). Thus
\[
u_k=-\frac{\rho B}{\beta A+C}x_k,\qquad x_{k+1}=g x_k,\qquad g=1-\frac{zB}{\beta A+C}.
\]
Here \(A,B,C>0\), so \(g<1\), and \(-1<g\) is equivalent to \(\beta A+C>zB/2\), or \(\beta>\phi(z)\) with the displayed \(\phi\). Since \(\beta=r\rho^2=(r/h^2)z^2\), this is \(r/h^2>\psi(z)\). Equality gives \(g=-1\); the reversed strict inequality gives \(g<-1\). In the undiscouted case direct quadrature yields
\[
g(h,r,0)=1-\frac{h^2}{2r+2h^2/3}\in(-1/2,1).
\]

**2. Unique global peak.** The exponential series gives \(\lim_{z\downarrow0}\psi(z)=-1/12\) and \(\lim_{z\to\infty}\psi(z)=0\) (the latter approached from above). Direct differentiation yields the identity
\[
2z^3(e^z-1)^2\psi'(z)=K(z)
=(8-z)e^{2z}-(16+2z+4z^2+z^3)e^z+8+3z.
\]
The coefficients of \(z^n/n!\) for \(n\ge2\) in \(K\) are exactly
\[
a_n=2^{n-1}(16-n)-(n^3+n^2+16).
\]
The constant and linear coefficients vanish. Exactly \(a_2=a_3=a_4=0\), the eleven integers \(a_5,\ldots,a_{15}\) are
\[
10,52,168,432,966,1956,3652,6304,9906,13428,12768,
\]
and \(a_n<0\) for every integer \(n\ge16\), immediately because \(16-n\le0\). Consequently \(K(z)/z^{15}\) is **strictly decreasing** for \(z>0\): all terms with exponents \(n-15<0\) have positive coefficients and strictly decreasing values, the \(n=15\) term is constant, and all positive-power terms have negative coefficients and strictly decreasing values. Termwise differentiation is legitimate by locally uniform convergence of the entire exponential series. Moreover \(K(z)>0\) sufficiently close to zero since \(a_5=10\), whereas \(K(z)<0\) for every \(z\ge8\) by the first displayed representation. Hence \(K\) has exactly one positive zero \(z_\dagger\), and \(\psi\) strictly increases before that zero and strictly decreases thereafter. Its global maximum \(M>0\) is unique. Since the stability requirement is \(r/h^2>\psi(\rho h)\) and \(z=\rho h\) runs through all positive reals, comparing \(r/h^2\) against \(M\) proves the universal three-case discount-rate classification, including exactly two crossings whenever \(0<r/h^2<M\).

**3. Unique fixed-discount sampling boundary.** Define \(F(z)=zB-2C=(z-4)+(z^2+3z+4)e^{-z}\). Elementary differentiation gives
\[
F(0)=F'(0)=0,\qquad F'(z)=B-z^2e^{-z},\qquad F''(z)=z(z-1)e^{-z}.
\]
Thus \(F'\) strictly decreases on \((0,1)\), strictly increases on \((1,\infty)\), and tends to \(1\). Starting from zero, \(F\) first decreases and eventually increases to infinity, so it has exactly one positive zero \(z_0\) (numerically \(z_0=2.6879993454994913415\ldots\)), with \(z_0>1\) and \(F>0\) on \((z_0,\infty)\). Since \(\phi=F/(2A)\), it is nonpositive before \(z_0\). For \(z\ge z_0\), write \(N=F'A-FA'\). Then \(N(z_0)>0\) and
\[
N'(z)=e^{-z}\bigl[z(z-1)A(z)+F(z)\bigr]>0.
\]
Therefore \(\phi'(z)=N/(2A^2)>0\) on \([z_0,\infty)\). Finally \(\phi(z)\sim z/2-2\to\infty\). Every \(\beta>0\) admits exactly one crossing \(\phi(z)=\beta\); the fixed-\(\rho\) claim follows.

**4. Exact instability witness.** At \(h=6,r=1,\rho=1\), direct substitution simplifies the sampled multiplier to
\[
g=\frac{-1-3e^{-6}}{1-17e^{-6}}<-1,
\]
because \(e^6>17\). At \(\rho=0\) the multiplier is \(-5/13\). The two positive critical rates in this example are \(0.8927203477806972133\ldots\) and \(2.0005877285196713611\ldots\), calculated by solving \(\psi(6\rho)=1/36\). The phase diagram, rather than finite testing, establishes stability again at every \(\rho>\rho_+\).

## Verification
Run `python verify.py` with Python 3.10+, SymPy and mpmath. The standalone verifier checks the exact differentiation identity, the decisive factorial-scaled Taylor coefficients, the rational undiscounted case, the exponential witness, sample direct numerical quadratures of the optimality condition, and the quoted high-precision roots and rate crossings. Its finite numerical samples are not substitutes for the all-parameter sign and uniqueness arguments in the proof. All formulas are derived from the exact running-cost integral without an integration scheme.

## Relationship to prior work
Zhang, Hørsholt and Jørgensen (2024, arXiv:2407.18769v1) provide exact matrix-weight discretization for discounted continuous-time linear-quadratic control with piecewise-constant inputs. The first-step quadratic integration here is an instance of that established framework. Granzotto, Postoyan, Bușoniu, Nešić and Daafouz (2021) analyze stability/performance for finite-horizon discounted **discrete-time** control, where a one-stage uniform discrete-time discount does not change the one-stage optimizer. The present one-interval controller instead weights *different times inside each hold*, so the discount changes the exact one-step optimizer. Schwenkel and collaborators (2024) study economic MPC with nonterminal discount functions under different objectives and guarantees. These works motivate but do not directly imply the exact unique two-rate instability window or universal threshold above. No claim is made of priority over unidentified equivalent published results.

## Limitations
The theorem is for a scalar integrator, positive control penalty, one step of lookahead, zero terminal penalty, fixed zero-order holds and exact state feedback. The intermediate instability is a property of this deliberately short-horizon policy, not a failure of exact running-cost discretization or a counterexample to discounted MPC results that impose terminal ingredients, long horizons or other stability hypotheses. Numerical constants are approximations of rigorously defined unique roots; no interval-arithmetic certificate is claimed. Generalization to multidimensional or constrained plants and robustness to perturbations have not been established. Publication-priority uncertainty persists beyond the inspected literature and mathematical-record search.

## References
1. Z. Zhang, J. B. Hørsholt and J. B. Jørgensen, *Numerical Discretization Methods for the Discounted Linear Quadratic Control Problem*, arXiv:2407.18769v1 (first public version, 2024-07-26). https://arxiv.org/html/2407.18769v1
2. M. Granzotto, R. Postoyan, L. Bușoniu, D. Nešić and J. Daafouz, *Finite-Horizon Discounted Optimal Control: Stability and Performance* (2021), accessible public manuscript: https://www.researchgate.net/publication/340573124_Finite-Horizon_Discounted_Optimal_Control_Stability_and_Performance
3. L. Schwenkel et al., *On discount functions for economic model predictive control without terminal conditions*, arXiv:2405.14361 (2024). https://arxiv.org/abs/2405.14361
