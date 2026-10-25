# Minimal forts, full zero-forcing enumerator, and optimal exchanges for Mycielski cliques

## Finding
For every integer \(n\ge 4\), the one-step Mycielski graph \(G_n=\mu(K_n)\) has exactly five forms of inclusion-minimal ordinary zero-forcing forts, as classified below. Its entire zero-forcing-set polynomial is
\[
\mathcal Z(G_n;x)=x^{2n+1}+(2n+1)x^{2n}+\binom{2n+1}{2}x^{2n-1}
+\frac{n(n-1)(2n+3)}2x^{2n-2}
+\frac{n(n-1)(n-2)(n+3)}4x^{2n-3}.
\]
Consequently the minimum zero-forcing number is \(2n-3\), and the number of minimum zero-forcing sets is \(n(n-1)(n-2)(n+3)/4\).

Let \(X_n\) be the graph of minimum zero-forcing sets, adjacent when one selected vertex is exchanged for another. Then \(X_n\) is connected, has exactly three degree strata \(4n-6\), \(4n-9\), and \(4n-10\), with multiplicities respectively
\[
\frac{n(n-1)(n-2)(n-3)}4,\qquad n(n-1)(n-2),\qquad \frac{n(n-1)(n-2)}2.
\]
The exact number of exchange edges is
\[
|E(X_n)|=\frac{n(n-1)(n-2)(2n^2+3n-19)}4.
\]
The emphasis is on the complete finite and infinite solution-set descriptions, rather than on claiming the scalar zero-forcing number as new independently of earlier Mycielski-graph studies.

## Assumptions and scope
All graphs are finite, simple and undirected. Fix \(n\ge4\). There are original vertices \(a_1,\ldots,a_n\), clones \(b_1,\ldots,b_n\) and an apex \(w\). The originals form a clique; the clones are independent; \(a_i\) is adjacent to \(b_j\) exactly if \(i\ne j\); and \(w\) is adjacent to all clones and to no originals. Ordinary zero forcing starts with blue vertices \(S\). A blue vertex with exactly one white neighbor may turn it blue; \(S\) is zero forcing if eventually every vertex is blue.

A **fort** is a nonempty set \(F\) such that no vertex outside \(F\) has exactly one neighbor in \(F\). The complement \(W=V(G_n)\setminus S\) is the initially white set. Write \(A=\{i:a_i\in W\}\) and \(B=\{i:b_i\in W\}\); these are subsets of \([n]\), and \(z=1\) means \(w\in W\). A one-for-one exchange preserves cardinality and the zero-forcing property. Vertex labels are distinct; no quotient by automorphisms is taken.

## Proof
### 1. Fort obstruction equivalence
Any white fort persists under ordinary blue-only forcing: if a blue vertex could first force a member of the fort, it would then have exactly one fort neighbor, contradicting the fort definition. Conversely, if a maximal legal forcing process stops with nonempty white set \(F\), every remaining blue vertex has either zero or at least two neighbors in \(F\). Thus \(F\) itself is a fort. Consequently \(S\) is zero forcing if and only if its white complement contains no fort.

### 2. Exhaustive minimal-fort classification
For any tentative fort \(F\), let \(P=\{i:a_i\in F\}\), \(Q=\{i:b_i\in F\}\) and \(z=\mathbf 1_{\{w\in F\}}\). A vertex outside \(F\) has the following exact number of neighbors inside \(F\):
\[
\begin{array}{ll}
 a_i\notin F:&|P|+|Q|-\mathbf 1_{\{i\in Q\}},\\
 b_i\notin F:&|P|-\mathbf 1_{\{i\in P\}}+z,\\
 w\notin F:&|Q|.
\end{array}
\]
The complete family of inclusion-minimal forts is:
\[
\begin{split}
&\{a_i,a_j,a_k\},\quad \{b_i,b_j,b_k\} &&(i,j,k\text{ pairwise distinct});\\
&\{a_i,a_j,w\},\quad \{a_i,a_j,b_i,b_j\} &&(i\ne j);\\
&\{a_i,b_i,w\}&&(1\le i\le n).
\end{split}
\]
Direct substitution in the displayed neighbor-count formulas proves that every listed set is a fort; none contains a smaller listed fort, hence all are inclusion-minimal once exhaustiveness is established.

