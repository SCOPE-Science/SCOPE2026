# Branching-sensitive endpoint analyticity on Kirchhoff metric stars

## Finding
For every integer \(m\ge 2\), let \(\Gamma_m\) consist of \(m\) copies of \([0,\infty)\) glued at their origins, equipped with edgewise Lebesgue measure. Let \(\Delta_m\) be the second derivative on each open ray with continuous vertex values and the Kirchhoff condition that the sum of outgoing derivatives is zero. Write \(T_m(t)=e^{t\Delta_m}\). Define the sharp endpoint derivative constant
\[
 C_m=\sup_{t>0}t\|\partial_tT_m(t)\|_{L^\infty(\Gamma_m)\to L^\infty(\Gamma_m)}.
\]
The same constant is obtained on \(L^1(\Gamma_m)\). In fact, the expression inside the supremum equals \(C_m\) for **every** \(t>0\).

Put
\[
 q(z)=\frac{z^2-2}{8\sqrt\pi}e^{-z^2/4},\quad
 F_m(x)=\int_0^\infty\left(\left|q(x-y)-\left(1-\frac2m\right)q(x+y)\right|+\left(2-\frac2m\right)|q(x+y)|\right)\,dy.
\]
Then \(C_m=\max_{x\ge0}F_m(x)\), which is an exact one-dimensional variational formula. For \(m=2\), \(F_2\) is constant and
\[
 C_2=\sqrt{\frac2\pi}e^{-1/2}.
\]
For every \(m>2\), its maximum occurs at some finite, strictly positive \(x\). The sharp constants obey
\[
 C_2<C_3<C_4<\cdots<C_\infty,\qquad 0<C_\infty-C_m\le \frac{2C_2}{m},
\]
where \(C_\infty=\max_{x\ge0}F_\infty(x)\) and
\[
 F_\infty(x)=\int_0^\infty\left(|q(x-y)-q(x+y)|+2|q(x+y)|\right)\,dy.
\]
An explicit certified lower bound follows by evaluating at \(x=\sqrt2\):
\[
 C_m\ge C_2+2\left(1-\frac2m\right)J,\qquad
 J=\frac{\sqrt2}{4\sqrt\pi}\left(e^{-1/2}-3e^{-9/2}\right)>0.
\]
The reciprocal-branching correction is **sharp to first order**. Let \(X=\operatorname*{argmax}_{x\ge0}F_\infty(x)\), a nonempty compact subset of \((0,\infty)\). Define
\[
 D(x)=4\int_0^\infty |q(x+y)|\,\mathbf1_{\{q(x+y)[q(x-y)-q(x+y)]<0\}}\,dy,
 \qquad \kappa=\min_{x\in X}D(x).
\]
Then \(0<\kappa<\infty\) and
\[
 \boxed{C_m=C_\infty-\frac{\kappa}{m}+o(m^{-1})\quad(m\to\infty).}
\]
Exploratory quadrature suggests \(C_\infty\approx0.7153312\) and \(\kappa\approx0.46536\); these decimals are not claimed as rigorous enclosures. The variational formulas, monotonicity, positivity of \(\kappa\), and asymptotic limit are proved independently of the numerics.

## Assumptions and scope
There are at least two rays, all of infinite length, a common unweighted Kirchhoff vertex, and no potentials or Robin terms. All \(L^p\) norms use unweighted edgewise length measure. The generator is normalized as \(\partial_x^2\), so the line heat kernel is \((4\pi t)^{-1/2}e^{-z^2/(4t)}\). Norms are for complex or real-valued functions. No uniqueness of the maximizing spatial coordinate is assumed or asserted.

## Proof
**1. Exact heat kernel and endpoint norm.** On rays indexed by \(i,j\), the standard Kirchhoff heat kernel is
\[
 K_{ij}(t;x,y)=\delta_{ij}g_t(x-y)+\left(\frac2m-\delta_{ij}\right)g_t(x+y),
 \qquad g_t(z)=(4\pi t)^{-1/2}e^{-z^2/(4t)}.
\]
This follows directly by decomposing the edge index space into the common symmetric mode (Neumann reflection) and its orthogonal complement (Dirichlet reflection); it also specializes the published metric-graph heat-kernel representation. Since \(K\) is symmetric in source and target, the \(L^1\) and \(L^\infty\) operator norms of its time derivative are both the essential supremum of an absolute row integral. Differentiation of \(g_t\) gives \(t\partial_tg_t(z)=t^{-1/2}q(z/\sqrt t)\). At a source position \(\sqrt t\,x\), integration over target positions \(\sqrt t\,y\) cancels this factor. Summing one diagonal and \(m-1\) off-diagonal rays produces \(F_m(x)\), with no dependence on \(t\). The Gaussian derivative is integrable and yields bounded operators for each positive \(t\).

