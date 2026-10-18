# Universal two-term diameter tails from polytope vertex cones

## Finding
Let \(K\subset\mathbb R^d\) be any full-dimensional convex polytope, \(d\ge2\), of volume \(V\) and diameter \(D\). For independent uniform \(X,Y\in K\), the upper tail of Euclidean pair distance has an exact first two terms:
\[
\Pr\{\|X-Y\|>D-\varepsilon\}=C_0\varepsilon^{2d}+C_1\varepsilon^{2d+1}+O_K(\varepsilon^{2d+2}),\qquad\varepsilon\downarrow0.
\]
The coefficients are finite sums over diametral vertex pairs, requiring only three low-order moments of their inward tangent cones. Both coefficients are strictly positive. In particular, the second term resolves the transverse geometry that is invisible to the first-order pointed-cap limit.

For each **unordered** diametral pair \(\{p,q\}\) of vertices, temporarily choose an order and put \(e=(q-p)/D\) and \(\Pi_e=I-ee^{\mathsf T}\). At \(p\), let \(T_p=\operatorname{cone}(K-p)\), \(\ell_p(u)=e\cdot u\); at \(q\), set \(T_q=\operatorname{cone}(K-q)\), \(\ell_q(v)=-e\cdot v\). Define the bounded cap \(S_p=\{u\in T_p:\ell_p(u)\le1\}\), likewise \(S_q\). Define their transverse moment data
\[
 A_p=\int_{S_p}du,\qquad M_p=\int_{S_p}\Pi_e u\,du,\qquad Q_p=\int_{S_p}\|\Pi_e u\|^2du,
\]
with analogous definitions at \(q\), using the **same** transverse projection \(\Pi_e\) and inward coordinates at both vertices. Then, with \(\Gamma\) the usual gamma function, put
\[
 B_{pq}=\frac{\Gamma(d+3)\Gamma(d+1)}{\Gamma(2d+3)}(Q_pA_q+A_pQ_q)
 -\frac{2\Gamma(d+2)^2}{\Gamma(2d+3)} M_p\cdot M_q.
\]
The promised coefficients are
\[
 \boxed{C_0=\frac{2}{V^2}\frac{\Gamma(d+1)^2}{\Gamma(2d+1)}\sum_{\{p,q\}}A_pA_q},
 \qquad
 \boxed{C_1=\frac{2(d+1)}{DV^2}\sum_{\{p,q\}}B_{pq}}.
\]
Both formulas are order-independent. Neither assumes simplicial tangent cones, a unique diametral pair, central symmetry, or general position.

## Assumptions and scope
The polytope is compact and has positive \(d\)-volume. Its diameter is its *Euclidean* diameter. The variable \(\varepsilon\) is a positive length below the diameter, and both points are independently volume-uniform. The finite set of diametral pairs consists exactly of vertex pairs at separation \(D\): strict convexity of the Euclidean norm excludes positive-dimensional continua of maximizers on a polytope.

For any such pair and nonzero \(u\in T_p\), the linear functional \(\ell_p(u)>0\), and analogously at \(q\). Indeed, for a vertex-ray generator \(u=z-p\) with \(z\in K\), the inequality \(\|q-(p+tu)\|\le D\) for sufficiently small positive \(t\) implies \(2Dt\,e\cdot u\ge t^2\|u\|^2\), and hence positive projection; finitely many extremal rays extend this to the full pointed cone. Thus all caps and moments above are finite.

## Proof
**1. Localization.** The pair-distance maximum on \(K\times K\) occurs only at finitely many ordered vertex pairs. For any fixed sufficiently small neighborhoods of them, compactness supplies a positive distance deficit on their complement. In each such neighborhood, the polytope agrees with the translate of the corresponding tangent cone. Since the positive projections bound the inward displacement by a constant times the distance deficit, all contributing points are within \(O(\varepsilon)\) of their vertices. The neighborhoods can be chosen disjoint so there is no double-counting.

**2. A universal local level.** At a fixed ordered pair write \(x=p+u\), \(y=q+v\). Put \(s=\ell_p(u)+\ell_q(v)\) and \(w=\Pi_e(v-u)\). The exact identity
\[
 \|y-x\|^2=(D-s)^2+\|w\|^2
\]
holds. For small displacements, the tail condition is equivalent to
\[
 2D(\varepsilon-s)+(s^2+\|w\|^2-\varepsilon^2)>0.
\]
Rescale \((u,v)=\varepsilon(U,W)\). The sum \(S=\ell_p(U)+\ell_q(W)\) is positive on every nonzero vector in the product cone. Its unit section is compact. Parameterize each ray by \((U,W)=tz\), with \(S(z)=1\). Writing \(H(z)=\|\Pi_e(z_q-z_p)\|^2\), the exact section inequality becomes
\[
 2D(1-t)+\varepsilon\bigl(t^2(1+H(z))-1\bigr)>0.
\]
Uniform implicit differentiation on the compact unit section gives a unique positive radial threshold
\[
 t_*(z,\varepsilon)=1+\frac{H(z)}{2D}\varepsilon+O_K(\varepsilon^2).
\]
The radial Jacobian is \(t^{2d-1}\), so the volume of allowed \((U,W)\) equals the unperturbed volume plus
\[
 \frac{\varepsilon}{2D}\int_{S=1}\frac{H}{\|\nabla S\|}\,d\mathcal H^{2d-1}+O_K(\varepsilon^2).
\]
Here the section is taken inside the product cone; the coarea integral equivalently equals \(2d+2\) times the integral of \(H\) over \(S\le1\), by homogeneity degree two. The section may have corners, but radial integration is valid for polyhedral cones, giving a uniform remainder.

