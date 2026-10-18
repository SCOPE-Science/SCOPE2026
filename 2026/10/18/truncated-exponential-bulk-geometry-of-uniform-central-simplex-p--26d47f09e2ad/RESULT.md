# Truncated-exponential bulk geometry of uniform central simplex polytopes

## Finding
For a fixed ratio \(c>1\), a uniformly sampled point of the central simplex polytope has an explicit high-dimensional coordinate profile. Define \(a_c=\log(c)/(c-1)\) and the probability measure
\[
\nu_c(ds)=\frac{e^{-s}\mathbf 1_{[a_c,ca_c]}(s)}{e^{-a_c}-e^{-ca_c}}\,ds.
\]
If \(X^{(m)}\) is uniform in \(P_m(c)\), the empirical measure of its \(m\) scaled barycentric coordinates converges weakly in probability to \(\nu_c\). Every fixed number of distinct coordinates becomes asymptotically independent with this law. Their extreme values obey
\[
m\min_iX_i^{(m)}\xrightarrow{\mathrm P}a_c,\qquad m\max_iX_i^{(m)}\xrightarrow{\mathrm P}ca_c.
\]
More geometrically, with \(o_m=m^{-1}\mathbf1\),
\[
\boxed{\quad m\|X^{(m)}-o_m\|_2^2\xrightarrow{L^q}
1-\frac{c(\log c)^2}{(c-1)^2}\quad}\qquad(1\le q<\infty).
\]
For the original edge-trisection construction, \(c=2\), this sharp limiting constant is \(1-2(\log2)^2=0.0390939722\ldots\). The normalized minimum of an associated independent-exponential sampling representation satisfies an exact finite-dimensional beta law, providing a nonasymptotic route to the limit.

## Assumptions and scope
Fix a real \(c>1\), independent of \(m\). For every integer \(m\ge2\), write
\[
\Delta_{m-1}=\{x\in\mathbb R^m:x_i\ge0,\ \sum_{i=1}^m x_i=1\},\qquad
P_m(c)=\{x\in\Delta_{m-1}:x_i\le c x_j\ \forall i,j\}.
\]
The expression 'uniform' always means normalized \((m-1)\)-dimensional Euclidean Hausdorff measure in the affine hyperplane \(\sum_i x_i=1\), not uniform over the vertices. Define \(\mu_m=m^{-1}\sum_{i=1}^m\delta_{mX_i^{(m)}}\). Weak convergence in probability means that for every bounded continuous function \(f\) on \(\mathbb R\), \(\int f\,d\mu_m\to\int f\,d\nu_c\) in probability. The coordinate limits are for every fixed integer \(k\ge1\) as \(m\ge k\to\infty\).

## Proof
**1. Exponential coupling and a beta-law minimum.** Let \(Y_1,\ldots,Y_m\) be independent rate-one exponentials and \(S_m=\sum_iY_i\). The vector \(Y/S_m\) has the uniform Dirichlet law on \(\Delta_{m-1}\) and is independent of \(S_m\sim\operatorname{Gamma}(m,1)\). Since the event
\[
E_m(c)=\{\max_i Y_i\le c\min_i Y_i\}
\]
is invariant under common positive rescaling, \(Y/S_m\) conditional on \(E_m(c)\) is uniform on \(P_m(c)\), while \(S_m\) remains independent of \(E_m(c)\).

There is almost surely a unique index attaining \(Y_{(1)}=\min_iY_i\). Summing over that index, its unnormalized conditional density on \(E_m(c)\) is
\[
m e^{-y}(e^{-y}-e^{-cy})^{m-1}
=m e^{-my}(1-e^{-(c-1)y})^{m-1},\quad y>0.
\]
Under \(Z_m=e^{-(c-1)Y_{(1)}}\), the substitution \(dy=-dz/((c-1)z)\) makes this density proportional to
\[
z^{m/(c-1)-1}(1-z)^{m-1}\,dz,\quad0<z<1.
\]
Thus, **exactly** under the conditional law,
\[
Z_m\sim\operatorname{Beta}\!\left(\frac{m}{c-1},m\right),\quad
\mathbb EZ_m=\frac1c,\quad
\operatorname{Var}(Z_m)=\frac{(c-1)^2}{c^2(mc+c-1)}.
\]
Chebyshev's inequality and continuity of the logarithm at \(1/c\) give \(Y_{(1)}\to a_c=\log(c)/(c-1)\) in probability.

**2. Conditional product structure and the empirical limit.** Conditional on the minimum value \(y>0\) and its unique index, the remaining \(m-1\) entries are independent with density
\[
q_y(s)=\frac{e^{-s}}{e^{-y}-e^{-cy}}\mathbf1_{[y,cy]}(s).
\]
For bounded continuous \(f\), the variance of the empirical average over these \(m-1\) entries, given \(y\), is at most \(4\|f\|_\infty^2/(m-1)\); the minimum contributes at most \(2\|f\|_\infty/m\) to the difference of empirical averages. Since \(Y_{(1)}\to a_c\) and \(y\mapsto\int f(s)q_y(s)ds\) is continuous at \(a_c\), conditional Chebyshev and bounded convergence prove
\[
\frac1m\sum_i f(Y_i)\ \Big|\ E_m(c)\quad\xrightarrow{\mathrm P}\quad \int f\,d\nu_c.
\]
Because \(S_m/m\to1\) in probability even after conditioning (independence from the event), scaling \(Y_i\) by \(m/S_m\) yields \(\mu_m\Rightarrow\nu_c\) in probability. One can justify the scaling without any unboundedness issue: under the conditional event, \(mX_i\in[1/c,c]\) deterministically, and the values \(Y_i\) lie with high probability in a fixed compact interval because the conditional minimum converges to \(a_c\) and the maximum is at most \(cY_{(1)}\). Uniform continuity on compact sets applies.

