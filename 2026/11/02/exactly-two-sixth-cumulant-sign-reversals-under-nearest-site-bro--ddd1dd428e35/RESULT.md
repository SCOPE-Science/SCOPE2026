# Exactly two sixth-cumulant sign reversals under nearest-site Brownian resetting

## Finding
Consider Brownian motion of generator \(D\partial_{xx}\) on \(\mathbb R\), started at the origin, with independent Poisson resetting of rate \(r\) to the closest site in \(\ell\mathbb Z\). Here \(D,r,\ell>0\), and ties, which occur with probability zero, may be resolved arbitrarily. Let \(\kappa_6(X_t)\) denote the sixth cumulant of its **actual continuous position**, not just its reset-site index. Put
\[
a=\frac{\ell}{2}\sqrt{\frac rD},\qquad S=\sinh a,\qquad H=\cosh a.\]
The asymptotic sixth cumulant rate exists and has the exact formula
\[
\boxed{\lim_{t\to\infty}\frac{\kappa_6(X_t)}t
=\frac{D\ell^4a^2H}{8S^8}\,N(a),}
\]
where the explicit even entire function \(N\) is
\[
\begin{aligned}
N(a)={}&\tfrac12\cosh(6a)+27\cosh(4a)+\tfrac{135}2\cosh(2a)-95\\
&+a\big[-\tfrac{15}2\sinh(5a)+\tfrac{45}8\sinh(4a)-\tfrac{405}2\sinh(3a)
+\tfrac{135}4\sinh(2a)-435\sinh a\big]\\
&+a^2\big[\tfrac{135}8\cosh(4a)+270\cosh(2a)+\tfrac{2745}8\big].
\end{aligned}
\]
**There exist precisely two numbers \(0<a_-<a_+<\infty\) satisfying \(N(a_\pm)=0\). Both zeros are simple.** The sixth-cumulant rate is strictly positive for \(0<a<a_-\), strictly negative for \(a_-<a<a_+\), and strictly positive for \(a>a_+\). Numerically,
\[
a_-\simeq0.1893047722836880,\qquad a_+\simeq3.7962487562346393.
\]
Thus, as the dimensionless resetting rate \(\rho=r\ell^2/D=4a^2\) increases, its sign passes through **positive–negative–positive** regimes, with thresholds
\[
\rho_-\simeq0.1433451872375159,\qquad \rho_+\simeq57.64601847685218.
\]
The defining equations and strict root count, rather than these rounded decimals, are the exact classification.

## Assumptions and scope
The model is on the infinite one-dimensional line, with nearest-site complete resets to an evenly spaced lattice. Between resets it follows standard Brownian motion of variance \(2Dt\); the reset clock is independent, homogeneous, and exponentially distributed; all parameter choices satisfy \(D,r,\ell>0\). The observation is the unwrapped physical position \(X_t\), not its reduction modulo \(\ell\). All limits are taken with these three parameters fixed and \(t\to\infty\). The sixth cumulant is the sixth derivative at zero of \(\log\mathbb E e^{qX_t}\), with respect to the real physical tilt \(q\).

## Proof
**1. Renewal kernel and displacement cumulants.** Set \(B_s=\sqrt{2D}W_s\), and let \(J_s\in\mathbb Z\) be the nearest integer to \(B_s/\ell\). During the first reset interval, which ends with intensity \(re^{-rs}\,ds\), the particle is moved to \(\ell J_s\). Translation invariance then restarts the complete process independently. Hence its moment generating function \(M(q,t)=\mathbb E e^{qX_t}\) satisfies
\[
M(q,t)=e^{-(r-Dq^2)t}+\int_0^t re^{-rs}\mathbb E[e^{q\ell J_s}]M(q,t-s)\,ds.
\tag{1}
\]
For \(\lambda\) near zero, exponentially killing the Brownian flight at total rate \(r+\lambda\) gives a symmetric Laplace law of scale \(\sqrt{D/(r+\lambda)}\). Summing its mass over the lattice Voronoi cells yields the exact joint transform, with \(u=q\ell\) and \(\beta=\ell\sqrt{(r+\lambda)/D}\):
\[
\int_0^\infty re^{-(r+\lambda)s}\mathbb E[e^{q\ell J_s}]\,ds
=\frac r{r+\lambda}\left[1+
\frac{\cosh(\beta/2)(\cosh u-1)}{\cosh\beta-\cosh u}\right].
\tag{2}
\]
The right side equals one exactly when
\[
\lambda\left[\cosh\!\left(\ell\sqrt{\frac{r+\lambda}{D}}\right)-\cosh(q\ell)\right]
=r\cosh\!\left(\frac\ell2\sqrt{\frac{r+\lambda}{D}}\right)[\cosh(q\ell)-1].
\tag{3}
\]
At \(q=\lambda=0\), the derivative of the left-minus-right side with respect to \(\lambda\) equals \(\cosh(\ell\sqrt{r/D})-1>0\); therefore (3) has a unique analytic, even branch \(\lambda(q)\) near zero. The exponentially integrable renewal kernel in (1) has a simple rightmost pole there: at \(q=0\) the only pole in a strip around zero is the renewal pole at zero, and analyticity plus positivity and the nonlattice continuous reset-time law preserve this isolated dominant pole for small complex \(q\). Analytic renewal asymptotics give \(\log M(q,t)=t\lambda(q)+O(1)\), locally uniformly with its first six derivatives near zero. In particular,
\[
\lim_{t\to\infty}\frac{\kappa_6(X_t)}{t}=\lambda^{(6)}(0).
\tag{4}
\]
This applies to the actual continuous position because equation (1) includes its terminal, incompletely reset Brownian flight.

