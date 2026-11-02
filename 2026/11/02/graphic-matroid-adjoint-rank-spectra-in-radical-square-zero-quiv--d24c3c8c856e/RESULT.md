# Graphic-matroid adjoint-rank spectra in radical-square-zero quiver algebras

## Finding
Let \(Q\) be any finite quiver with no loops and at most one arrow between each *unordered* pair of distinct vertices. Its underlying undirected graph \(G=(V,E)\) is therefore simple; isolated vertices are allowed. Fix any finite field \(k=\mathbb F_q\), including characteristic two, and let \(A=kQ/J^2\), where \(J\) is the ideal spanned by arrows. Write \(n=|V|\), \(m=|E|\), and \(c(G)\) for the number of connected components, including isolated vertices. For each spanning edge subset \(F\subseteq E\), put
\[
 r_G(F)=n-c(V,F),
\]
its graphic-matroid rank. The full inner-derivation rank enumerator is
\[
 \boxed{D_Q(q,z)=\sum_{\delta\in\operatorname{InnDer}_k(A)}z^{\operatorname{rank}_k\delta}
 =\sum_{\substack{F,S\subseteq E\\F\cap S=\varnothing}}
 (q-1)^{|F|}q^{r_G(E)-r_G(F\cup S)}
 z^{r_G(F)}(qz)^{m-|F|-|S|}(1-qz)^{|S|}.}
\]
Although its displayed form contains signed factors, it has nonnegative integer coefficients. In particular it depends only on the graphic cycle matroid of \(G\), not on the orientation of \(Q\) or on a particular graph presentation of that matroid.

For any **forest** on \(m\) edges, irrespective of its shape or number of isolated vertices,
\[
 \boxed{D_Q(q,z)=(1+(q^2-1)z)^m.}
\]
For any **connected unicyclic graph** with \(m\) edges and cycle length \(\ell\ge3\), with trees attached in arbitrary ways,
\[
 \boxed{D_Q(q,z)=(1+(q^2-1)z)^{m-\ell}
 \left[\frac{(1+(q^2-1)z)^\ell+(q-1)(1-z)^\ell}{q}
 +(q-1)^\ell(z^{\ell-1}-z^\ell)\right].}
\]
The formulas apply to odd and even cycles and do not require \(q\) to be prime. Thus they give every rank multiplicity for the entire forest and unicyclic families, and an exact rank-matroid expansion for every allowed quiver.

One derived invariant is the probability that two uniform independent elements of \(A\) commute:
\[
 \Pr(XY=YX)=q^{-(n+m-c(G))}D_Q(q,q^{-1}).
\]
For a forest this specializes to \(\big((q^2+q-1)/q^3\big)^m\). These are probability statements about the associative algebra \(A\), not about its multiplicative unit group.

## Assumptions and scope
The algebra is the path algebra modulo all paths of length at least two, not a full path algebra if the quiver has composable arrows. If \(m=0\), \(A\cong k^n\) is commutative and \(D_Q=1\); the empty quiver is also allowed with \(D_Q=1\). Each arrow has two distinct endpoints, and two different arrows cannot join the same unordered pair. The sole restriction on the coefficient field is finiteness. The stated polynomial counts **distinct linear maps** \(\operatorname{ad}_X:Y\mapsto XY-YX\), rather than the number of elements \(X\) realizing them. In particular, the meaning of rank is the rank of a linear endomorphism of the \((n+m)\)-dimensional space \(A\), not the rank of a matrix describing a quiver representation.

## Proof
**Step 1: coordinates, the center, and the adjoint matrix.** The quotient has a basis consisting of vertex idempotents \(e_v\) and arrows \(a_e\); all products of two arrows vanish. Write
\[
 X=\sum_{v\in V}\lambda_ve_v+\sum_{e\in E}x_ea_e,
 \qquad Y=\sum_{v\in V}\mu_ve_v+\sum_{e\in E}y_ea_e.
\]
Choose the source and target \(s(e),t(e)\) of each arrow according to its actual orientation. Up to a simultaneously consistent sign convention, the arrow coefficient of the commutator is
\[
 [X,Y]_e=(\lambda_{s(e)}-\lambda_{t(e)})y_e
       +x_e(\mu_{t(e)}-\mu_{s(e)}).
\]
All diagonal coefficients of commutators vanish. An element \(X\) is central if and only if every \(x_e=0\) and the vertex scalars \(\lambda_v\) are constant on each connected component of \(G\). The first assertion follows by commuting with individual vertex idempotents, and the second by commuting with each arrow. Thus \(\dim_kZ(A)=c(G)\), and each distinct inner derivation has exactly \(q^{c(G)}\) representing elements. Therefore the generating polynomial of ranks over **elements** is \(q^{c(G)}D_Q(q,z)\).

