# Monotone residence exchange and a quartic crossover law in a switching nilpotent center

## Finding

Consider the continuous, piecewise-cubic planar differential equation
\[
\dot x=y,\qquad
\dot y=\begin{cases}
-d_+x^3,&x\geq0,\\
cx^2-d_-x^3,&x<0,
\end{cases}
\]
with fixed \(c,d_+,d_->0\). For every \(E>0\), let \(\gamma_E\) be the periodic trajectory of energy \(E\), and let \(F(E)\) denote the fraction of its **original physical time** spent in \(x<0\):
\[
F(E)=\frac{1}{T(E)}\operatorname{Leb}\{t\in[0,T(E)):x_{\gamma_E}(t)<0\}.
\]
Here \(T(E)\) is its minimal period. Then \(F:(0,\infty)\to(0,1)\) is **strictly increasing**, with the exact endpoint laws
\[
F(E)\sim \frac{C_3}{C_4}\frac{d_+^{1/4}}{c^{1/3}}E^{1/12}
\quad(E\downarrow0),\qquad
\lim_{E\to\infty}F(E)=\frac{d_+^{1/4}}{d_+^{1/4}+d_-^{1/4}},
\]
where
\[
C_3=\frac{\sqrt2\,3^{1/3}}{3}B\!\left(\frac13,\frac12\right),\qquad
C_4=\frac12 B\!\left(\frac14,\frac12\right).
\]
Thus there is **exactly one** energy \(E_*\in(0,\infty)\) with \(F(E_*)=1/2\) if and only if \(d_+>d_-\). For \(d_+\leq d_-\), there is no such energy. In the case \(d_+>d_-\), put \(\Delta=d_+-d_-\). With \(c,d_-\) fixed and \(\Delta\downarrow0\), the unique crossing obeys the sharp singular law
\[
\boxed{\lim_{\Delta\downarrow0}\frac{E_*\Delta^4}{c^4d_-}
=\left(\frac{4\sqrt2}{3C_4}\right)^4.}
\]
In addition, the approach to the high-energy time share is quantified by
\[
F(E)=\frac{A}{A+B}-\frac{B D}{(A+B)^2}E^{-1/4}+O(E^{-1/2}),
\quad A=C_4d_-^{-1/4},\quad B=C_4d_+^{-1/4},\quad D=\frac{\sqrt2 c}{3d_-}.
\]
Every limit and error term is for the parameter range just stated, and each asymptotic with a fixed parameter tuple is understood pointwise in that tuple.

## Assumptions and scope

The restoring force is continuously differentiable across \(x=0\), but it need not be twice differentiable there. The equation is locally Lipschitz and Hamiltonian with conserved energy
\[
H(x,y)=\frac12y^2+V(x),\qquad
V(x)=\begin{cases}
\frac{d_+}{4}x^4,&x\geq0,\\
\frac c3|x|^3+\frac{d_-}{4}|x|^4,&x<0.
\end{cases}
\]
Both one-sided potentials are strictly increasing with distance from the origin and tend to infinity. Therefore every \(E>0\) is a regular, simple closed energy oval surrounding the unique equilibrium at the origin. There is one positive and one negative turning point. The claim is restricted to this conservative three-parameter subfamily and makes no assertion about general switching cubic systems, perturbations, or limit-cycle cyclicity.

## Proof

**1. Exact side-time quadratures.** For \(d>0\) and \(\alpha\geq0\), let \(r(\alpha,d)>0\) be the unique root of
\[
\frac\alpha3r^3+\frac d4r^4=1,
\]
and set
\[
P(\alpha,d)=\sqrt2\int_0^{r(\alpha,d)}
\frac{dz}{\sqrt{1-\alpha z^3/3-dz^4/4}}.
\]
Each half-line excursion (from \(x=0\) to its turning point and back) is traversed once per period. Changing position by \(x=E^{1/4}z\) gives the **exact**, not asymptotic, relations
\[
\tau_+(E)=E^{-1/4}P(0,d_+),\qquad
\tau_-(E)=E^{-1/4}P(cE^{-1/4},d_-),
\]
and \(T(E)=\tau_+(E)+\tau_-(E)\), \(F(E)=\tau_-(E)/T(E)\).
The quartic beta integral evaluates to
\[
P(0,d)=C_4d^{-1/4}.
\]

