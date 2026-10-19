# Conjugacy classes and cycle detection in unit groups of unicyclic incidence algebras

## Finding
Let \(P\) be a finite height-one poset whose undirected Hasse graph is connected and unicyclic. Let \(m\) be its number of cover edges and \(c\) the length of its unique cycle. Thus \(|P|=m\) and \(c\ge4\) is even. Write \(A(P,k)=I(P,k)\) for its incidence algebra and \(U(P,k)=A(P,k)^\times\).

**Structural classification.** Over every field \(k\), the algebraic group of units is isomorphic to
\[
\mathbb G_m\times \bigl(\mathbb G_a^m\rtimes T_{m,c}\bigr),\qquad
T_{m,c}=\left\{(w_1,\ldots,w_m)\in\mathbb G_m^m:
\prod_{i=1}^{c/2}w_{2i-1}=\prod_{i=1}^{c/2}w_{2i}\right\}.
\]
Here \(T_{m,c}\) acts diagonally on \(\mathbb G_a^m\) using coordinate weights \(w_1,\ldots,w_m\). In particular, the unit groups of any two such posets with the same \((m,c)\) are isomorphic, even if their incidence algebras are not.

**Arithmetic classification.** For every prime power \(q\), the number of conjugacy classes of \(U(P,\mathbb F_q)\) is
\[
\boxed{K_{m,c}(q)=q^m+(q-2)q^{m-c+1}.}
\]
Its order is \(q^m(q-1)^m\), and its element-commuting probability is
\[
\boxed{\operatorname{cp}(U(P,\mathbb F_q))
=\frac{1+(q-2)q^{1-c}}{(q-1)^m}.}
\]
For fixed \(q>2\), two groups in this unicyclic class are isomorphic **if and only if** their pairs \((m,c)\) agree. For \(q=2\), every such group is elementary abelian of order \(2^m\); its isomorphism type depends only on \(m\).

**Nonreconstruction example.** Let \(P_1,P_2\) have vertices \(0,1,2,3,4,5\), with the cover relations directed from the first vertex to the second:
\[
\begin{aligned}
E(P_1)&=\{01,21,23,03,04,05\},\\
E(P_2)&=\{01,21,23,03,04,25\}.
\end{aligned}
\]
Both have \(m=6,c=4\). Their undirected degree multisets are respectively \((4,2,2,2,1,1)\) and \((3,3,2,2,1,1)\). Hence their incidence algebras are neither isomorphic nor anti-isomorphic over any field, yet their algebraic unit groups are isomorphic over every field.

## Assumptions and scope
A height-one poset here has no strict chains of three elements; its Hasse graph is bipartite with edges going from minimal to maximal elements. The graph is assumed finite, simple, connected, and to have exactly one undirected cycle. There are no restrictions on the characteristic of \(k\), including characteristic two. The isomorphism assertion concerns groups of units, not isomorphism of associative algebras. For the finite-field *only-if* statement, the two unit groups are taken over the same fixed field \(\mathbb F_q\); no assertion compares different field sizes. All counts include the identity element and all conjugacy classes.

## Proof
**1. Multiplication and the weight action.** Since no two strict cover edges can be composed, the radical \(J\) of \(A(P,k)\), spanned by the cover matrix units, satisfies \(J^2=0\). The diagonal subalgebra is \(k^m\). Its invertible diagonal elements form the torus \(D=(\mathbb G_m)^m\), while \(1+J\cong\mathbb G_a^m\) is normal and abelian. Writing a unit uniquely as \((1+x)d\), the multiplication is
\[
(x,d)(y,e)=\bigl(x+dyd^{-1},de\bigr),
\qquad (dyd^{-1})_{a b}=\frac{d_a}{d_b}y_{a b}
\quad(a\prec b).
\]
Thus \(U(P,k)\cong\mathbb G_a^m\rtimes D\), where each cover edge \(a\prec b\) carries the multiplicative character \(w_{a b}(d)=d_a/d_b\).

