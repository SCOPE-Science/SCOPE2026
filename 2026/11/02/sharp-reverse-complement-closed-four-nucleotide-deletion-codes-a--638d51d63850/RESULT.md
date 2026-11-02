# Sharp reverse-complement-closed four-nucleotide deletion codes and their extremizers

## Finding

**Theorem.** Let \(\Sigma=\{A,C,G,T\}\), with Watson–Crick complement \(\overline A=T\), \(\overline T=A\), \(\overline C=G\), and \(\overline G=C\). For a four-letter word \(x=x_1x_2x_3x_4\), define reverse complementation by \(\rho(x)=\overline{x_4}\overline{x_3}\overline{x_2}\overline{x_1}\), and let \(D(x)\) be the set of *distinct* length-three words obtained by deleting exactly one coordinate of \(x\).

A **strand-closed one-deletion-correcting code** is a set \(C\subseteq\Sigma^4\) for which \(\rho(C)=C\) and \(D(x)\cap D(y)=\varnothing\) whenever \(x\ne y\) are members of \(C\). Among all such codes:

1. The maximum size is exactly **\(24\)**. Exactly **\(160\)** different subsets of \(\Sigma^4\) attain it, with the four nucleotide symbols considered labeled.
2. Every maximum code contains self-reverse-complementary words. Among the \(160\) maxima, the counts with exactly \(2,4,6,8\) such words are, respectively, \(4,44,76,36\). There are **\(28\)** classes of maxima under the eight alphabet permutations commuting with Watson–Crick complementation.
3. If the additional requirement \(x\ne\rho(x)\) is imposed on **every** codeword, the maximum falls to exactly **\(22\)**, and precisely **\(44\)** labeled codes attain that restricted maximum.

One maximum 24-word code, in alphabetical order, is

```
AAAA AACC AAGG ACGA AGTC ATTA CATG CCAA CCCC CCTT CGGC CTAC
GACT GCCG GGAA GGGG GGTT GTAG TAAT TCGT TGCA TTCC TTGG TTTT
```

A maximum 22-word code with no self-reverse-complementary word is

```
AAAA AACC AAGT ACGA ACTT CAGG CATC CCAA CCCC CCTG GATG GCTA
GGAC GGGG GGTT GTCC TAGC TCGT TGAA TTCA TTGG TTTT
```

## Assumptions and scope

The blocklength is fixed at four nucleotides; the alphabet is exactly the four **labeled** letters A, C, G, T. The receiver observes an unknown deletion of **exactly one** nucleotide. Duplicate deletion outcomes of the same transmitted word count only once; outcomes from distinct codewords must be disjoint. Strand closure means that the reverse complement of each codeword is included as a codeword, **not** that words and reverse complements must be far apart in Hamming distance. The optional self-complementarity exclusion concerns a four-letter word equal to its own reverse complement. No GC balance, insertion correction, substitution correction, or biochemical stability hypothesis is imposed.

## Proof

**1. Reduction to a finite weighted graph.** Reverse complementation is an involution on \(\Sigma^4\). It fixes precisely \(16\) words, of the form \(a b\overline b\overline a\), and pairs the other \(240\) into \(120\) two-element orbits. For every one of these \(136\) orbits, deletion shadows of distinct members within that orbit are disjoint, as verified by enumerating all four possible deletion sites and taking *sets* of the resulting length-three words. Consequently every involution orbit is individually admissible.

Construct a graph with one vertex per involution orbit. Give a vertex weight \(1\) or \(2\) according to the orbit size. Distinct vertices are adjacent exactly when their **unions** of deletion shadows are disjoint. Then taking the union of orbits gives a bijection between strand-closed correcting codes and graph cliques; code size equals total clique weight. Requiring no fixed word means restricting the graph to its \(120\) weight-two vertices. There are \(4^3=64\) possible deletion outputs, represented by exact integer bit masks.

**2. Complete upper bounds and equality counting.** The standalone exhaustive verifier `verify.py` builds the 136-vertex graph directly from the definitions and performs exact weighted maximum-clique search. It partitions each candidate set greedily into classes whose vertices are pairwise **nonadjacent** in the compatibility graph. Any clique takes at most one vertex from each class. Therefore the sum of the maximum vertex weight in each color class bounds the weight of a clique from that set. The verifier records a vertex order class by class and each prefix's cumulative class-weight upper bound. Recursion branches on inclusion of a vertex, restricts its future candidates to neighbors, and deletes the vertex before exploring the next branch. Whenever the current clique weight plus the recorded prefix bound cannot beat the current best, the maximization branch is correctly discarded. An analogous recursion enumerates every clique whose weight equals the certified maximum, pruning only when the bound is strictly less than that target.

