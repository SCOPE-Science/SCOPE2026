# A two-orbit Gaussian angular law and half-normal widths for star cosmological polytopes

## Finding
Let \(m\ge1\) and let \(P_m\) be the **standard-coordinate cosmological polytope** of the star graph \(K_{1,m}\), with hub \(0\), leaves \(1,\ldots,m\), and edge coordinates \(y_1,\ldots,y_m\). Its vertices are the \(3m\) vectors
\[
 p_{i,-}=e_{x_0}+e_{x_i}-e_{y_i},\qquad
 p_{i,+}=e_{x_0}-e_{x_i}+e_{y_i},\qquad
 p_{i,0}=-e_{x_0}+e_{x_i}+e_{y_i}
 \quad (1\le i\le m).
\]
They lie in the affine hyperplane with coordinate sum one; the intrinsic translation space has dimension \(2m\). All Euclidean statements use these original orthonormal coordinates, not a nonorthogonal lattice realization.

Let \(Z,X_1,\ldots,X_m,Y_1,\ldots,Y_m\) be independent standard normal variables, and put
\[
 M_m=\max_{1\le i\le m}|X_i|,\quad
 N_m=\max_{1\le i\le m}Y_i,\quad
 q_m=\mathbb E\,\Phi\!\left(\frac{M_m-N_m}{\sqrt2}\right),
\]
where \(\Phi\) is the standard normal distribution function. The following constitutes one Gaussian geometric law for this polytope family.

**Exact support and angular probabilities.** For a standard Gaussian vector \(G\) in the original \((2m+1)\)-dimensional coordinates, the ambient support function has the exact distributional representation
\[
 h_{P_m}(G)\ \stackrel d=\
 \max\{Z+\sqrt2 M_m,-Z+\sqrt2 N_m\}
 =\frac{M_m+N_m}{\sqrt2}
 +\left|Z+\frac{M_m-N_m}{\sqrt2}\right|.
\tag{1}
\]
In particular, for every real \(t\), writing \(\varphi\) for the standard normal density,
\[
 \Pr\{h_{P_m}(G)\le t\}
 =\int_{-\infty}^{t}\!\varphi(z)
 \left[2\Phi\!\left(\frac{t-z}{\sqrt2}\right)-1\right]^m
 \Phi\!\left(\frac{t+z}{\sqrt2}\right)^m dz.
\tag{2}
\]
A uniformly random intrinsic Euclidean direction exposes an individual vertex of type \(p_{i,-}\) or \(p_{i,+}\) with probability \(q_m/(2m)\), and an individual vertex \(p_{i,0}\) with probability \((1-q_m)/m\). Thus for every integer \(t\ge2\), the probability that \(t\) independent random directions expose the same vertex is
\[
 \boxed{C_t(m)=m^{1-t}\left(2^{1-t}q_m^t+(1-q_m)^t\right).}
\tag{3}
\]
All tie events have probability zero. The normal cones here are intrinsic normal cones in the \(2m\)-dimensional affine translation space.

**Limiting angular law.** As \(m\to\infty\),
\[
 q_m\longrightarrow\frac12,\qquad
 \boxed{m^{t-1}C_t(m)\longrightarrow 2^{1-2t}+2^{-t}}
 \quad\text{for each fixed integer }t\ge2.
\tag{4}
\]
In particular, \(mC_2(m)\to3/8\). Although there are \(3m\) vertices, their Gaussian angular distribution is asymptotically nonuniform: each of the \(2m\) first-type vertices has probability asymptotic to \(1/(4m)\), whereas each of the \(m\) second-type vertices has probability asymptotic to \(1/(2m)\). Hence the two-direction collision probability is asymptotically \(9/8\) times that of a uniform law on the same \(3m\) vertices.

