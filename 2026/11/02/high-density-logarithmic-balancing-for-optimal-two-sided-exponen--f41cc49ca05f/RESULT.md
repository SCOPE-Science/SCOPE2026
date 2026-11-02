# High-density logarithmic balancing for optimal two-sided-exponential Gabor frames

## Finding

For an integer \(q\ge2\), let \(g(t)=e^{-|t|}\) in \(L^2(\mathbb R)\), normalized so that \(\|g\|_2=1\). For each \(\eta>0\), let \(\mathcal G_{q,\eta}\) be the Gabor system
\[
\left\{e^{2\pi i m t/\eta}\,g(t-n\eta/q):m,n\in\mathbb Z\right\}.
\]
Its lattice has redundancy \(q\). Write \(A_q(\eta)>0\) and \(B_q(\eta)\) for the *optimal* lower and upper frame bounds and \(\kappa_q(\eta)=B_q(\eta)/A_q(\eta)\). The existence and uniqueness of a global minimizer \(\eta_q\) of this condition number are established in the earlier work of Faulhuber and Shafkulovska (Reference 2).

**The new asymptotic assertion** is that, as integer \(q\to\infty\), with \(L_q=\log(2q)\),
\[
\boxed{\eta_q=2L_q+O\!\left(\frac{L_q^2}{q^2}\right)}
\]
and
\[
\boxed{\min_{\eta>0}\kappa_q(\eta)
=1+\frac{2L_q^2+2L_q+1}{q^2}
+O\!\left(\frac{L_q^4}{q^4}\right).}
\]
The implied constants are absolute for all sufficiently large integer \(q\). In particular, the minimum condition-number excess is asymptotic to \(2(\log q)^2/q^2\). The location estimate resolves the optimizing-lattice parameter to an additive error vanishing much faster than one; the earlier location theorem confines it only to an interval of order \(\log q\).

## Assumptions and scope

The window is exactly the real two-sided exponential \(g(t)=e^{-|t|}\). The rectangular lattice is \((\eta/q)\mathbb Z\times\eta^{-1}\mathbb Z\), and \(q\) is a *positive integer at least two*. Frame bounds are for the standard Gabor frame inequality on all of \(L^2(\mathbb R)\), not a finite sample or a truncated matrix. The condition number is the ratio of its optimal spectral bounds. The limiting regime varies both lattice side lengths while holding the window fixed and sending integer redundancy to infinity. Neither uniqueness nor the exact finite-redundancy formula is asserted to be new; both are inputs from Reference 2.

## Proof

**1. Exact prior formulas and normalization.** Put \(x=\eta/q\) and
\[
 a(x)=\frac{x}{\sinh x},\qquad b(x)=x\coth x,
 \qquad u(\eta)=\frac{\eta}{\sinh\eta}.
\]
The sharp frame bounds calculated by Janssen and recorded in Equation (8.1) of Reference 2, in the normalization used here, are
\[
 A_q(\eta)=\tanh(\eta/2)\,[a(x)-u(\eta)],
 \qquad B_q(\eta)=\coth(\eta/2)\,[b(x)+u(\eta)].
\]
Since \(x<\eta\) and \(z/\sinh z\) is strictly decreasing on \((0,\infty)\), the lower bound is positive. The exact ratio therefore admits the factorization
\[
 \kappa_q(\eta)=\cosh x\,\coth^2(\eta/2)
 \frac{1+u(\eta)/b(x)}{1-u(\eta)/a(x)}. \tag{1}
\]
Reference 2, Theorem 2.7, proves that \(\eta_q\) exists uniquely and satisfies
\[
 \operatorname{arcosh}q<\eta_q<4\operatorname{arcosh}q. \tag{2}
\]
In particular, \(\eta_q\asymp\log q\), \(\eta_q/q\to0\), and \(e^{-\eta_q}\to0\). The proof below only needs (1) and the stated prior uniqueness/localization theorem.

**2. Uniform asymptotic expansion, with derivative.** Write \(\rho=e^{-\eta}\) and \(F_q(\eta)=\log\kappa_q(\eta)\). On the entire interval in (2), for large \(q\), the quantities \(x\), \(\rho\), and \(u/a\) tend uniformly to zero. Here are the elementary expansions used, with uniform remainder bounds in this interval:
\[
\begin{aligned}
 \log\cosh x&=\tfrac12x^2+O(x^4),\\
 2\log\coth(\eta/2)&=4\rho+O(\rho^3),\\
 u(\eta)&=2\eta\rho+O(\eta\rho^3),\\
 a(x)^{-1}+b(x)^{-1}&=2+O(x^2).
\end{aligned}
\]
Expanding the two logarithms in the last factor of (1), whose arguments remain uniformly in a fixed neighborhood of one, gives
\[
 F_q(\eta)=\frac{\eta^2}{2q^2}+4(1+\eta)e^{-\eta}
  +O\!\left(\frac{\eta^4}{q^4}
 +\frac{\eta^3 e^{-\eta}}{q^2}
 +\eta^2 e^{-2\eta}+e^{-3\eta}\right). \tag{3}
\]
To control *the location* rather than just the value, we also need to differentiate. Differentiating the exact elementary factors of (1), and using the same convergent expansions (not differentiating an unspecified remainder), yields uniformly on (2)
\[
 F_q'(\eta)=\frac1q\tanh(\eta/q)-4\eta e^{-\eta}
 +O\!\left(\frac{\eta^3e^{-\eta}}{q^2}
 +\eta^2e^{-2\eta}+e^{-3\eta}\right). \tag{4}
\]
For completeness, the exact derivatives of the nontrivial factors are
\[
\begin{aligned}
 a'(x)&=\operatorname{csch}x\,(1-x\coth x),\\
 b'(x)&=\coth x-x\operatorname{csch}^2x,\\
 u'(\eta)&=\operatorname{csch}\eta\,(1-\eta\coth\eta),\\
 \frac{d}{d\eta}[2\log\coth(\eta/2)]&=-2\operatorname{csch}\eta.
\end{aligned}
\]
Substitution into the logarithmic derivative of (1) proves (4). In particular the derivative of \(4(1+\eta)e^{-\eta}\) is \(-4\eta e^{-\eta}\), explaining the balancing equation.

