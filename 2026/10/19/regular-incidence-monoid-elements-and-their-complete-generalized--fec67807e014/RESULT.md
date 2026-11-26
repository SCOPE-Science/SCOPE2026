# Regular incidence-monoid elements and their generalized-inverse counts

## Finding

Let \(P\) be a nonempty finite poset, \(q\) a prime power, and \(A=I(P,\mathbb F_q)\) its incidence algebra. Write \(n=|P|\), \(E=\{(x,y):x<y\}\), \(m=|E|\), and \(N=n+m\). For a prescribed nonzero diagonal support \(T\subseteq P\), put \(Z=P\setminus T\), let \(m_T,m_Z\) count strict comparable pairs inside the respective sets, and let \(c_T=m-m_T-m_Z\) count crossing pairs. Write \(\mathcal R_T\) for the regular elements of support \(T\). Then
\[
 |\mathcal R_T|=(q-1)^{|T|}q^{m-m_Z}.
\]
For each \(a\in\mathcal R_T\) the counts of inner, reflexive, and invertible inner inverses are respectively
\[
\begin{aligned}
 |\{b\in A:aba=a\}|&=q^{N-|T|-m_T},\\
 |\{b\in A:aba=a,\ bab=b\}|&=q^{c_T},\\
 |\{b\in A^\times:aba=a\}|&=q^{c_T+m_Z}(q-1)^{|Z|}.
\end{aligned}
\]
There is exactly one commuting reflexive inverse (the group inverse). For each support the regular elements form one double-unit orbit with representative the diagonal idempotent \(e_T\).

All of these numerical counts, including the support-wise inverse multiplicities, are determined by the undirected comparability graph \(G_P\), with supports matched by a graph isomorphism. For the total count sum \(|\mathcal R_T|\) over supports; for total ordered inverse-pair counts multiply each multiplicity by \(|\mathcal R_T|\) before summing. This counts inverse elements; it does not identify them across different transitive orientations. If \(w(G_P)=\sum_v\binom{\deg(v)}2\) and \(\tau(G_P)\) is the number of triangles, the regular fraction satisfies, for fixed \(P\),
\[
 \frac{\sum_T|\mathcal R_T|}{q^N}=1-\frac{m}{q^2}+\frac{m+w(G_P)-\tau(G_P)}{q^3}+O_P(q^{-4}).
\]

## Assumptions and scope

Use incidence convolution \((ab)(x,z)=\sum_{x\le y\le z}a(x,y)b(y,z)\). A linear extension embeds \(A\) into upper-triangular matrices with zeros at incomparable pairs. Its nilpotent radical consists of the zero-diagonal matrices; its units are exactly the matrices with all diagonal entries nonzero. Regularity and the inverse conditions are imposed inside \(A\). Counts refer to actual elements and ordered pairs, not conjugacy classes.

## Proof

**Regularity and support.** Put \(e=e_T\), \(f=1-e\), and write the Peirce blocks of \(a\) as \(u=eae\), \(x=eaf\), \(y=fae\), \(z=faf\). The corner element \(u\) is a unit of \(eAe\). Multiplying on the left by \(1-yu^{-1}\) and on the right by \(1-u^{-1}x\) isolates the diagonal blocks \(u\) and \(s=z-yu^{-1}x\). These multipliers are units of \(A\) since the off-block terms square to zero. The element \(s\) has zero diagonal and belongs to the nilpotent radical of \(fAf\). Inner-inverse existence for the block diagonal element implies \(s=sbs\) for some \(b\) in the corner. This puts \(s\) in successively doubled powers of the radical and hence forces \(s=0\). Conversely \(u\oplus 0\) is regular. Thus \(z=yu^{-1}x\) is necessary and sufficient. It is also equivalent to ambient matrix rank \(|T|\), and the block operations put every regular element into the double-unit orbit of \(e\). Diagonal supports are preserved by multiplying by units. Empty corners are interpreted as zero-dimensional; in particular \(T=\varnothing\) gives just the zero regular element, and \(T=P\) gives all units.