The conditional joint law of the \(m\) coordinates is exchangeable. Drawing \(k\) distinct labeled coordinates differs from drawing \(k\) times with replacement from \(\mu_m\) with probability at most \(k(k-1)/(2m)\). Since \(\mu_m\Rightarrow\nu_c\) in probability and \(\nu_c\) is deterministic, every fixed \(k\)-tuple of scaled coordinates converges jointly to \(\nu_c^{\otimes k}\).

**3. Extremes.** The minimum converges as shown. For any small \(\epsilon>0\), the truncated-exponential law \(q_y\) assigns a positive probability (uniformly for \(y\) near \(a_c\)) to \([cy-\epsilon,cy]\). Conditional independence of the remaining \(m-1\) observations then implies \(\max_iY_i-cY_{(1)}\to0\) in probability. Dividing both extremes by \(S_m/m\to1\) proves the two claimed normalized endpoint limits.

**4. Exact second moment and Euclidean radius.** Write \(a=a_c\) and \(r=e^{-(c-1)a}=1/c\). Integration by parts gives
\[
\int s\,\nu_c(ds)=\frac{(a+1)-(ca+1)r}{1-r}=1
\]
and
\[
\int s^2\,\nu_c(ds)=\frac{(a^2+2a+2)-((ca)^2+2ca+2)r}{1-r}
=2-ca^2.
\]
It follows that \(\int(s-1)^2\nu_c(ds)=1-ca^2>0\). Because
\[
m\|X^{(m)}-o_m\|_2^2=\frac1m\sum_i(mX_i^{(m)}-1)^2,
\]
empirical convergence proves the claimed limit in probability. Also \(1/c\le mX_i^{(m)}\le c\) for every member of \(P_m(c)\), so the squared radial statistics are bounded deterministically by a finite constant depending on \(c\). This upgrades convergence in probability to convergence in each fixed \(L^q\), \(1\le q<\infty\). The coefficient is strictly positive because \(\nu_c\) has a nondegenerate density on an interval of positive length. This completes the proof.

## Verification
The standalone standard-library program `verify.py` checks the transformed beta parameters, exact mean and variance identities, the two moment evaluations by numerical quadrature, the exact two-coordinate central-segment benchmark, and an independent conditional-exponential Monte Carlo sampler. The numerical experiments only corroborate the analytical proof: they neither claim nor establish convergence for all dimensions.

To run: `python verify.py` (Python 3.9+; no nonstandard libraries). The finite simulated sample uses the exact latent beta sampler followed by independent truncated exponentials; this checks normalization and radial predictions on an object sampled with its correct conditional uniform-volume law.

## Relationship to prior work
Kazakov (2026) introduced the edge-trisection central simplex polytopes with \(c=2\), gave their volume fraction and combinatorial data, and used the unconditional exponential/Dirichlet representation. These established facts are used as motivation and sampling machinery, not claimed as new. Kazakov's conclusion points to studying an appropriately rescaled large-dimensional geometry. The new content here is the fixed-ratio **uniform-volume bulk coordinate law**, the exact beta localization identity, asymptotic coordinate independence, concentration of the extreme coordinates, and the sharp Euclidean radial limit for each \(c>1\).

A prior mathematical finding derives exact fixed-ratio volume fractions and Hausdorff distances together with a logarithmic volume/Hausdorff transition when the ratio grows with dimension. Its statements concern overall volume and worst-case distance, and neither assert nor logically determine the conditional joint coordinate law or the typical Euclidean radius proved here. Standard general results on the maximum coordinate of an unconditioned uniform simplex do not impose the ratio constraint; the conditional regime is different.

## Limitations
Only fixed \(c>1\) is considered: no uniformity as \(c\downarrow1\) or \(c\to\infty\), and no regime where \(c=c_m\) changes with \(m\), is proved. Weak convergence is an empirical random-point (bulk-volume) statement, not Hausdorff or Banach–Mazur convergence of the whole polytope. The beta variable belongs to the latent independent-exponential coupling rather than being a deterministic function of the normalized point. The underlying exponential and beta techniques are classical; bibliographic uniqueness of this specific application is not independently certified.

## References
1. Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087, initially public June 1, 2026, https://arxiv.org/abs/2606.02087. Source inspected through an openly accessible full-text mirror of the manuscript, particularly Sections 2–5 and the probabilistic example appendix.
2. Eric W. Weisstein, *Marion's Theorem*, MathWorld, https://mathworld.wolfram.com/MarionsTheorem.html, background on the classical triangle and Kazakov's high-dimensional volume ratio.
3. S. Fried, *The restrictiveness of the hazard rate order and the moments of the maximal coordinate of a random vector uniformly distributed on the probability n-simplex*, Statistics & Probability Letters 185 (2022), 109414, doi:10.1016/j.spl.2022.109414. Relevant background on unconditioned simplex-coordinate extrema; only the abstract and bibliographic record were inspected.
