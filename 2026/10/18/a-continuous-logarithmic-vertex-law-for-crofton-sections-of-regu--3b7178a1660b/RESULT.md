# A continuous logarithmic vertex law for Crofton sections of regular simplices

## Finding

Let \(N\ge3\), and write \(\Delta_{N-1}=\operatorname{conv}\{e_1,\ldots,e_N\}\) in the Euclidean affine space \(H=\{x\in\mathbb R^N:\sum_i x_i=1\}\). Choose an affine hyperplane by the rigid-motion-invariant measure \(d\sigma(u)\,dt\), where the normal \(u\) is a unit vector of \(H-H\), \(d\sigma\) is uniform spherical measure, and \(t\) is signed offset in the equation \(u\cdot x=t\). Condition on intersection with the simplex. This is a **Crofton section**, not a uniformly oriented central section: its normal has probability proportional to the width of the simplex in that direction. Denote by \(K_N\) the number of its vertices satisfying \(u\cdot e_i<t\), and by \(V_N\) the number of vertices of the section.

Let \(G_1,\ldots,G_N\) be independent standard Gaussian variables, \(\Phi\) the standard-normal CDF, and
\[
M_N=\mathbb E\bigl(\max_iG_i-\min_iG_i\bigr)
=\int_{-\infty}^{\infty}\bigl[1-\Phi(s)^N-(1-\Phi(s))^N\bigr]ds.
\]
For every integer \(1\le k<N\), the exact law and conditional vertex count are
\[
\boxed{\mathbb P(K_N=k)=\frac{\binom Nk}{M_N}\int_{\mathbb R}\Phi(s)^k(1-\Phi(s))^{N-k}\,ds,\qquad V_N=K_N(N-K_N).}
\]
In particular,
\[
\boxed{\mathbb E V_N=\frac{N(N-1)}{\sqrt\pi\,M_N}
\sim\frac{N^2}{2\sqrt{2\pi\log N}}.}
\]
Yet the typical section has a much smaller power-law size. If \(U\) is uniform on \([-1,1]\), then
\[
\boxed{\frac{\log V_N}{\log N}\ \Longrightarrow\ 2-U^2.}
\]
Its limiting distribution function is zero for \(v<1\), is \(1-\sqrt{2-v}\) for \(1\le v\le2\), and is one for \(v>2\). The median logarithmic exponent is \(7/4\), whereas \(V_N/\mathbb E V_N\to0\) in probability. The complete section face lattice, almost surely, is that of \(\Delta_{K_N-1}\times\Delta_{N-K_N-1}\); the convention \(\Delta_0\) denotes a point.

## Assumptions and scope

The result holds for every integer \(N\ge3\). Its probability measure is the **restriction of translation-and-rotation-invariant hyperplane measure to hyperplanes intersecting the simplex**, then normalized to mass one. For each normal the allowable offsets constitute an interval of length \(w_{\Delta}(u)\), so this measure is not equivalent to first choosing a uniform normal and then choosing a uniform intersecting offset. Hyperplanes through a simplex vertex have measure zero; all section polygons and face counts are interpreted almost surely. All Euclidean measures are intrinsic to \(H\), which has dimension \(N-1\); the result is invariant under Euclidean similarities of the simplex.

## Proof

**1. Sections and the face lattice.** For generic \(u,t\), reorder the vertex projections as \(u_{(1)}<\cdots<u_{(N)}\). An offset in \((u_{(k)},u_{(k+1)})\) separates \(k\) and \(N-k\) vertices. Because the simplex has all vertex pairs as edges, precisely \(k(N-k)\) edges cross the hyperplane, each in one distinct section vertex. To see the entire face structure, let \(a_i=t-u_i>0\) for low vertices and \(b_j=u_j-t>0\) for high vertices. Every section point has unique barycentric coordinates \(\lambda\) obeying \(\sum_{i\in L}a_i\lambda_i=\sum_{j\in R}b_j\lambda_j\). Positive rescaling gives normalized vectors \(p\in\Delta_{k-1}\) and \(q\in\Delta_{N-k-1}\); conversely, with \(D=\sum_{i\in L}p_i/a_i+\sum_{j\in R}q_j/b_j\), put \(\lambda_i=p_i/(a_iD)\) and \(\lambda_j=q_j/(b_jD)\). This bijection preserves the zero-coordinate face incidences, proving the asserted product face lattice.

