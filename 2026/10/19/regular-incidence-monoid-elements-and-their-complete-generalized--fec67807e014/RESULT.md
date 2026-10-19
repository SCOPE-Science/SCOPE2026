# Regular incidence-monoid elements and their complete generalized-inverse spectrum

## Finding

Let \(P\) be any nonempty finite poset and \(q\) any prime power. A uniform formula determines, for every prescribed diagonal support, the number of von Neumann regular elements in its finite incidence algebra and the number of their inner, reflexive, and invertible inner inverses. In particular the regular-element count depends only on the undirected comparability graph and has an explicit first nontrivial asymptotic correction detecting incident edge pairs and triangles.

Write \(n=|P|\), \(E=\{(x,y):x<y\}\), \(m=|E|\), and \(N=n+m\). For \(T\subseteq P\), set \(Z=P\setminus T\), \(m_T=|E\cap(T\times T)|\), \(m_Z=|E\cap(Z\times Z)|\), and \(c_T=m-m_T-m_Z\). Let \(A=I(P,\mathbb F_q)\), and let \(\mathcal R_T\) consist of regular elements \(a\in A\) with \(a(x,x)\ne0\) exactly for \(x\in T\).

**Theorem.** Every element of \(\mathcal R_T\) has, in order, exactly
\[
\begin{aligned}
|\mathcal R_T|&=(q-1)^{|T|}q^{m-m_Z},\\
|\{b\in A:aba=a\}|&=q^{N-|T|-m_T},\\
|\{b\in A:aba=a,\ bab=b\}|&=q^{c_T},\\
|\{b\in A^\times:aba=a\}|&=q^{c_T+m_Z}(q-1)^{|Z|}.
\end{aligned}
\]
Moreover, each regular element has exactly one *commuting reflexive inverse* (the group inverse): exactly one \(b\in A\) satisfies \(aba=a\), \(bab=b\), and \(ab=ba\). The regular elements with fixed \(T\) form one double orbit under \(A^\times\times A^\times\), with representative the diagonal idempotent \(e_T\).

Consequently the complete regular-element count and ordered generalized-inverse pair counts are obtained by summing these formulas over all \(T\subseteq P\). For the undirected comparability graph \(G_P\), with \(w(G_P)=\sum_{v\in P}\binom{\deg(v)}2\) and \(\tau(G_P)\) triangles,
\[
\frac{|\{a\in A:\exists b,\ aba=a\}|}{q^N}
=1-\frac{m}{q^2}+\frac{m+w(G_P)-\tau(G_P)}{q^3}+O_P(q^{-4}).
\]
The equality of the entire regular-element counting polynomial for posets with isomorphic undirected comparability graphs follows from the exact finite sum (the inverse-fiber refinements may retain the orientation of the poset).

## Assumptions and scope

The incidence algebra consists of functions on intervals \((x,y)\) with \(x\le y\), with convolution \((ab)(x,z)=\sum_{x\le y\le z}a(x,y)b(y,z)\). Choose any linear extension to represent these functions as zero-pattern upper-triangular matrices. The algebra \(A\) has dimension \(N\), Jacobson radical \(J\) consisting of matrices with zero diagonal, and unit group consisting of matrices with all diagonal entries nonzero. "Regular" always means von Neumann regular **inside \(A\)**, not regular in the unrestricted full matrix algebra. The quantities above count actual elements and ordered pairs, not conjugacy classes. No condition on the characteristic or height of \(P\) is required. For a given support \(T\), all numbers of inverses are constant across \(\mathcal R_T\).

## Proof

**Step 1: A support-by-support criterion.** Fix \(T\) and put \(e=e_T=\sum_{x\in T}e_{xx}\) and \(f=1-e\). Decompose \(a\) into four Peirce blocks \(a_{11}=eae\), \(a_{12}=eaf\), \(a_{21}=fae\), \(a_{22}=faf\). All diagonal coordinates of \(a_{11}\) are nonzero, so \(u=a_{11}\) is invertible in the unital corner algebra \(eAe\). The usual block Gaussian elimination is valid **within \(A\)**: left and right multiplication by units reduces \(a\) to the block diagonal element \(u\oplus s\), where
\[
s=a_{22}-a_{21}u^{-1}a_{12}\in fAf.
\]
This is an exact identity in the Peirce decomposition, not an appeal to unrestricted elementary matrices. Every diagonal coordinate of \(s\) is zero; hence \(s\) belongs to the nilpotent radical \(fJf\) of \(fAf\). The element \(u\oplus s\) is regular iff \(s\) is regular in \(fAf\): apply \(f\) to any inner-inverse identity; the reverse direction uses the inverse of \(u\). If a radical element \(s\in fJf\) satisfies \(s=sbs\), then \(s\in(fJf)^2\), and recursively \(s\in(fJf)^{2^k}\) for every \(k\). Nilpotence forces \(s=0\). Thus
\[
a\text{ is regular inside }A\quad\Longleftrightarrow\quad a_{22}=a_{21}a_{11}^{-1}a_{12}.
\]
This is equivalent to \(a\in A^\times e A^\times\), and also equivalent to matrix rank \(|T|\) in the natural \(n\)-dimensional representation. (For a general nonregular incidence element its matrix rank can exceed the number of nonzero diagonal entries.)

