# Poisson extremal-field fluctuations of widths across interval-weighted associahedra

## Finding

For every continuous function \(f:\{(s,t):0\le s\le t\le1\}\to(0,\infty)\), define the interval-simplex realization
\[
 P_n(f)=\sum_{1\le i\le j\le n} f((i-1)/n,j/n)\,\operatorname{conv}\{e_i,\ldots,e_j\}\subset\mathbb R^n,\qquad n\ge3.
\]
Every summand coefficient is strictly positive, so these are deformations with the path-associahedral normal fan. Let \(U_n\) be uniform on the unit sphere of the zero-sum subspace \(H_n=\{x:\sum_i x_i=0\}\), and let \(W_n\) be the Euclidean directional width of \(P_n(f)\) along \(U_n\). Define
\[
 a_n=(2\log n)^{-1/2},\quad b_n=\sqrt{2\log n}-\frac{\log\log n+\log(4\pi)}{2\sqrt{2\log n}},\quad
 C_n=\sum_{1\le i\le j\le n}f((i-1)/n,j/n),
\]
and \(\eta_n=\sqrt2\,\Gamma(n/2)/\Gamma((n-1)/2)\).

Let \(\mathcal N_+\) and \(\mathcal N_-\) be independent Poisson point processes on \((0,1)\times\mathbb R\), each with intensity \(du\,e^{-z}dz\), and define their interval-extremal fields by
\[
 M_\pm(s,t)=\sup\{z:(u,z)\in\mathcal N_\pm,\ s<u<t\},\qquad 0\le s<t\le1.
\]
Then the following integrable, **non-Gaussian** random variable governs the full second-order directional-width fluctuations:
\[
 \Xi_f=\int_0^1\int_s^1 f(s,t)\bigl(M_+(s,t)+M_-(s,t)\bigr)\,dt\,ds,
\]
\[
 \boxed{\quad\frac{\eta_n W_n-2b_n C_n}{n^2a_n}\ \Longrightarrow\ \Xi_f.\quad}
\]
Moreover the centered means converge, with an explicit continuous-profile correction:
\[
 \boxed{\quad\lim_{n\to\infty}\frac{\eta_n\mathbb EW_n-2b_n C_n}{n^2a_n}
 =2\int_0^1\int_s^1 f(s,t)\bigl(\gamma_{\mathrm E}+\log(t-s)\bigr)\,dt\,ds.\quad}
\]
For the canonical unit-weight path associahedron \(f\equiv1\), the right-hand side is \(\gamma_{\mathrm E}-3/2\), so the first two terms of its mean Euclidean width are determined explicitly. Non-Gaussianity persists for *every* strictly positive continuous interval-weight profile.

## Assumptions and scope

The weights are sampled on a fixed profile \(f\) that is continuous and strictly positive on the closed triangle, hence bounded above and away from zero. The ambient Euclidean metric is the unscaled standard one. The affine hull of \(P_n(f)\) is parallel to \(H_n\), of dimension \(n-1\). Width is the maximum minus minimum of the Euclidean linear functional in the stated unit direction; it is invariant under translations perpendicular or parallel to the affine hull. The asymptotic is \(n\to\infty\) with \(f\) fixed. No growth of \(f\) with dimension, no discontinuous profile, and no claim concerning volume or higher intrinsic volumes is included. Singleton simplices are allowed; they contribute translations only.

## Proof

**1. Exact support formula and Gaussian-to-spherical conversion.**  Write \(w_{ij}=f((i-1)/n,j/n)\). The support function of \(\operatorname{conv}\{e_i,\ldots,e_j\}\) at \(g\in\mathbb R^n\) is \(\max_{i\le k\le j}g_k\). Minkowski additivity therefore gives, for all \(g\),
\[
 \mathcal W_n(g):=h_{P_n(f)}(g)+h_{P_n(f)}(-g)
 =\sum_{1\le i\le j\le n}w_{ij}\left(\max_{i\le k\le j}g_k-\min_{i\le k\le j}g_k\right). \tag{1}
\]
This identity is unaffected by adding a common constant to all \(g_k\). If \(G_k\) are independent standard normals, their orthogonal projection onto \(H_n\) can be written \(G-\overline G\mathbf1=R_nU_n\), where \(R_n\sim\chi_{n-1}\), \(U_n\) is uniform as above, and \(R_n,U_n\) are independent. Consequently \(\mathcal W_n(G)=R_nW_n\), \(\mathbb E R_n=\eta_n\), and \(\eta_n\mathbb EW_n=\mathbb E\mathcal W_n(G)\) exactly.

