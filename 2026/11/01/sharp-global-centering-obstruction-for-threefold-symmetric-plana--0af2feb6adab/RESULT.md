# Sharp global-centering obstruction for threefold-symmetric planar shadows

## Finding

For a unit vector \(n\in S^2\), write \(P_n=I-nn^{\mathsf T}\) for orthogonal projection onto \(n^\perp\). Let \(H:\mathbb R^3\to\mathbb R\) be a real homogeneous harmonic polynomial of degree three, and suppose \(1+\varepsilon H\) restricted to \(S^2\) is the support function of a convex body \(K_{H,\varepsilon}\), where \(\varepsilon\ne0\). Denote by \(c_{H,\varepsilon}(n)\in n^\perp\) the unique center of threefold rotation of the projected planar body \(K_{H,\varepsilon}|n^\perp\). Then
\[
\boxed{c_{H,\varepsilon}(n)=-\frac{\varepsilon}{4}P_n\nabla H(n).}
\]
This is also the Steiner point of that planar shadow. If \(H\not\equiv0\), there is no fixed \(a\in\mathbb R^3\) with \(c_{H,\varepsilon}(n)=P_na\) for every \(n\). In fact, with \(d\omega\) normalized spherical area measure,
\[
\boxed{\int_{S^2}\|c_{H,\varepsilon}(n)-P_na\|^2\,d\omega(n)
=\frac{3\varepsilon^2}{4}\int_{S^2}H(n)^2\,d\omega(n)+\frac23\|a\|^2.}
\]
Thus \(a=0\) uniquely minimizes the mean-square failure of a common three-dimensional projection center for every nonzero harmonic cubic.

For the canonical exceptional family \(H(x)=x_1x_2x_3\), write \(K_\varepsilon=K_{H,\varepsilon}\). Its shadow centers have the explicit field
\[
\boxed{c_\varepsilon(n)=-\frac{\varepsilon}{4}
\left((n_2n_3,n_1n_3,n_1n_2)-3n_1n_2n_3n\right).}
\]
Every admissible \(\varepsilon\ne0\) has the **sharp uniform centering obstruction**
\[
\boxed{\inf_{a\in\mathbb R^3}\ \sup_{n\in S^2}
\|c_\varepsilon(n)-P_na\|=\frac{|\varepsilon|}{8},}
\]
with the **unique** optimal common center \(a=0\). Its full equality and vanishing sets are:

- \(\|c_\varepsilon(n)\|=|\varepsilon|/8\) precisely at the 12 oriented normals obtained by permuting \((\pm1,\pm1,0)/\sqrt2\);
- \(c_\varepsilon(n)=0\) precisely at the six signed coordinate axes and eight signed body diagonals, giving seven unoriented planes.

The exact average is
\[
\boxed{\int_{S^2}\|c_\varepsilon(n)-P_na\|^2\,d\omega(n)
=\frac{\varepsilon^2}{140}+\frac23\|a\|^2.}
\]
The source's qualitative phrase “up to translation” therefore has a strictly positive, sharp quantitative obstruction to being realized by *one* global translation.

## Assumptions and scope

All space and plane norms are Euclidean. The planes pass through the chosen ambient origin, and \(n\) and \(-n\) represent the same plane; the center field is even under this change. The convex bodies are smooth support perturbations \(h(u)=1+\varepsilon H(u)\) with \(H\) homogeneous harmonic cubic, and the geometric conclusions require the stated support-function hypothesis. It holds for all sufficiently small \(|\varepsilon|>0\) for any fixed \(H\). In the coordinate-product family, an entirely elementary sufficient range is \(0<|\varepsilon|\le1/4\), since \(\|D^2H\|_{\rm op}\le\sqrt2\), \(2|H|\le2/(3\sqrt3)\) on \(S^2\), and hence the support curvature-radius operator \(I+\varepsilon(\nabla^2_{S^2}H+HI)\) is positive definite in that range. The sharp admissible parameter range is not asserted as a new result.

