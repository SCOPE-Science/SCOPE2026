# Exact homotopy spectrum of random shortest-geodesic polygons on the round projective plane

## Finding
Let \(M=\mathbb{RP}^{2}=S^2/\{\pm1\}\) carry the quotient of the unit round-sphere metric and its normalized Riemannian area measure. For every integer \(n\ge3\), take independent area-uniform points \(P_1,\ldots,P_n\in M\). Connect successive points, including \(P_n\) to \(P_1\), by the almost surely unique **shortest geodesic** and regard their concatenation as a based closed path \(\Gamma_n\). Define \(q_n=\Pr([\Gamma_n]\ne0\text{ in }\pi_1(M)\cong\mathbb Z/2)\).

For \(k\ge0\) put \(c_k=\frac{1}{2^{2k+1}}\frac{1}{k+1}\binom{2k}{k}\). Then the complete exact law is
\[
\boxed{q_n=\frac12\left[1-\sum_{k=0}^{\infty}(4k+3)(-1)^{kn}c_k^n\right],\qquad n\ge3.}
\]
The series converges absolutely. In particular,
\[
\boxed{q_3=\frac1\pi,\quad q_4=\frac4{\pi^2},\quad 0<q_3<q_4<q_5<\cdots<\frac12.}
\]
The following explicit *two-mode, all-length error bound* holds for every \(n\ge3\):
\[
\boxed{\left|q_n-\left(\frac12-\frac3{2^{n+1}}-\frac72\left(-\frac18\right)^n\right)\right|\le\frac{18}{16^n}.}
\]
Thus the bias towards contractible loops decays exponentially with exact dominant coefficient \(3\), and its first correction alternates with the number of edges.

There is also a geometric conditional law. If the distance between \(P_1,P_2\) of a random triangle is \(\theta\in[0,\pi/2]\), the conditional probability that its shortest-geodesic loop is noncontractible is \(\theta/\pi\). For a random quadrilateral, conditioning instead on the distance between its opposite vertices \(P_1,P_3\) gives probability \(2(\theta/\pi)(1-\theta/\pi)\). These formulas are understood as versions of regular conditional probabilities, and are valid away from measure-zero endpoint degeneracies.

## Assumptions and scope
The word *polygon* denotes the cyclic geodesic loop defined above, not necessarily an embedded or simple polygon; self-intersections are allowed. The sampling is independent, exactly uniform by Riemannian area, and uses the standard curvature-one metric. No assertion is made for arbitrarily chosen nonminimizing geodesics, different metrics, nonuniform samples, or other manifolds. The homotopy class is measured by whether its lift to the double cover \(S^2\to M\) closes. Every sampled pair has a unique shortest geodesic almost surely, since the exceptional set of orthogonal spherical lifts has measure zero.

## Proof
**1. Lift parity.** Choose independent uniform spherical lifts \(X_i\in S^2\). Write \(X_{n+1}=X_1\) and \(\varepsilon_i=\operatorname{sgn}\langle X_i,X_{i+1}\rangle\). The unique shortest projective geodesic between their classes lifts from \(X_i\) toward \(\varepsilon_i X_{i+1}\), since its length is \(\arccos|\langle X_i,X_{i+1}\rangle|<\pi/2\). Starting from \(X_1\) and continuing around the concatenation, the lifted endpoint is \((\prod_i\varepsilon_i)X_1\). Because \(S^2\) is the simply connected double cover of \(M\), the loop is noncontractible exactly when \(\prod_i\varepsilon_i=-1\). This condition is independent of the arbitrary signs of the chosen lifts: replacing any \(X_i\) by \(-X_i\) changes exactly two adjacent signs.

**2. Spherical sign spectrum.** Let \(\sigma\) be probability surface area on \(S^2\) and let \(T:L^2(S^2,\sigma)\to L^2(S^2,\sigma)\) be the self-adjoint Hilbert–Schmidt operator
\[
(Tf)(x)=\int_{S^2}\operatorname{sgn}\langle x,y\rangle f(y)\,d\sigma(y).
\]
Its bounded measurable kernel makes \(T^n\) trace class for \(n\ge2\). Fubini's theorem and the Hilbert–Schmidt trace identity identify the cyclic product integral with \(\operatorname{tr}(T^n)\). Consequently
\[
1-2q_n=\mathbb E\prod_i\varepsilon_i=\operatorname{tr}(T^n).
\]
The spherical harmonic space of degree \(\ell\) has multiplicity \(2\ell+1\). The Funk–Hecke identity gives its eigenvalue
\[
\lambda_\ell=\frac12\int_{-1}^{1}\operatorname{sgn}(t)P_\ell(t)\,dt,
\]
where \(P_\ell\) is the ordinary Legendre polynomial. Even degrees yield zero. For \(\ell=2k+1\), the standard derivative identity \((2\ell+1)P_\ell=P'_{\ell+1}-P'_{\ell-1}\) and \(P_{2j}(0)=(-1)^j\binom{2j}{j}/4^j\) give
\[
\lambda_{2k+1}=\int_0^1P_{2k+1}(t)\,dt
=(-1)^k\frac{1}{2^{2k+1}}\frac{1}{k+1}\binom{2k}{k}=(-1)^kc_k.
\]
Thus the multiplicity is \(4k+3\) and the exact series follows. The trace identity also shows \(\sum_{k\ge0}(4k+3)c_k^2=\|T\|_{\rm HS}^2=\iint1\,d\sigma\,d\sigma=1\); this establishes absolute convergence for all \(n\ge2\), because \(c_k\le1/2\).

