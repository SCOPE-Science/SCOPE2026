# The anticanonical trichotomy for rectangular grid blow-ups

## Finding
Let \(k\) be an algebraically closed field of characteristic zero. Choose integers \(r,s\geq3\), distinct points \(a_1,\ldots,a_r\in\mathbf P^1_k\), and distinct points \(b_1,\ldots,b_s\in\mathbf P^1_k\). Let \(T_{r,s}\) be the blow-up of \(\mathbf P^1_k\times\mathbf P^1_k\) at the full rectangular grid \(\{(a_i,b_j):1\leq i\leq r,\ 1\leq j\leq s\}\). Set
\[
\delta(r,s)=4-(r-2)(s-2).
\]
The complete anticanonical trichotomy is:

1. If \(\delta(r,s)>0\), the anticanonical divisor \(-K_{T_{r,s}}\) is big, and its Iitaka dimension is \(2\).
2. If \(\delta(r,s)<0\), \(-K_{T_{r,s}}\) is not pseudo-effective. Every positive anticanonical multiple has zero sections, and its Iitaka dimension is \(-\infty\).
3. If \(\delta(r,s)=0\), then \((r,s)\) is one of \((3,6),(4,4),(6,3)\), and the graded section ring is
\[
R(T_{r,s},-K_{T_{r,s}}):=\bigoplus_{m\geq0}H^0(T_{r,s},\mathcal O(-mK_{T_{r,s}}))\ \cong\ k[z],
\]
with \(\deg z=3\) for \((3,6)\) and \((6,3)\), and \(\deg z=2\) for \((4,4)\). Thus the Iitaka dimension is \(0\). At each boundary pair the positive-degree sections have a unique fixed effective divisor, and for **every** closed point \(q\in T_{r,s}\) the further blow-up \(Y=\operatorname{Bl}_q(T_{r,s})\) has \(R(Y,-K_Y)=k\), equivalently no positive pluri-anticanonical sections.

In particular, the exceptional \(3\times6\) and \(6\times3\) grids have eighteen blown-up points yet retain a unique effective triple-anticanonical divisor, while grids beyond the stated hyperbolic wall have no pseudo-effective anticanonical class.

## Assumptions and scope
Write \(A,B\) for the two pulled-back ruling classes, normalized by \(A^2=B^2=0\) and \(A\cdot B=1\). Write \(E_{ij}\) for the exceptional curves, \(V_i\) for the proper transforms of the \(r\) vertical fibers, and \(H_j\) for the proper transforms of the \(s\) horizontal fibers. Hence
\[
K_T=-2A-2B+\sum_{i,j}E_{ij},\qquad
[V_i]=A-\sum_jE_{ij},\qquad [H_j]=B-\sum_iE_{ij}.
\]
The \(r+s\) curves \(V_i,H_j\) are pairwise disjoint; \(V_i^2=-s\), \(H_j^2=-r\). The result is valid for all choices of distinct grid coordinates, not just generic or transcendental ones. Pseudo-effectivity is taken in the closed real effective cone of the smooth projective surface.

## Proof
**A nef supporting class.** Let
\[
L=rA+sB-\sum_{i,j}E_{ij}.
\]
If \(F\) and \(G\) are the products of the \(r\) and \(s\) distinct linear forms defining the ruling fibers, the ideal of the grid is \((F,G)\) on \(\mathbf P^1\times\mathbf P^1\). Sections of \(\mathcal O(r,s)\) vanishing on the grid include \(F\cdot H^0(\mathcal O(0,s))\) and \(G\cdot H^0(\mathcal O(r,0))\). They have no common base point away from the grid. Near each grid point, \(F,G\) are independent regular parameters, and their initial linear forms span the conormal directions on the exceptional curve. Thus \(|L|\) is basepoint-free on the blow-up, so \(L\) is nef. Intersection gives
\[
L\cdot(-K_T)=2r+2s-rs=\delta(r,s).
\]
When \(\delta<0\), nefness excludes \(-K_T\) from the closed pseudo-effective cone, proving case 2.

**The big side.** When \(\delta>0\), the strict inequality
\[
1-\frac2s<\frac2r
\]
holds. Choose a rational \(\lambda\) strictly between these bounds and choose \(m\geq1\) such that \(a=m\lambda\), \(b=m(1-\lambda)\) are nonnegative integers. Then \(a+b=m\), \(2m-ra>0\), and \(2m-sb>0\). The effective divisor
\[
D_m=a\sum_iV_i+b\sum_jH_j
\]
has class \(raA+sbB-m\sum E_{ij}\), and hence
\[
-mK_T\sim D_m+(2m-ra)A+(2m-sb)B.
\]
The last two summands are the pullback of a positive-bidegree ample divisor on \(\mathbf P^1\times\mathbf P^1\), hence give a big divisor. A big divisor plus an effective divisor is big, proving case 1.

