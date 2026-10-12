# Derivation-rank polynomials of height-two incidence algebras recover graph girth

## Finding

Let \(G=(V,E)\) be a finite simple bipartite graph without isolated vertices, with bipartition \(V=V_{-}\sqcup V_{+}\). Form the height-two poset \(P_G\) in which \(s<t\) precisely when \(st\in E\), \(s\in V_{-}\), and \(t\in V_{+}\). Let \(A_G=I(P_G,\mathbb F_q)\), the incidence algebra over a finite field of any prime-power order \(q\). Every derivation is linear over \(\mathbb F_q\). Put \(m=|E|\), \(v=|V|\), and \(c(U)\) for the number of connected components of the spanning graph \((V,U)\), including isolated vertices. Write \(r(U)=v-c(U)\).

The complete operator-rank enumerator of the derivation space is
\[
\boxed{\mathcal D_{G,q}(z)=\sum_{\delta\in\operatorname{Der}_{\mathbb F_q}(A_G)}z^{\operatorname{rank}_{\mathbb F_q}(\delta)}=\sum_{\substack{L,U\subseteq E\\L\cap U=\varnothing}}[q(q-1)]^{|L|}(q-1)^{|U|}z^{|L|+r(U)}.}
\]
In particular, \(\dim_{\mathbb F_q}\operatorname{Der}(A_G)=2m\), and the distribution depends only on the underlying undirected graph. This is not merely a dimension formula: every coefficient counts actual derivations of the specified rank.

An equivalent Tutte-polynomial specialization makes the graph-theoretic structure explicit. With \(B=1+q(q-1)z\) and \(\rho=v-c(E)\), and with the standard graphic-matroid Tutte polynomial \(T_G(x,y)\),
\[
\boxed{\mathcal D_{G,q}(z)=B^m\left(\frac{(q-1)z}{B}\right)^\rho T_G\left(1+\frac{B}{(q-1)z},\,1+\frac{q-1}{B}\right).}
\]
The displayed rational expression is an identity of rational functions whose right side simplifies to the preceding polynomial; it is not a prescription to substitute \(z=0\) before cancellation.

The rank distribution recovers two fundamental cycle invariants. From \(\mathcal D_{G,q}(1)=q^{2m}\), it determines \(m\) when \(q\) is known. Let \(H_m(z)=(1+(q^2-1)z)^m\). If \(G\) is a forest then \(\mathcal D_{G,q}(z)=H_m(z)\), and conversely equality characterizes forests. If \(G\) contains a cycle, let \(g\) be its girth and let \(c_g\) denote the number of (unoriented) simple cycles of length \(g\). Then
\[
\boxed{[z^j](\mathcal D_{G,q}-H_m)=0\ \text{for all }0\le j<g-1,\qquad[z^{g-1}](\mathcal D_{G,q}-H_m)=c_g(q-1)^g.}
\]
Thus the first departure from the forest polynomial determines \(g\), and its coefficient determines \(c_g\). Since the graph is bipartite, any finite girth is even and at least four.

For a connected unicyclic graph whose unique cycle has length \(h\) and whose other \(b=m-h\) edges are bridges, the complete distribution reduces to
\[
\boxed{\mathcal D_{G,q}(z)=(1+(q^2-1)z)^b\left((1+(q^2-1)z)^h+(q-1)^h(z^{h-1}-z^h)\right).}
\]
This includes all even cycle lengths and all tree attachments, without restrictions on the characteristic.

## Assumptions and scope

The graph is finite, simple, bipartite, and has no isolated vertices, ensuring the poset has precisely two nonempty levels. Multiple components are allowed. The field is any \(\mathbb F_q\) of prime-power order, including characteristic two and nonprime extension fields. For an edgeless finite poset, the same formulas with \(m=0\) trivially give only the zero derivation, but edgeless posets are not needed in the main scope. Directed arrows always point from a minimal to a maximal poset vertex. The incidence algebra has a basis \(\{e_v:v\in V\}\cup\{a_e:e\in E\}\), with
\[
e_ve_w=\mathbf 1_{v=w}e_v,\qquad e_sa_{(s,t)}=a_{(s,t)}=a_{(s,t)}e_t,
\]
all other products involving two arrows or an inappropriate idempotent being zero. This is the path algebra of the oriented bipartite graph; no directed paths of length two exist. It has dimension \(v+m\), with radical spanned by the arrows and \(J^2=0\). Here \(\operatorname{rank}\delta\) always means rank of the linear operator \(\delta:A_G\to A_G\), not dimension or rank of the derivation space itself.

## Proof

