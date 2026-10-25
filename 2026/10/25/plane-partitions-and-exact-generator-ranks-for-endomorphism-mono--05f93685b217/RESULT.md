# Plane partitions and exact generator ranks for endomorphism monoids of full transformation semigroups

## Finding
Let \(\mathcal T_n\) be the full transformation semigroup on an \(n\)-element set, and write \(m(n)\) for the minimum size of a generating set of its semigroup endomorphism monoid \(\operatorname{End}(\mathcal T_n)\). For every integer \(n\ge5\), the following formal power series determine \(m(n)\) exactly.

For a series \(F(z)=\sum_{j\ge1} f_jz^j\) with nonnegative integer coefficients, define the multiset transform
\[
\mathscr M(F)(z)=\prod_{j\ge1}(1-z^j)^{-f_j}.
\]
Put
\[
A(z)=\frac{z}{1-z},\quad
B(z)=\frac{z^2}{(1-z)(1-z^2)},\quad
F_0(z)=A(z)\mathscr M(A)(z),\quad
F_1(z)=A(z)\mathscr M(A+B)(z).
\]
Let \(r_3(n)\) be the number of conjugacy orbits of rank-three semigroup endomorphisms of \(\mathcal T_n\); let \(r_2(n)\) be the number of *essential* rank-two conjugacy orbits, meaning those which cannot be produced by endomorphisms of larger rank. Then
\[
\boxed{\quad r_3(n)=[z^n]\big(\mathscr M(F_1)-\mathscr M(F_0)\big),\quad
r_2(n)=[z^n]\left(\prod_{j\ge1}(1-z^j)^{-j}-\prod_{j\ge1}(1-z^j)^{-1}\right).\quad}
\]
Consequently, if \(\operatorname{pp}(n)\) counts plane partitions of \(n\), and \(p(n)\) counts ordinary integer partitions, then
\[
\boxed{\quad m(n)=3+\operatorname{pp}(n)-p(n)+[z^n]\big(\mathscr M(F_1)-\mathscr M(F_0)\big),\qquad n\ge5.\quad}
\]
The initial exact values are \(m(5)=35\), \(m(6)=86\), \(m(7)=207\), \(m(8)=503\), \(m(9)=1206\), \(m(10)=2880\), \(m(11)=6808\), and \(m(12)=15996\). All products are locally finite as formal series: the coefficient of degree \(n\) requires only factors of degree at most \(n\).

## Assumptions and scope
The underlying set has \(n\ge5\) distinct elements. Endomorphisms here preserve composition but are not required to preserve the identity map. The *rank of a semigroup endomorphism* means the cardinality of its image in \(\mathcal T_n\); it is distinct from the minimum generator number \(m(n)\). The base algebraic description and minimal-generator reduction used below are established results of Gould, Grau, and Johnson, ultimately relying on Schein and Teclezghi. The new enumeration concerns conjugacy orbits and their essentiality, not a reproof of the structural classification.

Write compositions of transformations multiplicatively; the equations \(t^3=t\), \(e^2=e\), and \(te=et=e\) are independent of the choice of left-versus-right function notation. Simultaneous conjugation by the symmetric group classifies the orbits of the corresponding singular endomorphisms. In the established classification, the rank-three orbits correspond precisely to permissible pairs whose transformation \(t\) has a two-cycle. Every rank-two orbit corresponds to \(t^2=t\) and \(t\ne e\).

## Proof
**1. Functional-graph normal form.** By the permissible-pair classification, a singular endomorphism is represented uniquely by transformations \((t,e)\) such that
\[
t^3=t,\qquad e^2=e,\qquad te=et=e.
\]
Every functional-digraph component of \(t\) is either a fixed-point loop with zero or more incoming leaves, or a two-cycle with zero or more leaves incident to its two vertices. The map \(e\) fixes pointwise a nonempty subset of the fixed points of \(t\). It sends *every vertex in a given component of \(t\)* to a single such distinguished fixed point. Conversely, every structure of this form gives one permissible pair. Relabeling the underlying set gives precisely the simultaneous-conjugation action.

A distinguished \(e\)-fixed vertex together with its \(t\)-component (a fixed-point loop with an arbitrary number of leaves) has generating series \(A(z)=z/(1-z)\). A nondistinguished fixed-point component likewise has series \(A(z)\). A two-cycle with \(a\) and \(b\) leaves at its ends is determined up to isomorphism by the unordered pair \(\{a,b\}\); consequently its series is
\[
B(z)=z^2\sum_{0\le a\le b} z^{a+b}=\frac{z^2}{(1-z)(1-z^2)}.
\]
A fiber of \(e\) consists of its distinguished fixed-point component and a multiset of ordinary fixed-point and two-cycle components. Its type generating series is therefore \(F_1=A\mathscr M(A+B)\). The entire structure is a multiset of nonempty \(e\)-fibers, giving \(\mathscr M(F_1)\). Removing every two-cycle changes \(F_1\) to \(F_0=A\mathscr M(A)\), giving \(\mathscr M(F_0)\). Rank-three singular endomorphisms are characterized by the presence of a two-cycle. This proves the first coefficient formula for \(r_3(n)\).