**3. Evaluation of the cap moments.** Scaling gives \(\operatorname{vol}\{u\in T_p:\ell_p(u)\le t\}=A_pt^d\), \(\int\Pi_eu\,du=M_pt^{d+1}\) and \(\int\|\Pi_eu\|^2du=Q_pt^{d+2}\) on those caps. Beta integration over \(\ell_p(U)+\ell_q(W)\le1\) therefore gives
\[
 \int 1=\frac{\Gamma(d+1)^2}{\Gamma(2d+1)}A_pA_q
\]
and
\[
 \int\|\Pi_e(W-U)\|^2
 =\frac{\Gamma(d+3)\Gamma(d+1)}{\Gamma(2d+3)}(Q_pA_q+A_pQ_q)
 -\frac{2\Gamma(d+2)^2}{\Gamma(2d+3)}M_p\cdot M_q=B_{pq}.
\]
Thus the local **ordered-pair** contribution is \(\varepsilon^{2d}\bigl(\Gamma(d+1)^2 A_pA_q/\Gamma(2d+1)+(d+1)B_{pq}\varepsilon/D+O_K(\varepsilon^2)\bigr)\). Sum over the two orderings of every unordered pair and divide by \(V^2\), proving both displayed formulas. Since the transverse difference is nonzero on a set of positive product-cone volume in every dimension at least two, \(B_{pq}>0\); the positivity of \(C_0\) is immediate.

## Verification
For the rectangle \(K=[0,a]\times[0,b]\), write \(D=\sqrt{a^2+b^2}\). There are two unordered diametral pairs, with equal cone data after symmetries. At one corner
\[
 A=\frac{D^2}{2ab},\quad M=\frac A3\left(\frac ab-\frac ba\right)n,\quad Q=\frac A6\left(\frac{b^2}{a^2}+\frac{a^2}{b^2}-1\right),
\]
where \(n=(-b,a)/D\) is transverse; at the opposite corner the transverse first moment is \(-M\). Consequently
\[
 C_0=\frac{2A^2}{3a^2b^2},\qquad C_1=\frac{12}{Da^2b^2}\left(\frac{2AQ}{15}+\frac{\|M\|^2}{10}\right).
\]
For the unit square this is the concrete expansion
\[
 \Pr\{\|X-Y\|>\sqrt2-\varepsilon\}=\frac23\varepsilon^4+\frac{4}{15\sqrt2}\varepsilon^5+O(\varepsilon^6).
\]
An **independent** exact one-dimensional integral, valid for sufficiently small \(\varepsilon>0\), follows from the product triangular densities of two rectangle coordinate differences. Put
\[
 x_*=a-\sqrt{(D-\varepsilon)^2-b^2},\qquad y_*(x)=b-\sqrt{(D-\varepsilon)^2-(a-x)^2}.
\]
Then
\[
 \Pr\{\|X-Y\|>D-\varepsilon\}=\frac2{a^2b^2}\int_0^{x_*}x\,[y_*(x)]^2\,dx.
\]
The standalone script `verify_tail.py` evaluates this independent integral at high precision for three aspect ratios, verifies the cap-moment formulas and checks numerical convergence of the fifth-order quotient to its predicted coefficient. It reports `DIAMETER_TAIL_CHECK_OK` when successful. Numerical tests are evidence for these benchmark examples, not a substitute for the all-dimensional cone proof.

## Relationship to prior work
Mayer and Molchanov (2006) investigate asymptotic extrema of random-sample diameters, including first-order pointed-cap limit laws. The present statement instead concerns the **two-point** distance survival probability in every polytopal dimension and computes both its first and its transverse second coefficient, without a unique diametral pair assumption.

Tong and Pan (2016) give a kinematic-measure algorithm for the **complete planar polygonal pair-distance distribution**, building from triangles. Their algorithm subsumes numerical or symbolic evaluation of the entire two-dimensional distribution, including planar tail coefficients in principle; the planar square benchmark is therefore not separately presented as a newly discovered distribution. Their text does not state the all-dimensional vertex-cone second-term formula. Pure–Durrani–Tong–Pan (2019) subsequently provide a general planar polar-decomposition method for the whole polygonal distance density; that stronger planar coverage is also acknowledged and does not supply the all-dimensional local cone expression. Ruben (1978) described related planar polygon-distance methods, but its full text could not be inspected here. No unconditional claim of historical priority is made.

## Limitations
This is an asymptotic statement for a fixed full-dimensional **polytope**, not an arbitrary smooth convex body, a non-Euclidean norm, or the distribution of the diameter of a many-point sample. The \(O_K\)-constant need not be uniform as the shape varies. The cap moments are finite-dimensional geometric integrals and are not necessarily rational for arbitrary polytope coordinates. The result is verified analytically here but has **not** undergone independent mathematical audit. Earlier generalized distance-distribution formulas may imply selected special cases, and uninspected literature remains a historical-priority risk.

## References
Mayer, M. and Molchanov, I. (2006), *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*. arXiv:math/0605289, https://arxiv.org/pdf/math/0605289 .

Tong, F. and Pan, J. (2016), *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*. arXiv:1602.03407, https://arxiv.org/pdf/1602.03407 .

Ruben, H. (1978), *On the Distance Between Points in Polygons*. https://doi.org/10.1007/978-3-642-93089-8_5 (full text not inspected).

Pure, R., Durrani, S., Tong, F. and Pan, J. (2021), *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*. arXiv:1903.07757, https://arxiv.org/abs/1903.07757 (full text not inspected; subsequent general planar treatment).