**1. Parameterize all derivations.** Write \(J=\operatorname{span}_{\mathbb F_q}\{a_e\}\). Any derivation \(\delta\) of \(A_G\) satisfies \(\delta(1)=0\). From \(\delta(e_v^2)=\delta(e_v)e_v+e_v\delta(e_v)\), the coefficient of every diagonal idempotent in \(\delta(e_v)\) is zero: at \(e_v\) it obeys \(c=2c\), hence \(c=0\), in every characteristic, and at other idempotents the right side has no component. The idempotent equation also permits only arrows incident to \(v\). Differentiating \(e_se_t=0\) for distinct vertices forces their coefficients to be opposite on their common arrow. Thus, for uniquely determined \(b_e\in\mathbb F_q\),
\[
\delta(e_v)=\sum_{e=(s,v)}b_ea_e-\sum_{e=(v,t)}b_ea_e.
\]
Each arrow is \(a_e=e_sa_ee_t\); differentiation of this identity confines \(\delta(a_e)\) to \(e_sA_Ge_t=\mathbb F_qa_e\). Therefore \(\delta(a_e)=\lambda_ea_e\) for a unique \(\lambda_e\in\mathbb F_q\). Conversely, the displayed assignment for arbitrary \(b_e,\lambda_e\) respects the Leibniz rule on every product of basis elements: idempotent products are handled by the incidence signs, the only nonzero idempotent-arrow products by the scalar arrow rule, and products of two arrows vanish. Thus the assignment is a bijection \(\mathbb F_q^{2m}\to\operatorname{Der}(A_G)\).

**2. Determine the operator rank.** Relative to the ordered basis (vertex idempotents, arrows), \(\delta\) has zero top block and its arrow-row block is
\[
\bigl[\operatorname{diag}(b_e)\partial_G\ \big|\ \operatorname{diag}(\lambda_e)\bigr],
\]
where \(\partial_G\) is the \(m\)-by-\(v\) oriented edge-vertex incidence matrix, with entries \(-1\) at sources and \(+1\) at targets. Define \(L=\{e:\lambda_e\ne0\}\) and \(U=\{e:\lambda_e=0,\ b_e\ne0\}\). Rows indexed by \(L\) supply \(|L|\) pivot directions from the right block. Projecting away those rows leaves a nonzero row-scaled incidence matrix supported exactly on \(U\). The orientation is harmless, even when \(-1=1\), and every nonzero row scale is invertible. The incidence matrix of a finite undirected graph over any field has rank \(v-c(U)\): on each connected component the kernel consists exactly of functions constant on that component. Hence
\[
\operatorname{rank}\delta=|L|+v-c(U)=|L|+r(U).
\]
Each edge of \(L\) admits \(q-1\) nonzero values of \(\lambda_e\) and independently \(q\) values of \(b_e\); each edge of \(U\) has \(\lambda_e=0\) and \(q-1\) possible nonzero values of \(b_e\); each remaining edge has both zero. Summing these multiplicities proves the first formula. Its value at \(z=1\) is \((1+q(q-1)+(q-1))^m=q^{2m}\).

**3. Identify the Tutte specialization.** Sum over \(L\) outside a fixed \(U\), obtaining the polynomial identity
\[
\mathcal D_{G,q}(z)=B^m\sum_{U\subseteq E}\left(\frac{q-1}{B}\right)^{|U|}z^{r(U)}.
\]
Using the rank-generating definition
\[
T_G(x,y)=\sum_{U\subseteq E}(x-1)^{\rho-r(U)}(y-1)^{|U|-r(U)},
\]
substitution of \(x-1=B/((q-1)z)\) and \(y-1=(q-1)/B\), followed by multiplication by \(B^m((q-1)z/B)^\rho\), yields the stated specialization term by term. No assumptions about connectedness are used.

**4. Recover shortest cycles.** Compare the exact rank with the naive degree \(|L|+|U|\) obtained by pretending that all active incidence rows are independent. The generating polynomial for that naive degree is \(H_m(z)=(1+(q^2-1)z)^m\). The two degrees differ precisely when \(U\) contains a cycle. If the graph is a forest this never occurs. Conversely, if a cycle exists, let \(g\) be minimal. Every cyclic \(U\) contains at least \(g\) edges and its incidence rank is at least \(g-1\), since any contained simple \(g\)-cycle has \(g\) vertices and incidence rank \(g-1\). Adding nonzero \(L\) cannot decrease the actual rank. Therefore, for degrees below \(g-1\), the actual and naive enumerators coincide coefficientwise: all states producing either a naive or actual contribution in that range are forest states.

The states of actual rank exactly \(g-1\) whose naive rank is strictly larger must have \(L=\varnothing\), \(U\) equal to a shortest \(g\)-cycle, and all other edges inactive. Indeed extra active edges would either join a previously isolated vertex and increase rank or give a chord on that \(g\)-cycle, contradicting minimality of girth. A shortest cycle contributes \((q-1)^g\) such states (the independent nonzero \(b_e\) choices), while their naive degree is \(g\) rather than \(g-1\). No cyclic state has a naive contribution at degree \(g-1\), since it requires at least \(g\) active edges. Hence the coefficient of \(z^{g-1}\) in the difference is exactly \(c_g(q-1)^g\), strictly positive for all \(q\ge2\). The first-difference and reconstruction statements follow.

