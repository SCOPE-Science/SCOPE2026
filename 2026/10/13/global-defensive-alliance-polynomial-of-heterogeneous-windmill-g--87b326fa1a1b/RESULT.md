# Global defensive-alliance polynomial of heterogeneous windmill graphs

## Finding

Let \(r\ge2\) and \(m_1,\ldots,m_r\ge2\). For the clique bouquet
\[
W(m_1,\ldots,m_r)=K_1\vee(K_{m_1}\cup\cdots\cup K_{m_r}),
\]
write \(c\) for its unique universal center and \(B_i\) for its mutually disjoint peripheral cliques, with \(|B_i|=m_i\). Set \(T=\sum_{i=1}^r m_i\) and \(L=\lfloor T/2\rfloor\). For any selected vertex set \(S\), write \(s_i=|S\cap B_i|\) and \(t=\sum_i s_i\).

**All-set characterization.** A set \(S\) is a global defensive alliance precisely in one of the following disjoint cases:

1. \(c\in S\), \(t\ge L\), and, for every \(i\), either \(s_i=0\) or \(s_i\ge\lfloor m_i/2\rfloor\).
2. \(c\notin S\) and \(s_i\ge\lfloor m_i/2\rfloor+1\) for every \(i\).

Let
\[
A_m(x)=1+\sum_{j=\lfloor m/2\rfloor}^{m}\binom mjx^j,
\qquad B_m(x)=\sum_{j=\lfloor m/2\rfloor+1}^{m}\binom mjx^j,
\]
and use \([x^{\ge L}]P(x)=\sum_{j\ge L}[x^j]P(x)\,x^j\) for the degree-at-least-\(L\) truncation. The complete global defensive-alliance polynomial is
\[
\boxed{\mathcal G_W(x)=x[x^{\ge L}]\prod_{i=1}^rA_{m_i}(x)+\prod_{i=1}^rB_{m_i}(x).}
\]
In particular, the minimum cardinality is
\[
\boxed{\gamma_a(W)=1+\left\lfloor\frac12\sum_{i=1}^r m_i\right\rfloor.}
\]
All minimum alliances include \(c\) apart from a precisely determined exception: when \(r=2\) and both \(m_1,m_2\) are odd, there are also minimum alliances omitting \(c\), with \(s_i=(m_i+1)/2\) in each blade. Their complete count is
\[
\boxed{N_{\min}(W)=[x^L]\prod_{i=1}^r A_{m_i}(x)
+\mathbf 1_{\{r=2,\,m_1,m_2\text{ odd}\}}
\prod_{i=1}^{2}\binom{m_i}{(m_i+1)/2}.}
\]
For the friendship graph \(W(2,\ldots,2)\) of \(r\) triangles meeting in one vertex, this simplifies to
\[
\mathcal G_W(x)=x\sum_{j=r}^{2r}\binom{2r}{j}x^j+x^{2r},
\qquad \gamma_a(W)=r+1,\qquad N_{\min}(W)=\binom{2r}{r}.
\]
The center threshold couples all blades, so the first summand is a truncated product rather than a product of independent local counts.

## Assumptions and scope

Graphs are finite, undirected, and simple. There are at least two blades, and each blade has at least two vertices. A nonempty set \(S\subseteq V(G)\) is a *defensive alliance* when every \(v\in S\) satisfies
\[
|N[v]\cap S|\ge |N(v)\setminus S|.
\]
It is *global* when \(N[S]=V(G)\), equivalently when it is also a dominating set. Disconnected induced subgraphs \(G[S]\) are permitted. These are the standard definitions of Haynes, Hedetniemi, and Henning [1]. The polynomial counts actual vertex subsets of each size, not isomorphism classes and not only connected alliances. \(\gamma_a(G)\) denotes the least permitted cardinality.

## Proof

If \(c\in S\), its presence dominates the whole graph. For a selected peripheral vertex \(v\in S\cap B_i\), the number of allied vertices in its closed neighborhood is \(s_i+1\), and the number of unselected neighbors is \(m_i-s_i\). Thus its defensive condition is
\[
2s_i\ge m_i-1
\quad\Longleftrightarrow\quad
s_i\ge\left\lfloor\frac{m_i}{2}\right\rfloor.
\]
There is no condition in an empty blade, because the defensive inequality is imposed only on selected vertices. For the selected center itself, \(|N[c]\cap S|=t+1\) and \(|N(c)\setminus S|=T-t\), giving
\[
2t\ge T-1\quad\Longleftrightarrow\quad t\ge L.
\]
These are all vertices of \(S\), so they are necessary and sufficient in the center-included case.