**2. Strict monotonicity.** Write \(W_\alpha(z)=\alpha z^3/3+dz^4/4\) and let \(z_\alpha(u)>0\) solve \(W_\alpha(z_\alpha(u))=u\) for \(0<u\leq1\). The inverse-potential change of variable gives
\[
P(\alpha,d)=\sqrt2\int_0^1
\frac{du}{\sqrt{1-u}\,G_\alpha(u)},\qquad
G_\alpha(u)=\alpha z_\alpha(u)^2+d z_\alpha(u)^3.
\]
At fixed \(u>0\), implicit differentiation yields
\[
\partial_\alpha z_\alpha(u)=-\frac{z_\alpha(u)}{3(\alpha+dz_\alpha(u))},\qquad
\partial_\alpha G_\alpha(u)=\frac{\alpha z_\alpha(u)^2}{3(\alpha+dz_\alpha(u))}>0
\quad(\alpha>0).
\]
Consequently \(G_\alpha(u)^{-1}\) strictly decreases with \(\alpha\) for each \(u>0\), including comparison to \(\alpha=0\) by continuity. The positive integrable kernel preserves strict inequalities. Thus \(P(\alpha,d)\) is strictly decreasing on \([0,\infty)\). Since \(cE^{-1/4}\) strictly decreases with \(E\), the ratio \(\tau_-(E)/\tau_+(E)\), and hence \(F(E)\), is strictly increasing. The inverse-potential integrand is integrable near \(u=0\) (power \(u^{-2/3}\) when \(\alpha>0\), and \(u^{-3/4}\) when \(\alpha=0\)) and near \(u=1\) (power \((1-u)^{-1/2}\)); all changes of variable are justified.

**3. Endpoint limits.** At \(\alpha\to\infty\), rescale \(z=\alpha^{-1/3}w\). By dominated convergence of the regularized turning-point integral,
\[
P(\alpha,d)\sim C_3\alpha^{-1/3},\qquad
C_3=\sqrt2\,3^{1/3}\int_0^1\frac{dw}{\sqrt{1-w^3}}.
\]
At \(\alpha\downarrow0\), the same root-rescaled integral gives \(P(\alpha,d)\to C_4d^{-1/4}\). Substitution into the exact side-time formulas yields the two limits in the finding and the small-energy exponent \(1/12\).

**4. Sharp high-energy expansion.** The root \(r=r(\alpha,d)\) is smooth for small nonnegative \(\alpha\). Put \(q=\alpha r^3/3\) and
\[
I(q)=\int_0^1[1-qs^3-(1-q)s^4]^{-1/2}\,ds.
\]
Then \(P(\alpha,d)=\sqrt2rI(q)\). The factorization
\[
1-qs^3-(1-q)s^4=(1-s)[q(1+s+s^2)+(1-q)(1+s+s^2+s^3)]
\]
justifies twice differentiating the integral near \(q=0\). With \(r_0=(4/d)^{1/4}\), we have \(r'(0)=-1/(3d)\), \(q'(0)=r_0^3/3\), and
\[
I'(0)=\frac12\int_0^1\frac{s^3(1-s)}{(1-s^4)^{3/2}}\,ds
=\frac14(I(0)-1).
\]
The last equality follows by integrating \((1-s)\,d(1-s^4)^{-1/2}\) by parts. Therefore
\[
P'(0,d)=\sqrt2\bigl[r'(0)I(0)+r_0q'(0)I'(0)\bigr]
=-\frac{\sqrt2}{3d},
\]
and
\[
P(\alpha,d)=C_4d^{-1/4}-\frac{\sqrt2}{3d}\alpha+O(\alpha^2).
\]
Inserting \(\alpha=cE^{-1/4}\) into \(F\) and expanding the quotient proves the stated high-energy correction.

