# Gaussian normal-cone angles and a third-order width transition for partial permutohedra

## Finding
For positive integers \(m,n\), consider the standard Euclidean partial permutohedron
\[
\mathcal P(m,n)=\operatorname{conv}\{x\in\{0,1,\ldots,n\}^{m}:\text{the positive coordinates of }x\text{ are distinct}\}\subset\mathbb R^m.
\]
Write \(V_s\) for its vertex orbit consisting of the permutations of \((n,n-1,\ldots,n-s+1,0,\ldots,0)\), with \(0\le s\le\min(m,n)\). Define the normalized external solid angle of the normal cone at a vertex \(v\) by
\[
\alpha(v)=\Pr\{v\text{ uniquely maximizes }\langle G,x\rangle\text{ over }x\in\mathcal P(m,n)\},\qquad G\sim N(0,I_m).
\]
**Exact angular census.** Every \(v\in V_s\) has
\[
\boxed{\alpha(v)=\begin{cases}
\displaystyle\frac{1}{2^m s!},&s<n,\\[5pt]
\displaystyle\frac{\Pr\{\operatorname{Bin}(m,1/2)\ge n\}}{m!/(m-n)!},&s=n\le m.
\end{cases}}
\]
Each orbit has \(|V_s|=m!/(m-s)!\) vertices. In particular, the total spherical normal-cone angle of \(V_s\) is \(2^{-m}\binom ms\) for \(s<n\), and is the binomial upper tail when \(s=n\le m\). This treats all vertices, including the origin, for every \(m,n\ge1\).

**Exact mean width.** Put \(q(t)=1-\Phi(t)\), \(r_s=\min(s,n)\), and \(R_m=\sqrt2\,\Gamma((m+1)/2)/\Gamma(m/2)\). Then the ordinary Euclidean mean width is
\[
\boxed{w(\mathcal P(m,n))=\frac2{R_m}\int_0^\infty
\sum_{s=0}^{m}\binom ms q(t)^s(1-q(t))^{m-s}\,
\frac{r_s(2n-r_s+1)}2\,dt.}
\]
The convention is \(w(K)=\mathbb E_{U\in S^{m-1}}[h_K(U)+h_K(-U)]\).

**Sharp aspect-ratio transition.** Let \(m\to\infty\) through positive integers and let \(n=n_m\) satisfy \(n_m/m\to\rho\in(0,\infty)\). Then
\[
\boxed{\frac{w(\mathcal P(m,n_m))}{m^{3/2}}\longrightarrow W(\rho)
=\begin{cases}
\displaystyle\frac{\operatorname{erfc}(\Phi^{-1}(1-\rho))}{2\sqrt\pi},&0<\rho\le\frac12,\\[6pt]
\displaystyle\frac1{2\sqrt\pi}+\sqrt{\frac2\pi}\left(\rho-\frac12\right),&\rho\ge\frac12.
\end{cases}}
\]
The limiting profile is strictly increasing and twice continuously differentiable throughout \((0,\infty)\), but is **not three times differentiable** at \(\rho=1/2\): the one-sided third derivatives there are \(-2\sqrt{2\pi}\) and \(0\), respectively. Thus the competition between the rank cap and positive Gaussian coordinates produces a third-order geometric transition.

**Critical normal-cone window.** If \(n_m=m/2+\tau\sqrt m+o(\sqrt m)\) for a fixed real \(\tau\), and \(S_m\) is the orbit rank of the vertex exposed by an independent standard Gaussian objective, then
\[
\boxed{\frac{S_m-m/2}{\sqrt m}\ \Longrightarrow\ \min\{Z/2,\tau\},\qquad Z\sim N(0,1),}
\]
and the total normal-cone angle of the rank-saturated orbit tends to \(1-\Phi(2\tau)\). The limiting distribution has an atom of precisely that mass at \(\tau\).

## Assumptions and scope
The realization uses standard coordinate Euclidean geometry; a different affine realization need not have these external angles or widths. All Gaussian vectors have independent standard normal entries. \(\Phi\) and \(\phi\) denote the standard normal CDF and density, and \(\operatorname{erfc}(z)=2\pi^{-1/2}\int_z^\infty e^{-u^2}\,du\). The rank \(s\) is the number of nonzero vertex coordinates. The scaling theorem takes \(n_m\to\infty\) proportionally to \(m\), and it does not assert uniform error bounds over all aspect ratios. The finite integral is absolutely convergent.

The geometric primary source is Behrend et al. (arXiv:2207.14253, first publicly posted July 28, 2022), with primary MSC2020 classification 52B05; it develops the complete vertex structure. Heuer--Striker (arXiv:2012.09901, first posted December 17, 2020) originally introduced the object. The specific Gaussian assertions below are proved here, rather than taken as results of those papers.