**The zero wall and complete section ring.** Suppose \(\delta=0\); equivalently \(1/r+1/s=1/2\). The only integer pairs with \(r,s\geq3\) are \((3,6),(4,4),(6,3)\). Let \(m>0\) and let \(D\) be an effective divisor linearly equivalent to \(-mK_T\). Its intersection with each \(V_i\) is \(-m(s-2)\). If \(a_i\) is the coefficient of \(V_i\) in \(D\), positivity of intersections of distinct irreducible curves gives
\[
a_i\geq\frac{m(s-2)}s.
\]
Since the pushforward of \(D\) has vertical degree \(2m\), its total multiplicity along the \(r\) vertical grid fibers is at most \(2m\). But the lower bounds already sum to \(rm(s-2)/s=2m\). Thus each coefficient equals \(a=m(s-2)/s\) and there is no spare vertical degree. The analogous horizontal argument gives coefficient \(b=m(r-2)/r\) on every \(H_j\) and consumes the entire horizontal degree. The identity \(1/r+1/s=1/2\) gives \(a+b=m\). Consequently, whenever \(a,b\) are integers, the effective divisor
\[
D=a\sum_iV_i+b\sum_jH_j
\]
has the complete class \(-mK_T\), and any other effective representative would differ from it by an effective numerically trivial divisor, necessarily zero. Otherwise no such divisor exists. The integrality conditions are precisely \(2\mid m\) in the \(4\times4\) case and \(3\mid m\) for the two \(3\times6\) orientations. This proves the claimed section rings.

**Loss after any further point blow-up.** In any nonzero boundary system the unique divisor is a positive combination of the pairwise disjoint smooth curves \(V_i,H_j\), each with coefficient strictly less than \(m\). Its multiplicity at an arbitrary closed point of \(T\) is therefore strictly less than \(m\). For \(\pi:Y=\operatorname{Bl}_q T\to T\), the canonical formula \(K_Y=\pi^*K_T+E_q\) shows that a section of \(-mK_Y\) would push forward to a divisor of \(|-mK_T|\) having multiplicity at least \(m\) at \(q\), a contradiction. There are no such sections for any \(m>0\).

## Verification
The standalone exact-arithmetic diagnostic `check_grid.py` tests the wall identity and the construction of integer witnesses over \(784\) parameter pairs \((r,s)\) with \(3\leq r,s\leq30\), and checks boundary generator degrees and point-multiplicity inequalities. Run `python3 check_grid.py` from this package directory; the expected terminal line begins `VERIFY_OK`. These finite tests validate the formulas but the universal theorem rests on the preceding geometric argument, not on enumeration.

## Relationship to prior work
Dinh, Oguiso, Yu, and Zhou (arXiv:2609.40045v1, first public 2026-09-30) study automorphisms of the \(4\times4\) grid blow-up and an additional point blow-up. Dinh, Oguiso, and Yu (arXiv:2106.05687v3, Lemma 2.1(3)) already prove that the \(4\times4\) grid surface has a unique bi-anticanonical divisor consisting of eight disjoint \((-4)\)-curves. That specific case is **not claimed as new**. The result here classifies *all* rectangular grids with \(r,s\geq3\), including the additional \(3\times6\) and \(6\times3\) boundary pairs, the sharp nef-supported non-pseudo-effective region, the big region, the complete graded rings on the boundary, and uniform disappearance under a further point blow-up. Earlier work on general-position blow-ups and symbolic powers concerns different incidence hypotheses; possible implicit coverage in broader effective-cone treatments remains a literature risk.

## Limitations
The trichotomy concerns rectangular Cartesian grids and their smooth point blow-ups, not arbitrary sets of \(rs\) points in \(\mathbf P^1\times\mathbf P^1\). It says nothing about minimal-model uniqueness, automorphism generation, rational polyhedrality of the whole effective cone, or anticanonical birational models outside this family. The statement of originality is relative to specifically checked literature, not a certification that no equivalent formulation exists.

## References
1. T.-C. Dinh, K. Oguiso, X. Yu, Q. Zhou, *A rational surface with discrete and non-finitely generated automorphism group*, arXiv:2609.40045v1 (first public 2026-09-30), https://arxiv.org/html/2609.40045v1.
2. T.-C. Dinh, K. Oguiso, X. Yu, *Smooth complex projective rational surfaces with infinitely many real forms*, arXiv:2106.05687v3, Lemma 2.1(3), https://arxiv.org/pdf/2106.05687.
3. American Mathematical Society, *MSC2020*, class 14J26 (rational and ruled surfaces), https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=14J26.