**2. Sixth-order expansion.** Introduce \(k=r\ell^2/D=4a^2\), \(\Lambda(u)=\ell^2\lambda(u/\ell)/D\). Then equation (3) becomes
\[
\Lambda[\cosh\sqrt{k+\Lambda}-\cosh u]
=k\cosh(\tfrac12\sqrt{k+\Lambda})(\cosh u-1).
\tag{5}
\]
Write \(\Lambda(u)=Au^2+Bu^4+Cu^6+O(u^8)\). Comparing coefficients and simplifying gives
\[
A=\frac{a^2\cosh a}{\sinh^2a},\qquad
B=\frac{A\,[2\sinh a(3+\sinh^2a)-3a(2+\sinh^2a)]}{24\sinh^3a},
\]
\[
\boxed{C=\frac{a^2\cosh a}{5760\sinh^8a}\,N(a).}
\tag{6}
\]
For an independently checkable coefficient identity, set \(L=2S^2\), \(L_1=SH/(2a)\), \(L_2=(2a\cosh2a-\sinh2a)/(32a^3)\), \(H_1=S/(8a)\), \(H_2=(aH-S)/(64a^3)\). Directly from (5),
\[
C=\frac{B/2+A/24+4a^2(H/720+H_1A/24+H_1B/2+H_2A^2/4)-2ABL_1-A^3L_2/2}{L}.
\tag{7}
\]
Reducing (7) to (6) is an exact Laurent-polynomial identity in \(e^a\) and \(a\), independently verified by `CHECK.py`. Since \(\lambda^{(6)}(0)=6!D\ell^4C\), this proves the claimed sixth-cumulant formula.

**3. Exact count of positive zeros.** Let \(b_n=(2n)![a^{2n}]N(a)\). Direct hyperbolic Taylor expansion shows \(b_0=b_1=b_2=b_3=0\), and, for every integer \(n\ge2\),
\[
\begin{aligned}
b_n={}&\tfrac12 36^n-3n25^n
+\left(27+\tfrac{45n}{16}+\tfrac{135n(2n-1)}{64}\right)16^n
-135n9^n\\
&+\left(\tfrac{135}{2}+\tfrac{135n}{4}+135n(2n-1)\right)4^n-870n.
\end{aligned}
\tag{8}
\]
Exact integer calculations give \(b_4=2880>0\), \(b_n<0\) for \(5\le n\le11\), and \(b_{12}>0\). Moreover \(b_n>0\) for **every** \(n\ge12\): the strictly increasing ratios \((36/25)^n/n\), \((16/9)^n/n\), and \(4^n/n\) for \(n\ge12\), with the exact base inequalities
\[
(36/25)^{12}>72,\qquad (16/9)^{12}>60,\qquad \tfrac{135}{2}4^{12}>870\cdot12,
\]
allow \(\tfrac12 36^n\) to dominate \(3n25^n\), \(27\cdot16^n\) to dominate \(135n9^n\), and \(\tfrac{135}{2}4^n\) to dominate \(870n\). All remaining terms in (8) are nonnegative.