## Proof
**1. Exact exposure rule and vertex orbits.** For a coefficient vector \(g\) with pairwise distinct nonzero entries, let \(g_{(1)}>\cdots>g_{(m)}\) be the sorted values. Because zero is an admissible coordinate value, any negative coefficient must receive zero at a maximizer: replacing a positive coordinate value there by zero is feasible and strictly improves the objective. Among positive coefficients, the rearrangement inequality shows that the largest chosen labels must be \(n,n-1,\ldots,n-s+1\), placed in decreasing order on the \(s\) largest positive coefficients. Each additional positive coefficient strictly increases the objective until \(s=n\). Therefore the unique maximizer places \(n,n-1,\ldots,n-S+1\) at the \(S=\min\{n,\#\{i:g_i>0\}\}\) largest positive coefficient positions, and zero elsewhere. Conversely, prescribing precisely \(s\) positive coordinates with a strict order exposes any prescribed vertex in \(V_s\) whenever \(s<n\). If \(s=n\le m\), choosing those \(n\) coordinates as strictly larger and positive also exposes any vertex in \(V_n\). Thus \(V_s\) are exactly the vertex orbits and have cardinalities \(m!/(m-s)!\). The Gaussian objective lies in the generic set with probability one.

**2. Normal-cone angles.** The signs of independent centered Gaussians are independent fair signs, and conditional on their number, all orders of the positive entries are equally likely. Hence for \(s<n\), a specified \(s\)-vertex is exposed precisely when exactly its \(s\) positions are positive and those positive values occur in the specified order: probability \(2^{-m}/s!\). For \(s=n\le m\), the \(n\) largest Gaussian coordinates must be positive and must appear in the fixed order at the specified positions. Conditional on at least \(n\) positive entries, exchangeability makes each of the \((m)_n=m!/(m-n)!\) ordered top-index tuples equally likely. This gives \(\Pr\{\operatorname{Bin}(m,1/2)\ge n\}/(m)_n\). Multiplying by orbit sizes proves the complete census, including the cases \(n\ge m\) (where no separate saturated rank appears except possibly \(n=m\)).

**3. Mean width.** For \(G\sim N(0,I_m)\), step 1 gives the support identity
\[
h_{\mathcal P}(G)=\sum_{j=1}^{\min(m,n)}(n-j+1)(G_{(j)})_+.
\]
For each \(t>0\), the number \(N_t=\#\{i:G_i>t\}\) is \(\operatorname{Bin}(m,q(t))\). Layer-cake integration, followed by Tonelli's theorem (all terms nonnegative), gives
\[
\mathbb E h_{\mathcal P}(G)=\int_0^\infty\mathbb E\left[\sum_{j=1}^{\min(N_t,n)}(n-j+1)\right]dt
=\int_0^\infty\mathbb E\left[\frac{r(2n-r+1)}2\right]dt,
\]
where \(r=\min(N_t,n)\). Substituting the binomial distribution gives the stated finite integral. Decompose \(G=RU\), where \(R=\|G\|_2\) is independent of uniform spherical \(U\), with mean \(R_m\). Positive homogeneity and reflection symmetry of the distribution of \(U\) imply \(w(\mathcal P)=2\mathbb E h_{\mathcal P}(G)/R_m\), proving the width formula.

**4. Limiting width and smoothness.** Write \(\rho_m=n_m/m\) and \(a_{m,t}=\min(n_m,N_t)/m\). The strong law for the binomial variable yields \(a_{m,t}\to a_t=\min(\rho,q(t))\) in probability for each fixed \(t\ge0\). Dividing the inner expression from step 3 by \(m^2\) gives
\[
\rho_m a_{m,t}-\frac12a_{m,t}^2+\frac{a_{m,t}}{2m}
\longrightarrow\rho a_t-\frac12a_t^2.
\]
For \(m\) large, \(\rho_m\le C\) and \(0\le a_{m,t}\le N_t/m\). Thus the integrand expectations are bounded by \((C+1)q(t)\), which is integrable on \([0,\infty)\). Dominated convergence gives
\[
\frac{\mathbb E h_{\mathcal P}(G)}{m^2}\longrightarrow
F(\rho)=\int_0^\infty\left[\rho\min(\rho,q(t))-\frac12\min(\rho,q(t))^2\right]dt.
\]
As \(R_m/\sqrt m\to1\), the normalized width tends to \(2F(\rho)\).

For \(0<\rho<1/2\), set \(z=\Phi^{-1}(1-\rho)>0\), so \(q(z)=\rho\). Differentiating the two integrals obtained by splitting at \(z\) (boundary terms cancel) gives \(F'(\rho)=\rho z+\int_z^\infty q(t)dt=\phi(z)\). Since \(F(0+)=0\), comparison of derivatives shows
\[
F(\rho)=\int_z^\infty\phi(t)^2dt=\frac{\operatorname{erfc}(z)}{4\sqrt\pi}.
\]
For \(\rho\ge1/2\), all \(t\ge0\) have \(q(t)\le\rho\); hence \(F(\rho)\) is affine in \(\rho\), and continuity at \(1/2\) gives \(2F(\rho)=1/(2\sqrt\pi)+\sqrt{2/\pi}(\rho-1/2)\). For \(\rho<1/2\), differentiation yields \(W'(\rho)=2\phi(z)\), \(W''(\rho)=2z\), and \(W'''(\rho)=-2/\phi(z)\). Above \(1/2\), \(W'\) is constant and \(W''=W'''=0\). At \(1/2\), \(z=0\) and the first two derivatives match, while the third does not; this proves the sharp regularity transition.

**5. Critical window.** By step 1, \(S_m=\min(n_m,K_m)\) with \(K_m\sim\operatorname{Bin}(m,1/2)\). The de Moivre--Laplace central limit theorem gives \((K_m-m/2)/\sqrt m\Rightarrow Z/2\). Applying the continuous mapping theorem to the minimum yields the asserted clipped-normal limit, while the same CLT applied to \(\Pr(K_m\ge n_m)\) gives its atom weight \(1-\Phi(2\tau)\). No finite sample approximation is used to justify these limits.

## Verification
The standalone standard-library file `verify.py` enumerates all sign patterns and absolute-magnitude orders for \(1\le m\le5\), \(1\le n\le6\), thereby checking the exact rational external angles of **every vertex** in 30 parameter profiles. It also evaluates 1,360 direct support-function optimizations for \(1\le m,n\le4\), tests the exact planar segment and triangle mean-width benchmarks, and numerically checks three large-dimensional normalized width profiles. Run `python3 verify.py` from the directory containing this file; it prints `CHECKS_PASSED` or fails an assertion. The analytical arguments above establish the results for all indicated integers and limits; the finite replay is corroborative and is not an exhaustive infinite proof.

## Relationship to prior work
Heuer and Striker introduced partial permutohedra as projections of partial alternating-sign-matrix polytopes and studied facets and face lattices. Behrend et al. systematically established the vertex structure, face lattice, volume and Ehrhart theory and their relation to anti-blocking permutohedra. Those full texts were inspected, including the object definition, vertex characterization and the sections on generalized permutohedra and further directions. Neither presents the Gaussian external solid-angle distribution, the mean-width integral, the aspect-ratio width transition, or the clipped-normal angular-window law.

Published geometric investigations of the same object include exact Euclidean diameters, inscribed balls, and Löwner ellipsoids; these are different invariants and their conclusions do not imply the four Gaussian angle/width formulas. In particular, the previously recorded diameter saturation at \(m=2n\) concerns an extremal **pair of vertices**, not typical Gaussian supporting directions. Likewise, normal fans of ordinary (type-A/B) permutohedra are related through ordered coordinates, but a normal-fan classification alone does not supply the capped positive-rank Gaussian-angle and third-order width laws here. The proof transparently uses classical Gaussian order statistics, binomial asymptotics and spherical Gaussian-width normalization; these general techniques are not claimed as new.

## Limitations
The result is specific to the standard partial-permutohedron coordinate realization and the isotropic Euclidean sphere. It does not give the full distribution of directional width, general Gaussian anisotropy, other valuations, non-Gaussian objective laws, or quantitative convergence rates uniform in \(\rho\). The angular formula follows from elementary signs and rankings; the new contribution asserted is the combined exact geometric census and sharp third-order asymptotic width phase, not invention of binomial or Gaussian limit laws. Equivalent expressions may exist under anti-blocking generalized permutohedron or normal-fan terminology and remain a residual bibliographic risk.

## References
1. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris and E. Insko, *Partial permutohedra*, arXiv:2207.14253, first public preprint 2022-07-28, https://arxiv.org/html/2207.14253v3. Primary MSC2020 52B05.
2. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first public preprint 2020-12-17, https://arxiv.org/html/2012.09901v3. Earlier introduction and foundational combinatorics.
3. *Projections and Angle Sums of Belt Polytopes and Permutohedra*, Results in Mathematics (2023), DOI 10.1007/s00025-023-01918-2. Related classical normal-fan framework, not asserted to contain the present formulas.
