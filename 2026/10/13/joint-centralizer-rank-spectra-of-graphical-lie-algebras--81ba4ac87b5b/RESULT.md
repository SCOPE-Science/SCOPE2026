# Joint centralizer rank spectra of graphical Lie algebras

## Finding

Let \(G=(V,E)\) be a finite simple graph with \(n=|V|\ge1\) and \(m=|E|\). Over any finite field \(\mathbb F_q\), form the graphical class-two Lie algebra \(L_G\) with vertex basis \((v_i)_{i\in V}\), central edge basis \((z_{ij})_{\{i,j\}\in E}\), and brackets \([v_i,v_j]=z_{ij}\) for oriented edges \(i<j\) (with the opposite bracket given by antisymmetry); all other basis brackets are zero. These definitions also give an alternating Lie bracket in characteristic two.

For integers \(t\ge1\), write \(\mathcal J_{G,q,t}(T)\) for the polynomial that counts ordered \(t\)-tuples \((a_1,\ldots,a_t)\in L_G^t\) by the codimension of their **common centralizer**:

\[
\mathcal J_{G,q,t}(T)=\sum_{(a_1,\ldots,a_t)\in L_G^t}
T^{\dim L_G-\dim\bigcap_{j=1}^{t} C_{L_G}(a_j)}.
\]

Let \(P=(q^t-1)/(q-1)\). For each vertex subset \(S\subseteq V\), let \(N[S]\) be its closed neighborhood, \(c(S)\) the number of components of the induced graph \(G[S]\) (with \(c(\varnothing)=0\)), and \(\operatorname{Comp}(G[S])\) its set of vertex components. Then the **complete simultaneous-centralizer rank polynomial** is

\[
\boxed{\displaystyle
\mathcal J_{G,q,t}(T)=q^{tm}\sum_{S\subseteq V}(q-1)^{|S|}
T^{|N[S]|-c(S)}
\prod_{C\in\operatorname{Comp}(G[S])}
\left(P+(P^{|C|}-P)T\right).}
\]

Every coefficient counts actual tuples. Equivalently, for the graphical group defined using the same integral commutator rules, division of the coefficient of \(T^r\) by \(q^r\) gives the number of orbits of size \(q^r\) under **simultaneous conjugation on ordered \(t\)-tuples**. Thus the formula also specifies the full orbit-size distribution, not merely the total orbit count.

Let \(i(G)\) be the number of isolated vertices and \(c(G)\) the number of connected components, including isolated vertices. The largest occurring exponent is exactly \(n-c(G)\) for \(t=1\), and exactly \(n-i(G)\) for every \(t\ge2\). Therefore whenever \(G\) has at least one edge, a single element cannot have centralizer equal to \(Z(L_G)\), but **two elements can**, over every finite field, including \(\mathbb F_2\). For graphs without isolated vertices and \(t\ge2\), the number of tuples with common centralizer exactly \(Z(L_G)\) equals

\[
q^{tm}\sum_{\substack{S\subseteq V\\N[S]=V}}(q-1)^{|S|}
\prod_{C\in\operatorname{Comp}(G[S])}(P^{|C|}-P).
\]

The earlier single-element polynomial is recovered at \(t=1\), when \(P=1\), and is **not** claimed as new.

## Assumptions and scope

The graph is finite, simple, and may be disconnected or contain isolated vertices; \(n\ge1\), \(t\ge1\), and \(q\) is any prime power. No odd-characteristic assumption or connectedness assumption is made. By convention the product over an empty set of components is one. The common centralizer is computed inside the whole Lie algebra, including the central edge space. Each ordered tuple is counted individually, not modulo automorphisms. The graphical-group orbit statement uses its standard class-two commutator description and is not an assertion about conjugacy classes in arbitrary groups.

## Proof

**1. Common-centralizer equations.** Write \(a_j=\sum_{v\in V}a_{jv}v+z_j\), with \(z_j\) in the central edge space, and for each vertex put \(u_v=(a_{1v},\ldots,a_{tv})\in\mathbb F_q^t\). If \(b=\sum_v b_vv+z\), then \(b\in\bigcap_j C_{L_G}(a_j)\) exactly when, for every edge \(\{v,w\}\in E\),

\[
 u_v b_w-u_w b_v=0\quad\text{in }\mathbb F_q^t.
\]

The edge-basis coordinates are independent, and all central entries in \(b\) are unconstrained.

**2. Kernel on a fixed support.** Let \(S=\{v:u_v\ne0\}\). If \(w\notin S\) has a neighbor in \(S\), the corresponding edge equation forces \(b_w=0\). Each vertex outside \(N[S]\) is free. Within a connected component \(C\) of \(G[S]\), all \(u_v\) are nonzero. If they span a single projective line, the edge equations determine all \(b_v\) from one freely chosen scalar, giving one kernel dimension. If not, some edge of the connected graph \(G[C]\) joins nonproportional \(u_v,u_w\), forcing \(b_v=b_w=0\). Since every \(u_x\) in \(C\) is nonzero, the zero values propagate along edges throughout \(C\). Such a component contributes zero kernel dimensions.

Writing \(h\) for the number of connected components of \(G[S]\) whose nonzero vectors \(u_v\) are all proportional, we therefore have

