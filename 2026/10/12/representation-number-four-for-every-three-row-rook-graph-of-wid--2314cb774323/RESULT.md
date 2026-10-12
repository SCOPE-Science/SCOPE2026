# Representation number four for every three-row rook graph of width at least four

## Finding
Let \(n\ge4\) be an integer. The rook graph \(R_{3,n}=K_3\square K_n\) has vertices \((i,j)\) for \(i\in\{1,2,3\}\), \(1\le j\le n\), with two distinct vertices adjacent exactly when they agree in a coordinate. A \(k\)-uniform word over its vertices *represents* the graph if each vertex occurs exactly \(k\) times and each pair of distinct vertices alternates in the word precisely when it is an edge. Let \(\mathcal R\) denote the minimum such \(k\).

**Theorem.** For all integers \(n\ge4\),
\[
\mathcal R(R_{3,n})=4.
\]
The lower bound is a finite exhaustive obstruction on \(R_{3,4}\); the upper bound is an explicit previously established Cartesian-product word construction. The motivating paper left the lower bound at \(R_{3,4}\) open rather than treating its computer observation as proof.

## Assumptions and scope
Graphs are finite and simple. A pair of letters alternates in a \(k\)-uniform word exactly when its two-letter projection is one of the alternating length-\(2k\) binary words. The product \(K_3\square K_n\) is equivalently the three-by-\(n\) rook-move graph and the line graph of \(K_{3,n}\). This result determines the representation number only for the three-row infinite family \(n\ge4\). The earlier case \(n=3\) has representation number three [1]; it is not a new assertion.

## Proof
**Upper bound.** The complete graph \(K_n\) has the \(2\)-uniform representing word \((1\,2\,\cdots\,n)^2\). The Cartesian-product construction in Broere--Zantema [2, Section 5] transforms any \(k\)-uniform representation of \(G\), with \(k>1\), into a \((k+r-1)\)-uniform representation of \(G\square K_r\). Applying it to \(G=K_n\), \(k=2\), and \(r=3\) gives a \(4\)-uniform representation of \(K_n\square K_3\) for every \(n\). For a concrete reproducible form, put \(w=(1\,2\,\cdots\,n)^2\); for each occurrence of a letter \(x\), replace its first and second occurrences, respectively, using
\[
\begin{array}{c|cc}
&\text{first}&\text{second}\\\hline
f_1&x_1&x_3x_2x_1\\
f_2&x_2&x_1x_3x_2\\
f_3&x_3&x_2x_1x_3
\end{array}
\]
and concatenate \(f_3(w)f_2(w)f_1(w)\), interpreting each \(f_i\) on the original \(w\). This is precisely the \(r=3,k=2\) substitution from [2] and contains each \(x_i\) four times.

**Lower bound: canonical words.** The earlier \(R_{3,3}\) result [1] excludes \(1\)- and \(2\)-uniform representations of \(R_{3,4}\), since \(R_{3,3}\) is an induced subgraph. Thus it remains to exclude a \(3\)-uniform representation of \(R_{3,4}\). Denote its three row cliques by \(A=\{A_0,\ldots,A_3\}\), \(B=\{B_0,\ldots,B_3\}\), and \(C=\{C_0,\ldots,C_3\}\). Between different row cliques, only equal-column pairs are adjacent. For any \(k\)-uniform word, the projection onto a clique consists of \(k\) repetitions of a single permutation: every two letters in the clique must alternate, so their order in all occurrence layers is the same.

If a \(3\)-uniform representing word existed, rotate it cyclically to begin with an occurrence of \(A_0\). Such rotation preserves alternating and nonalternating two-letter patterns, because each letter appears three times. Relabel the four columns so the \(A\)-projection becomes
\[
(A_0A_1A_2A_3)^3.
\]
The \(B\)-projection must be \((B_{\pi(0)}B_{\pi(1)}B_{\pi(2)}B_{\pi(3)})^3\), for one of the \(24\) permutations \(\pi\); similarly for \(C\).

