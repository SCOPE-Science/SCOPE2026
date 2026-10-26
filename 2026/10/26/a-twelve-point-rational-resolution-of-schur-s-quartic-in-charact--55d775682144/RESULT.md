# A twelve-point rational resolution of Schur’s quartic in characteristic two

## Finding
Let \(k\) be algebraically closed of characteristic \(2\). The coefficientwise characteristic-two reduction \(X\subset\mathbf P^3_k\) of Schur's quartic,
\[
X:\quad x^4+xy^3+z^4+zw^3=0,
\]
is normal and has a unique singular point \(P=[1:0:1:0]\). Its minimal resolution is the blowup of \(\mathbf P^2_k\) in a reduced complete intersection of twelve \(\mathbf F_4\)-rational points. The exceptional set consists of three smooth rational \((-3)\)-curves intersecting pairwise transversely at one common point. The twelve points correspond bijectively to the twelve geometric projective lines on \(X\) through \(P\).

The singularity at \(P\) is non-rational, with local geometric genus \(1\) and intrinsic Jacobian (Tjurina) length \(16\). Blowing up the triple crossing in the minimal resolution gives a simple-normal-crossings exceptional star with weights \((-1;-4,-4,-4)\). No assertion is made about lines on \(X\) not passing through \(P\).

## Assumptions and scope
All geometric statements are over an algebraically closed field \(k\) of characteristic \(2\). To specify the reduction, start with the integral equation \(x^4-xy^3-z^4+zw^3=0\). Coordinates on the projection plane are \([U:Y:W]\), with \(U=x+z\), \(Y=y\), \(W=w\). Define
\[
H=Y^3+W^3,\qquad G=U^4+UW^3.
\]
The reduced base scheme \(B=V(H,G)\subset\mathbf P^2\) has points
\[
B=\{[\beta:\alpha:1]:\ \alpha^3=1,\quad \beta=0\ \text{or}\ \beta^3=1\}.
\]
Write \(h\) for the pullback of the class of a plane line and \(E_b\) for the exceptional curve over \(b\in B\).

## Proof
**(1) The singular point and normality.** The four partial derivatives of the displayed quartic in characteristic \(2\) are \(y^3,xy^2,w^3,zw^2\). All vanish only if \(y=w=0\), and then the equation gives \((x+z)^4=0\). Thus \(P=[1:0:1:0]\) is the only singular point. Upon substituting \(z=x+U\), the quartic becomes \(xH+G=0\). The forms \(H\) and \(G\) are relatively prime: the three distinct linear factors of \(H\) involve \(Y,W\), whereas \(G\) is not divisible by any of them. Hence the linear polynomial \(xH+G\) is primitive and irreducible. An integral hypersurface is Cohen--Macaulay, and here all codimension-one points are regular, so Serre's criterion makes \(X\) normal.

**(2) The twelve transverse points.** Since \(H=G=0\) has no point with \(W=0\), set \(W=1\). Its equations are \(Y^3=1\) and \(U(U^3+1)=0\). Both polynomials are squarefree in characteristic \(2\) (derivatives \(Y^2\) and \(1\), respectively). Thus the scheme consists of precisely \(3\cdot4=12\) reduced points, all defined over \(\mathbf F_4\). The two defining curves meet transversely everywhere.

**(3) The resolved map.** Projection from \(P\) gives the rational inverse of the map on \(\mathbf P^2\) defined by the four degree-four forms
\[
[G:YH:UH+G:WH].
\]
Indeed, the substitution \(x=G\), \(y=YH\), \(z=UH+G\), \(w=WH\) satisfies the characteristic-two quartic identically: in the equivalent coordinates \((x,U,Y,W)\), the three plane coordinates are scaled by \(H\), so \(H(YH,WH)=H^4\) and \(G(UH,WH)=H^4G\). Hence the defining equation becomes \(G H^4+H^4G=0\).

The base ideal is the complete intersection ideal \((H,G)\). Its degree-four forms have basis \(G,UH,YH,WH\): a degree-four member of \((H,G)\) is a scalar multiple of \(G\) plus a linear form times \(H\), and these four are independent. Thus the blowup \(Y_0=\operatorname{Bl}_B\mathbf P^2\) resolves the rational map by the globally generated line bundle
\[
L=4h-\sum_{b\in B}E_b.
\]
The resulting morphism \(\pi:Y_0\to X\) is birational because, wherever \(H\ne0\), the direction \([U:Y:W]\) is recovered from \([x+z:y:w]\). Its image is the entire irreducible surface \(X\), as both are projective and the image contains a dense open. The self-intersection \(L^2=16-12=4\) agrees with the quartic degree.

**(4) Complete exceptional configuration.** A curve contracted by \(\pi\) must be mapped to \(P\), since the inverse projection is defined away from \(P\). Outside the basepoints the preimage of \(P\) is exactly \(H=0\): when \(H=0\) and \(G\ne0\), all four coordinates reduce to \([G:0:G:0]\); conversely, if \(H\ne0\), projection recovers a nontrivial direction. The three components of \(H=0\) are the lines \(\ell_\alpha:\ Y=\alpha W\), \(\alpha^3=1\). Each contains exactly four of the basepoints. Their strict transforms \(C_\alpha\) have classes \(h-\sum_{b\in B\cap\ell_\alpha}E_b\) and hence \(C_\alpha^2=1-4=-3\). The three lines meet at \(Q=[1:0:0]\), which is not a basepoint, and their strict transforms meet transversely at that same point. Each blowup-exceptional curve \(E_b\) maps nonconstantly, indeed isomorphically, to a line through \(P\): in local coordinates \((G,H)\), the map on \(E_b\) has projective coordinates linear in \([G:H]\) and its projection from \(P\) has direction fixed at \(b\). No other positive-dimensional fibre exists, since \(Y_0\setminus\bigcup C_\alpha\to X\setminus\{P\}\) is proper and birational with no contracted curves; the smooth target makes this an isomorphism by Zariski's Main Theorem. The smooth \(Y_0\) is therefore the minimal resolution: its only exceptional irreducible curves all have self-intersection \(-3\).

