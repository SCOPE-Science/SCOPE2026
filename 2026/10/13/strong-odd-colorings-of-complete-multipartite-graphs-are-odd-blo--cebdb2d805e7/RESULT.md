# Strong odd colorings of complete multipartite graphs are odd-block partitions
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\), and put \(e=|\{i:n_i\text{ is even}\}|\). A proper coloring of \(G\) is a strong odd coloring if and only if every nonempty color class has odd cardinality. Consequently,
\[
\chi_{\mathrm{so}}(G)=r+e.
\]
More generally, if \(F_G(q)\) denotes the number of strong odd colorings \(V(G)\to[q]\) with a fixed labeled palette and
\[
A(n,k)=2^{-k}\sum_{j=0}^{k}(-1)^j\binom{k}{j}(k-2j)^n=n![z^n](\sinh z)^k,
\]
then for every integer \(q\ge1\),
\[
F_G(q)=\sum_{\substack{1\le k_i\le n_i,\ k_i\equiv n_i\pmod 2\\K=\sum_i k_i\le q}}
\frac{q!}{(q-K)!\prod_i k_i!}\prod_i A(n_i,k_i).
\]
In particular, with \(k=r+e\), the number of optimal strong odd colorings using the labeled palette \([k]\) is
\[
k!\,2^{\sum_{i:n_i\text{ even}}(n_i-2)},
\]
and modulo permutation of the colors the number is \(2^{\sum_{i:n_i\text{ even}}(n_i-2)}\).

For a complete bipartite graph this specializes to \(\chi_{{\mathrm{{so}}}}(K_{{m,n}})=2\) when both shores are odd, \(3\) when exactly one shore is even, and \(4\) when both shores are even. Thus the previously recorded uniform upper bound \(\chi_{{\mathrm{{so}}}}(K_{{m,n}})\le4\) has a sharp parity refinement.

## Assumptions and scope
Graphs are finite, simple, and vertex-labeled when colorings are counted. The complete multipartite graph has \(r\ge2\) nonempty partite sets \(V_1,\ldots,V_r\), with \(|V_i|=n_i\). A strong odd coloring is a proper vertex coloring such that, for every vertex \(v\) and every color occurring in \(N(v)\), that color occurs an odd number of times in \(N(v)\). The counting function \(F_G(q)\) counts maps to the fixed labeled palette \([q]\); colors are permitted to be unused. The final optimal-count formula uses exactly \(k=\chi_{{\mathrm{{so}}}}(G)\) labeled colors.

## Proof
Properness forces every color class to lie in a single partite set, because vertices in different parts are adjacent. Fix a nonempty color class \(C\subseteq V_i\). Since \(r\ge2\), choose a vertex \(v\in V_j\) with \(j\ne i\). Every vertex of \(C\) is adjacent to \(v\), so color \(C\)'s multiplicity in \(N(v)\) is exactly \(|C|\). Hence every color class of a strong odd coloring has odd size. Conversely, if every color class has odd size, then for any vertex \(v\in V_j\), each color visible in \(N(v)\) belongs to some part \(V_i\) with \(i\ne j\), and its neighborhood multiplicity equals its odd global class size. This proves the characterization.

Therefore coloring a part \(V_i\) amounts exactly to partitioning its \(n_i\) vertices into nonempty odd blocks, using colors that cannot be used in any other part. An odd \(n_i\) needs one block and an even \(n_i\) needs at least two; two suffice for even \(n_i\) by splitting it as \(1+(n_i-1)\). Summing over parts gives \(\chi_{{\mathrm{{so}}}}(G)=r+e\).

