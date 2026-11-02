# Sharp GC-balanced strand-closed tetranucleotide comma-free codes

## Finding
Let \(\Sigma=\{\mathrm A,\mathrm C,\mathrm G,\mathrm T\}\) with Watson–Crick complement \(\overline{\mathrm A}=\mathrm T\), \(\overline{\mathrm C}=\mathrm G\), and the reverse-complement involution \(\rho(w_1w_2w_3w_4)=\overline{w_4}\overline{w_3}\overline{w_2}\overline{w_1}\). For \(\delta\in\{1,2,3\}\), let \(M_\delta\) be the maximum cardinality of a set \(C\subseteq\Sigma^4\) satisfying the following three conditions: (i) every word has exactly two positions occupied by C or G; (ii) \(\rho(C)=C\); (iii) \(C\) is comma-free and its pairwise Hamming distance is at least \(\delta\). Then
\[
(M_1,M_2,M_3)=(21,17,7).
\]
There are exactly \(136,16,72\) labeled maximizing codebooks, respectively. The respective maxima contain exactly \(3,1,1\) reverse-complement-fixed words. Under the eight alphabet permutations commuting with Watson–Crick complementation, the maxima form \(17,2,9\) equivalence classes, respectively; every class has eight elements.

Here "labeled" means that nucleotide letters and the four coordinate positions are fixed. In particular, the size-\(17\) code detects one nucleotide substitution in a correctly identified four-symbol frame, whereas the size-\(7\) code corrects one substitution in that frame; comma-freeness concerns the undisturbed concatenation of codewords.

## Assumptions and scope
A code \(C\subseteq\Sigma^4\) is *comma-free* if, for every \(u,v,w\in C\) and every offset \(k\in\{1,2,3\}\), the splice consisting of the final \(4-k\) symbols of \(u\) followed by the initial \(k\) symbols of \(v\) is not \(w\). Repetitions among \(u,v,w\) are allowed. The minimum Hamming-distance requirement is imposed on distinct codewords only, and is vacuous at \(\delta=1\). Codes may contain words fixed by reverse complementation. The result concerns finite four-nucleotide block codebooks, without biochemical constraints.

## Proof
**Orbit reduction.** Exactly \(\binom42 2^4=96\) length-four nucleotide words have GC content two. Reverse complementation preserves this condition. Eight of the 96 words are fixed by \(\rho\), so they form \((96-8)/2+8=52\) orbits. A reverse-complement-closed code is therefore uniquely a union of these orbits, with orbit weights one or two.

**Forbidden supports.** For each ordered pair of orbits \(O_i,O_j\), choose \(u\in O_i,v\in O_j\) and \(k\in\{1,2,3\}\). Whenever the resulting splice \(s\) belongs to the 96-word universe, forbid simultaneously selecting the orbit of \(s\) and \(O_i,O_j\). This produces forbidden supports of cardinality one, two or three. Also forbid every one- or two-orbit support containing a pair of *distinct* codewords at Hamming distance less than \(\delta\). These constraints are necessary and sufficient: every failure of a defining condition has exactly such a witness, and every listed forbidden support exhibits a failure. Consequently the desired maximum is an exact maximum-weight subset avoiding a completely defined finite family of supports on 52 vertices.

**Exhaustive upper bounds and equality cases.** The accompanying `verify.py` generates these supports directly from the definitions, representing them as exact integer bitsets. Its `prove_no_larger` procedure searches all eligible orbit subsets, branching on inclusion and exclusion, rejecting incompatible pairs and completing forbidden triples as soon as their other two vertices are selected. A rigorously valid pruning bound partitions the remaining vertices into classes whose members are pairwise incompatible. Each feasible extension can take at most one vertex from each class, so the sum of maximum orbit weights in the classes is an upper bound for any extension. The branch recurrence removes only supports already proved infeasible or branches whose upper bound cannot exceed the tested target. It therefore proves the impossibility of attaining \(22,18,8\) words, respectively, with no probabilistic assumptions or floating-point tolerances.

