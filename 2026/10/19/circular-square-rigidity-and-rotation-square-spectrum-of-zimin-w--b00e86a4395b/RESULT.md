# Circular-square rigidity and rotation-square spectrum of Zimin words

## Finding
Let \(Z_1=1\), \(Z_n=Z_{n-1}\,n\,Z_{n-1}\) for every \(n\ge2\), and let \(N_n=2^n-1\). The alphabet has a different letter for each positive integer. A circular factor of \(Z_n\) begins at one of its \(N_n\) zero-based positions and has length at most \(N_n\); it is read from the periodic word \(Z_nZ_n\). A *square* is a nonempty factor \(XX\) with half-length \(p=|X|\), so \(2p\le N_n\).

**Theorem (complete cyclic-square and rotation spectrum).** For every \(n\ge2\), the complete set of cyclic-square occurrences, expressed as (zero-based starting position, half-length), is
\[
\left\{\left(N_n-(2^k-1),\,2^k-1\right):1\le k<n\right\}.
\]
Each corresponding square is literally \(Z_kZ_k\). There are exactly \(n-1\) occurrences and \(n-1\) distinct square factors. For \(n=1\) there are none. No circular factor of length at most \(N_n\) is a fractional power of exponent strictly greater than \(2\).

For each rotation \(\rho_c(Z_n)=Z_n[c:]Z_n[:c]\), with \(0\le c<N_n\), let \(q_n(c)\) be its number of ordinary linear-square occurrences, counted by starting position and half-length. They are all distinct factors. Exactly **one** rotation has \(q_n(c)=0\): the unrotated word \(c=0\). For \(n\ge2\), exactly \(2^{j+1}\) rotations have \(q_n(c)=j\) for each \(1\le j\le n-2\), and exactly **two** rotations have \(q_n(c)=n-1\). No other values occur. For \(n=1\), the unique rotation has zero squares.

## Assumptions and scope
The definition of circular factor allows wraparound but never repeats a position more than once: \(1\le\ell\le N_n\). Linear squares in a rotation are wholly contained in the rotated finite word. The words \(Z_n\) are primitive because their largest letter \(n\) occurs exactly once, so their \(N_n\) rotations are distinct. The theorem concerns exact factor equality, not Abelian or approximate squares. The assertion on exponent excludes factors whose period \(p\) gives length \(>2p\), including integral cubes.

## Proof
**Lemma 1: each finite Zimin word is linearly squarefree.** Induct on \(n\). The assertion is immediate for \(Z_1=1\). In \(Z_n=U\,n\,U\), with \(U=Z_{n-1}\), a linear square containing the unique letter \(n\) would need that letter to appear in both identical halves, impossible. Every square avoiding \(n\) would lie entirely in one of the two copies of \(U\), contradicting the induction hypothesis.

**Lemma 2: exact squares of the doubled linear word.** Set \(a=|Z_m|\). In the \(2|Z_m|\)-letter linear word \(T_m=Z_mZ_m\), every square occurrence is one of
\[
\bigl(|Z_m|-(2^k-1),\,2^k-1\bigr),\qquad 1\le k\le m,
\]
where the first coordinate is its zero-based start; there is exactly one such occurrence per \(k\). The base case is \(T_1=11\), with one square at start \(0\), half-length \(1\). Write \(Z_m=U\,m\,U\) for \(m\ge2\) and \(a=|U|\). Then
\[
T_m=U\,m\,U\,U\,m\,U.
\]
The letter \(m\) occurs precisely at positions \(a\) and \(a+|Z_m|\). A square containing \(m\) needs two equal-offset copies of \(m\), hence its half-length is exactly \(|Z_m|\). By its total length it must be all of \(T_m\), starting at \(0\). Every square avoiding \(m\) lies inside one of the three maximal \(m\)-free regions \(U\), \(UU\), \(U\). Lemma 1 excludes the outer regions. The central \(UU=T_{m-1}\) begins at position \(a+1\); inductively its squares start at relative positions \(a-(2^k-1)\) for \(1\le k<m\). Consequently their absolute starts are \(2a+1-(2^k-1)=|Z_m|-(2^k-1)\), as required. There are no unaccounted squares.

**Circular-square classification.** For \(n\ge2\), the unique letter \(n\) cannot belong to any length-at-most-\(N_n\) circular square: identical halves would each contain it, but the circular factor never visits its single position twice. Starting immediately after that letter, the entire remaining circular arc is \(Z_{n-1}Z_{n-1}\), of length \(N_n-1\). Lemma 2 with \(m=n-1\) enumerates every square in this arc. Translating its start \(|Z_{n-1}|-(2^k-1)\) to the original circular positions gives \(N_n-(2^k-1)\). Thus the listed \(n-1\) squares exhaust all possibilities, and each is \(Z_kZ_k\).