To prove exhaustiveness, suppose \(F\) is any nonempty fort. If \(|P|\ge3\), it contains an original triple. If \(|P|=2\) and \(z=1\), it contains \(\{a_i,a_j,w\}\). If \(|P|=2\) and \(z=0\), both clones paired with the two original indices must belong to \(F\), because an omitted one would have exactly one fort neighbor; thus the fourth family occurs. If \(|P|=1\) and \(z=1\), its paired clone must belong to \(F\), giving the last family. If \(|P|=1\) and \(z=0\), every clone not paired with that original must belong to \(F\); because \(n\ge4\), three such clones give a clone triple. Finally, if \(|P|=0,z=1\), every clone must be present, producing a clone triple; while if \(|P|=0,z=0\), a nonempty \(Q\) of size one or two violates a neighbor-count condition, so \(|Q|\ge3\), again giving a clone triple. These cases cover every fort, establishing the exact list.

### 3. Characterization of every forcing set
Avoiding the two triple-fort families requires \(|A|\le2\) and \(|B|\le2\). If \(z=0\), the three-point forts involving the apex are automatically absent, leaving only the four-point fort, which is present exactly when \(|A|=|B|=2\) and \(A=B\). If \(z=1\), apex-containing original pairs force \(|A|\le1\), and apex-containing matched pairs force \(A\cap B=\varnothing\). The fourth family cannot occur then, because \(|A|\le1\). By the fort obstruction equivalence:
\[
S\text{ is zero forcing}\quad\Longleftrightarrow\quad
\begin{cases}
|A|\le2,\ |B|\le2,\ \neg(|A|=|B|=2\ \text{and }A=B),&z=0;\\
|A|\le1,\ |B|\le2,\ A\cap B=\varnothing,&z=1.
\end{cases}
\]
This also proves that every zero-forcing set leaves at most four white vertices.

### 4. Exact enumerator
Define the enumerator by white cardinality \(Q_n(y)=\sum_{S\text{ forcing}}y^{|V(G_n)\setminus S|}\), and write \(p_n(y)=1+ny+\binom n2 y^2\). The preceding characterization gives
\[
Q_n(y)=p_n(y)^2-\binom n2y^4+y\,p_n(y)
+n y^2\left(1+(n-1)y+\binom{n-1}{2}y^2\right).
\]
The first two terms correspond to apex blue, excluding exactly the diagonal ordered pairs of two-subsets. The last two count apex white with, respectively, zero and one white originals. Collecting coefficients gives \(Q_n(y)=1+(2n+1)y+\binom{2n+1}{2}y^2+\frac{n(n-1)(2n+3)}2y^3+\frac{n(n-1)(n-2)(n+3)}4y^4\). Reversing exponents gives \(\mathcal Z(G_n;x)=x^{2n+1}Q_n(1/x)\). Since the degree is exactly four, the largest permissible white set has four vertices, proving the minimum and its count.

### 5. Exchanges, degree strata, and connectivity
A minimum forcing set corresponds to a permissible four-element white set. There are two types. Type I has \(w\notin W\), \(|A|=|B|=2\), \(A\ne B\). Type II has \(w\in W\), \(A=\{i\}\) and \(B=\{j,k\}\) with \(i\notin B\). Split Type I into I0 and I1 according as \(|A\cap B|=0\) or \(1\). Direct choices give their stated multiplicities.