**Step 2: Count regular elements.** The block \(a_{11}\) has exactly \(|T|\) nonzero diagonal choices and \(m_T\) arbitrary strict-interval coordinates, contributing \((q-1)^{|T|}q^{m_T}\). The blocks \(a_{12}\) and \(a_{21}\) contain altogether \(c_T\) free field coordinates. The Schur equation forces every coordinate of \(a_{22}\), including the \(m_Z\) off-diagonal coordinates, uniquely. Conversely these free choices always produce an element of \(A\), as the prescribed product lies in \(fAf\). Therefore \(|\mathcal R_T|=(q-1)^{|T|}q^{m_T+c_T}=(q-1)^{|T|}q^{m-m_Z}\). Distinct supports give disjoint nonempty double-unit orbits and exhaust all regular elements.

**Step 3: All inverse fibers.** For a regular \(a=u_0ev_0\), with \(u_0,v_0\) units of \(A\), the bijection \(b\mapsto v_0bu_0\) takes any of the three respective inverse conditions for \(a\) to the corresponding condition for \(e\); it preserves invertibility and the reflexive condition. Thus it suffices to count inverses of \(e\). Write \(b=\begin{psmallmatrix}B&X\\Y&W\end{psmallmatrix}\) in Peirce blocks, where \(B\in eAe\), \(X\in eAf\), \(Y\in fAe\), and \(W\in fAf\). The condition \(ebe=e\) is exactly \(B=e\), imposing \(|T|+m_T\) independent scalar constraints among the \(N\) coordinates of \(b\). Hence \(q^{N-|T|-m_T}\) inner inverses. With \(B=e\), the additional relation \(beb=b\) reads \(W=YX\), leaving precisely \(\dim(eAf)+\dim(fAe)=c_T\) free entries, hence \(q^{c_T}\) reflexive inverses. Finally \(b\) with \(B=e\) is a unit iff \(W-YX\) is a unit in \(fAf\), by the Schur complement. That corner has exactly \(q^{m_Z}(q-1)^{|Z|}\) units; choose \(X,Y\) independently to obtain \(q^{c_T+m_Z}(q-1)^{|Z|}\) unit inner inverses.

For the *commuting* reflexive inverse, work first with the idempotent \(e\): \(eb=be\) forces \(X=Y=0\), and reflexivity forces \(W=0\), so \(b=e\). General unit left/right equivalence need not preserve commutation; instead, use intrinsic linear algebra: the decomposition in Step 1 implies \(\operatorname{rank}a=|T|\) and the characteristic polynomial \(\prod_{x\in P}(t-a(x,x))\) has exactly \(|Z|\) zero roots counted with multiplicity. Thus \(0\) is a semisimple eigenvalue of \(a\), so its Drazin index is at most one. Its unique commuting reflexive inverse is a polynomial in \(a\) with zero constant term, obtained by Chinese-remainder interpolation modulo the minimal polynomial to act as the reciprocal on nonzero primary factors and zero on the zero-primary factor. This polynomial belongs to \(A\) and yields the unique group inverse.

**Step 4: Graph identity and asymptotics.** Summing Step 2 gives
\[
R_P(q)=\sum_{T\subseteq P}(q-1)^{|T|}q^{m-m_{P\setminus T}}.
\]
The exponent uses only the number of edges induced by the complementary vertex set of the undirected comparability graph; therefore it depends only on that graph. Divide by \(q^{n+m}\), write \(Z=P\setminus T\), and set \(p=q^{-1}\). This normalized quantity equals \(\mathbb E[q^{-e(G_P[Z])}]\), where each vertex independently belongs to \(Z\) with probability \(p\). Because \(q^{-e(G_P[Z])}=\prod_{\{i,j\}\in E(G_P)}(1-(1-p){\bf1}_{\{i,j\}\subseteq Z})\), expand the product. Single-edge terms contribute \(-mp^2+mp^3\). A pair of distinct edges on three vertices contributes \(p^3+O(p^4)\), and there are \(w(G_P)\) such pairs. A triple of edges on three vertices is exactly a triangle, contributing \(-p^3+O(p^4)\); every other collection of at least two edges uses four or more vertices and is \(O_P(p^4)\). This proves the stated expansion.

