# Finite-field multiplication-rank spectra of graph face algebras

## Finding
Let \(G=(V,E)\) be a finite simple graph with \(n=|V|\ge1\), \(m=|E|\), and \(k=\mathbb F_q\), where \(q\) is any prime power of characteristic \(p\). Form the Artinian squarefree face algebra of the one-dimensional simplicial complex \(G\):
\[
A_G=k[x_v:v\in V]/(x_v^2,\ x_ux_v:\{u,v\}\notin E,\ x_ux_vx_w:u,v,w\text{ distinct}).
\]
Its natural basis consists of \(1\), all \(x_v\), and all \(y_{uv}=x_ux_v\) with \(\{u,v\}\in E\), so \(\dim_k A_G=d=1+n+m\). For \(a\in A_G\), let \(M_a:b\mapsto ab\) and define the complete multiplication-rank enumerator
\[
R_{G,q}(T)=\sum_{a\in A_G} T^{\operatorname{rank}_k M_a}.
\]
For nonempty \(S\subseteq V\), let \(z_G(S)=|V\setminus(S\cup N_G(S))|\). Define \(c_p(S)\) as the number of connected components of the induced graph \(G[S]\) if \(p=2\), and as the number of its **bipartite** connected components if \(p\ne2\); isolated vertices count as bipartite components. Then, for every \(G\) and every finite field,
\[
\boxed{R_{G,q}(T)=1+(q^m-1)T+(q-1)q^{n+m}T^d
 +q^m\sum_{\varnothing\ne S\subseteq V}(q-1)^{|S|}T^{1+n-z_G(S)-c_p(S)}.}
\]
This is the **exact** distribution of annihilator dimensions as well: each element of multiplication rank \(r\) has an annihilator of cardinality \(q^{d-r}\).

Write \(b(G)\) for the number of bipartite connected components of \(G\) and \(c(G)\) for the total number of components. Among all elements of the maximal ideal of \(A_G\), the maximum multiplication rank is exactly
\[
\boxed{1+n-b(G)\quad(p\ne2),\qquad 1+n-c(G)\quad(p=2).}
\]
Thus the top nonunit multiplication rank detects, for odd characteristic, the number of bipartite connected components, and for characteristic two the number of all connected components.

For the cycle graph \(C_n\), \(n\ge3\), the entire enumerator can instead be computed through a fixed \(4\times4\) transfer matrix, independently of \(n\). Put
\[
M(t,z)=\begin{pmatrix}
z&1&0&0\\0&0&tz&tz\\1&1&0&0\\0&0&t&t
\end{pmatrix},\qquad
\delta_{p,n}=\begin{cases}1,&p=2\text{ or }n\text{ even},\\0,&p\ne2\text{ and }n\text{ odd}.\end{cases}
\]
The weighted support-nullity polynomial satisfies
\[
\boxed{P_{C_n,p}(t,z)=\operatorname{tr}(M(t,z)^n)+\delta_{p,n}t^n(z-1).}
\]
Here \(P_{C_n,p}(t,z)=\sum_{S\subseteq V(C_n)}t^{|S|}z^{z_{C_n}(S)+c_p(S)}\), with \(z_{C_n}(\varnothing)=n\) and \(c_p(\varnothing)=0\). Consequently the full ring rank enumerator for \(C_n\) is
\[
R_{C_n,q}(T)=1+(q^n-1)T+(q-1)q^{2n}T^{2n+1}
+q^n T^{n+1}\big(P_{C_n,p}(q-1,T^{-1})-T^{-n}\big).
\]
The formal Laurent expression on the right simplifies to an ordinary polynomial. For odd cycles, the only support on which characteristic two changes the nullity relative to odd characteristic is the full support.

## Assumptions and scope
The graph is finite, simple, undirected and has at least one vertex; isolated vertices are allowed. The field can be prime or nonprime, including characteristic two. The graph is treated as a one-dimensional simplicial complex even when it has triangles, so all degree-three monomials vanish. Multiplication rank is for the entire unital algebra, not just its degree-one component. No claim is made that the polynomial alone determines the graph up to isomorphism.

## Proof
**1. Algebra and block structure.** In the displayed quotient, all monomials of degree three or greater vanish; the remaining monomials give the asserted basis. Write an arbitrary element uniquely as \(a=\alpha+u+w\), with \(\alpha\in k\), \(u=\sum_{v\in V}a_vx_v\), and \(w\) in the span \(W\) of edge monomials. If \(\alpha\ne0\), the element is a unit (the positive-degree ideal is nilpotent), hence \(\operatorname{rank}M_a=d\). There are \((q-1)q^{n+m}\) such elements. If \(\alpha=0\) and \(u=0\), multiplication has rank zero for \(w=0\), and rank one for each of the other \(q^m-1\) choices of \(w\).