**Step 2: exact rank for a fixed element.** Define the two disjoint sets
\[
 B(\lambda)=\{e\in E:\lambda_{s(e)}\ne\lambda_{t(e)}\},
 \qquad F(\lambda,x)=\{e\in E\setminus B(\lambda):x_e\ne0\}.
\]
On each row indexed by \(B(\lambda)\), the independent input coordinate \(y_e\) has a nonzero coefficient. Eliminating the corresponding row using that coordinate gives \(|B(\lambda)|\) pivot rows and leaves the rows with equal endpoint labels. On those remaining rows, only the vertex-input coordinates \(\mu_v\) occur, and every row outside \(F(\lambda,x)\) vanishes. Scaling each nonzero row indexed by \(F\) makes this remaining matrix an oriented incidence matrix of \((V,F)\). Its kernel consists exactly of vertex functions constant on each component of \((V,F)\), over every field including characteristic two. It consequently has rank \(r_G(F)\). Hence
\[
 \boxed{\operatorname{rank}\operatorname{ad}_X=|B(\lambda)|+r_G(F(\lambda,x)).}
\]
This equality is valid pointwise, not just generically. It supplies a direct verification algorithm and controls all cycle corrections.

**Step 3: the matroid expansion.** Fix \(\lambda:V\to\mathbb F_q\) and choose a support \(F\) on equal-label edges. Each distinct-label edge has \(q\) free choices for \(x_e\); every edge in \(F\) has \(q-1\) choices, and every remaining equal-label edge has \(x_e=0\). Summing the pointwise rank formula gives
\[
 q^{c(G)}D_Q(q,z)=\sum_{F\subseteq E}(q-1)^{|F|}z^{r_G(F)}
 \sum_{\lambda\text{ constant on }F}(qz)^{|B(\lambda)|}.
\]
For each edge not in \(F\), put \(t=qz\) and expand
\[
 t^{\mathbf1_{\lambda_s\ne\lambda_t}}
 =t+(1-t)\mathbf1_{\lambda_s=\lambda_t}.
\]
Select \(S\subseteq E\setminus F\) of edges on which the equality term is chosen. The conditions on \(F\cup S\) force \(\lambda\) to be constant on its connected components, leaving exactly \(q^{c(V,F\cup S)}\) choices. The identity
\[
 c(V,F\cup S)-c(G)=r_G(E)-r_G(F\cup S)
\]
then produces the displayed three-state matroid formula. As only \(r_G(F)\), \(r_G(F\cup S)\), sizes of edge subsets, and \(q\) occur, the invariance under matroid isomorphism follows. The original counting formula also proves integrality and nonnegativity, independently of cancellation in the expansion.

**Step 4: forests.** On any forest choose one root vertex in each connected component and record every oriented edge difference \(\lambda_s-\lambda_t\). These are independent and unrestricted field coordinates; together with root labels they give a bijective change of variables. Each edge has the independent two-dimensional datum \((\lambda_s-\lambda_t,x_e)\). It contributes rank one exactly when the datum is nonzero. No set of forest edges has a cycle, so its graphic rank equals its size. Each edge therefore contributes \(1+(q^2-1)z\) to the rank enumerator; the \(q^{c(G)}\) freely chosen root labels cancel the \(q^{c(G)}\) representatives per inner derivation. This proves the forest formula.

**Step 5: one cycle and its attachments.** Let \(\ell\) be the length of the unique cycle. Along its edges, signed vertex differences \(d_1,\ldots,d_\ell\) satisfy one nontrivial linear relation, with coefficients \(\pm1\): the oriented sum around the cycle vanishes. Every one of the other \(m-\ell\) differences is an independent free coordinate. Choose one root value (\(q\) choices). For the cycle, initially record each edge as *active* whenever \((d_e,x_e)\ne(0,0)\). The active-edge count agrees with the adjoint rank unless **all** differences along the cycle vanish and **all** its arrow coefficients are nonzero. In that unique type of exceptional assignment, the nonzero-support graph has exactly one cycle, so the true rank is \(\ell-1\) rather than \(\ell\).