The same exhaustive recurrence, with the bound adjusted to retain equality, generates *every* selected-orbit set of weights \(21,17,7\). It finds respectively \(136,16,72\) different labeled maxima. Every maximizing codebook is then separately checked against the direct word-level conditions, and the accompanying `optimal_codebooks.json` supplies the entire resulting list. Counting fixed words and applying all eight complement-preserving alphabet permutations directly to that complete list gives the asserted fixed-word and symmetry-class counts. These checks also establish attainability. One witness at each threshold is:

| Minimum distance | One optimal codebook (space-separated four-mers) |
|---|---|
| \(1\) | `AACC AACG AAGC AAGG ACAG ACCT ACGT ACTC ACTG AGGT CAGT CATC CATG CCTT CGTT CTGT GAGT GATC GATG GCTT GGTT` |
| \(2\) | `AACG AAGC ACAG ACCA ACTC ATCC CGTT CTAC CTGT GAGT GCTT GGAT GTAG GTCA TGAC TGCA TGGT` |
| \(3\) | `AACC ACAG AGGA CATG CTGT GGTT TCCT` |

## Verification
Place `verify.py` and `optimal_codebooks.json` in one directory and run `python3 verify.py` with Python 3.9 or later. The verifier reconstructs all 96 words and 52 reverse-complement orbits, independently regenerates the forbidden supports, checks each strict upper bound, recreates the full maximizer census and compares the fully reconstructed data structurally with the embedded JSON inventory. It then directly checks each maximizing codeword set against the original comma-free, GC-content, strand-closure and Hamming definitions, and recomputes the eight-permutation symmetry census. A successful execution ends with `VERIFY_OK`. A separate integer-programming search was used as a secondary finite optimum check, but the enumerator and its explicit upper-bound argument constitute the reproducible finite proof.

For the three distance requirements in order, the enumerator finds \(4668,4732,5174\) forbidden supports and respectively \(381,360,89\) branch nodes for the strict upper-bound proof. It enumerates equality cases with respectively \(1534,718,259\) nodes. All arithmetic in the standalone verifier is integer arithmetic.

## Relationship to prior work
Golomb, Gordon and Welch introduced and studied ordinary comma-free codes; Jiggs considered further unrestricted quaternary comma-free bounds. Their ambient unconstrained maxima and bounds do not identify the present GC-balanced, strand-closed, distance-constrained optimum. King studied constant-GC DNA codes with Hamming-distance and reverse-complement-*separation* requirements; that latter requirement demands positive distance between \(x\) and the reverse complement of \(y\) for all codewords \(x,y\), which is incompatible with reverse-complement *closure* of a nonempty code when applied to \(y=\rho(x)\). Thus King's reverse-complement separation results do not imply the closed-code classifications here. More restrictive non-overlapping codes (forbidding proper prefix/suffix matches), binary comma-free codes and deletion-correcting codes have different constraints and do not imply the claimed three-way threshold or maximizer census. The exact claim remains subject to ordinary historical-priority uncertainty regarding unindexed literature.

## Limitations
This is an exact exhaustive finite theorem for word length four only. Hamming distances \(2\) and \(3\) guarantee respectively detection and correction of one substitution only when word boundaries are known and the substitution channel is the standard framed Hamming channel. Comma-freeness alone does not prove recovery of boundaries under corruption. No claim is made for larger blocks, different GC fractions, insertion/deletion channels, chemical stability, or independent priority certification. The complete enumeration is reproducible by the included verifier but has not undergone independent scientific audit.

## References
1. S. W. Golomb, B. Gordon and L. R. Welch, “Comma-Free Codes,” *Canadian Journal of Mathematics* **10** (1958), 202–209. DOI: 10.4153/CJM-1958-023-9. https://doi.org/10.4153/CJM-1958-023-9
2. B. H. Jiggs, “Recent Results in Comma-Free Codes,” *Canadian Journal of Mathematics* **15** (1963), 178–187. DOI: 10.4153/CJM-1963-021-1. https://doi.org/10.4153/CJM-1963-021-1
3. O. D. King, “Bounds for DNA codes with constant GC-content,” arXiv:math/0306197 (first posted 2003-06-12). https://arxiv.org/abs/math/0306197
