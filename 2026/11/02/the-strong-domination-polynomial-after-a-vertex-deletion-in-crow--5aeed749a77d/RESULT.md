# The strong-domination polynomial after a vertex deletion in crown graphs

## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph obtained by deleting a perfect matching, and let \(v\) be any vertex. A subset \(D\) strongly dominates a graph \(G\) when each vertex \(w\notin D\) has a neighbor \(u\in D\) satisfying \(\deg_G(u)\ge\deg_G(w)\). Write
\[
P_n(z)=\sum_{D\text{ strongly dominates }\operatorname{Cr}_n-v}z^{|D|}.
\]
Then
\[
\boxed{P_n(z)=z^{n-1}(1+z)^{n-1}+z^n+(n-1)z^3(1+z)^{n-2}
+z(1+z)^{n-1}\big((1+z)^{n-1}-1-(n-1)z\big).}
\]
In particular, \(\gamma_{\mathrm{st}}(\operatorname{Cr}_3-v)=2\), while \(\gamma_{\mathrm{st}}(\operatorname{Cr}_n-v)=3\) for \(n\ge4\). For \(n\ge4\), there are exactly \(\binom n2+\mathbf 1_{n=4}\) minimum strong dominating sets. For \(n=3\), there is exactly one. Evaluating at \(z=1\) gives exactly \(4^{n-1}+1-(n-1)2^{n-2}\) strong dominating sets in total.

The polynomial is stronger than the scalar sensitivity result: it enumerates all strong dominating sets by size, distinguishes the exceptional small orders, and determines the shapes of all minima.