Inside Type I, one-for-one exchange changes either one member of \(A\) or one member of \(B\), corresponding to two coordinates of the Cartesian product \(J(n,2)\mathbin{\square}J(n,2)\), with the diagonal \(A=B\) deleted. The internal degree equals \(4(n-2)\) for I0 and \(4(n-2)-2\) for I1 (the latter loses its two diagonal neighbors). Replacing one original white vertex by the white apex leads to Type II in exactly two ways from I0 and one way from I1. Thus the total degrees are \(4n-6\) and \(4n-9\).

For Type II, its original index may change to any of the \(n-3\) other indices outside \(B\); either of its two clone indices can change in \(n-3\) ways; and replacing the white apex with any other original produces \(n-1\) Type I neighbors. Therefore its degree is \((n-3)+2(n-3)+(n-1)=4n-10\). The handshaking lemma yields the displayed exchange-edge formula.

For connectivity, the Johnson graph \(J(n,2)\) stays connected after removal of any one vertex for \(n\ge4\): any disjoint two-subsets have a common neighbor, and at least four such choices exist, so removing one does not disconnect the graph. For any two distinct-coordinate pairs \((A,B)\) and \((C,D)\), choose a two-subset \(H\) different from \(B\) and \(D\). Move \(A\) to \(H\) in \(J(n,2)-\{B\}\), then \(B\) to \(D\) in \(J(n,2)-\{H\}\), then \(H\) to \(C\) in \(J(n,2)-\{D\}\). Every intermediate pair has unequal coordinates, so Type I is connected. Every Type II vertex has \(n-1\) neighbors in Type I, hence the full exchange graph is connected.

## Verification
The standalone Python 3 script `verify.py` reconstructs graph adjacency, exhaustively tests every initial white subset for \(4\le n\le8\), checks a separate chronological single-force implementation for \(4\le n\le6\), enumerates every inclusion-minimal fort for \(4\le n\le7\), and independently builds the optimal-solution exchange graph. It checks the full polynomial, degree strata, edge count and connectivity; its final line is `ALL_VERIFY_OK`. These finite checks corroborate but do not replace the all-parameter proof.

## Relationship to prior work
The ordinary zero-forcing and \(k\)-forcing framework appears in Amos–Caro–Davila–Pepper [1], an accessible foundational preprint dated 2014-01-23. Boyer et al. [2] introduce the general zero-forcing polynomial and enumerate several graph families; the inspected family results do not treat these Mycielski clique graphs. Geneson–Haas–Hogben [3] introduce minimum-zero-forcing-set reconfiguration and establish general theorems, but their inspected constructions do not classify this family. The fort-obstruction approach is part of the established general zero-forcing toolkit [4]. An indexed 2021 study concerning zero-forcing numbers for some Mycielski graphs [5] may overlap with the scalar minimum; its complete text was inaccessible and the scalar is not asserted as a novel isolated contribution. No stronger inspected result was found that logically gives the five minimal-fort types, full enumerator, and three-stratum connected exchange graph.

## Limitations
Only ordinary (blue-only) zero forcing on the one-step Mycielskian of \(K_n\) for \(n\ge4\) is covered. There is no result here for smaller parameters, iterated Mycielskians, positive-semidefinite forcing, or arbitrary base graphs. The verifier is exhaustive only over the stated finite parameters. Originality remains subject to possible coverage in unindexed literature, notably the inaccessible complete text of [5]; no independent audit or global novelty certification is claimed.

## References
[1] D. Amos, Y. Caro, R. Davila, R. Pepper, *Upper bounds on the k-forcing number of a graph*, arXiv:1401.6206v1 (2014-01-23). https://arxiv.org/abs/1401.6206

[2] K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018). https://arxiv.org/abs/1801.08910

[3] J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (2020). https://arxiv.org/abs/2009.00220

[4] B. Brimkov and J. Carlson, *Minimal Zero Forcing Sets*, arXiv:2204.01810 (2022). https://arxiv.org/abs/2204.01810

[5] Z. Rameh, indexed 2021 publication on zero-forcing numbers for Mycielski graph constructions; indexed abstract only, full text not available in this review. https://sid.ir/paper/953698/en