Use orthogonality of the \(q\) additive characters of \(\mathbb F_q\) to impose the single linear relation among differences. The local character sum, including the arbitrary choice of \(x_e\), equals \(1+(q^2-1)z\) for the trivial character and \(1-z\) for every nontrivial character: in the latter case \(\sum_{d\ne0}\chi(d)=-1\). After multiplying by the \(q\) choices of root value, the cycle's active-edge polynomial over elements is
\[
 (1+(q^2-1)z)^\ell+(q-1)(1-z)^\ell.
\]
There are \(q(q-1)^\ell\) exceptional assignments, each requiring the correction \(z^{\ell-1}-z^\ell\). All attached-tree edge pairs contribute independent factors \(1+(q^2-1)z\). Finally divide by the center size \(q\). This proves the unicyclic formula, including its characteristic-independent and orientation-independent boundary cases.

**Step 6: commuting probability.** For each \(X\), the centralizer of \(X\) in \(A\) has \(q^{n+m-\operatorname{rank}\operatorname{ad}_X}\) elements. Dividing the sum over \(X\) by \(q^{2(n+m)}\), and replacing the sum over elements by \(q^{c(G)}\) times the sum over distinct inner derivations, yields the stated probability formula. The forest specialization follows by direct substitution.

## Verification
The accompanying `check.py` builds the actual adjoint matrices, computes their ranks over \(\mathbb F_2\), \(\mathbb F_3\), and the nonprime field \(\mathbb F_4\), and compares them pointwise against the rank formula. It then checks the independent three-state matroid subset sum and the forest and one-cycle closed forms. The exhaustive configurations include trees, disconnected forests, both triangle and square cycles, longer cycles, a cycle with a pendant edge, two cycles meeting at one vertex, and an orientation reversal. The deterministic command is `python check.py` and the expected success marker is `INCIDENCE_ADJOINT_MATROID_CYCLE_OK 17`. For example, the rank histogram of **distinct inner derivations** for a four-cycle over \(\mathbb F_2\) is \((1,4,30,53,40)\); for a triangle it is \((1,3,16,12)\). All counts include the zero derivation. These exhaustive small cases independently test arithmetic and signs but are not substitutes for the unrestricted proof above.

## Relationship to prior work
Baclawski's 1972 structural description of incidence-algebra derivations identifies inner derivations and their central kernel, and Zhang--Khrypchenko (first arXiv version July 30, 2016) treats proper Lie derivations of incidence algebras. Those works establish the context but do not compute the finite-field distribution of ranks of all individual inner derivations. Sánchez-Flores studies outer derivations and first Hochschild cohomology for monomial and radical-square-zero algebras, rather than the rank distribution of \(\operatorname{ad}_X\). The finite-field matroid expansion and the forest/unicyclic formulas concern a different invariant. The underlying incidence-matrix rank, character orthogonality, and graphic-matroid theory used as ingredients are classical, and novelty is not claimed for these ingredients individually.

## Limitations
The quiver is assumed finite, loopless, and without parallel or opposite arrow pairs sharing the same unordered endpoints. This exclusion matters: multiple arrows can couple adjoint-matrix rows on equal-label edges, invalidating the simple graphic-incidence rank formula. The algebra must have radical square zero. This theorem counts inner derivations, not all algebra derivations or outer derivations, and it gives no classification modulo algebra automorphisms. The general three-state formula can be exponentially expensive to evaluate for large graphs. Historical priority is not independently certified; an equivalent expression in literature on graphic arrangements, monomial algebras, or adjoint centralizers may exist.

## References
1. K. Baclawski, *Automorphisms and derivations of incidence algebras*, Proceedings of the American Mathematical Society 36 (1972), 351--356, DOI: 10.1090/S0002-9939-1972-0313133-8.
2. X. Zhang and M. Khrypchenko, *Lie Derivations of Incidence Algebras*, arXiv:1608.00110, first submitted July 30, 2016.
3. S. Sánchez-Flores, *On the Semisimplicity of the Outer Derivations of Monomial Algebras*, Communications in Algebra 39 (2011), 3410--3434, DOI: 10.1080/00927872.2010.510815.
