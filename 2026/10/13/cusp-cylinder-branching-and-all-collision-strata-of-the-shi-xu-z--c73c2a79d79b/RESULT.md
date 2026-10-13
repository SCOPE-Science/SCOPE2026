# Cusp-cylinder branching and all collision strata of the Shi–Xu–Zuo quartic cover

## Finding
Let \(F:\mathbb A^3_{\mathbb C}\to\mathbb A^3_{\mathbb C}\) be the polynomial map
\[
F(x,y,z)=(y,yz-x^2,z^2+yx^2+y^2z+x^3)=(u,v,w).
\]
Define the target polynomials
\[
\begin{aligned}
B&=v^2+u^3v-u^2w,\\
S&=9u^4-64u^3-64v,\\
T&=512w+u(27u^5-288u^4+512u^3-288uv+512v),\\
Q&=(S^3-T^2)/1024.
\end{aligned}
\]
The reduced branch divisor of this finite degree-four map is \(D=V(BQ)\). The component \(V(B)\) is a Whitney umbrella, singular exactly along the line \(L_B=V(u,v)\). The other irreducible component \(V(Q)\) is polynomially equivalent to the cuspidal cylinder \(T^2=S^3\), singular exactly on \(L_Q=V(S,T)\). The two singular lines are disjoint away from the origin.

The reduced intersection of the two branch components is exactly the union of the two affine curves
\[
C_{31}=\{v=-u^3,\ w=0\},\qquad
C_{22}=\left\{v=\frac{u^3(u-8)}8,\ w=\frac{u^5(u-8)}{64}\right\}.
\]
Both are smooth rational affine curves, and they intersect only at \((u,v,w)=(0,0,0)\). At their nonzero points the components of \(D\) are smooth, with generic local intersection multiplicities \(3\) along \(C_{31}\) and \(1\) along \(C_{22}\).

The complete table of fibre-length partitions, counting each geometric point by its local scheme length, is:

| Target stratum | Fibre partition |
| --- | --- |
| Outside \(D\) | \((1,1,1,1)\) |
| Smooth part of exactly one branch component, away from the special curves and lines below | \((2,1,1)\) |
| \(C_{31}\setminus\{0\}\) or \(L_Q\setminus\{0\}\) | \((3,1)\) |
| \(C_{22}\setminus\{0\}\) or \(L_B\setminus\{0\}\) | \((2,2)\) |
| Origin | \((4)\) |

The two branch lines and intersection curves intersect each other only as stated: \(L_B\cap V(Q)=L_Q\cap V(B)=\{0\}\), and \(C_{31}\cap C_{22}=\{0\}\). Thus the table is exhaustive and its exceptional strata do not overlap away from the origin.

## Assumptions and scope
All schemes and algebraic sets are over \(\mathbb C\); singular loci of components and curve intersections are stated on their reduced supports. A fibre partition lists the lengths of its Artinian local algebras, so the entries sum to four. An intersection multiplicity of the two branch surfaces along a curve means the length after localizing their scheme-theoretic intersection at the generic point of that curve. These are target-space branch and fibre invariants; no Bernstein–Sato ideal computation is asserted.

## Proof
**Finiteness and a quartic eliminant.** The defining equations imply the monic relation
\[
p_{u,v,w}(x)=x^4+u^2x^3+2(v+u^3)x^2+B=0.
\]
Also \(z\) satisfies the monic quadratic obtained from the third coordinate. Hence \(F\) is finite. On \(u\ne0\), one recovers \(z=(v+x^2)/u\), and the fibre is cut out by \(p=0\). Thus its generic degree is four. Both affine source and target are smooth threefolds and the map is finite, so the finite Cohen–Macaulay flatness criterion makes \(F\) finite flat of degree four. In particular, fibre lengths always sum to four.

**The branch equation.** The source Jacobian determinant is
\[
\det(dF)=x(3xy+4y^2+4z).
\]
Direct expansion of the quartic discriminant gives
\[
\operatorname{disc}_x(p)=-u^4 BQ.
\]
For \(u\ne0\), this gives the branch equation \(BQ=0\). The entire branch over \(u=0\) is checked directly: there \(v=-x^2\), the Jacobian is \(4xz\), and hence critical points have either \(x=0\), mapping to \(v=0\) and \(B=0\), or \(z=0\), mapping to \(w=x^3\) and \(v^3+w^2=0\), precisely \(Q=0\) on that plane. Conversely these loci arise from critical points. Neither factor is repeated in the reduced branch divisor.

**Geometry of the two components.** The first equation is
\[
B=v^2-u^2(w-uv),
\]
so \((u,v,w)\mapsto(u,v,w-uv)\) identifies \(V(B)\) with the standard Whitney umbrella. Its partial derivatives vanish precisely when \(u=v=0\). The change of target coordinates \((u,v,w)\mapsto(u,S,T)\) is a triangular polynomial automorphism (the coefficients of \(v\) in \(S\) and of \(w\) in \(T\) are \(-64\) and \(512\)). Consequently, \(Q=(S^3-T^2)/1024\) is irreducible and its zero set is a cuspidal cylinder; the gradient of \(S^3-T^2\) vanishes exactly along \(S=T=0\). Substitution on \(L_Q\) gives \(B=-27u^8/4096\), proving \(L_Q\cap V(B)=\{0\}\). On \(L_B\), \(Q=-256w^2\), so \(L_B\cap V(Q)=\{0\}\).