**Half-normal intrinsic width law.** Let \(U_m\) be uniform on the unit sphere in the \(2m\)-dimensional translation space of \(P_m\), and write \(W_m(U_m)=h_{P_m}(U_m)+h_{P_m}(-U_m)\) for its Euclidean directional width. Then
\[
 \boxed{\sqrt{2m}\,W_m(U_m)-4\sqrt{\log m}
 \ \xrightarrow[m\to\infty]{L^2\ \mathrm{under\ a\ Gaussian\ coupling}}\ 2|Z|.}
\tag{5}
\]
The coupling and moment interpretation are specified in the proof. In particular this implies convergence in distribution and of the first two centered moments, giving
\[
 \boxed{\mathbb E W_m(U_m)
 =\frac{4\sqrt{\log m}+2\sqrt{2/\pi}+o(1)}{\sqrt{2m}},}
\tag{6}
\]
\[
 \boxed{\operatorname{Var}(\sqrt{2m}\,W_m(U_m))
 \longrightarrow4\left(1-\frac2\pi\right).}
\tag{7}
\]
The residual width fluctuation is half-normal, not Gumbel, because all edge triples share one hub coordinate.

## Assumptions and scope
The star has \(m\ge1\) unweighted edges and no isolated vertices. The original cosmological-polytope definition uses the displayed \(3m\) edge-triple vectors; adding coordinate unit vectors for graph vertices does not change their convex hull. Its translation space is
\[
 H_m=\left\{u\in\mathbb R^{2m+1}:\sum_j u_j=0\right\}.
\]
All distances and widths use the ordinary ambient Euclidean inner product restricted to \(H_m\). A standard Gaussian direction projected orthogonally to \(H_m\) is radially isotropic there. Gaussian support in (1)--(2) is intentionally measured in the full canonical coordinates; it depends on the choice of origin, unlike intrinsic widths and normal-cone probabilities.

## Proof
**1. Orthogonal separation of leaf directions.** Write a standard Gaussian vector in source coordinates as \(G=(Z,B_1,\ldots,B_m,D_1,\ldots,D_m)\). Set
\[
 X_i=(B_i-D_i)/\sqrt2,\qquad Y_i=(B_i+D_i)/\sqrt2.
\]
For each \(i\), this is an orthogonal transformation of two independent standard normals. Thus all \(X_i,Y_i\) and \(Z\) are independent and standard normal. Maximizing \(\langle G,p\rangle\) over the displayed vertices gives
\[
 \max_i\{Z+B_i-D_i,Z-B_i+D_i,-Z+B_i+D_i\}
 =\max\{Z+\sqrt2 M_m,-Z+\sqrt2 N_m\}.
\]
The identity \(\max(a,b)=(a+b)/2+|a-b|/2\) proves (1). Conditional on \(Z=z\), both maxima in (1) must lie below \(t\). Independence, the cdfs \(\Pr(M_m\le u)=(2\Phi(u)-1)^m\) for \(u\ge0\) and \(\Pr(N_m\le v)=\Phi(v)^m\), and integration over \(z\le t\) prove (2). The integral is valid also for negative \(t\).

**2. Intrinsic normal-cone probabilities.** The first branch of (1) wins precisely when \(Z>(N_m-M_m)/\sqrt2\). Conditioning on \(M_m,N_m\) therefore gives its probability \(q_m\). Conditional on the first branch, the index maximizing \(|X_i|\) and its sign are uniformly distributed over \(2m\) choices and independent of \(M_m\), \(N_m\), and \(Z\). Conditional on the other branch, the index maximizing \(Y_i\) is uniform among \(m\) choices. This proves the individual exposure probabilities. An ambient Gaussian and its projection to \(H_m\) expose the same vertex: their objectives differ by the constant \(\langle G,\mathbf1\rangle/(2m+1)\) on every vertex, since every vertex has coordinate sum one. Independence of random directions proves (3).