**Example distinguishing comparability graphs.** On four vertices, compare the height-two star \(0<1,\ 0<2,\ 0<3\) and the height-two fence \(0<2,\ 1<2,\ 1<3\). Both have \(n=4\), \(m=3\), and \(|I(P,\mathbb F_q)|=q^7\), but the regular-element polynomials are respectively
\[
\begin{aligned}
R_{\mathrm{star}}(q)&=q^7-3q^5+6q^4-7q^3+6q^2-3q+1,\\
R_{\mathrm{fence}}(q)&=q^7-3q^5+5q^4-4q^3+3q^2-2q+1.
\end{aligned}
\]
Over \(\mathbb F_2\) the counts are \(91\) and \(89\), respectively, while the ordered reflexive-inverse pair counts are \(341\) and \(337\). This demonstrates that equal poset size and equal incidence-algebra dimension do not determine the generalized-inverse spectrum.

## Verification

A standalone standard-library checker, `CHECK.py`, directly enumerates incidence-algebra elements and ordered inverse pairs using convolution. It tests every \(a,b\) for \(aba=a\), \(bab=b\), membership in the unit group and the commuting group-inverse condition. It compares all support-wise counts with the exact formulas over fields of orders \(2,3,4,5\). It checks the four-element star and fence, three-element chain and fork, two-element chain and antichain, including a nonprime field realization of \(\mathbb F_4\). The checker prints `ALL_INCIDENCE_INVERSE_SPECTRA_PASSED`. These finite enumerations corroborate but do not establish the general theorem, which follows from the algebraic argument above. Run with `python3 CHECK.py` in the extracted package directory.

## Relationship to prior work

Bilen Can (2021) analyzes incidence monoids as algebraic monoids, their automorphism groups, torus complexity, unit-group actions, and star-poset orbit geometry; its structural framework motivates the finite-field inverse statistics. Wright (online 2020, journal 2022) characterizes and implicitly counts regular **full upper-triangular** matrices, so upper-triangular regularity and its chain specialization are explicitly **prior work**, not asserted to be new here. Hartwig, Patrício, and Puystjens (2005) study diagonalization of regular triangular matrices by Peirce methods; the simple block elimination is likewise not claimed as novel. The additional statement assessed here is the uniform **all-poset, diagonal-support-resolved spectrum of three distinct generalized-inverse fibers**, and its comparability-graph counting consequence. Earlier formulas for isolated idempotents, general algebraic-monoid orbits, or total upper-triangular regular elements do not by themselves provide the stated three inverse-fiber multiplicities for arbitrary finite incidence algebras.

## Limitations

This is an enumeration of von Neumann regular elements only, not a count of inverses for nonregular elements. It applies to finite incidence algebras over fields; no assertion is made for arbitrary finite rings. The polynomial example and exhaustive checks are finite tests and are not uniqueness or priority proofs. Wright's highly relevant full article could not be obtained for complete inspection; its available abstract discusses upper-triangular generalized inverses and implicit counting, leaving possible priority overlap in chain cases. A fuller historical comparison with general Peirce inverse-enumeration work remains an originality risk; the claimed contribution is accordingly limited to the joint all-poset inverse-fiber spectrum and comparability-graph refinement. Independent audit has not been performed.

## References

1. M. Bilen Can, *Incidence Monoids: Automorphisms and Complexity*, 2021, arXiv:2105.09826 (first posted 2021-05-20), https://arxiv.org/abs/2105.09826.
2. S. E. Wright, *Constructing and counting regular triangular matrices*, *Linear and Multilinear Algebra* 70 (2022), 3936–3943, DOI:10.1080/03081087.2020.1857679 (public abstract available; full text not inspected).
3. R. E. Hartwig, P. Patrício and R. Puystjens, *Diagonalizing triangular matrices via orthogonal Pierce decompositions*, *Linear Algebra and its Applications*, DOI:10.1016/j.laa.2004.10.002 (abstract consulted).
