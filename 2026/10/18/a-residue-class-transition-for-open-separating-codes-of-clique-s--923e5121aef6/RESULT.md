# The one-isolate extension of open-separating codes on clique subdivisions

## Finding

Let \(n\ge3\), and let \(H_n=S(K_n)\) be the incidence graph of a labeled complete graph: the edge \(ij\) is replaced by a vertex \(e_{ij}\) adjacent to \(i,j\). An OD-code is a closed-neighborhood dominating set \(C\) for which the open signatures \(N(x)\cap C\) are distinct for all vertices \(x\). An OTD-code is an OD-code with no empty open signature. Its classification, size polynomial and minimum-forest counts on this graph are given in [1]. The result here describes the OD-codes that are not OTD and identifies when they strictly improve the minimum.

Write \(P_{\rm OD}(H_n;z)\) and \(P_{\rm OTD}(H_n;z)\) for the cardinality polynomials, with each code weighted by \(z^{|C|}\). Let
\[
W_s(z)=\sum_{F\subseteq E(K_s):\,([s],F)\text{ has no component of size }1\text{ or }2}z^{|F|}.
\]
In particular \(W_2(z)=0\). Then
\[
\boxed{P_{\rm OD}(H_n;z)-P_{\rm OTD}(H_n;z)=nz^{n-1}(z+n-1)W_{n-1}(z).}
\]
For \(n\ge4\), the same difference is \(nzP_{\rm OTD}(H_{n-1};z)\). This follows from a bijection: choose a label \(y\) and an OTD-code of the clique subdivision on the remaining original vertices, and add exactly the original vertex \(y\) to that code. In the resulting larger graph \(y\) is the unique vertex with empty open signature. At \(n=3\) there are no non-total OD-codes.

Consequently
\[
\boxed{\gamma_{\rm OD}(H_n)=2n-1-\left\lfloor n/3\right\rfloor-\mathbf 1_{3\nmid n}.}
\]
The difference \(\gamma_{\rm OTD}-\gamma_{\rm OD}\) is zero exactly when \(3\mid n\), and one otherwise. Write \(B_s\) for the number of forests on \([s]\) with \(\lfloor s/3\rfloor\) tree components, each of order at least three. Thus \(B_2=0\), and the labeled count can be written as
\[
B_s=s!\,[u^s t^{\lfloor s/3\rfloor}]\exp\left(t\sum_{r\ge3}\frac{r^{r-2}}{r!}u^r\right).
\]
The number of minimum OD-codes is
\[
\begin{cases}
nB_n+n(n-1)B_{n-1},&3\mid n,\\
n(n-1)B_{n-1},&3\nmid n.
\end{cases}
\]
The first summand, when present, is exactly the previously computed minimum OTD family; every other optimizer is the described extension of a minimum OTD-code on the remaining clique subdivision. All counts are for labeled subsets, not symmetry orbits.

## Proof

Let \(A=C\cap[n]\) and \(F=\{ij:e_{ij}\in C\}\). If \(A\) is empty, the subdivision-vertex signatures are all empty, violating open separation. If two originals \(i,j\) are omitted and \(k\in A\), the vertices \(e_{ik},e_{jk}\) both have signature \(\{k\}\). Hence \(|A|\ge n-1\). Conversely, with at most one original omitted, all subdivision signatures \(A\cap\{i,j\}\) are nonempty and pairwise distinct (distinct endpoint pairs or distinct selected singleton endpoints). In particular the subdivision vertices are dominated.

The original signature of \(i\) is the set of chosen subdivision vertices corresponding to edges incident to \(i\). Two distinct originals' signatures can coincide only if both are empty, or both equal the singleton \(\{e_{ij}\}\) for their common edge. Thus separation among originals requires at most one isolated vertex and no isolated edge in \(([n],F)\). Nonempty original signatures contain subdivision vertices, whereas subdivision signatures contain only originals and are nonempty, so there are no collisions across the two classes. Any nonisolated original is dominated by its signature. The possible isolated original \(y\) is dominated in the closed sense exactly when \(y\in A\). These are necessary and sufficient conditions, including total domination precisely when there is no isolate.

