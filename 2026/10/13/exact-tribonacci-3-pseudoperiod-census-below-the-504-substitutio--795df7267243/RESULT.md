# Exact Tribonacci 3-pseudoperiod census below the 504 substitution scale
## Finding
Let \(\mathbf t\) be the Tribonacci word, the fixed point beginning in \(0\) of
\[
0\mapsto 01,\qquad 1\mapsto 02,\qquad 2\mapsto 0.
\]
A triple \((a,b,c)\) with \(1\le a<b<c\) is a 3-pseudoperiod when every position \(i\ge0\) satisfies
\[
t_i\in\{t_{i+a},t_{i+b},t_{i+c}\}.
\]

Among all triples with largest shift \(c<504\), exactly \(9352\) are 3-pseudoperiods of \(\mathbf t\). Here \(504=|\sigma^{10}(0)|\) is the tenth canonical substitution length for the Tribonacci morphism.

At the successive substitution scales
\[
7,13,24,44,81,149,274,504,
\]
the numbers of 3-pseudoperiods with largest shift strictly below the scale are respectively
\[
0,2,9,42,172,676,2402,9352.
\]
The first nine triples, namely all those with \(c<24\), are
\[
\begin{aligned}
&(4,6,7),\ (6,7,11),\ (4,7,13),\ (7,11,13),\ (11,13,14),\\
&(6,7,17),\ (7,13,17),\ (6,11,20),\ (11,13,20).
\end{aligned}
\]
The complete list through \(c<504\) is supplied in `triples.tsv`.

## Assumptions and scope
The indexing convention is zero-based. The claim is a finite exact classification inside the open problem of characterizing all 3-pseudoperiods of the Tribonacci word. It does not assert a complete infinite characterization.

Write \(q_n=|\sigma^n(0)|\). Then
\[
(q_0,q_1,\ldots,q_{10})=(1,2,4,7,13,24,44,81,149,274,504).
\]
The cutoff \(504=q_{10}\) is therefore a canonical substitution scale, not an arbitrary numerical bound.

## Proof
Fix \(1\le a<b<c\). The pseudoperiod condition is local at factor length \(c+1\). It holds for every position of \(\mathbf t\) if and only if every factor
\[
x=x_0x_1\cdots x_c
\]
of length \(c+1\) satisfies
\[
x_0\in\{x_a,x_b,x_c\}.
\]
Indeed, the length-\((c+1)\) factor beginning at position \(i\) contains exactly the four symbols occurring in the defining condition at offsets \(0,a,b,c\).

The Tribonacci word has factor complexity
\[
p(m)=2m+1.
\]
Generate the prefix \(\sigma^{15}(0)\), of length \(10609\). For every \(1\le m\le504\), direct factor extraction from this prefix produces exactly \(2m+1\) distinct length-\(m\) factors. By the published factor-complexity theorem, these are therefore all length-\(m\) factors of the infinite word.

For each \(3\le c<504\), the complete length-\((c+1)\) factor set is then tested against every pair \(1\le a<b<c\). A triple is retained exactly when no factor disagrees with the origin symbol simultaneously at all three offsets. This exhausts every triple in the stated range and produces exactly \(9352\) survivors.

## Verification
Run `python3 verify.py` beside `certificate.json` and `triples.tsv`.

The verifier regenerates \(\sigma^{15}(0)\), checks the factor-complexity count \(2m+1\) separately for every \(1\le m\le504\), and recomputes the entire triple census with a mismatch-bitset predicate: a candidate survives exactly when the three mismatch-factor bitsets have empty intersection. This exhaustive computation reproduces the stored ordered list of \(9352\) triples. A second direct-string pass independently rechecks every stored survivor against every relevant factor.

The verifier also recomputes the cumulative counts at all listed substitution scales and the complete nine-triple layer with \(c<24\).

## Relationship to prior work
Meleshko, Ochem, Shallit, and Shan prove that the Tribonacci word is 3-pseudoperiodic but not 2-pseudoperiodic. Their explicit witness is \((4,6,7)\), which they verify by checking all factors of length \(8\). Immediately afterward they pose the problem of characterizing all 3-pseudoperiods of the Tribonacci word and explain that a direct automaton computation appeared beyond their available computational resources.

The present result does not solve that infinite characterization problem. It gives a complete certified initial region through a natural morphic scale, showing in particular that the published witness is only the first member of a rapidly growing finite family: there are \(9352\) valid triples before the largest shift reaches \(504\).

A separate earlier result establishes the usual factor complexity \(p(m)=2m+1\) for the Tribonacci word; that theorem is used only to certify that each finite factor list extracted during the census is exhaustive.

## Limitations
No automaton or closed-form description of all Tribonacci 3-pseudoperiods is claimed. The census stops strictly below \(504\), and triples with \(c\ge504\) are not classified.

The computation relies on the published factor-complexity theorem to turn finite-prefix factor extraction into an exhaustive factor list. The package independently checks the factor counts but does not reprove that theorem.

An unindexed computation or unpublished table could contain part or all of the same bounded census despite the targeted literature and database searches.

## References
1. J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, “Pseudoperiodic Words and a Question of Shevelev,” arXiv:2207.10171v1, first public version 2022-07-20; Discrete Mathematics & Theoretical Computer Science 25:2 (2023), DOI 10.46298/dmtcs.9919.
2. M. Lejeune, M. Rigo, and M. Rosenfeld, “Templates for the k-binomial complexity of the Tribonacci word,” Advances in Applied Mathematics 112 (2020), 101947, DOI 10.1016/j.aam.2019.101947.
