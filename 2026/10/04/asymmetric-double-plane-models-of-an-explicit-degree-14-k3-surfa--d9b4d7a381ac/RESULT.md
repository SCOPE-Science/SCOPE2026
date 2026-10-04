# Asymmetric double-plane models of an explicit degree-14 K3 surface
## Finding
Consider the smooth cubic fourfold in Staglianò's worked example with coordinates \([t:u:v:x:y:z]\), containing the disjoint planes \(P=V(x,y,z)\) and \(P'=V(t,u,v)\). Write its equation uniquely as \(F=A+B\), where \(A\) has bidegree \((2,1)\) and \(B\) has bidegree \((1,2)\) for \(\mathbb P^2_{t,u,v}\times\mathbb P^2_{x,y,z}\). The inverse-map base surface is
\[
S=V(A,B)\subset \mathbb P^2\times\mathbb P^2.
\]
Its two projections give geometrically asymmetric genus-two models. The first projection \(\pi_1:S\to\mathbb P^2_{t,u,v}\) is a finite double cover branched over the smooth sextic \(D_1=0\), where
\[
D_1=-5t^6+16t^5u+10t^5v-14t^4u^2-24t^4uv+t^4v^2-10t^3u^3+22t^3u^2v-20t^3uv^2+2t^3v^3+15t^2u^4-26t^2u^3v+26t^2u^2v^2-28t^2uv^3-5t^2v^4-2tu^5+12tu^4v-10tu^3v^2+20tu^2v^3+8tuv^4-4tv^5-u^6-4u^3v^3-4v^6.
\]
The second projection \(\pi_2:S\to\mathbb P^2_{x,y,z}\) has exactly one positive-dimensional fiber,
\[
C=\{([0:u:v],[0:1:0]):[u:v]\in\mathbb P^1\},
\]
and its Stein factor is a double plane branched over the sextic \(D_2=0\), where
\[
D_2=-x^6-2x^5y-6x^5z-5x^4y^2+2x^4yz+17x^4z^2-4x^3y^3+8x^3y^2z-2x^3yz^2+2x^3z^3-4x^2y^4-16x^2y^3z-16x^2y^2z^2+12x^2yz^3-17x^2z^4-16xy^4z-12xy^2z^3+4y^4z^2-4y^3z^3-4yz^5+4z^6.
\]
The branch sextic \(D_2\) has exactly one singular point \([0:1:0]\), an ordinary node. The curve \(C\) is a smooth rational \((-2)\)-curve and is contracted to the corresponding \(A_1\) point on the normal double-plane model.

## Assumptions and scope
All schemes and computations are over characteristic zero. The finding concerns the specific cubic polynomial printed in the cited worked example, not every cubic fourfold containing two disjoint planes. The source already identifies the inverse base locus as a smooth degree-\(14\) K3 surface in \(\mathbb P^2\times\mathbb P^2\), cut by one equation of each bidegree \((2,1)\) and \((1,2)\). Classical work also gives the intersection numbers \(H_1^2=H_2^2=2\) and \(H_1H_2=5\). The new content here is the exact branch geometry of the two named projections and the unique contraction in the second model.

## Proof
Splitting the printed cubic by bidegree gives
\[
\begin{aligned}
A={}&t^2y+tux-tuy+tuz-tvy-u^2x+uvx-v^2x+v^2z,\\
B={}&tx^2-txy-txz-ty^2-tz^2-ux^2-uyz+uz^2-vxy-vyz.
\end{aligned}
\]
On the line joining \([t:u:v:0:0:0]\) to \([0:0:0:x:y:z]\), the cubic restricts to \(\lambda\mu(\lambda A+\mu B)\). Thus the residual third-point construction is undefined exactly when \(A=B=0\), recovering \(S\).