In the non-total case, deleting \(y\) and the subdivision vertices of its incident edges removes only \(y\) from \(C\). On the remaining originals, the selected edge graph has no components of size one or two, and at most one original is omitted from the code. Therefore the restriction is OTD. Conversely such a code on the smaller graph, with \(y\) added but no incident subdivision vertex added, satisfies the full signature conditions above; \(y\) is its unique empty-signature vertex. The lift multiplies the weighting by \(z\) and there are \(n\) choices of \(y\). Directly, the edge factor for any given \(y\) is \(W_{n-1}\), and the original factor is \(z^n+(n-1)z^{n-1}\), because only an original other than \(y\) can be omitted. For \(n=3\) the two remaining originals cannot support an edge graph without a component of size one or two, so the branch is absent. This proves the difference formula at all orders. For numerical evaluation the edge factor is the established restricted graph polynomial from [1], with the exact inclusion–exclusion formula
\[
W_s(z)=\sum_{i+2j\le s}\frac{(-1)^{i+j}s!}{i!\,2^j j!\,(s-i-2j)!}\,z^j(1+z)^{\binom{s-i-2j}{2}},
\]
where \(i,j\ge0\) prescribe disjoint singleton and isolated-edge components. The full OD polynomial is the stated difference plus the OTD polynomial of [1], namely \((z^n+nz^{n-1})W_n(z)\).

For \(s\ge3\), a graph counted by \(W_s\) has at most \(\lfloor s/3\rfloor\) components. With \(c\) components it has at least \(s-c\) edges, with equality exactly for a forest. Taking components of size three and assigning the remainder of zero, one or two vertices to one component realizes the least edge count \(d_s=s-\lfloor s/3\rfloor\), with exactly \(B_s\) minimizing edge sets by Cayley's labeled tree count and the exponential formula. The minimum OTD size is therefore \(n-1+d_n\), with \(nB_n\) optimizers, as in [1]. For \(n\ge4\) the non-total branch has minimum size \(n-1+d_{n-1}\), and exactly \(n(n-1)B_{n-1}\) codes of that size: choose \(y\), the omitted original from the other \(n-1\) labels, and one of the minimum forests. For \(n\ge4\), \(d_n-d_{n-1}=1-\mathbf1_{3\mid n}\), so both families attain the overall minimum exactly when \(3\mid n\). For \(n=3\) only the OTD family exists, with minimum size four and nine optima. The formulas include this case because \(B_2=0\).

## Verification and scope

The signature proof and forest count apply at every stated order. The accompanying `verify.py` checks the two code types against full graph adjacency for orders three through six, and checks the OD polynomial's minimum size and coefficient over orders three through eleven. `verification_output.txt` records the finite test output; these tests neither establish the all-order result nor its bibliographic priority.

The general OD/OTD terminology and the inequality \(\gamma_{\rm OTD}-1\le\gamma_{\rm OD}\le\gamma_{\rm OTD}\) are from [2]. The census of OTD-codes on this same family, including the minimum forest count and exact polynomial \(W_s\), is covered by [1]; no new priority for that part is asserted, and calendar date alone does not resolve the ordering of the two findings. The one-isolate extension and the exact comparison of the two optima are the distinct claims. They are specific to the full one-subdivision of a clique, not to arbitrary central graphs, subdivisions or identification codes.

## References

1. *All identifying open codes of subdivided complete graphs*, Resultary, 2026-10-18, [Result](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-all-identifying-open-codes-of-subdivided-complete-graphs--078f1db52295/RESULT.md).
2. D. Chakraborty and A. K. Wagler, *On open-separating dominating codes in graphs*, [arXiv:2402.03015](https://arxiv.org/abs/2402.03015), Theorem 3(b).
