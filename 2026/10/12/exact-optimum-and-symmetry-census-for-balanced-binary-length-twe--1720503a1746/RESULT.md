# Exact optimum and symmetry census for balanced binary length-twelve error-correcting synchronization codes

## Finding
For the binary alphabet \(\{0,1\}\), the maximum size of a length-\(12\) balanced, mutually uncorrelated (non-overlapping) code having minimum Hamming distance at least \(4\) is
\[
\boxed{13}.
\]
There are exactly \(4{,}996\) distinct labeled optimum thirteen-word codes. Reversing every word and complementing every bit generate a four-element symmetry group acting freely on these codes, hence exactly \(1{,}249\) symmetry classes. Every optimum code has minimum Hamming distance exactly \(4\).

## Assumptions and scope
A binary length-\(12\) word is *balanced* when its Hamming weight is exactly \(6\). For words \(x,y\), let \(p_k(x)\) be the length-\(k\) prefix and \(s_k(y)\) the length-\(k\) suffix. A code \(C\) is *mutually uncorrelated* (also termed non-overlapping or cross-bifix-free) when
\[
\forall x,y\in C\;\forall k\in\{1,\ldots,11\}:\quad p_k(x)\ne s_k(y).
\]
The quantifiers include \(x=y\). The aligned Hamming-distance constraint is \(d_H(x,y)\ge4\) whenever \(x\ne y\). Because the words have the same even weight, all pair distances are even. The constraint permits correction of one substituted bit given known codeword boundaries; it does not guarantee reliable detection of a boundary when a substitution has occurred.

The label order of the twelve coordinates and the identities of the two alphabet symbols are fixed when counting \(4{,}996\) optimum code sets. The symmetry count quotients only the order-two global reversal and global bit-complementation operations, not arbitrary coordinate permutations or cyclic rotations.

## Proof
**Finite reduction.** Start with the \(\binom{12}{6}=924\) balanced binary words. An admissible word cannot have a nonempty proper prefix equal to its own same-length suffix. Discarding such bordered words leaves exactly \(272\) vertices. Define a simple undirected graph \(G\) on these vertices, joining distinct words \(x,y\) if and only if both orientations of every proper prefix/suffix overlap are unequal and \(d_H(x,y)\ge4\). This construction yields exactly \(11{,}206\) edges. By the definitions, an admissible code is exactly a clique of \(G\).

**Exhaustiveness lemma.** The included C++ and Python checkers implement a complete Bron–Kerbosch search with candidate set \(P\), excluded set \(X\), and growing clique \(R\). It starts with \(R=X=\varnothing\) and \(P=V(G)\). When \(P=X=\varnothing\) the current clique is maximal. At each internal node, select a pivot \(u\in P\cup X\), recurse once for every vertex in \(P\setminus N(u)\), intersecting the candidate and excluded sets with its neighborhood, and then move that vertex from \(P\) to \(X\). The pivot rule cannot omit a maximal clique: if a maximal clique extending \(R\) had all new vertices in \(N(u)\), it could also be extended by \(u\), contradicting maximality unless \(u\) already occurred in the branch. The familiar induction on the remaining vertex set establishes that each maximal clique is generated exactly once. The source files implement the full base cases and updates, making the finite result reproducible without trusting a stored log.

The independently written implementations both find the following number of maximal cliques, sorted by cardinality:

| Cardinality | Number of maximal cliques |
| ---: | ---: |
| \(6\) | \(2{,}648\) |
| \(7\) | \(40{,}764\) |
| \(8\) | \(437{,}600\) |
| \(9\) | \(1{,}883{,}356\) |
| \(10\) | \(1{,}870{,}068\) |
| \(11\) | \(584{,}172\) |
| \(12\) | \(63{,}740\) |
| \(13\) | \(4{,}996\) |

The sum is \(4{,}887{,}344\). In particular no maximal clique has more than thirteen vertices; every clique extends to a maximal one, so \(|C|\le13\). All \(4{,}996\) size-thirteen maximal cliques are distinct and constitute every optimum code. The complete lexicographically sorted catalogue is embedded as `optimizers.txt`.

**Symmetries.** Reversing all coordinates swaps prefix with suffix, and complementing all coordinates preserves equality, balanced weight, and Hamming distance. These two involutions commute. Checking their action on the complete catalogue shows that all \(4{,}996\) codes are mapped to codes in the catalogue, with no code fixed by reversal, complementation, or their product. Therefore every orbit has four members, giving \(4{,}996/4=1{,}249\) orbits. Direct inspection also finds a distance-four pair in every optimum code.

A concrete optimum is

```
000000111111 000011001111 000011110101 000101010111 000101101011
000110011011 000110101101 001001011011 001001101101
001010010111 001010101011 001100011101 001100100111
```

## Verification
Compile and run the standalone C++ enumerator with

```
g++ -O3 -std=c++17 verify_cpp.cpp -o verifier
./verifier optimizers_cpp.txt
```

Independently run the standard-library-only Python implementation with

```
python3 verify_py.py optimizers_py.txt
```

The resulting optimizer files must equal the embedded `optimizers.txt` byte-for-byte. Its SHA-256 is `63a11362c2775f93caebe0a2c00b94afddf3d4e2aab491055efdb9dabf18fdea`, and its exact size is \(844{,}324\) bytes. Each row records one distinct code as thirteen lexicographically ordered twelve-bit words. Both independent algorithms reconstruct eligibility, compatibility, and the complete maximal-clique census from scratch. The orbit and Hamming-distance checks can be rerun with `verify_symmetry.py`.

## Relationship to prior work
Yazdi, Kiah, and Milenkovic's preprint on weakly mutually uncorrelated codes (arXiv:1601.08176; publicly released 2016-01-29) explicitly studies balanced error-correcting synchronization codes. Its strict \(k=1\) condition is the non-overlap constraint used here; its constructions and asymptotic bounds do not furnish this exact length-twelve optimum or list of optimizers. Blackburn's earlier non-overlapping-code paper (arXiv:1303.1026) studies the synchronization condition without both added constraints. Levy and Yaakobi (arXiv:1804.05371) separately develop balanced and error-correcting mutually uncorrelated code families but do not determine this finite combined optimum. Stanovnik, Moškon, and Mraz (DOI 10.1007/s40314-024-03055-0) compute balanced optimum cardinalities for small lengths without imposing the additional Hamming-distance requirement, and their discussion explicitly identifies large-distance compatibility as a further issue. Neither a result for the unrestricted balanced problem nor a construction with some minimum distance logically classifies all balanced error-correcting optima of this instance.

## Limitations
This is an exact, computer-assisted *finite* theorem at length twelve only. No all-length formula or information-theoretic performance bound is claimed. The exhaustive search and complete catalogue permit replay and auditing but do not replace independent mathematical or bibliographic review. We do not claim robust synchronization under errors, only non-overlap in the noiseless stream together with aligned one-bit substitution correction. An earlier unindexed classification could affect originality.

## References
1. S. M. H. T. Yazdi, H. M. Kiah and O. Milenkovic, *Weakly Mutually Uncorrelated Codes*, arXiv:1601.08176 (first submitted 2016-01-29), https://arxiv.org/abs/1601.08176.
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (first submitted 2013-03-05), https://arxiv.org/abs/1303.1026.
3. M. Levy and E. Yaakobi, *Mutually Uncorrelated Codes for DNA Storage*, arXiv:1804.05371 (2018), https://arxiv.org/abs/1804.05371.
4. L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, *Computational and Applied Mathematics* 44, 109 (2025), https://doi.org/10.1007/s40314-024-03055-0.