For \(\pi_1\), the equation \(A=0\) cuts a line in the second \(\mathbb P^2\). With
\[
\ell=(tu-u^2+uv-v^2,\ t^2-tu-tv,\ tu+v^2)^T
\]
and \(2B=X^TQX\), \(X=(x,y,z)^T\), where
\[
Q=\begin{pmatrix}
2(t-u)&-(t+v)&-t\\
-(t+v)&-2t&-(u+v)\\
-t&-(u+v)&2(-t+u)
\end{pmatrix},
\]
the discriminant of the conic restricted to the line \(\ell^TX=0\) is \(\ell^T\operatorname{adj}(Q)\ell=D_1\). Exact Gröbner-basis checks on the three projective affine charts show that the three first derivatives of \(D_1\) have no common projective zero, so the sextic is smooth. A positive-dimensional fiber would force the restricted conic to vanish identically on its line; then its binary quadratic discriminant and all first derivatives of that discriminant vanish. Smoothness of \(D_1\) therefore excludes positive-dimensional fibers. A general line meets a conic in two points, hence \(\pi_1\) is finite of degree two with branch sextic \(D_1\).

For \(\pi_2\), write
\[
m=(x^2-xy-xz-y^2-z^2,\ -x^2-yz+z^2,\ -xy-yz)^T
\]
and \(2A=T^TPT\), \(T=(t,u,v)^T\), where
\[
P=\begin{pmatrix}
2y&x-y+z&-y\\
x-y+z&-2x&x\\
-y&x&2(-x+z)
\end{pmatrix}.
\]
Then \(D_2=m^T\operatorname{adj}(P)m\). Exact chartwise Gröbner bases show that its projective singular locus is the singleton \([0:1:0]\). In the chart \(y=1\), with local coordinates \((X,Z)=(x,z)\), the quadratic term is
\[
-4(X^2+4XZ-Z^2),
\]
whose symmetric matrix has determinant \(-5\), so this singularity is an ordinary node. At \([x:y:z]=[0:1:0]\), the defining equations become \(B=-t\) and \(A=t(t-u-v)\), hence the full fiber is exactly \(C\). Any other positive-dimensional fiber would again force a singular branch point, so there is no other contracted curve. The Stein factor is therefore the normal degree-two cover of \(\mathbb P^2\) branched along \(D_2\); a node of the branch gives an \(A_1\) surface singularity. Since \(S\) is smooth and \(C\cong\mathbb P^1\), adjunction on the K3 surface gives \(C^2=-2\).

## Verification
The accompanying exact symbolic checker reconstructs \(F=A+B\), forms both adjugate discriminants, verifies their degree, checks the projective singular loci by Gröbner bases, verifies the nondegenerate quadratic tangent cone at \([0:1:0]\), confirms the exceptional fiber equations, and checks the degree \(14\) intersection-number identity. A separate chartwise Jacobian check of \(A=B=0\) on all nine standard affine charts also found no singular point, agreeing with the source's smoothness computation. The packaged checker terminates with `VERIFY_OK`.

## Relationship to prior work
Staglianò's example supplies the explicit cubic, the smooth degree-\(14\) K3 inverse base locus, its bidegree generators, and the multidegree coefficients \((2,5,2)\), but does not give equations or singularity types for the branch sextics of the two projections. Hassett's classical analysis of cubic fourfolds containing two disjoint planes identifies the associated K3 as a \((1,2)\)-\((2,1)\) complete intersection and gives the same rank-two intersection lattice; this covers the abstract K3 construction and lattice but not the coordinate-specific asymmetric branch models above. Searches for the explicit cubic together with branch-sextic, double-plane, nodal-branch, and projection terms did not locate a prior statement of these two branch equations or of the unique contracted curve.

## Limitations
The result is coordinate-specific and makes no classification claim for all degree-\(14\) K3 surfaces or all cubics containing two disjoint planes. It does not compute the full Néron–Severi group of the example. The originality comparison is bounded by the sources and searches listed in the accompanying review, so uncatalogued computations could in principle contain the same explicit branch equations.

## References
1. Giovanni Staglianò, *Computations with rational maps between multi-projective varieties*, Journal of Software for Algebra and Geometry 11 (2021), 143–153, doi:10.2140/jsag.2021.11.143; arXiv:2101.04503v1.
2. Brendan Hassett, *Special cubic fourfolds*, Compositio Mathematica 120 (2000), 1–23.
3. Asher Auel, *Brill–Noether special cubic fourfolds of discriminant 14*, arXiv:2007.15590.
