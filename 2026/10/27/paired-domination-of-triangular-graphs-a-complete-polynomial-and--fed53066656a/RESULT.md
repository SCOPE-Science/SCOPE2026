# Paired domination of triangular graphs: a complete polynomial and minimum-set census

## Finding

Let \(T_n=J(n,2)=L(K_n)\), for every integer \(n\ge3\). Vertices of \(T_n\) are unordered pairs from \([n]\), adjacent when they intersect. For any set \(D\subseteq V(T_n)\), interpret its vertices as edges \(F\subseteq E(K_n)\). Write \(i(F)\) for the number of isolated vertices in the spanning graph \(([n],F)\), and list the connected components containing edges as \(H_1,\ldots,H_s\).

**Structural classification.** The subset \(D\) is a paired-dominating set of \(T_n\) if and only if
\[
i(F)\le1\quad\text{and}\quad |E(H_j)|\equiv0\pmod2\quad(1\le j\le s).
\]
Here paired domination means that every vertex outside \(D\) has a neighbor in \(D\), and that the graph induced on \(D\) has a perfect matching.

**Complete cardinality polynomial.** If
\[
A(x,z)=\sum_{j\ge0}\frac{x^j}{j!}(1+z)^{\binom j2},
\]
then the polynomial \(Q_n(z)=\sum_{D\text{ paired-dominating}}z^{|D|}\) is
\[
\boxed{Q_n(z)=n!\,[x^n]\,(1+x)e^{-x}\sqrt{A(x,z)A(x,-z)}.}
\]
The square root means the unique formal power series in \(x\) with constant term \(1\), and the expression is interpreted in the ring of formal series in \(x\) with rational-polynomial coefficients in \(z\).

**Minimum size and complete minimum-set census.** Define \(b=\lceil(n-1)/3\rceil\). Then
\[
\boxed{\gamma_{\mathrm{pr}}(T_n)=2b.}
\]
Let \(M_n\) be the number of sets of this size. For integers \(t\ge1\), the following are exact; an indicated term is omitted when its indexing condition fails:
\[
\begin{aligned}
M_{3t}&=\frac{(3t)!}{2^t t!}
 +\mathbf1_{\{t\ge2\}}\frac{(3t)!\,125}{5!\,2^{t-2}(t-2)!},\\
M_{3t+1}&=\frac{(3t+1)!}{2^t t!},\\
M_{3t+2}&=(3t+2)!\left(
 \frac{125}{5!\,2^{t-1}(t-1)!}
 +\frac{15}{4!\,2^{t-1}(t-1)!}
 +\mathbf1_{\{t\ge2\}}\frac{7^5}{7!\,2^{t-2}(t-2)!}
 +\mathbf1_{\{t\ge3\}}\frac{125^2}{2(5!)^2\,2^{t-3}(t-3)!}
 \right).
\end{aligned}
\]
In terms of actual selected-edge components, the minimum families are exhausted by the following mutually exclusive types. A \(P_3\) is a two-edge path on three original vertices; an *internal tree* means any labeled tree on the prescribed original vertex set.

* For \(n=3t\): either \(t\) disjoint \(P_3\) components and no isolated vertex; or \(t-2\) such paths, one five-vertex tree, and one isolated vertex (second type requires \(t\ge2\)).
* For \(n=3t+1\): \(t\) disjoint \(P_3\) components and one isolated vertex.
* For \(n=3t+2\): either \(t-1\) disjoint \(P_3\) components and a five-vertex tree, with no isolate; or exactly one isolate and one of these: a connected four-edge graph on four vertices plus \(t-1\) disjoint paths; a seven-vertex tree plus \(t-2\) paths (\(t\ge2\)); or two five-vertex trees plus \(t-3\) paths (\(t\ge3\)).

## Assumptions and scope

All graphs are finite, simple, and undirected. The parameters are integers \(n\ge3\). A perfect matching of the induced subgraph \(T_n[D]\) pairs up *all* selected vertices in adjacent pairs. Isolated vertices and connected components in the structural criterion refer to \(([n],F)\), **not** to \(T_n\). No assumption is made that \(F\) is connected. All counts distinguish the labels \([n]\), but not the order of edges or components. The generating-function identity is formal and does not require convergence.

## Proof