**3. Localization to a vanishing absolute error.** At the interior minimum \(\eta=\eta_q\), Equation (4) vanishes. The Taylor expansion \(\tanh z=z+O(z^3)\) gives, with \(\rho_q=e^{-\eta_q}\),
\[
 \frac1{q^2}-4\rho_q
 =O\!\left(\frac{\eta_q^2}{q^4}
 +\frac{\eta_q^2\rho_q}{q^2}
 +\eta_q\rho_q^2+\frac{\rho_q^3}{\eta_q}\right). \tag{5}
\]
By (2), \(\eta_q\asymp\log q\) and \(\eta_q\rho_q\to0\). The terms in (5) containing \(\rho_q\) are therefore \(o(\rho_q)\), while its first error term is \(o(q^{-2})\). Equation (5) first gives \(\rho_q\sim1/(4q^2)\). Substituting this preliminary estimate back into (5) improves it to
\[
 \rho_q=\frac1{4q^2}\left(1+O\!\left(\frac{(\log q)^2}{q^2}\right)\right). \tag{6}
\]
Taking the negative logarithm of (6) gives the claimed location law
\[
 \eta_q=\log(4q^2)+O\!\left(\frac{(\log q)^2}{q^2}\right)
 =2\log(2q)+O\!\left(\frac{(\log q)^2}{q^2}\right).
\]

**4. Three terms of the optimal condition number.** At \(\eta=\eta_q\), all error terms in (3) are \(O((\log q)^4/q^4)\), by (2) and (6). Substituting \(\eta_q=2L_q+O(L_q^2/q^2)\) and \(e^{-\eta_q}=1/(4q^2)(1+O(L_q^2/q^2))\) into (3) gives
\[
 F_q(\eta_q)=\frac{2L_q^2+2L_q+1}{q^2}
 +O\!\left(\frac{L_q^4}{q^4}\right). \tag{7}
\]
The right side tends to zero. Finally \(e^y=1+y+O(y^2)\) converts (7) into the stated expansion for \(\kappa_q(\eta_q)\). This completes the proof.

## Verification

The proof is analytical and valid for the infinite sequence of all integers \(q\ge2\) in the asserted limit. The accompanying `check_asymptotic.py` uses high-precision arithmetic to compute the stationary point of the *exact* formula (1), verify the derivative at that point, and compare the finite-density values with the three-term approximation. Tested redundancies range from \(q=2\) to \(q=16384\). Those finite numerical checks detect transcription or normalization errors but do not independently establish a uniform asymptotic bound.

## Relationship to prior work

Reference 1 (publicly posted 2026-08-05) establishes the exact qualitative frame set of every continuous integrable totally positive window, providing the recent general framework in which quantitative stability becomes natural. The two-sided exponential is an illustrative already-known window within that class; the 2026 paper does not assert optimized condition-number asymptotics.

Reference 2 already gives the *exact* finite-\(q\) frame-bound functions and establishes existence and uniqueness of the minimizing lattice (Theorem 2.7); its result includes the much broader finite-parameter setup. Those are used here and **are not claimed as discoveries**. What is established here is the asymptotic extraction from the implicitly defined optimizer: the explicit logarithmic centering with an absolute vanishing error and the three logarithmic coefficients of the optimal spectral-conditioning excess. Unlike merely substituting a fixed lattice into the known frame-bound formula, the argument controls the moving optimal lattice via a uniform differentiated expansion.

Reference 3 treats Zak transforms and lower estimates for totally positive functions but does not, in the inspected portions, state the optimizer asymptotic (although the earlier quantitative frame literature remains a residual coverage risk).

## Limitations

Only integer redundancy tending to infinity, a fixed normalized symmetric two-sided exponential, and rectangular lattices are considered. The theorem does not classify nonrectangular optimal lattices or provide uniform asymptotics for arbitrary totally positive windows. The finite-\(q\) uniqueness theorem and sharp frame-bound identities are imported faithfully from Reference 2. The 1996 original source of some exact exponential frame-bound formulas and potential unindexed follow-up work were not exhaustively searched in full text. The novelty claim is limited to the displayed high-density asymptotic estimates, not the exact frame-bound formulas or qualitative frame existence.

## References

1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992, first public preprint 2026-08-05. https://arxiv.org/abs/2608.04992
2. M. Faulhuber and I. Shafkulovska, *Gabor Frame Bound Optimizations*, arXiv:2204.02917, Equation (8.1) and Theorem 2.7; 2022 preprint, revised 2023, also Appl. Comput. Harmon. Anal. 67 (2023), 101574. https://arxiv.org/abs/2204.02917
3. T. Kloos and J. Stöckler, *Zak Transforms and Gabor Frames of Totally Positive Functions and Exponential B-Splines*, arXiv:1311.7359, 2013 preprint / J. Approx. Theory 184 (2014), 209–237. https://arxiv.org/abs/1311.7359
4. A. J. E. M. Janssen, *Some Weyl-Heisenberg Frame Bound Calculations*, Indag. Math. (N.S.) 7 (1996), 165–183; older formulas credited through Reference 2.