**2. The single cycle relation.** Because the undirected graph is connected with \(m\) edges and \(m\) vertices, choose a spanning tree by deleting one cycle edge and choose a root vertex. Specifying a root value in \(\mathbb G_m\) and all edge ratios along the spanning tree recovers every diagonal value, by multiplication and inversion. These are inverse monomial maps, so they are isomorphisms of algebraic tori, not merely bijections of field-valued points. The omitted edge ratio is the alternating product of the others along the unique even cycle. Number the cycle edges in their cyclic order, with pendant edges following; the precise image of \(D\to\mathbb G_m^m\) is the split subtorus
\[
T_{m,c}=\{w:w_1w_3\cdots w_{c-1}=w_2w_4\cdots w_c\}.
\]
The kernel is the scalar diagonal \(\mathbb G_m\). The root coordinate splits that kernel. Hence \(D\cong\mathbb G_m\times T_{m,c}\), with the first factor acting trivially on \(J\). This proves the structural assertion. The description depends only on \(m,c\), not on the trees attached to the cycle.

**3. Commuting pairs.** Write \(G=U(P,\mathbb F_q)\) and \(D=(\mathbb F_q^\times)^m\). For any fixed \(d,e\in D\), elements \((x,d)\) and \((y,e)\) commute exactly when, for each edge \(i\),
\[
(1-w_i(e))x_i=(1-w_i(d))y_i.
\]
This equation has \(q^2\) solutions \((x_i,y_i)\) if both weights are one, and \(q\) solutions otherwise. Let \(h(d,e)\) be the number of edges with \(w_i(d)=w_i(e)=1\). The number of commuting ordered pairs in \(G\) is
\[
q^m\sum_{d,e\in D}q^{h(d,e)}.
\]
The usual conjugation orbit-count identity \(|\{(g_1,g_2)\in G^2:g_1g_2=g_2g_1\}|=|G|K(G)\) therefore gives
\[
K(G)=\frac{1}{|D|}\sum_{d,e\in D}q^{h(d,e)}
=\frac{q-1}{|T_{m,c}(\mathbb F_q)|}\sum_{w,z\in T_{m,c}(\mathbb F_q)}q^{h(w,z)}.
\]
The torus-image cardinality is \((q-1)^{m-1}\).

**4. Evaluation of the cycle constraint.** Set \(b=q-1\). Each pendant edge is an unconstrained coordinate in each of \(w,z\), contributing
\[
\sum_{u,v\in\mathbb F_q^\times}q^{\mathbf1_{u=v=1}}=b^2+b=bq.
\]
Let \(S_c\) be the corresponding double sum restricted to the \(c\) cycle coordinates, each satisfying the alternating product-one relation. Expand
\[
q^{h(w,z)}=\prod_{i=1}^{c}\left(1+b\mathbf1_{w_i=z_i=1}\right).
\]
For a specified set of \(j<c\) cycle coordinates fixed at one, exactly \(b^{c-j-1}\) tuples obey the cycle relation; for \(j=c\) there is exactly one. Consequently
\[
\begin{aligned}
S_c&=\sum_{j=0}^{c-1}\binom cj b^{j+2(c-j-1)}+b^c\\
&=b^{c-2}\bigl(q^c+q^2-2q\bigr).
\end{aligned}
\]
Combining the \(m-c\) pendant factors, \(S_c\), and the torus-image cardinality yields
\[
K(G)=\frac{b}{b^{m-1}}(bq)^{m-c}b^{c-2}(q^c+q^2-2q)
=q^{m-c}(q^c+q^2-2q),
\]
which equals the displayed formula. Since \(|G|=q^m(q-1)^m\), dividing \(K(G)\) by \(|G|\) gives the claimed commuting probability.

**5. Completeness of the finite-field classification.** Fix \(q>2\). The order \([q(q-1)]^m\) of the group determines \(m\); with \(m\) fixed, the class count \(q^m+(q-2)q^{m-c+1}\) strictly decreases as the even integer \(c\) increases. Thus a group isomorphism forces equal \(c\). Conversely Step 2 constructs an isomorphism for equal \((m,c)\). At \(q=2\) the diagonal group is trivial, hence \(U(P,\mathbb F_2)=1+J\cong(C_2)^m\), as claimed.