**1. Ordinary domination becomes a bound on isolates.** Each vertex of \(T_n\) is a possible edge \(uv\) of \(K_n\). It is in \(D\) or adjacent to a vertex of \(D\) exactly when \(u\) or \(v\) is incident to a selected edge. A non-dominated vertex therefore exists if and only if at least two original vertices are isolated in \(([n],F)\). Thus \(D\) dominates \(T_n\) exactly when \(i(F)\le1\).

**2. Adjacent-edge pairing lemma.** Let \(H\) be a finite connected graph with at least one edge. The edges of \(H\) can be partitioned into pairs of edges sharing a common endpoint **if and only if** \(|E(H)|\) is even. Necessity follows by counting pairs. For sufficiency, fix a rooted spanning tree of \(H\), and arbitrarily assign each non-tree edge to one endpoint. Work upward from the leaves. At a nonroot vertex, its currently unpaired incident edges consist of edges passed from its children, plus assigned non-tree edges, say \(r\) edges. When \(r\) is even, pair these edges locally and leave its parent-tree edge available for the parent. When \(r\) is odd, pair one of them with the parent-tree edge and pair the remaining edges locally. At the root, all earlier pairings have consumed an even number of edges, so the number left is even because \(|E(H)|\) is even; pair those remaining incident edges at the root. Every edge is paired exactly once, and each pair shares the chosen vertex. This establishes sufficiency without invoking a matching theorem.

Since \(T_n[D]=L(F)\), its connected components come from the edge-containing connected components of \(F\). A matching of \(L(F)\) is precisely a partition of selected edges into adjacent pairs. Applying the lemma componentwise proves the structural classification with Step 1.

**3. Exponential enumeration.** The formal labeled-graph exponential generating function is \(A(x,z)\), since there are \(\binom j2\) potential edges among a fixed set of \(j\) labels. Let \(C(x,z)=\log A(x,z)\); the exponential formula says \(C\) enumerates connected graphs, including isolated one-vertex components. The even-edge connected components are selected by
\[
C_{\mathrm{even}}(x,z)=\tfrac12(C(x,z)+C(x,-z)),
\]
which includes isolated one-vertex components with term \(x\). Taking an arbitrary set of even-edge components while forbidding *two or more isolates* therefore gives
\[
(1+x)\exp(C_{\mathrm{even}}(x,z)-x)
=(1+x)e^{-x}\sqrt{A(x,z)A(x,-z)}.
\]
The coefficient of \(x^n/n!\) counts exactly the admissible labeled selected-edge graphs by their edge counts. This gives the displayed polynomial.

**4. Exact minimum cardinality.** Suppose \(|F|=2b'\) is a paired-dominating set. Its adjacent-edge pairing has \(b'\) pairs. Each pair has precisely three incident original vertices, so \(F\) covers at most \(3b'\) original vertices. Since it leaves at most one isolated original vertex, \(3b'\ge n-1\). Thus \(|F|\ge2\lceil(n-1)/3\rceil\). To attain equality when \(n=3t\) or \(3t+1\), take \(t\) disjoint \(P_3\) paths, leaving respectively zero or one original vertices isolated. For \(n=3t+2\), take \(t+1\) wedges formed by two incident edges, arranged to cover precisely \(3t+2\) vertices by letting one pair of wedges meet at exactly one original vertex and all remaining wedges be disjoint. This works for \(t\ge1\). Each constructed edge-bearing component has an even number of edges, and Step 1 shows domination. Hence the lower bound is sharp.

**5. Classification of equality and its census.** Every edge-containing component of a minimum \(F\) has an even number \(2r_j\) of edges, covers \(v_j\) original vertices, and is connected, so \(v_j\le2r_j+1\). Define its nonnegative defect \(\delta_j=3r_j-v_j\). Then \(\delta_j\ge r_j-1\). For a two-edge component \(r_j=1\), connectivity forces a \(P_3\) with defect zero. With \(b=\sum_jr_j=\lceil(n-1)/3\rceil\), the identity
\[
\sum_j\delta_j=3b+i(F)-n
\]
shows that total defect is at most two. Therefore no component has more than six edges. If a component has four edges, its defect is one exactly when it is a tree on five vertices, or two exactly when it is a connected graph on four vertices. There are \(5^{5-2}=125\) labeled trees on five vertices and exactly \(\binom64=15\) four-edge graphs on four labeled vertices, all connected. If a component has six edges, defect two forces a tree on seven vertices, of which there are \(7^{7-2}=7^5\) labeled examples. These exhaust all positive-defect possibilities, together with pairs of independent defect-one five-vertex trees.