**3. Gaussian maxima concentrate at a common level.** For independent standard normals, the elementary Gaussian tail estimates imply
\[
 \max_{i\le m}Y_i-\sqrt{2\log m}\longrightarrow0,
 \qquad\max_{i\le m}|X_i|-\sqrt{2\log m}\longrightarrow0
 \quad\text{in }L^2.
\tag{8}
\]
For completeness, set \(b_m=\sqrt{2\log m}\). The union bound and Gaussian upper tail show that for any fixed \(s>0\), \(\Pr(\max_i|X_i|>b_m+s)\le2m\exp(-(b_m+s)^2/2)\to0\); integrating this bound controls the squared positive overshoot. The Mills lower bound makes \(m\Pr(Y_1>b_m-s)\to\infty\), hence the lower deviation probability tends rapidly to zero; integration of lower tails bounds its squared contribution. For \(\max Y_i\), the rare event that all observations are negative has probability \(2^{-m}\) and negligible second moment. These arguments give both statements in (8) without appealing to finite simulation.

Consequently, \(M_m-N_m\to0\) in \(L^2\), and the bounded continuous function \(\Phi\) in the definition of \(q_m\) gives \(q_m\to1/2\). Substitution in (3) proves (4).

**4. The Gaussian width and its surviving hub fluctuation.** Define \(N_m^-:=\max_i(-Y_i)\). For the same standard Gaussian vector \(G\), negating every coordinate leaves the absolute leaf maximum \(M_m\) unchanged, exchanges \(Z\) with \(-Z\), and replaces \(N_m\) by \(N_m^-\). Hence
\[
 \begin{aligned}
 \mathcal W_m(G)&:=h_{P_m}(G)+h_{P_m}(-G)\\
 &=\max\{Z+\sqrt2M_m,-Z+\sqrt2N_m\}
 +\max\{-Z+\sqrt2M_m,Z+\sqrt2N_m^-\}.
 \end{aligned}
\tag{9}
\]
Both \(N_m\) and \(N_m^-\) satisfy (8), though they need not be independent. Since the maximum of two real numbers is 1-Lipschitz in the maximum norm, (8) and (9) imply
\[
 \mathcal W_m(G)-4\sqrt{\log m}\longrightarrow2|Z|
 \quad\text{in }L^2.
\tag{10}
\]
This is a statement on a common probability space with nested independent Gaussian arrays; ordinary coupling of the finite Gaussian vectors suffices for \(L^2\) convergence.

Let \(\widetilde G\) be the orthogonal projection of \(G\) onto \(H_m\), let \(R_m=\|\widetilde G\|\), and put \(U_m=\widetilde G/R_m\). The variable \(U_m\) is uniform on the sphere of \(H_m\), independent of the \(\chi_{2m}\)-distributed radius \(R_m\). Since width ignores adding a scalar multiple of \(\mathbf1\) to the direction, \(\mathcal W_m(G)=R_m W_m(U_m)\). Moreover, \(R_m/\sqrt{2m}\to1\) with inverse-radius moments sufficient to show
\[
 \bigl(\sqrt{2m}/R_m-1\bigr)\mathcal W_m(G)\longrightarrow0
 \quad\text{in }L^2.
\]
For instance, for \(m\ge3\) the chi-distribution has fourth inverse moments, its normalized inverse-radius error has fourth moment \(O(m^{-2})\), and the Gaussian-maximal formula gives \(\mathbb E\mathcal W_m(G)^4=O((\log m)^2)\). Cauchy--Schwarz completes the bound. Equation (5) follows from (10).

Taking expectations in the exact identity \(\mathcal W_m(G)=R_m W_m(U_m)\) and using independence gives \(\mathbb E\mathcal W_m(G)=\mathbb E\chi_{2m}\cdot\mathbb E W_m(U_m)\). By (10), \(\mathbb E\mathcal W_m(G)=4\sqrt{\log m}+2\sqrt{2/\pi}+o(1)\); the gamma-ratio formula gives \(\mathbb E\chi_{2m}=\sqrt{2}\,\Gamma(m+1/2)/\Gamma(m)=\sqrt{2m}(1+O(m^{-1}))\). This proves (6). The \(L^2\) convergence proves the variance limit (7).

