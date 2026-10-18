# Sharp square-root control of the real numerical index by Hilbertian distortion

## Finding
Let \(X\) be a **real** Banach space of dimension at least two, linearly isomorphic to a real Hilbert space \(H\) of the same dimension. Write
\[
d=d_{\mathrm{BM}}(X,H)=\inf_{U:X\longrightarrow H}\|U\|\,\|U^{-1}\|,
\]
where the infimum is over bounded invertible real-linear maps. The numerical index is
\[
n(X)=\inf_{\|A\|=1}v_X(A),\qquad
v_X(A)=\sup_{(x,f)\in\Pi(X)}|f(Ax)|,
\]
with \(\Pi(X)=\{(x,f):\|x\|=\|f\|=f(x)=1\}\). Then
\[
\boxed{\quad n(X)\le\sqrt{d^2-1}.\quad}
\]
The coefficient and square-root order are **simultaneously sharp**. For every integer \(m\ge1\), the real normed plane \(X_m\) whose unit ball is the regular \(4m\)-gon inscribed in the Euclidean unit circle satisfies, with \(\beta_m=\pi/(4m)\),
\[
\boxed{\quad d_{\mathrm{BM}}(X_m,\ell_2^2)=\sec\beta_m,\qquad
n(X_m)=\tan\beta_m=\sqrt{d_{\mathrm{BM}}(X_m,\ell_2^2)^2-1}.\quad}
\]
Thus if \(d\le1+\varepsilon\), then \(n(X)\le\sqrt{2\varepsilon+\varepsilon^2}\). Since \(\sec\beta_m-1\sim\beta_m^2/2\) and \(\tan\beta_m\sim\beta_m\), the exponent \(1/2\) and leading constant \(\sqrt2\) cannot be improved uniformly. These bounds concern the ordinary **linear numerical index**, not the rank-one or polynomial index.

## Assumptions and scope
All spaces, maps, norming functionals and inner products are real. The Hilbert comparison is assumed finite, and dimension at least two is essential: the real one-dimensional numerical index equals one while the Hilbert distortion equals one. No finite-dimensionality or smoothness assumption is imposed on \(X\). Multiplicative Banach--Mazur distortion is used, not its logarithm. The inequality may be vacuous when \(d\ge\sqrt2\), since every numerical index is at most one; it is quantitative in the near-Hilbert regime.

## Proof
**1. A Hilbertian skew-rotation test.** Fix \(D>d\). By the definition of Banach--Mazur distance, transport a Hilbert norm \(|\cdot|\) to \(X\) so that for positive \(r,R\) satisfying \(R/r<D\), its Euclidean ball and the original unit ball obey
\[
rB_H\subseteq B_X\subseteq RB_H.
\]
Choose orthonormal Hilbert vectors \(e_1,e_2\) and let \(J\) be rotation by a right angle on their span and zero on its Hilbert-orthogonal complement. Thus \(J^*=-J\), \(\|J\|_H=1\), and \(J^2=-P\) for the nonzero Hilbert-orthogonal projection \(P\) onto this two-plane. The operator \(J\) is bounded on \(X\), and
\[
\|J\|_X^2\ge\|P\|_X\ge1,
\]
since every nonzero projection has operator norm at least one.

For an arbitrary \((x,f)\in\Pi(X)\), represent \(f(y)=\langle h,y\rangle_H\) by the Hilbert Riesz theorem. The ball sandwich gives \(|x|\le R\) and \(|h|\le1/r\), while \(\langle h,x\rangle_H=f(x)=1\). Using \(\langle x,Jx\rangle_H=0\) and \(|Jx|\le|x|\), Cauchy--Schwarz yields
\[
\begin{aligned}
|f(Jx)|
&=\left|\left\langle h-\frac{x}{|x|^2},Jx\right\rangle_H\right|\\
&\le\left(|h|^2-|x|^{-2}\right)^{1/2}|Jx|\\
&\le\left(|h|^2|x|^2-1\right)^{1/2}\\
&\le\sqrt{(R/r)^2-1}\le\sqrt{D^2-1}.
\end{aligned}
\]
(The square roots are defined because \(1=|\langle h,x\rangle_H|\le|h||x|\).) Hence \(v_X(J)\le\sqrt{D^2-1}\). Normalizing the nonzero operator \(J\), and using \(\|J\|_X\ge1\), gives
\[
n(X)\le\frac{v_X(J)}{\|J\|_X}\le\sqrt{D^2-1}.
\]
Letting \(D\downarrow d\) proves the universal bound, also in infinite dimensions.

**2. Exact Euclidean Banach--Mazur distortion of the regular polygons.** Fix \(m\ge1\), let \(N=4m\), \(\beta=\pi/N\), and set
\[
u_j=(\cos(2\pi j/N),\sin(2\pi j/N)),\qquad
B_m=\operatorname{conv}\{u_j:0\le j<N\}.
\]
Its largest and smallest Euclidean radii are respectively \(1\) (at vertices) and \(\cos\beta\) (at side midpoints). This gives the upper bound \(d_{\mathrm{BM}}\le\sec\beta\).

