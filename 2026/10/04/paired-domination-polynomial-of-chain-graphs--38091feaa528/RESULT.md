# Paired-domination polynomial of chain graphs
## Finding
Let \(G\) be a finite connected chain graph with canonical nonempty twin classes \(A_1,\ldots,A_p\) and \(B_1,\ldots,B_p\), ordered so that a vertex of \(A_i\) is adjacent to a vertex of \(B_j\) exactly when \(j\le i\). Put \(\alpha_i=|A_i|\) and \(\beta_i=|B_i|\). For \(S\subseteq V(G)\), write \(a_i=|S\cap A_i|\) and \(b_i=|S\cap B_i|\).

Then \(S\) is paired-dominating if and only if
\[
\sum_{i=1}^p a_i=\sum_{i=1}^p b_i=q\ge1,
\qquad a_p\ge1,
\qquad b_1\ge1,
\]
and
\[
\sum_{i=1}^k a_i\le \sum_{i=1}^k b_i
\quad\text{for every }1\le k\le p.
\]
Hence
\[
D_{pr}(G;x)=
\sum_{\substack{0\le a_i\le\alpha_i,\ 0\le b_i\le\beta_i\\
 a_p\ge1,\ b_1\ge1,\ \sum_i a_i=\sum_i b_i\\
 \sum_{i\le k}a_i\le\sum_{i\le k}b_i\ (1\le k\le p)}}
\left(\prod_{i=1}^p\binom{\alpha_i}{a_i}\binom{\beta_i}{b_i}\right)
x^{2\sum_i a_i}.
\]
In particular,
\[
\gamma_{pr}(G)=2,
\qquad d_{pr}(G,2)=\alpha_p\beta_1.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The graph \(G\) is connected and bipartite with the displayed canonical chain ordering; every \(\alpha_i\) and \(\beta_i\) is positive. A paired-dominating set is a dominating set whose induced subgraph admits a perfect matching. The polynomial \(D_{pr}(G;x)\) counts paired-dominating vertex sets by cardinality.

The theorem concerns all paired-dominating sets, not only minimum or inclusion-minimal ones. The case \(p=1\) is included and is the complete bipartite specialization.

## Proof
Let \(S_A=S\cap(A_1\cup\cdots\cup A_p)\) and \(S_B=S\cap(B_1\cup\cdots\cup B_p)\).

Suppose first that \(S\) is paired-dominating. A perfect matching in the bipartite graph \(G[S]\) matches every vertex of \(S_A\) to one of \(S_B\), so \(|S_A|=|S_B|=q\ge1\). For every \(k\), every selected vertex in \(A_1\cup\cdots\cup A_k\) can only be matched to a selected vertex in \(B_1\cup\cdots\cup B_k\). Therefore
\[
\sum_{i=1}^k a_i\le\sum_{i=1}^k b_i.
\]
If \(b_1=0\), then no selected vertex of \(A_1\) can be matched. Hence \(a_1=0\); but then every vertex of the nonempty class \(A_1\) lies outside \(S\) and has no neighbor in \(S\), contradicting domination. Thus \(b_1\ge1\). By symmetry at the other end of the chain, \(a_p\ge1\): if \(a_p=0\), then matching forces \(b_p=0\), leaving the nonempty class \(B_p\) undominated.

Conversely, assume the displayed conditions. A selected vertex from \(B_1\) is adjacent to every vertex in every \(A_i\), and a selected vertex from \(A_p\) is adjacent to every vertex in every \(B_j\). Thus \(S\) dominates \(G\).

It remains to prove that \(G[S]\) has a perfect matching. Consider any set \(X\subseteq S_A\). If \(X\ne\varnothing\), let \(k\) be the largest index of an \(A_k\)-class met by \(X\). Since the neighborhoods are nested, the neighborhood of \(X\) inside \(S_B\) is exactly the selected vertices in \(B_1\cup\cdots\cup B_k\). Therefore
\[
|X|\le\sum_{i=1}^k a_i\le\sum_{i=1}^k b_i=|N_{G[S]}(X)|.
\]
Hall's condition holds for every \(X\subseteq S_A\). Since \(|S_A|=|S_B|\), Hall's theorem gives a perfect matching of \(G[S]\). This proves the characterization.

For fixed count vectors, the number of vertex sets realizing them is \(\prod_i\binom{\alpha_i}{a_i}\binom{\beta_i}{b_i}\), and every feasible vector has size \(2\sum_i a_i\). Summing gives the stated polynomial.

For a computational form, set \(F_0(0;x)=1\) and \(F_0(d;x)=0\) for \(d>0\). For \(1\le i\le p\), let
\[
F_i(d';x)=
\sum_{\substack{d\ge0,\ 0\le a\le\alpha_i,\ 0\le b\le\beta_i\\ d'=d+b-a\ge0}}
\epsilon_i(a,b)F_{i-1}(d;x)\binom{\alpha_i}{a}\binom{\beta_i}{b}x^{a+b},
\]
where \(\epsilon_i(a,b)=0\) when \(i=1\) and \(b=0\), or when \(i=p\) and \(a=0\), and \(\epsilon_i(a,b)=1\) otherwise. Then \(D_{pr}(G;x)=F_p(0;x)\). Finally, choosing one vertex from \(A_p\) and one from \(B_1\) always gives a paired-dominating edge, proving \(\gamma_{pr}(G)=2\) and the count \(\alpha_p\beta_1\).

## Verification
The included verifier constructs every canonical chain-graph profile of order at most \(10\) with at most four twin-class pairs. It compares, for every vertex subset, the definition of paired domination against the characterization above, and independently compares the resulting coefficient table with the dynamic program. Running `python3 artifacts/verify.py` prints `VERIFY_OK graph_types=510 subset_checks=348500 polynomial_profiles=1681 max_order=10`.

This finite computation corroborates the theorem but is not used as its proof.

## Relationship to prior work
Haynes and Slater introduced paired domination and its minimum parameter in 1998. Puttaswamy, Alwardi, and Nayaka later introduced the paired-domination polynomial and reported computations for some standard graph families. Pradhan and Panda gave a minimum paired-domination algorithm on strongly orderable graphs, while Henning and Pradhan later treated the upper paired-domination problem and explicitly included chain graphs among their polynomial-time classes.

Those results concern the minimum parameter, the upper parameter over inclusion-minimal paired-dominating sets, or unspecified standard-family polynomial examples. The present statement instead characterizes every paired-dominating set of an arbitrary chain graph and converts the characterization into the full cardinality enumerator. The complete bipartite case is only a specialization of the theorem and is not an originality claim by itself.

## Limitations
The literature search did not establish bibliographic uniqueness. In particular, the accessible 2016 paired-domination-polynomial record is only a one-page abstract and does not enumerate the standard graph families treated in the underlying presentation, and the closest chain-graph upper-paired-domination article was accessible only through its abstract and bibliographic records. These access limits are retained as residual originality risks. The theorem itself is independent of those access limitations because its proof is self-contained.

The verifier is exhaustive only over the stated finite test range; the infinite theorem is justified by the Hall-theorem argument above, not by enumeration.

## References
1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
2. Puttaswamy, A. Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” conference abstract, 2016, https://publications.waset.org/abstracts/52964.pdf.
3. D. Pradhan and B. S. Panda, “Computing a minimum paired-dominating set in strongly orderable graphs,” *Discrete Applied Mathematics* 253 (2019), 37–50. DOI: 10.1016/j.dam.2018.08.022.
4. M. A. Henning and D. Pradhan, “Algorithmic aspects of upper paired-domination in graphs,” *Theoretical Computer Science* 804 (2020), 98–114. DOI: 10.1016/j.tcs.2019.10.045.