**Intersection and contact orders.** On \(B=0\) with \(u\ne0\), eliminate \(w=(v^2+u^3v)/u^2\). Exact polynomial division gives
\[
u^4Q\big|_{B=0}=32(v+u^3)^3(u^4-8u^3-8v).
\]
The zero sets of the two factors are precisely \(C_{31}\) and \(C_{22}\) after substitution for \(w\). They are distinct and meet only at \(u=0\). On \(u=0\), simultaneous equations imply \(v=w=0\), so the two curves exhaust the intersection globally. The partial derivative \(\partial B/\partial w=-u^2\) is invertible along either curve away from the origin. Thus the displayed factorization on this smooth branch surface gives the generic local intersection lengths \(3\) and \(1\). Each curve is away from the cusp and Whitney singular lines except at the origin, so both components are smooth there.

**Fibre partitions.** On \(u\ne0\) the local algebras are governed by the multiplicities of roots of \(p\). On the intersection curves, substitution factors this polynomial as
\[
p|_{C_{31}}=x^3(x+u^2),\qquad
p|_{C_{22}}=x^2(x+u^2/2)^2.
\]
On the cusp line \(L_Q\), solving \(S=T=0\) gives
\[
v=\frac{9u^4-64u^3}{64},\quad
w=-\frac{u(27u^5-288u^4+512u^3-288uv+512v)}{512}.
\]
For \(u\ne0\), \(B=-27u^8/4096\ne0\), and \(p\) has a triple root at \(x=-3u^2/8\), detected by its first two vanishing derivatives and nonzero third derivative. Its remaining root is simple.

For a point of \(V(B)\) with \(u=v=0\) and \(w\ne0\), the fibre equations reduce to \(x^2=0\) and \(z^2=w\), giving two local length-two points. For \(u=0\), \(v\ne0\), \(Q=0\) means \(w^2=-v^3\): the two possible nonzero values of \(x\) with \(x^2=-v\) have one solution with \(z^2=0\) (length two) and the other with two distinct \(z\) values (both simple). At the origin the unique fibre is \(\operatorname{Spec}\mathbb C[x,z]/(x^2,z^2)\), of length four.

It remains to exclude other repeated-root patterns when \(u\ne0\). Away from \(B=0\), the only repeated roots of \(p\) are zeros of its cubic derivative factor. A repeated nonzero root becomes triple exactly on \(L_Q\) (the discriminant locus of this cubic factor); otherwise it is double. On \(B=0\), the origin root has order at least two and becomes triple only at \(v=-u^3\), while an additional double root appears precisely when \(v=u^3(u-8)/8\). The quartic has no root of multiplicity four for \(u\ne0\): its coefficient of \(x\) is zero, and a fourth-power polynomial with vanishing \(x\) coefficient has zero cubic coefficient, contrary to \(u^2\ne0\). The cases already exhausted show that any remaining branch fibre has one double and two simple points.

## Verification
The accompanying standalone `branch_strata_verify.py` is an exact symbolic identity checker over \(\mathbb Q\), using Python and SymPy. Execute `python branch_strata_verify.py`; success prints `BRANCH_COLLISION_EXACT_OK`. It checks the full Jacobian, the quartic discriminant factorization, the cusp coordinate identity, the intersection factorization, the two collision factorizations, the cusp-line triple root and the relevant specializations at \(u=0\). The global arguments about fibres, singular supports and generic intersection length are explained above; the checker is supporting algebra, not a substitute for proof.

## Relationship to prior work
Shi–Xu–Zuo introduce the specific polynomial map as a counterexample concerning the zero set of its Bernstein–Sato ideal. Their theorem and technical development concern differential operators, not this branch-collision classification. A separate earlier calculation identifies the degree-four covering, two branch components, their normalizations and full symmetric monodromy. The present result goes beyond those statements by identifying the second component as a polynomial cusp cylinder and determining the complete collision strata and the unequal intersection lengths \(3\) and \(1\). These local and incidence invariants do not follow from the mere count or normalization of branch components without an additional calculation.

## Limitations
The calculation does not describe the full scheme-theoretic branch conductor at the origin, equisingular deformations, integral structures, or the Bernstein–Sato ideal. The exact collision description is for the displayed map over \(\mathbb C\), not all polynomial maps with degree four. A broader implicit classification in the literature cannot be excluded solely by searches.

## References
Shi, Q.; Xu, Y.; Zuo, H., *Zero loci of Bernstein–Sato ideals are not necessarily linear*, arXiv:2610.04408v1 (first publicly posted 2026-10-03), Theorem 1.2 and Sections 2–4. https://arxiv.org/html/2610.04408v1
