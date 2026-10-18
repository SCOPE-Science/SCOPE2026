# Universal attraction and a singular zealot–feedback crossover in competing contagion

## Finding

Consider the autonomous mean-field equation obtained by freezing the reciprocal-complexity feedback in Huang and Prokopenko's competing contagion model [1]. Let \(Z\) be the fraction permanently committed to each of two competing opinions. Let \(u\) be the **total** fraction holding opinion A, including its committed agents. The equation is

\[
\dot u=F_{Z,\rho}(u):=(1-Z-u)u^{1+\rho}-(u-Z)(1-u)^{1-\rho},
\qquad Z\leq u\leq1-Z.
\]

**Theorem (global equilibrium selection and the singular small-commitment frontier).** For every \(0<Z<1/2\) and \(-1<\rho<1\), the displayed equation has exactly one equilibrium \(u_*(Z,\rho)\) in \((Z,1-Z)\). Every solution starting in \([Z,1-Z]\) converges to this equilibrium; the equilibrium is hyperbolic and its approach is eventually exponential. For \(\rho>0\), \(Z<u_*(Z,\rho)<1/2\); for \(\rho<0\), \(1/2<u_*(Z,\rho)<1-Z\), and

\[
u_*(Z,-\rho)=1-u_*(Z,\rho),\qquad
\partial_{\rho}u_*(Z,\rho)<0.
\]

At \(\rho=0\) the equilibrium is exactly \(1/2\), and its sensitivity is

\[
\left.\partial_{\rho}u_*(Z,\rho)\right|_{\rho=0}
=-\frac{(1-2Z)\log4}{8Z}.
\]

Let \(Z_n\downarrow0\) and \(\rho_n/Z_n\to c\in\mathbb R\), with \(|\rho_n|<1\). Then

\[
\lim_{n\to\infty}u_*(Z_n,\rho_n)=U(c).
\]

Here \(U(0)=1/2\), \(U(-c)=1-U(c)\), and for \(c>0\), \(U(c)\) is the unique point in \((0,1/2)\) satisfying

\[
c=\frac{1-2U(c)}{U(c)(1-U(c))[-\log(U(c)(1-U(c)))]}.
\]

In particular, \(U\) is continuous and strictly decreasing, with \(U(c)=1/2-(\log4)c/8+O(c^2)\) near zero. In the distinct limit where \(\rho\in(0,1)\) is held fixed and \(Z\downarrow0\), the flexible-A equilibrium fraction has the sharp power law

\[
u_*(Z,\rho)-Z\sim Z^{1+\rho}.
\]

For fixed negative \(\rho\), the reflected flexible-B minority obeys \(1-Z-u_*(Z,\rho)\sim Z^{1+|\rho|}\).

The combination reveals a non-uniform zero-commitment limit. An asymmetry as small as \(\rho=cZ\) is sufficient to shift the equilibrium total opinion by a nonzero amount independent of \(Z\). In contrast, every fixed positive asymmetry selects a near-boundary state as the committed fractions vanish.

## Assumptions and scope

Two opinions A and B are mutually exclusive. A fraction \(Z\) of the entire population is permanently committed to A, and another fraction \(Z\) permanently committed to B, with \(0<Z<1/2\). The fraction of flexible A holders is \(u-Z\). Adoption exponents are \(1+\rho\) for B-to-A and \(1-\rho\) for A-to-B, with \(-1<\rho<1\) fixed in time. This includes the source model's feedback range \([-0.9,0.9]\). The theorem concerns a deterministic, well-mixed, infinite-population mean-field equation, not a time-dependent feedback signal or a finite stochastic network. Initial states may include the endpoints of the admissible interval.

## Proof

**1. Physical invariance and the neutral case.** At \(u=Z\), the vector field is \((1-2Z)Z^{1+\rho}>0\). At \(u=1-Z\), it is \(-(1-2Z)Z^{1-\rho}<0\). Hence the closed interval is positively invariant and its boundary is not stationary. At \(\rho=0\), direct cancellation gives \(F_{Z,0}(u)=Z(1-2u)\), so \(u_*=1/2\) is its sole equilibrium, with derivative \(-2Z<0\).

