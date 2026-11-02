# A rank-three coloured order with no optimal induced suborder

## Finding

There are two finite words over the alphabet \(\{r,b\}\) of respective lengths \(70\) and \(73\) that are equivalent in the three-round Ehrenfeucht–Fraïssé game, although **none** of the \(70\)-letter subsequences of the longer word is three-round equivalent to it. The \(70\)-letter word is shortest possible in its three-round equivalence class. Thus a finite two-coloured linear order need not contain an optimal induced suborder in its three-round equivalence class.

An explicit pair is obtained by concatenating the following three blocks (the bars in the display are separators, not letters):

```text
L  = rrrrrrbbbbbbrbbbbbr
M0 = rbrbrrbbbrbrbbrbbbbbrrrrrbrrrbbr
M  = rbrrrbbrbbbbbrbrrbrbrbbrrrrrbrrbbbr
R  = rbbbbbrbbbbbbrrrrrr

A = L | M0 | R
W = L | M  | R
```

The \(70\)-letter word \(A\) is the de Bruijn-based construction in Mwesigye–Truss (2017/2018); its optimality is independently checked here. The \(73\)-letter word \(W\) and its non-embedding obstruction are the new assertion. No minimality of \(73\) among all possible counterexamples is claimed.

## Assumptions and scope

A finite binary-coloured linear order is viewed as a word with its natural strict position order and two unary colour predicates. An *induced suborder* is obtained by deleting arbitrary positions, retaining the order of the remaining letters: it need not be a contiguous factor. The relation \(U\equiv_q V\) means that Duplicator wins the ordinary \(q\)-move Ehrenfeucht–Fraïssé game on these relational structures. An *optimal representative* has minimum word length among all members of its \(\equiv_q\)-class.

Only \(q=3\) and the displayed words are asserted. The statement is a finite logical counterexample, not an all-length structural classification.

## Proof

**Lemma (exact finite-word game fingerprint).** Let \(\Phi_0(U)\) be a constant symbol, and inductively define

\[
\Phi_q(U)=\{(\Phi_{q-1}(U_{<i}),\,U_i,\,\Phi_{q-1}(U_{>i})):1\le i\le |U|\},\quad q\ge1.
\]

The empty set is allowed. Then \(U\equiv_q V\) if and only if \(\Phi_q(U)=\Phi_q(V)\). For \(q=1\), the fingerprint is just the set of colours appearing in the word. Inductively, after the first move at position \(i\), Duplicator must answer with the same colour at a position \(j\). An order-preserving partial isomorphism can then be maintained for the remaining moves precisely when both the left intervals and both the right intervals are \((q-1)\)-equivalent. This is the standard first-move characterization, also stated as Theorem 1.1 by Mwesigye–Truss.

It follows that \(\Phi_2(U)\) is the set of triples consisting of the left colour-set, the colour at a position, and the right colour-set. Each such triple is encoded by one of \(32\) possible bits. For every position, the pair of \(32\)-bit fingerprints of its left and right subwords, together with its colour, gives an exact \(\Phi_3\)-character. Thus all the computations below use exact integer bit operations and exact set equality, without hashes as mathematical surrogates.

**Complete finite certificate.** The standalone program `verify_rank3.cpp`, supplied with this result, enumerates these \(\Phi_3\)-characters. Its exact checks establish:

\[
|A|=70,\quad |W|=73,\quad
|\Phi_3(A)|=|\Phi_3(W)|=70,\quad
\Phi_3(A)=\Phi_3(W).
\]

The \(70\) different characters in \(\Phi_3(A)\) force every equivalent word to have at least \(70\) positions, since each position can realize only one character. Hence \(A\) is optimal and \(W\equiv_3 A\).

Every \(70\)-position induced suborder of \(W\) is obtained by deleting exactly three of its \(73\) positions. The program exhaustively enumerates all

\[
\binom{73}{3}=62\,196
\]

triples of deleted positions, recomputes the full exact fingerprint of each remaining word \(V\), and verifies the stronger bound

\[
\max_{|V|=70,\ V\text{ induced in }W}
|\Phi_3(V)\cap\Phi_3(A)|=68<70.
\]

Thus none of these induced suborders is three-round equivalent to \(A\) or \(W\). As every optimal representative of the common class has exactly \(70\) positions, \(W\) contains no optimal induced suborder. This proves the claim.

## Verification

From the directory containing the two supplied source files, run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verify_rank3.cpp -o verify_rank3
./verify_rank3
python3 verify_independent.py
```

The exhaustive C++ computation returns `CHECKED=62196`, `EQUIVALENT_70_SUBSEQUENCES=0`, `MAX_REFERENCE_TYPES_PRESENT=68`, and `RANK3_NO_OPTIMAL_SUBSEQUENCE_PASS`. The independently written Python implementation checks the two displayed fingerprints using direct finite sets, tests the fingerprint/game equivalence on all \(961\) pairs of binary words of length at most four, and checks \(1203\) deterministically sampled deletion triples. Sampling is corroboration only; the exhaustive certificate is the C++ check over every deletion triple.

## Relationship to prior work

Mwesigye and Truss proved that an optimal two-round representative can always be found as an induced suborder and, in their subsequent work, suggested this fails in three rounds. Their paper provides the \(70\)-letter optimal word used above and a separate \(74\)-letter optimal example, but gives no explicit word without an optimal three-equivalent induced suborder. The present \(73\)-letter construction confirms that stated expectation with a finite, fully checkable counterexample. The first-move fingerprint lemma and the original \(70\)-letter construction are credited prior work, not claimed as new.

## Limitations

The computation establishes no smallest possible counterexample length, no general characterization of all three-equivalence classes, and no analogous assertion for more colours or more rounds. Independent mathematical review and exhaustive historical-priority checking beyond the identified primary and related records have not been performed. The source paper's oldest verified public preprint is dated 12 May 2017; its journal version appeared online on 2 May 2018 and in the 2019 volume.

## References

1. F. Mwesigye and J. K. Truss, *On optimal representatives of finite coloured linear orders*, arXiv:1705.04632, first version 12 May 2017; *Order* 36 (2019), 107–117, DOI 10.1007/s11083-018-9458-3. See Theorem 1.1, the \(70\)-letter construction in Section 3, and the final paragraph of Future Work.
2. F. Mwesigye and J. K. Truss, *Classification of finite coloured linear orderings*, *Order* 28 (2011), 387–397. The cited prior framework establishes general finite-class bounds and the earlier two-round setting.
