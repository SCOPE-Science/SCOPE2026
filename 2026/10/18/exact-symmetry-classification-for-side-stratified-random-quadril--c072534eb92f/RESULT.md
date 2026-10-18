# Exact symmetry classification for side-stratified random quadrilateral areas

## Finding
Let \(Q=ABCD\) be any strictly convex planar quadrilateral and let \(O=AC\cap BD\). Define the affine-invariant diagonal fractions \(p=|AO|/|AC|\) and \(q=|BO|/|BD|\), where \(0<p,q<1\). Independently choose one uniformly distributed arclength point from each of \(AB,BC,CD,DA\) and let \(R\) be their hull area divided by \(\operatorname{area}(Q)\). Then
\[
\mathbb E R=\tfrac12,\qquad \mathbb E(R-\tfrac12)^3=0,\qquad
\mathbb E(R-\tfrac12)^5=-\frac{(p-q)^2(p+q-1)^2}{2160}.
\]
The following equivalence is exact:
\[
R\stackrel{d}{=}1-R\quad\Longleftrightarrow\quad p=q\ \text{or}\ p+q=1.
\]
Consequently every such quadrilateral has zero third central moment, but the entire area law is asymmetric away from two explicit families, as witnessed by a strictly negative fifth central moment.

## Assumptions and scope
A side-stratified sample means four mutually independent points, one on each *specified whole side*, individually uniform in Euclidean arclength. Under any invertible affine transformation, each edge fraction remains uniform and the area fraction \(R\) is unchanged. The diagonals intersect in their interiors because the host quadrilateral is strictly convex. The result concerns the probability law of the area fraction, not geometric reflection symmetry of the host polygon.

## Proof
**Affine normalization.** Send the diagonal intersection to the origin and its two diagonal directions to coordinate axes. The vertices become
\[
A=(-p,0),\quad B=(0,-q),\quad C=(1-p,0),\quad D=(0,1-q).
\]
The host area is \(1/2\). Take independent \(u,v,w,t\) uniform on \([0,1]\) and write the sampled vertices as \(A+u(B-A), B+v(C-B), C+w(D-C), D+t(A-D)\), cyclically. Their oriented shoelace area is nonnegative, and its ratio to host area is exactly
\[
\begin{aligned}
R={}&1+ptu-pu-pvw+pw-qtw+qt+quv-qv\\
&+tw-t+vw-w.
\end{aligned}
\]
Direct integration over the four unit intervals gives \(\mathbb E R=1/2\). Every moment is a finite rational polynomial in \(p,q\): expand the corresponding power in \(u,v,w,t\) and integrate a monomial using \(\int_0^1 z^j\,dz=1/(j+1)\). In particular, exhaustive exact polynomial expansion and collection, reproducible by `checker.py`, produce
\[
\mathbb E(R-\tfrac12)^3=0,\qquad
\mathbb E(R-\tfrac12)^5=-\frac{(p-q)^2(p+q-1)^2}{2160}.
\]
The checker is an implementation of this finite algebraic coefficient identity; its code is not a substitute for an infinite or probabilistic approximation.

**Sufficiency of the two symmetry families.** Put \(a=p-1/2\), \(b=q-1/2\) and introduce independent, symmetric centered side coordinates \(X=2u-1\), \(Y=2v-1\), \(Z=2w-1\), \(T=2t-1\). The polynomial above becomes
\[
\begin{aligned}
4(R-\tfrac12)={}&\tfrac12(T+Y)(X+Z)\\
&+a(TX+T-X-YZ-Y+Z)\\
&+b(-TZ+T+XY+X-Y-Z).
\end{aligned}
\]
If \(p=q\), equivalently \(a=b\), this factors as
\[
4(R-\tfrac12)=(T+Y)\bigl[\tfrac12(X+Z)+a(X-Z)\bigr]+2a(T-Y).
\]
Changing the signs of \((T,Y)\) changes the sign of the whole expression but preserves the joint uniform law. If \(p+q=1\), equivalently \(a=-b\), the factorization is
\[
4(R-\tfrac12)=\bigl[\tfrac12(T+Y)+a(T-Y)\bigr](X+Z)-2a(X-Z).
\]
Changing the signs of \((X,Z)\) has the same law-preserving sign reversal. Thus \(R\) and \(1-R\) have identical distributions in either family.

**Necessity.** If \(R\stackrel d=1-R\), then every bounded odd central moment must vanish, including the fifth. The exact fifth-moment identity forces \((p-q)(p+q-1)=0\). Both fractions lie strictly between zero and one, so no exceptional degeneracy is omitted. This proves the equivalence.

## Verification
Running `python checker.py` with SymPy independently reconstructs the shoelace polynomial, integrates its third and fifth centered powers exactly over the four side parameters, and verifies the two involution factorizations and the mean. The checker uses rational symbolic arithmetic, not Monte Carlo, for the critical moment identities. A direct fraction-valued finite-configuration consistency test is also provided. Its reported equalities are reproducible from the delivered file alone with SymPy installed.

## Relationship to prior work
Area moments for random polytopes sampled from convex boundaries have been studied by Besau–Rosen–Thäle and Reitzner–Schütt–Werner, principally for asymptotic, smooth-boundary or pooled boundary sampling regimes. An earlier exact quadrilateral side-stratified calculation gives the mean, the variance and a complete law for parallelograms; the present statement instead classifies when the *full* distribution is symmetric for **all** strictly convex quadrilaterals, and supplies the first nonzero odd central-moment obstruction. The source literature does not directly settle this four-side, finite-sample symmetry classification. Different sampling mechanisms and the orientation of the host vertices are not interchangeable.

## Limitations
The result does not give an elementary closed probability density for every nonsymmetric quadrilateral. Distributional symmetry here does not imply the host polygon has a Euclidean axis or center of symmetry. The finite moment computation is exact; numerical checks alone would not prove vanishing of all odd moments, which follows instead from explicit involutions. The bibliographic comparison cannot exclude every unpublished or unindexed prior treatment; independent review has not been conducted.

## References
1. F. Besau, D. Rosen, C. Thäle, *Random inscribed polytopes in projective geometries*, arXiv:2005.10502, first public 2020-05-21; *Mathematische Annalen* 381 (2021), 1345–1372; DOI: 10.1007/s00208-021-02257-9.
2. M. Reitzner, C. Schütt, E. M. Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope*, *Discrete & Computational Geometry* 69 (2023), 453–504; DOI: 10.1007/s00454-022-00460-2.