For the full count, let \(A(n,k)\) be the number of onto maps from an \(n\)-element labeled set to \(k\) labeled colors with every fiber odd. The exponential generating function for one nonempty odd fiber is \(\sinh z\), hence
\[
A(n,k)=n![z^n](\sinh z)^k.
\]
Expanding \((\sinh z)^k=2^{{-k}}(e^z-e^{{-z}})^k\) gives the displayed finite sum. In a coloring of \(G\), suppose part \(V_i\) uses \(k_i\) colors and set \(K=\sum_i k_i\). Necessarily \(1\le k_i\le n_i\) and \(k_i\equiv n_i\pmod2\). Choose pairwise disjoint labeled color sets for the parts in
\[
\frac{{q!}}{{(q-K)!\prod_i k_i!}}
\]
ways, then color each \(V_i\) onto its selected colors in \(A(n_i,k_i)\) ways. Summation proves the formula for \(F_G(q)\).

At the minimum \(k=r+e\), every odd part uses one color and every even part uses two. For a fixed unordered pair of colors on an even part of order \(n_i\), exactly \(2^{{n_i-1}}\) assignments have both color classes odd. Allocating the \(k\) labeled colors among the parts contributes \(k!/2^e\); multiplying yields \(k!2^{{\sum_{{i:n_i\text{{ even}}}}(n_i-2)}}\). Dividing by \(k!\) gives the count modulo color permutation.

## Verification
The general proof is symbolic and does not rely on finite enumeration. The accompanying `verify.py` independently constructs neighborhoods and tests strong oddness for every coloring in 48 small multipartite parameter tuples with \(2\le r\le4\), part sizes at most \(4\), total order at most \(6\), and every palette size through \(\min\{|V(G)|,5\}\). It checks the full formula for \(F_G(q)\), the minimum-color consequence, and the optimal-count consequence. It also checks the closed minimum and optimal-count formulas on 700 larger deterministic parameter tuples. Its replay output is recorded in `VERIFICATION.md`.

## Relationship to prior work
Kwon and Park introduced strong odd coloring in arXiv:2401.11653. Caro, Petruševski, Škrekovski, and Tuza explicitly note for complete bipartite graphs only the uniform bound \(\chi_{{\mathrm{{so}}}}(K_{{m,n}})\le4\) while contrasting strong odd coloring with square coloring. Manattu, Vinay, and Lakshmanan study joins of a cycle with an empty graph in arXiv:2602.03259v1. Their Observation 1 is the related local fact that every color used on the cycle side of \(C_n\vee\overline{{K}}_m\) has odd cardinality, and their Theorem 2 determines that cycle-empty-graph join family. Their paper lists primary AMS classification 05C15 and states that exact values are known for few classes. Its full text does not state a complete bipartite or complete multipartite classification. Pradhan, Sharma, and Verma, arXiv:2610.01441v1, again use the complete-bipartite example only through the bound \(\chi_{{\mathrm{{so}}}}(K_{{m,n}})\le4\) while studying complexity.

A published-finding corpus comparison found the nearby published result `2026/9/30/SCOPE-exact-odd-chromatic-number-and-optimal-coloring-count-for-comple--2f4a2e65a3d2`, which treats the weaker ordinary odd chromatic number of complete multipartite graphs. Its value \(r+\max\{{0,2-o\}}\), where \(o\) counts odd parts, does not imply the present strong-odd formula. For example, when all \(r\) parts are even and \(r>2\), the ordinary odd value there is \(r+2\), while the strong odd value here is \(2r\).

## Limitations
The theorem is restricted to complete multipartite graphs with at least two parts. It does not determine strong odd coloring counts for arbitrary joins whose factors contain edges. The literature comparison cannot exclude an unindexed equivalent observation under different terminology, although exact-family, parity-formula, complete-bipartite, and counting searches were carried out and highly relevant full texts were inspected. The executable verification is finite supplementary evidence; the infinite statement rests on the proof above.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336; Discrete Mathematics 348 (2025), 114601.
3. A. J. Manattu, A. Vinay, and A. Lakshmanan S., *On a conjecture about the strong odd chromatic number of planar graphs*, arXiv:2602.03259v1; primary AMS 05C15.
4. D. Pradhan, V. Sharma, and S. Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441v1.
