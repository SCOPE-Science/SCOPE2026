# A length-\(11\) singular scheme on the characteristic-\(11\) Klein cubic threefold

## Finding
Let \(\mathcal X\subset\mathbb P^4_{\mathbb Z}\) be defined by
\[
F=\sum_{i\in\mathbb Z/5\mathbb Z} X_i^2X_{i+1}=0.
\]
For every algebraically closed field of characteristic different from \(11\), the geometric fiber is smooth. Its characteristic-\(11\) fiber has exactly one geometric singular point, \(P=[1:3:9:5:4]\). This fiber is geometrically integral and normal. The Tjurina algebra at \(P\) has the exact form
\[
\mathcal O_{\mathcal X_{11},P}/(\partial f/\partial x_1,\ldots,\partial f/\partial x_4)
\cong \overline{\mathbb F}_{11}[t]/(t^{11}),
\]
where the completed/local quotient is intended and \(f\) is the affine defining equation. Its length is \(11\); the quadratic tangent form has rank \(3\). Projection from \(P\) is birational to \(\mathbb P^3\) over \(\mathbb F_{11}\). Finally,
\[
\#\mathcal X_{11}(\mathbb F_{11})=1464=\#\mathbb P^3(\mathbb F_{11}).
\]
The location of a singular point modulo \(11\) is present in de Bondt's prior work and is not presented as new.

## Assumptions and scope
Indices are taken modulo \(5\). The hypersurface is the *literal* reduction of the displayed integral equation, with no claim concerning alternative integral models or stable degenerations. The local algebra statement holds after any algebraically closed extension of \(\mathbb F_{11}\); the point count is only asserted over the specified prime field. A Tjurina length does not, by itself, identify an ADE type or the Milnor number in positive characteristic.

## Proof
Write \(F_i=\partial F/\partial X_i=X_{i-1}^2+2X_iX_{i+1}\). If one coordinate of a common zero of the \(F_i\) vanishes, the previous coordinate vanishes by \(F_i=0\), and descending cyclically forces all five coordinates to vanish. Thus every projective critical point has nonzero coordinates. In characteristics other than \(2\), multiplying all five equations gives \(2^5=-1\), hence \(33=0\). In characteristic \(2\) each derivative is \(X_{i-1}^2\), and there is no projective common zero. Therefore only characteristics \(3\) and \(11\) require attention.

In characteristic \(3\), normalize \(X_0=1\) and set \(t=X_1/X_0\). The critical equations become \(X_{i-1}^2=X_iX_{i+1}\) and give
\[
(X_0,X_1,X_2,X_3,X_4)=(1,t,t^{-1},t^3,t^{-5}),\qquad t^{11}=1.
\]
Every term \(X_i^2X_{i+1}\) then equals \(t\), so \(F=5t=2t\ne0\). None of these critical points lies on the cubic. Thus the characteristic-\(3\) fiber is smooth as well.

In characteristic \(11\), work on \(X_0=1\) and put \(a=X_1,b=X_2,c=X_3,s=X_4\). The homogeneous gradient equations read
\[
2a+s^2=0,\quad 1+2ab=0,\quad a^2+2bc=0,\quad b^2+2cs=0,\quad c^2+2s=0.
\]
The second equation makes \(a,b\) units in the quotient ring, and the first then makes \(s\) a unit. The first, second, and fourth equations give
\[
a=5s^2,\qquad b=s^{-2},\qquad c=5s^{-5}.
\]
Substituting into the third gives \(3s^{11}-1=0\), or \(s^{11}=4\); the fifth is then automatic. Conversely these formulas satisfy all five equations. Since the Euler equation is \(3F=\sum_iX_iF_i\) and \(3\) is invertible, the singular subscheme of the cubic is exactly the gradient scheme. Its affine coordinate algebra is
\[
\mathbb F_{11}[s,s^{-1}]/(s^{11}-4)
=\mathbb F_{11}[s]/((s-4)^{11}).
\]
In characteristic \(11\) there is just one geometric support point, \(s=4\), giving \(P=[1:3:9:5:4]\) and the claimed local Tjurina algebra with length \(11\).

