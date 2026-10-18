# Exact strong odd chromatic numbers of fan graphs and clique–path joins

## Finding

For every pair of integers \(r,n\ge1\), let \(J_{r,n}=K_r\vee P_n\) be the graph formed by joining every vertex of an \(r\)-vertex clique to every vertex of a path with \(n\) vertices. Its strong odd chromatic number is

\[
\chi_{\mathrm{so}}(J_{r,n})=r+f(n),\qquad
f(n)=\begin{cases}
n,&1\le n\le6,\\
3,&n\ge7,\quad n\equiv3\pmod6,\\
4,&n\ge7,\quad n\equiv0,2,4\pmod6,\\
5,&n\ge7,\quad n\equiv1,5\pmod6.
\end{cases}
\]

The fan graph is the case \(r=1\). In particular, the known seven-color example \(K_1\vee P_6\) is followed by the strictly smaller values \(6,5,4\) at path orders \(7,8,9\); afterward the values follow a six-periodic pattern.

## Assumptions and scope

All graphs are finite, undirected, simple and nonempty. The join \(G\vee H\) takes disjoint copies of \(G\) and \(H\) and adds every edge between them. A strong odd coloring of a graph is a proper vertex coloring such that, for every vertex and every color appearing in its open neighborhood, the multiplicity of that color in that neighborhood is odd. The minimum number of used colors is \(\chi_{\mathrm{so}}\). The path vertices are in natural order \(v_1,\ldots,v_n\); the clique vertices are \(u_1,\ldots,u_r\).

A path color word is *admissible* if its symbols at positions differing by one or two are distinct and every symbol occurring in the word occurs an odd number of times. The theorem also establishes a characterization: strong odd colorings of \(J_{r,n}\) correspond precisely to \(r\) mutually distinct clique-only colors together with admissible path words using colors absent from the clique.

## Proof

**Reduction to odd classes of a square-path coloring.** Every clique vertex is adjacent to every other clique vertex and every path vertex, so the clique colors are mutually distinct and cannot appear on the path. Fix a clique vertex \(u\). Its open neighborhood contains every path vertex and every other clique vertex. Therefore any path color that appears has odd total multiplicity on the path. Conversely, at an internal path vertex \(v_i\), the colors on its two path neighbors must be different: if they were equal, that color would appear exactly twice among the neighbors of \(v_i\), since all clique colors are distinct and path-exclusive. Properness likewise makes consecutive path colors distinct. Thus the path word must have unequal symbols at distance one or two. At an endpoint there is only one path neighbor. All clique colors occur exactly once in the neighborhood of every path vertex, and each path color occurring in the neighborhood of a clique vertex occurs an odd number of times by assumption. These observations also prove the converse. Hence the required value equals \(r\) plus the minimum number \(f(n)\) of letters in an admissible path word.

**Lower bounds.** In an admissible word, equal letters are separated by at least three positions. Hence any letter repeated three times occupies positions at least as far apart as the first, fourth, and seventh positions. Every used letter has odd multiplicity; for \(1\le n\le6\), it must consequently be used just once, so \(f(n)=n\). For \(n\ge7\), the first three positions require three distinct letters. Since all nonempty letter classes have odd cardinality, the number \(k\) of used letters has the same parity as \(n\). If \(k=3\), each following letter is forced to equal the letter three positions earlier, yielding the repeated word `012012...`. Such a word has all three class sizes odd exactly when \(n\equiv3\pmod6\). Therefore \(k\ge3\), with equality possible only in that residue class; if \(n\) is even then \(k\ge4\), and if \(n\) is odd but not congruent to three modulo six then \(k\ge5\).

**Matching explicit upper constructions.** Regard digits as distinct color names. The following seed words are admissible (the column \(s\) gives the seed length):

| \(s\) | Seed word |
|---:|:---|
| \(3\) | `012` |
| \(4\) | `0123` |
| \(5\) | `01234` |
| \(7\) | `0120340` |
| \(8\) | `01201301` |
| \(12\) | `012013023123` |

For \(n\ge7\), select the seed length \(s=12,7,8,3,4,5\), respectively, when \(n\equiv0,1,2,3,4,5\pmod6\), and prepend \((n-s)/6\) copies of the six-letter block `012012`. The selected seed always begins `012`; the block ends `012`, so two-adjacent-position inequalities hold across every join. Prepending the block adds exactly two occurrences to each of the colors `0`, `1`, and `2`, preserving the oddness of every used class. All seed words themselves have every used class of odd size, and they use exactly \(4,5,4,3,4,5\) colors in the displayed residue-class order. The lower bounds are therefore attained. For \(1\le n\le6\), the all-distinct length-\(n\) word attains \(f(n)=n\). Adding the \(r\) distinct clique colors completes the proof. \(\square\)

## Verification

Run `python verification.py`, requiring only Python's standard library. Its first independent check constructs the displayed words and tests both distance-two inequalities and odd symbol multiplicities for each \(1\le n\le200\). A separate parity-mask dynamic program determines the exact feasible palette sizes for each \(1\le n\le80\). Finally, a direct graph-neighborhood exhaustive search over unlabelled color partitions of \(K_1\vee P_n\) for \(1\le n\le12\) checks properness and all local odd-neighborhood constraints without using the word-reduction lemma. All checks matched the formula. None of these finite checks substitutes for the preceding all-integers proof.

## Relationship to prior work

Kwon and Park introduced strong odd coloring and studied sparse graph bounds [1]. Caro, Petruševski, Škrekovski, and Tuza proved \(\chi_{\mathrm{so}}(K_1\vee P_6)=7\) in Proposition 3.2 of [2], using this fan as an outerplanar lower-bound example; that individual value is not new. Their broader outerplanar bounds do not specify the other fan orders. Goetze and collaborators improved bounds on entire minor-closed classes [3], and Pilipczuk established a bounded-expansion theorem [4]; neither provides this exact infinite-family profile. Manattu, Vinay, and Lakshmanan [5] studied joins involving **cycles** and the exact wheel parameter, with a related odd-class / distance-two mechanism; their cyclic boundary conditions and resulting wheel numbers do not imply the path-join formula. Pradhan, Sharma, and Verma [6] treat complexity and an algorithm for block graphs; a fan with more than one triangle is not a block graph. The present statement thus supplies the full fan and clique-path family beyond the previously reported isolated fan value.

## Limitations

This theorem gives an exact minimum number of colors and an admissible-word characterization, not the number of labeled optimal colorings or a classification for arbitrary joins or for wheels. The older \(n=6\), \(r=1\) case is already published. Although relevant primary papers and published mathematical records were compared, this assessment is not a claim of exhaustive coverage of all unpublished results or all mathematical literature.

## References

[1] H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (first public preprint 2024-01-22), https://arxiv.org/abs/2401.11653.

[2] Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336 (2024-10-03), especially Proposition 3.2, https://arxiv.org/pdf/2410.02336.

[3] M. Goetze et al., *Strong odd coloring in minor-closed classes*, arXiv:2505.02736 (2025), https://arxiv.org/pdf/2505.02736.

[4] M. Pilipczuk, *Strong odd colorings in graph classes of bounded expansion*, arXiv:2505.15288 (2025), https://arxiv.org/abs/2505.15288.

[5] A. J. Manattu, A. Vinay, and A. Lakshmanan, *On a conjecture about the strong odd chromatic number of planar graphs*, arXiv:2602.03259 (2026), Theorem 1, https://arxiv.org/pdf/2602.03259.

[6] D. Pradhan, V. Sharma, and S. Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441 (2026), https://arxiv.org/abs/2610.01441.