**3. Strict monotonicity.** Put \(b_n=1-2q_n=\operatorname{tr}(T^n)\). The coefficient recurrence
\[
 c_0=\tfrac12,\qquad c_{k+1}=c_k\frac{2k+1}{2(k+2)}
\]
shows \(c_1=1/8\) and \(c_k\le1/8\) for \(k\ge1\). For every even \(n\),
\[
b_n-b_{n+1}=\sum_{k\ge0}(4k+3)\lambda_{2k+1}^n(1-\lambda_{2k+1})>0,
\]
since \(\lambda_{2k+1}\le1/2<1\). For odd \(n\ge3\), the \(k=0\) term equals \(3/2^{n+1}\), whereas the absolute sum of the remaining terms is bounded by
\[
\frac98\left(\frac18\right)^{n-2}\sum_{k\ge1}(4k+3)c_k^2
=\frac9{32}\left(\frac18\right)^{n-2}
<\frac3{2^{n+1}}.
\]
The last inequality is valid for every \(n\ge3\). Hence \(b_n>b_{n+1}\), and therefore \(q_n<q_{n+1}\), for all \(n\ge3\). The Hilbert–Schmidt identity also implies \(|b_n|\le(1/2)^{n-2}\to0\). Strict increase and this limit give \(q_n<1/2\).

**4. Exact short-loop values and conditional laws.** For two signed spherical unit vectors with acute angle \(\theta\), a third independent uniform spherical vector lies in the symmetric difference of their positive hemispheres with probability \(\theta/\pi\). This is the elementary area of two spherical lunes. It proves the stated triangle conditional law. For four vertices, condition on opposite vertices \(X_1,X_3\): the two independent intermediate vertices produce independent signs, each with mean \(1-2\theta/\pi\). Therefore the conditional probability of a nontrivial four-edge loop is
\[
\frac{1-(1-2\theta/\pi)^2}{2}=2\frac\theta\pi\left(1-\frac\theta\pi\right).
\]
For independent uniform points of \(M\), the acute projective distance \(\theta\in[0,\pi/2]\) has density \(\sin\theta\), since \(|\langle X,Y\rangle|\) is uniform on \([0,1]\) in \(\mathbb R^3\). Direct integration gives \(\mathbb E\theta=1\) and \(\mathbb E\theta^2=\pi-2\). Substitution yields \(q_3=1/\pi\) and \(q_4=4/\pi^2\), providing a separate calculation of the first two spectral values.

**5. Sharp spectral remainder.** The two largest nonzero eigenvalue magnitudes are \(1/2\) (multiplicity \(3\)) and \(1/8\) with negative sign (multiplicity \(7\)). All remaining magnitudes are at most \(1/16\), and their squared-multiplicity sum is \(1-3/4-7/64=9/64\). Thus, for \(n\ge3\),
\[
\left|b_n-\frac3{2^n}-7\left(-\frac18\right)^n\right|
\le\frac9{64}\left(\frac1{16}\right)^{n-2}
=\frac{36}{16^n}.
\]
Dividing by two proves the claimed explicit error bound for \(q_n\).

## Verification
The accompanying reproducible `check.py` uses a separate Simpson integration of the first eight odd Legendre polynomials, separate evaluations of the triangle and quadrilateral constants, 13 finite-length spectral-tail diagnostics, and direct geodesic-lift Monte Carlo samples for five loop lengths. All checks succeeded. The infinite series, monotonicity for every integer \(n\ge3\), and remainder estimate are proved analytically above; finite diagnostics do not replace those proofs.

## Relationship to prior work
Glorieux and Yarmola (arXiv:2003.08190, first posted March 18, 2020) ask for the homotopy class of random shortest-geodesic triangles and calculate the probability on **flat tori**. Their universal cover, deck group, and Dirichlet overlap integral are different; their formula does not imply the projective-plane law here. Hubard, Kaluža, de Mesmay, and Tancer (arXiv:1602.06778, first posted February 22, 2016) study deterministic shortest-path embeddings and prove relevant existence statements for the round projective plane; they do not calculate probabilities of random geodesic loops. The elementary random-hyperplane sign-correlation identity and classical Funk–Hecke harmonic analysis underlie the proof but are not claimed as new. A previously recorded **flat-torus** many-vertex homotopy distribution likewise does not cover the positively curved projective plane. The claimed contribution is the complete projective-plane loop-length law, its strict ordering, and its sharp two-mode decay. Historical priority has not been independently certified.

## Limitations
Only the round \(\mathbb{RP}^{2}\), independent uniform vertices, and uniquely minimizing geodesics are treated. The polygon need not be embedded, and the result does not imply a distribution for geometric perimeter, area, self-intersections, or nonround projective metrics. The proof does not establish analogous spectral formulas for projective spaces of higher dimension. The literature comparison may miss differently titled results on products of random spherical signs; this remains a historical-priority risk.

## References
1. O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190 (first public posting 2020-03-18), https://arxiv.org/abs/2003.08190.
2. A. Hubard, V. Kaluža, A. de Mesmay, and M. Tancer, *Shortest path embeddings of graphs on surfaces*, arXiv:1602.06778 (first public posting 2016-02-22), https://arxiv.org/html/1602.06778v3.
3. The classical Funk–Hecke formula and spherical-harmonic addition theorem; used here with the standard probability-area normalization on \(S^2\).
