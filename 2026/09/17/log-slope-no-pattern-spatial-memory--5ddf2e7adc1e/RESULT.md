# Global logarithmic-slope obstruction to spatial-memory steady patterns

## Result

Consider the no-growth steady problem associated with the spatial-memory system of Salmaniw, Liu, Shi and Wang on a bounded connected smooth domain \(\Omega\):

\[
0=d\Delta U+\alpha\nabla\!\cdot(U\nabla V),\qquad
0=g_1(U)-g_2(U)K,\qquad
0=-R^2\Delta V+V-K,
\]
with homogeneous Neumann conditions \(\partial_n U=\partial_n V=0\), \(d,R>0\), and a positive classical state \(U>0\). Assume \(g_2(u)>0\) for \(u>0\), and write
\[
h(u)=\frac{g_1(u)}{g_2(u)},\qquad \phi(z)=h(e^z).
\]
Let \(\lambda_1>0\) be the first nonzero Neumann eigenvalue of \(-\Delta\) on \(\Omega\).

### Theorem

Every positive steady state obeys the exact relation
\[
d\log U+\alpha V=\text{constant}. \tag{1}
\]
Consequently:

1. **Sign obstruction.** If \(\alpha\phi\) is nondecreasing on \(\mathbb R\), then every positive steady state is spatially constant. If \(h\) is differentiable, a sufficient equivalent pointwise condition is
   \[
   \alpha\,u h'(u)\ge 0\qquad (u>0). \tag{2}
   \]
   Thus the sign-compatible side of the coupling cannot support a nonconstant positive steady state, irrespective of the magnitude of \(\alpha\).

2. **Quantitative no-pattern region.** If \(\phi\) is globally Lipschitz with constant \(L\), then every positive steady state is spatially constant whenever
   \[
   |\alpha|L<d(1+R^2\lambda_1). \tag{3}
   \]
   In particular, when \(h\in C^1(0,\infty)\), one may take
   \[
   L=\sup_{u>0}u|h'(u)|. \tag{4}
   \]

For the original one-dimensional even-periodic problem, Proposition 2.1 of the source paper identifies it with the Neumann problem on \((0,\pi)\), where \(\lambda_1=1\). Hence (3) becomes
\[
|\alpha|\sup_{u>0}u|h'(u)|<d(1+R^2). \tag{5}
\]
This is a global exclusion of all finite-amplitude positive stationary patterns, not merely a local stability or local bifurcation statement.

## Proof

Set
\[
\Psi=d\log U+\alpha V.
\]
The first stationary equation can be rewritten as
\[
\nabla\!\cdot(U\nabla\Psi)=0.
\]
Multiplying by \(\Psi\), integrating over \(\Omega\), and using \(\partial_nU=\partial_nV=0\), hence \(\partial_n\Psi=0\), gives
\[
0=-\int_\Omega U|\nabla\Psi|^2.
\]
Since \(U>0\), \(\Psi\) is constant, proving (1). When \(\alpha=0\), the first equation and the Neumann condition already imply that \(U\) is constant, so suppose below that \(\alpha\ne0\).

The second stationary equation gives \(K=h(U)\). Put
\[
z=\log U,\qquad w=V-\overline V,
\]
where bars denote spatial averages. From (1),
\[
z-\overline z=-\frac{\alpha}{d}w. \tag{6}
\]
Centering the elliptic equation yields
\[
-R^2\Delta w+w=\phi(z)-\overline{\phi(z)}. \tag{7}
\]
Multiplying (7) by \(w\), integrating, and using (6) gives the exact identity
\[
R^2\|\nabla w\|_2^2+\|w\|_2^2
=-\frac d\alpha\int_\Omega
(\phi(z)-\overline{\phi(z)})(z-\overline z). \tag{8}
\]

For any integrable \(z\), the covariance term has the representation
\[
\int_\Omega(\phi(z)-\overline{\phi(z)})(z-\overline z)
=\frac1{2|\Omega|}\int_{\Omega\times\Omega}
(\phi(z(x))-\phi(z(y)))(z(x)-z(y))\,dx\,dy. \tag{9}
\]
If \(\alpha\phi\) is nondecreasing, then the right-hand side of (8) is nonpositive, while the left-hand side is nonnegative. Hence \(w=0\), and (6) gives that \(U\) is constant. This proves the sign obstruction.

