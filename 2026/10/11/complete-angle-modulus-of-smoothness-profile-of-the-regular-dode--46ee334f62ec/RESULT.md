# Complete angle-modulus-of-smoothness profile of the regular dodecagonal plane
## Finding
Let
\[
X_{12}=(\mathbb R^2,N_{12}),
\]
where
\[
N_{12}(s,t)=\max\left\{|s|,|t|,\left|\frac{\sqrt3s+t}{2}\right|,\left|\frac{s+\sqrt3t}{2}\right|,\left|\frac{-s+\sqrt3t}{2}\right|,\left|\frac{-\sqrt3s+t}{2}\right|\right\}.
\]
For \(0\le\epsilon\le2\), define
\[
m(\epsilon)=\min_{\substack{x,y\in S_{X_{12}}\\N_{12}(x-y)=\epsilon}}N_{12}(x+y).
\]
Then
\[
\boxed{m(\epsilon)=\begin{cases}
2-(2-\sqrt3)\epsilon,&0\le\epsilon\le1,\\[2pt]
1+\sqrt3-\epsilon,&1\le\epsilon\le\sqrt3,\\[2pt]
(2+\sqrt3)(2-\epsilon),&\sqrt3\le\epsilon\le2.
\end{cases}}
\tag{1}
\]
Hence the angle modulus of smoothness introduced by Du, Ahmad, Din and Li is
\[
\boxed{\rho^a_{X_{12}}(\epsilon)=1-\frac12m(\epsilon)^2.}
\tag{2}
\]
The minimizing chord type changes exactly at \(\epsilon=1\) and \(\epsilon=\sqrt3\).

## Assumptions and scope
All scalars are real. Put \(r=2-\sqrt3\). The consecutive vertices
\[
v_0=(1,r),\quad v_1=(\sqrt3-1,\sqrt3-1),\quad v_2=(r,1),
\]
continue by rotations through \(\pi/6\); write \(E_j=[v_j,v_{j+1}]\), with indices modulo \(12\). By dihedral symmetry, one unit vector may be placed on \(E_0\).

For signed facet functionals use
\[
f_0(s,t)=s,\quad f_1(s,t)=t,\quad f_2(s,t)=\frac{\sqrt3s+t}{2},
\]
\[
f_3(s,t)=\frac{s+\sqrt3t}{2},\quad f_4(s,t)=\frac{-s+\sqrt3t}{2},\quad f_5(s,t)=\frac{-\sqrt3s+t}{2},
\]
and their negatives. Then \(N_{12}(z)=\max f(z)\) over these twelve signed functionals.

## Proof
Fix \(x\in E_0\), let \(y\in E_j\), and abbreviate
\[
d=N_{12}(x-y),\qquad s=N_{12}(x+y).
\]
For the first six relative edges, direct facet certificates give the following lower bounds:
\[
\begin{array}{c|c}
 j& s\ge L_j(d)\\ \hline
0&2\\
1&2-(2-\sqrt3)d\\
2&(4-d)/\sqrt3\\
3&1+\sqrt3-d\\
4&4-\sqrt3 d\\
5&(2+\sqrt3)(2-d).
\end{array}
\tag{3}
\]
Here is the certificate behind (3). For \(j=0\), the common supporting facet gives \(f_2(x+y)=2\). For \(j=2,3,4\), respectively,
\[
f_3(x+y)+\frac1{\sqrt3}(-f_5)(x-y)=\frac4{\sqrt3},
\]
\[
f_1(x+y)+(-f_5)(x-y)=1+\sqrt3,
\]
and
\[
f_1(x+y)+\sqrt3 f_0(x-y)=4.
\]
Since every signed facet is bounded above by the norm, these identities imply the stated lines.

For \(j=1\), write \(x=E_0(a)\), \(y=E_1(b)\). If \(a+b\le1\),
\[
f_2(x+y)+(2-\sqrt3)(-f_4)(x-y)-2
=2(4\sqrt3-7)(a+b-1)\ge0.
\]
If \(a+b\ge1\),
\[
f_3(x+y)+(2-\sqrt3)(-f_5)(x-y)-2
=(14-8\sqrt3)(a+b-1)\ge0.
\]
This proves the \(L_1\) line. For \(j=5\), the same split gives
\[
f_1(x+y)+(2+\sqrt3)f_0(x-y)-2(2+\sqrt3)
=2(\sqrt3-2)(a+b-1)\ge0
\]
when \(a+b\le1\), and
\[
f_4(x+y)+(2+\sqrt3)f_2(x-y)-2(2+\sqrt3)
=(4-2\sqrt3)(a+b-1)\ge0
\]
when \(a+b\ge1\). Thus (3) holds everywhere on \(E_0\times E_j\) for \(0\le j\le5\).

