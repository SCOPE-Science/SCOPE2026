# Weight enumerator for quasi-total double Roman functions on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be connected, with \(r\ge2\) and \(N=\sum_i n_i\). A quasi-total double Roman dominating function is a map \(f:V(G)\to\{0,1,2,3\}\) such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), every vertex labeled \(1\) has a neighbor labeled at least \(2\), and every isolated vertex in the positive support is labeled \(2\).

Write \(D_3\) for the set of parts containing a label \(3\). If \(D_3=\varnothing\), write \(D_2\) for the set of parts containing a label \(2\). Then every valid function belongs to exactly one of the following cases.

1. If \(|D_3|\ge2\), every assignment of the remaining labels is valid.
2. If \(D_3=\{i\}\), let \(a\) be the number of label-\(2\) vertices outside \(X_i\).
   - If \(a=0\), then \(X_i\) uses only labels \(2,3\), contains at least one \(3\), and the outside uses labels \(0,1\) with at least one \(1\).
   - If \(a=1\), then \(X_i\) uses only labels \(1,2,3\), contains at least one \(3\), and the outside has exactly one label \(2\).
   - If \(a\ge2\), then \(X_i\) may use all four labels, contains at least one \(3\), and the outside has at least two labels \(2\).
3. Suppose \(D_3=\varnothing\).
   - If \(|D_2|\ge3\), every \(0,1,2\)-assignment with that label-\(2\) support is valid.
   - If \(D_2=\{i,j\}\), then zeros are allowed in \(X_i\) exactly when \(X_j\) contains at least two labels \(2\), and symmetrically.
   - If \(D_2=\{i\}\), every vertex of \(X_i\) is labeled \(2\). For \(n_i\ge2\), every outside vertex may independently receive \(0\) or \(1\). For \(n_i=1\), every outside vertex must receive \(1\).
   - No valid function has \(D_2=\varnothing\).

This classification gives a closed weight enumerator. Define, for \(m\ge0\),
\[
C_m=(1+z)^m,\qquad A_m=(1+z+z^2)^m,\qquad B_m=(1+z+z^2+z^3)^m.
\]
For \(m\ge1\), define
\[
X_m=mz^2C_{m-1},\qquad Y_m=mz^{m+1},
\]
and set \(X_0=Y_0=0\). Also put
\[
H_m=A_m-C_m-X_m,
\qquad
R_m=(z+z^2)^m-z^m-Y_m.
\]
The contribution from functions having labels \(3\) in at least two parts is
\[
P_3=
B_N-A_N-
\sum_i(B_{n_i}-A_{n_i})A_{N-n_i}.
\]
For a unique label-\(3\) part \(X_i\), with \(M_i=N-n_i\), put
\[
J_i=
\big((z^2+z^3)^{n_i}-z^{2n_i}\big)(C_{M_i}-1)
+
\big((z+z^2+z^3)^{n_i}-(z+z^2)^{n_i}\big)X_{M_i}
+
(B_{n_i}-A_{n_i})H_{M_i}.
\]
The contribution from functions with no label \(3\) and labels \(2\) in at least three parts is
\[
P_2=
A_N-C_N
-
\sum_i(A_{n_i}-C_{n_i})C_{N-n_i}
-
\sum_{i<j}
(A_{n_i}-C_{n_i})
(A_{n_j}-C_{n_j})
C_{N-n_i-n_j}.
\]
For exactly two label-\(2\) parts, define
\[
L_{ij}=
C_{N-n_i-n_j}
\big(
Y_{n_i}Y_{n_j}
+
X_{n_i}R_{n_j}
+
R_{n_i}X_{n_j}
+
H_{n_i}H_{n_j}
\big).
\]
For exactly one label-\(2\) part, put
\[
U_i=
\begin{cases}
z^{2n_i}C_{N-n_i},&n_i\ge2,\\
z^{N+1},&n_i=1.
\end{cases}
\]
Therefore the exact weight enumerator is
\[
\mathcal Q_G(z)
=
P_3
+
\sum_i J_i
+
P_2
+
\sum_{i<j}L_{ij}
+
\sum_iU_i.
\]