**2. Joint upper and lower extremal processes.**  Put \(u_{nk}=(k-1/2)/n\) and
\[
 \mathcal N_n^+=\sum_{k=1}^n\delta_{(u_{nk},(G_k-b_n)/a_n)},\qquad
 \mathcal N_n^-=\sum_{k=1}^n\delta_{(u_{nk},(-G_k-b_n)/a_n)}.
\]
The Gaussian Mills-ratio expansion gives, locally uniformly for fixed real \(z\),
\[
 n\Pr\{G_1>b_n+a_nz\}\longrightarrow e^{-z}.
\]
For disjoint spatial subintervals and bounded-below mark sets, independent rare-event counts converge to Poisson counts. Upper and lower exceedances cannot occur simultaneously at a single index once \(n\) is large; their mixed joint generating functions factor asymptotically. Thus \((\mathcal N_n^+,\mathcal N_n^-)\) converges jointly (vaguely on bounded-below mark regions) to the *independent* pair \((\mathcal N_+,\mathcal N_-)\).

**3. Passage from extremal point processes to interval integrals.**  Normalize each interval maximum by \(a_n\) and \(b_n\), and define
\[
 Y_{n,ij}^{\pm}=\max_{i\le k\le j}\frac{\pm G_k-b_n}{a_n}.
\]
Then (1) yields the exact algebraic identity
\[
 \frac{\mathcal W_n(G)-2b_n C_n}{n^2a_n}
 =\frac1{n^2}\sum_{1\le i\le j\le n}w_{ij}(Y_{n,ij}^{+}+Y_{n,ij}^{-}). \tag{2}
\]
Fix \(\varepsilon>0\). On lattice intervals \((i-1)/n\le s<t=j/n\) of length at least \(\varepsilon\), truncate the point processes to marks above \(-L\). Partition \([0,1]\) into finitely many cells of length smaller than \(\varepsilon/3\). The probability that every cell contains at least one retained mark tends to one as \(L\to\infty\), uniformly in all sufficiently large \(n\): the limiting empty-cell probabilities are \(\exp(-|J|e^L)\). On this event every interval of length at least \(\varepsilon\) has a retained atom, so the interval maxima are determined by finitely many atoms. Almost surely no such atom lies at a predetermined integration boundary. The resulting bounded, piecewise-constant extremal fields are continuous as functionals of the atom locations outside sets of planar Lebesgue measure zero. Riemann-sum convergence for the continuous weight \(f\) and joint point-process convergence imply convergence of (2), restricted to these long intervals, to the integral of \(f(M_++M_-)\) over \(t-s\ge\varepsilon\).

The discarded short intervals are uniformly negligible **in first absolute moment**, not merely in expectation. A standard normal-maximum tail estimate, obtained by integrating the Mills-ratio bounds above and below \(b_n\), gives a numerical constant \(C\) such that for every \(n\ge3\) and \(1\le k\le n\),
\[
 \mathbb E\left|\frac{\max(G_1,\ldots,G_k)-b_n}{a_n}\right|
 \le C\left(1+\log\frac nk\right). \tag{3}
\]
One verification of (3) is to split the upper/lower tail integrals at \(b_n\). Above \(b_n\), \(k\overline\Phi(b_n+a_nz)\) has uniformly integrable exponential decay. Below \(b_n\), \(\Phi(b_n-a_nz)^k\) is bounded by \(\exp[-c(k/n)e^{z/4}]\) until the threshold becomes negative; the remaining negative-normal tail is summable. When \(b_n-a_nz<0\), use \(\Phi(y)^k\le2^{-(k-1)}\Phi(y)\) for \(y\le0\), whose remaining integral is at most \(C\sqrt{\log n}\,2^{-k}\) and is also bounded by \(C(1+\log(n/k))\). Substituting \(v=(k/n)e^{z/4}\) in the preceding region bounds the lower contribution by that same logarithmic expression. The same estimate holds for minus signs. Hence, with \(\|f\|_\infty<\infty\),
\[
 \limsup_{n\to\infty}\mathbb E\left|\frac1{n^2}
 \sum_{j-i+1\le\varepsilon n}w_{ij}(Y_{n,ij}^++Y_{n,ij}^-)\right|
 \le C_f\varepsilon(1+|\log\varepsilon|). \tag{4}
\]
For a Poisson process, \(M_\pm(s,t)\) has the law \(\gamma\)-centered Gumbel shifted by \(\log(t-s)\), so \(\mathbb E|M_\pm(s,t)|\le C+|\log(t-s)|\); its integral over \(t-s<\varepsilon\) satisfies the same vanishing bound. Sending \(L\to\infty\) and then \(\varepsilon\downarrow0\) proves convergence in distribution in (2), along with uniform integrability sufficient for the stated first-moment limit.

**4. The explicit mean.**  The void probability of the limiting process in \((s,t)\times(z,\infty)\) is \(\exp(-(t-s)e^{-z})\), hence
\[
 \mathbb E M_\pm(s,t)=\gamma_{\mathrm E}+\log(t-s).
\]
Fubini is justified by the preceding logarithmic integrability bound. This gives the displayed expression for \(\mathbb E\Xi_f\). Independently, for every finite \(n\) there is an exact integral formula
\[
 \eta_n\mathbb EW_n=2\sum_{1\le i\le j\le n}w_{ij}\mu_{j-i+1},\qquad
 \mu_k=\int_0^\infty\!\left[1-\Phi(z)^k-(1-\Phi(z))^k\right]dz, \tag{5}
\]
where \(\Phi\) is the standard normal distribution function. For \(f\equiv1\), evaluating \(2\int_0^1(1-v)(\gamma_{\mathrm E}+\log v)dv\) gives \(\gamma_{\mathrm E}-3/2\).

