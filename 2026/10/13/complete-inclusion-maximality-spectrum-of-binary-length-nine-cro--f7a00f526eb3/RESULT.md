# The complete inclusion-maximality spectrum of binary length-nine cross-bifix-free codes

## Finding

For a set \(C\subseteq\{0,1\}^{9}\), impose the non-overlap condition that for every ordered pair \(u,v\in C\) (including \(u=v\)) and every integer \(1\le j\le8\), the length-\(j\) prefix of \(u\) differs from the length-\(j\) suffix of \(v\). Call such a nonempty code *inclusion-maximal* if no ninth-bit binary word outside the code can be added while preserving non-overlap. Distinguish this notion from *maximum-cardinality*.

The complete cardinality enumerator of inclusion-maximal codes, counting distinct sets of labeled binary words, is

\[
\begin{aligned}
M(z)={}&4z+12z^4+20z^5+48z^6+200z^7+588z^8\\
&+1712z^9+5056z^{10}+13520z^{11}+23136z^{12}\\
&+16832z^{13}+1152z^{14}.
\end{aligned}
\]

Thus there are exactly \(62{,}280\) inclusion-maximal non-overlapping codes. Their possible cardinalities are \(1\) and each integer from \(4\) through \(14\); no nonempty inclusion-maximal code has cardinality \(2\) or \(3\). Global bit complementation and word reversal generate a four-element symmetry group, and its action on these \(62{,}280\) codes is free; there are therefore precisely \(15{,}570\) orbits. The coefficient of \(z^{14}\) is part of the full spectrum and is not separately claimed as a new optimal-code enumeration.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the length is exactly nine, no cyclic wraparound of individual words is introduced, and the code is an *unordered* set of distinct indexed nine-bit words. Overlap tests exclude the empty word and whole-word overlap and consider every proper length \(j\) from one through eight. An individual codeword is admissible only when it is *unbordered* (has no nonempty proper prefix equal to its suffix). Inclusion maximality means that not even one additional word can be inserted while maintaining the property; it does not demand maximum cardinality and does not mean robustness to bit errors.

## Proof

Let \(U\) be the set of all unbordered nine-bit words. For \(u,v\in U\), define compatibility by the simultaneous inequalities \(\operatorname{prefix}_j(u)\ne\operatorname{suffix}_j(v)\) and \(\operatorname{prefix}_j(v)\ne\operatorname{suffix}_j(u)\) for every \(1\le j\le8\). Let \(G\) be the simple graph on \(U\) whose distinct vertices are adjacent exactly when compatible.

**Reduction lemma.** The nonempty non-overlapping binary length-nine codes are precisely the nonempty cliques of \(G\), and the inclusion-maximal codes are precisely the maximal cliques. To prove this, a word with a proper border fails self-compatibility, so every codeword belongs to \(U\). On \(U\) the remaining conditions are exactly pairwise graph adjacency. A word outside \(U\) can never extend a code, while a word in \(U\) extends the code exactly when its vertex is adjacent to every existing vertex. Hence graph maximality and code inclusion-maximality coincide.

The computation is a *finite exhaustive proof* of the resulting graph statement. Generate all \(512\) binary length-nine words; filter self-overlapping words using each of the eight proper prefix/suffix lengths; this leaves exactly \(148\) unbordered vertices. Compare all distinct pairs at all eight lengths; exactly \(3{,}080\) unordered edges remain. Enumerate all maximal cliques by a recursive Bron–Kerbosch search with pivot. At a recursive call, \(R\) is a clique, \(P\) comprises not-yet-processed common neighbors of \(R\), and \(X\) comprises already-processed common neighbors. A maximal clique is emitted precisely if \(P=X=\varnothing\). Choosing a pivot \(p\in P\cup X\), it is sufficient to branch on \(P\setminus N(p)\): any maximal clique extension of \(R\) must contain one of those vertices; otherwise adjoining \(p\) would contradict maximality. After a branch, move its vertex from \(P\) to \(X\). Induction on the number of possible extension vertices proves every maximal clique appears exactly once and no nonmaximal clique appears.

