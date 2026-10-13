# Independent Italian domination of complete prisms
## Finding
For every integer \(n\ge3\), let
\[
P_n^{\mathrm{cl}}=K_n\square K_2
\]
be the complete prism, with clique layers
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and matching edges \(a_i b_i\).

Every independent Italian dominating function on \(P_n^{\mathrm{cl}}\) has the following form. Choose an ordered pair
\[
(i,j)\in\{1,\ldots,n\}^2,\qquad i\ne j,
\]
put
\[
f(a_i)=2,\qquad f(b_j)=2,
\]
and put \(f(v)=0\) on all remaining vertices. Conversely every such labeling is valid.

Therefore
\[
i_I(P_n^{\mathrm{cl}})=4,
\]
there are exactly
\[
n(n-1)
\]
independent Italian dominating functions, every feasible function is minimum, and the complete weight enumerator is
\[
\mathcal I_{P_n^{\mathrm{cl}}}(z)=n(n-1)z^4.
\]

## Assumptions and scope
An Italian dominating function is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every vertex \(v\) with \(f(v)=0\) satisfies
\[
\sum_{u\in N(v)}f(u)\ge2.
\]
It is independent when the positive support
\[
\{v:f(v)>0\}
\]
is an independent set. This parameter is also called independent Roman \(\{2\}\)-domination.

The theorem is stated for \(n\ge3\). The boundary \(P_2^{\mathrm{cl}}=C_4\) behaves differently: it has eight independent Italian functions, minimum weight \(2\), and two minimum functions.

## Proof
Let \(f\) be an independent Italian dominating function on \(P_n^{\mathrm{cl}}\).

Because each of \(A\) and \(B\) is a clique, independence of the positive support implies that at most one vertex of \(A\) and at most one vertex of \(B\) can be positive.

The positive support must meet both layers. Suppose, for example, that every vertex of \(B\) has label \(0\). Then \(A\) contains at most one positive vertex, say \(a_i\). Since \(n\ge3\), choose \(k\ne i\). The vertex \(b_k\) is adjacent in the other layer only to \(a_k\), and hence has no positive neighbor at all. Its neighborhood-label sum is \(0\), contradicting Italian domination. By symmetry the positive support cannot lie only in \(B\).

Thus the positive support is exactly
\[
\{a_i,b_j\}
\]
for some indices \(i,j\). These two vertices must be nonadjacent, so
\[
i\ne j,
\]
because the only edges between the layers are the matching edges \(a_kb_k\).

Since \(n\ge3\), choose an index \(k\) distinct from both \(i\) and \(j\). The zero vertex \(a_k\) is adjacent to \(a_i\) inside its clique but is not adjacent to \(b_j\), because \(k\ne j\). Hence the whole positive neighborhood of \(a_k\) consists of \(a_i\), and the Italian condition forces
\[
f(a_i)=2.
\]
Similarly, the zero vertex \(b_k\) has \(b_j\) as its only positive neighbor, so
\[
f(b_j)=2.
\]

This proves that every feasible function has exactly the stated form and weight \(4\).

Conversely, fix \(i\ne j\), label \(a_i\) and \(b_j\) by \(2\), and label every other vertex by \(0\). The positive vertices are nonadjacent. Every zero vertex in \(A\) sees \(a_i\), and every zero vertex in \(B\) sees \(b_j\), so every zero has neighborhood-label sum at least \(2\). Therefore the labeling is valid.

There are exactly \(n(n-1)\) ordered pairs \(i\ne j\). Since these are all feasible functions, all have weight \(4\), proving the number, minimum, and enumerator statements.

## Verification
The included checker constructs \(K_n\square K_2\) directly and tests the definition without using the theorem.

It exhausts every ternary labeling for
\[
2\le n\le6,
\]
a total of
\[
597{,}861
\]
labelings. For every exhaustive case \(n\ge3\), the entire feasible set—not merely the minimum layer—matches the stated ordered anti-matching construction exactly: \(6,12,20,30\) functions for \(n=3,4,5,6\), respectively, all of weight \(4\). The boundary \(n=2\) has eight feasible functions and minimum weight \(2\).

The checker also constructs and directly tests every claimed function for
\[
3\le n\le50.
\]

## Relationship to prior work
Independent Roman \(\{2\}\)-domination was introduced before the present result and is equivalent to independent Italian domination. The 2018 public preprint by Chen and Lu explicitly defines an independent Roman \(\{2\}\)-dominating function as a Roman \(\{2\}\)-function whose positive support is independent and studies algorithms on trees. A later journal version records Mathematics Subject Classification \(05C69\).

Wei and Lu subsequently use the independent-Italian terminology and give a linear-time algorithm for connected block graphs. Their full public text defines exactly the same function class and focuses on block-cutpoint dynamic programming. The complete prism \(K_n\square K_2\) with \(n\ge3\) is not a block graph, and targeted full-text searches found no Cartesian-product or prism treatment.

Targeted literature-index searches under both “independent Italian” and “independent Roman \(\{2\}\)” terminology, together with “complete prism,” “Cartesian product,” and \(K_n\square K_2\), did not locate an exact complete-prism classification. Nearby exact results for ordinary Roman \(\{2\}\)-domination, independent Roman domination, double Italian domination, and other Roman variants use different feasibility conditions and do not imply the theorem.

## Limitations
The theorem concerns \(K_n\square K_2\) for \(n\ge3\); the cycle \(C_4\) at \(n=2\) is a genuine boundary exception.

The result classifies independent Italian functions only. It does not enumerate unrestricted Italian dominating functions on complete prisms.

The earliest introducing journal article is bibliographically indexed to 2017/2018 in the inspected sources, but an exact public day for that article was not resolved. The metadata date in this package is therefore the earliest exact day-resolved public source inspected, namely the 25 April 2018 arXiv record; no day has been invented for the earlier journal record.

Finite exhaustive computation is corroborative only. The arbitrary-\(n\) classification follows from the two-clique independence argument.

Search coverage cannot exclude a differently phrased or non-indexed treatment of the same family.

## References
1. A. Rahmouni, M. Chellali, “Independent Roman \(\{2\}\)-domination in graphs,” Discrete Applied Mathematics 236 (2018), 408–414, DOI 10.1016/j.dam.2017.10.028.
2. H. Chen, C. Lu, “A Note on Roman \(\{2\}\)-domination problem in graphs,” arXiv:1804.09338v1, first public version 25 April 2018; later Discussiones Mathematicae Graph Theory 42 (2022), 641–660, DOI 10.7151/dmgt.2332.
3. P. Wu, Z. Li, Z. Shao, S. M. Sheikholeslami, “Trees with equal Roman \(\{2\}\)-domination number and independent Roman \(\{2\}\)-domination number,” RAIRO Operations Research 53 (2019), 389–400, DOI 10.1051/ro/2018116.
4. D. Wei, C. Lu, “Independent Italian Domination on Block Graphs,” arXiv:1908.00784v1, first public version 2 August 2019.
