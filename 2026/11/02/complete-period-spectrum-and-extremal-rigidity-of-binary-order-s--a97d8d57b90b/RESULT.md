# Complete period spectrum and extremal rigidity of binary order-seven orientable necklaces

## Finding
Let \(\mathcal O_7\) consist of cyclic binary words in which the seven-letter windows, read in either direction, are all pairwise distinct. Words differing only by a cyclic rotation are identified. If \(c_7(\ell)\) denotes the number of rotational classes of length \(\ell\), then the following is the **complete** nonzero spectrum:

| \(\ell\) | \(c_7(\ell)\) | \(\ell\) | \(c_7(\ell)\) | \(\ell\) | \(c_7(\ell)\) |
|---:|---:|---:|---:|---:|---:|
| 6 | 2 | 16 | 44 | 26 | 268 |
| 7 | 4 | 17 | 48 | 27 | 248 |
| 8 | 12 | 18 | 78 | 28 | 444 |
| 9 | 12 | 19 | 100 | 29 | 224 |
| 10 | 12 | 20 | 138 | 30 | 656 |
| 11 | 12 | 21 | 144 | 31 | 0 |
| 12 | 20 | 22 | 160 | 32 | 352 |
| 13 | 24 | 23 | 168 | 33 | 352 |
| 14 | 22 | 24 | 232 | 34 | 448 |
| 15 | 28 | 25 | 200 | 35 | 0 |
| | | | | 36 | 336 |

All other lengths have count zero. Thus there are exactly \(4788\) cyclic classes, and exactly \(336\) have the known maximum length \(36\).

Every maximum-length necklace has **exactly 18 ones, 20 cyclic runs**, and the same complete cyclic three-window frequency profile:
\[
\#000=\#111=3,\qquad \#001=\#010=\#011=\#100=\#101=\#110=5.
\]
Under reversal and simultaneous exchange of the two symbols, the \(336\) maximum-length necklaces split into exactly \(90\) symmetry classes: \(78\) orbits of size \(4\) and \(12\) orbits of size \(2\). Exactly \(24\) of the maximum necklaces are invariant, up to rotation, under combined reversal-complementation; none is invariant under reversal or complementation separately.

## Assumptions and scope
A *cyclic word* \(w=w_0\cdots w_{\ell-1}\) has positions read modulo \(\ell\). Its length-seven cyclic window at \(i\) is \(u_i=w_iw_{i+1}\cdots w_{i+6}\). It is *orientable of order seven* if the \(2\ell\) words
\(u_0,\ldots,u_{\ell-1},u_0^R,\ldots,u_{\ell-1}^R\) are all distinct. Thus palindromic seven-windows are forbidden and each nonpalindromic reversal pair contributes at most one window. A necklace is a rotation class, represented by its lexicographically least rotation. Cyclic runs are positions \(i\) with \(w_i\ne w_{i-1}\). A cyclic three-window frequency counts starting indices, including wraparound. No assumption about Hamming weight is imposed.

## Proof
**1. Finite state reduction.** Represent a seven-window \(e\) as an edge of the binary de Bruijn digraph from its length-six prefix \(p(e)\) to its length-six suffix \(s(e)\). There are exactly \(16\) palindromic binary seven-words, leaving \((128-16)/2=56\) nonpalindromic reversal pairs. The cyclic windows of any order-seven orientable word form a directed closed trail, using no palindrome and no more than one edge from each reversal pair. Conversely, every nonempty directed closed trail satisfying these restrictions spells an orientable cyclic word: consecutive edges overlap in six symbols, and the last symbols of the edges recover the cyclic word. The pair constraint makes all edge labels distinct, so the resulting cyclic word is primitive. Therefore its length cannot exceed \(56\).

