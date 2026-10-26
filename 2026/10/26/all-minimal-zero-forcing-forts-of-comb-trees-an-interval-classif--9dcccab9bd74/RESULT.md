# All minimal zero-forcing forts of comb trees: an interval classification and quadratic enumerator

## Finding
For every integer \(n\geq1\), let \(B_n=P_n\circ K_1\) be the comb tree whose spine is \(v_1\cdots v_n\) and whose private pendant leaf at \(v_i\) is \(w_i\). A fort is a nonempty vertex set \(F\) such that no vertex outside \(F\) has exactly one neighbor in \(F\). The fort is *minimal* when no nonempty proper subset is also a fort.

**Classification.** Every minimal fort is specified uniquely by \(1\leq a\leq b\leq n\) with \(b-a\) even. Put \(S_{a,b}=\{a,a+2,\ldots,b\}\). Its vertex set is
\[
F_{a,b}=\{v_i,w_i:i\in S_{a,b}\}\cup
\bigl(\{w_{a-1}\}\text{ if }a>1\bigr)\cup
\bigl(\{w_{b+1}\}\text{ if }b<n\bigr).
\]
The two conditional boundary sets are empty when their condition fails. Distinct parameter pairs give distinct minimal forts.

Consequently, the **number of minimal forts**, and their **size-generating polynomial** \(\Phi_n(z)=\sum_{F\text{ minimal fort}}z^{|F|}\), are respectively
\[
\boxed{\#\{F\text{ minimal fort of }B_n\}=\left\lfloor\frac{(n+1)^2}{4}\right\rfloor},
\]
\[
\boxed{\Phi_n(z)=\sum_{k=1}^{\lfloor n/2\rfloor}
\bigl(2z^{2k+1}+(n-2k)z^{2k+2}\bigr)
+\mathbf1_{\{n\text{ odd}\}}z^{n+1}.}
\]
In particular, every \(n\geq2\) has smallest minimal-fort cardinality \(3\) and largest minimal-fort cardinality \(n+1\); for \(n=1\), its unique minimal fort is the two-vertex graph.

## Assumptions and scope
Graphs are finite, simple and undirected; \(P_1\circ K_1\) is a single edge. Vertex labels \(v_i,w_i\) are distinguished, while the polynomial counts each vertex subset once. A minimal fort means *inclusion-minimal*, not a fort of minimum size. The statement is for all positive integers \(n\), with no asymptotic or computational cutoff.

## Proof
**Step 1: canonical forts.** Given a fort \(F\), let \(S=\{i:v_i\in F\}\). The set \(S\) is nonempty: otherwise any leaf \(w_i\in F\) has its spine vertex \(v_i\notin F\) with exactly one neighbor in \(F\). If \(i\in S\), then \(w_i\in F\), since its degree-one neighborhood would otherwise contain exactly one fort vertex. For \(j\notin S\), let \(d_j(S)\in\{0,1,2\}\) count the adjacent spine vertices whose indices lie in \(S\). To avoid exactly one fort neighbor at \(v_j\), its leaf \(w_j\) must be absent when \(d_j=0\), present when \(d_j=1\), and may be present or absent when \(d_j=2\). At \(d_j=2\), deleting \(w_j\) preserves the fort property; hence a minimal fort never contains such an optional leaf.

Define \(F(S)\) by containing each \(v_i,w_i\) for \(i\in S\), and for \(j\notin S\) containing \(w_j\) exactly when \(d_j(S)=1\). Every \(F(S)\) is a fort, and all minimal forts are among the \(F(S)\).

**Step 2: an exact inclusion criterion.** For \(\varnothing\neq T\subseteq S\), inclusion \(F(T)\subseteq F(S)\) fails precisely if there is some \(j\notin S\) such that \(d_j(S)=2\) but \(d_j(T)=1\). Indeed, the only way \(F(T)\) can contain a leaf missing from \(F(S)\) is to create exactly one chosen spine neighbor at such an index. For every \(j\notin S\) with both \(j-1,j+1\in S\), introduce an edge \(\{j-1,j+1\}\) in an auxiliary graph \(H_S\), whose vertex set is \(S\). The preceding condition shows that \(F(T)\subseteq F(S)\) exactly when \(T\) is a nonempty union of connected components of \(H_S\).

Therefore \(F(S)\) is inclusion-minimal **if and only if** \(H_S\) is connected. If \(H_S\) has two components, choosing one gives a proper subfort; if it is connected, the only nonempty permissible \(T\) is \(S\). A proper fort of \(F(S)\) is necessarily canonical by the same argument as in Step 1 (or contains a canonical subfort), so this criterion detects *all* proper subforts.

**Step 3: connected sets.** Edges in \(H_S\) join indices at distance exactly two, with their intermediate index absent from \(S\). Therefore a connected \(H_S\) has \(S=\{a,a+2,\ldots,b\}\); conversely, every such progression induces a connected path (including a one-vertex path). In this case an outside spine index has exactly one neighbor in \(S\) only when it is \(a-1\) or \(b+1\), provided that index exists. Thus the canonical fort is exactly \(F_{a,b}\), establishing the classification.

**Step 4: exact sizes.** Fix \(k=|S_{a,b}|\), so \(b=a+2(k-1)\). There are \(n-2k+2\) possible starting indices \(a\), for \(1\leq k\leq\lceil n/2\rceil\). The fort has \(2k\) vertices from chosen spine-leaf pairs, plus one leaf at each existing outside boundary. For \(1\leq k\leq\lfloor n/2\rfloor\), exactly two starting indices meet one endpoint and yield size \(2k+1\); the remaining \(n-2k\) meet neither endpoint and yield size \(2k+2\). If \(n\) is odd, the final \(k=(n+1)/2\) has a single progression meeting both endpoints and gives size \(n+1\). This proves the displayed size polynomial. Evaluating at \(z=1\) gives \(\sum_{k=1}^{\lceil n/2\rceil}(n-2k+2)=\lfloor(n+1)^2/4\rfloor\). The extreme cardinalities follow from the same formula. \(\square\)

## Verification
A standalone Python 3 standard-library verifier, supplied as `verify.py`, constructs the graph from edges and independently enumerates all nonempty subsets, checks the original neighborhood definition, and uses a subset dynamic program to determine inclusion-minimality. It compares the *full labeled set family* with the theorem and then compares cardinality counts for every \(1\leq n\leq9\): exactly \(349524\) subsets, \(2055\) forts, and \(95\) minimal forts were processed. The verifier recorded `VERIFICATION_OK`. The proof above, not the finite experiment, establishes the all-order result.

## Relationship to prior work
Becker–Cameron–Hanely–Ong–Previte (arXiv:2404.05963, first public 9 April 2024) introduced the minimal-fort enumerative program and explicitly depicted a fort of the 4-comb in Figure 1. Their explicit formulas address paths, cycles and spiders, while Section 5.2 concerns different corona constructions; the figure is not a family classification. Cameron–Li (arXiv:2512.12874, Theorem 3.3) gives a necessary-and-sufficient cut characterization of minimal forts in **all trees**; this offers a general membership test but does not itself state the comb interval classification or its cardinality polynomial. Dat–Kenter (arXiv:2605.07298) proves a general tree-count upper bound and develops a small-tree enumeration algorithm; neither result supplies this closed, all-order comb census. The proof here does not assume these prior theorems.

## Limitations
The formula applies to exactly one leaf per spine vertex and does not classify arbitrary caterpillars, unequal leaf multiplicities, cyclic coronas or other rooted tree products. Priority remains subject to unindexed equivalent enumerations and to detailed independent literature verification. The result has received a self-review only; no independent mathematical audit has been performed.

## References
1. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963 (first public 2024-04-09), especially Figure 1, Theorem 16 and Section 5.2.
2. T. R. Cameron and K. Li, *On the minimal forts of trees*, arXiv:2512.12874 (first public 2025-12-14), Theorem 3.3.
3. N. H. Dat and F. H. J. Kenter, *On the Number of Zero Forcing Minimal Forts on Trees*, arXiv:2605.07298 (first public 2026-05-08), Theorem 1 and Section 3.