The normalized measure \(d\omega\) has total mass one. A “common center” means a single point \(a\) of ambient space whose orthogonal projection equals the center of each corresponding planar shadow. The variational problem permits arbitrary \(a\in\mathbb R^3\), not just points inside the convex body.

## Proof

**1. Planar first-mode identity.** Fix \(n\in S^2\), put \(P=n^\perp\), and restrict \(H\) to \(P\). Every homogeneous planar cubic decomposes uniquely as \(T_3(y)+\|y\|^2\ell(y)\), where \(T_3\) is planar harmonic of degree three and \(\ell\) is linear. Since \(\Delta_P(\|y\|^2\ell(y))=8\ell(y)\),
\[
\ell(y)=\frac18\Delta_PH(y)=-\frac18D^2H(y)[n,n]
=-\frac14\langle\nabla H(n),y\rangle,\qquad y\in P.
\]
The middle equality uses the ambient harmonicity \(\Delta H=0\); the last uses the symmetry of the cubic polarization and Euler's identity \(D^2H(n)n=2\nabla H(n)\). On the unit circle of \(P\), \(T_3\) is a pure third harmonic while \(\ell\) is exactly the first harmonic. Thus the planar support function is \(1+\varepsilon T_3+\varepsilon\ell\); its unique threefold-rotation center and its Steiner point both equal the vector representing \(\varepsilon\ell\). This proves the first boxed identity. The uniqueness follows because a bounded planar body cannot be invariant under a nontrivial rotation around two distinct centers (the composition yields a nonzero translation).

**2. Universal mean-square identity.** For any spherical degree-three harmonic, \(-\Delta_{S^2}H=12H\). Integration by parts yields
\[
\int_{S^2}\|\nabla_{S^2}H\|^2d\omega=12\int_{S^2}H^2d\omega.
\]
Moreover \(\int_{S^2}\nabla_{S^2}H\,d\omega=2\int_{S^2}H(n)n\,d\omega=0\), by integration by parts with tangent vector field \(P_na\) and the orthogonality of degrees one and three. Finally \(\int P_n\,d\omega=(2/3)I\), so the mixed term vanishes and the displayed mean-square formula follows. If one \(a\) projected to every planar center, its mean-square residual would be zero; the right side is strictly positive for every nonzero \(H\), a contradiction.

**3. Explicit coordinate-product field and zero set.** For \(H(n)=n_1n_2n_3\), \(\nabla H(n)=(n_2n_3,n_1n_3,n_1n_2)\) and \(n\cdot\nabla H(n)=3n_1n_2n_3\). This gives the stated field. Put \(p=n_1^2\), \(q=n_2^2\), \(r=n_3^2\), with \(p+q+r=1\). Direct expansion yields
\[
\frac{16}{\varepsilon^2}\|c_\varepsilon(n)\|^2
=pq+qr+rp-9pqr=:F(p,q,r).
\]
If one coordinate is zero, the field vanishes precisely when another is zero, giving the six oriented coordinate axes. If all coordinates are nonzero, the condition \(P_n\nabla H(n)=0\) makes \(n_2n_3/n_1=n_1n_3/n_2=n_1n_2/n_3\); hence \(p=q=r=1/3\), giving the eight oriented body diagonals. These exhaust the zeros.

**4. Sharp maximum.** Let \(t=\min\{p,q,r\}\), say \(r=t\), so \(p+q=1-t\) and \(pq\le(1-t)^2/4\). When \(0\le t\le1/9\),
\[
F=(1-9t)pq+t(1-t)
\le\frac{(1-t)(1-3t)^2}{4}\le\frac14.
\]
The last expression decreases strictly on \((0,1/9]\), so equality requires \(t=0\) and \(p=q=1/2\). When \(t>1/9\), the coefficient of \(pq\) is negative, and
\[
F\le t(1-t)\le\frac29<\frac14
\]
because \(t\le1/3\). Thus \(\max F=1/4\), with exactly the 12 asserted oriented normals, proving \(\sup\|c_\varepsilon\|=|\varepsilon|/8\).