For \(z>0\), form the entire function \(G(z)=N(\sqrt z)/z^4\), extended at zero by \(G(0)=b_4/8!=1/14>0\). The coefficient sign pattern implies that
\[
\frac{G'(z)}{z^6}=
\sum_{n=5}^{11}\frac{(n-4)b_n}{(2n)!}z^{n-11}
+\sum_{n=12}^\infty\frac{(n-4)b_n}{(2n)!}z^{n-11}
\tag{9}
\]
is **strictly increasing**: every term in the first sum has negative coefficient and a nonpositive exponent, whereas every term in the second has positive coefficient and positive exponent. In fact its derivative is strictly positive (the first sum includes negative powers and the second positive powers). Its limits are negative infinity as \(z\downarrow0\) and positive infinity as \(z\to\infty\). Hence \(G\) has exactly one critical point, a strict global minimum.

An exact rational certificate proves \(G(1)=N(1)<0\): writing \(z=e\), expand \(16z^6N(1)\) as the integer polynomial printed and checked in `CHECK.py`, and bound \(e\) between \(\sum_{j=0}^{20}1/j!\) and this rational sum plus \(1/(20\cdot20!)\). Taking the upper or lower endpoint separately for positive or negative monomials gives a strictly negative rational upper bound. Finally the leading exponential term \(\tfrac14e^{6a}\) dominates the remaining terms of \(N(a)\), so \(G(z)\to+\infty\). Thus \(G\) decreases from a positive value to a negative minimum, then increases to positive infinity: exactly two positive, simple roots. Multiplication by \(z^4\) does not create nonzero roots, so the same is true for \(N(a)\). The signs in the theorem follow.

## Verification
Run `python3 CHECK.py` with Python 3, `sympy`, and `mpmath`. It checks the exact Laurent-polynomial identity in (6)–(7), the coefficient values and rigorous tail inequalities from (8), an exact rational certificate that \(N(1)<0\), and numerical agreement between the independently evaluated renewal-root equation (5) and its sixth-order expansion. It reports 30 passed checks and approximate threshold locations. The infinite root count is proved in step 3, not inferred from finite tests or sign plots. The threshold digits are numerical approximations, not interval-arithmetic certificates for every displayed digit.

## Relationship to prior work
Alston and Bertrand (2024), `arXiv:2401.12772v1`, introduce nearest-site resetting and derive its effective diffusion coefficient and transport-optimal regular lattice; their main text's equations (1)–(20), sections on first passage, splitting and effective diffusivity do not give a sixth displacement cumulant or its sign transitions. The established effective diffusion coefficient is recovered here as \(D_{\mathrm{eff}}=DA\). A previously recorded result (identifier `c991ac64-5238-4cf5-a452-90f6cdcdb988`) gives the **full analytic counting-field root** for completed-reset-cell displacement on an asymmetric periodic lattice, which specializes to (3) and therefore *already implies the possibility of deriving (6) by differentiation*. No novelty is claimed for a generic counting-field equation or for the existence of a sixth-order Taylor coefficient. Another result for this exact nearest-site model (identifier `88701ce9-5655-49ee-8f08-34795844182a`) already proves positivity of the **fourth** long-time displacement cumulant for all rates. Neither prior claim states or implies without a new global sign analysis that the **sixth** coefficient has exactly two parameter zeros. The new contribution is the exact two-transition classification and the finite-to-infinite coefficient-sign proof, not the routine formal differentiation. Di Bello *et al.* (2023), `arXiv:2302.06696v1`, study an initial-position resetting mechanism and a many-particle crossing current; its full text defines a different reset map and observable, so its current large-deviation formulas do not directly settle this single-particle nearest-lattice sixth cumulant. Generic analytic renewal theory supplies the underlying generating-function method, not the two-zero sign classification. A wider theorem about cumulants of Markov-additive processes may imply some algebraic ingredients and remains a literature-priority risk.

## Limitations
This is an exact classification for fixed positive diffusivity and lattice spacing with spatially uniform Poisson nearest-site resetting, on an infinite one-dimensional line. It does not assert sixth-cumulant signs at finite times, a result for nonuniform/resetting-rate-dependent spatial arrays, or higher-order cumulant classification. The presence of a positive fourth cumulant throughout does not force the sixth to remain positive. The theorem's mathematical proof has been reviewed within the same analytical process; no independent audit or independent publication-priority adjudication has been performed. Supplemental material mentioned by the motivating article could not be independently checked in full.

## References
1. H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772v1, publicly posted 2024-01-23. https://arxiv.org/html/2401.12772v1
2. C. Di Bello, A. K. Hartmann, S. N. Majumdar, F. Mori, A. Rosso, and G. Schehr, *Current fluctuations in stochastically resetting particle systems*, arXiv:2302.06696v1, publicly posted 2023-02-13. https://arxiv.org/html/2302.06696v1
3. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic resetting and applications*, Journal of Physics A 53 (2020), 193001. https://doi.org/10.1088/1751-8121/ab7cfe
