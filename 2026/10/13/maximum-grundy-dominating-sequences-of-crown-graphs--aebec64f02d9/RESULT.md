# Maximum Grundy dominating sequences of crown graphs
## Finding
For every integer \(n\ge5\), let
\[
\operatorname{Cr}_n=K_{n,n}-M_n
\]
be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted matching \(M_n=\{a_i b_i:1\le i\le n\}\). Then
\[
\gamma_{\mathrm{gr}}(\operatorname{Cr}_n)=n.
\]
More strongly, every maximum Grundy dominating sequence is, after possibly exchanging \(A\) and \(B\), exactly one of the following four forms.

1. An arbitrary ordering of all vertices of \(A\).
2. Choose distinct \(j,s\). Either order all vertices of \(A\setminus\{a_s\}\) arbitrarily and then append \(b_j\), or order all vertices of \(A\setminus\{a_j,a_s\}\) arbitrarily and then append \(b_j,a_j\).
3. Choose distinct \(j,s,k\) with \(k\notin\{j,s\}\). Order \(A\setminus\{a_j,a_s\}\) arbitrarily and then append \(b_j,b_k\).
4. Choose distinct \(j,k\). Order \(A\setminus\{a_j,a_k\}\) arbitrarily and then append \(b_j,b_k\), with the two terminal vertices allowed in either order.

The underlying maximum sets are therefore exactly the sets with side-size/intersection profiles, up to exchanging the two sides,
\[
(n,0,0),\qquad (n-1,1,1),\qquad (n-2,2,1),\qquad (n-2,2,0),
\]
where the third coordinate is the number of matched indices represented on both sides. Hence the number of underlying maximum sets is
\[
2+n(n-1)(2n-1),
\]
and the number of ordered maximum sequences is
\[
4n\,n!.
\]

## Assumptions and scope
A closed-neighborhood sequence \((v_1,\ldots,v_t)\) is legal when each \(v_i\) has a vertex in \(N[v_i]\) not contained in \(\bigcup_{h<i}N[v_h]\). A legal sequence is dominating when its closed neighborhoods cover the graph. A longest such sequence is a Grundy dominating sequence, and its length is \(\gamma_{\mathrm{gr}}\).

The theorem is stated for \(n\ge5\). The smaller crowns have additional exceptional maximum-set types: they are intentionally outside the claim rather than folded into the uniform classification.

## Proof
Write a legal sequence from left to right. If it uses only one bipartition side, its length is at most \(n\), and every ordering of one full side is legal: the first selected vertex dominates itself and all but one vertex of the opposite side, the second selected vertex covers that remaining opposite vertex, and every later vertex footprints itself. Thus sequences of length \(n\) exist.

It remains to bound and classify mixed-side sequences. Suppose, after exchanging the two sides if necessary, that the sequence begins with \(t\ge1\) vertices from \(A\) before its first vertex \(b_j\in B\). If \(t=1\), write the first vertex as \(a_i\). When \(i=j\), the pair \(a_i,b_i\) already dominates the whole graph. When \(i\ne j\), after \(a_i,b_j\) the only undominated vertices are \(a_j\) and \(b_i\); hence at most two further legal moves are possible. Therefore every such sequence has length at most \(4<n\).

Now assume \(t\ge2\). Two selected vertices of \(A\) already dominate every vertex of \(B\). Consequently the first vertex \(b_j\) can be legal only by footprinting an unselected vertex of \(A\setminus\{a_j\}\). Once \(b_j\) is selected, every vertex of \(A\setminus\{a_j\}\) is dominated: previously selected vertices are dominated already, and every previously unselected one other than \(a_j\) lies in \(N[b_j]\). Thus the only possible later vertex from \(A\) is \(a_j\). Also, after two vertices of each side have appeared, the graph is fully dominated, so at most one additional vertex of \(B\) can follow \(b_j\), and if it does it is terminal.

These observations imply that every mixed legal sequence has at most \(n\) vertices. Since a full-side sequence has length \(n\), the Grundy domination number is exactly \(n\).

Equality forces the preceding restrictions to be tight. If exactly one vertex of \(B\) occurs, then the sequence contains \(n-1\) vertices of \(A\). Let the omitted vertex be \(a_s\). Legality of \(b_j\) forces \(s\ne j\). Either \(b_j\) is last, giving an arbitrary ordering of \(A\setminus\{a_s\}\) followed by \(b_j\), or exactly \(n-2\) vertices of \(A\) precede \(b_j\); then the only legal final vertex from \(A\) is \(a_j\), giving the second order in type 2.