**5. Global minimax center and exact dispersion.** Fix any \(a\in\mathbb R^3\) and coordinate \(i\). Choose two normals with \(n_i=0\) and their other two coordinates \((1,\pm1)/\sqrt2\). Their centers are \(\mp\varepsilon e_i/8\). Because the \(i\)-th coordinate of \(P_na\) is always \(a_i\) at both normals,
\[
\sup_{n\in S^2}\|c_\varepsilon(n)-P_na\|
\ge\max\{|a_i+\varepsilon/8|,|a_i-\varepsilon/8|\}
=|a_i|+|\varepsilon|/8.
\]
Taking the maximum over \(i\) gives the stronger certificate
\[
\sup_{n\in S^2}\|c_\varepsilon(n)-P_na\|
\ge |\varepsilon|/8+\|a\|_\infty.
\]
The maximum computed in Step 4 shows \(a=0\) attains the required infimum and is its unique minimizer. Finally spherical moment integration gives \(\int H(n)^2d\omega=\int n_1^2n_2^2n_3^2d\omega=1/105\). Substitution in Step 2 produces \(\varepsilon^2/140+(2/3)\|a\|^2\).

## Verification

Run `python3 verify_centers.py` with Python 3's standard library. The verifier checks 17,977 exact-rational inequalities, Fourier-coefficient identities on sampled orthogonal frames (including another independent harmonic cubic), threefold symmetry after recentering, all stated extremal and zero orbits, the two-orientation minimax certificate, exact sphere moments, and an independently sampled numerical mean-square estimate. Its completed execution reported `PASS: 17977 deterministic rational, Fourier, symmetry, minimax, and stochastic checks`. These finite tests corroborate the explicit formulas; the analytic arguments above prove the universal assertions. No unbounded search, numerical optimization, or external certificate is used in the proof.

## Relationship to prior work

Myroshnychenko, Ryabogin, and Saroglou [1, Proposition 5.1 and Theorem 5.4] prove the qualitative threefold symmetry *up to translation* for the cubic exception; they identify the degree-one and degree-three circle modes but leave the plane-dependent translation vectors unspecified. Their finding is the direct motivation and is not claimed here. The classical planar Steiner-point/Fourier formula is likewise prior knowledge [2]. Earlier calculations for the same family determine its sharp convexity threshold [3] and directional projected-area profile [4]; neither statement determines the full shadow-center field, its exceptional zero/maximal plane configurations, or the sharp global minimax alignment and mean-square obstruction.

The new comparison is at the statement level: a result about permissible plane-by-plane translations does not imply that their centers form a projected fixed point, nor does an area formula locate the projection center. The present proof solves these questions exactly. Search coverage does not establish absolute historical uniqueness; classical Steiner-point integral transforms remain an identified priority risk.

## Limitations

The sharp \(L^\infty\) constant and 14/12 normal-orbit classifications concern the coordinate-product cubic, not every degree-three spherical harmonic. The general harmonic-cubic part establishes the center field and the \(L^2\) identity only. The results are three-dimensional, require Euclidean orthogonal projection and a genuine support function, and say nothing about arbitrary support perturbations or higher-dimensional shadows. Independent mathematical validation and exhaustive historical priority assessment have not been performed.

## References

1. S. Myroshnychenko, D. Ryabogin and C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1, first public 2026-09-23, especially Section 5.
2. C. Thäle, *A note on a problem posed by Linderholm*, *Journal of Geometry* (2025), DOI: 10.1007/s00022-025-00783-4, Section 1 (Steiner-point Fourier formula).
3. *Sharp convexity threshold for the cubic constant-width support family*, publicly indexed geometric result, 2026-10-04, identifier `b3681da24cdc`.
4. *Exact brightness profile of the cubic threefold-projection exception*, publicly indexed geometric result, 2026-10-11, identifier `a6ac80c263be`.
