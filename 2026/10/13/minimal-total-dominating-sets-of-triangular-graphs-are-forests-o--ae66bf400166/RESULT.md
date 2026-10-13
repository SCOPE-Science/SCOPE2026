# Minimal total dominating sets of triangular graphs are forests of subdivided stars

## Finding
For every integer \(n\ge3\), the inclusion-minimal total dominating sets of the triangular graph \(T_n=L(K_n)\) are exactly the edge sets of the following two types of spanning subgraphs of \(K_n\):

1. A disjoint union of three-vertex paths, with no isolated vertex; this type is possible only when \(3\mid n\).
2. A forest with exactly one isolated vertex, whose other components are spiders with at least two arms, each arm having one or two edges. Equivalently, each such component arises from a star with at least two spokes by subdividing an arbitrary subset of spokes once.

Let \(M_n(z)=\sum_S z^{|S|}\), where the sum is over inclusion-minimal total dominating subsets \(S\) of \(V(T_n)\). Define
\[
B(u,z)=u\bigl(\exp(zu+z^2u^2)-1-zu-z^2u^2\bigr)-\tfrac12z^3u^4.
\]
Then the complete, coefficientwise-exact exponential generating function is
\[
\boxed{\sum_{n\ge3}M_n(z)\frac{u^n}{n!}
 =\exp\!\left(\tfrac12z^2u^3\right)-1-u+u\exp(B(u,z)).}
\]
Consequently the minimum total domination number and the upper total domination number are, respectively,
\[
\gamma_t(T_n)=\left\lfloor\frac{2n}{3}\right\rfloor,
\qquad
\Gamma_t(T_n)=\begin{cases}2,&n=3,\\n-2,&n\ge4.\end{cases}
\]
The exact number \(a_n\) of minimum-size total dominating sets is as follows, with \(m\ge1\), and terms with negative factorial indices omitted:
\[
\begin{aligned}
a_{3m}&=\frac{(3m)!}{2^m}\left(\frac1{m!}+\frac{25}{6(m-2)!}+\frac{16}{9(m-3)!}\right),\\
a_{3m+1}&=\frac{(3m+1)!}{2^m m!},\\
a_{3m+2}&=\frac{4(3m+2)!}{3\,2^m(m-1)!}.
\end{aligned}
\]
The first formula uses the convention that a summand with a negative factorial argument is zero. The enumeration is of **inclusion-minimal** sets, not of all total dominating sets.

## Assumptions and scope
All graphs are simple and finite. The graph \(T_n\) has a vertex for each unordered pair from \([n]\), with two vertices adjacent precisely when the corresponding pairs intersect. A total dominating set \(S\) means that every vertex of \(T_n\), including a vertex already in \(S\), has a **different**, adjacent vertex in \(S\). Inclusion-minimal means that no proper subset is total dominating. A spider here is a tree having a hub and at least two vertex-disjoint arms ending at distinct leaves, each of length one or two; a three-vertex path is included. The variable \(z\) counts selected edges, which are vertices in \(T_n\). Formal power series are over rational coefficients.

## Proof
**The basic edge criterion.** Given a candidate \(S\subseteq E(K_n)\), form the spanning graph \(F=([n],S)\). Every edge of \(K_n\) is incident with some *different* selected edge precisely when (i) \(F\) has at most one isolated vertex and (ii) \(F\) has no component consisting of a single edge. Indeed, a pair of isolated vertices gives an edge not incident with any selected edge. Conversely, if there is at most one isolated vertex, every edge whose endpoints are not both isolated is incident with some selected edge, unless it is itself the sole edge incident with each endpoint: exactly a two-vertex component. The criterion includes selected edges because a selected edge must meet another selected edge.

**Removing cycles.** If a selected component contains a cycle, deleting any one cycle edge leaves unchanged the set of nonisolated vertices, and it cannot create a two-vertex component: the endpoints remain in the same component by the rest of the cycle, a component with at least three vertices. Hence such a set is not inclusion-minimal. Thus every minimal set gives a forest.

**No isolated vertex.** Suppose a forest \(F\) has no isolated vertex. Every component has at least three vertices. If one has at least four, delete a pendant edge: precisely one isolated vertex appears, and the remaining component still has at least three vertices. The basic criterion still holds, contradicting minimality. Therefore all components have three vertices and are paths. Conversely, deleting any edge from such a forest creates a two-vertex component or two isolated vertices, so the forest is inclusion-minimal.

**Exactly one isolated vertex.** All other components are trees of order at least three. Deleting a pendant edge creates a second isolated vertex and therefore defeats domination. Deleting any non-pendant edge keeps the number of isolates at one, so it defeats domination exactly when one resulting component is a two-vertex tree. Consequently a component \(Q\) is allowed exactly when each of its non-pendant edges cuts off a two-vertex component on at least one side.

To classify such trees, consider the induced connected subtree \(C\) of vertices of degree at least two in \(Q\). It is nonempty because \(|V(Q)|\ge3\). If \(C\) contains a path on four vertices, its central edge separates \(Q\) into two trees each of at least three vertices (the two vertices on either side in \(C\) have exterior pendant extensions at its ends), contradicting the condition. Thus \(C\) has diameter at most two. If \(C\) is a single vertex, \(Q\) is a star. If \(C\) is a star with at least two core leaves, every core leaf has exactly one pendant neighbor: the edge joining it to the core center otherwise separates two subtrees each of size at least three. The core center may have any number of pendant neighbors. If \(C\) consists of one edge, at least one endpoint has exactly one pendant neighbor (otherwise deletion of that core edge would violate the condition); take the other endpoint as hub. Therefore \(Q\) is exactly a star with any subset of arms subdivided once. The converse follows because deleting a non-pendant edge along a length-two arm cuts off exactly one two-vertex subtree. Since at least two arms are needed to avoid a two-vertex component, this is precisely the asserted class.

