# Complete length-four palindrome spectrum of order-three de Bruijn cycles

## Finding
For every integer \(q\ge2\), let \(\mathcal B_{q,3}\) be the set of cyclic words of length \(q^3\) over an alphabet \(A\) of size \(q\), with each word of length \(3\) appearing exactly once as a cyclic factor. For \(C\in\mathcal B_{q,3}\), let \(P(C)\) count the cyclic starting positions of palindromic factors of length \(4\). Every such factor has the form \(abba\), and its first three symbols occur just once, so this also counts *distinct* palindromic length-four factors. Then
\[
\{P(C):C\in\mathcal B_{q,3}\}=\{0,1,\ldots,q(q-2)\}.
\]

The stronger transition-prescription statement below realizes every permitted local permutation independently, not merely every integer in the spectrum.

## Assumptions and scope
Fix a finite alphabet \(A\) of size \(q\ge2\). A cyclic word is indexed modulo its length; factor occurrences may wrap around the end. Use the directed order-two de Bruijn graph with vertex set \(A^2\) and, for each triple \(abc\), one edge \(ab\to bc\) labeled \(abc\). A cyclic de Bruijn sequence of order \(3\) is precisely a cyclic Euler tour of this graph, read via the first symbol of each successive edge. Length-four factors occur at consecutive edges \(abc\), \(bcd\).

At a diagonal vertex \(bb\), a tour pairs each incoming edge \(abb\) to its immediately following outgoing edge \(bbc\). Denote this bijection by \(\sigma_b:A\to A\), where \(c=\sigma_b(a)\). Such a transition pairing has \(\sigma_b(b)\ne b\) because the loop \(bbb\) cannot form an isolated length-one tour when \(q\ge2\).

## Proof
**Palindromes and the upper bound.** The pair \(abb\), \(bba\) is present consecutively exactly when \(\sigma_b(a)=a\), and every palindrome \(abba\) appears through exactly that pair. Thus
\[
P(C)=\sum_{b\in A}|\operatorname{Fix}(\sigma_b)|.
\]
Since \(\sigma_b(b)\ne b\), a permutation \(\sigma_b\) must move at least two letters: a permutation cannot move exactly one letter. Hence \(|\operatorname{Fix}(\sigma_b)|\le q-2\), giving \(P(C)\le q(q-2)\).

**Independent realization lemma.** Conversely choose, for each \(b\in A\), an arbitrary permutation \(\sigma_b\) with \(\sigma_b(b)\ne b\). We construct one cyclic Euler tour realizing all these transitions simultaneously. Let \(e_b=\sigma_b^{-1}(b)\), so \(e_b\ne b\). Construct a macro-digraph \(H\) whose vertices are the ordered pairs \(ab\) with \(a\ne b\). Its macroedges are:

(1) For every \(a\ne b\) and \(c\ne b\), one edge \(ab\to bc\) expanded as the original single edge labeled \(abc\).

(2) For every \(a\ne b\), one macroedge starting at \(ab\). If \(a=e_b\), it expands as the three original edges
\[
(abb,\ bbb,\ bb\sigma_b(b));
\]
otherwise it expands as the two edges
\[
(abb,\ bb\sigma_b(a)).
\]
Its terminal vertex is \(b\sigma_b(b)\) in the first case and \(b\sigma_b(a)\) otherwise. The terminal pair is off-diagonal because \(\sigma_b(a)\ne b\) for \(a\ne e_b\) and \(\sigma_b(b)\ne b\). Here parenthesized strings denote consecutive edge labels, not products.

Every original triple appears in exactly one expanded macroedge: (1) covers triples \(abc\) with \(a\ne b\) and \(c\ne b\); (2) covers all \(abb\) with \(a\ne b\), all \(bbc\) with \(c\ne b\), and each loop \(bbb\) exactly once. The transitions at each diagonal vertex are precisely those specified by \(\sigma_b\).