**No proper fractional-power extensions.** A square \(Z_kZ_k\) begins at circular position \(N_n-L_k\), with \(L_k=2^k-1\). Its next circular symbol is the position \(L_k\) in zero-based indexing, which equals \(k+1\), whereas its first symbol is \(1\). Hence no such square extends one more symbol preserving period \(L_k\). Any circular factor with exponent strictly larger than \(2\) would have a square prefix and at least one period-preserving extension, contradiction. This is also true for \(n=1\), when no square exists.

**Complete rotation histogram.** Fix \(1\le k<n\) and write \(L_k=2^k-1\). The associated circular square occupies the wrapped interval starting at \(N_n-L_k\) and continuing for \(2L_k\) positions. It is a wholly linear factor of the rotation cut at position \(c\) exactly when the cut falls in the (inclusive) interval
\[
L_k\le c\le N_n-L_k.
\]
These integer intervals are nested as \(k\) increases. The interval for \(k=1\) is \([1,N_n-1]\), so \(c=0\) is the unique squarefree cut. For \(1\le j\le n-1\), the number of cuts retaining at least \(j\) squares is \(N_n-2L_j+1\). For \(1\le j\le n-2\), subtract the corresponding count for \(j+1\):
\[
\bigl(N_n-2L_j+1\bigr)-\bigl(N_n-2L_{j+1}+1\bigr)=2^{j+1}.
\]
For \(j=n-1\), the number is \(N_n-2L_{n-1}+1=2\). The counts sum to \(N_n\). Since each cyclic square is unique, counting surviving occurrences also counts distinct squares in a rotation. This proves all claims. \(\square\)

## Verification
Run `python3 verify.py` using Python 3 and the standard library; no third-party packages, datasets, or network access are needed. The checker independently constructs the words using the defining recursion and the two-adic ruler formula, enumerates every circular-square start and half-length for orders \(1\) through \(11\), checks the no-extension property, directly searches squares in all \(502\) rotations through order \(8\), and compares their complete histograms with the theorem. Its successful output is:

`VERIFY_OK cyclic_square_levels=1..11 cyclic_square_occurrences=55 independently_scanned_conjugates_levels=1..8_count=502 linear_square_histogram_exact=1..8 no_proper_circular_power_above_exponent_2=1..11 recursive_equals_ruler=1..11`

The computation tests finite instances; the induction and circular-cut argument establish the theorem for every order.

## Relationship to prior work
Cummings and Mays, *A One-Sided Zimin Construction* (Electronic Journal of Combinatorics 8, 2001, article R27; DOI:10.37236/1571), explicitly state and prove linear Zimin squarefreeness and maximal Abelian squarefreeness; those are prior results, not the proposed discovery. Their inspected sections on the recursion and modified one-sided words do not address the exact circular-square spectrum or the histogram of every cyclic cut. Głowinski and Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words* (arXiv:1307.1560, public 2013-07-05), provide historical Zimin-word context; only title, abstract and bibliographic description were available for inspection, so possible overlap in the inaccessible full paper is a residual risk. Rytter and Shur, *On Searching Zimin Patterns* (arXiv:1409.8235, public 2014-09-29), analyze occurrence and containment of Zimin patterns, not the present exact circular-square and cut histogram. Amit and Gawrychowski, *Distinct Squares in Circular Words* (arXiv:1708.00639), derive general extremal bounds on circular-square counts, not the complete spectrum for these recursively constructed words. Clokie, Gabrić, and Shallit, *Circularly Squarefree Words and Unbordered Conjugates: A New Approach* (arXiv:1904.08187), treat circular squarefreeness and unbordered conjugates for other word families. None of the materially inspected results yields the specific all-order occurrence and rotation-distribution theorem, but absence of an earlier equivalent is not certified.

## Limitations
The theorem is for the specific recursive words \(Z_n\) and for factors of length at most one circular period. The rotation histogram concerns exact (not Abelian) squares. It gives no estimate for arbitrary words, infinite words, or repetitions longer than a circular traversal. The claim of historical originality depends on the available primary sources and mathematical-record searches; an earlier unindexed equivalent or a result in inaccessible material is possible. Computational checks are not a substitute for the mathematical proof.

## References
1. L. J. Cummings and M. Mays, *A One-Sided Zimin Construction*, The Electronic Journal of Combinatorics 8 (2001), #R27, first publicly published 2001-07-23, https://doi.org/10.37236/1571.
2. R. Głowinski and W. Rytter, *Compressed Pattern-Matching with Ranked Variables in Zimin Words*, arXiv:1307.1560 (first public posting 2013-07-05), https://arxiv.org/abs/1307.1560.
3. W. Rytter and A. Shur, *On Searching Zimin Patterns*, arXiv:1409.8235 (first public posting 2014-09-29), https://arxiv.org/abs/1409.8235.
4. M. Amit and P. Gawrychowski, *Distinct Squares in Circular Words*, arXiv:1708.00639 (2017), https://arxiv.org/abs/1708.00639.
5. T. Clokie, D. Gabrić and J. Shallit, *Circularly Squarefree Words and Unbordered Conjugates: A New Approach*, arXiv:1904.08187 (2019), https://arxiv.org/abs/1904.08187.
