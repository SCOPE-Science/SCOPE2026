# The characteristic-three Cremona transition of the cubic Hankel determinant

## Finding
Let \(k\) be an algebraically closed field, put \(R=k[a,b,c,d,e]\), and let
\[
F=\det\begin{pmatrix}a&b&c\\ b&c&d\\ c&d&e\end{pmatrix}
=ace-ad^2-b^2e+2bcd-c^3.
\]
The polar map \(\nabla F:\mathbb P^4\dashrightarrow\mathbb P^4\), defined by its five homogeneous quadratic partial derivatives, exhibits the following exact characteristic dependence.

* If \(\operatorname{char} k\ne2,3\), it is dominant and generically separable of degree \(2\). Its generic quadratic function-field extension is branched along the smooth quadric \(y_2^2-3y_1y_3+12y_0y_4=0\) in the target with coordinates \([y_0:\cdots:y_4]=[F_a:F_b:F_c:F_d:F_e]\).
* If \(\operatorname{char} k=3\), it is a birational quadratic Cremona transformation. Its projective base scheme is reduced and is the **disjoint union** of the rational normal quartic
\[
C_4=\{[s^4:s^3t:s^2t^2:st^3:t^4]:[s:t]\in\mathbb P^1\}
\]
and the isolated point \(p=[0:0:1:0:0]\), which does **not** lie on \(V(F)\). The intrinsic singular scheme \(V(F,F_a,F_b,F_c,F_d,F_e)\) is exactly \(C_4\), with its reduced structure.
* If \(\operatorname{char} k=2\), the polar image has dimension at most \(2\), so the map is not dominant.

Thus the very same integral cubic acquires a homaloidal polar map precisely in characteristic three, whereas its separable polar degree in characteristic different from two and three is two.

## Assumptions and scope
All schemes and maps are over \(k\); the projective base scheme means \(\operatorname{Proj}(R/(F_a,F_b,F_c,F_d,F_e))\), without artificially adding the equation \(F=0\). The term *degree* means the degree of the induced extension of rational function fields for a dominant generically finite map. The word *branched* in the first case refers to the finite double covering of the target induced after passing to the birational Grassmannian model, not to any unsupported statement about a resolved source morphism. No claim about an inverse map's smallest polynomial degree or its exceptional-divisor scheme is made.

## Proof
Set
\[
\begin{aligned}
 A&=ac-b^2,&B&=ad-bc,&C&=ae-bd,\\
 D&=bd-c^2,&E&=be-cd,&G&=ce-d^2.
\end{aligned}
\]
These are the six ordered \(2\times2\) minors of
\(H=\begin{psmallmatrix}a&b&c&d\\b&c&d&e\end{psmallmatrix}\).
They satisfy the Pluecker equation
\[
AG-BE+CD=0.
\]
Direct differentiation gives the exact identity, valid integrally,
\[
(F_a,F_b,F_c,F_d,F_e)=(G,-2E,C+3D,-2B,A),
\]
and \(F=aG+eA-cC+cD\).

The rational map \(\Phi:\mathbb P^4\dashrightarrow\operatorname{Gr}(2,4)\subset\mathbb P^5\) formed by all six minors is birational. Indeed, for a general row-space \(W\subset k^4\), let \(u,v\) be a basis of \(W^\perp\). Asking that both rows of \(H\) lie in \(W\) imposes four homogeneous linear equations
\[
(a,b,c,d)\cdot u=(b,c,d,e)\cdot u
=(a,b,c,d)\cdot v=(b,c,d,e)\cdot v=0
\]
on the five entries \((a,b,c,d,e)\). These four equations have rank four generically: for \(u=(-1,0,1,0)\) and \(v=(0,-2,0,1)\) the kernel is spanned by \((1,0,1,0,2)\), and the corresponding rows of \(H\) are independent. (The same calculation works in every characteristic.) Rank four and row independence are open conditions, so on a nonempty open subset of \(\operatorname{Gr}(2,4)\) they reconstruct exactly one source point; the map is birational onto the full Grassmannian quadric.

