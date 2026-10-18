# Cubic frequency law and Koopman spectrum of an integrable polygonal square map

## Finding

For the nine-piece continuous area-preserving square map at the parameter \(\theta=\pi/8\) introduced by Ostrovski, the outer polygonally foliated annulus \(\Omega\) has an **exact angular rotation law**, an **exact cubic probability-density law for rotation rates**, and **maximal Koopman spectral type equal to a point mass at one plus Haar measure**. More precisely, for the polygonal leaf \(\Gamma_r\), \(0<r\le1\),
\[
\rho(r)=\frac{r}{4(2+\sqrt2+(1-\sqrt2)r)},\qquad 0<\rho\le\frac1{12}.
\]
If \(m\) is unnormalized planar Lebesgue area on \(\Omega\), the pushforward of \(m\) by the leafwise rotation-number map has density
\[
\boxed{\frac{d(\rho_*m)}{d\omega}=\frac{8}{[1+4(\sqrt2-1)\omega]^3},\quad 0<\omega<1/12.}
\]
The outer annulus has area \(m(\Omega)=(11-7\sqrt2)/2\); dividing the boxed expression by this area gives its probability density. All \(0<p/q\le1/12\) (lowest terms) occur on exactly one leaf, every point of which has least period \(q\). The Koopman operator \(Uf=f\circ F\) on \(L^2(\Omega,m)\) has only the eigenvalue \(1\), with the entire leafwise-constant subspace as its eigenspace. Its remaining maximal spectral type is Haar measure on the unit circle, with no singular-continuous or other point spectrum. Correlations of observables with zero conditional mean on every leaf tend to zero.

## Assumptions and scope

