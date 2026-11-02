# Exact single-neighbor equilibrium polynomial on subdivided stars

## Finding
For every spider tree \(S(\ell_1,\ldots,\ell_d)\) with a central vertex of degree \(d\ge3\) and positive integer arm lengths \(\ell_i\), consider a homogeneous binary public-goods game in which a vertex strictly prefers action \(1\) if and only if exactly one of its neighbors chooses \(1\). Write \(I_r=\{i:\ell_i\equiv r\pmod 3\}\), \(m=|I_2|\), and \(\delta=1\) when \(m=0\) and \(|I_1|=1\), and \(\delta=0\) otherwise. The exact polynomial enumerating pure Nash equilibria by the number of producers is

\[
Z_S(z)=\prod_{i\in I_2}\left(1+z^{2(\ell_i+1)/3}\right)
-\sum_{i\in I_2}z^{2(\ell_i+1)/3}
+\delta z^{2+2\sum_{i=1}^{d}\lfloor\ell_i/3\rfloor}.
\]

In particular, the number of equilibria (including the all-zero profile) is \(2^m-m+\delta\), and a nonzero equilibrium exists precisely when \(m\ge2\), or when \(m=0\) and \(|I_1|=1\). For every nonnegative integer \(q\), the coefficient of \(z^q\) is the number of equilibria with exactly \(q\) producers. The formula applies to all positive integer arm lengths and all center degrees at least three, without genericity assumptions.

## Assumptions and scope
The graph is finite, undirected, unweighted, simple and a tree consisting of one hub \(h\) and \(d\) internally disjoint paths from \(h\) to leaves, with \(\ell_i\ge1\) edges in arm \(i\). Every vertex chooses \(s_v\in\{0,1\}\). The unique best-response action is
\[
T(k)=\begin{cases}1,&k=1,\\0,&k\ne1,\end{cases}
\]
where \(k=\sum_{u\in N(v)}s_u\) counts active **open** neighbors (not the vertex itself). For instance, one can choose payoff difference \(u_v(1,k)-u_v(0,k)=1\) when \(k=1\) and \(-1\) otherwise, so the preference is strict at every profile. A pure Nash equilibrium means \(s_v=T(\sum_{u\in N(v)}s_u)\) at every vertex. The producer-count polynomial counts labeled profiles: the individual arms remain distinguished, including when arm lengths coincide.

## Proof
Fix an arbitrary equilibrium. Along an arm, number vertices \(0,1,\ldots,\ell\), with vertex \(0=h\), and denote actions by \(x_j\). At an internal degree-two vertex \(1\le j<\ell\), precisely one of its two neighbors must be active exactly when its action is one. Hence, over \(\mathbb F_2\),
\[
x_j=x_{j-1}\oplus x_{j+1},\qquad x_{j+1}=x_{j-1}\oplus x_j.
\]
Writing the hub action as \(c\) and the first arm action as \(a\), induction yields the three-periodic sequence
\[
(x_0,x_1,x_2,x_3,x_4,\ldots)=(c,a,c\oplus a,c,a,\ldots).
\]
At the leaf the degree is one, so its equilibrium condition is exactly \(x_\ell=x_{\ell-1}\). Inserting the periodic sequence gives the following **necessary and sufficient** boundary constraints:
\[
\begin{array}{c|c}
\ell\bmod3 &\text{leaf constraint}\\ \hline
0&a=0\\ 1&a=c\\ 2&c=0\quad(a\text{ unrestricted}).
\end{array}
\]

If \(c=0\), every arm in \(I_0\cup I_1\) is identically zero. Each arm \(i\in I_2\) independently chooses \(a_i=0\) or \(1\); an activated arm has word \((1,1,0)\) repeated along its noncentral vertices, ending after \(\ell_i\equiv2\pmod3\), and contributes exactly \(2(\ell_i+1)/3\) producers. The hub has as many active neighbors as activated arms. Its own action \(c=0\) is a best response unless **exactly one** arm is activated. Thus all subsets of \(I_2\) are allowed except singleton subsets, giving the product-minus-singletons term. This includes the all-zero profile.