**2. Exact monotone equilibrium parametrization.** The stationary condition with positive factors can be written as

\[
A_Z(u)=\rho B(u),\qquad
A_Z(u)=\log\frac{u}{u-Z}-\log\frac{1-u}{1-u-Z},\qquad
B(u)=-\log[u(1-u)]>0.
\]

For \(\rho>0\), the left side must be positive, forcing \(u<1/2\). If \(Z<u<1/2\), differentiation of logarithms yields the **exact integral representation**

\[
A_Z(u)=(1-2u)I_Z(u),\qquad
I_Z(u)=\int_0^Z\frac{dt}{(u-t)(1-u-t)}.
\]

Set \(D_t(u)=(u-t)(1-u-t)\) and \(J_Z(u)=\int_0^Z D_t(u)^{-2}\,dt\). On this interval, \(D_t(u)>0\), \(D_t(u)\leq u(1-u)\), and

\[
-\frac{A'_Z(u)}{A_Z(u)}=\frac2{1-2u}+(1-2u)\frac{J_Z(u)}{I_Z(u)}
\geq\frac2{1-2u}+\frac{1-2u}{u(1-u)},
\]

whereas

\[
-\frac{B'(u)}{B(u)}
=\frac{1-2u}{u(1-u)B(u)}
<\frac{1-2u}{u(1-u)},
\]

because \(B(u)\geq\log4>1\). Consequently \(R_Z(u):=A_Z(u)/B(u)\) is strictly decreasing on \((Z,1/2)\). Moreover, \(R_Z(u)\to+\infty\) as \(u\downarrow Z\), and \(R_Z(u)\to0\) as \(u\uparrow1/2\). Thus each \(\rho>0\) admits one and only one equilibrium, given by \(R_Z(u_*)=\rho\). Strict decrease also gives \(\partial_{\rho}u_*<0\). The substitution \((u,\rho)\mapsto(1-u,-\rho)\) reverses the vector field sign, proving both the negative-\(\rho\) and reflection assertions.

**3. Global attraction and smooth response.** For \(\rho>0\), the logarithm of the ratio of the positive forward and reverse fluxes is \(A_Z(u)-\rho B(u)=B(u)(R_Z(u)-\rho)\). It is positive below its unique root and negative from that root to \(1/2\) because \(R_Z\) decreases; for \(u>1/2\), the same expression is negative because \(A_Z(u)<0\) and \(B(u)>0\). Thus the flow points toward the root throughout the invariant interval. At the root, the derivative of that log ratio is \(B(u_*)R'_Z(u_*)<0\), which implies \(F'_{Z,\rho}(u_*)<0\). Reflection handles \(\rho<0\); the neutral case was explicit. Every orbit converges monotonically and is eventually exponentially close to its hyperbolic equilibrium. The implicit function theorem gives a smooth, locally analytic equilibrium branch in \(\rho\). At \(u=1/2\), logarithmic differentiation of the stationarity equation yields

\[
\left.\partial_\rho u_*\right|_{\rho=0}=-\frac{(1-2Z)\log4}{8Z}.
\]

**4. Universal double scaling.** Uniformly on each compact subset of \((0,1/2)\), the integral formula gives

\[
\frac{R_Z(u)}{Z}\longrightarrow C(u):=\frac{1-2u}{u(1-u)[-\log(u(1-u))]}.
\]

The function \(C\) is continuous and strictly decreasing from \(+\infty\) to zero. Indeed

\[
\frac{C'(u)}{C(u)}=-\frac2{1-2u}
-\frac{1-2u}{u(1-u)}\left(1-\frac1{-\log(u(1-u))}\right)<0.
\]

For any \(c>0\), choose two interior comparison points straddling the unique solution \(C(U)=c\). Uniform convergence and monotonicity squeeze the finite-\(Z\) root between them whenever \(\rho/Z\to c\). For \(c=0\), compare with arbitrarily small positive/negative scaled feedbacks; reflection handles \(c<0\). This proves the universal limit, symmetry, and continuity. The expansion \(C(1/2-h)=8h/\log4+O(h^2)\) proves the stated small-\(c\) response.

**5. Fixed-bias minority boundary layer.** Fix \(0<\rho<1\), and write \(x_*=u_*-Z\). As \(Z\downarrow0\), the root satisfies \(u_*<1/2\). Any positive subsequential limit in \((0,1/2]\) would solve the zealot-free equilibrium equation \([u(1-u)]^\rho=1\), impossible since \(u(1-u)\leq1/4\); hence \(u_*\to0\). The stationary relation now reads

\[
x_*=(1-2Z-x_*)\frac{(x_*+Z)^{1+\rho}}{(1-Z-x_*)^{1-\rho}}.
\]

Because \(x_*\to0\) and \(1+\rho>1\), the right side divided by \(x_*\) would converge to zero along any subsequence with \(x_*/Z\) bounded below by a positive constant: in that case \(x_*+Z\leq Kx_*\) for a fixed \(K\), yielding \(1\leq O(x_*^\rho)\), a contradiction. Therefore \(x_*/Z\to0\), and division by \(Z^{1+\rho}\) gives \(x_*/Z^{1+\rho}\to1\). Reflection proves the negative-bias assertion. This completes the proof.

## Verification

The standalone Python 3 program `check.py` uses only the standard library. Run `python3 check.py` to check finite-grid equilibrium roots directly against the original equation, reflection symmetry, flow orientation, the exact neutral sensitivity, the fixed-bias fractional-power profile, and numerical approximations to the universal crossover. For example, at \(Z=0.225\), \(\rho=0.6\) the equilibrium total-A fraction is approximately \(0.306881540819791\), while \(U(1)\approx0.332915461747212\). These are corroboration only: the parameter-uniform claims and asymptotic limits follow from the preceding analysis, not finite tests.

## Relationship to prior work

Huang and Prokopenko [1, equations (18)–(27), Figure 2] introduce the underlying reciprocal-complexity dynamics, the two equal committed fractions, and the stationary transcendental equation, and plot numerical equilibria for \(Z=0.225\). The model and its stationary equation are not new here. The new mathematical assertion is **global uniqueness and attraction throughout the positive-commitment parameter domain, together with the sharp \(\rho/Z\) equilibrium crossover and fixed-bias minority scaling**; a finite numerical curve does not imply these uniform conclusions.

Vasconcelos, Levin, and Pinheiro [2] derive the competing nonlinear contagion framework without committed agents and analyze consensus/polarization regimes. Their zealot-free model does not determine the singular restoration of an interior equilibrium under simultaneously vanishing positive commitment and bias. Mobilia [3] analyzes a zealot-containing nonlinear \(q\)-voter model with equal superlinear adoption exponents \(q>1\) and identifies zealotry-driven bistability. That model does not subsume the present reciprocal exponents \(1+\rho\) and \(1-\rho\), one of which is sublinear whenever \(\rho\ne0\); thus its bistability and thresholds do not imply the present theorem. The logical overlap is a shared mean-field/zealot setting, not coverage of the same parameterized vector field.

## Limitations

The theorem is for the autonomous frozen-feedback deterministic mean-field equation. It makes no stability claim for time-varying \(\rho(t)\), coupled crisis dynamics, spatially structured networks, or finite-population stationary distributions. The asymptotic assertion presumes equal positive committed fractions and reciprocal adoption exponents that straddle one. The universality is within this precisely defined class, not across arbitrary competing-contagion models. Although relevant primary sources and mathematical records were examined, independent verification of publication priority is still appropriate.

## References

[1] J. Huang and M. Prokopenko, *Modelling opinion dynamics during crises as complex contagion with feedback* (2026), arXiv:2609.18684v1, publicly available 2026-09-16. https://arxiv.org/abs/2609.18684

[2] V. V. Vasconcelos, S. A. Levin, and F. L. Pinheiro, *Consensus and Polarisation in Competing Complex Contagion Processes* (2018 preprint / 2019 journal), arXiv:1811.08525. https://arxiv.org/abs/1811.08525

[3] M. Mobilia, *Nonlinear q-voter model with inflexible zealots* (2015), arXiv:1506.04911. https://arxiv.org/abs/1506.04911
