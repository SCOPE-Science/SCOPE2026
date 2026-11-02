# Exact capacity of strand-invariant, GC-balanced, non-overlapping DNA five-mers

## Finding

The maximum cardinality is

\[
\boxed{24}.
\]

Specifically, on the Watson–Crick alphabet \(\Sigma=\{A,C,G,T\}\), the following three constraints hold: each word has two or three \(G/C\) positions, the code is closed under reverse complementation, and it is non-overlapping (cross-bifix-free), including prohibiting overlaps of a word with itself. An explicit attaining code is obtained by adjoining the reverse complement of each of the twelve representatives below:

```text
AAGAG AAGGG AAGGT ACAGT ACCGT ACCTG
ACGAG ACTGG ACTTG CAATG CAGAG CATAG
```

The resulting code has \(24\) distinct words: twelve have two \(G/C\) symbols and twelve have three.

## Assumptions and scope

Watson–Crick complement exchanges \(A\leftrightarrow T\) and \(C\leftrightarrow G\). If \(w=w_1\cdots w_5\), define \(\rho(w)=\overline{w_5}\cdots\overline{w_1}\). A set \(C\subseteq\Sigma^5\) is *non-overlapping* when, for every ordered \(u,v\in C\) and every integer \(1\le k\le4\), the first \(k\) letters of \(u\) differ from the last \(k\) letters of \(v\). No Hamming-distance, homopolymer-run, or thermodynamic constraint is assumed beyond the stated three properties.

The balance condition represents \(40\%\) or \(60\%\) GC content for a five-letter word, rather than exact \(50\%\), which is impossible at odd length. Closure means **both** strands appear as codewords, not merely that the code avoids close reverse-complement pairs.

## Proof

**Step 1: Exhaust all eligible reverse-complement orbits.** Exactly

\[
2^5\left(\binom{5}{2}+\binom{5}{3}\right)=640
\]

DNA five-mers have two or three \(G/C\) symbols. Since length five is odd and no DNA letter equals its complement, no five-mer is fixed by reverse complementation. Thus these \(640\) words form exactly \(320\) disjoint orbits \(\{w,\rho(w)\}\), each of size two. An orbit is *admissible* when its two words, together, satisfy all \(4\) nonempty proper prefix–suffix exclusion tests for every ordered pair. Complete generation from the four-letter alphabet leaves exactly \(120\) admissible orbits. Any permitted code is a disjoint union of admissible orbits.

**Step 2: Certify an upper bound with a twelve-class incompatibility partition.** On the admissible orbits define a simple undirected incompatibility graph: two distinct vertices are adjacent exactly when some ordered pair of their constituent five-mers exhibits a forbidden proper prefix–suffix overlap. The file `certificate.json` explicitly lists each of the \(120\) canonical orbit representatives and assigns a class from \(0\) through \(11\). The twelve class cardinalities are

\[
(10,10,7,8,6,8,7,12,12,12,14,14).
\]

The verifier regenerates the complete eligible universe without trusting its contents and checks that every pair of distinct orbits **within the same class** is incompatible. Therefore the twelve classes partition the vertices into twelve cliques of the incompatibility graph. A code can select at most one orbit from each class, so it has at most \(12\) orbits, hence at most \(24\) words. No optimization software or heuristic output is assumed by this upper-bound argument: the partition is an explicit finite certificate, checked against every relevant pair.

**Step 3: Certify the lower bound.** The twelve representatives in the Finding section are a subset of the admissible-orbit list. Direct ordered-pair comparison shows that their \(24\) words after reverse-complement closure satisfy all \(4\) prefix–suffix exclusions. All words meet the stated GC condition and no orbit is repeated. This yields a code of size \(24\). Together with Step 2, the optimum is exactly \(24\).

## Verification

From the directory containing `certificate.json`, use standard-library Python:

```bash
python3 verify.py certificate.json
python3 crosscheck.py certificate.json
```

`verify.py` uses literal DNA strings and all ordered prefix–suffix tests. `crosscheck.py` separately uses a two-bit encoding of each DNA symbol and bit-masked suffix/prefix equality; it independently regenerates the admissible orbit graph and verifies every stated class and witness pair. Both return success, respectively `VERIFY_OK` and `CROSSCHECK_OK`. The entire check is finite: \(640\) candidate words, \(320\) reverse-complement orbits, and \(120\) admissible orbits. The certificate is not a claim of a general formula for other lengths.

## Relationship to prior work

King (2003) studies DNA code bounds under GC-content and reverse-complement *distance* constraints, not the closure-plus-non-overlap extremum here. Chee, Kiah, Purkayastha and Wang (2012) and Blackburn (2013) develop general non-overlapping codes. Yazdi and collaborators (2015) motivate joint DNA biochemical and synchronization restrictions, but do not give this exact constrained maximum. Stanovnik, Moškon and Mraz (2024) treat nearly GC-balanced non-overlapping codes and report exact small cases primarily for even lengths; their definitions and computations do not impose reverse-complement closure or give this five-mer optimum. A published exact theorem for unrestricted four-letter length-five non-overlapping codes yields maximum \(81\), but its unrestricted optimum and its classifications do not imply the optimum \(24\) for the present strictly constrained family.

The value \(24\) should not be construed as an error-correcting, sequencing-ready, or experimentally validated DNA code size. It is the mathematical capacity for the three specified constraints only.

## Limitations

The claim is exact only for five-letter DNA words and the explicitly given closure, GC balance and overlap conditions. It does not assert a Hamming-distance guarantee, homopolymer constraint, secondary-structure resistance, or a biochemical performance prediction. The finite certificate proves this parameter exactly but neither enumerates all optimal codes nor gives an all-length formula. Historical priority, particularly against unindexed constrained-code tables, has not been independently certified.

## References

1. O. D. King, “Bounds for DNA codes with constant GC-content,” arXiv:math/0306197 (first publicly posted 2003-06-12). https://arxiv.org/abs/math/0306197
2. Y. M. Chee, H. M. Kiah, P. Purkayastha and C. Wang, “Cross-Bifix-Free Codes Within a Constant Factor of Optimality,” arXiv:1209.0236 (2012). https://arxiv.org/abs/1209.0236
3. S. R. Blackburn, “Non-overlapping codes,” arXiv:1303.1026 (2013). https://arxiv.org/abs/1303.1026
4. S. M. H. Tabatabaei Yazdi et al., “A Rewritable, Random-Access DNA-Based Storage System,” *Scientific Reports* **5**, 14138 (2015). https://doi.org/10.1038/srep14138
5. L. Stanovnik, M. Moškon and M. Mraz, “On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths,” arXiv:2410.18458 (2024). https://arxiv.org/abs/2410.18458
6. “Exact size and enumeration of maximum length-five non-overlapping codes,” publicly archived research finding (2026). https://github.com/Resultary/2026