## Assumptions and scope
All graphs are finite, simple, undirected and have ordinary vertex degree measured **after** deletion. Label the two parts of \(\operatorname{Cr}_n\) as \(A=\{a_0,\ldots,a_{n-1}\}\) and \(B=\{b_0,\ldots,b_{n-1}\}\); the edge \(a_ib_j\) exists exactly when \(i\ne j\). Every vertex is equivalent by an automorphism interchanging parts and permuting paired indices, so it suffices to delete \(a_0\). The vertices of the resulting graph are \(A'=\{a_1,\ldots,a_{n-1}\}\) and all \(B\). Their degrees are
\[
\deg(a_i)=n-1\ (i\ge1),\quad \deg(b_0)=n-1,\quad \deg(b_j)=n-2\ (j\ge1).
\]
The definition uses the non-strict degree comparison \(\ge\), not strict \(>\).

## Proof
Write \(D_A=D\cap A'\), \(D_B=D\cap B\). We prove a disjoint, necessary-and-sufficient partition of all strongly dominating sets.

**Case 1: \(b_0\notin D\).** Every vertex \(a_i\notin D\) would need to be dominated by some selected neighbor in \(B\). All its neighbors are among \(b_j\) with \(j\ge1\), of degree \(n-2<n-1=\deg(a_i)\), which cannot strongly dominate \(a_i\). Thus \(D_A=A'\). Conversely these selected \(n-1\) vertices dominate every unselected vertex of \(B\), since \(n\ge3\) and each \(b_j\) has an adjacent member of \(A'\) of degree at least its own. The selection among \(b_1,\ldots,b_{n-1}\) is unrestricted. Its contribution is \(z^{n-1}(1+z)^{n-1}\).

**Case 2: \(b_0\in D\).** The selected \(b_0\) strongly dominates every \(a_i\notin D\); every \(b_j\notin D\), with \(j\ge1\), requires a selected \(a_i\) with \(i\ne j\). If \(|D_A|=0\), all \(b_1,\ldots,b_{n-1}\) must be selected; contribution \(z^n\). If \(D_A=\{a_i\}\), then \(b_i\) must be selected, while every other \(b_j\) is optional. There are \(n-1\) choices of \(i\), giving \((n-1)z^3(1+z)^{n-2}\). If \(|D_A|\ge2\), each \(b_j\) has an adjacent selected \(a_i\), because at most one of the selected \(a_i\) can be indexed by \(j\). Thus all other \(B\)-vertices are optional, contributing
\[
z(1+z)^{n-1}\sum_{k=2}^{n-1}\binom{n-1}{k}z^k
=z(1+z)^{n-1}\big((1+z)^{n-1}-1-(n-1)z\big).
\]
These cases exhaust all subsets, and summing proves the polynomial.

For \(n=3\), the unique term of least degree is \(z^{2}\) from Case 1. For \(n\ge4\), the least possible degree in Cases 2(b) and 2(c) is \(3\). They give \(n-1\) sets \(\{b_0,a_i,b_i\}\) and \(\binom{n-1}{2}\) sets \(\{b_0,a_i,a_j\}\), respectively. Case 1 contributes a size-three set only when \(n=4\), namely \(A'\). Hence the stated minimum numbers and counts. All other cases have cardinality at least these minima.

For comparison, \(\gamma_{\mathrm{st}}(\operatorname{Cr}_n)=2\) for \(n\ge3\): the graph is regular, and selecting matched nonadjacent vertices \(\{a_i,b_i\}\) dominates it; no single vertex dominates its own part. Thus single-vertex deletion changes this parameter exactly for \(n\ge4\), and the polynomial resolves the full residual family.

## Verification
The standalone `verify.py` builds each deleted crown graph directly, recomputes every degree, and checks every vertex subset against the defining strong-domination condition. It separately expands the displayed polynomial using integer binomial coefficients. For every \(3\le n\le9\), the complete size histogram agrees coefficient by coefficient, over a total of 174752 inspected subsets. Run `python3 verify.py`. This finite census corroborates but is not needed for the unrestricted proof.

## Relationship to prior work
Alikhani, Mehraban and Shojaaldini Ardakani study vertex-deletion sensitivity of the strong domination number (arXiv:2601.03891; first public 2026-01-07). Their manuscript treats complete bipartite graphs and cocktail-party graphs, but not the matching-deleted bipartite crown family or its all-set polynomial. In particular \(K_{n,n}\) and \(\operatorname{Cr}_n\) are different graphs; the latter is not the ordinary cocktail-party graph \(K_{2n}-M\).

Alikhani and Ghanbari's earlier vertex-modification bounds (arXiv:2212.01860) concern scalar strong-domination numbers, not this enumerator. Raj and Abirami's published *Strong Domination Polynomials of Queen Crown Graph* (2020) uses a graph denoted \(Q_{m,2}\) that is actually \(K_{m,2}\), not \(K_{n,n}-M\); its formulas do not imply the present result. Other domination polynomials on crown graphs concern different domination predicates. No complete-priority claim beyond the searched and inspected literature is asserted.

## Limitations
The exact expression concerns only removal of one vertex from ordinary crown graphs of order \(2n\) for \(n\ge3\). It does not treat arbitrary vertex removals, other kinds of domination, or every minimum solution for an unrelated graph. The literature comparison cannot rule out inaccessible or unindexed equivalent results, including an inaccessible complete 2023 article about strong dominating sets on other families. Self-review is not independent mathematical validation.

## References
1. S. Alikhani, M. Mehraban, H. Shojaaldini Ardakani, *Stability of the Strong Domination Number of Graphs*, arXiv:2601.03891 (initial submission 2026-01-07), https://arxiv.org/abs/2601.03891.
2. S. Alikhani and N. Ghanbari, *Strong domination number of a modified graph*, arXiv:2212.01860 (2022), https://arxiv.org/html/2212.01860v1.
3. S. Angelin Kavitha Raj and S. Jeya Mangala Abirami, *Strong Domination Polynomials of Queen Crown Graph*, International Journal of Mathematics Trends and Technology 66(2) (2020), 99–104, https://ijmttjournal.org/public/assets/volume-66/issue-2/IJMTT-V66I2P510.pdf.
4. H. Zaherifar, S. Alikhani and N. Ghanbari, *On the strong dominating sets of graphs*, Journal of Algebraic Systems 11(1) (2023), 65–76, DOI:10.22044/JAS.2022.11646.1595 (full text not retrievable for this comparison).
