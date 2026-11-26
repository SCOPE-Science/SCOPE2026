# Cubic frequency law and Koopman spectrum of the outer annulus of an integrable square map

## Finding

For Ostrovski's continuous area-preserving square map at \(\theta=\pi/8\), let \(\Omega\) be its outer polygonally foliated annulus and \(\Gamma_r\), \(0<r\le1\), the invariant polygons specified below, with \(\Gamma_1\) the inner boundary. Their positive rotation number is
\[
 \rho(r)=\frac{r}{4(2+\sqrt2+(1-\sqrt2)r)},\qquad 0<\rho\le 1/12.
\]
For ordinary planar area \(m\) on \(\Omega\), the pushforward by the rotation-number map has density
\[
 \frac{d(\rho_*m)}{d\omega}=\frac{8}{[1+4(\sqrt2-1)\omega]^3},\qquad 0<\omega<1/12,
\]
with zero mass outside this interval. The normalized-area probability density is this expression divided by \(m(\Omega)=(11-7\sqrt2)/2\). Each reduced rational \(p/q\) in \((0,1/12]\) occurs on exactly one of these polygons, and every point of that polygon has least period \(q\).

On \(L^2(\Omega,m)\), the Koopman operator \(Uf=f\circ F\) has maximal spectral type \(\delta_1+\mathrm{Haar}\) (as a measure class). Its only eigenvalue is \(1\), with eigenspace the leafwise-constant functions. The orthogonal complement is absolutely continuous and of maximal type Haar; in particular there is no singular-continuous component. For any two \(L^2\) functions with zero conditional mean on almost every leaf, \(\langle f,U^ng\rangle\to0\).

## Map and scope

Set \(S=[0,1]^2\), \(s=\sqrt2/4\), \(t=(2-\sqrt2)/4\), \(\delta=1-2s=2t\), and \(R(x,y)=(1-y,x)\). Use \(E_1=(0,0),E_2=(1,0),E_3=(1,1),E_4=(0,1)\) and \(P_1=(s,t), P'_1=(1-s,t)\), with \(P_i=R^{i-1}P_1\), \(P'_i=R^{i-1}P'_1\). The map fixes \(E_i\), sends \(P_i\) to \(P'_i\), is affine on each triangle \(\triangle(E_i,E_{i+1},P_i)\) and \(\triangle(E_i,P_i,P_{i-1})\), and is the rotation by \(\pi/4\) about the center on the central quadrilateral. Indices are cyclic. The nine cells map to the primed triangulation with determinant one. This defines an orientation-preserving, area-preserving homeomorphism commuting with \(R\).

On the first bottom and corner triangles the formulas are \(A(x,y)=(x+2y,y)\) and
\[
 B=\begin{pmatrix}\tfrac12+\sqrt2 & \tfrac12-\tfrac{\sqrt2}2\\-\tfrac12+\tfrac{\sqrt2}2 & \tfrac12\end{pmatrix},
\]
respectively. Put \(v_0=P_4\), \(v_j=B^jv_0\) for \(1\le j\le3\). Direct multiplication gives
\[
 v_1=(t,s),\quad v_2=((\sqrt2-1)/2,(\sqrt2-1)/2),\quad v_3=P_1.
\]
The polygon \(\Gamma_r\) joins the marked points \(R^k(rv_j)\) in lexicographic \((k,j)\) order (collinear consecutive segments are allowed). Use this cyclic order for positive rotation. The open annulus lies between \(\partial S\) and \(\Gamma_1\). Boundaries do not affect the measure or spectral claims.

## Proof

**Foliation and invariance.** Within the first corner triangle, the rays to \(v_0,v_1,v_2,v_3\) are in strictly decreasing angular order, and each segment between consecutive points meets each intermediate ray exactly once. Scaling those segments by \(r\) gives disjoint arcs as \(r\) varies; they sweep the portion of that triangle between \(E_1\) and the chain for \(r=1\). In the bottom triangle, the segment \([rv_3,R(rv_0)]\) is exactly the slice at height \(rt\) (from \(rs\) to \(1-r(1-s)\)). The corner arcs and bottom slices therefore fit with their quarter-turn images to give disjoint simple nested polygons for \(0<r<1\) that exhaust \(\Omega\).

The first two corner segments map by \(B\) onto their successors. The last corner segment maps from \(rv_3\) to \(A(rv_3)=rv_3+(r\delta,0)\), since \(A\) and \(B\) agree on their common edge. The bottom segment then maps by \(A\) from \(A(rv_3)\) to \(R(rv_1)\). These two images concatenate into the horizontal arc from \(rv_3\) to \(R(rv_1)\). That arc is precisely \([rv_3,R(rv_0)]\) followed by \([R(rv_0),R(rv_1)]\), since \(v_0\) and \(v_1\) have the same first coordinate. The image join need not be the original join: it may be on either of the two collinear segments. It lies on the combined arc since \(r\delta\le(1-r)+r\delta\). Rotating the argument by quarter-turns proves invariance, including at \(r=1\) where the bottom segment collapses.