For the reverse inequality, let \(Q\) be an arbitrary positive definite quadratic form. Denote by \(M_Q\) and \(m_Q\) the maximum and minimum of \(\sqrt{Q(x)}\) over the unit sphere of \(X_m\). Average \(Q\) over rotations by integer multiples of \(2\pi/N\). This averaging gives \(\overline Q(x)=\lambda|x|^2\), with \(\lambda>0\), because a symmetric quadratic form invariant under a nontrivial planar rotation of order \(N\ge4\) is a scalar Euclidean form. Every such rotation preserves the polygon unit sphere, so \(m_Q^2\le\lambda|x|^2\le M_Q^2\) on that sphere. Applying this to a unit-circle vertex and to a side midpoint of Euclidean radius \(\cos\beta\) gives
\[
M_Q^2\ge\lambda,\qquad m_Q^2\le\lambda\cos^2\beta,
\]
and hence \(M_Q/m_Q\ge\sec\beta\). Taking the infimum over quadratic forms proves \(d_{\mathrm{BM}}=\sec\beta\).

**3. Exact numerical index of the regular polygons.** Let \(J\) now denote the Euclidean quarter-turn, an isometry of \(X_m\), since \(4\mid N\). At each vertex \(u\), the two extreme norming functionals are
\[
f_\pm(z)=\langle u\pm(\tan\beta)Ju,z\rangle_{\mathbb R^2}.
\]
They have dual norm one and take value one at \(u\). Given a linear operator \(A\), write \(Au=p u+q Ju\). Then the vertex-norming pairs imply
\[
v_{X_m}(A)\ge\max(|p+(\tan\beta)q|,|p-(\tan\beta)q|)
=|p|+(\tan\beta)|q|.
\]
Since \(\tan\beta\le1\) and both \(u,Ju\) are norm-one vectors,
\[
|p|+(\tan\beta)|q|\ge(\tan\beta)(|p|+|q|)
\ge(\tan\beta)\|Au\|_{X_m}.
\]
The operator norm is attained on a polygon vertex: \(\|A\|=\max_u\|Au\|\), because the polygon is the convex hull of its vertices. Hence \(v_{X_m}(A)\ge(\tan\beta)\|A\|\) for all \(A\), and therefore \(n(X_m)\ge\tan\beta\).

Conversely, the quarter-turn \(J\) has norm one. For any vertex \(u\), its two extremal norming functionals satisfy \(|f_\pm(Ju)|=\tan\beta\). The finite-dimensional polyhedral numerical-radius formula reduces \(v(J)\) to the maximum over such vertex--extreme-support pairs. To see the reduction directly: for each fixed unit vector the supremum over its norming face is attained at a dual extreme; on the relative interior of each polygon edge the norming functional is the fixed outward facet normal and \(f(Jx)\) is linear in \(x\), hence maximized in modulus at an endpoint. At vertices use the extreme functionals. Consequently \(v(J)=\tan\beta\), proving \(n(X_m)=\tan\beta\).

**4. Sharpness near a Hilbert norm.** The identities \(\tan^2\beta=\sec^2\beta-1\) give equality in the universal inequality for every \(m\). As \(m\to\infty\), \(\beta_m\to0\), and
\[
\frac{n(X_m)}{\sqrt{d_{\mathrm{BM}}(X_m,\ell_2^2)-1}}
\longrightarrow\sqrt2.
\]
This rules out a smaller leading coefficient and any exponent strictly larger than \(1/2\) in a uniform near-Hilbert bound.

## Verification
The proof is analytic and does not depend on numerical sampling. The accompanying self-contained Python script `CHECK.py` evaluates the exact polygon vertex and facet-normal formulas for \(N=4,8,12,16,24\), checking the quarter-turn norm/numerical radius and the lower bound for all \(625\) matrices with entries in \(\{-2,-1,0,1,2\}\) at each polygon (\(3125\) matrix diagnostics total). These finite tests do not certify the infinite-dimensional theorem or exhaust arbitrary matrices; those conclusions follow from the Hilbertian argument and the vertex reduction.

## Relationship to prior work
The theorem is motivated by the 2026 study by Monika, Amrutam and Dey on convergence of the numerical index under operator openings and by earlier work of Finet, Martín and Payá establishing continuity of the index in the metric of equivalent norms. The present assertion is a globally sharp **explicit modulus** in terms of Hilbertian Banach--Mazur distortion, not a reproof of qualitative continuity. Martín and Merí already computed the numerical index of regular even polygons; the polygon index formula itself is therefore **not claimed as new**. The new comparison combines a universal Hilbertian skew-rotation bound with a sequence of exact equality witnesses. The equality witnesses' Banach--Mazur distortion is proved here by symmetry averaging.

## Limitations
The numerical-index upper bound requires **real** scalars and Hilbert-isomorphism; the complex Hilbert-space numerical index is positive and does not satisfy the same estimate at distance one. No characterization of all equality cases or of sharpness at every prescribed distortion is claimed. Prioritization under different terminology remains possible despite the inspected literature. The upper bound becomes uninformative for \(d\ge\sqrt2\). No independent mathematical audit has been performed.

## References
1. Monika, T. Amrutam, and P. Dey, *On the Convergence of Numerical Index via Operator Openings and Ultraproducts*, arXiv:2603.21311v1 (first publicly posted 2026-03-22). https://arxiv.org/abs/2603.21311
2. C. Finet, M. Martín, and R. Payá, *Numerical index and renorming*, Proc. Amer. Math. Soc. **131** (2003), 871–877. https://doi.org/10.1090/S0002-9939-02-06576-0 ; author's open manuscript https://www.ugr.es/~mmartins/Curriculum/Papers/2003-renorming.pdf
3. M. Martín and J. Merí, *Numerical index of some polyhedral norms on the plane*, Linear Multilinear Algebra **55** (2007), 175–190. https://doi.org/10.1080/03081080600628323 ; author's open manuscript https://www.ugr.es/~mmartins/Curriculum/Papers/2007-Polygons.pdf
