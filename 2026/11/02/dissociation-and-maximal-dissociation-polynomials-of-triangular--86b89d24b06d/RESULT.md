# Dissociation and maximal-dissociation polynomials of triangular graphs

## Finding

For every integer \(n\ge 2\), write \(T_n=L(K_n)=J(n,2)\), whose vertices are the edges of the labeled complete graph \(K_n\). Two vertices of \(T_n\) are adjacent if their root edges share an endpoint. A *dissociation set* is a vertex subset inducing maximum degree at most one; *maximal* always means inclusion-maximal, not necessarily largest.

Let \(D_n(z)\) enumerate **all** dissociation sets by cardinality (including the empty set), and let \(M_n(z)\) enumerate inclusion-maximal dissociation sets. Their exact formulas are

\[
D_n(z)=\sum_{\substack{u,a,b\ge0\\u+2a+3b=n}}
\frac{n!}{u!\,2^{a+b}a!b!}\,z^{a+2b},
\]

\[
M_n(z)=\sum_{\substack{a,b\ge0\\2a+3b=n}}
\frac{n!}{2^{a+b}a!b!}\,z^{a+2b}
+\mathbf1_{\{n\equiv1\pmod3\}}
\frac{n!}{2^{(n-1)/3}((n-1)/3)!}\,z^{2(n-1)/3}.
\]

In the second formula the final term is present only when \(n\equiv1\pmod3\). These formulas have the exponential generating functions

\[
\sum_{n\ge0} D_n(z)\frac{x^n}{n!}
 =\exp\left(x+\frac{zx^2}{2}+\frac{z^2x^3}{2}\right),
\qquad
\sum_{n\ge0} M_n(z)\frac{x^n}{n!}
 =\exp\left(\frac{zx^2}{2}+\frac{z^2x^3}{2}\right)
 +x\exp\left(\frac{z^2x^3}{2}\right).
\]

For these generating functions only, \(T_0\) and \(T_1\) are interpreted as empty graphs on zero vertices; each has one empty dissociation set, which is maximal.

Every coefficient of \(M_n(z)\) between exponents \(\lceil n/2\rceil\) and \(\lfloor2n/3\rfloor\) is positive and all other coefficients vanish. Thus

\[
\operatorname{supp}M_n=\{\lceil n/2\rceil,\lceil n/2\rceil+1,\ldots,\lfloor2n/3\rfloor\}.
\]

The consecutive positive coefficients of \(M_n(z)\) are **strictly log-concave** whenever there are at least three of them. All maximal dissociation sets have the same size precisely for \(n\in\{2,3,4,5,7\}\). In particular \(T_7\), unlike \(T_6\) and \(T_8\), has this property.

Examples are \(M_6(z)=15z^3+90z^4\), \(M_7(z)=945z^4\), and \(M_8(z)=105z^4+2520z^5\).

## Assumptions and scope

The base graph is the simple complete graph on the labeled vertex set \([n]\). An individual edge of this base graph represents one vertex of \(T_n\); there is no quotient by graph automorphisms. Vertex subsets of \(T_n\) are counted once each. The variable \(z\) records the number of selected base edges, equivalently the cardinality of the selected vertex subset of \(T_n\). The parameter \(n\) is an arbitrary integer at least two. No weighted, directed, or multigraph extension is asserted.

## Proof

**1. Incidence characterization.** Let \(S\subseteq V(T_n)\) and let \(H\) be the graph on \([n]\) with edge set corresponding to \(S\). For a selected edge \(uv\) of \(H\), its degree in \(T_n[S]\) is exactly

\[
\deg_H(u)+\deg_H(v)-2.
\]

Consequently, \(S\) is a dissociation set if and only if each edge \(uv\) of \(H\) satisfies \(\deg_H(u)+\deg_H(v)\le3\). No nonisolated vertex of \(H\) can have degree at least three. Moreover, an edge cannot join two degree-two vertices. It follows that every nontrivial component of \(H\) is either one edge \(K_2\) or a path \(P_3\) with two edges. Conversely every disjoint union of such components, together with isolated base vertices, satisfies the condition.

**2. Exact maximality criterion.** Call a base vertex *unused* if it is isolated in \(H\). If there are at least two unused vertices, adding their joining edge creates a new \(K_2\), so \(S\) is not maximal. If there is exactly one unused vertex and \(H\) contains a \(K_2\) component, joining the unused vertex to an endpoint of that \(K_2\) changes it to a \(P_3\), so \(S\) again is not maximal.

Conversely, suppose there are no unused vertices. Any omitted edge with endpoints in two distinct nontrivial components meets two selected edges, so its newly added vertex in \(T_n\) has at least two selected neighbors. An omitted edge inside one \(P_3\) joins its two leaves and also meets both selected edges; every edge of a \(K_2\) is already selected. Hence no edge can be added. Finally, suppose there is exactly one unused vertex and every nontrivial component is a \(P_3\). Any edge joining that unused vertex to a \(P_3\) leaf gives an existing selected edge two neighbors in \(T_n\); joining it to the \(P_3\) center meets both selected edges. No extension exists. Thus **the maximal configurations are exactly (A) complete partitions of \([n]\) into \(K_2\) and \(P_3\) components, and (B) one unused vertex with all remaining vertices partitioned into \(P_3\) components**. These alternatives are disjoint, and each selected edge set uniquely determines its components.