As a minimum-weight corollary,
\[
\gamma_{qtdR}(G)=
\begin{cases}
3,&G=K_2,\\
4,&N\ge3\text{ and }\min_i n_i\le2,\\
6,&\min_i n_i\ge3.
\end{cases}
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. The graph is connected, so there are at least two nonempty partite classes. The weight enumerator is
\[
\mathcal Q_G(z)=\sum_f z^{\sum_{v\in V(G)}f(v)},
\]
where the sum ranges over all quasi-total double Roman dominating functions.

The minimum-weight corollary is included because it drops immediately out of the all-function classification. The originality claim is the complete multipartite classification and weight enumerator, not merely the minimum value.

## Proof
For a part \(X_i\), let \(c_i,u_i,v_i,w_i\) be the counts of labels \(0,1,2,3\), respectively. Let \(V_2=\sum_i v_i\) and \(V_3=\sum_i w_i\). Since vertices in one part are pairwise nonadjacent and every vertex is adjacent to every vertex in every other part, the defining conditions become
\[
c_i>0
\Longrightarrow
V_3-w_i\ge1
\text{ or }
V_2-v_i\ge2,
\]
and
\[
u_i>0
\Longrightarrow
(V_2-v_i)+(V_3-w_i)\ge1.
\]
The quasi-total condition has an equally simple form: if positive labels occur in at least two parts, every positive vertex has a positive neighbor; if positive labels occur in exactly one part, every positive vertex is isolated, so every such vertex must be labeled \(2\).

If labels \(3\) occur in at least two parts, every part sees a label \(3\) outside itself. Both double-Roman inequalities are automatic, and the positive support already meets two parts. This proves Case 1.

Suppose labels \(3\) occur only in \(X_i\). Every vertex outside \(X_i\) automatically satisfies its double-Roman requirement because it sees a label \(3\). Inside \(X_i\), a label \(1\) needs at least one label \(2\) outside, while a label \(0\) needs at least two. If there are no outside labels \(2\), labels \(0,1\) are therefore forbidden inside \(X_i\), and at least one outside label \(1\) is required to stop the labels \(3\) from being isolated in the positive support. With exactly one outside label \(2\), zeros are forbidden inside but ones are allowed. With at least two outside labels \(2\), no further restriction remains. This proves Case 2.

Now suppose there is no label \(3\). If labels \(2\) occur in at least three parts, each part sees at least two of them outside, so every zero and one is defended. If labels \(2\) occur in exactly two parts \(X_i,X_j\), then a zero in \(X_i\) is legal exactly when \(X_j\) contains at least two labels \(2\), and symmetrically; labels \(1\) are automatically defended because each part sees at least one outside label \(2\). If labels \(2\) occur only in \(X_i\), then labels \(0,1\) are impossible inside \(X_i\), so that part is entirely labeled \(2\). Outside zeros require \(n_i\ge2\); if \(n_i=1\), every outside vertex must instead be labeled \(1\). With no labels \(2\) or \(3\), neither zeros nor ones can satisfy the double-Roman requirements. This proves Case 3.

The polynomial follows by translating the disjoint cases into generating functions. The terms \(P_3\) and \(P_2\) are obtained by inclusion-exclusion on the number of parts supporting labels \(3\) or \(2\). The polynomials \(X_m\) and \(Y_m\) count assignments with exactly one label \(2\), respectively allowing or forbidding zeros among the remaining vertices; \(H_m\) and \(R_m\) count assignments with at least two labels \(2\), again respectively allowing or forbidding zeros. The terms \(J_i,L_{ij},U_i\) are exactly the three remaining support cases above, so the sum is disjoint and exhaustive.

For the minimum corollary, \(K_2\) admits labels \(1,2\), giving weight \(3\). If \(N\ge3\) and a singleton part exists, place label \(3\) on that vertex and label \(1\) on one vertex outside it; if a part of size two exists, label both of its vertices \(2\). Thus weight \(4\) is attainable whenever the smallest part has size at most two. No quasi-total double Roman function on a graph of order at least three has weight below four. If every part has size at least three, the classification rules out weights below six, while placing one label \(3\) in each of two distinct parts attains weight six.

## Verification
The included checker builds every connected complete multipartite isomorphism type of orders two through eight. It enumerates every map to \(\{0,1,2,3\}\), tests the two double-Roman conditions directly from graph adjacency, tests isolation in the induced positive support directly, and records the full weight distribution.

Independently, it evaluates the displayed generating-function formula by integer polynomial arithmetic. Every coefficient agrees. It also compares the minimum nonzero coefficient index with the stated minimum-weight corollary.

## Relationship to prior work
The 2024 paper introducing quasi-total double Roman domination defines exactly the same function class, proves NP-hardness, determines paths and cycles, characterizes several small and large parameter values, and proves a general upper bound. Its full accessible text contains no arbitrary complete-multipartite theorem, and targeted searches did not locate a complete-bipartite or complete-multipartite weight enumerator.

Total double Roman domination is an earlier, strictly stronger support condition: every positive vertex must have a positive neighbor. The 2019/2020 total-double-Roman literature develops minimum-parameter bounds and selected graph families, but its full text contains no arbitrary complete-multipartite theorem. Those results therefore do not imply the quasi-total all-function classification, which additionally permits isolated label-\(2\) vertices.

A 2026 follow-up on quasi-total double Roman stability confirms that the 2024 paper initiated this parameter and studies deletion stability rather than all-function enumeration. Exact full-text searches in that follow-up likewise did not locate complete multipartite or complete bipartite classifications.

The minimum-value corollary may overlap with the foundational paper's general small-value characterizations; it is not used as the originality basis. The new statement assessed here is the complete classification of all functions and the resulting exact weight enumerator.

## Limitations
The theorem is restricted to connected complete multipartite graphs and to the quasi-total double Roman definition above. It does not enumerate total double Roman, signed double Roman, or other related function classes. Exhaustive verification through order eight is finite corroboration only; the arbitrary-order theorem follows from the proof. Search coverage cannot exclude a differently phrased or non-indexed complete-multipartite enumerator.

## References
1. S. Kosari, S. Babaei, J. Amjadi, M. Chellali, S. M. Sheikholeslami, “Quasi total double Roman domination in graphs,” AKCE International Journal of Graphs and Combinatorics 21 (2024), 171–180, DOI 10.1080/09728600.2024.2315275, published online 26 February 2024.
2. G. Hao, L. Volkmann, D. A. Mojdeh, “Total double Roman domination in graphs,” Communications in Combinatorics and Optimization 5 (2020), 27–39, DOI 10.22049/CCO.2019.26484.1118, published online 16 July 2019.
3. S. Kosari, H. Jiang, M. Esmaeili, “Quasi total double Roman domination stability in graphs,” AKCE International Journal of Graphs and Combinatorics, published online 9 January 2026.