Writing \(u=(u_1,u_2,u_3,u_4)=(a-3,b-9,c-5,s-4)\), one has exactly \(f(P+u)=Q(u)+C(u)\), with
\[
Q=-2u_1^2-5u_1u_2+5u_2^2-4u_2u_3+4u_3^2-u_3u_4+u_4^2,
\qquad C=u_1^2u_2+u_2^2u_3+u_3^2u_4.
\]
All coefficients here are reduced modulo \(11\). The symmetric matrix of \(Q\) has rank \(3\): its leading \(3\times3\) principal minor is nonzero, while its full determinant vanishes. As the singular set is zero-dimensional, the degree-three hypersurface is geometrically irreducible: any nontrivial factorization would give a positive-dimensional singular intersection of components. A hypersurface is Cohen--Macaulay, and an isolated singularity in dimension three has codimension at least two, so Serre's criterion gives normality.

For a generic direction \([u]\in\mathbb P^3\), the line through \(P\) meets the hypersurface away from \(P\) at the rational parameter \(-Q(u)/C(u)\), since its equation is \(\lambda^2(Q(u)+\lambda C(u))=0\). Projection therefore has a rational inverse, proving rationality of this special fiber.

For point counting, put \(Y=V(Q,C)\subset\mathbb P^3_{\mathbb F_{11}}\). The line-through-\(P\) decomposition gives, over any finite extension \(\mathbb F_q/\mathbb F_{11}\),
\[
\#\mathcal X_{11}(\mathbb F_q)=1+\#\mathbb P^3(\mathbb F_q)-\#V(Q)(\mathbb F_q)+q\#Y(\mathbb F_q).
\]
Indeed, a direction contributes one non-vertex point unless \(Q=0,C\ne0\) (none), while \(Q=C=0\) yields an entire line (\(q\) non-vertex points). Exact exhaustive projective enumeration over \(\mathbb F_{11}\), implemented in the accompanying dependency-free program, gives \(\#V(Q)(\mathbb F_{11})=133\) and \(\#Y(\mathbb F_{11})=12\). Consequently \(1+1464-133+11\cdot12=1464\). An independent enumeration of all \(16105\) projective points of \(\mathbb P^4(\mathbb F_{11})\) obtains the same count.

## Verification
Run `python3 verify.py` using Python 3.8 or later. The finite code checks the defining equation and derivatives in the exact algebra \(\mathbb F_{11}[s]/(s^{11}-4)\), the rank-three Hessian, and two independent finite-field point counts. It prints `VERIFY_OK` on success. The proof of the completeness of the singular scheme, for all algebraic extensions, is the preceding elimination argument; finite checks are supporting evidence, not its substitute.

## Relationship to prior work
The Klein hypersurface form and characteristic-zero automorphism results appear in González-Aguilera--Liendo--Montero--Villaflor Loyola, *On a Torelli Principle for automorphisms of Klein hypersurfaces* (arXiv:2212.13308, first posted 2022-12-26). De Bondt, *Rational maps H for which K(tH) has transcendence degree 2 over K* (arXiv:1501.06046, first posted 2015-01-24), explicitly noted that the point represented by powers of \(3\) becomes singular in characteristic \(11\). Neither inspected passage computes the fat singular scheme, its Tjurina algebra or this finite-field count. Marquand--Viktorova's *The defect of a cubic threefold* (arXiv:2312.05118, 2023) studies the complex case and does not imply these wild-characteristic local or arithmetic calculations. Earlier knowledge of the singular point implies rationality by the familiar projection argument; rationality is included as geometry, not presented as a novel theorem by itself.

## Limitations
No classification of the completed hypersurface singularity up to analytic equivalence, its Milnor number, a small resolution, the full zeta function, or an invariant of a stable integral model is claimed. The rational-point computation is for the prime field only. The singular point and its immediate rationality consequence are already implicit in prior literature. Searches cannot exclude all unindexed or inaccessible historical special-characteristic calculations; independent literature and mathematical validation have not been performed.

## References
1. V. González-Aguilera, A. Liendo, P. Montero, R. Villaflor Loyola, *On a Torelli Principle for automorphisms of Klein hypersurfaces*, arXiv:2212.13308, v1 dated 2022-12-26.
2. M. de Bondt, *Rational maps H for which K(tH) has transcendence degree 2 over K*, arXiv:1501.06046, v1 dated 2015-01-24, especially discussion following equation (1.6).
3. L. Marquand, S. Viktorova, *The defect of a cubic threefold*, arXiv:2312.05118, v1 dated 2023-12-08.