**Area coordinates and frequency.** On each corner segment use coordinates \(z=r[(1-u)v_j+uv_{j+1}]\), \(0<u<1\). The absolute Jacobian is \(r|\det(v_j,v_{j+1})|=r t\delta\), since \(\det B=1\) and \(\det(v_0,v_1)=-t\delta\). The bottom segment has strip mass per \(dr\) equal to \(t(1-r)\), its length times the derivative of its height. Thus the full mass per \(dr\) is
\[
 M(r)=4t[1+(3\delta-1)r]=(2-\sqrt2)+(7-5\sqrt2)r>0,
\]
and \(m(\Omega)=\int_0^1 M(r)\,dr=(11-7\sqrt2)/2\). These strip coordinates give a disintegration \(dm=M(r)\,dr\,d\mu_r\) with each \(\mu_r\) nonatomic, of full support and normalized. Since \(F\) preserves \(r\) and area, it preserves \(\mu_r\) for almost every \(r\) by uniqueness of disintegration. The preservation holds for every \(0<r\le1\): the integral against any continuous test function of both \(\mu_r\) and \(F_*\mu_r\) depends continuously on \(r\) by the segment parametrizations and weights, including zero weight for the collapsed bottom segment at \(r=1\).

The cumulative positive \(\mu_r\)-mass from \(rv_0\) is an orientation-preserving circle coordinate. An orientation- and measure-preserving circle homeomorphism in this coordinate is a translation, and its translation amount is the mass of the arc to \(F(rv_0)=rv_1\). Thus \(\rho(r)=r t\delta/M(r)\), the claimed formula. Writing \(c=2+\sqrt2\) and \(d=1-\sqrt2\), the derivative \(c/[4(c+dr)^2]\) is strictly positive, with limits \(\rho(0+)=0\) and \(\rho(1)=1/12\). Translation by reduced \(p/q\) has least period \(q\) at every point, including at the boundary leaf when \(p/q=1/12\).

**Pushforward and spectral type.** The substitution \(r=4c\omega/(1-4d\omega)\) has derivative \(4c/(1-4d\omega)^2\). If \(M(r)=M_0+M_1r\), then \(4cM_0=8\) and \(cM_1=dM_0\). Consequently \(M(r)\,dr=8(1-4d\omega)^{-3}\,d\omega\), with no atoms at the endpoints.

The cumulative-mass coordinate identifies \(F\) on the annulus with \((r,u)\mapsto(r,u+\rho(r))\) and area with \(M(r)\,dr\,du\). Fourier expansion in \(u\) reduces the Koopman operator on mode \(n\in\mathbb Z\) to multiplication by \(e^{2\pi i n\rho(r)}\). Mode zero gives precisely the leafwise-constant subspace. For each nonzero \(n\), the spectral measures are pushforwards of \(|g(r)|^2 M(r)\,dr\) under the displayed multiplier, and are absolutely continuous by the positive differentiable rotation-number density and the finite-to-one circle projection on the interval. The countable orthogonal sum remains absolutely continuous. In mode 12, the multiplier makes one full turn and the vector with \(g(r)=1\) has spectral measure equivalent to Haar. This proves the claimed maximal spectral type. The Riemann–Lebesgue lemma, applied to the absolutely continuous cross spectral measures on the orthogonal complement of mode zero, gives the correlation limit.

## Verification

The accompanying `verify_square.py` checks the algebraic vertex chain, determinant, horizontal edge endpoint identities, polygon area, and identities for the rotation law and change of variables using exact arithmetic in \(\mathbb Q(\sqrt2)\). The geometric argument for the combined horizontal arc is needed in addition to the endpoint tests. The infinite spectral claim follows from the area-coordinate and Fourier argument, not from finite orbit simulations.

## Relationship to prior work and limitations

Ostrovski proved the invariant polygonal foliation and the endpoint range in Theorem 5.1, Corollary 5.4 and Remark 5.5 of [1]; see also Theorem 5.9 and Corollary 5.12 of [2]. The paper and thesis describe linear variation in the segment coordinate between successive periodic leaves. For the physical coordinate \(rp_\mathrm{break}\), with \(p_\mathrm{break}=P_1\), the explicit formula here is strictly nonlinear: \(\rho''(r)=-cd/[2(c+dr)^3]\ne0\). Thus linear interpolation of the endpoint frequencies in that physical coordinate does not give the density. The total area is also given for this parameter by the area comparison [3], and [4] treats discrete sublevel areas for the periodic leaves and a slow-frequency asymptotic. The distinct calculation here is the frequency and area density throughout the interval and the maximal spectral type on this annulus. The Fourier-spectral method is standard. No claim is made about the spectral type of the whole square, other parameters, or exhaustive priority.

## References

1. G. Ostrovski, *Dynamics of a Continuous Piecewise Affine Map of the Square*, Physica D **271** (2014), 1–9, https://arxiv.org/abs/1305.4282.
2. G. Ostrovski, *Topics Arising from Fictitious Play Dynamics*, PhD thesis, University of Warwick (2013), Chapter 5, https://wrap.warwick.ac.uk/58894/.
3. *Quadratic vanishing of the unfoliated core in an integrable piecewise-affine square map*, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-quadratic-vanishing-of-the-unfoliated-core-in-an-integrable-piec--22de24ee92be.
4. *Exact slow-winding area law for the integrable Ostrovski square maps*, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-exact-slow-winding-area-law-for-the-integrable-ostrovski-square--9d9a41caf0a3.