**2. Crofton measure is a Gaussian-spacing ratio.** Integrating the offset within the interval for a fixed normal yields
\[
\mathbb P(K_N=k)=
\frac{\mathbb E_u(u_{(k+1)}-u_{(k)})}{\mathbb E_u(u_{(N)}-u_{(1)})}.
\]
Let \(\overline G=N^{-1}\sum_iG_i\), \(Y=(G_i-\overline G)_{i=1}^N\), and \(R=\|Y\|_2\). The direction \(Y/R\) is uniform on the unit sphere of the zero-sum subspace and independent of \(R\). Gaussian gaps equal \(R\) times direction gaps, and hence all common factors \(\mathbb ER\) cancel in the last ratio:
\[
\mathbb P(K_N=k)=\frac{\mathbb E(G_{(k+1)}-G_{(k)})}{M_N}.
\]
For the Gaussian count \(B_N(s)=\#\{i:G_i\le s\}\), the pathwise equality \(G_{(k+1)}-G_{(k)}=\int_{\mathbb R}{\boldsymbol 1}\{B_N(s)=k\}\,ds\) and Tonelli's theorem give the stated binomial integral. Summing the gaps over \(k=1,\ldots,N-1\) also gives the stated integral for \(M_N\).

**3. Exact expectation.** For arbitrary ordered real numbers,
\[
\sum_{k=1}^{N-1}k(N-k)(G_{(k+1)}-G_{(k)})
=\sum_{1\le i<j\le N}(G_{(j)}-G_{(i)})
=\sum_{i<j}|G_i-G_j|.
\]
Because \(G_i-G_j\) is Gaussian with variance \(2\), \(\mathbb E|G_i-G_j|=2/\sqrt\pi\). Division by \(M_N\) yields the exact expectation. Standard Gaussian tail inequalities show
\(\max_i G_i/\sqrt{2\log N}\to1\) in \(L^1\) (and analogously for the negative minimum): for each fixed \(0<\varepsilon<1\), the upper-tail union bound is \(O(N^{1-(1+\varepsilon)^2}/\sqrt{\log N})\), and the lower-tail failure is at most \(\exp[-c_\varepsilon N^{1-(1-\varepsilon)^2}/\sqrt{\log N}]\). Tail integration gives uniform integrability. Hence \(M_N\sim2\sqrt{2\log N}\), proving the mean asymptotic.

**4. The continuous logarithmic exponent.** Put \(b_N=\sqrt{2\log N}\). Introduce a real auxiliary level \(S_N\) with density
\[
f_N(s)=\frac{1-\Phi(s)^N-(1-\Phi(s))^N}{M_N}.
\]
Conditional on \(S_N=s\), the integer \(K_N\) is distributed as \(\operatorname{Bin}(N,\Phi(s))\) conditioned to belong to \(\{1,\ldots,N-1\}\). This joint construction reproduces the exact law in the finding. For each fixed \(|z|<1\), both \(N\Phi(b_Nz)\) and \(N(1-\Phi(b_Nz))\) tend to infinity, while for \(|z|>1\), one of these tends to zero. Thus \(b_Nf_N(b_Nz)\to\tfrac12\boldsymbol1_{\{|z|<1\}}\) for almost every \(z\), using \(M_N/b_N\to2\). Both sides are probability densities, so Scheffé's lemma gives \(S_N/b_N\Longrightarrow U\) with \(U\) uniform on \([-1,1]\).

For fixed \(|z|<1\), Mills' ratio implies
\[
\frac{\log\bigl[N\min\{\Phi(b_Nz),1-\Phi(b_Nz)\}\bigr]}{\log N}
\longrightarrow1-z^2.
\]
The convergence is uniform on compact subintervals of \((-1,1)\), with the case \(z=0\) given by \(\Phi(0)=1/2\). Standard binomial Chernoff bounds, uniformly over such compact subintervals, show that the log of \(\min(K_N,N-K_N)\) has the same exponent in probability conditional on the level. Since the limiting level law assigns arbitrarily small probability to neighborhoods of \(\pm1\), the joint limit is
\[
\frac{\log\min(K_N,N-K_N)}{\log N}\Longrightarrow1-U^2.
\]
Finally \(N/2\le\max(K_N,N-K_N)\le N\), so \(\log V_N/\log N=1+\log\min(K_N,N-K_N)/\log N+o(1)\) uniformly. This proves the limit law. For any fixed \(\eta>0\), the probability of \(V_N\ge\eta\mathbb EV_N\) tends to zero: by the expectation asymptotic, this event requires a logarithmic exponent approaching \(2\), while the continuous limiting law has no mass at \(2\). This proves the last assertion.

## Verification

Run the standalone, standard-library-only script `python3 verify.py`. It independently checks Gaussian-spacing quadrature and the pairwise-distance moment identity for \(N=3,4,5,8,16,64\), compares the tetrahedral exact quadrilateral probability for \(N=4\), and compares exact integral probabilities with 35,000 seeded width-weighted Gaussian trials at \(N=4\) and \(N=8\). All checks passed. These finite checks do **not** establish the all-\(N\) proof or its asymptotic limit; those rest on the preceding identities, tail estimates, and conditional binomial arguments.

## Relationship to prior work

Birkemeyer, Brose, Brandenburg and Prün (2026, arXiv:2609.16195v1) motivate combinatorial questions about polytope slices and reconstruction. Their accessible abstract does not state an affine Crofton probability law; their complete manuscript was not accessible here, leaving a specifically recorded priority risk. Baryshnikov and Vitale (1994) relate regular simplex projections to Gaussian samples, an antecedent to the Gaussian-normal representation; that connection alone does not provide the width-biased affine-section law or its nondegenerate logarithmic exponent. Published analyses of uniformly oriented **central** simplex sections treat a different sampling measure and have contrasting \(N^2\)-order face counts. Fish, Ryabogin, Sun and Yaskin (arXiv:2610.10229v1), whose accessible HTML text was inspected, study determinacy by hyperplane section functions, not this combinatorial stochastic invariant.

## Limitations

The sampling model conditions the invariant measure of *affine hyperplanes* on intersecting a regular simplex; changing the model to central or uniformly direction-first sections changes the answer. There is no assertion of a sharp rate of weak convergence. The finite computations are corroboration and not certificates for infinitely many dimensions. Historical priority remains uncertain because the full text of at least one plausible 2026 slicing paper and older geometric probability sources was unavailable for complete comparison. The work has only a self-review; no independent audit has been performed.

## References

1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195v1 (first submitted 2026-09-14), https://arxiv.org/abs/2609.16195 .
2. Y. Baryshnikov and R. A. Vitale, *Regular simplices and Gaussian samples* (1994), (bibliographic title and year) .
3. H. Dirksen, *Sections of the regular simplex—Volume formulas and estimates* (2017), (bibliographic title and year) .
4. A. Fish, D. Ryabogin, W. R. Sun, V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229v1 (2026-10-07), https://arxiv.org/abs/2610.10229 .