**2. Exhaustive recurrence.** Let \(v\) be the present six-bit vertex, \(a\) the initial vertex, \(S\) the 56-bit mask of used reversal pairs, and \(b\) the word of trailing edge symbols. For each bit \(d\in\{0,1\}\), form the edge \(e=2v+d\). Discard it if palindromic or its reversal pair is in \(S\); otherwise pass to \(v'=e\bmod64\), append \(d\), and set its mask bit. Whenever \(v'=a\), record the lexicographically least cyclic rotation of the newly spelled word, *and continue extending*: an Eulerian closed trail may revisit its initial vertex. Start from every one of the \(64\) six-bit vertices with the empty mask and empty word. Each recursion strictly increases the number of set bits, so the enumeration is finite. It omits no permissible closed trail because every edge of a permissible trail survives precisely the stated tests. Canonical rotation eliminates all repetitions from different starting positions. Applying this exact integer recurrence yields the table and \(4788\) classes in total. In particular, no admissible cycle of length greater than \(36\) occurs.

**3. Extremal profiles and symmetries.** The exhaustive certificate includes every one of the \(336\) length-36 necklaces, each in its smallest rotation. Direct cyclic window counts on each certificate word yield the stated weight, run count and three-window profile. For every maximum necklace \([w]\), compute the four images represented by \([w]\), \([w^R]\), \([\overline w]\), and \([\overline{w}^R]\). The exact orbit census gives \(78\) orbits of size four and \(12\) of size two, and the fixed-class counts for reversal, complementation and their product are \(0,0,24\). Burnside's identity verifies \((336+0+0+24)/4=90\).

## Verification
Run `python3 code/check.py` from any directory. It uses only Python's standard library, independently recomputes all cyclic classes (including shorter periods), validates every listed extremal necklace, and checks the complete spectrum and symmetry counts. The recorded run visited \(6{,}355{,}050\) recursive states and obtained `CHECK_OK`.

An independently implemented C++17 search fixes the least numerical seven-window before extending a cycle; this avoids the other implementation's vertex-root duplication. Compile with `g++ -O2 -std=c++17 code/check_cpp.cpp -o check_cpp`, and run `./check_cpp certificates/maximum_necklaces.txt`. It visited \(766{,}602\) states and independently agreed on all \(29\) nonzero period counts and the exact \(336\)-word certificate. The certificate's SHA-256 is `e0838ac18297e49a77632d2017f8cee1d40359f65a6db4bec60bfab6b650432b`. The recorded scientific check outputs `certificates/python-check-output.txt` and `certificates/cpp-check-output.txt` document the executions; the source code and exhaustive enumeration, rather than the outputs alone, provide the finite proof.

## Relationship to prior work
Mitchell's *Searching for binary orientable sequences* (first public version October 24, 2026, arXiv:2610.33601v1) gives the exact maximum periodic length \(36\) at order seven and one example (Section 5.2, Table 5). It separately gives counts of **aperiodic** maximum-length strings at orders four through seven (Section 4.1). The latter counts are not counts of cyclic orientable necklaces: cyclic closure and rotation identification are extra restrictions. The source does not state the period-refined cyclic census or the extremal weight, run and three-window rigidity.

Gabrić and Sawada, *Efficient Construction of Long Orientable Sequences* (CPM 2024, DOI:10.4230/LIPIcs.CPM.2024.15), supplies constructions and bounds for the same object, including an order-seven example of period \(36\), but not this exact census. The present result counts and classifies admissible cycles; it does not claim discovery of the maximum period or the existence of order-seven orientable sequences.

## Limitations
The census and rigidity assertions are finite exact results **only for binary order seven**. They are proved by reproducible exhaustive enumeration, not a symbolic formula for arbitrary order. They do not classify order eight or larger, and do not assert a general periodic-count asymptotic. Earlier sources not fully accessible, in particular the 1993 original *Orientable Sequences*, leave a residual risk of an unindexed equivalent enumeration. Independent mathematical audit has not been performed.

## References
1. C. J. Mitchell, *Searching for binary orientable sequences*, arXiv:2610.33601v1, first public October 24, 2026. https://arxiv.org/abs/2610.33601
2. D. Gabrić and J. Sawada, *Efficient Construction of Long Orientable Sequences*, Proceedings of CPM 2024, LIPIcs 296, 15:1–15:12, DOI:10.4230/LIPIcs.CPM.2024.15. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2024.15
3. Z. D. Dai, K. M. Martin, M. J. B. Robshaw and P. R. Wild, *Orientable Sequences*, Cryptography and Coding III, pp. 97–115, 1993 (bibliographic reference; full text not inspected).
