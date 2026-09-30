# Self- and solid-locating domination in complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite sets \(V_1,\ldots,V_r\), and \(N=\sum_{i=1}^r n_i\). Put
\[
p=\bigl|\{i:n_i\ge2\}\bigr|,
\qquad
s=\bigl|\{i:n_i=1\}\bigr|.
\]
For a code \(C\subseteq V(G)\), write \(I(C;u)=N[u]\cap C\).

The solid-locating-dominating number is
\[
\gamma^{DLD}(G)=N-\max\{1,p\}.
\]
More precisely, if \(U=V(G)\setminus C\), then \(C\) is solid-locating-dominating exactly in the following cases: \(U=\varnothing\); \(|U|=1\); or \(|U|\ge2\), every part contains at most one vertex of \(U\), and every part meeting \(U\) has size at least two. Consequently, the number of minimum solid-locating-dominating codes is
\[
\begin{cases}
\displaystyle\prod_{i:n_i\ge2} n_i,&p\ge2,\\
N,&p\le1.
\end{cases}
\]
If \(e_k\) denotes the \(k\)-th elementary symmetric polynomial in the sizes \(n_i\ge2\), then the complete cardinality generating function of solid-locating-dominating codes is
\[
F_{DLD}(G;x)=x^N+Nx^{N-1}+\sum_{k=2}^{p} e_k\,x^{N-k}.
\]

The self-locating-dominating number is
\[
\gamma^{SLD}(G)=
\begin{cases}
N-1,&s=1,\\
N,&s\ne1.
\end{cases}
\]
Indeed, a self-locating-dominating code is either \(V(G)\) itself, or, when \(s=1\), the set obtained by deleting the unique vertex in the unique singleton part. Hence the minimum self-locating-dominating code is unique, and
\[
F_{SLD}(G;x)=x^N+\mathbf 1_{\{s=1\}}x^{N-1}.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. The graph \(K_{n_1,\ldots,n_r}\) has \(r\ge2\) nonempty parts, so it is connected. The definitions of self-locating-dominating and solid-locating-dominating codes are those introduced by Junnila, Laihonen, and Lehtilä. For a connected graph on at least two vertices, a solid-locating-dominating code is dominating and distinct non-codewords have identifying sets incomparable by inclusion in the directed sense required by the definition.

The generating functions above count codes by cardinality only; they are introduced here as bookkeeping devices and are not asserted to be previously standardized graph polynomials.

## Proof
Fix \(C\subseteq V(G)\), put \(C_i=C\cap V_i\), and let \(u\in V_i\setminus C\). Since a vertex of a complete multipartite graph is adjacent to every vertex outside its own part and to no other vertex of its own part,
\[
I(C;u)=C\setminus C_i.
\]
If \(u\in V_i\setminus C\) and \(v\in V_j\setminus C\) lie in distinct parts, then
\[
I(C;u)\setminus I(C;v)=C_j.
\]
If they lie in the same part, their identifying sets are equal.

For solid location-domination, two non-codewords therefore cannot lie in the same part. If there are at least two non-codewords, every part containing one of them must still contain a codeword: otherwise, for an omitted vertex \(u\in V_i\) and any other omitted vertex \(v\in V_j\), the ordered difference \(I(C;v)\setminus I(C;u)=C_i\) is empty. Thus, when \(|U|\ge2\), the omitted vertices occur one per selected non-singleton part. Conversely, any such selection works because for omitted vertices in distinct selected parts both relevant codeword sets \(C_i\) and \(C_j\) are nonempty. When \(|U|=1\), domination follows from connectedness, so every one-vertex omission works.

It follows that the largest possible complement has size \(p\) when \(p\ge2\), obtained by omitting one vertex from every non-singleton part, and has size one when \(p\le1\). This proves
\[
\gamma^{DLD}(G)=N-\max\{1,p\}.
\]
For \(p\ge2\), a minimum code is specified by choosing one omitted vertex independently from every non-singleton part, giving \(\prod_{i:n_i\ge2}n_i\) minimum codes. For \(p\le1\), every single omitted vertex gives a minimum code, giving \(N\) choices. More generally, for \(k\ge2\), a complement of size \(k\) is obtained by selecting \(k\) non-singleton parts and then one omitted vertex in each; its number is the elementary symmetric sum \(e_k\). Together with the unique full code and the \(N\) one-vertex omissions, this gives \(F_{DLD}(G;x)\).

For self location-domination, use the equivalent characterization that for every non-codeword \(u\) and every distinct vertex \(v\), one has \(I(C;u)\setminus I(C;v)\ne\varnothing\). Suppose \(u\in V_i\setminus C\). If \(C_i\ne\varnothing\), choose \(v\in C_i\). Then
\[
I(C;v)=\{v\}\cup(C\setminus C_i),
\]
so \(I(C;u)\setminus I(C;v)=\varnothing\), a contradiction. Hence any part containing a non-codeword contains no codeword. Such a part cannot contain two vertices, because two non-codewords in the same part have equal identifying sets. Therefore every omitted vertex lies in a singleton part. There cannot be two omitted singleton vertices, since then both identifying sets equal \(C\).

Thus a proper self-locating-dominating code can omit only one singleton vertex \(u\), say from \(V_i\). Then \(I(C;u)=C\). For a codeword \(v\in V_j\), where \(j\ne i\),
\[
I(C;u)\setminus I(C;v)=C_j\setminus\{v\},
\]
which is nonempty exactly when \(n_j\ge2\). Hence deleting a singleton vertex gives a self-locating-dominating code exactly when it is the unique singleton part. This proves the formula for \(\gamma^{SLD}(G)\), the uniqueness statement, and \(F_{SLD}(G;x)\).

## Verification
A standalone exhaustive checker constructs every complete multipartite isomorphism type of orders \(2\) through \(8\), tests every vertex subset directly against the definitions, and compares the entire code-size histograms with the two formulas. It covers \(58\) multipartite types and \(16{,}168\) subset/property checks and terminates with `VERIFY_OK`. The computation is corroborative; the proof above establishes the formulas for all admissible part sizes.

## Relationship to prior work
The 2018 paper *On regular and new types of codes for location-domination* introduced self-locating-dominating and solid-locating-dominating codes and obtained exact results for rook graphs together with bounds and constructions in binary Hamming spaces. The later paper *On Stronger Types of Locating-dominating Codes* developed equivalent characterizations, structural bounds, tree results, and Cartesian-product results. A 2023 follow-up studies further graph families and optimal constructions.

Targeted searches for complete multipartite graphs, the exact two parameters, their common synonyms, and stronger or equivalent formulations did not locate an existing complete-multipartite classification. The formulas and full code-structure descriptions here are therefore stated as best-of-knowledge new results, not as claims of independently certified novelty.

## Limitations
The result is restricted to connected complete multipartite graphs. It does not classify the corresponding codes in arbitrary cographs, joins, or multipartite graphs with deleted cross-edges. The originality assessment is best-of-knowledge and may miss inaccessible or differently indexed literature. The finite exhaustive check is not an independent audit and does not replace the general proof. No formal proof-assistant verification or expert attestation has been performed.

## References
1. V. Junnila, T. Laihonen, and T. Lehtilä, *On regular and new types of codes for location-domination*, `doi:10.1016/j.dam.2018.03.050`. The article was available online on 13 April 2018.
2. V. Junnila, T. Laihonen, T. Lehtilä, and M. L. Puertas, *On Stronger Types of Locating-dominating Codes*, `doi:10.23638/DMTCS-21-1-1`, also `arXiv:1808.06891`.
3. *New Optimal Results on Codes for Location in Graphs*, `arXiv:2306.07862`.