Define \(S=[0,1]^2\), \(s=\sqrt2/4\), \(t=(2-\sqrt2)/4\), and \(R(x,y)=(1-y,x)\). Label the corners counterclockwise \(E_1=(0,0),E_2=(1,0),E_3=(1,1),E_4=(0,1)\). Define four interior break points \(P_1=(s,t)\), \(P_2=(1-t,s)\), \(P_3=(1-s,1-t)\), \(P_4=(t,1-s)\), and image points \(P'_1=(1-s,t)\), \(P'_2=(1-t,1-s)\), \(P'_3=(s,1-t)\), \(P'_4=(t,s)\). The map \(F:S\to S\) fixes the four \(E_i\), maps each \(P_i\) to \(P'_i\), is affine on the four triangles \(\triangle(E_i,E_{i+1},P_i)\) and on the four triangles \(\triangle(E_i,P_i,P_{i-1})\) (indices modulo four), and maps the central four-sided cell affinely by rotation through \(\pi/4\) about \((1/2,1/2)\). Its defining triangulation maps to the corresponding primed triangulation; all nine Jacobian determinants are \(1\). In particular it is a well-defined area-preserving orientation-preserving homeomorphism commuting with \(R\).

Set \(v_0=P_4\) and \(B=\begin{pmatrix}\tfrac12+\sqrt2&\tfrac12-\tfrac{\sqrt2}{2}\\-\tfrac12+\tfrac{\sqrt2}{2}&\tfrac12\end{pmatrix}\), and let \(v_j=B^jv_0\) for \(j=1,2,3\). The matrix \(B\) is the linear formula for \(F\) on the triangle \(\triangle(E_1,P_4,P_1)\). Exact evaluation gives
\[
v_1=(t,s),\quad v_2=((\sqrt2-1)/2,(\sqrt2-1)/2),\quad v_3=(s,t).
\]
For \(0<r\le1\), \(\Gamma_r\) is the closed polygon whose cyclic vertices are \(R^k(rv_j)\) for \(k=0,1,2,3\) and \(j=0,1,2,3\) in lexicographic order; the last vertex is joined to the first. Some adjacent edges merge at \(r=1\). These are nested invariant simple polygons. Write \(\Omega\) for the open region between \(\partial S\) and \(\Gamma_1\); adjoining or excluding either bounding polygon changes no area or \(L^2\) claim. The word *rotation number* refers to the positive orientation induced by this cyclic order.

## Proof

**1. Invariant foliation and its exact area.** On \(\triangle(E_1,P_1,E_2)\), the affine map is \(A(x,y)=(x+2y,y)\). The first three consecutive polygon edges starting at \(rv_0\) lie in the \(B\) cell. Their images advance by one edge, while the last such edge maps to the initial horizontal portion of the next edge. Indeed, with \(\delta=1-2s\),
\[
B^3v_0=v_3,\quad A(rv_3)=rv_3+(r\delta,0),\quad A(R(rv_0))=R(rv_1).
\]
Consequently the remaining horizontal edge maps across the rest of that edge and the next one, and the four rotated copies close the invariant polygon. Since the vertices depend affinely on \(r\), the polygons are nested and exhaust \(\Omega\) as \(r\downarrow0\). Shoelace evaluation gives
\[
\operatorname{area}(\operatorname{int}\Gamma_r)=1-(2-\sqrt2)r+\frac{5\sqrt2-7}{2}r^2.
\]
Differentiating the area outside \(\Gamma_r\) gives the positive leaf-area density
\[
M(r)= (2-\sqrt2)+(7-5\sqrt2)r,\qquad m(\Omega)=\int_0^1M(r)\,dr=\frac{11-7\sqrt2}{2}.
\]
This is also an explicit disintegration \(dm=M(r)\,dr\,d\mu_r\), with \(\mu_r\) a normalized, full-support, nonatomic, leafwise invariant measure.

**2. Exact twist.** The area strip on the first \(B\)-edge \([rv_0,rv_1]\) has mass per \(dr\)
\[
m_B(r)=r\,t(1-2s)=r\,t\delta.
\]
Area preservation makes the next two \(B\)-edges have the same conditional mass. The horizontal edge \([rv_3,R(rv_0)]\) has constant height \(rt\), Euclidean length \(1-r\), hence strip mass \(m_A(r)=t(1-r)\). Fourfold symmetry yields \(M(r)=4(3m_B(r)+m_A(r))\). The conditional invariant measure \(\mu_r\) carries the positively oriented arc from \(rv_0\) to \(F(rv_0)=rv_1\) with mass \(m_B(r)/M(r)\). Cumulative \(\mu_r\)-mass is a circle coordinate in which \(F\) is translation by this mass, since \(F\) preserves \(\mu_r\) and orientation. Substitution gives
\[
\rho(r)=\frac{m_B(r)}{M(r)}=\frac{r}{4(2+\sqrt2+(1-\sqrt2)r)}.
\]
The derivative is \((2+\sqrt2)/\{4[2+\sqrt2+(1-\sqrt2)r]^2\}>0\). Thus \(\rho(0+)=0\) and \(\rho(1)=1/12\), and a reduced rational \(p/q\) corresponds to the unique
\[
r=\frac{4(2+\sqrt2)(p/q)}{1-4(1-\sqrt2)(p/q)}.
\]
Translation by \(p/q\) on the leaf proves its least period is exactly \(q\).

**3. Cubic frequency law.** Write \(c=2+\sqrt2\), \(d=1-\sqrt2\), so \(\rho=r/[4(c+dr)]\). Then \(r=4c\omega/(1-4d\omega)\) and \(dr/d\omega=4c/(1-4d\omega)^2\). The identities \(4c(2-\sqrt2)=8\) and \(c(7-5\sqrt2)=d(2-\sqrt2)\) give
\[
M(r(\omega))\frac{dr}{d\omega}=\frac{8}{(1-4d\omega)^3}
=\frac8{[1+4(\sqrt2-1)\omega]^3}.
\]
No probabilistic approximation or discretized sampling enters this identity.

**4. Full Koopman spectral type on \(\Omega\).** In cumulative conditional-area coordinate \(u\in\mathbb R/\mathbb Z\), the normalized system is measurably equivalent to \((r,u)\mapsto(r,u+\rho(r))\) with measure \(M(r)dr\,du\). Fourier decomposition in \(u\) reduces \(U\) to the direct sum of multiplication operators \(g(r)\mapsto e^{2\pi i n\rho(r)}g(r)\), for \(n\in\mathbb Z\). The \(n=0\) summand is the eigenvalue \(1\). For every \(n\ne0\), strict monotonicity and positive differentiable density imply all spectral measures are absolutely continuous with respect to Haar measure. Conversely the \(n=12\) summand, taking any positive nonzero function of \(r\) with full support, produces a measure equivalent to Haar, since \(12\rho((0,1))=(0,1)\). Thus the maximal spectral type is \(\delta_1+\mathrm{Haar}\), with no other eigenvalues and no singular-continuous part. For any two \(L^2\) observables orthogonal to the \(n=0\) subspace, absolute continuity and the Riemann–Lebesgue lemma give \(\langle f,U^kg\rangle\to0\) as \(k\to\infty\).

## Verification

The standalone `verify_square.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\), checks \(\det B=1\), the full four-vertex corner chain, the two horizontal edge-mapping identities, the entire polygon area polynomial, the twist identity at distinct algebraic test parameters, and the algebraic cubic pushforward identity. It reports `VERIFY_OK`. Direct high-precision finite orbit tests on several rational rotation leaves also agreed with their predicted least periods. The infinite-spectrum statements are deductions from the proved action-angle representation, not extrapolations from those tests.

## Relationship to prior work

Ostrovski, *Dynamics of a Continuous Piecewise Affine Map of the Square* (arXiv:1305.4282, 2013; Physica D 2014), constructed the relevant polygonal invariant foliation and described its continuously varying rotation numbers (Theorem 5.1, Corollary 5.4, Remark 5.5). **Those existence and qualitative foliation facts are not claimed as new.** The present claim adds the explicit radius-to-frequency formula, the exact area-distribution density, full rational-leaf classification in one formula, and the complete Koopman spectral decomposition of this specified positive-area component. General operator-spectral methods are standard; see Budišić–Mohr–Mezić, *Applied Koopmanism*, arXiv:1206.3164. These sources do not state the cubic density or the spectral type for this map.

## Limitations

The theorem concerns the outer annulus \(\Omega\), **not** the spectral type or global statistical behaviour of all of \(S\). It makes no assertion about perturbations of \(\theta\), and the presence of countably many rational periodic leaves does not give them positive planar area. The original author's 2013 doctoral thesis treats related square dynamics; a full copy was not available for comparison, leaving a bibliographic overlap risk.

## References

1. Georg Ostrovski, *Dynamics of a Continuous Piecewise Affine Map of the Square*, arXiv:1305.4282, submitted 18 May 2013; *Physica D* **271** (2014), 1–9. https://arxiv.org/abs/1305.4282.
2. M. Budišić, R. Mohr, and I. Mezić, *Applied Koopmanism*, arXiv:1206.3164 (2012). https://arxiv.org/abs/1206.3164.
3. Georg Ostrovski, *Topics Arising from Fictitious Play Dynamics*, doctoral thesis, University of Warwick (2013), repository record https://wrap.warwick.ac.uk/58894/ (full-text comparison incomplete).
