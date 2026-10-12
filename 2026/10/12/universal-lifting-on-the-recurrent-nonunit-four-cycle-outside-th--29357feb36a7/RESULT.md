# Universal lifting on the recurrent nonunit four-cycle outside the unique exceptional parameter
## Finding
For every integer \(c\ge 2\) with \(c\ne 4\), define
\[
P_0(T)=T^2+cT+c,\quad P_1(T)=T^2-cT-c,\quad P_2(T)=T^2-cT+c,\quad P_3(T)=T^2+cT-c.
\]
Every nonzero integral point \((x,y)\) on
\[
x^2-y^2+c(x-y)+c=cxy
\]
starts an infinite primitive normalized congruence-jump chain following the recurrent state cycle
\[
(P_0,P_3)\to(P_1,P_0)\to(P_2,P_1)\to(P_3,P_2)\to(P_0,P_3).
\]
No coprimality condition on \(x,y,c\), no sign condition, and no prescribed residue class modulo \(c\) is needed. The parameter exclusion is sharp: when \(c=4\), the point \((-2,4)\) lies on the conic and the first quotient is zero.

## Assumptions and scope
Here \(c\) is an integer with \(c\ge2\). Coordinates and quotient coordinates are required to be nonzero because the divisibility states use nonzero integer coordinates. “Primitive normalized” means that after a raw reciprocal transform, its scalar content is cancelled and the resulting primitive polynomial is used as the next coefficient state.

The claim concerns the explicit recurrent four-cycle above and the displayed conic. It does not classify all integral points on the conic, and it does not assert that the exceptional parameter \(c=4\) has no infinite chains; it only shows that the universal all-points statement fails there.

## Proof
For a point \((x,y)\) on the conic define
\[
z_1=cx+y+c,\qquad z_2=cz_1+x+c,\qquad z_3=cz_2+z_1-c,\qquad z_4=cz_3+z_2-c.
\]
Direct expansion using the conic relation gives
\[
P_0(x)=yz_1,\quad P_1(z_1)=xz_2,\quad P_2(z_2)=z_1z_3,\quad P_3(z_3)=z_2z_4,
\]
and the returned pair \((z_4,z_3)\) again satisfies the same conic. These identities are the normalized divisibilities needed for one full traversal of the four coefficient states: they show directly that the scalar content occurring in each raw reciprocal transform can be cancelled at the current arithmetic point.

It remains to prove that no quotient coordinate can vanish when \(c\ne4\). If \(z_1=0\), then \(P_0(x)=0\). The discriminant of \(P_0\) is \(c(c-4)\). For \(2\le c<4\) it is negative. For \(c>4\), if \(d^2=c(c-4)\), then
\[
(c-2-d)(c-2+d)=4.
\]
Both factors are positive integers of the same parity. The only same-parity positive factorization of \(4\) is \(2\cdot2\), which would force \(d=0\) and \(c=4\), a contradiction. Hence \(P_0\) has no integer root for \(c\ne4\). The same argument applies to \(P_2\).

If \(z_2=0\), then because \(x\ne0\), the identity \(P_1(z_1)=xz_2\) gives \(P_1(z_1)=0\). The discriminant is \(c(c+4)\). If \(d^2=c(c+4)\), then
\[
(c+2-d)(c+2+d)=4.
\]
Again the two factors are positive integers of the same parity; the only possibility \(2\cdot2\) would give \(c=0\), impossible for \(c\ge2\). Thus \(P_1\) has no integer root. The same argument applies to \(P_3\).

Having shown \(z_1,z_2\ne0\), if \(z_3=0\) then \(P_2(z_2)=0\), impossible for \(c\ne4\). Having shown \(z_2,z_3\ne0\), if \(z_4=0\) then \(P_3(z_3)=0\), also impossible. Therefore a full cycle is nondegenerate and returns a nonzero integral point on the same conic. Induction gives an infinite primitive normalized chain.

For sharpness at \(c=4\), substituting \((x,y)=(-2,4)\) gives equality in the conic, while
\[
z_1=4(-2)+4+4=0.
\]
So the all-points nondegeneracy statement fails exactly at the excluded parameter.

## Verification
The accompanying `verify.py` checks the four quotient identities and conic preservation as polynomial identities, checks the discriminant transformations
\[
(c-2)^2-c(c-4)=4,\qquad (c+2)^2-c(c+4)=4,
\]
and checks the \(c=4\) exceptional point exactly. The infinite conclusion itself is mathematical induction from one-cycle preservation and the proved absence of integer roots; finite computation is not used as a substitute for that induction.

## Relationship to prior work
Alekseyev and Khomovsky, arXiv:2610.00808v1, Proposition 4.12, introduce this recurrent nonunit four-cycle, derive the same quotient formulas and full-cycle conic preservation, and prove existence of infinitely many positive integral points by starting from \((1,1)\) in the chamber \(x\equiv y\equiv1\pmod c\). Their Proposition 4.11 gives a general sufficient coprime chamber for normalized coefficient orbits. The result here removes those chamber, positivity, and coprimality restrictions on this explicit conic for every \(c\ne4\), and identifies \(c=4\) as the unique parameter where a universal all-points statement can fail because an endpoint polynomial acquires an integer root.

Exact-phrase and formula searches for the conic, the four polynomials, “recurrent nonunit four-cycle,” and the \(c=4\) zero-quotient boundary returned the source paper but no broader published statement asserting this all-point lifting theorem. Semantic searches over published findings likewise returned no statement implying it.

## Limitations
The exceptional parameter \(c=4\) is not fully classified here. Some \(c=4\) points, including the positive orbit constructed in the source paper, still have infinite chains. This result only proves that \(c=4\) is the unique parameter at which the universal claim for every nonzero conic point is false. No claim is made about coefficient cycles outside this explicit four-state family.

## References
1. Max A. Alekseyev and Dmitry I. Khomovsky, “Congruence Jumping in Polynomial Divisibility Systems: Arithmetic Structure and Solution Sets,” arXiv:2610.00808v1, first public 2026-09-30, especially Proposition 4.11, Proposition 4.12, and Proposition 4.13.