**2. Precise essentiality criterion for rank two.** Suppose \(t^2=t\ne e\). The structural multiplication rule shows that a rank-two orbit is nonessential exactly when there is a permissible rank-three pair \((u,e)\) with \(u^2=t\), up to simultaneous conjugation. Such a \(u\) necessarily has a two-cycle \((a,b)\); since \(u^2=t\), both \(a,b\) are fixed by \(t\). Since \(ue=e\), \(u\) fixes every point in the image of \(e\), so neither \(a\) nor \(b\) is an \(e\)-fixed vertex. Since \(eu=e\), they have the same \(e\)-image. Thus one \(e\)-fiber contains at least two nondistinguished fixed-point components of \(t\).

Conversely, if distinct nondistinguished \(t\)-fixed vertices \(a,b\) have the same \(e\)-image, form \(u\) by swapping \(a,b\), directing every former \(t\)-leaf of \(a\) to \(b\) and every former \(t\)-leaf of \(b\) to \(a\), and leaving the other components of \(t\) unchanged. Then \(u^3=u\), \(u^2=t\), and \(ue=eu=e\). The associated rank-three orbit maps to the rank-two orbit by the established even-type product operation. Therefore *a rank-two orbit is essential if and only if each \(e\)-fiber contains at most one nondistinguished \(t\)-fixed component*.

**3. Plane partitions.** When two-cycles are forbidden, an essential rank-two fiber has its distinguished fixed-point component and either zero or one additional fixed-point component. Its type series is
\[
A(z)(1+A(z))=\frac{z}{(1-z)^2}=\sum_{j\ge1}jz^j.
\]
Taking a multiset of fibers produces the generating series \(\mathscr M(A(1+A))=\prod_{j\ge1}(1-z^j)^{-j}\), the classical MacMahon series for plane partitions. Structures with no additional fixed-point component in *any* fiber have \(t=e\), hence rank one, and are enumerated by \(\mathscr M(A)=\prod_{j\ge1}(1-z^j)^{-1}\), the ordinary partition series. Subtracting gives exactly the essential rank-two orbit count \(r_2(n)=\operatorname{pp}(n)-p(n)\).

**4. Minimal generator number.** The prior structural result (Gould–Grau–Johnson, Proposition 4.2) proves, for \(n\ge5\),
\[
m(n)=3+r_3(n)+r_2(n),
\]
where the three accounts are two generators for the unit group and the unique essential rank-one orbit. Substituting the two established orbit formulas gives the asserted complete expression. No asymptotic approximation is used.

## Verification
The standalone script `verify.py` uses only the Python standard library. It calculates the formal-series coefficients through degree twelve with integer arithmetic. Independently, for each of \(n=3,4,5,6\), it enumerates *actual transformation pairs* on a labeled set, checks all four defining composition equations, canonicalizes permissible pairs under the full symmetric group, and counts rank-three and essential rank-two orbits. For \(n\le5\), it also independently detects nonessential rank-two orbits by direct enumeration of all rank-three square roots instead of the fiber criterion. It obtains \((r_3,r_2)=(1,3),(4,8),(15,17),(46,37)\) for \(n=3,4,5,6\). These agree coefficientwise with the generating functions. The resulting values of \(m(n)\) for \(5\le n\le12\) are computed and printed. The script terminates with `VERIFY_OK` when all assertions hold. The smaller values \(n=3,4\) serve only as checks of the combinatorial orbit formulas; the minimum-generator theorem is claimed for \(n\ge5\).

## Relationship to prior work
Gould, Grau, and Johnson (2023 preprint; 2025 journal publication) classify the endomorphism-monoid structure and prove the reduction of the minimum generator size to rank-three and essential rank-two orbit counts. Their Section 4 explicitly raises the task of computing these orbit counts with generating functions; Section 8 reiterates this counting direction. The present contribution supplies those generating functions for all \(n\ge5\), a criterion deciding essentiality directly from the blue/red functional graph, and the previously unstated plane-partition/ordinary-partition difference. It does not claim novelty for the permissible-pair structural theorem or for MacMahon's identity. Schein and Teclezghi (1998) determine the endomorphisms and count labeled maps, a different statistic from the orbit-based minimum generator number. No claim of exhaustive literature priority is made.

## Limitations
The generator formula is restricted to \(n\ge5\); exceptional small-degree endomorphisms are excluded from the assertion. The multiset formula computes exactly but does not give a closed elementary expression for each coefficient or an asymptotic growth law. The source comparison used the complete available arXiv textual rendition of the 2023 preprint, the 2025 publication record, and the accessible descriptions of the 1998 classification; identical formulas elsewhere under colored functional-digraph or plane-partition terminology remain a residual originality risk. Exhaustive finite checks do not replace the all-degree proof.

## References
1. V. Gould, A. Grau, M. Johnson, *The structure of End(T_n)*, arXiv:2307.11596, publicly posted 21 July 2023; subsequently *Monatshefte für Mathematik*, DOI: 10.1007/s00605-025-02147-1. https://arxiv.org/abs/2307.11596
2. B. M. Schein, B. Teclezghi, *Endomorphisms of finite full transformation semigroups*, *Proceedings of the American Mathematical Society* 126 (1998), 2579–2587. DOI: 10.1090/S0002-9939-98-04764-9.
3. P. A. MacMahon, classical product identity for plane partitions: \(\sum_{n\ge0}\operatorname{pp}(n)z^n=\prod_{j\ge1}(1-z^j)^{-j}\). This identity is used for identification of the series, not the orbit-classification proof.