**2. Kernel of the degree-one multiplication map.** Suppose \(u\ne0\), and let \(S=\{v:a_v\ne0\}\). Multiplying a degree-one element \(b=\sum b_vx_v\) by \(u\) gives, at edge \(\{i,j\}\), the coefficient \(a_i b_j+a_j b_i\). If \(j\notin S\) has a neighbor in \(S\), its coefficient \(b_j\) must vanish; if \(j\notin S\cup N_G(S)\), it is free. For \(i\in S\), write \(b_i=a_i h_i\). Each edge of \(G[S]\) then imposes \(h_i+h_j=0\). On a connected component these equations admit exactly one dimension of solutions when \(p=2\), whereas in odd characteristic they admit one dimension precisely if that component is bipartite (and otherwise only the zero solution, by following an odd cycle). Thus the kernel of \(L_u:A_{G,1}\to A_{G,2}\) has dimension \(z_G(S)+c_p(S)\). Accordingly \(\operatorname{rank}L_u=n-z_G(S)-c_p(S)\). Since \(M_a(1)=u+w\) has a nonzero degree-one part, it is independent of the image \(L_u(A_{G,1})\subseteq W\). Hence \(\operatorname{rank}M_a=1+n-z_G(S)-c_p(S)\), independently of \(w\) and of the nonzero values of the \(a_v\).

**3. Enumerating fibers.** A fixed nonempty support \(S\) occurs for exactly \((q-1)^{|S|}\) degree-one coefficient vectors, and each admits \(q^m\) choices of \(w\). Summing their ranks together with the unit, degree-two, and zero cases proves the rank enumerator. Rank-nullity yields the annihilator-cardinality statement. The coefficients sum to \(q^{1+n+m}\): the nonunit terms total \(q^{n+m}\) and the unit term has coefficient \((q-1)q^{n+m}\).

**4. Sharp maximum.** Within any connected bipartite component of \(G\), every support either omits the entire component (leaving at least one unconstrained outside vertex) or meets it (contributing at least one bipartite component of the induced support). Thus \(z_G(S)+c_p(S)\ge b(G)\) for odd characteristic. In characteristic two the same argument gives \(z_G(S)+c_p(S)\ge c(G)\). Full support \(S=V\) realizes equality in both inequalities, proving the sharp maxima.

**5. Cycles.** Encode a support by a binary cyclic word \(s_1\ldots s_n\), where a one means membership in \(S\). For proper nonempty support, every one-run is a path component and contributes one to \(c_p(S)\). Each zero-run of length \(\ell\) contributes \(\max(\ell-2,0)\) vertices to \(z_G(S)\). These contributions can be counted as transitions \(01\) and triples \(000\), respectively. The same triple rule gives exponent \(n\) for the empty support. Use the ordered pair of consecutive bits as a four-state transfer system: the transition \((a,b)\to(b,c)\) has weight \(t^b z^{[a=b=c=0]+[a=0,b=1]}\). Its matrix, in state order \(00,01,10,11\), is precisely \(M(t,z)\). The trace of its \(n\)-th power counts every labeled cyclic binary word with its proper-support weight exactly once. Only the all-one word needs correction: the transfer system assigns exponent zero, while \(G[S]=C_n\) contributes one component to \(c_p(S)\) if and only if \(p=2\) or \(n\) is even. This yields the correction \(\delta_{p,n}t^n(z-1)\). Removing the empty support and inserting the count of each nonempty support proves the displayed cycle rank formula.

## Verification
Run `python verify.py` with Python 3 (standard library only). It constructs and row-reduces the **full multiplication matrices** for every algebra element in ten small graph/field instances, using native arithmetic for prime fields and the quotient \(\mathbb F_2[h]/(h^2+h+1)\) for \(\mathbb F_4\). It independently computes the graph-support formula and checks exact rank frequencies and total algebra sizes. It also checks the cycle transfer identity independently against direct support enumeration for lengths \(3\) through \(8\), both characteristics and three numerical specializations. The run ends `VERIFY_OK` on successful completion. These finite checks corroborate, but do not replace, the universal algebraic proof.

## Relationship to prior work
Cook and Nagel (2015) develop a combinatorial Lefschetz analysis of monomial Artinian quotients. Boij, Migliore, Miró-Roig, and Nagel (2016) study non-Lefschetz loci, including complete intersections. More directly, Dao and Nair (2021) show that multiplication by a **generic** degree-one form in a squarefree face algebra is governed by the graph's incidence-matrix rank; Holleben (2023) extends weak-Lefschetz criteria and analyzes positive characteristic. These precedents provide the exact incidence-rank ingredient and motivate graph-dependent multiplication maps. The contribution here is the **all-element finite-field rank distribution**, including zero/support/degree-two strata and a fixed-state full distribution for every cycle. The classical incidence-matrix rank and generic Lefschetz criteria are not claimed as new.

## Limitations
The arbitrary-graph formula is a finite support sum and need not have a simpler closed form for general graphs; the transfer simplification is proved specifically for cycles. The proof concerns only the defined degree-three-truncated squarefree graph face algebras, not all Stanley–Reisner algebras. Search and source inspection cannot exclude an equivalent rank enumerator in all literature. No independent mathematical audit or proof-assistant certification has been performed.

## References
- D. Cook II and U. Nagel, *The weak Lefschetz property for monomial ideals of small type*, arXiv:1507.03853, first posted 2015-07-14. https://arxiv.org/abs/1507.03853
- M. Boij, J. Migliore, R. M. Miró-Roig and U. Nagel, *The non-Lefschetz locus*, arXiv:1609.00952, first posted 2016-09-04. https://arxiv.org/abs/1609.00952
- H. Dao and R. Nair, *On the Lefschetz property for quotients by monomial ideals containing squares of variables*, arXiv:2112.09434, first posted 2021-12-17, especially Section 3. https://arxiv.org/abs/2112.09434
- T. Holleben, *The weak Lefschetz property and mixed multiplicities of monomial ideals*, arXiv:2306.13274, first posted 2023-06-23. https://arxiv.org/abs/2306.13274
