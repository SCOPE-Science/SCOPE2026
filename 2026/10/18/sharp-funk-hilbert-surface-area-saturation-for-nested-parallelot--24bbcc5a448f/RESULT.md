# Sharp Funk–Hilbert surface-area saturation for nested parallelotopes

## Finding
Let \(d\ge3\) be an integer, let \(K=b+T[-1,1]^d\) for an invertible real matrix \(T\), and let \(G_t=b+tT[-1,1]^d\) with \(0<t<1\). Write \(F_d(t)=\operatorname{area}^{F}_{K}(G_t)\) and \(H_d(t)=\operatorname{area}^{H}_{K}(G_t)\) for their Funk and Hilbert Holmes–Thompson hypersurface areas. Put \(m=d-1\), \(a=\operatorname{arctanh}t\), \(\omega_m=\pi^{m/2}/\Gamma(1+m/2)\), and \(\beta_m=2^{-m}\binom{2m}{m}\). Then
\[
F_d(t)=\frac{2d(4a)^m}{m!\,\omega_m},\qquad
1<\frac{H_d(t)}{F_d(t)}<\beta_m,
\qquad \lim_{t\uparrow1}\frac{H_d(t)}{F_d(t)}=\beta_m.
\]
The universal Rogers–Shephard/Faifman comparison factor is therefore optimal already inside this narrowly restricted class of nested parallelotopes, and is not attained at any \(t<1\). Moreover, when \(d=3\), the entire dependence on \(t\) is
\[
\frac{H_3(t)}{F_3(t)}=1+\frac{1}{a^2}\int_0^a u\tanh u\,du
=1+\int_0^1s\tanh(as)\,ds,
\quad F_3(t)=\frac{48a^2}{\pi}.
\]
This ratio is strictly increasing from \(1\) to \(3/2\), and
\[
\frac32-\frac{H_3(t)}{F_3(t)}\sim \frac{\pi^2}{24a^2}\qquad(t\uparrow1).
\]

## Assumptions and scope
All convex bodies are Euclidean full-dimensional and all hypersurface areas use the Holmes–Thompson normalization: at each smooth boundary point, the density is the \(m\)-dimensional volume of the tangent-plane projection of the polar Finsler unit ball, divided by \(\omega_m\). For a polytope the facet integrals define the area; its edges are null. Funk is nonreversible; Hilbert is its symmetric Finsler counterpart. All formulas are valid for all integers \(d\ge3\) and all real \(t\in(0,1)\). The two areas are affine invariant for this simultaneous transformation of ambient and enclosed bodies, so it suffices to take \(K=[-1,1]^d\) and \(G_t=tK\).

## Proof
**1. Local cotangent polytope.** At \(x\in\operatorname{int}K\), the Funk Finsler unit ball is \(K-x\); its polar is
\[
B_F^*(x)=\operatorname{conv}\left\{\frac{e_j}{1-x_j},\frac{-e_j}{1+x_j}:1\le j\le d\right\}.
\]
The Hilbert dual unit ball is \((B_F^*(x)-B_F^*(x))/2\) (Arya–Mount, Lemma 2.2). At either facet \(x_i=\pm t\) of the inner cube the tangent coordinates are the \(m\) indices different from \(i\). Orthogonal projection sends the vertices in direction \(i\) to zero and leaves the asymmetric cross-polytope
\[
P_m(z)=\operatorname{conv}\left\{\frac{e_j}{1-z_j},\frac{-e_j}{1+z_j}:1\le j\le m\right\},\qquad z\in(-t,t)^m.
\]
Projection commutes with Minkowski difference. Every orthant portion of \(P_m\) is an axis simplex. Summing their volumes gives
\[
|P_m(z)|=\frac{1}{m!}\prod_{j=1}^m\left(\frac1{1-z_j}+\frac1{1+z_j}\right)
=\frac{2^m}{m!\prod_{j=1}^m(1-z_j^2)}.
\]
Define the exact local ratio
\[
\rho_m(z)=\frac{|(P_m(z)-P_m(z))/2|}{|P_m(z)|}.
\]
There are \(2d\) facets; therefore the area formulas reduce to
\[
F_d(t)=\frac{2d}{\omega_m}\int_{[-t,t]^m}|P_m(z)|\,dz,
\quad\frac{H_d(t)}{F_d(t)}=
\frac{\int_{[-t,t]^m}|P_m(z)|\rho_m(z)\,dz}{\int_{[-t,t]^m}|P_m(z)|\,dz}.
\]
With \(z_j=\tanh u_j\), each factor \(dz_j/(1-z_j^2)=du_j\), the integration box becomes \([-a,a]^m\), and the displayed formula for \(F_d\) follows. The ratio becomes the uniform-cube average
\[
R_d(t):=\frac{H_d(t)}{F_d(t)}=
\frac{1}{(2a)^m}\int_{[-a,a]^m}\rho_m(\tanh u_1,\ldots,\tanh u_m)\,du.
\]

**2. Sharp all-dimensional upper limit.** The Rogers–Shephard difference-body inequality applied in dimension \(m\) gives \(1\le\rho_m(z)\le2^{-m}\binom{2m}{m}=\beta_m\). Equality on the right holds only for simplices, and equality on the left only for centrally symmetric convex bodies. For \(m\ge2\) and finite \(z\), the polytope \(P_m(z)\) has \(2m>m+1\) distinct vertices, hence is not a simplex. It is centrally symmetric precisely when every \(z_j=0\). Thus its local ratio is strictly between \(1\) and \(\beta_m\) for almost every point in the integration box; the same strict inequalities hold for \(R_d(t)\).