**6. Different associative algebras with the same units.** Both displayed posets are connected height-one unicyclic with \(m=6,c=4\), so Step 2 gives an isomorphism of their unit group schemes. Their degree multisets differ, so the posets are not isomorphic, even after reversing all relations. The standard incidence-algebra reconstruction theorem (Stanley, 1970, Theorem 1) implies that neither an algebra isomorphism nor an algebra anti-isomorphism can exist. This proves the final assertion.

## Verification
The standalone standard-library script `verify.py` enumerates diagonal torus elements over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), independently counts the solutions to their commutation equations, and compares the resulting class numbers with the general closed formula for a four-cycle, two nonisomorphic six-edge graphs containing a four-cycle, and a six-cycle. It also constructs the torus isomorphism between the two six-vertex four-cycle examples explicitly and checks its injectivity, multiplicativity, and weight preservation. For \(\mathbb F_3\), the two nonisomorphic six-edge examples each give \(756\) conjugacy classes, while the six-cycle example gives \(732\). The script prints `VERIFY_OK` when all tests succeed. Finite tests corroborate, but do not replace, the general proof.

## Relationship to prior work
Stanley's *Structure of incidence algebras and their automorphism groups* (1970) proves that a poset can be recovered from its incidence algebra, which supplies the algebra nonisomorphism criterion used here; that theorem does not classify groups of units with coincident isomorphism types. Baclawski's *Automorphisms and derivations of incidence algebras* (1972), Section 3, uses the unit group to describe **inner automorphisms of a fixed incidence algebra**. It does not compute the conjugacy-class number of that unit group or classify cross-poset unit-group isomorphisms. Joseph's (2002) directed-graph treatment gives algebraic models for incidence algebras, not this finite-field class enumeration. Quinn's (2013) path-algebra presentation treats Gröbner bases and shellability rather than unit-group conjugacy.

Rossmann's *Enumerating conjugacy classes of graphical groups over finite fields* studies graph-associated class-two nilpotent groups defined by central commutator relations among vertex generators. Those groups are not the generally nonnilpotent semidirect products \(\mathbb G_a^m\rtimes T_{m,c}\) considered here. Existing forest-poset Lie-reduct and joint-centralizer formulas rely on the independence of edge characters; the present unicyclic character dependence is precisely the missing obstruction and does not follow from the forest case by substituting parameters. Targeted searches found no published result with the same group-isomorphism classification and unicyclic class-number formula; absence of a search result is not proof of uniqueness.

## Limitations
The group-isomorphism sufficiency theorem holds over all fields; its necessary condition from conjugacy counts is asserted only within the class of unicyclic height-one posets over a fixed finite field of size exceeding two. It does not characterize the unit groups of arbitrary posets, graphs with multiple cycles, or groups over distinct fields. The count is for ordinary conjugacy classes in the finite **unit group**, not inner-derivation ranks in the incidence algebra and not automorphisms of the incidence algebra. An independent mathematical audit has not been performed, and equivalent unlocated literature is an originality risk.

## References
1. R. P. Stanley, *Structure of incidence algebras and their automorphism groups*, Bulletin of the American Mathematical Society **76** (1970), 1236–1239. Theorem 1.
2. K. Baclawski, *Automorphisms and derivations of incidence algebras*, Proceedings of the American Mathematical Society **36** (1972), 351–356, Section 3. DOI: 10.1090/S0002-9939-1972-0313133-8.
3. A. Joseph, *On incidence algebras and directed graphs*, International Journal of Mathematics and Mathematical Sciences **31** (2002), 301–305. DOI: 10.1155/S0161171202007925.
4. D. Quinn, *The incidence algebra of posets and acyclic categories*, Kyushu Journal of Mathematics **67** (2013), 117–127. DOI: 10.2206/kyushujm.67.117.
5. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, available open manuscript, https://torossmann.github.io/files/csp.pdf.