If \(\phi\) is \(L\)-Lipschitz, (9) also gives
\[
\left|\int_\Omega(\phi(z)-\overline{\phi(z)})(z-\overline z)\right|
\le L\|z-\overline z\|_2^2. \tag{10}
\]
Using (6) in (10) and the Neumann Poincare inequality
\(\|\nabla w\|_2^2\ge\lambda_1\|w\|_2^2\), identity (8) implies
\[
(1+R^2\lambda_1)\|w\|_2^2
\le \frac{|\alpha|L}{d}\|w\|_2^2. \tag{11}
\]
Under (3), this forces \(w=0\), and then (6) again forces spatial constancy. Finally,
\(\phi'(z)=e^z h'(e^z)\), which gives (4). \(\square\)

## Sharp match to the first local bifurcation for a saturating memory law

Take
\[
g_1(u)=\frac{u}{1+u},\qquad g_2(u)=1,
\]
so \(h(u)=u/(1+u)\). Then
\[
\sup_{u>0}u h'(u)=\sup_{u>0}\frac{u}{(1+u)^2}=\frac14,
\]
with equality at \(u=1\). For conserved mean density \(u_*=1\), the source paper's no-growth critical value
\[
\alpha_1(R)=\frac{(1+R^2)d\,w_{k_*}}{u_*w_{u_*}}
\]
has \(w_{k_*}=-1\) and \(w_{u_*}=1/4\), so
\[
\alpha_1(R)=-4d(1+R^2). \tag{12}
\]
The sign obstruction excludes nonconstant positive steady states for every \(\alpha\ge0\), while (5) excludes them for
\(-4d(1+R^2)<\alpha<0\). Therefore, for this admissible saturating feedback and mean density \(u_*=1\),
\[
\boxed{\alpha>-4d(1+R^2)\quad\Longrightarrow\quad
\text{the constant state is the only positive steady state}.} \tag{13}
\]
Thus the global no-pattern boundary reaches exactly the first local bifurcation threshold from the linearly stable side. In particular, there is no detached or subcritical finite-amplitude positive steady branch anywhere before that threshold.

## Relation to the literature

Salmaniw, Liu, Shi and Wang establish well-posedness, linear stability thresholds, and local steady-state bifurcation for the coupled spatial-memory PDE-ODE system. In the no-growth case they show that the first critical wavenumber is always \(n=1\), with critical strength (9.3), so patterned branches emerging locally from the homogeneous state are single-peaked. Their analysis is local around the bifurcation point. The theorem above instead supplies a global stationary obstruction: it excludes every nonconstant positive steady state in an explicit parameter region, regardless of amplitude.

A 2026 review by Shi surveys nonlocal-advection pattern formation largely through stability and bifurcation mechanisms. Searches of that review, the motivating paper and related spatial-memory literature did not locate the logarithmic-slope criterion (3)-(5) or the sharp saturating-law consequence (13). The contribution is therefore claimed only to the best of our knowledge.

## Limitations

- The result concerns positive classical **steady states**. It does not prove convergence of time-dependent solutions, nonlinear asymptotic stability, or absence of nonstationary attractors.
- The multidimensional statement applies to the displayed local parabolic-ordinary-elliptic stationary system. The exact equivalence with the original nonlocal exponential-kernel model is established in the source paper for the one-dimensional even \(2\pi\)-periodic setting, corresponding to the Neumann interval \((0,\pi)\).
- Strict inequality is required in (3). The argument is inconclusive at equality in general.
- When \(\sup_{u>0}u|h'(u)|=\infty\), the quantitative criterion may be vacuous, although the sign obstruction can still apply.
- Originality is to the best of our knowledge. Broad chemotaxis and aggregation-diffusion literatures contain related steady-state energy methods; no source located in the documented search was found to imply this exact spatial-memory logarithmic-slope theorem.

## References

1. Y. Salmaniw, D. Liu, J. Shi, H. Wang, *Dynamics of a Coupled Nonlocal PDE-ODE System with Spatial Memory: Well-Posedness, Stability, and Bifurcation Analysis*, Journal of Nonlinear Science 36, 19 (2026), DOI: 10.1007/s00332-025-10233-9; arXiv:2503.11550.
2. J. Shi, *Bifurcation and Pattern formation in reaction-diffusion models with nonlocal advection and time delays*, Discrete and Continuous Dynamical Systems 57 (2026), 496-533, DOI: 10.3934/dcds.2026134.
3. H. Wang, Y. Salmaniw, *Open problems in PDE models for knowledge-based animal movement via nonlocal perception and cognitive mapping*, Journal of Mathematical Biology 86, 71 (2023), DOI: 10.1007/s00285-023-01905-9; arXiv:2201.09150.
