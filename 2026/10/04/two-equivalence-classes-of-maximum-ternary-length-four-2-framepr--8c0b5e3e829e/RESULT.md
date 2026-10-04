# Two equivalence classes of maximum ternary length-four 2-frameproof codes
## Finding
Let \(Q=\{0,1,2\}\). A code \(C\subseteq Q^4\) is 2-frameproof when for every \(P\subseteq C\) with \(1\le |P|\le2\), the coordinatewise descendant \(\operatorname{desc}(P)\) contains no codeword of \(C\setminus P\).

Among maximum ternary length-four 2-frameproof codes, every maximum has \(12\) words. There are exactly \(5{,}616\) labeled maximum codes. Under the natural action of coordinate permutations and independent permutations of the three symbols in each coordinate, the maxima form exactly two equivalence classes. Their orbit sizes are \(5{,}184\) and \(432\), with stabilizer orders \(6\) and \(72\), respectively.

Representatives are
\[
\{0000,0011,0022,0101,0202,1001,1112,1120,1210,2002,2110,2221\}
\]
and
\[
\{0000,0011,0101,0222,1001,1112,1120,1210,2022,2110,2202,2221\}.
\]

## Assumptions and scope
The alphabet symbols are labels only. Two codes are equivalent here precisely when one can permute the four coordinates and, independently in each coordinate, permute the three alphabet symbols. The acting group therefore has order \(4!\,(3!)^4=31{,}104\).

The claim is a finite classification for ternary length four only. The fact that the maximum size is \(12\) is included to identify the extremal layer; the new content assessed here is the complete labeled census and two-orbit classification of that layer.

## Proof
For three distinct words \(x,y,z\), the triple is forbidden exactly when one of the three words belongs to the descendant of the other two. Thus 2-frameproof codes are exactly the independent sets of a 3-uniform hypergraph on the \(3^4=81\) ternary words. Direct construction from the descendant definition yields exactly \(18{,}792\) forbidden triples.

First rule out a code of size \(13\). Any two distinct codewords can be carried by the equivalence group to \(0000\) and a word whose first \(d\) coordinates are \(1\) and whose remaining coordinates are \(0\), where \(d\in\{1,2,3,4\}\) is their Hamming distance. The exact branch-and-bound verifier exhausts all four normalized cases. It visits \(27\), \(5{,}631\), \(8{,}225\), and \(4{,}675\) search nodes, respectively, and finds no size-\(13\) code. Because the 2-frameproof property is hereditary under taking subsets, this also rules out every larger code.

Next fix \(0000\) and enumerate every size-\(12\) independent set containing it. Exact include/exclude branching, with only valid matching and disjoint-forbidden-triple upper bounds, gives exactly \(832\) such codes after \(140{,}463\) nodes. Because the equivalence group is transitive on the \(81\) words and each maximum contains \(12\) words, double counting incidences gives
\[
832\cdot 81/12=5{,}616
\]
labeled maxima.

Finally traverse all \(31{,}104\) group elements on the \(832\) normalized maxima. Canonicalization gives exactly two orbits. Of the normalized maxima containing \(0000\), \(768\) lie in the first orbit and \(64\) in the second. The stabilizers have orders \(6\) and \(72\), so orbit-stabilizer gives \(31{,}104/6=5{,}184\) and \(31{,}104/72=432\). Their sum is \(5{,}616\), and the incidence checks \(5{,}184\cdot12/81=768\) and \(432\cdot12/81=64\) independently agree with the normalized enumeration.

## Verification
Compile and run `verify.cpp` with a C++17 compiler, for example `c++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. The packaged captured run reports `VERIFY_OK bad_triples=18792 maximum=12 labeled_maxima=5616 normalized_with_0000=832 orbits=2 orbit_sizes=5184,432 stabilizers=6,72 normalized_orbit_counts=768,64 search13_nodes=27,5631,8225,4675 enum_nodes=140463` and prints the two representatives. The program reconstructs the words, forbidden triples, four symmetry-normalized size-\(13\) searches, all normalized maxima, and the complete equivalence-group action from definitions.

## Relationship to prior work
Chee and Zhang study length-four 2-frameproof codes as the case \(c=2\) and \(l=c+2\), giving general constructions and asymptotic sharpness. Their 2012 construction specializes to a nine-word ternary code. Cheng, Jiang and Wang subsequently sharpen upper bounds for large alphabets. Rochanakul's 2020 paper gives an explicit ternary length-four 2-frameproof code of size \(12\), while concentrating on upper bounds and leaving larger-alphabet gaps for further study.

The inspected literature supplies constructions, witnesses, and bounds rather than the \(5{,}616\)-code census or the two-orbit decomposition. The present verifier independently establishes the extremal layer before classifying it.

## Limitations
No claim is made for larger alphabets, other lengths, or other coalition sizes. The exhaustive proof is finite and specific to \(Q^4\). Search absence is not itself treated as novelty evidence; originality rests on statement-level comparison with the inspected primary literature and the prior exact separable result, with a residual risk of an unindexed finite enumeration.

## References
1. Y. M. Chee and X. Zhang, “Improved Constructions of Frameproof Codes,” IEEE Transactions on Information Theory 58(8), 5449–5453 (2012), arXiv:1206.5863, DOI 10.1109/TIT.2012.2197812.
2. M. Cheng, J. Jiang and Q. Wang, “Improved bounds on 2-frameproof codes with length 4,” Designs, Codes and Cryptography 87, 97–106 (2019), DOI 10.1007/s10623-018-0490-5.
3. P. Rochanakul, “New Bounds on 2-Frameproof Codes of Length 4,” International Journal of Mathematics and Mathematical Sciences 2020, Article 4879108, DOI 10.1155/2020/4879108.