Their pairwise intersection is \(1\). The exceptional intersection matrix has diagonal \(-3\), off-diagonal \(1\), with eigenvalues \(-1,-4,-4\). A blowup at their common ordinary triple point makes their transforms pairwise disjoint with self-intersection \(-4\); its new exceptional curve has self-intersection \(-1\), meeting each of the three once. This is the stated simple-normal-crossings star. The sum \(\sum C_\alpha\) has class \(3h-\sum E_b=-K_{Y_0}\).

**(5) Twelve lines through the singular point.** A projective line through \(P\) is determined by a plane direction \([U:Y:W]\). Along that line the quartic equation, with affine line parameter \(t\) and \(x=1\), has the form \(t^3H(U,Y,W)+t^4G(U,Y,W)\). It vanishes identically if and only if both \(H=G=0\), giving exactly the twelve basepoints in step (2). The images of \(E_b\) are exactly these lines.

**(6) Jacobian length and local geometric genus.** In the affine chart \(x=1\), write \(z=1+u\), \(y=v\), \(w=t\). The completed local hypersurface equation is
\[
f=u^4+v^3+(1+u)t^3.
\]
Its derivative ideal together with \(f\), in the completed local ring at \((0,0,0)\), is precisely \((u^4,v^2,t^2)\): \(\partial_v f=v^2\), \(\partial_t f=(1+u)t^2\) with \(1+u\) a unit, and \(\partial_u f=t^3\), while \(f\) reduces to \(u^4\) modulo \((v^2,t^2)\). Therefore
\[
\operatorname{length}_k k[[u,v,t]]/(f,\partial f)=4\cdot2\cdot2=16.
\]
Since \(Y_0\) is a blowup of \(\mathbf P^2\) at twelve distinct points, \(H^1(Y_0,\mathcal O)=H^2(Y_0,\mathcal O)=0\). The hypersurface exact sequence \(0\to\mathcal O_{\mathbf P^3}(-4)\to\mathcal O_{\mathbf P^3}\to\mathcal O_X\to0\) gives \(H^1(X,\mathcal O)=0\) and \(H^2(X,\mathcal O)\cong k\). The Leray exact sequence for the resolution consequently identifies \(H^0(X,R^1\pi_*\mathcal O_{Y_0})\cong H^2(X,\mathcal O_X)\cong k\). As the sheaf is supported at \(P\), the local geometric genus is \(1\); the singularity is not rational. In particular \(X\) is not a quartic with rational-double-point K3 resolution.

## Verification
A standalone Python/SymPy checker named `check.py` reproduces the characteristic-two polynomial substitution, the four-section map identity, the Jacobian derivatives, the complete \(\mathbf F_4\) basepoint set, the transverse Jacobian criterion at its twelve points, the exceptional intersection matrices, and the length-sixteen local Jacobian quotient. Run `python check.py` with SymPy installed. These finite and symbolic checks are subordinate to the blowup and cohomological proofs above; the finite-field enumeration alone does not prove the infinite-field resolution statement.

## Relationship to prior work
Schur's classical equation is analyzed in Rams--Schütt, *64 lines on smooth quartic surfaces* (first public arXiv version 2012-12-14), which expressly assumes characteristic different from \(2,3\). Rams--Schütt, *At most 64 lines on smooth quartic surfaces (characteristic 2)* (2015), explicitly notes that the classical Schur and Fermat quartics degenerate in characteristic \(2\), but addresses bounds for smooth quartics rather than the exceptional fibre's blowup configuration and singularity invariants. Veniani's work on characteristic-two K3 quartics requires rational double points, whereas this special fibre has a non-rational singularity. Catanese--Schütt treats normal quartic surfaces in characteristic \(2\) generally, but the inspected manuscript does not provide this exact twelve-point projection resolution. The distinctive result here is the explicit complete resolution and local invariants of the singular special fibre, not the already-known classical equation or the observation that the reduction degenerates.

## Limitations
The calculation concerns this coefficientwise reduction and does not classify stable models of an arithmetic family, all lines away from \(P\), or its deformation theory. Earlier modular geometry under alternative names may contain an equivalent resolution. Identified general treatments and a finite set of searches do not establish exhaustive novelty. The review is self-review only; no independent scientific audit is claimed.

## References
1. S. Rams and M. Schütt, *64 lines on smooth quartic surfaces*, arXiv:1212.3511 (first public version 2012-12-14), https://arxiv.org/abs/1212.3511.
2. S. Rams and M. Schütt, *At most 64 lines on smooth quartic surfaces (characteristic 2)*, arXiv:1512.01358 (first public version 2015-12-04), https://arxiv.org/abs/1512.01358.
3. D. Veniani, *Lines on K3 quartic surfaces in characteristic 2*, arXiv:1606.02135, https://arxiv.org/abs/1606.02135.
4. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces II (char=2)*, arXiv:2110.03078, https://arxiv.org/abs/2110.03078.