These pruning rules are valid for **all** graph cliques, not merely sampled examples. The verifier evaluates \(104{,}470\) search states and returns maximum weight \(24\). Equality enumeration evaluates \(214{,}187\) states and outputs exactly \(160\) different maximum cliques. The inventories `optimal_rc24.tsv` and `optimal_rc22_no_self.tsv` are full lists, not samples; the verifier regenerates and compares them in lexicographic order, then separately checks every listed word's reverse complement and deletion shadow.

When vertices from the \(16\) fixed-point orbits are disallowed, the exact maximum search visits \(4{,}848\) states and establishes upper bound \(22\); equality enumeration visits \(19{,}219\) states and gives exactly \(44\) optimal codes. The two explicit displayed codes certify the corresponding lower bounds independently through direct shadow-disjointness checks.

**3. Fixed points and symmetry.** Counting words satisfying \(x=\rho(x)\) inside each of the \(160\) codebooks yields the distribution in the theorem and shows that no 24-word optimum avoids fixed words. The subgroup of the 24 nucleotide relabelings commuting with complement consists of precisely eight permutations. Applying those eight maps to each maximum code partitions all \(160\) codes into \(28\) distinct classes. Their orbit-size and fixed-word-count multiplicities are

| Group-orbit size | Fixed words per code | Number of symmetry classes |
|---:|---:|---:|
| 4 | 2 | 1 |
| 4 | 4 | 5 |
| 4 | 6 | 7 |
| 4 | 8 | 3 |
| 8 | 4 | 3 |
| 8 | 6 | 6 |
| 8 | 8 | 3 |

The orbit-count identity \(4(1+5+7+3)+8(3+6+3)=160\) independently checks the classification cardinality.

## Verification

All result-specific dependencies are included alongside this document, and use only the Python 3 standard library:

```
python3 verify.py
```

Expected beginning: `VERIFY_OK`, followed by the declared graph size and the maxima, optimizer counts, symmetry classes and search-state counts. The program **recomputes** the orbit graph and both complete inventories from first principles. It checks the four-letter alphabet, all 256 words, 64 distinct possible outputs, 136 admissible orbits, and every claimed codeword compatibility, rather than trusting the TSV files. The finite, exhaustive algorithm is a proof of the stated finite result; none of the computations is claimed to prove anything for larger blocklengths.

## Relationship to prior work

Sloane (2002) defines single-deletion-correcting codes via disjoint deletion-descendant sets and surveys primarily **binary** codes. King (2003) studies DNA-code **Hamming** distance with optional reverse-complement **separation** and often constant GC content, a different requirement from inclusion of every reverse complement. Chee, Ge and Ling (2010) determine spectra of perfect one-deletion codes of length three and perfect two-deletion codes of length four, not this length-four single-deletion strand-closed classification. Cai and collaborators (2019) study quaternary single-indel constructions, including GC-balanced variants, rather than the short-length reverse-complement-invariant optimum and its full census. García-Claro (2025) classifies *linear* quaternary codes invariant separately under reversal and complementation using module structure and Hamming bounds, not the general nonlinear deletion-correcting codes invariant under the combined involution here.

The present proof is a direct finite exhaustive argument under a distinct simultaneous constraint. Literature searches did not identify the same numerical theorem or equality classification, but unindexed historical computations or equivalent formulations may exist and have not been independently ruled out.

## Limitations

This is a **finite, blocklength-four** theorem. It does not assert a capacity law, a longer-length bound, PCR/barcoding performance, thermodynamic desirability of self-complementary words, protection against substitutions or insertions, or uniqueness of an optimal code. The conclusion about self-complementary words is mathematical and does not establish biochemical viability. The verifier and proof have been internally reviewed only; independent mathematical audit and independent historical-priority verification have not been performed.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes* (first public arXiv version 22 July 2002), https://arxiv.org/abs/math/0207197.
2. O. D. King, *Bounds for DNA codes with constant GC-content* (first public arXiv version 12 June 2003), https://arxiv.org/abs/math/0306197.
3. Y. M. Chee, G. Ge and A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes* (first public arXiv version 7 August 2010), https://arxiv.org/abs/1008.1343.
4. K. Cai, Y. M. Chee, R. Gabrys, H. M. Kiah and T. T. Nguyen, *Optimal Codes Correcting a Single Indel / Edit for DNA-Based Data Storage* (first public arXiv version 15 October 2019), https://arxiv.org/abs/1910.06501.
5. E. J. García-Claro, *On reversible and reversible-complementary DNA codes over the finite field of four elements* (first public arXiv version 23 June 2025), https://arxiv.org/abs/2506.19170.