**5. Unique exchange and the sharp contrast law.** The increasing function \(F\) begins at zero and tends to \(d_+^{1/4}/(d_+^{1/4}+d_-^{1/4})\). It crosses \(1/2\) exactly once precisely when \(d_+>d_-\). Equivalently, the unique \(\alpha_*>0\) solves
\[
P(\alpha_*,d_-)=C_4d_+^{-1/4},\qquad E_*=(c/\alpha_*)^4.
\]
As \(d_+=d_-+\Delta\) with \(\Delta\downarrow0\), the equation and the expansion from Step 4 imply
\[
\alpha_* = \frac{3C_4}{4\sqrt2}d_-^{-1/4}\Delta+O(\Delta^2).
\]
Taking its negative fourth power gives the stated exact scaled limit.

## Verification

The standalone standard-library script `verify/check.py` evaluates the **exact** regularized time quadrature by composite Simpson integration. It checks monotone sample values, the predicted crossing for \(c=d_-=1\), \(d_+=4\), the sign alternatives, the derivative at zero, and the small-contrast fourth-power constant. Running `python verify/check.py` prints `CHECK_OK` if these finite diagnostics agree. The scientific conclusions, including uniqueness, rely on the preceding analytic inequalities and asymptotics, not on sampled energies.

For the illustrative tuple \(c=d_-=1\), \(d_+=4\), the unique crossing is
\[
E_*=0.01637080865477\ldots.
\]

## Relationship to prior work

Chen, Li, and Yu (arXiv:2308.15102v1, Theorem 1.2, case \(G_1\)) classify this Hamiltonian switching family as a global nilpotent center. Their center classification and the existence of its periodic ovals are **not** new claims here. The contribution is the **global physical-time side-occupation law**, its complete unique-crossing criterion, and the critical fourth-power divergence of the crossing energy as the quartic coefficient contrast vanishes.

Research on switching-system period constants, including Yang, Liu, and Lu (2024), addresses local critical periods for a different quartic switching vector field. General energy-period monotonicity criteria concern the sum of excursion times; they do not by themselves give the sign or uniqueness of an exchange between the two side-times of the present mixed cubic–quartic potential. Equivalence with an uninspected prior formulation of the side-occupation problem cannot be ruled out.

## Limitations

The theorem is exact for \(c,d_+,d_->0\) only. It does not assert that all switching nilpotent centers have monotone residence fractions. The formulas concern the fraction of **physical time**, not uniform arclength or a transformed clock. The \(O(\alpha^2)\) and \(O(E^{-1/2})\) bounds are for fixed positive parameters, and the contrast limit holds with \(c,d_-\) fixed. The numerical checker is illustrative and not an exhaustive or machine-certified proof. Publication priority outside the inspected literature is not established.

## References

1. T. Chen, F. Li, and P. Yu, *Nilpotent center conditions in cubic switching polynomial Liénard systems by higher-order analysis*, arXiv:2308.15102v1 (first posted 2023-08-29), Theorems 1.1–1.2 and Sections 3–4. https://arxiv.org/html/2308.15102v1
2. J. Yang, J. Liu, and J. Lu, *Limit Cycles and Local Bifurcation of Critical Periods in a Class of Switching \(Z_2\) Equivariant Quartic System*, *Discrete Dynamics in Nature and Society* (2024), article 4786384. https://doi.org/10.1155/2024/4786384
3. A. R. Chouikha, *The Period Function of Second Order Differential Equations*, arXiv:math/0103180 (2001), background on total-period monotonicity. https://arxiv.org/abs/math/0103180