If \(c\notin S\), a selected peripheral vertex in \(B_i\) has \(s_i\) selected closed-neighborhood vertices and \(m_i-s_i+1\) outside neighbors (the additional outside neighbor being \(c\)). Its condition is
\[
2s_i\ge m_i+1
\quad\Longleftrightarrow\quad
s_i\ge\left\lfloor\frac{m_i}{2}\right\rfloor+1.
\]
Because \(m_i\ge2\), these inequalities select at least one vertex in each blade. Every unselected peripheral vertex is then adjacent to a selected vertex in its own clique, and the center is adjacent to every selected vertex; hence domination follows. Thus the two cases prove the characterization.

For each blade, a center-included choice may either select nothing or choose \(j\ge\lfloor m_i/2\rfloor\) vertices, giving \(A_{m_i}(x)\). The center inequality deletes the terms with fewer than \(L\) peripheral vertices and then adds one to the total cardinality. The center-excluded choices have local polynomial \(B_{m_i}(x)\) independently. Since these two classes are disjoint, their polynomials add as displayed.

For the minimum, a center-included alliance has at least \(L+1\) vertices. This bound is attained: take \(\lfloor m_i/2\rfloor\) vertices from each blade and add \(\lfloor o/2\rfloor\) further peripheral vertices, where \(o=|\{i:m_i\text{ odd}\}|\). Indeed,
\[
L=\sum_i\left\lfloor\frac{m_i}{2}\right\rfloor
+\left\lfloor\frac{o}{2}\right\rfloor,
\]
and every blade has spare vertices after its local minimum. A center-excluded alliance has at least
\[
\sum_i\left(\left\lfloor\frac{m_i}{2}\right\rfloor+1\right)
=\sum_i\left\lfloor\frac{m_i}{2}\right\rfloor+r
\ge L+1.
\]
The last inequality uses \(r\ge2\) and \(o\le r\). Equality occurs exactly when \(r=2\) and \(o=2\): equivalently both blade sizes are odd. In that case the only center-excluded minimum sets choose exactly \((m_i+1)/2\) vertices per blade. Among center-included sets, minimum requires exactly \(L\) peripheral vertices, counted by the coefficient \([x^L]\prod_iA_{m_i}(x)\). The two contributions give the displayed complete minimum count. The friendship specialization follows by \(A_2(x)=(1+x)^2\), \(B_2(x)=x^2\), and \(L=r\).

## Verification

The included standard-library script `verify.py` independently constructs each graph, enumerates all vertex subsets, tests domination and the original closed-neighborhood defensive inequality, and separately tests the claimed center/blade criterion. It then compares every coefficient, the minimum size, and the exact number of minimizers with the polynomial formula. Running `python3 verify.py` reports:

`VERIFY_OK size_vectors=65 membership_checks=251104 valid_sets=78096 coefficient_checks=782 max_vertices=13`

The check covers every nondecreasing blade-size vector with at least two entries, every entry at least two, and total peripheral size between four and twelve inclusive. Exhaustion at these finite orders validates the implementation and boundary cases but is not a proof for arbitrary orders; the preceding argument supplies the infinite-family proof.

## Relationship to prior work

Haynes, Hedetniemi, and Henning [1] introduced the global defensive-alliance requirement and proved scalar results for stars, complete bipartite graphs, cycles, and trees, together with general bounds. A clique bouquet is not a complete bipartite graph or a tree when every blade has size at least two; the local blade inequalities plus the global center threshold are additional structure, and the current claim is the complete cardinality distribution rather than a bound.

Ibrahim [2] defines a bivariate defensive-alliance polynomial based specifically on *connected induced* subsets. Its friendship-graph proposition characterizes the family using a particular low-degree coefficient; it does not give the global defensive-alliance enumerator. In the two-odd-blade exceptional case described here, there are center-free minimum global alliances whose induced subgraphs are disconnected. Thus the connected-subset polynomial does not directly enumerate the objects considered here. Its friendship-graph section was compared at statement level, not excluded merely by title.

The global *offensive* alliance predicate and the *strong defensive* alliance predicate on a complete multipartite graph test different neighborhood conditions. The offensive condition is imposed on vertices outside the set, while the condition here is imposed on vertices inside it; complementary graph families do not preserve domination and defensive strength in the required form. No implication giving the two-case global defensive enumeration was found in those comparisons. This is a limited literature comparison, not a claim of exhaustive novelty.

## Limitations

No statement is asserted for blades of size one or for a single blade. The all-orders proof is elementary and self-contained, but the literature comparison cannot eliminate every poorly indexed prior treatment of friendship graphs or clique bouquets. The 2018 connected-alliance polynomial is a genuinely related framework, and an unpublished or inaccessible full formula might subsume part of the result. Independent validation has not been performed; the finite checker is supplementary and proves no new general theorem by itself.

## References

[1] T. W. Haynes, S. T. Hedetniemi, and M. A. Henning, “Global defensive alliances in graphs,” *Electronic Journal of Combinatorics* 10 (2003), R47, published 2003-12-08, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v10i1r47/pdf/ .

[2] H. Ibrahim, “Defensive alliance polynomial,” arXiv:1811.10089 (2018), https://arxiv.org/abs/1811.10089 .
