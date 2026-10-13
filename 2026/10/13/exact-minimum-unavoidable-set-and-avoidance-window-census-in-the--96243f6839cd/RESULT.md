# Exact minimum unavoidable-set and avoidance-window census in the golden-mean shift through length eight

## Finding
Fix the binary golden-mean language, in which the adjacent factor `11` is forbidden. For each integer \(2\le k\le8\), let \(G_k\) be the directed order-\(k\) shift graph on length-\(k\) admissible words, with the usual one-symbol overlap arcs. Let \(c_k\) be the number of cyclic rotation classes whose periodic extensions remain admissible. A minimum unavoidable set is a set of admissible length-\(k\) factors that every sufficiently long admissible word contains and has smallest possible cardinality.

The minimum cardinality \(c_k\), which is **previously known** in this restricted language, and the **complete counts of distinct minimum unavoidable sets** and **complete longest surviving directed-path spectra** are:

| \(k\) | Admissible vertices | \(c_k\) (known minimum) | Candidate necklace transversals | All optimal sets | Longest surviving path (vertices): number of optimal sets |
|---:|---:|---:|---:|---:|:---|
| 2 | 3 | 2 | 2 | 2 | 1:2 |
| 3 | 5 | 2 | 3 | 1 | 2:1 |
| 4 | 8 | 3 | 8 | 4 | 3:2, 4:2 |
| 5 | 13 | 3 | 25 | 1 | 6:1 |
| 6 | 21 | 5 | 216 | 40 | 7:10, 8:16, 9:2, 10:8, 11:4 |
| 7 | 34 | 5 | 2,401 | 2 | 13:2 |
| 8 | 55 | 8 | 262,144 | 240 | 15:16, 16:20, 17:52, 18:58, 19:36, 20:18, 21:24, 22:16 |

In particular, exactly \(240\) distinct eight-element sets are unavoidable among the admissible eight-bit factors, and exactly \(16\) of them minimize the maximum avoidance window. Each of these \(16\) sets hits every admissible binary word of length \(23\), whereas all \(240\) minimum-cardinality sets hit every admissible word of length \(30\). The best bound \(23\) is sharp: a length-\(22\) admissible word can avoid each best set. The list `optimizers.tsv` contains **every** optimum for all seven values of \(k\), in decimal vertex encoding and its longest residual path length.

## Assumptions and scope
A length-\(k\) word is a vertex precisely if it contains no occurrence of `11` at internal adjacent positions. A directed arc from \(u=u_1\cdots u_k\) to \(v=v_1\cdots v_k\) exists if \(v=u_2\cdots u_kb\) for a binary bit \(b\) and \(v\) remains admissible. A rotation necklace is *periodic-admissible* if every one of its cyclic rotations is admissible; this is equivalent to its bi-infinite periodic extension avoiding `11`. A set is *unavoidable* when every sufficiently long finite admissible word contains a length-\(k\) factor from it. Counts regard binary words as labeled by their actual ordered digits; reversal is not quotiented out.

For a deletion set \(S\), the longest residual path length \(\ell(S)\) is the maximum number of vertices in a directed path of the induced graph \(G_k-S\), provided that graph is acyclic. Consequently the longest finite admissible word avoiding \(S\) has exactly \(k+\ell(S)-1\) letters, and the first guaranteed hit length is \(k+\ell(S)\). All finite results are for exactly \(2\le k\le8\).

## Proof
**Cycle lower bound.** Each periodic-admissible rotation necklace forms a directed cycle in \(G_k\), including a self-loop when the word is constant. Distinct necklaces have disjoint vertex sets. An unavoidable set must meet every such cycle, so its size is at least \(c_k\). If equality holds, the set must select exactly one vertex from each periodic-admissible necklace and none outside them.

**Finite exhaustion lemma.** For any candidate transversal \(S\), an admissible infinite sequence avoids \(S\) if and only if \(G_k-S\) contains a directed cycle: successive length-\(k\) windows trace a walk; a walk in a finite graph is infinite exactly when some reachable cycle can be traversed forever. Thus a transversal is unavoidable exactly when the induced graph is acyclic. The same equivalence applies to two-sided sequences and to eventual avoidance. Every smallest unavoidable set appears exactly once in the Cartesian product of the disjoint necklace vertex lists. A topological-sort computation on every candidate therefore yields a complete, nonredundant enumeration of all optimum sets.

