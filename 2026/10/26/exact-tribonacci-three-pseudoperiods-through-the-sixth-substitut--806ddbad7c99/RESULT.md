# Exact Tribonacci three-pseudoperiods through the sixth substitution scale

## Finding
Let \(T=t_0t_1\cdots\) be the infinite Tribonacci word, the fixed point beginning with \(0\) of the substitution \(\tau(0)=01,\ \tau(1)=02,\ \tau(2)=0\). Call integers \(1\le a<b<c\) a *three-pseudoperiod* when, for every integer \(i\ge0\), \(t_i\in\{t_{i+a},t_{i+b},t_{i+c}\}\).

**Theorem (complete finite initial classification).** Of the \(\binom{44}{3}=13{,}244\) triples satisfying \(1\le a<b<c\le44\), exactly **55** are three-pseudoperiods. All of them, without exception, are:

- Largest shift \(7\): \(4,6,7\).
- Largest shift \(11\): \(6,7,11\).
- Largest shift \(13\): \(4,7,13\), \(7,11,13\).
- Largest shift \(14\): \(11,13,14\).
- Largest shift \(17\): \(6,7,17\), \(7,13,17\).
- Largest shift \(20\): \(6,11,20\), \(11,13,20\).
- Largest shift \(24\): \(6,7,24\), \(6,20,24\), \(7,13,24\), \(13,14,24\), \(13,20,24\), \(19,20,24\).
- Largest shift \(26\): \(7,17,26\), \(7,24,26\), \(20,24,26\).
- Largest shift \(27\): \(11,13,27\), \(13,24,27\), \(24,26,27\).
- Largest shift \(30\): \(11,20,30\), \(20,24,30\).
- Largest shift \(31\): \(4,13,31\), \(11,13,31\), \(13,17,31\), \(13,24,31\).
- Largest shift \(37\): \(4,7,37\), \(7,11,37\), \(7,17,37\), \(7,24,37\), \(7,28,37\), \(7,35,37\), \(11,20,37\), \(11,27,37\), \(20,24,37\), \(24,27,37\).
- Largest shift \(38\): \(11,13,38\), \(13,24,38\).
- Largest shift \(41\): \(7,37,41\), \(13,31,41\).
- Largest shift \(43\): \(20,24,43\).
- Largest shift \(44\): \(6,11,44\), \(6,24,44\), \(11,13,44\), \(11,30,44\), \(11,37,44\), \(13,24,44\), \(19,24,44\), \(24,26,44\), \(24,30,44\), \(24,37,44\), \(24,43,44\), \(30,35,44\), \(35,37,44\).

In particular, the sole triple with \(c\le7\) is \(4,6,7\), already known; the next smallest possible largest shift is \(c=11\), uniquely attained by \(6,7,11\). The full sorted list is also in the bundled `census.json`.

## Assumptions and scope
The shifts are *positive distinct integers*, sorted increasingly, and the inequality must hold for **every position of the infinite word**, not only a finite prefix. The cutoff \(44\) is the length of \(\tau^6(0)\) (the sixth Tribonacci substitution scale): the lengths of successive iterates are \(1,2,4,7,13,24,44,81,\ldots\). This work concerns only the bounded region \(c\le44\); no characterization for all shifts is asserted.

## Proof
Put \(L=45\), \(W=\tau^9(0)\), and define \(S\) as the set of all contiguous length-\(L\) factors of \(W\). By nine direct substitution iterations, \(|W|=274\) and \(|S|=91\). The bundled finite certificate verifies the following **substitution-closure condition**: for every \(s\in S\), every length-\(L\) factor of \(\tau(s)\) belongs to \(S\).

To see why closure proves completeness for the *infinite* word, consider any \(v\) of length at least \(L\). Each length-\(L\) factor of \(\tau(v)\) is contained in \(\tau(s)\) for some length-\(L\) factor \(s\) of \(v\): a window of \(L\) output symbols crosses at most \(L\) input letters, since all substitution images are nonempty, and that input interval can be extended to \(L\) letters within \(v\). Therefore closure implies inductively that every length-\(L\) factor of \(\tau^k(W)\) lies in \(S\) for all \(k\ge0\). Every factor of \(S\) already occurs in the prefix \(W\) of the infinite fixed point, so \(S\) is exactly the set of *all* length-\(L\) factors of \(T\).

For a given \(a<b<c\le44\), its defining universal condition involves only positions from \(i\) through \(i+c\), hence is equivalent to the **finite exact test**

\[\forall s\in S:\quad s_0\in\{s_a,s_b,s_c\}.\]

The standalone `verify.py` exhaustively applies this test to all \(13{,}244\) candidate triples using the complete \(91\)-factor set; it obtains exactly the \(55\) listed above and independently compares them with direct tests of \(500\) consecutive starting positions in a longer substitution iterate. This is a finite, checkable certificate establishing the complete infinite-position statement, not an extrapolation from an observed prefix.

## Verification
Run `python3 verify.py` in the same directory as `census.json` with Python 3 standard library. The verifier (i) reconstructs \(W\) and its \(91\) length-\(45\) factors; (ii) checks the factors match the embedded data exactly; (iii) checks all substitution-image factor inclusions; (iv) enumerates every sorted triple with largest shift at most \(44\); (v) compares the \(55\) accepted triples against the embedded table; (vi) independently rechecks the conclusion on a longer prefix, and (vii) verifies an explicit violated factor exists for each rejected triple. Expected terminal line: `TRIBONACCI_PSEUDOPERIOD_CENSUS_PASS factors= 91 triples= 13244 valid= 55`.

## Relationship to prior work
Meleshko, Ochem, Shallit and Shan, *Pseudoperiodic Words and a Question of Shevelev* (first public 20 July 2022; arXiv:2207.10171), introduced and studied this formulation. Their Theorem 29 proves that the Tribonacci word is three-pseudoperiodic, giving \(4,6,7\), and their Open Problem 30 asks for all valid triples. They explicitly note the full automaton computation was out of reach. The present statement is deliberately a **finite initial classification**, not a solution of that open infinite problem. General decidability established in their work does not provide the explicit count of \(55\), the \(54\) additional positive triples, or this length-\(45\), \(91\)-factor closure certificate.

## Limitations
No statement is made about triples with largest shift greater than \(44\), about the eventual shape of the full set of triples, or about the computational complexity of full automaton determination. The finite classification depends on the exact definition of the Tribonacci morphism, zero-based indexing, and the stated three-pseudoperiod convention. The result has received no independent mathematical audit. Equivalent unpublished or differently indexed finite tables may exist.

## References
1. Joseph Meleshko, Pascal Ochem, Jeffrey Shallit, and Sonja Linghui Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171, first posted 20 July 2022, especially §4.5, Theorem 29 and Open Problem 30. https://arxiv.org/abs/2207.10171
2. The Electronic Journal/Discrete Mathematics & Theoretical Computer Science publication record, vol. 25:2, 2023, DOI 10.46298/dmtcs.9919. https://dmtcs.episciences.org/en/articles/9919