## Verification
The standalone `verify.py` included in this result uses deterministic pseudorandom input vectors to compare direct maxima over all \(3m\) source vertices against (1) and its folded-normal identity, verifies that projected and unprojected Gaussian vectors yield the same intrinsic width, and verifies winning-branch labels. Its tests cover \(1\le m\le20\) with 180 input vectors per size (3,600 exact-to-floating-tolerance support/width checks). Twelve independent one-dimensional numerical integrations of (2) are compared with empirical Gaussian simulations for \(m\in\{1,2,4\}\). The \(m=1\) equilateral-triangle case gives \(q_1=2/3\) and \(C_2(1)=1/3\). The checker also prints non-certifying finite-size diagnostics for (10). All checks completed successfully. The analytic proof, not finite sampling or numerical integration, proves the limiting assertions.

## Relationship to prior work
Arkani-Hamed, Benincasa, and Postnikov introduced the standard cosmological-polytope source vertices. Kühne and Monin's *Faces of Cosmological Polytopes* (first public 2022) gives the graph-dependent face structure, connected-subgraph facet theorem, and a tree face-count recursion. Its primary MSC classification is 52B05, as verified in the first page of the published full text. The source construction, vertex count, and affine dimension are not new assertions.

Published results on **Euclidean inballs of star cosmological polytopes** determine tangent facets and one incenter, and results on **minimum enclosing balls of connected cosmological polytopes** determine a common vertex sphere. Neither assertion determines the Gaussian normal-cone probabilities, all-order collision moments, or directional-width fluctuations: those depend on the distribution of exposed vertices under random linear functionals, not on facet contact distances or enclosing radii. The polytope's uniform-vertex covariance is likewise a second-moment statistic of sampled vertices, not a law of maximizing Gaussian functionals.

The present finding concerns exactly the two-orbit angular distribution and the half-normal width regime. Gaussian extreme-value concentration itself is classical; its particular geometric coupling through the common hub coordinate and resulting non-Gumbel width law are the claimed contributions. Relevant published geometric results and available mathematical research records were compared for equivalent formulations and stronger coverage.

## Limitations
The formulas assume the **star** graph and the **standard orthonormal coordinate realization**. General trees and graphs, edge weights, independent random perturbations of vertices, and projectively equivalent but nonorthogonal realizations are not covered. The ambient support CDF is origin-dependent; only the angular and width conclusions are translation-invariant. The limiting law is asymptotic as \(m\to\infty\) and is not an exact half-normal distribution at finite \(m\). The normal-cone argument uses generic directions; Gaussian ties have probability zero. No independent mathematical audit is claimed. A residual bibliographic risk is an equivalent formulation in earlier physics-oriented or Gaussian-process literature under different terminology.

## References
1. N. Arkani-Hamed, P. Benincasa, and A. Postnikov, *Cosmological Polytopes and the Wavefunction of the Universe*, arXiv:1709.02813, 2017; source construction.
2. L. Kühne and L. Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069v1, first public 2022-09-16; DOI 10.4171/AIHPD/192; vertex definition, face theorem, tree face recursion, and primary MSC2020 52B05. Full text: https://arxiv.org/html/2209.08069v2.
3. M. Juhnke-Kubitzke, L. Solus, and L. Venturello, *Triangulations of cosmological polytopes*, arXiv:2303.05876v1, 2023-03-10; triangulations, toric ideals, and normalized volumes.
4. *Every star cosmological polytope is tangential with an exact unique inball*, publicly accessible mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-every-star-cosmological-polytope-is-tangential-with-an-exact-uni--22da9e5835c2.
5. *Every connected cosmological polytope has graph-independent Euclidean circumradius*, publicly accessible mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-every-connected-cosmological-polytope-has-graph-independent-eucl--099bd090b126.
