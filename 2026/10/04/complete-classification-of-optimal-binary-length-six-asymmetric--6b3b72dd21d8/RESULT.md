# Complete classification of optimal binary length-six asymmetric 1-codes
## Finding
Identify a binary word with its support in \([6]=\{{1,2,3,4,5,6\}}\). Let \(M\) be a perfect matching of \([6]\). A transversal of \(M\) is a three-set containing exactly one point from each matched pair. The eight transversals form a three-dimensional cube by declaring two transversals adjacent when they differ on exactly one matched pair; this cube has two bipartition classes, each of size four.

For either bipartition class \(E\), define
\[
C(M,E)=\{\varnothing,[6]\}\cup M\cup\{[6]\setminus e:e\in M\}\cup E.
\]
Then \(C(M,E)\) has \(12\) codewords and minimum asymmetric distance \(2\). Conversely, every binary length-six code with minimum asymmetric distance at least \(2\) and maximum cardinality \(12\) equals \(C(M,E)\) for a unique pair \((M,E)\).

There are \(15\) perfect matchings of six labeled coordinates and two bipartition classes for each matching, so there are exactly \(30\) labeled maxima. The coordinate-permutation group \(S_6\) is transitive on these \(30\) codes; consequently the stabilizer of each maximum has order \(720/30=24\).

A representative is
\[
\{{000000,000011,001100,001111,010101,011010,100110,101001,110000,110011,111100,111111\}}.
\]
This is exactly the length-six optimal code displayed in Example 2.4 of Grassl--Shor--Smith--Smolin--Zeng.

## Assumptions and scope
For \(x,y\in\{0,1\}^6\), write \(N(x,y)\) for the number of coordinates with \(x_i=0\) and \(y_i=1\), and set
\[
\Delta(x,y)=\max\{N(x,y),N(y,x)\}.
\]
The claim concerns arbitrary, not necessarily linear, binary codes \(C\subseteq\{0,1\}^6\) satisfying \(\Delta(x,y)\ge2\) for all distinct \(x,y\in C\). By the standard characterization, these are exactly binary one-asymmetric-error-correcting codes for the Z-channel.

The classification is only for length six and one asymmetric error. It makes no claim for larger lengths, multiple asymmetric errors, or probabilistic optimality criteria.

## Proof
First verify that every displayed construction is valid. Distinct matching edges are disjoint, so their asymmetric distance is \(2\). A matching edge and the complement of any matching edge have asymmetric distance at least \(2\), and the same is true for pairs of complements. A transversal meets each matching edge in one point, so its asymmetric distance from every matching edge and every matching-edge complement is exactly \(2\). Two distinct transversals in the same cube bipartition class differ on exactly two matched pairs; each therefore has two points absent from the other, so their asymmetric distance is \(2\). Finally, \(\varnothing\) and \([6]\) are at asymmetric distance at least \(2\) from every other member. Thus \(C(M,E)\) is a valid \(12\)-word code.

For completeness and uniqueness, the finite search in `verify.py` reconstructs all \(64\) binary words and the compatibility graph whose edges join pairs with asymmetric distance at least \(2\). An exact Bron--Kerbosch enumeration with cardinality pruning finds maximum clique size \(12\) and exactly \(30\) maximum cliques. Independently, the program generates all \(15\) perfect matchings of the six coordinates and both cube bipartition classes for each matching, producing exactly \(30\) distinct codes \(C(M,E)\). It then checks equality of the two sets of \(30\) codes. This equality proves that no other maximum code exists.

Uniqueness of \(M\) inside a maximum code is immediate from the classification: the three weight-two codewords are exactly the three edges of \(M\). Thus different matchings cannot produce the same code. The program also exhausts all \(720\) coordinate permutations of one representative and obtains all \(30\) maxima, proving transitivity and stabilizer order \(24\).

## Verification
Run

`python3 verify.py`

using a standard Python 3 interpreter. The expected terminal line is

`VERIFY_OK maximum=12 labeled_maxima=30 matchings=15 maxima_per_matching=2 coordinate_orbit=30 stabilizer=24 nodes=118645`

The verifier constructs the asymmetric distance from its definition, performs the exact maximum-clique search, generates every matching-based construction, compares the complete sets, and checks the coordinate-permutation orbit. No randomized step, heuristic cutoff, external solver, or timeout is used.

## Relationship to prior work
Grassl--Shor--Smith--Smolin--Zeng define the same asymmetric distance and state that minimum asymmetric distance greater than one is equivalent to correction of one asymmetric error. Their Example 2.4 gives the representative above as a \(12\)-word optimal length-six code, obtained by pairing coordinates and applying their ternary construction. The present finding strengthens that existence statement: every optimal length-six code is a coordinate permutation of that example, and the complete labeled census is \(30\).

Butenko--Pardalos--Sergienko--Shylo--Stetsyuk give the same asymmetric-distance graph formulation and tabulate the exact optimum \(12\) for length six. Their inspected discussion concerns optimum sizes, bounds, partitions, and constructions; it does not give the \(30\)-code census or the matching/transversal classification.

The earlier Weber--de Vroedt--Boekee article is indexed under MSC 94B60 and is described as tabulating optimal sizes for short asymmetric codes. Only metadata and summary material were available during this check, so it is retained as an originality risk rather than treated as evidence that the classification is absent there.

## Limitations
The maximum size \(12\) is already known. The new content is the complete labeled classification, the uniqueness up to coordinate permutation, and the perfect-matching/transversal structure. The completeness proof is finite and computational, although the construction and its validity are elementary and explicit.

A residual originality risk remains that an older thesis, code list, or unindexed table may contain an equivalent census without using the same structural language. Searches for the exact parameter, the count \(30\), the displayed representative, perfect-matching language, Constantin--Rao terminology, and Z-channel aliases did not locate such a result.

## References
1. Markus Grassl, Peter W. Shor, Graeme Smith, John A. Smolin, Bei Zeng, *New Constructions of Codes for Asymmetric Channels via Concatenation*, ISIT 2012 / arXiv:1310.7536.
2. Sergiy Butenko, Panos Pardalos, Ivan Sergienko, Vladimir Shylo, Petro Stetsyuk, *Estimating the Size of Correcting Codes Using Extremal Graph Problems*, DOI:10.1007/978-0-387-98096-6_12.
3. J. H. Weber, C. de Vroedt, D. E. Boekee, *Bounds and Constructions for Binary Codes of Length Less than 24 and Asymmetric Distance Less than 6*, DOI:10.1109/18.21262.
4. OEIS A010101, maximal size of a binary code of length \(n\) and asymmetric distance \(2\).
