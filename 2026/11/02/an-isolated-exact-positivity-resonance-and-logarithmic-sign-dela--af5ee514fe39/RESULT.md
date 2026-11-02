# An isolated exact-positivity resonance and logarithmic sign-delay for five-step BDFL decay

## Finding

For the five-step, second-order, L-stable BDFL method of Jensen, Ketcheson and Lóczi [1], apply four backward-Euler starting steps to the scalar dissipative equation \(y'=-\lambda y\), with \(\lambda>0\), initial value \(y(0)=1\), fixed \(h>0\), and \(r=h\lambda\). There is an **isolated positive parameter**
\[
 r_0=\sqrt5
\]
where the computed sequence stays strictly positive at every time index, namely
\[
 y_n=\left(\frac{\sqrt5-1}{4}\right)^n,\qquad n\ge0.
\]
In a punctured open interval about \(r_0\), the very same recurrence with the same positive backward-Euler starting rule has infinitely many negative terms and infinitely many positive terms, notwithstanding its asymptotic stability. The first negative index \(N_-(r)=\min\{n\ge5:y_n<0\}\) has the sharp asymptotic law
\[
 N_-(r)=\frac{\log(1/|r-\sqrt5|)}{\log(\rho_0/t_0)}+O(1),
 \qquad r\to\sqrt5,\quad r\ne\sqrt5,
\]
where \(t_0=(\sqrt5-1)/4\) and \(\rho_0\in(0.498,0.499)\) is the modulus of the larger-modulus conjugate root pair of the explicit quartic below. Numerically, \(1/\log(\rho_0/t_0)\approx2.09108896394658\).

## Assumptions and scope

Use exact real arithmetic and an unforced scalar initial-value problem. The method coefficients (from [1], Table 1) are
\[
\begin{aligned}
a_4&=\frac{45+14\sqrt5}{44},&a_3&=-\frac{\sqrt5}{2},\\
a_2&=\frac{25+9\sqrt5}{88},&a_1&=-\frac{10-3\sqrt5}{22},\\
a_0&=\frac{13-5\sqrt5}{88},&\beta&=\frac{5(7-\sqrt5)}{44}.
\end{aligned}
\]
Set \(y_j=(1+r)^{-j}\) for \(0\le j\le4\), and for every integer \(n\ge0\) use
\[
 (1+\beta r)y_{n+5}=\sum_{j=0}^{4}a_j y_{n+j}.
\]
The starting procedure is expressly **four backward-Euler steps**, not the TR-BDF2 starter used in [1]'s numerical experiments. No claim is made about variable steps, rounding, other starters, or nonlinear vector equations.

## Proof

**1. Algebraic eigenmode coincidence.** Define
\[
 F_r(z)=(1+\beta r)z^5-\sum_{j=0}^{4}a_j z^j,
 \qquad q(r)=\frac1{1+r}.
\]
Direct exact simplification gives
\[
 F_r(q(r))=\frac{r^2(\sqrt5-3)(7-\sqrt5)(r-\sqrt5)
 (r^2+(5+3\sqrt5)/2)}{176(1+r)^5}.
\]
For \(r>0\), this expression vanishes if and only if \(r=\sqrt5\). The starting values \(y_j=q(r)^j\) then agree with a genuine characteristic eigenmode of the recurrence for every \(j\in\{0,1,2,3,4\}\), and so the recurrence propagates precisely \(y_n=q(r)^n\) for all \(n\ge0\). This proves positivity at \(r_0\) and the uniqueness of a positive *exact geometric-starter/eigenmode coincidence*. It does not yet assert a global classification of all other step sizes.

**2. Spectral separation at the coincidence.** At \(r_0=\sqrt5\), \(F_{r_0}(z)=(1+\beta r_0)(z-t_0)Q(z)\), with
\[
 \begin{aligned}
 Q(z)={}&z^4+\frac{-69+3\sqrt5}{131}z^3
 +\frac{217-55\sqrt5}{262}z^2\\
 &+\frac{-74+26\sqrt5}{131}z
 +\frac{37-13\sqrt5}{262}.
 \end{aligned}
\]
Here is a reproducible rational-arithmetic root-isolation certificate. The strictly rational bounds \(2236067977/10^9<\sqrt5<2236067978/10^9\) are checked by squaring. Put \(\varepsilon=1/4000\) and select complex rational centers
\[
 c_1=-\frac{23}{2000}+\frac{623}{1250}i,
 \qquad c_2=\frac{2493}{10000}+\frac{2443}{10000}i.
\]
For each \(c\in\{c_1,c_2\}\), exact evaluation with the above rational interval for \(\sqrt5\) verifies
\[
 |Q(c)|<10^{-5},\quad |Q'(c)|>\frac18,
 \quad\left|\frac{Q^{(j)}(c)}{j!}\right|<10\quad(j=2,3,4).
\]
Because \(10^{-5}+10(\varepsilon^2+\varepsilon^3+\varepsilon^4)<\varepsilon/8\), Rouché's theorem relative to the linear Taylor term gives exactly one zero in each open \(\varepsilon\)-disk about \(c_1,c_2\), and real coefficients give a zero in each of their conjugate disks. These four disjoint disks exhaust the quartic roots. The first pair, denoted \(z_0,\overline{z_0}\), has strictly greater modulus \(\rho_0=|z_0|\in(0.498,0.499)\) than the second pair \(w_0,\overline{w_0}\), with \(|w_0|\in(0.348,0.350)\); all four exceed \(t_0\approx0.3090\) in modulus. Their roots are simple. The unique root in the upper half-plane near \(c_1\) has argument within \(0.03\) radians of \(\pi/2\). In particular \(\rho_0>t_0>0\). All these inequalities persist for \(r\) in some open neighborhood of \(r_0\).

**3. Perturbing the starter and the modes.** Denote the continued simple roots by \(t(r)\in\mathbb R_{>0}\), \(z(r),\overline{z(r)}\), \(w(r),\overline{w(r)}\), retaining their strict modulus order. For five distinct roots \(\xi_i(r)\), the solution whose first five values are \(q(r)^j\) has the exact Lagrange/Vandermonde decomposition
\[
 y_n=\sum_i C_i(r)\xi_i(r)^n,
 \qquad C_i(r)=\prod_{k\ne i}\frac{q(r)-\xi_k(r)}{\xi_i(r)-\xi_k(r)}.
\]
The coefficients are real-analytic in \(r\) near \(r_0\) after selecting smooth root branches. At \(r_0\), the coefficient of \(t\) equals one and all others vanish. The factorization in Step 1 shows \(q(r)-t(r)\) vanishes **to first order**, since \(F_r(q)=(1+\beta r)\prod_i(q-\xi_i)\), the other factors are nonzero, and the first-order factor \(r-\sqrt5\) in Step 1 is simple. Hence the coefficient of the dominant complex root satisfies
\[
 C_z(r)=\gamma(r-r_0)+O((r-r_0)^2),\qquad \gamma\ne0,
\]
while \(C_t(r)=1+O(|r-r_0|)\), \(C_w(r)=O(|r-r_0|)\). The amplitude of the growing-relative-to-\(t\) oscillation is therefore proportional to the detuning, not identically zero off resonance.

**4. Infinitely many sign changes.** Write \(z(r)=\rho(r)e^{i\theta(r)}\). Since \(|\theta(r)-\pi/2|<0.03\) near resonance, every four consecutive cosine values \(\cos(n\theta(r)+\psi)\) include one smaller than \(-1/2\) and one greater than \(1/2\), uniformly in the starting phase \(\psi\). To see this, four samples spaced exactly \(\pi/2\) contain extrema below \(-1/\sqrt2\) and above \(1/\sqrt2\), and a perturbation of at most \(3(0.03)<0.09\) in phase preserves the weaker half-unit bounds. The asymptotically dominant component is \(2\Re(C_z z^n)\), whose magnitude is proportional to \(|r-r_0|\rho(r)^n\). Because \(\rho(r)>|w(r)|\) and \(\rho(r)>t(r)\), it dominates the other components for sufficiently large \(n\), so the claimed positive and negative subsequences are infinite.

**5. Sharp delay.** Set \(\delta=r-r_0\), \(L(r)=\log(\rho(r)/t(r))>0\). Uniform analytic bounds give \(C_t(r)>1/2\), \(c|\delta|\le|C_z(r)|\le C|\delta|\), \(|C_w(r)|\le C|\delta|\) for small nonzero \(\delta\). It follows that for every fixed sufficiently large \(K\), all integer \(n\le\log(1/|\delta|)/L(r)-K\) have \(y_n>0\), because the total nonpositive absolute contribution is bounded by a small multiple of \(t(r)^n\). For all \(n\ge\log(1/|\delta|)/L(r)+K\), the dominant complex term outweighs both the positive real term and the subdominant complex term on the negative-cosine samples; some such sample occurs in each block of four. Thus
\[
 N_-(r)=\frac{\log(1/|\delta|)}{L(r)}+O(1).
\]
Analytic continuation implies \(L(r)=L(r_0)+O(|\delta|)\); consequently replacing the denominator by \(L(r_0)=\log(\rho_0/t_0)\) changes the right-hand side by \(o(1)\), proving the stated law.

## Verification

The supplied `verify.py` independently evaluates the exact factorization of \(F_r(q)\), checks the quartic factor, implements the four Rouché disk certificates using rational inequalities (including exact enclosures for \(\sqrt5\)), and checks the generated recurrence at 170-digit precision. The root-isolation computations validate finite algebraic statements; the infinite sign and delay assertions rest on Steps 3–5, not finite experiments. To reproduce, run `python verify.py` with SymPy and mpmath installed.

## Relationship to prior work

Jensen–Ketcheson–Lóczi [1, Table 1, Sections 3.2–3.3] introduce the five-step L-stable formula, and [1, Section 5] uses TR-BDF2 for initialization. Their presented stability and error-constant theory does not identify a backward-Euler startup step size at which a complex-dominant recurrence is exactly restricted to its positive real root. Standard multistep root analysis [2,3] provides the modal-decomposition ingredients, but no source inspected supplied the explicit \(r_0=\sqrt5\) coincidence together with the dominant-root ordering and logarithmic detuning delay for this method. The conclusion is limited to the searched sources; absence from those sources is not a guarantee of historical priority.

## Limitations

The special trajectory requires exact arithmetic, a constant positive timestep, the stated scalar equation and exactly four backward-Euler starting steps. It is not claimed to occur for the TR-BDF2 starter of [1], nor to describe finite-precision computations, PDE spatial discretizations, general stiff nonlinear systems, positivity of arbitrary initial histories, or a global sign classification over all \(r>0\). The neighborhood in which the punctured statement holds exists by rigorous continuity but is not assigned a sharp numerical endpoint. The near-resonance delay is asymptotic and has a bounded but not universally constant integer phase correction. Independent mathematical audit remains outstanding.

## References

[1] T. Jensen, D. I. Ketcheson and L. Lóczi, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1 (first submitted 2026-10-15), https://arxiv.org/abs/2610.22685 . Full text inspected: introductory stability discussion, Table 1 and Sections 3.2–3.3, numerical starting procedures in Section 5, and variable-step distinctions in Section 6.

[2] E. Hairer and G. Wanner, *Solving Ordinary Differential Equations II*, Springer, 1996, stability and multistep root theory; cited in [1].

[3] T. A. Driscoll and R. J. Braun, *Fundamentals of Numerical Computation*, section on zero-stability and the root condition, https://fncbook.github.io/v1.0/ivp/zerostability.html .