**Exact computation.** Enumerating every periodic-admissible necklace gives sizes \((2,2,3,3,5,5,8)\) for \(k=2,\ldots,8\), in agreement with the prior periodic-orbit table. The seven Cartesian products have respectively \(2,3,8,25,216,2401,262144\) candidates. Tests on **all** candidates give accepted counts \((2,1,4,1,40,2,240)\) and precisely the spectra above. Nonemptiness in each case proves sharpness of the periodic-cycle lower bound; existence of minimum cardinality was already established in the earlier literature for this shift. For each acyclic deletion the longest path is computed by dynamic programming over a topological ordering. A separate depth-first cycle detector and memoized longest-path computation independently generates identical complete optimum catalogues.

**Exact avoidance cutoff.** A path containing \(p\) successive vertices corresponds to an admissible word of length \(k+p-1\) whose \(p\) consecutive length-\(k\) factors are the path vertices. Thus the longest avoiding word has length \(k+\ell(S)-1\). At \(k=8\), the smallest observed \(\ell(S)\) is \(15\), attained by exactly \(16\) of the \(240\) optimum sets, giving a sharp guaranteed hit length of \(23\). The greatest \(\ell(S)\) is \(22\), giving first guaranteed hit length \(30\) for those sets.

## Verification
Run `python3 verify_python.py` and compile `verify_cpp.cpp` using `g++ -std=c++17 -O2 -o verify_cpp verify_cpp.cpp` followed by `./verify_cpp`. These two independent implementations use topological sorting and depth-first detection respectively. Every listed optimum is checked for exact one-per-necklace membership and acyclic residual graph; both independently enumerate all candidate transversals. The complete `optimizers.tsv` catalogue is additionally checked against both computed lists. Reproduction requires only a Python 3 standard library and a C++17 compiler. An explicit best length-eight set, shown as binary strings, is `{00000000, 00001000, 00010100, 00100100, 00101010, 01000100, 01001010, 10101010}`.

## Relationship to prior work
Champarnaud–Hansel–Perrin (2004, manuscript dated 2003) **already prove** that for the golden-mean language, the minimum unavoidable-set size is the number of admissible necklaces, and list these necklace counts in a periodic-orbit table (their \(X_2\), with the forbidden letter renamed). The minimum sizes \(c_k\) are therefore context, not the new contribution. Moreno (2003) develops the golden-mean restricted de Bruijn graph and enumerates restricted *de Bruijn sequences*, a distinct object; in particular his number of length-eight sequences is not a count of minimum unavoidable sets. Zheng–Kingsford–Marçais (2020 online) demonstrate the relevance of the longest avoidance path to sequence sketches, but treat the unrestricted full-alphabet de Bruijn graph. The new statement is the complete optimizer multiplicity and per-optimizer longest-path distribution for \(2\le k\le8\) in the golden-mean graph. Literature comparison does not certify priority against unindexed data.

## Limitations
This is an exact **finite** census; no formula for the number of optimal sets or the best avoidance window beyond length eight is proved. Only the language forbidding the internal factor `11` is considered. The path-cutoff interpretation concerns admissible strings with `11` forbidden everywhere, not unrestricted binary strings. The literature review cannot exclude unindexed prior computations. All mathematical checks were conducted within this result; independent external audit has not been performed.

## References
1. J.-M. Champarnaud, G. Hansel, D. Perrin, *Unavoidable Sets of Constant Length*, International Journal of Algebra and Computation **14** (2004), 241–251. DOI: `10.1142/S0218196704001700`. Author-hosted manuscript dated 2003-10-28; the published paper establishes the restricted-language minimum-size theorem.
2. E. Moreno, *Lyndon Words and de Bruijn Sequences in a Subshift of Finite Type*, WORDS 2003 proceedings, 400–410. Author manuscript: `https://www.dim.uchile.cl/~emoreno/publicaciones/PREPRINTS/preprint-WORDS03-Lyndon_words_and_de_Bruijn_sequences_in_a_subshift_of_finite_type.pdf`.
3. A. Burstein and S. Kitaev, *On Unavoidable Sets of Word Patterns*, arXiv:`math/0311399`, publicly posted 2003-11-23. Related overlap-graph work; not a theorem about the golden-mean optimiser census.
4. H. Zheng, C. Kingsford, G. Marçais, *Lower Density Selection Schemes via Small Universal Hitting Sets with Short Remaining Path Length*, Journal of Computational Biology **28** (2021), online 2020-12-15, DOI: `10.1089/cmb.2020.0432`.
5. G. Marçais, D. DeBlasio, C. Kingsford, *Sketching Methods with Small Window Guarantee Using Minimum Decycling Sets*, Journal of Computational Biology (2024), preprint arXiv:`2311.03592`. Related full-shift optimization, not a cited golden-mean optimizer census.