If exactly two vertices of \(B\) occur, then the sequence contains exactly \(n-2\) vertices of \(A\), all of which must precede the first \(B\)-vertex. If that first vertex is \(b_j\), the only vertex that can remain undominated after it is \(a_j\), so \(a_j\) must be one of the two omitted \(A\)-vertices and the second \(B\)-vertex must have an index different from \(j\). If the second \(B\)-index is represented in the chosen \(A\)-set, this is type 3 and the order of the two terminal \(B\)-vertices is forced. If both terminal \(B\)-indices are exactly the two omitted \(A\)-indices, this is type 4 and either terminal order is legal. This exhausts the equality cases.

For the set count, on each choice of heavy side there are \(1\) sets of type 1, \(n(n-1)\) of type 2, \(n(n-1)(n-2)\) of type 3, and \(\binom n2\) of type 4. Doubling and simplifying gives
\[
2+n(n-1)(2n-1).
\]
For ordered sequences, the four types on one heavy side contribute respectively
\[
n!,\qquad n(n-1)\bigl((n-1)!+(n-2)!\bigr),\qquad n(n-1)(n-2)(n-2)!,\qquad 2\binom n2(n-2)!.
\]
After doubling for the two heavy-side choices, the sum is \(4n\,n!\).

## Verification
The standalone verifier `verify.py` constructs \(\operatorname{Cr}_n\) directly, computes legality from closed neighborhoods, and for every \(n\in\{5,6,7\}\) checks every \(n\)-vertex candidate set. For each candidate it uses dynamic programming over internal orderings to count exactly the legal dominating orders, compares that count with the four structural types above, and independently confirms both aggregate formulas. It also checks by global dynamic programming that the maximum legal-sequence length is \(n\) for the tested values.

A successful replay prints
`VERIFY_OK n_range=5..7 maximum_sets=1062 maximum_sequences=160800 max_order=14`.
The computation is a finite stress test; the all-\(n\) theorem is supplied by the symbolic proof above.

## Relationship to prior work
Brešar, Gologranc, Milanič, Rall, and Rizzi introduced the Grundy domination number and its closed-neighborhood sequence formulation. A public institutional record for that work is dated 2014-01-01, and the published article is DOI:10.1016/j.disc.2014.07.016.

Bacsó, Brešar, Kuenzel, and Rall study the broader equality class \(\alpha(G)=\gamma_{\mathrm{gr}}(G)\) in arXiv:2212.01335v2. Their full text gives the closed-neighborhood definition, lists primary MSC 05C69, and characterizes the equality class through properties of legal sequences. It does not state the crown-graph maximum-set classification or the two counting formulas above; exact full-text searches found no occurrence of “crown” or “perfect matching”. Thus the scalar equality is consistent with their broader theory, while the retained contribution is the exact extremal structure and enumeration.

Brešar and Dravec study uniqueness and iso-uniqueness of Grundy dominating sets in DOI:10.1007/s40314-026-03835-w. Their theorem that complete graphs are the only connected iso-unique Grundy domination graphs concerns orbit-uniqueness, not the number or structure of maximum sequences in crown graphs; the full text contains no occurrence of “crown”.

A published published-finding corpus finding gives a complete classification and enumeration of maximum Grundy dominating sequences for complete multipartite graphs. Crown graphs are not complete multipartite when \(n\ge3\): each vertex is missing exactly its matched cross-edge, so that theorem does not specialize to the present family. The present counts also differ qualitatively because maximum sets may use both sides in the matching-sensitive profiles above.

## Limitations
The theorem is specific to ordinary closed-neighborhood Grundy domination on crown graphs and to \(n\ge5\). It does not give the exceptional small-order classifications, nor does it assert analogous formulas for Grundy total, Z-Grundy, L-Grundy, or hop variants. The literature comparison found no statement implying the exact four-type classification or the formulas \(2+n(n-1)(2n-1)\) and \(4n\,n!\), but a differently indexed or differently phrased source could still exist.

## References
1. B. Brešar, T. Gologranc, M. Milanič, D. F. Rall, and R. Rizzi, “Dominating sequences in graphs,” Discrete Mathematics 336 (2014), 22–36. DOI:10.1016/j.disc.2014.07.016; public institutional record hdl:11562/933301.
2. G. Bacsó, B. Brešar, K. Kuenzel, and D. F. Rall, “Graphs with equal Grundy domination and independence number,” arXiv:2212.01335v2; later Discrete Optimization 48 (2023), 100777.
3. B. Brešar and T. Dravec, “Graphs with unique Grundy dominating sets,” Computational and Applied Mathematics 45 (2026), Article 444. DOI:10.1007/s40314-026-03835-w.