If \(c=1\), no arm may lie in \(I_2\) by the leaf constraint. The first vertex is active precisely on arms in \(I_1\). The hub is active in equilibrium precisely if \(|I_1|=1\). Under those two restrictions there is exactly one equilibrium assignment: all \(I_0\) arms start at zero and all \(I_1\) arms start at one. Every \(I_0\) arm contributes \(2\lfloor\ell_i/3\rfloor\) producers, while its unique \(I_1\) arm contributes \(1+2\lfloor\ell_i/3\rfloor\); the hub contributes one. The total is \(2+2\sum_i\lfloor\ell_i/3\rfloor\), giving the final monomial if \(\delta=1\).

The two hub cases partition every profile, so the polynomial identity is exhaustive. Evaluation at \(z=1\) yields \(2^m-m+\delta\). For \(m=0,1\) the product-minus-singletons counts only the all-zero profile; for \(m\ge2\) there are additional subsets. The hub-active option exists precisely when \(m=0\), \(|I_1|=1\). This proves the existence criterion and the producer-count interpretation.

## Verification
The standalone, standard-library-only program `verify_spiders.py` computes the predicted polynomial independently from the formula and exhaustively enumerates all binary profiles of every spider with \(d\in\{3,4,5\}\), arm lengths bounded in its source and a maximum of sixteen vertices. On execution it reports `PASS 704 spider instances; 4468176 binary profiles exhaustively checked`. Representative formulas include \(Z_{S(2,2,2)}(z)=1+3z^4+z^6\), \(Z_{S(2,3,3)}(z)=1\), and \(Z_{S(1,3,3)}(z)=1+z^6\). The independent direct equilibrium test checks every vertex's open-neighbor active count. These finite checks corroborate, but do not replace, the arbitrary-arm proof above.

## Relationship to prior work
Gilboa and Nisan [1] introduced the specific single-neighbor best-response pattern and proved NP-completeness of deciding whether a **nontrivial** pure Nash equilibrium exists on arbitrary undirected graphs (Theorem 3.1). Their Section 3 explains the corresponding period-three behavior for paths and cycles. The present classification extends that local pattern calculation to a branching hub and enumerates **all** pure equilibria on spiders by producer count; the cited paper's relevant sections do not state this formula or the residue-dependent hub restriction. Gilboa [2] gives a broader complexity characterization; Yang and Wang [3] treat computationally tractable graph families, including bounded treewidth, but do not give this producer-count enumerator. Klimm and Stahlberg [4] investigate different decreasing and picky response patterns. The new claim is the explicit spider family classification, not the general graph hardness or the previously known period-three path recurrence.

## Limitations
The theorem is restricted to a strict, homogeneous, open-neighbor single-neighbor rule on spider trees and to labeled pure equilibria. It does not assert uniqueness of equilibria, convergence of best-response dynamics, or an algorithm on arbitrary graphs. Literature-priority search cannot rule out uncatalogued equivalent enumerations; the path recurrence is classical in the cited 2022 paper. Exhaustive computer enumeration covers only the specified finite sample, while the proof supplies the universal conclusion.

## References
[1] M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, first public arXiv version 2022-07-09, https://arxiv.org/abs/2207.04238, particularly Section 3 and Theorem 3.1.

[2] M. Gilboa, *A Characterization of Complexity in Public Goods Games*, first public arXiv version 2023-01-27, https://arxiv.org/abs/2301.11580.

[3] Y. Yang and J. Wang, *A Refined Study of the Complexity of Binary Networked Public Goods Games*, first public arXiv version 2020-12-05, https://arxiv.org/abs/2012.02916.

[4] M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, 2023, https://arxiv.org/abs/2301.11849.
