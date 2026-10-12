# Paired-domination polynomial of generalized windmill graphs
## Finding
For integers \(k\ge2\) and \(m\ge2\), let
\[
W_{k,m}=K_1\vee kK_m
\]
have center \(c\) and pairwise disjoint peripheral cliques \(B_1,\ldots,B_k\), each of size \(m\). For \(S\subseteq V(W_{k,m})\), write \(s_i=|S\cap B_i|\). A set \(S\) is paired-dominating if and only if exactly one of these two conditions holds:

1. \(c\in S\), exactly one of \(s_1,\ldots,s_k\) is odd, and every other \(s_i\) is even.
2. \(c\notin S\), and every \(s_i\) is positive and even.

Define
\[
E_m(x)=\frac{(1+x)^m+(1-x)^m}{2},\qquad
O_m(x)=\frac{(1+x)^m-(1-x)^m}{2}.
\]
Then the paired-domination polynomial, whose coefficient of \(x^r\) counts paired-dominating sets of cardinality \(r\), is
\[
D_{\mathrm{pr}}(W_{k,m};x)=kx\,O_m(x)E_m(x)^{k-1}+(E_m(x)-1)^k.
\]
In particular,
\[
\gamma_{\mathrm{pr}}(W_{k,m})=2,
\]
there are exactly \(km\) minimum paired-dominating sets, and the total number of paired-dominating sets is
\[
k2^{k(m-1)}+(2^{m-1}-1)^k.
\]
The scalar equality \(\gamma_{\mathrm{pr}}(W_{k,m})=2\) is known; the new statement retained here is the complete all-cardinality classification and enumerator.

## Assumptions and scope
Graphs are finite, simple, and undirected. A paired-dominating set is a dominating set whose induced subgraph has a perfect matching. The parameters satisfy \(k\ge2\) and \(m\ge2\). The peripheral cliques have no edges between distinct blades, while the center is adjacent to every peripheral vertex.

## Proof
First suppose \(c\notin S\). If some blade \(B_i\) misses \(S\), then every vertex of \(B_i\) has no neighbor in \(S\), because its only neighbors lie in \(B_i\) or are the absent center. Hence domination forces \(s_i\ge1\) for every \(i\). The induced graph \(W_{k,m}[S]\) is then the disjoint union of the cliques \(K_{s_i}\). Such a disjoint union has a perfect matching exactly when every component has even order. Therefore \(S\) is paired-dominating exactly when every \(s_i\) is positive and even.

Now suppose \(c\in S\). Domination is automatic. In any perfect matching of \(W_{k,m}[S]\), the center is matched to one selected vertex in a unique blade, say \(B_j\). After deleting that matched edge, the remaining selected vertices induce pairwise disjoint cliques of orders \(s_j-1\) and \(s_i\) for \(i\ne j\). They admit a perfect matching exactly when \(s_j-1\) and all \(s_i\) for \(i\ne j\) are even. Thus exactly one blade has odd selected cardinality. Conversely, if exactly one blade has odd selected cardinality, match the center to any selected vertex in that blade and match the remaining even cliques internally. This proves the classification.

The polynomial follows by ordinary subset enumeration. The polynomial \(E_m(x)\) counts even subsets of one blade, while \(O_m(x)\) counts odd subsets. With the center selected, choose the unique odd blade in \(k\) ways, contributing \(kxO_m(x)E_m(x)^{k-1}\). With the center absent, each blade contributes a nonempty even subset, contributing \((E_m(x)-1)^k\). The two cases are disjoint and exhaustive.

The coefficient of \(x^2\) comes only from a center-plus-one-peripheral-vertex set, so there are \(km\) minimum sets. Evaluating the polynomial at \(x=1\), where \(E_m(1)=O_m(1)=2^{m-1}\), gives the stated total count.

## Verification
A standalone exhaustive checker independently constructs each graph, tests domination, finds perfect matchings by recursive search, and compares every subset with the parity criterion and with the polynomial coefficients. It checks eight parameter pairs, including boundary instances with \(m=1\) as an additional out-of-scope stress test, and all in-scope tested pairs agree exactly. The replay output is stored with the checker.

## Relationship to prior work
Haynes and Slater introduced paired domination. A later full-text treatment of the French windmill \(W_{p,q}\), which is the same graph as \(K_1\vee qK_p\), proves the scalar equality \(\gamma_{\mathrm{pr}}(W_{p,q})=2\). That result does not classify paired-dominating sets of larger cardinalities and does not give their generating polynomial. The paired-domination polynomial was introduced as an all-cardinality counting invariant in 2016. The exact formula above supplies that invariant for the generalized windmill family.

The closest indexed comparisons found for the same invariant concern complete multipartite graphs and chain graphs. Neither family contains \(W_{k,m}\) for \(k,m\ge2\): generalized windmills contain triangles, so they are not chain graphs, and their pattern of adjacency within blades together with nonadjacency across blades is incompatible with complete multipartite nonadjacency classes. Thus those formulas do not imply the stated parity classification.

## Limitations
The result is for ordinary paired domination on \(K_1\vee kK_m\); it does not address induced-paired domination, weighted variants, or windmill constructions with nonclique blades. The 2023 journal article on windmill paired-domination numbers was not itself available as open full text in the inspected sources; however, the corresponding 2023 dissertation by the same first author was available in full and its windmill section was inspected directly. That section defines the same French windmill family and proves only the scalar paired-domination number. No claim of independence or external validation is made.

## References
1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” Networks 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
2. W. Ulatowski, “All graphs with paired-domination number two less than their order,” Opuscula Mathematica 33 (2013), 763–783. DOI: 10.7494/OpMath.2013.33.4.763. MSC: 05C69.
3. P. Eakawinrujee and N. Trakultraipruk, “Total and paired domination numbers of windmill graphs,” Asian-European Journal of Mathematics 16 (2023). DOI: 10.1142/S1793557123501231.
4. P. Eakawinrujee, “Total and Paired Domination Numbers and γ-Total and γ-Paired Dominating Graphs of Some Graphs,” doctoral dissertation, Thammasat University, 2023. Windmill section 3.5.1.
5. Puttaswamy, A. Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” International Journal of Physical and Mathematical Sciences 10(9) (2016), conference abstract dated September 26–27, 2016.