The pointwise minimum of the six affine functions in (3) is exactly
\[
M(d)=\begin{cases}
2-(2-\sqrt3)d,&0\le d\le1,\\
1+\sqrt3-d,&1\le d\le\sqrt3,\\
(2+\sqrt3)(2-d),&\sqrt3\le d\le2.
\end{cases}
\tag{4}
\]
The unused lines in (3) lie above this lower envelope. On \(E_6=-E_0\), one has \(d=2\), so \(s\ge M(2)=0\).

The remaining edges follow from central symmetry. Replacing \(y\) by \(-y\) swaps \(d\) and \(s\). The function \(M\) is strictly decreasing and satisfies
\[
M(M(t))=t\qquad(0\le t\le2),
\tag{5}
\]
because its first and third branches are mutual inverses and its middle branch is self-inverse. Thus, if the reflected pair gives \(d\ge M(s)\), applying the decreasing involution \(M\) yields \(s\ge M(d)\). Therefore every unit pair satisfies
\[
N_{12}(x+y)\ge M(N_{12}(x-y)).
\tag{6}
\]

It remains to show sharpness. For \(0\le\epsilon\le1\), take
\[
x=E_0(1-\epsilon),\qquad y=E_1(\epsilon).
\]
For \(1\le\epsilon\le\sqrt3\), put
\[
t=\frac{\epsilon-1}{\sqrt3-1},\qquad x=E_0(1-t),\qquad y=E_3(t).
\]
For \(\sqrt3\le\epsilon\le2\), put
\[
t=\frac{\epsilon-\sqrt3}{2-\sqrt3},\qquad x=E_0(1-t),\qquad y=E_5(t).
\]
Direct substitution into the twelve facet functionals gives
\[
N_{12}(x-y)=\epsilon,
\qquad
N_{12}(x+y)=M(\epsilon)
\]
in all three cases. Hence (1) holds. Finally, by the definition
\[
\rho^a_X(\epsilon)=\sup_{\substack{x,y\in S_X\\\|x-y\|=\epsilon}}\left(1-\frac12\|x+y\|^2\right),
\]
formula (2) follows.

## Verification
The bundled `verify.py` reconstructs the twelve signed dodecagonal facets symbolically over \(\mathbb Q(\sqrt3)\). It verifies every facet certificate in (3), the two half-square certificates needed for \(E_1\) and \(E_5\), the pointwise lower-envelope comparisons, the involution (5), and all three sharp witness families by exact affine endpoint domination.

The computation is finite because a polygonal norm is the maximum of finitely many signed linear functionals. No sampled search or numerical optimization is used as a proof of the continuum statement.

## Relationship to prior work
Du, Ahmad, Din and Li introduced \(\delta_X^a\) and \(\rho_X^a\) in 2022, proved structural relations with classical moduli and geometric constants, and computed selected classical spaces. Their full text contains no regular-dodecagon or regular-polygon computation.

The closest indexed exact result found for the same modulus is the unit-separation value for the regular octagon. A prior exact dodecagonal result determines the angle modulus of convexity, equivalently the largest possible \(N_{12}(x+y)\) at fixed distance. That does not determine the present minimum-chord profile. Other exact dodecagonal constants optimize different expressions and do not imply the three-branch lower envelope (1).

## Limitations
The theorem is specific to the regular dodecagonal plane. No formula is asserted for every regular polygon.

The result determines the extremal value at each separation but does not classify all minimizing pairs beyond the explicit sharp families and the natural symmetries.

Bibliographic and semantic-index searches cannot prove absolute novelty. An equivalent profile could exist under the equivalent minimum-chord or classical-modulus formulation without using the angle-modulus notation.

## References
1. D. Du, A. Ahmad, A. Din and Y. Li, “Some Moduli of Angles in Banach Spaces,” *Mathematics* 10 (2022), 2965, doi:10.3390/math10162965. Published 17 August 2022. Mathematics Subject Classification: 46B20.