For every coordinate sign pattern \(s\in\{-1,1\}^m\), let \(z\to s\) from within \((-1,1)^m\). Reflect coordinate signs so that each \(z_j\to1\), then apply the invertible diagonal map with \(j\)-th scale \(1-z_j\) to \(P_m(z)\). Its positive vertex converges to \(e_j\), and its negative vertex converges to \(0\). The resulting polytopes converge in Hausdorff distance to the simplex \(\operatorname{conv}(0,e_1,\ldots,e_m)\). Because the difference-body volume ratio is continuous and affine invariant, \(\rho_m(z)\to\beta_m\) at every corner. If \(U_j\) are independent uniform variables on \([-a,a]\), then \(|U_j|\to\infty\) in probability as \(a\to\infty\) and \((\tanh U_j)_j\) approaches the set of cube corners in probability. The boundedness \(1\le\rho_m\le\beta_m\) proves by bounded convergence in probability that \(R_d(t)\to\beta_m\) as \(t\uparrow1\). This proves sharpness without asserting finite attainment.

**3. Complete dimension-three density.** Let \(m=2\), writing \(z=(y,w)\) and the four axial vertices of \(P_2\) as \((p,0),(0,q),(-r,0),(0,-s)\), where \(p=1/(1-y)\), \(r=1/(1+y)\), \(q=1/(1-w)\), \(s=1/(1+w)\). The polygon has \(|P_2|=(p+r)(q+s)/2\). Its oriented edge vectors are
\[
(-p,q),\quad(-r,-q),\quad(r,-s),\quad(p,s).
\]
For any planar polygon, its difference body is the zonotope generated by its oriented edge vectors: equality of support functions follows because both give the projection width in every direction. The planar zonotope area is the sum of absolute determinants over unordered pairs of generators. Hence
\[
\left|\frac{P_2-P_2}{2}\right|
=\frac12(p+r)(q+s)+\frac14\bigl(|ps-qr|+|pq-rs|\bigr).
\]
Using \((p+r)(q+s)=4/((1-y^2)(1-w^2))\), \(ps-qr=2(y-w)/((1-y^2)(1-w^2))\) and \(pq-rs=2(y+w)/((1-y^2)(1-w^2))\), one gets
\[
\rho_2(y,w)=1+\frac{|y-w|+|y+w|}{4}
=1+\frac12\max(|y|,|w|).
\]
For independent \(U,V\) uniform on \([-a,a]\), the maximum of \(|U|,|V|\) has density \(2u/a^2\) on \([0,a]\). Consequently
\[
R_3(t)=1+\frac{1}{2}\mathbb E\max(|\tanh U|,|\tanh V|)
=1+\frac1{a^2}\int_0^a u\tanh u\,du.
\]
Differentiating its unit-interval representation yields \(\frac{d}{da}R_3=\int_0^1s^2\operatorname{sech}^2(as)\,ds>0\). The limit as \(a\to\infty\) is \(1+\int_0^1s\,ds=3/2\). Finally
\[
\frac32-R_3(t)=\frac1{a^2}\int_0^a u(1-\tanh u)\,du,
\quad\int_0^\infty u(1-\tanh u)\,du=\frac{\pi^2}{24},
\]
where the last identity follows by the substitution \(v=2u\) and the standard alternating-series evaluation of \(\int_0^\infty v/(1+e^v)\,dv=\pi^2/12\). This proves the stated asymptotic.

## Verification
The standalone standard-library checker `VERIFY.py` carries out \(49\) exact rational two-dimensional polar/difference-body volume checks, and compares independent midpoint double integration against the one-dimensional formula at four values of \(t\). It confirms the intermediate \(m=2\) identity without relying on the algebra in the preceding derivation. These finite tests are not used to establish the general-dimensional limit, for which the analytic Hausdorff convergence and boundedness argument is essential. Reproduce with `python VERIFY.py`.

## Relationship to prior work
Arya and Mount (2026, arXiv:2601.16468, Theorem 1 and Corollary 5.1) establish a Funk Holmes–Thompson Cauchy formula and the dimension-only Hilbert-versus-Funk comparison \(1\le H/F\le\beta_m\); their bound is a premise here and is not claimed as new. Their full arXiv text gives planar equality and ellipsoidal equality, but no concentric-homothetic-parallelotope ratio profile or sharp saturation construction. Faifman (2020/2023) treats Funk/Hilbert volume phenomena and difference-body inequalities; the specific parallelotope hypersurface profile is not a consequence of the inspected volume statements alone. The classical Rogers–Shephard theorem supplies the sharp local simplex inequality and its equality cases; the new content is its realization as an integrated boundary limit of a nested symmetric-polytope family and the exact, strictly monotone spatial profile.

## Limitations
This does not prove that the upper comparison constant is attained by any fixed pair: in fact it is strict throughout the stated class at finite \(t\). No monotonicity is asserted for \(d\ge4\), and no formula for \(H_d(t)\) more elementary than the displayed cross-polytope integral is claimed in general. The historical-priority comparison is limited to the cited full primary text and searched records; earlier uncatalogued treatments of Funk/Hilbert parallelotopes remain a possible risk. Independent audit has not been performed.

## References
1. S. Arya and D. M. Mount, *Cauchy’s Surface Area Formula in the Funk Geometry*, arXiv:2601.16468 (first version 2026-01-23); SoCG 2026, LIPIcs 367, article 8, DOI: 10.4230/LIPIcs.SoCG.2026.8.
2. D. Faifman, *A Funk perspective on billiards, projective geometry and Mahler volume*, arXiv:2012.12159 (2020).
3. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Arch. Math. 8 (1957), 220–233; the classical sharp difference-body inequality and equality criterion.