\[
\dim\bigcap_{j=1}^{t}C_{L_G}(a_j)
=m+|V\setminus N[S]|+h,
\qquad
r=|N[S]|-h.
\]

This is a complete classification of the rank for each tuple of vertex coefficient vectors, not an average-case statement.

**3. Exact count.** The number of projective lines in \(\mathbb F_q^t\) is \(P\), and each nonzero vector has a unique projective line with \(q-1\) representatives. For a component \(C\) containing \(k\) vertices, there are exactly \(P\) constant projective assignments (kernel contribution one) and \(P^k-P\) nonconstant assignments (kernel contribution zero). Such choices are independent between induced components. The nonzero scalar representatives contribute \((q-1)^{|S|}\). Starting at rank \(|N[S]|-c(S)\), changing a component from constant to nonconstant raises the rank by one. Hence that component contributes \(P+(P^k-P)T\). Finally the central parts of \(a_1,\ldots,a_t\) contribute the factor \(q^{tm}\). Summing disjointly over supports proves the displayed polynomial.

**4. Boundaries, normalization, and maximal rank.** At \(T=1\), the component products become \(P^{|S|}\), so the result sums to

\[
q^{tm}\sum_{S\subseteq V}(q-1)^{|S|}P^{|S|}
=q^{tm}(1+(q-1)P)^n=q^{t(n+m)},
\]

as required. For \(t=1\), every nonzero vector lies on the unique projective line and the rank is at most \(n-c(G)\); equality holds when \(S=V\). For any \(t\), isolated vertices lie in the center, hence rank is at most \(n-i(G)\). If \(t\ge2\), choose nonzero \(u_v\) at every nonisolated vertex, with at least two distinct projective lines in each nontrivial connected component; such a choice exists over every field since \(P\ge3\). Every induced nontrivial component is then nonconstant, while isolated vertices are left zero. The common centralizer is precisely the center, proving attainment of \(n-i(G)\). If \(G\) has an edge, a lone noncentral element belongs to its own centralizer and therefore cannot have centralizer equal to the center.

For a graph without isolated vertices, the coefficient of rank \(n\) requires \(N[S]=V\) and every induced component to be projectively nonconstant, giving the second formula. The corresponding graphical-group orbit statement follows from the equality of group and Lie commutator equations for graphical groups and orbit-stabilizer: a common-centralizer codimension \(r\) yields orbit size \(q^r\).

## Verification

The accompanying Python checker constructs the actual simultaneous-adjoint matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), and computes their ranks by independent finite-field row elimination. It tests the closed polynomial on ten small graphs and all \(64\) labeled four-vertex graphs in the binary two-tuple case. It compares \(132\) cases, covering \(400389\) enumerated vertex-coefficient tuples, and checks normalization and maximal-rank boundaries. The output is `VERIFY_OK_JOINT_GRAPH` on successful replay. Finite checks corroborate, but do not replace, the proof for arbitrary graphs, field orders, or tuple lengths.

For two binary tuples on the four-vertex path, the coefficients (including all central coordinates) are
\[
64+384T+3648T^2+3840T^3+8448T^4,
\]
while for the four-vertex star they are
\[
64+4032T+1536T^3+10752T^4.
\]
Both graphs have four vertices and three edges, but the distributions differ. All displayed coefficients sum to \(2^{14}\), the total number of ordered pairs in a seven-dimensional binary Lie algebra.

## Relationship to prior work

The graphical Lie-algebra construction and its graph-faithfulness are due to earlier work of Dani--Mainkar and Mainkar. DeCoste--DeMeyer--Mainkar analyze the distinct metric operator \(j(Z)\), indexed by central vectors, including its singularity. Rossmann's published graph polynomial \(\mathcal C_G(X,Y)=\sum_{S\subseteq V}(X-1)^{|S|}Y^{|N[S]|-c(S)}\) gives the complete **one-element** centralizer and conjugacy-class-size distribution. The present formula explicitly specializes to that known result when \(t=1\). Its new content is the full joint common-centralizer distribution for arbitrary \(t\ge2\), involving projective coefficient configurations and component sizes, together with simultaneous-orbit-size multiplicities and the exact two-element center-cutting threshold. No broader prior statement establishing these tuple distributions was located in the inspected sources.

## Limitations

No classification up to graph isomorphism is claimed from this polynomial. The support-sum formula can require exponential work in \(n\); no polynomial-time evaluation algorithm is claimed. The literature search is not a proof of historical uniqueness, and a differently phrased simultaneous-centralizer formula may exist in uninspected work. The result is mathematically proved here but has not undergone independent mathematical audit.

## References

1. M. G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, Groups Geom. Dyn. **9** (2015), 55--65; first correct arXiv preprint: arXiv:1310.3414v1, 2013-10-12. https://arxiv.org/abs/1310.3414
2. R. DeCoste, L. DeMeyer, M. Mainkar, *Graphs and Metric 2-step Nilpotent Lie Algebras*, arXiv:1512.07944v1 (2015-12-25). https://arxiv.org/abs/1512.07944
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bull. Lond. Math. Soc. **54** (2022), 1923--1943; arXiv:2107.05564v1. https://doi.org/10.1112/blms.12665