**5. Spherical normalization.**  Standard chi concentration implies \(R_n-\eta_n=O_{\Pr}(1)\) and \(R_n\asymp_{\Pr}\sqrt n\). Formula (1) and Gaussian maximum bounds give \(\mathcal W_n(G)=O_{\Pr}(n^2b_n)\). Hence
\[
 \frac{(R_n-\eta_n)W_n}{n^2a_n}
 =O_{\Pr}\left(\frac{b_n}{\sqrt n\,a_n}\right)
 =O_{\Pr}\left(\frac{\log n}{\sqrt n}\right)\longrightarrow0.
\]
Slutsky's lemma transfers the Gaussian width limit to the claimed spherical width limit; the mean identity follows from independence, not an approximation.

**6. Genuine non-Gaussianity.**  Write \(m_f=\min f>0\). Retain all negative-process atoms, but initially retain in the positive process only atoms with marks \(z\le0\). The resulting integral \(\Xi_f^{(0)}\) is finite almost surely, so for some fixed \(K\), \(\Pr\{\Xi_f^{(0)}\ge-K\}>0\). This event is independent of positive-process atoms with \(z>0\). If one such extra atom occurs at \(u\in[1/3,2/3]\) with mark \(h>0\), it raises the positive maximum on every interval \(s<u<t\) by at least \(h\), since every baseline positive-process mark is nonpositive. The corresponding weighted interval area is at least \(m_fu(1-u)\ge 2m_f/9\). Thus
\[
 \Pr\{\Xi_f>x\}\ge c_f\exp\left(-\frac{9(x+K)}{2m_f}\right)
\]
for all sufficiently large \(x\), by the independent Poisson exceedance probability on the central third. Every nondegenerate Gaussian random variable has a quadratically decaying logarithmic upper tail, whereas this distribution has at least an exponentially decaying tail. Therefore \(\Xi_f\) is not Gaussian (nor a degenerate constant).

## Verification

A standalone checker (`verify.py`) recomputes support values by independent explicit Minkowski-vertex enumeration in dimension four, checks all-interval range identities and translation invariance, and compares the exact normal-integral mean formula (5) against independent Gaussian sampling. It covers positive constant, interval-length, and nonseparable endpoint-dependent profiles. A truncated-Poisson simulation is included as a diagnostic, explicitly **not** a proof of the limit. Its observed output is recorded in `VERIFICATION.md`. The proof of the distributional limit uses the analytical extremal-process and short-interval arguments above, not simulation.

## Relationship to prior work

Postnikov's construction of generalized permutohedra as sums of coordinate simplices and the path graph-associahedron construction are established results, as are the nested-fan and deformation-cone results of Padrol--Pilaud--Poullot. The exact mean-width identity (5) is an immediate application of Minkowski support additivity and standard Gaussian maxima, and is not independently claimed as a new general principle. Kabluchko--Litvak--Zaporozhets established related Gaussian width and Gumbel limit laws for a **single** regular simplex or crosspolytope. The present claim concerns the **strongly dependent sum over all consecutive-coordinate simplices** and its integrated spatial Poisson-field law, including continuous positive nonuniform weights and the explicit profile-dependent second-order correction. Neither simplex extremes alone nor deformation-cone structure alone yields this joint limit. Relevant mathematical database records about tree graphical-zonotope widths and tree-associahedron braid walls concern different objects or invariants. Bibliographic equivalences under the terms integrated sliding-window extremes or subarray-maxima functionals are possible and are recorded in the accompanying review.

## Limitations

The claim concerns the stated Euclidean realization and its positive continuous weight profiles; an arbitrary combinatorially equivalent realization need not obey the formula. It does not establish a density, exact variance, exponential moments, or a universal covariance formula for \(\Xi_f\). Independence of the two limiting Poisson processes is asymptotic; upper and lower maxima at finite dimension are not independent. The full integral is not the maximum over only finitely many macroscopic windows. Numerical simulations cannot establish Poisson convergence or originality. Independent scholarly audit and exhaustive bibliographic verification have not been performed.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200 (first publicly submitted 2021-09-19), especially Theorem 2.2, Remark 2.4, and the interval deformation framework.
2. A. Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163 (first publicly submitted 2005-07-07), especially the coordinate-simplex Minkowski-sum realization and nested families.
3. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (first publicly submitted 2015-11-26), especially Sections 1 and 3--4 on Gaussian widths and Gumbel limits.
4. E. C. Bailey and J. P. Keating, *Maxima of log-correlated fields: some recent developments*, Journal of Physics A 55 (2022), 053001, for the classical independent-normal extremal normalization used here (not for the new integral limit).