There are \(q-1\) choices for each of the \(|T|\) nonzero diagonal coordinates in \(u\) and \(q^{m_T}\) choices for its other entries. The two crossed blocks have \(c_T\) free coordinates together and determine \(z\) uniquely by the Schur equation. This gives the stated support-wise count.

**Inverse counts.** If \(a=u_0 e v_0\) with \(u_0,v_0\) units, then \(b\mapsto v_0bu_0\) transports the inner and reflexive inverse conditions to those for \(e\) and preserves invertibility. For \(e\), write \(b\) as \(\begin{psmallmatrix}B&X\\Y&W\end{psmallmatrix}\). The inner equation requires exactly \(B=e\), prescribing \(|T|+m_T\) coordinates. The reflexive equation further prescribes \(W=YX\) with no new constraint on the crossed blocks. Invertibility instead requires that \(W-YX\) be a unit of \(fAf\), which has \((q-1)^{|Z|}q^{m_Z}\) units. These give the three claimed multiplicities.

Commutation is not transported by general left/right unit equivalence. Instead, the ambient matrix \(a\) has nullity \(|Z|\), which equals the algebraic multiplicity of zero in its triangular characteristic polynomial. Thus the zero primary part is semisimple. The matrix group inverse acts as zero there and as the ordinary inverse on the complementary invertible part. This action is forced by the commuting reflexive equations and is a polynomial in \(a\), by interpolation modulo its minimal polynomial (or by Cayley–Hamilton when \(a\) is invertible). It therefore lies in \(A\).

**Graph formula and asymptotics.** Every exponent in the counts depends only on support sizes and induced or crossing undirected edge counts. In particular the total regular count is \(\sum_{T}(q-1)^{|T|}q^{m-m_{P\setminus T}}\). With \(p=q^{-1}\), divide this sum by \(q^N\); the result is \(\mathbb E[p^{e(G_P[Z])}]\) when vertices enter \(Z\) independently with probability \(p\). Expand the product over edges of \(1-(1-p){\bf 1}_{\{i,j\}\subseteq Z}\). An edge contributes \(-p^2+p^3\), an incident pair contributes \(p^3+O(p^4)\), and a triangle contributes \(-p^3+O(p^4)\). All other nonempty collections use at least four vertices and contribute \(O_P(p^4)\) in total. This proves the expansion.

## Example and reproduction

On four vertices, the star \(0<1,0<2,0<3\) and fence \(0<2,1<2,1<3\) both have \(n=4,m=3\). The regular-count polynomials are, respectively,
\[
 q^7-3q^5+6q^4-7q^3+6q^2-3q+1,\qquad
 q^7-3q^5+5q^4-4q^3+3q^2-2q+1.
\]
Over \(\mathbb F_2\) the regular counts are 91 and 89, and the ordered reflexive-inverse counts are 341 and 337. Thus equal ambient dimension and equal poset size do not fix these counts. The accompanying unchanged `CHECK.py` checks the formulas by finite convolution enumeration, including the two examples and specified other fields and posets. The enumeration corroborates the formulas only in its finite test cases.

## Relationship to prior work and limitations

Bilen Can, *Incidence Monoids: Automorphisms and Complexity* (arXiv:2105.09826v1), studies incidence monoids and their double-unit actions, including orbit geometry for a star. S. E. Wright, *Constructing and counting regular triangular matrices* (DOI 10.1080/03081087.2020.1857679), addresses the full upper-triangular case; its detailed chain-case coverage has not been resolved here. R. E. Hartwig, P. Patrício and R. Puystjens, *Diagonalizing triangular matrices via orthogonal Pierce decompositions* (DOI 10.1016/j.laa.2004.10.002), is related to the block method. Neither the block method nor upper-triangular regularity is claimed as new. The Resultary record `6c54ef06a12b` on tree-shaped incidence algebras overlaps the height-at-most-two regular totals and the star/fence example, but does not give the joint inverse multiplicities. The scope here is the joint numerical spectrum for arbitrary finite posets over finite fields and its comparability-graph consequences. The formulas do not describe the actual inverse sets across different orientations or assert an analogue for arbitrary finite rings.