Suppose first that \(\operatorname{char}k\ne2\). The polar map is \(\Phi\) followed by a linear projection from the single point of \(\mathbb P^5\) specified by \(A=B=E=G=0\), \(C=-3D\). This projection center lies on the Pluecker quadric if and only if \(3=0\) in \(k\). Writing \(y_0=G\), \(y_1=-2E\), \(y_2=C+3D\), \(y_3=-2B\), \(y_4=A\) and eliminating \(C\), the quadric equation becomes
\[
3D^2-y_2D+\tfrac14 y_1y_3-y_0y_4=0.
\]
For \(\operatorname{char} k\ne2,3\), this is a separable quadratic over \(k(\mathbb P^4_y)\): its discriminant \(y_2^2-3y_1y_3+12y_0y_4\) is a nondegenerate quadratic form, hence cannot be a square in the rational function field. The map therefore has degree two and the double-cover model is branched on this smooth quadric. In characteristic three, the equation is linear in \(D\) over the open set \(y_2\ne0\). Thus it reconstructs \(D=(\tfrac14 y_1y_3-y_0y_4)/y_2\) and then \(C=y_2\), proving birationality. Equivalently, the projection of a smooth quadric from a point on that quadric is birational.

For the base scheme in characteristic three, put \(K=(A,B,C,E,G)\), \(I=(A,B,C,D,E,G)\) and \(\mathfrak p=(a,b,d,e)\). The homogeneous ideal \(I\) is the prime ideal of the rational normal quartic \(C_4\), and \(\mathfrak p\) defines \(p\). The elementary Laplace relations
\[
\begin{aligned}
 aD&=bB-cA,&bD&=cB-dA,\\
 dD&=cE-bG,&eD&=dE-cG
\end{aligned}
\]
show \(D\mathfrak p\subseteq K\). Because \(I=K+(D)\), \(K\subseteq\mathfrak p\), and \(D\notin\mathfrak p\), primality of \(\mathfrak p\) implies \(K=I\cap\mathfrak p\). This is radical, and the disjointness follows from \(D(p)=-1\), since \(D\) vanishes on \(C_4\). In characteristic three \(F\equiv cD\pmod K\); after adding \(F\), all five homogeneous variables annihilate \(D\) modulo \((K,F)\). Consequently the saturation of \((K,F)\) is \(I\), so the intrinsic singular scheme is reduced \(C_4\). Moreover \(F(p)=-1\ne0\), confirming that the extra polar base point lies outside the cubic. In characteristic two, the second and fourth partials vanish identically, and hence the polar image lies in a projective plane. This completes the proof.

## Verification
Run `python verify.py` with SymPy installed. The script checks the determinant, all five integral derivative expressions, Pluecker relation, annihilator syzygies, excluded point, a characteristic-independent rank-four reconstruction witness, and the quadratic discriminant identity. The identity/projection argument, the open rank-four reconstruction, and the saturated-ideal argument prove the infinite-field assertions; spot checks alone are not invoked as such proofs.

## Relationship to prior work
Mostafazadehfard and Simis, *Homaloidal determinants* (first public arXiv version 2014-07-30, arXiv:1407.8089), study the same generic \(3\times3\) Hankel determinant and prove it is not homaloidal **in characteristic zero** (Proposition 3.20); they explicitly assume characteristic zero in their introduction. Their sections 3.3–3.4.1 also establish relationships between the five derivatives and the six catalecticant minors. The present theorem identifies the previously unaddressed characteristic-three change of projection center, its birational effect, its extra genuine base point, and the precise degree-two comparison outside characteristics two and three. Those results are not consequences of the characteristic-zero non-homaloidality theorem. Related general literature on determinantal and catalecticant polar maps is extensive; unlocated equivalent characteristic-three calculations remain a residual originality risk.

## Limitations
The result applies to this particular universal cubic in five coordinates and is not a general theorem for larger Hankel determinants or arbitrary catalecticants. It does not describe a global resolution of the polar map or the scheme structure of the branch locus in a blowup of the original source. The base-scheme statement is specific to characteristic three. The novelty comparison is literature-based rather than a completeness theorem for all historical sources. Independent validation has not been performed.

## References
Mostafazadehfard, M. and Simis, A., *Homaloidal determinants*, arXiv:1407.8089, first publicly posted 2014-07-30; especially Introduction and §§3.3–3.4.1, Proposition 3.20. https://arxiv.org/abs/1407.8089 ; complete text https://arxiv.org/pdf/1407.8089 .