**3. Counting and generating functions.** A \(K_2\) component uses two labeled base vertices and contributes one selected edge; a \(P_3\) component uses three base vertices with three choices of its center and contributes two selected edges. An unused singleton contributes no selected edge. The exponential formula therefore gives

\[
\exp(x)\exp(zx^2/2)\exp(3z^2x^3/6)
=\exp(x+zx^2/2+z^2x^3/2)
\]

for all dissociation sets. The two maximal classes above give respectively \(\exp(zx^2/2+z^2x^3/2)\) and \(x\exp(z^2x^3/2)\). Extracting \(n!\) times the coefficient of \(x^n\) yields the stated sums and generating functions. In particular the factors \(2^{a+b}\) arise from \(2!^a(3!/3)^b\), so no orientation or overcount is hidden.

**4. Cardinality support and the exceptional uniform cases.** For a full partition, \(2a+3b=n\) and the number of selected edges is \(k=a+2b=(n+b)/2\). Admissible \(b\) range over all nonnegative integers congruent to \(n\) modulo two and at most \(n/3\). Increasing \(b\) by two increases \(k\) by one, giving every integer from \(\lceil n/2\rceil\) through \(\lfloor2n/3\rfloor\). The class with one unused vertex exists exactly when \(n=3q+1\) and has \(k=2q=\lfloor2n/3\rfloor\), so it adds multiplicity but no new cardinality. The support is a singleton exactly when \(\lceil n/2\rceil=\lfloor2n/3\rfloor\), which for integers \(n\ge2\) occurs precisely at \(n=2,3,4,5,7\).

**5. Strict log-concavity.** Write \(B_k\) for the full-partition contribution to \([z^k]M_n(z)\). In the support interval let \(a=2n-3k\) and \(b=2k-n\). Then

\[
B_k=\frac{n!\,2^{k-n}}{a!b!},\qquad
\frac{B_{k+1}}{B_k}=\frac{2a(a-1)(a-2)}{(b+1)(b+2)}
\]

whenever \(k\) and \(k+1\) lie in the support. These successive ratios strictly decrease because \(a\) decreases by three and \(b\) increases by two. The only alteration is at the largest exponent when \(n=3q+1\), where its coefficient is \(B_{2q}(1+4/q)\). For \(q\le4\) the polynomial has at most two positive coefficients. For \(q\ge5\), the last two adjacent ratios (the penultimate one after the correction, and the one immediately preceding it) are respectively

\[
R_{\mathrm{last}}=\frac{120}{(q-2)(q-1)}\left(1+\frac4q\right),
\qquad R_{\mathrm{prev}}=\frac{672}{(q-4)(q-3)}.
\]

Their quotient is less than \((5/28)(9/5)=9/28<1\). Hence the corrected last ratio is also strictly smaller than the preceding ratio, proving strict log-concavity throughout whenever an interior coefficient exists.

## Verification

The accompanying standalone `verify.py` constructs the adjacency graph of \(T_n\) directly and tests the definition of dissociation and one-vertex maximality; it does not use the structural characterization to decide those properties. Complete subset enumeration is used for \(2\le n\le6\). For \(7\le n\le9\), the search enumerates all subsets of size at most \(\lfloor2n/3\rfloor\), an exhaustive range for feasible sets by the proved upper bound, rather than enumerating all larger infeasible subsets. Both polynomials agree for every tested order. The program examines 2,555,347 candidate vertex subsets in total and checks strict log-concavity arithmetically for \(2\le n\le200\). These computations are finite corroboration, not a substitute for the unrestricted proof.

Run `python verify.py` from the directory containing the provided script. The expected final line begins `VERIFY_OK` and includes `candidate_subsets=2555347`.

## Relationship to prior work

Orlovich, Dolgui, Finke, Gordon, and Werner (2011) study dissociation problems on line graphs and show the maximum dissociation size for line graphs of graphs with a Hamiltonian path; the known scalar maximum \(\lfloor2n/3\rfloor\) for \(T_n\) is **not** claimed as new here. Their complexity and extremal results do not supply the all-set or maximal-set cardinality polynomials. Tu, Li, and Du (2021) obtain general maximal-dissociation-set counting bounds and extremal graph classifications; these are not exact formulas for the triangular graph. Tu, Xiao, and Lang (2023) study dissociation polynomials and bounds for cubic graphs, whereas \(T_n\) is not cubic. The present contribution is the simultaneous full and maximal labeled census, the maximality classification with a one-unused-vertex exception, and strict log-concavity with the isolated \(n=7\) equal-cardinality case.

## Limitations

The theorem concerns triangular graphs only. It does not claim that counting all \(K_2/P_3\)-packings is an unknown general combinatorial technique, and it does not supersede the known scalar dissociation maximum. Publication priority remains provisional: searches and inspected literature did not reveal an equivalent full formula, but differently indexed statements or earlier partition-enumerator treatments could exist. The publisher's full text of the especially relevant 2011 paper was not accessible in the available reading route; the visible article material was compared at the level of the relevant line-graph theorem and scope. No independent mathematical review or external certification has been performed.

## References

- J. Tu, Y. Li, and J. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs*, arXiv:2103.01402, first publicly posted 2021-03-02, https://arxiv.org/abs/2103.01402.
- Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366, https://doi.org/10.1016/j.dam.2011.04.023.
- J. Tu, J. Xiao, and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8 (2023), 10021–10032, https://doi.org/10.3934/math.2023507.