When \(n=3t\), the defect identity is \(\sum_j\delta_j=i(F)\), yielding exactly the two families stated. When \(n=3t+1\), it is \(\sum_j\delta_j=i(F)-1\), hence one isolate and only \(P_3\) components. When \(n=3t+2\), it is \(\sum_j\delta_j=1+i(F)\), giving precisely the four listed component profiles. These derivations also prove no minimum family is missing.

Finally choose disjoint labeled vertex blocks for each component and, where present, the isolated vertex. Each \(P_3\) on three fixed labels has exactly three possibilities. Thus \(k\) disjoint \(P_3\) components contribute \(3^k/(3!^k k!)=1/(2^k k!)\) times the appropriate global factorial and other component factors. A five-vertex tree contributes \(125/5!\); a four-vertex four-edge graph contributes \(15/4!\); a seven-vertex tree contributes \(7^5/7!\); and two indistinguishable five-vertex trees introduce a factor \(1/2\). Multiplying these factors, using one distinguished unselected isolate where applicable, gives the formulas for \(M_n\).

## Verification

The standalone files `verify.py`, `full_n7.py`, and `count_min.py` independently implement finite cases of the original definitions and structural criterion. `verify.py` exhaustively checks all \(2^{\binom n2}\) vertex subsets for \(3\le n\le6\), comparing ordinary domination and a direct matching dynamic program with the component-parity characterization, and checks minimum counts. `full_n7.py` exhaustively enumerates all \(2^{21}=2{,}097{,}152\) choices for \(n=7\), using the original paired-domination definition without testing the structural criterion. `count_min.py` exhaustively enumerates all candidate minimum edge sets through \(n=8\), comparing the census formulas. The captured deterministic output is in `CHECKS.txt`.

The resulting optimum multiplicities for \(n=3,4,5,6,7,8\) are respectively \(3,12,200,840,630,168056\). A separate symbolic formal-series calculation through \(n=7\) independently agreed with every brute-force polynomial coefficient; this symbolic check does not replace the combinatorial proof. All verifiers use only the Python standard library. Re-run with `python verify.py`, `python full_n7.py`, and `python count_min.py` in the same directory.

## Relationship to prior work

Paired domination requires both ordinary domination and a perfect matching in the induced selected subgraph. Jiang, Wu, Zhang, and Rao (2021) investigate *upper* paired-domination complexity and variants and provide a verified 2021 public source with graph-domination MSC classification. Their results do not imply the component-even-edge characterization or all-subset enumerator for \(L(K_n)\). Puttaswamy, Alwardi, and Nayaka introduce paired-domination polynomials as an object of study, not this family-specific explicit polynomial. Lu, Wang, Wang, and Wu establish upper bounds for claw-free graphs in general, rather than an equality classification or a full optimizer census for these triangular line graphs. Prior results for paired domination in complete multipartite graphs and chain graphs concern different graph classes: \(T_n\) is neither of those for general \(n\). The general fact that a line graph translates edge adjacency does not itself supply the nontrivial minimum-set classification or the polynomial coefficient identity; those are proved above.

## Limitations

The result treats ordinary paired domination of triangular graphs \(L(K_n)\) only. It does not classify arbitrary Johnson graphs, line graphs of general host graphs, or upper paired domination. Finite verification is evidence of implementations and boundary cases, not an infinite proof. A targeted literature comparison did not identify a stronger published theorem covering this complete enumeration; inaccessible or unindexed equivalent work remains a possible priority risk. Independent mathematical validation has not been performed.

## References

1. H. Jiang, P. Wu, J. Zhang, and Y. Rao, "Upper paired domination in graphs," *AIMS Mathematics* 7 (2022), 1009–1020, first made public 2021-10-21. DOI: 10.3934/math.2022069.
2. Puttaswamy, A. Alwardi, and S. R. Nayaka, "Introduction to Paired Domination Polynomial of a Graph," World Academy of Science, Engineering and Technology (2016), accessible abstract.
3. C. Lu, K. Wang, C. Wang, and M. Wu, "Paired-domination in claw-free graphs with minimum degree at least three," *Discrete Applied Mathematics* (2019). DOI: 10.1016/j.dam.2018.09.005.
