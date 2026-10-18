# Closed-factor rigidity of binary de Bruijn cycles

## Finding
Let \(h\geq 1\), and let \(B\) be any binary de Bruijn cycle of order \(h\), of circumference \(N=2^h\). Count **distinct, nonempty, closed circular factors** of lengths between \(1\) and \(N\), inclusive; denote their number by \(C(B)\). Then
\[
 N\leq C(B)\leq 2+(h-1)N.
\]
At order \(h=5\), the exact complete distribution over the \(2048\) rotation classes of binary de Bruijn cycles is:

| \(C(B)\) | Number of cycles |
| ---: | ---: |
| 93 | 360 |
| 94 | 888 |
| 95 | 600 |
| 96 | 200 |
| **Total** | **2048** |

No other value occurs. For a cycle chosen uniformly among the \(2048\) rotation classes, the mean is \(1509/16\), and the variance is \(195/256\). In particular, the complete order-five family has a closed-factor count varying by only three, although its members are distinct universal cycles.

## Assumptions and scope
A binary de Bruijn cycle of order \(h\) is a circular word in which each binary word of length \(h\) occurs exactly once as a cyclic factor. Every cyclic position is counted modulo \(N=2^h\); a circular factor has a specified start and a length \(1\leq \ell\leq N\). Distinct factors are distinguished by their letter sequences, not by their starting positions. A nonempty word is *closed* if it has length one, or else has a nonempty proper border occurring exactly twice in the word, once as prefix and once as suffix, with overlapping occurrences allowed. The empty word is excluded from \(C(B)\); including it adds exactly one to every reported count.

The general bound holds for every order \(h\geq1\). The distribution, extrema, and moments are asserted only for order five. The classification is of cycles modulo rotation, not of rooted linear cuts.

## Proof
**General structural bound.** Choose any linear cut of \(B\). Every linear word of length \(N\) contains at least \(N\) distinct nonempty closed factors. For completeness, at each final position choose a longest closed suffix of the prefix ending there. If it had occurred earlier, the factor running from its latest earlier occurrence to the current occurrence would be a strictly longer complete first return, a contradiction; thus a new closed factor appears at every position. Each such linear factor is also a circular factor of \(B\), proving the lower bound.

Consider a closed circular factor \(w\) with \(|w|\geq2\). It has a nonempty border \(u\). If \(|u|\geq h\), the first \(h\) letters of \(u\) occur at the prefix and suffix starts of \(w\); these are different cyclic positions, since their positive displacement is less than \(|w|\leq N\). This contradicts order-\(h\) de Bruijn uniqueness. Thus every border of \(w\) has length \(1\leq b<h\). Fix a circular starting position \(i\) and one such \(b\). At most one closed factor starting at \(i\) can be the complete first return to its first \(b\) letters: its suffix must begin at the earliest later start of that same \(b\)-letter factor. The \(N(h-1)\) pairs \((i,b)\), plus the two single-letter factors, therefore cover all distinct closed factors. This proves the upper bound.

**Complete finite order-five proof.** Use the directed binary de Bruijn graph whose vertices are the 16 four-bit words and edges are the 32 five-bit words. Each vertex has two incoming and two outgoing edges. Every Eulerian circuit pairs its two incoming edges bijectively with its two outgoing edges; each vertex has exactly two possible pairings. Consequently all Eulerian circuits occur among the \(2^{16}=65536\) binary pairing assignments. For any assignment, following the successor of each edge gives a permutation on the 32 edges. It defines one de Bruijn cycle precisely when that permutation consists of one 32-cycle. Fixing the unique edge `00000` first gives one representative of every rotation class without duplication. Exact enumeration yields 2048 accepted assignments.

For each resulting circular word, enumerate cyclic factors at every length \(1\) to \(32\). At lengths at most five there are all \(2^\ell\) binary factors and duplicates across positions must be discarded. At greater lengths all 32 factors are different, because equality would imply equality of their starting five-letter factors. To recognize a closed factor, inspect its proper borders and count (possibly overlapping) occurrences of each border; a factor is closed if and only if some nonempty border occurs exactly twice, or it is a singleton. This finite algorithm gives the four counts and their multiplicities in the table. It is exhaustive by the established pairing bijection and factor enumeration.

A second complete circuit construction enumerates edge-simple closed walks directly, starting with `00000`. It produces exactly the same 2048 representative words. The independently implemented border-occurrence predicate agrees on all circular factors with a longest-border predicate, and a third algorithm directly constructs all complete first returns to circular factors of lengths one through four. Their complete distributions coincide. The exact moment formulas follow by summing the four weighted cells; in particular \(\sum_B C(B)/2048=1509/16\) and \(\sum_B(C(B)-1509/16)^2/2048=195/256\).

## Verification
The standalone `verify.py` runs without external dependencies using Python 3: `python3 verify.py`. It checks all 65536 edge-pairing assignments, independently generates all circuits by Eulerian depth-first search, asserts equality of their full canonical word sets, and checks the defining five-factor uniqueness for every accepted cycle. For each of the 2048 cycles it independently computes the closed-factor count by two border methods and by enumerating first returns. The program asserts the exact histogram and rational moments, terminating with `VERIFY_OK` only if every check succeeds. Direct execution produced:

```
VERIFY_OK order5_cycles=2048 local_pairing_assignments=65536 independent_euler_enumeration=2048 identical_complete_sets=2048 independent_closed_predicates=2 independent_first_return_enumeration=2048 circular_nonempty_closed_factor_spectrum=93:360,94:888,95:600,96:200 mean=1509/16 variance=195/256
```

## Relationship to prior work
Badkobeh, Fici, and Lipták study the general count of closed factors in linear words, prove the linear lower bound, and characterize closed-poor words [1]. Parshina and Puzynina establish the asymptotic extremal number of closed factors for unrestricted words and use powers of de Bruijn words as a construction [2]. The latter work also defines closed factors of circular words, so the circular interpretation used here follows that established convention. Neither inspected work gives an order-five census over *single primitive binary de Bruijn cycles* or the stated all-order upper bound exploiting universal uniqueness of length-\(h\) factors. Published exact binary closed-rich maxima at lengths 25–27 concern unrestricted rooted binary words, not this circular de Bruijn family.

## Limitations
The exact four-cell distribution is finite and says nothing by itself about orders six or greater. The general upper bound need not be sharp. The finite computations are a complete proof only because the two enumeration methods are accompanied by explicit exhaustion and factor-recognition arguments; computation alone is not a proof of a theorem for arbitrary order. The literature comparison is not a certification of historical priority, and an unindexed equivalent result remains possible. No independent audit has been performed.

## References
[1] G. Badkobeh, G. Fici, and Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395, first public version 28 May 2013. https://arxiv.org/abs/1305.6395

[2] O. Parshina and S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863, first public version 1 November 2021. https://arxiv.org/abs/2111.00863