**Lower bound: exhaustive finite lemma.** A possible projection onto \(A\cup B\) is determined by its permutation \(\pi\) and a shuffle of the two fixed 12-letter row strings, with the first letter \(A_0\). There are exactly
\[
24\binom{23}{11}=32,449,872
\]
such candidates. Retain a candidate precisely if \(A_i\) alternates with \(B_j\) exactly when \(i=j\), for all 16 column pairs. The exact enumeration gives **354** surviving projections. The same set of 354 shapes is possible for \(A\cup C\).

Every hypothetical full word determines an ordered pair of surviving projections. These projections share their twelve ordered \(A\)-letters; between consecutive \(A\)-letters, and after the last one, there are twelve gaps. In each gap, shuffle the prescribed subsequence of \(B\)-letters with that of \(C\)-letters, preserving both internal orders. This reconstructs **every** full word consistent with that projection pair, without assuming any relative order of \(B\) and \(C\). Exhaustively checking all \(354^2=125,316\) ordered pairs and all their gapwise shuffles yields 158,483,130 complete shuffles, **none** of which has \(B_i\) alternating with \(C_j\) exactly when \(i=j\) for all 16 pairs. Thus no \(3\)-uniform representation of \(R_{3,4}\) exists.

The exhaustive lemma is a finite theorem because the normalization, candidate ranges, gap decomposition, and complete pair tests are proved above; the included independent enumerators execute all such cases without heuristics, sampling, or time limits. `verify_interval_merge.cpp` counts all complete shuffles, while `verify_mask_automaton.cpp` independently generates the admissible pair projections using bitmasks and counts the 238,188 shuffles that meet the four required \(B_i,C_i\) alternations, of which none meets all twelve nonedge requirements.

Finally, for each \(n\ge4\), restricting a representing word for \(R_{3,n}\) to the columns \(1,2,3,4\) would give a \(3\)-uniform representation of the induced \(R_{3,4}\) if one existed. The induced \(R_{3,3}\) excludes one and two copies, and the obstruction above excludes three copies. Therefore \(\mathcal R(R_{3,n})\ge4\); combine with the upper bound.

## Verification
Compile and run the two exhaustive programs from their own standalone source files using a C++17 compiler:

```sh
g++ -O3 -std=c++17 verify_interval_merge.cpp -o verify_interval_merge
./verify_interval_merge
g++ -O3 -std=c++17 verify_mask_automaton.cpp -o verify_mask_automaton
./verify_mask_automaton
python3 verify_upper.py
```

The first program reports `pair patterns 354`, `pairs 125316 leaves 158483130 found 0`. The second reports `admissible_pair_projections=354`, `projection_pairs=125316`, `match_alternating_shuffles=238188`, and `full_representation_words=0`. The third checks the explicit upper construction for every width from two through ten. Exact captured outputs are included. The lower bound for arbitrary \(n\) is not an extrapolation from tested widths: it is the induced-subgraph consequence of the exhaustive \(n=4\) case.

## Relationship to prior work
Kitaev and Pyatkin [1, Section 2.3 and Section 3] established \(\mathcal R(R_{2,n})=3\) for \(n\ge3\), exhibited the three-uniform representation for \(R_{3,3}\), and stated that a computer search found no three-uniform word for \(R_{3,4}\), expressly leaving a proof open. The present work replaces that unproved observation with a complete, replayable exhaustive obstruction and thereby determines the entire three-row family. Broere and Zantema [2, Section 5] already proved the product upper bound; the upper bound alone does not imply the new equality.

## Limitations
The essential lower-bound obstruction depends on exact executable enumeration of a large but finite, mathematically complete search space. Both enumerators yield zero. This theorem does not determine the representation numbers for four or more rows, nor does it assert that no equivalent proof might exist in unindexed literature.

## References
[1] S. Kitaev and A. Pyatkin, *On the representation number of chessboard graphs*, arXiv:2609.22311v1 (first posted 15 September 2026); *Acta Informatica* 63, article 33 (2026), DOI:10.1007/s00236-026-00547-w. Relevant material: Sections 2.3 and 3.

[2] B. Broere and H. Zantema, *The k-cube is k-representable*, arXiv:1808.01800v1 (2018); *Journal of Automata, Languages and Combinatorics* 24 (2019), 3--12, DOI:10.25596/jalc-2019-003. Relevant material: Section 5 (Cartesian product with a complete graph).