Each vertex \(ab\) with \(a\ne b\) has exactly \(q\) outgoing macroedges: \(q-1\) of type (1) and one of type (2). It also has exactly \(q\) incoming macroedges: \(q-1\) of type (1), and one of type (2) whose terminal letter is \(b\) and whose middle letter is \(a\). Uniqueness follows from bijectivity of \(\sigma_a\). Thus \(H\) is balanced.

Its type-(1) subgraph contains all transitions \(ab\to bc\) with \(a\ne b\), \(b\ne c\). This is the directed line graph of the complete loopless directed graph on \(A\), hence strongly connected for \(q\ge2\). Therefore \(H\) has an Euler tour. Expanding all its macroedges in the Euler tour yields one Euler tour of the original de Bruijn graph, respecting every independently prescribed \(\sigma_b\). This proves the realization lemma without requiring a disconnected local transition system to be Eulerian.

**Every integer occurs.** For any \(b\in A\) and any \(f\in\{0,\ldots,q-2\}\), choose \(f\) letters from \(A\setminus\{b\}\) to fix, and cyclically permute all remaining \(q-f\ge2\) letters. The resulting permutation moves \(b\) and has exactly \(f\) fixed points. As the \(q\) choices at diagonal vertices are independent by the lemma, their fixed-point counts can sum to any integer from \(0\) to \(q(q-2)\). The general upper bound excludes every other integer, completing the proof. \(\square\)

## Verification
The self-contained program `verify.py` constructs the expanded macrograph, executes Hierholzer's algorithm, checks that each constructed tour uses all \(q^3\) triples exactly once, checks cyclic overlaps, and independently counts palindromic length-four windows of the *resulting cyclic word*. It realizes all attainable values for \(2\le q\le8\) and all \(64\) permitted local-permutation tuples for \(q=3\). It prints `ALL_CONSTRUCTED_DEBRUIJN_PALINDROME_SPECTRA_PASSED` on success.

A separate C++ exhaustive search `check_ternary.cpp` enumerates all \(373248\) cyclic order-three ternary de Bruijn tours with the fixed starting edge `000`, obtaining counts \(55296,165888,124416,27648\) at palindrome counts \(0,1,2,3\), respectively. These finite checks do not establish the infinite-alphabet theorem; the macrograph argument does.

## Relationship to prior work
De Bruijn's classical Euler-tour representation is foundational rather than new here. Nellore and Ward's work [1] addresses frequency-constrained and arbitrary-length analogues; Chee and coauthors [2] study locally constrained de Bruijn codes. Neither inspected paper establishes the precise length-four-palindrome spectrum of order-three cyclic de Bruijn words or the simultaneous diagonal transition-prescription lemma. Anisiu, Anisiu and Kása [3] discuss palindromes and a construction associated with de Bruijn words; their short palindrome examples are not this factor-count spectrum. The transition-permutation formulation makes clear how the claim differs from counting de Bruijn cycles, constructing strings containing palindromes, and reversal-identification of windows.

## Limitations
This result is for cyclic order-three de Bruijn words and palindromic windows of length exactly four, with arbitrary finite alphabet size at least two. It does not classify cycles with each palindrome count, higher-order de Bruijn cycles, or longer palindromic windows. No assertion of an exhaustive literature search or independent audit is made; equivalent uncatalogued results remain possible.

## References
[1] S. Nellore and R. Ward, *Arbitrary-Length Analogs to de Bruijn Sequences*, arXiv:2108.07759v1 (public 2021-08-17), later CPM 2022. https://arxiv.org/abs/2108.07759

[2] Y. M. Chee et al., *Locally-Constrained de Bruijn Codes: Properties, Enumeration, Code Constructions, and Applications*, IEEE Transactions on Information Theory 67 (2021). https://doi.org/10.1109/TIT.2021.3112300

[3] M.-C. Anisiu, V. Anisiu and Z. Kása, *Properties of palindromes in finite words*, Pure Mathematics and Applications 17 (2006), 183–195.
