# The complete square-zero rank distribution of multipartite partial-isometry monoids

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph with \(r\geq2\) nonempty parts \(V_1,\ldots,V_r\), and let \(\mathcal D(G)\) be the inverse monoid of all distance-preserving partial maps of its vertex set. Composition is the monoid operation, and its zero is the empty partial map. Define the element-rank polynomial
\[
Z_G(z)=\sum_{f\in\mathcal D(G),\ f^2=0}z^{|\operatorname{dom}f|}.
\]
Put \(N=\sum_{i=1}^r n_i\). For a vector \(s=(s_1,\ldots,s_r)\) with \(0\le s_i\le n_i\), set \(T(s)=\{i:s_i>0\}\). With the convention that \(\binom nk=0\) whenever \(k<0\) or \(k>n\), the entire polynomial is
\[
\boxed{Z_G(z)=1+\sum_{\substack{0\le s_i\le n_i\\T(s)\ne\varnothing}}z^{\sum_i s_i}\left(\prod_{i\in T(s)}\binom{n_i}{s_i}s_i!\right)\sum_{\theta:T(s)\hookrightarrow[r]}\ \prod_{i\in T(s)}\binom{n_{\theta(i)}-s_{\theta(i)}}{s_i}.}
\]
Here \(\theta\) runs over injections between part indices. In particular, every rank coefficient is a nonnegative integer calculated from the part sizes alone.

For the bipartite graph \(K_{a,b}\), this becomes the closed double sum
\[
\boxed{Z_{K_{a,b}}(z)=\sum_{i=0}^{a}\sum_{j=0}^{b}\binom ai\binom bj i!j!\left[\binom{a-i}{i}\binom{b-j}{j}+\binom{b-j}{i}\binom{a-i}{j}\right]z^{i+j}-1.}
\]
The maximum degree, equivalently the largest possible rank of a square-zero partial isometry, is
\[
\boxed{R(a,b)=\max\left\{\left\lfloor\frac a2\right\rfloor+\left\lfloor\frac b2\right\rfloor,\ \min(a,b)\right\}.}
\]
Every rank between \(0\) and \(R(a,b)\) occurs. When \(a+b\) is even, this maximum is strictly less than \((a+b)/2\) if and only if \(a\) and \(b\) are odd and unequal; in that case it equals \((a+b)/2-1\). Thus a genuinely graph-induced one-rank obstruction occurs exactly for these imbalanced odd bipartitions.

## Assumptions and scope
Graphs are finite, undirected, loopless, connected, and completely multipartite, with all \(n_i\ge1\) and \(r\ge2\). The distance is shortest-path graph distance: distinct vertices in the same part have distance \(2\), and vertices in different parts have distance \(1\). Partial maps preserve all pairwise distances on their domain and hence are injective. Rank is the cardinality of the domain, not the minimum number of monoid generators. The empty map has rank \(0\) and satisfies \(0^2=0\). The formula includes star graphs and complete graphs, as well as all other complete multipartite graphs. A sum over an empty set of active parts is represented solely by the leading \(1\).

## Proof
**Step 1: The square-zero condition.** For every partial injection \(f:D\to V\), the domain of \(f^2\) is \(\{x\in D:f(x)\in D\}\). Hence \(f^2=0\) if and only if \(D\cap f(D)=\varnothing\). In particular \(2|D|\le N\).

**Step 2: Classification of partial isometries.** Fix a nonempty domain \(D\) and let \(s_i=|D\cap V_i|\). All images of vertices from a single active part \(V_i\) lie in one target part \(V_{\theta(i)}\): whenever there are two domain vertices from that part, their mutual distance is \(2\), forcing the image vertices to share a part; with one vertex the target part is unique. Images of vertices from distinct active parts must lie in distinct target parts, since their mutual distances are \(1\). Thus \(\theta:T(s)\hookrightarrow[r]\) is injective. Conversely, any such part injection and a collection of arbitrary injective maps of the chosen source subsets into their respective target parts define a partial isometry, since every distance \(1\) and \(2\) is preserved. The part injection is uniquely recoverable from the resulting nonempty partial map: no overcounting occurs.