**5. Unicyclic factorization.** In a connected unicyclic graph, every subset \(U\) is independent in the graphic matroid unless it contains the entire unique \(h\)-cycle. The corresponding rank deficit is then exactly one. Each of the \(b\) bridge edges has three edge states with independent-degree enumerator \(1+(q^2-1)z\). For the cycle edges, the naive product has the same factor to the \(h\)th power; only the unique state assigning \(\lambda_e=0,b_e\ne0\) to all \(h\) cycle edges has to move weight \((q-1)^h\) from degree \(h\) to degree \(h-1\). This proves the last formula.

## Verification

An accompanying self-contained Python 3 standard-library program, `verify.py`, builds both a direct matrix for each derivation and the graph-component formula. Its direct enumerations cover all \(256\) derivations of the four-cycle over \(\mathbb F_2\), all \(6561\) over \(\mathbb F_3\), the six-cycle over \(\mathbb F_2\), a tree over two fields, a four-cycle with an attached bridge, and \(K_{2,3}\) over \(\mathbb F_2\). For the four-cycle over each of \(\mathbb F_2\) and \(\mathbb F_3\), the program also independently solves the full Leibniz linear-equation system for all linear maps \(A_G\to A_G\), confirming the predicted derivation-space dimension \(2m=8\). Additional component enumerations test girth and shortest-cycle multiplicity on \(K_{3,3}\).

For \(G=C_4\) over \(\mathbb F_2\), the exact polynomial is
\[\mathcal D_{C_4,2}(z)=1+12z+54z^2+109z^3+80z^4,\]
compared with \((1+3z)^4=1+12z+54z^2+108z^3+81z^4\); the coefficient difference at degree three is \((2-1)^4=1\), recovering the unique four-cycle. For \(K_{2,3}\), that difference is three, recovering its three four-cycles.

The finite enumerations test the implementation and representative small instances. The proof above, rather than any finite test, establishes the theorem for all finite simple bipartite graphs and all prime-power fields. The script checks prime fields of orders two and three; extension-field generality follows from the field-independent linear-algebra argument, not a separate extension-field computation.

## Relationship to prior work

Kenneth Baclawski's *Automorphisms and Derivations of Incidence Algebras* (1972) characterizes incidence-algebra derivations using inner and additive-function components, and gives derivation-space dimensions. Zhankui Xiao's *Jordan Derivations of Incidence Algebras* (arXiv:1411.6123, first posted 2014-11-22) also develops the general derivation normal form. These results explain why the first step is natural and are not claimed as new. The present statement concerns the rank of each derivation **as an operator on the algebra**, the exact distribution of those ranks over a finite field, its Tutte specialization, and recovery of girth and the count of shortest cycles; the inspected general-derivation statements do not supply these counts.

Krylov and Tuganbaev's *Derivations of Incidence Algebras* (arXiv:2305.02984; later published 2024) supplies more general structural descriptions of derivation modules; it is not an operator-rank enumeration. The known graphic-matroid rank definition of the Tutte polynomial is used without a claim of novelty. This graph specialization is a mathematical reduction from the proved rank formula, not evidence that an identical prior enumeration has been ruled out universally.

The 1972 article does not have a verified day-specific first-publication date in the consulted records. Its author-uploaded publicly accessible full text is timestamped 2014-06-07, which is the earliest day-verified public availability date among the primary sources used to seed the research direction. The year 1972 is acknowledged as the original publication year; 2014-06-07 is **not** represented as its original paper-publication date.

## Limitations

The theorem applies to finite simple bipartite height-two posets; additional comparable intervals or nonzero products of two radical arrows change the derivation matrices and are not covered. The graph is recovered only partially: the polynomial determines the number of edges, detects acyclicity, and recovers girth and its shortest-cycle multiplicity, but no complete graph-isomorphism reconstruction is asserted. Rank enumeration alone need not distinguish all graphs, and the theorem makes no claim about incidence-algebra automorphisms or general Jordan derivations. Exact priority among all historical equivalent Tutte specializations remains a bibliographic uncertainty; no independent mathematical audit or independent priority certification has been performed.

## References

1. K. Baclawski, *Automorphisms and Derivations of Incidence Algebras*, Proceedings of the American Mathematical Society **36** (1972), 351–356. DOI: 10.1090/S0002-9939-1972-0313133-8. Author-uploaded full text publicly timestamped 2014-06-07: https://www.researchgate.net/publication/243057171_Automorphisms_and_Derivations_of_Incidence_Algebras .
2. Z. Xiao, *Jordan Derivations of Incidence Algebras*, arXiv:1411.6123v1 (2014-11-22). https://arxiv.org/abs/1411.6123 .
3. P. Krylov and A. Tuganbaev, *Derivations of Incidence Algebras*, arXiv:2305.02984 (2023); Mathematics **12** (2024), article 999, DOI: 10.3390/math12070999. https://arxiv.org/abs/2305.02984 .
4. W. T. Tutte, *A contribution to the theory of chromatic polynomials*, Canadian Journal of Mathematics **6** (1954), 80–91. Used for standard graphic-matroid Tutte terminology, not for the new algebra-specific formula.
