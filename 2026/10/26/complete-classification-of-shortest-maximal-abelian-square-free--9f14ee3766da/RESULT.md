# Complete classification of shortest maximal Abelian-square-free words on five letters

## Finding

Let \(\Sigma=\{0,1,2,3,4\}\). A word is *Abelian-square-free* when no nonempty factor has the form \(UV\) with \(|U|=|V|\) and identical symbol-count vectors. A word is *maximal* when adjoining any letter of \(\Sigma\) on either side creates an Abelian square.

**Theorem.** The minimum length of a maximal Abelian-square-free word over \(\Sigma\) is exactly \(16\). There are exactly \(480\) such labeled words. Modulo simultaneous permutation of the alphabet, precisely the following four first-occurrence-canonical words occur:

```
0102134031201343
0102134031210343
0102342031024323
0102343021034232
```

The first and third words are paired by reversal followed by first-occurrence canonicalization, as are the second and fourth. Thus there are exactly two classes after allowing both alphabet relabeling and reversal. Every word above uses all five letters, so each first-occurrence class consists of exactly \(5!=120\) labeled words.

## Assumptions and scope

The alphabet consists of five *distinct* symbols; positions and symbol identities matter when counting labeled words. There is no cyclic wraparound. A forbidden factor may have any even positive length, and its two halves need only be permutations, not identical strings. A maximal word is blocked on **both** sides, a stronger condition than being right-crucial. The classification covers all words of every length at most \(16\), without a restriction to particular symbol-frequency profiles.

For any word \(w=w_1\cdots w_n\), its Parikh vector \(\Psi(w)\) records the multiplicities of the five alphabet symbols. An *Abelian square* is a factor \(w_i\cdots w_{i+2h-1}\) with \(h\ge1\) for which its first \(h\) symbols and last \(h\) symbols have equal Parikh vectors.

## Proof

**Lemma 1 (full support).** Every maximal Abelian-square-free word uses every alphabet letter. Indeed, adjoining a previously unused letter would produce an Abelian-square-free word: any newly introduced square would contain the new letter only once, whereas each symbol occurs an even number of times in an Abelian square. Therefore a candidate may be normalized by its order of first symbol appearances.

**Lemma 2 (canonical enumeration).** Relabel the first symbol of a nonempty word \(0\), its next unseen symbol \(1\), and so on. Every orbit of words under permutation of the five symbols contains exactly one such canonical representative. A canonical word starting with \(0\), currently having seen \(0,\ldots,m\), may next use only a symbol in \(\{0,\ldots,\min(4,m+1)\}\). Every valid canonical word is generated uniquely by this recursion.

**Lemma 3 (sound pruning).** If a word \(v\) is Abelian-square-free, extending it to \(vc\) creates an Abelian square if and only if an Abelian square ends at the new last position: every factor not ending there was already a factor of \(v\). For the candidate word of length \(n\), this can be checked for every \(1\le h\le\lfloor n/2\rfloor\) by comparing the Parikh vectors of its final two adjacent blocks of length \(h\). Consequently, discarding exactly the extensions with such a square never excludes an Abelian-square-free descendant.

**Lemma 4 (terminal tests).** In an Abelian-square-free word, a forbidden factor introduced by prepending a symbol must start at the first position. Thus a canonical full-support word \(v\) is maximal if and only if, for every \(c\in\Sigma\), the word \(cv\) has an Abelian-square prefix and \(vc\) has an Abelian-square suffix. The comparisons in `verify.cpp` perform exactly these tests by direct integer frequency differences, without numerical approximation.

**Finite exhaustive step.** Begin at \(v=0\) and apply Lemmas 2 and 3 to every canonical Abelian-square-free prefix of length at most \(16\). At each node with full alphabet support, apply Lemma 4. The standalone exhaustive implementation in `verify.cpp` checks all admissible next letters without heuristic filtering, using integer arithmetic and loops covering every possible block length. The number of canonical Abelian-square-free prefixes of lengths \(13,14,15,16\), respectively, is

\[
209190,\quad 690853,\quad 2278400,\quad 7421303.
\]

The exact numbers of two-sided maximal words among canonical full-support words at lengths \(1\) through \(16\) are zero at every length \(1\) through \(15\), and **four** at length \(16\). The complete four-word output is precisely the displayed list. This is an exhaustive *finite* proof because the bound \(16\) is fixed and the recursion and terminal predicates are proved equivalent to the definitions; it does not extrapolate from sampled words.

Finally, every canonical maximal word uses all five distinct symbols, so relabeling it yields \(5!\) distinct labeled words. Canonical representatives are unique, hence the four disjoint orbits give \(4\cdot120=480\). Reversing and renormalizing the representatives pairs them exactly as stated. This completes the proof.

## Verification

Compile the attached independent direct-Parikh exhaustive checker with a conforming C++17 compiler:

```
c++ -std=c++17 -O2 verify.cpp -o verify
./verify
```

The checker must print `VERIFY_OK length=16 canonical_count=4 labeled_count=480` and the four displayed representatives. It asserts the full search counts and absence of any shorter maximal word. `witnesses.csv` lists every representative, its normalized reversal, and explicit Abelian-square half-length witnesses for all five possible left and right extensions. For each listed word, the two half-block symbol multisets can also be directly compared using the definition. A separately implemented packed-Parikh recursion corroborated the same canonical counts and representatives, while the distributed checker uses five separate integer differences for each tested half length.

## Relationship to prior work

Cummings and Mays, *A One-Sided Zimin Construction* (2001), introduced a construction of shorter maximal Abelian-square-free words and exhaustively determined that the four-letter minimum is \(11\), with three relabeling classes; their five-letter construction gives a word of length \(19\) but not this length-\(16\) classification. Korn, *Maximal Abelian Square-Free Words of Short Length* (2003), gives general upper bounds by another construction. Bullock, *Improved Bounds on the Length of Maximal Abelian Square-Free Words* (2004), improves bounds for larger alphabets. Glen, Halldórsson, and Kitaev, *Crucial Words for Abelian Powers* (2009), address one-sided cruciality and discuss two-sided minimal words as a separate problem. In the accessible source material these works do not supply the four-orbit five-letter classification or the exact total \(480\).

## Limitations

The theorem is specific to a five-symbol alphabet and two-sided maximality. The finite exhaustive proof establishes no formula or algorithmic complexity improvement for arbitrary alphabet size. The full text of Korn (2003) could not be inspected, so a historical-priority overlap cannot be ruled out; neither the absence of a matching database result nor an inaccessible article proves novelty. Reproducibility depends on ordinary execution of the included independent checker or independently repeating the finite enumeration. No independent external mathematical audit is claimed.

## References

1. L. J. Cummings and M. Mays, *A One-Sided Zimin Construction*, Electronic Journal of Combinatorics **8** (2001), R27. DOI: `10.37236/1571` (first available July 23, 2001).
2. M. Korn, *Maximal Abelian Square-Free Words of Short Length*, Journal of Combinatorial Theory, Series A **102** (2003), 207–211. DOI: `10.1016/S0097-3165(03)00016-5`.
3. E. M. Bullock, *Improved Bounds on the Length of Maximal Abelian Square-Free Words*, Electronic Journal of Combinatorics **11** (2004), R17. DOI: `10.37236/1770`.
4. A. Glen, B. V. Halldórsson, and S. Kitaev, *Crucial Words for Abelian Powers* (2009), open-access manuscript: `https://spider-v.science.strath.ac.uk/sergey.kitaev/Papers/dlt2009.pdf`.