The emitted clique cardinalities give the polynomial in the Finding section. Directly test each output against every unselected admissible word for maximality, and compare the independently generated, lexicographically sorted catalogues described below. The resulting full catalogue has exactly \(62{,}280\) distinct lines. For every catalogue element \(C\), compute the images under identity, coordinate reversal, bit complementation, and their composition; each orbit has exactly four members of the catalogue, proving the symmetry assertion.

## Verification

The package includes `artifacts/verify_bitset.py`, a Python standard-library bit-mask search, and `artifacts/verify_strings.cpp`, a separate C++17 string-and-set search. Both independently construct the graph and enumerate every maximal clique, and both explicitly recheck mutual compatibility and inability to add any other admissible word. After running each program in a scratch directory with the `--catalog` argument, the files `catalog_python.txt` and `catalog_cpp.txt` must agree byte-for-byte; the common ASCII text catalogue contains sorted codeword strings on each line, with a single space separator and Unix newlines. Its SHA-256 is `ebacd3ecd51b08c10b05e462a3496200ca3261b0840a0a3351910af91436ecd3` and its byte length is \(7{,}338{,}080\). The exact file is also included as `artifacts/maximal_catalog.txt.gz` using gzip compression; decompress and compare this digest.

The expected vertex count, edge count, histogram, and symmetry-orbit count are all asserted in the Python program; the C++ program independently verifies the vertex/edge counts, histogram, and sorted catalogue. Use `python3 artifacts/verify_bitset.py --catalog`, compile `artifacts/verify_strings.cpp` using `c++ -std=c++17 -O2`, run the executable with `--catalog`, and compare its output catalogue with the Python file. The C++ source uses standard-library facilities only.

## Relationship to prior work

Bilotta, Pergola and Pinzani (2011) explicitly motivated non-expandable cross-bifix-free families and gave lattice-path constructions. Chee, Kiah, Purkayastha and Wang (2012/2013) treated maximum-size codes, with the binary length-nine case exceptional among their reported short-length constructions. Blackburn (2013/2015) studied general non-overlapping code bounds and constructions. Barcucci and collaborators (2014) supplied other non-expandable construction families. Qin, Chen and Luo (2023) characterized non-expandability of parameterized construction families and provided size tables for those families. These results motivate the question but are not an all-code cardinality census of *every* inclusion-maximal length-nine code.

A maximum-code count or the existence of non-expandable constructions does not imply the coefficients for all smaller cardinalities. In particular, the previously studied optimum of \(14\) is not the novel extremal assertion here: the new object is the complete inclusion-maximality spectrum together with its free symmetry action.

## Limitations

This is an exact finite result for one fixed binary block length, not an all-length formula or a statement about larger alphabets. The exhaustive computation relies on the stated complete recursive algorithm and exact integer/string comparisons; a table of output numbers alone is not a mathematical certificate. Both complete implementations, the catalogue, and the proof of exhaustive enumeration are provided to make the computation independently reproducible. Earlier unindexed catalogues of all inclusion-maximal codes might exist; no claim of absolute priority is made. No communication-channel error-correction performance is asserted.

## References

1. S. Bilotta, E. Pergola, R. Pinzani, *A new approach to cross-bifix-free sets*, arXiv:1112.3168v1 (first public 2011-12-14). https://arxiv.org/abs/1112.3168
2. Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236v1 (2012-09-03). https://arxiv.org/abs/1209.0236
3. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026v1 (2013-03-05). https://arxiv.org/abs/1303.1026
4. E. Barcucci, S. Bilotta, E. Pergola, R. Pinzani, J. Succi, *Cross-bifix-free sets via Motzkin paths generation*, arXiv:1410.4710v1 (2014-10-17). https://arxiv.org/abs/1410.4710
5. C. Qin, B. Chen, G. Luo, *On non-expandable cross-bifix-free codes*, arXiv:2309.08915v1 (2023-09-16). https://arxiv.org/abs/2309.08915