**Counting.** A component spider with a *distinguished hub* consists of one labeled hub (weight \(u\)), \(p\) ordinary leaves (each weight \(zu\)), and \(q\) two-edge arms (each weight \(z^2u^2\)), where \(p,q\ge0\) and \(p+q\ge2\). Their labeled exponential generating function is \(u(e^{zu+z^2u^2}-1-zu-z^2u^2)\). The only spider counted twice by hub choice is the four-vertex path: there are \(4!/2\) labeled paths, each with three edges, so the correction to the coefficient is \(\tfrac12z^3u^4\). This yields \(B(u,z)\) exactly. Type (2) has one distinguished isolated labeled vertex and an unordered set of spider components, hence generating function \(u\exp B(u,z)\). Type (1) is an unordered set of three-vertex paths, with labeled weight \(3z^2u^3/3!=z^2u^3/2\), hence \(\exp(z^2u^3/2)\). Subtract the contributions of sizes zero and one. This proves the boxed identity and every coefficient.

**Extremal consequences.** Every type (2) component on \(v\) vertices contributes \(v-1\) selected edges and contains at least three vertices. If it has \(c\) components, \(|S|=(n-1)-c\) and \(1\le c\le\lfloor(n-1)/3\rfloor\). Type (1), when possible, has \(2n/3\) edges. Comparing these cases gives the displayed minima and maxima; a spanning star on the \(n-1\) nonisolated vertices realizes \(n-2\) for \(n\ge4\). For minimum-set multiplicities, the three smallest spider component weights are \(z^2u^3/2\), \(2z^3u^4/3\), and \(25z^4u^5/24\), from respectively three, sixteen and 125 labeled trees of sizes three, four, five. If \(n=3m+1\), every minimum set is one isolate plus \(m\) size-three components; if \(n=3m+2\), exactly one size-four component is needed alongside \(m-1\) size-three components. For \(n=3m\), either type (1) applies, or one isolate with \(m-1\) components and exactly two vertices of excess over size three: one size-five component or two size-four components. Exponential coefficient extraction gives the three stated formulas.

## Verification
A standalone `verify.py` script reconstructs the labeled-component polynomial with exact rational arithmetic, independently enumerates **every subset** of \(E(K_n)\) for \(3\le n\le7\), directly tests total domination in \(L(K_n)\) and inclusion minimality, and compares every coefficient. The full enumeration covers 2,131,016 candidate sets. It returned:

```
n=3: {2:3}
n=4: {2:12}
n=5: {3:80}
n=6: {4:840}
n=7: {4:630,5:3402}
VERIFY_OK n=3..7 all_subset_checks=2131016 minimal_set_coefficients_agree
```
These exhaustive *finite* checks are not an infinite proof. The preceding classification and exponential formula prove the result for every \(n\ge3\).

## Relationship to prior work
Favaron and Henning (2003) defined and bounded upper total domination in claw-free graphs. Henning and Yeo (2006) proved general total domination inequalities for claw-free graphs; triangular graphs belong to that class. Kanté, Limouzy, Mary, and Nourine (2014) established general enumeration-complexity equivalences for minimal total dominating sets and minimal hypergraph transversals. Kanté and collaborators (2014) gave an algorithm for enumerating minimal **edge dominating** sets, i.e. using closed edge neighborhoods, a distinct object. Chaluvaraju and Chaitra (2014) treated the total-domination polynomial that counts **all** total dominating sets, rather than solely inclusion-minimal ones. None of the materially inspected full-text statements gives the explicit class of selected-edge forests or the above polynomial for \(L(K_n)\). The comparison is one of mathematical implication, not merely terminology or matching titles.

## Limitations
The classification applies to line graphs of complete graphs only and to inclusion-minimal *total* domination. It does not enumerate all total dominating sets, arbitrary line graphs, or minimal ordinary dominating sets. Prior publications can contain equivalent results under alternate phrases such as total edge domination or minimal open-neighborhood hitting sets; the originality conclusion is necessarily conditional on accessible sources. The full paper of Favaron–Henning (2003), relevant to the upper parameter, and the full text of a general total-domination-polynomial paper were not available for complete inspection. Neither accessible abstract claims this exact polynomial, but those access gaps remain material risks. The mathematical proof is independent of the finite tests and of the prior bounds.

## References
- O. Favaron and M. A. Henning, *Upper total domination in claw-free graphs*, Journal of Graph Theory 44 (2003), 148–158, DOI: https://doi.org/10.1002/jgt.10134 (first publicly verified 2003-09-03).
- M. A. Henning and A. Yeo, *Total domination and matching numbers in claw-free graphs*, Electronic Journal of Combinatorics 13 (2006), R59, DOI: https://doi.org/10.37236/1085; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r59/pdf/.
- M. M. Kanté, V. Limouzy, A. Mary and L. Nourine, *On the Enumeration of Minimal Dominating Sets and Related Notions*, arXiv:1407.2053 (2014), https://arxiv.org/pdf/1407.2053.
- M. M. Kanté, V. Limouzy, A. Mary, L. Nourine and T. Uno, *Polynomial Delay Algorithm for Listing Minimal Edge Dominating Sets in Graphs*, arXiv:1404.3501 (2014), https://arxiv.org/pdf/1404.3501.
- B. Chaluvaraju and V. Chaitra, *Total Domination Polynomial of A Graph*, Journal of Informatics and Mathematical Sciences 6 (2014), DOI: https://doi.org/10.26713/jims.v6i2.256.