**2. Baseline and existence.** The derivative \(q\) is negative on \((-\sqrt2,\sqrt2)\), positive outside, even, and has integral zero. Since \(q(z)=-\tfrac12(zg_1(z))'\), direct integration yields \(\int_\mathbb R|q(z)|dz=\sqrt{2/\pi}e^{-1/2}\). For \(m=2\) the two ray integrals partition the full line and give this constant. For any fixed finite \(m\), as \(x\downarrow0\) or \(x\to\infty\), \(F_m(x)\to C_2\); the same holds for \(F_\infty\). Continuity follows by translation continuity in \(L^1\). Hence any strict excess over \(C_2\) forces an interior global maximum.

**3. Strict branching monotonicity.** Set \(\alpha_m=1-2/m\). For real \(a,b\),
\[
 \Psi_\alpha(a,b)=|a-\alpha b|+(1+\alpha)|b|
\]
is nondecreasing in \(\alpha\in[0,1]\) by the reverse triangle inequality. If \(ab<0\), it increases *strictly*, with \(\Psi_\beta-\Psi_\alpha=2(\beta-\alpha)|b|\). For any \(x>0\), the interval
\[
 |x-\sqrt2|<y<x+\sqrt2
\]
has \(q(x-y)<0<q(x+y)\). Thus \(F_n(x)>F_m(x)\) whenever \(n>m\ge2\). In particular \(F_3(x)>C_2\) for \(x>0\). The explicit lower bound in the finding comes from evaluating the positive \(q(x+y)\) integral on \(0<y<2\sqrt2\) at \(x=\sqrt2\): \(\int_{\sqrt2}^{3\sqrt2}q(z)\,dz=J\). Every maximizing point of \(F_m\), for \(m>2\), lies in \((0,\infty)\); evaluating the next-degree function at that point proves \(C_{m+1}>C_m\). The limiting function has the same strict excess and an interior maximum.

**4. Uniform limit and rate upper bound.** With \(r=2/m\), the triangle inequality gives pointwise
\[
 0\le\Psi_1(a,b)-\Psi_{1-r}(a,b)\le 2r|b|.
\]
Therefore \(0\le F_\infty(x)-F_m(x)\le(4/m)\int_0^\infty|q(x+y)|dy\le2C_2/m\), uniformly in \(x\ge0\). Maximizing yields \(0<C_\infty-C_m\le2C_2/m\) and convergence of the constants.

**5. Sharp first-order correction.** Define \(D_m(x)=m(F_\infty(x)-F_m(x))\). At any \(x>0\) and almost every \(y>0\), the difference \(q(x-y)-q(x+y)\) is nonzero: it is a nontrivial real-analytic function of \(y\). If it vanished identically, evenness would give \(q(z+2x)=q(z)\) for all sufficiently large \(z\), contradicting Gaussian decay and nonzero \(q\). Expanding the absolute value pointwise gives
\[
 D_m(x)\longrightarrow D(x),\qquad 0\le D_m(x)\le4\int_0^\infty|q(x+y)|dy.
\]
The same convergence holds along **any** sequences \(m_j\to\infty\), \(x_j\to x>0\): the individual integrands converge except on a null set, and a Gaussian majorant permits dominated convergence. Consequently \(D\) is continuous on \((0,\infty)\).

Let \(x_m\) maximize \(F_m\). Since \(C_m\ge C_3>C_2\) for \(m\ge3\), and \(F_m\le F_\infty\), every \(x_m\) lies in the same compact subset \(\{x:F_\infty(x)\ge C_3\}\subset(0,\infty)\). Uniform convergence implies that every accumulation point lies in \(X\). For any \(x\in X\),
\[
 m(C_\infty-C_m)\le D_m(x),
\]
whereas for a maximizer \(x_m\),
\[
 m(C_\infty-C_m)\ge D_m(x_m).
\]
Take subsequences and use the moving-point dominated convergence; the upper and lower bounds identify the limit as \(\min_{x\in X}D(x)=\kappa\). Finally, the sign-opposite interval from Step 3 is contained in the integration domain defining \(D(x)\), and its integral is strictly positive for every \(x>0\). Compactness of \(X\) and continuity of \(D\) give \(\kappa>0\).

## Verification
Run `python3 verify_star.py` from a directory containing the standalone companion code. The standard-library checker evaluates derivative-kernel row integrals at multiple degrees, positions and times, compares heat scaling, verifies finite monotonicity, and checks exploratory approximations to the two limiting constants. It produced 71 passed finite assertions. This is numerical corroboration; the sign, compactness and dominated-convergence steps above establish all universal statements.

## Relationship to prior work
Kostrykin, Potthoff and Schrader give the general metric-graph heat-kernel expansion and Kirchhoff scattering coefficients; their star-kernel specialization is **known** and is not the contribution claimed here. Frank and Kovařík analyze geometry-dependent metric-tree heat-kernel estimates and spectral applications, also without this sharp endpoint time-derivative invariant. The new contribution is the **strict degree ordering of the globally optimized endpoint constants and its positive, exactly characterized reciprocal-degree correction**, rather than the Gaussian kernel formula itself. In the primary texts inspected, neither a degree-monotonicity theorem nor the optimized first-order coefficient is established.

## Limitations
The numerical decimals are not certified bounds. The result is for infinite equal-ray Kirchhoff stars, not finite stars, nonuniform edge weights, graph potentials, Robin couplings, or general trees. No uniqueness theorem for the maximizing spatial point is asserted, and historical priority remains open to further primary-literature verification. A differently named prior theorem concerning time-derivative total variation on star graphs may still exist.

## References
1. V. Kostrykin, J. Potthoff and R. Schrader, *Heat kernels on metric graphs and a trace formula*, arXiv:math-ph/0701009v1 (public 2007-01-04), especially Corollary 3.4 and the standard-boundary discussion following it. https://arxiv.org/abs/math-ph/0701009
2. R. L. Frank and H. Kovařík, *Heat kernels of metric trees and applications*, arXiv:1108.6145v1 (public 2011-08-31), SIAM J. Math. Anal. 45 (2013), 1027–1046. https://arxiv.org/abs/1108.6145
3. M. Hieber, *Gaussian Estimates and Holomorphy of Semigroups on \(L^p\) Spaces*, J. London Math. Soc. 54 (1996), 148–160, DOI:10.1112/jlms/54.1.148 (bibliographic context only).