**Step 3: Counting disjoint domains and images.** For each active \(i\), choose \(D\cap V_i\) in \(\binom{n_i}{s_i}\) ways. For a fixed injective \(\theta\), the image of these \(s_i\) selected vertices must lie in target part \(V_{\theta(i)}\), avoiding all domain vertices already there; exactly \(n_{\theta(i)}-s_{\theta(i)}\) target vertices remain available. The target subset is chosen in \(\binom{n_{\theta(i)}-s_{\theta(i)}}{s_i}\) ways and assigned bijectively to the source in \(s_i!\) ways. Different active source parts use different target parts, so no further collision conditions appear. Multiplication of these independent factors, followed by summation over \(s\) and \(\theta\), proves the general formula; adding the unique empty map gives the leading constant.

**Step 4: Bipartite specialization and rank boundary.** For two parts, the nonempty part injection is either part-preserving or part-exchanging whenever both source parts are active; when only one source part is active there are still exactly two possible target parts. Summing the two patterns yields the displayed double sum. The zero-domain map is represented in each pattern, so subtract one to count it only once. In the preserving case feasibility requires \(2i\le a\), \(2j\le b\) and therefore maximum \(\lfloor a/2\rfloor+\lfloor b/2\rfloor\). In the exchanging case, feasible source counts satisfy \(i+j\le b\) and \(i+j\le a\), hence maximum \(\min(a,b)\); each bound is attained by choosing corresponding disjoint subsets. Their maximum is \(R(a,b)\). Restricting an admissible maximal-rank map to any smaller domain keeps it square-zero and isometric, proving there are no missing intermediate ranks. If \(a+b\) is odd, the preserving maximum equals \(\lfloor(a+b)/2\rfloor\); if it is even and both parts even, it equals \((a+b)/2\). The only remaining case is both parts odd, when the preserving bound is \((a+b)/2-1\), and exchanging reaches \((a+b)/2\) exactly when \(a=b\). This proves the parity criterion.

## Verification
The reproducible script `check_multipartite.py` directly enumerates disjoint-domain/image partial bijections and tests preservation of pairwise graph distances; separately it evaluates the part-injection formula and the bipartite double sum. It compared all rank coefficients for nineteen configurations, including multipartite graphs with two, three, and four parts and the bipartite cases \(K_{3,5}\) and \(K_{4,4}\). All nineteen comparisons passed, with \(6119\) square-zero isometries enumerated in total across these configurations. For example, in increasing rank order \(K_{3,5}\) has coefficients \((1,56,420,840,0)\) and \(K_{4,4}\) has \((1,56,456,1056,528)\). The proof covers arbitrary positive part sizes; enumeration is only a finite corroboration.

## Relationship to prior work
Fernandes and Paulista [1] establish that partial graph isometries form inverse submonoids of symmetric inverse monoids and analyze the star family, including presentations, Green's relations, total cardinality, and semigroup generator rank. Their star-specific analysis is not a square-zero element-rank census for arbitrary complete multipartite graphs. Their cycle study [2] concerns graph cycles and gives cardinality, presentations, and Green's relations, not the displayed multipartite part-injection distribution. The exceptional overlap \(K_{2,2}\cong C_4\) is a common small graph and is not asserted as an independent discovery. The familiar square-zero count for the complete-graph symmetric inverse monoid follows as a specialization when all parts are singletons; it is not claimed as new. The novel claim assessed here is the uniform multipartite rank polynomial and its sharp imbalanced odd-bipartition rank obstruction.

## Limitations
This classification is for graph-distance partial isometries and square-zero elements, not arbitrary graph homomorphisms or all nilpotents of higher index. The bipartite rank criterion does not purport to classify the maximum rank for every multipartite part-size vector in a simpler closed expression than the general formula. Standard counting identities for partition-preserving or partial-permutation monoids may imply some individual coefficients; exhaustive priority against all such formulations is not established. No independent audit has been performed.

## References
[1] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504 (first version 2022-03-10), later *Communications in Algebra* 51 (2023), 1028–1048, DOI: 10.1080/00927872.2022.2121404.

[2] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (first version 2022-05-04), later *Turkish Journal of Mathematics* 47 (2023), 1746–1760, DOI: 10.55730/1300-0098.3460.

[3] V. H. Fernandes, *On the monoid of partial isometries of a wheel graph*, arXiv:2307.16257 (2023); abstract consulted, full text not materially inspected.
