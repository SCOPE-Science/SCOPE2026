# Higher-support geometry of the displayed ternary \([24,6,12]\) LCD code
## Finding

Let \(C_{3,3}\) be the ternary LCD code displayed by An--Hong--Kim--Lim with parameters
\[
[24,6,12]_3.
\]
Its complete generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5,d_6)=(12,16,19,21,23,24).
\]
More strongly, the support-size spectra of all subcodes are
\[
\begin{array}{c|l}
r&\text{support size : number of subcodes}\\
1&12:16,\ 13:35,\ 14:54,\ 15:50,\ 16:63,\ 17:48,\ 18:42,\ 19:27,\ 20:24,\ 21:4,\ 22:1\\
2&16:1,\ 17:41,\ 18:307,\ 19:955,\ 20:1721,\ 21:2598,\ 22:2716,\ 23:2018,\ 24:654\\
3&19:3,\ 20:150,\ 21:1511,\ 22:5577,\ 23:12738,\ 24:13901\\
4&21:3,\ 22:267,\ 23:2361,\ 24:8380\\
5&23:24,\ 24:340\\
6&24:1.
\end{array}
\]
The dimension-two minimum is attained by exactly one subcode. In the published message-space basis used by the generator matrix, that subcode has reduced-row-echelon basis
\[
\begin{bmatrix}
0&0&1&1&0&2\\
0&0&0&0&1&2
\end{bmatrix},
\]
and its eight zero coordinates are
\[
\{1,2,9,10,14,15,22,23\}.
\]

All \(24\) generator columns represent distinct points of \(\mathrm{PG}(5,3)\). Exactly three projective lines contain three of these points, with coordinate triples
\[
\{1,15,23\},\qquad \{2,5,11\},\qquad \{8,12,24\}.
\]
Hence
\[
d(C_{3,3}^{\perp})=3,
\]
and there are exactly six nonzero dual words of weight \(3\).

## Assumptions and scope

The calculation uses the exact \(6\times24\) generator matrix printed for \(C_{3,3}\) in Proposition 4.1 of the cited source and independently reproduced in its public companion data record. Coordinates are numbered \(1\) through \(24\) in the printed order. Generalized Hamming weights use the standard definition: \(d_r(C)\) is the minimum size of the coordinate support of an \(r\)-dimensional subcode.

The result is for this particular displayed representative. It does not classify all ternary LCD \([24,6,12]_3\) codes, nor does it assert that the hierarchy or support spectra determine monomial equivalence.

## Proof

Write the generator matrix as \(G\), with columns \(g_1,\ldots,g_{24}\in\mathbb F_3^6\). Direct row reduction gives \(\operatorname{rank}(G)=6\). The Euclidean Gram matrix \(GG^T\) has determinant \(1\) in \(\mathbb F_3\), so the displayed code is LCD.

Every \(r\)-dimensional subcode is uniquely of the form \(UG\), where \(U\leq\mathbb F_3^6\) is an \(r\)-dimensional message subspace. Choose the unique reduced-row-echelon basis matrix \(B\) of \(U\). A coordinate \(j\) vanishes identically on \(UG\) exactly when
\[
Bg_j=0,
\]
equivalently when \(g_j\in U^{\perp}\). Therefore
\[
|\operatorname{Supp}(UG)|=24-\#\{j:g_j\in U^{\perp}\}.
\]
Thus exhaustive reduced-row-echelon enumeration of message subspaces is also an exhaustive projective intersection calculation.

There are respectively
\[
364,\ 11011,\ 33880,\ 11011,\ 364,\ 1
\]
subspaces in dimensions \(1,2,3,4,5,6\). Enumerating all \(56631\) of them gives exactly the six support histograms stated above; taking the minimum in each row gives
\[
(12,16,19,21,23,24).
\]
The dimension-two histogram contains support size \(16\) exactly once, yielding the stated unique minimizer and zero-coordinate set.

For the dual assertion, projective normalization of the \(24\) nonzero columns gives \(24\) distinct projective points, excluding dual weights \(1\) and \(2\). Exhaustion of normalized three-column dependences gives exactly the three supports listed above. Each one-dimensional ternary relation has two nonzero scalar multiples, so the dual has exactly six weight-three words and minimum distance \(3\).

## Verification

The bundled `artifacts/verify.py` uses only the Python standard library. Starting from the published generator matrix, it checks rank \(6\), determinant \(1\) of \(GG^T\), and the complete ordinary weight distribution by enumerating all \(3^6\) messages. It then enumerates every reduced-row-echelon subspace of \(\mathbb F_3^6\), checks each support size both from the image matrix \(BG\) and from the column-annihilation criterion, and reproduces all \(56631\) support counts.

The verifier separately projectivizes all generator columns and exhausts normalized three-column dependences. It obtains exactly the three stated dependent triples and the unique dimension-two minimizer. Successful replay ends with `VERIFY_OK`. The expected data are also recorded in `artifacts/certificate.json`.

## Relationship to prior work

An--Hong--Kim--Lim introduced the displayed \(C_{3,3}\) as a new ternary LCD \([24,6,12]_3\) code, improving the previously recorded minimum distance for the same length and dimension. Their paper gives the generator matrix and ordinary minimum distance, but a full-text search finds no generalized-Hamming-weight calculation. The public companion record for this matrix likewise gives the field, LCD status, parameters, source-code parameters, and generator matrix, not higher-support spectra.

General generalized-weight theory and recent exact algorithms explain how such invariants can be defined or computed, but they do not imply the values for this matrix. Recent work on optimal codes for generalized Hamming weights determines ternary optimal parameters only through dimension five, so it does not cover this dimension-six code. The earlier small-field LCD work cited by the source concerns the pre-existing minimum-distance bounds and predates the displayed distance-twelve representative.

## Limitations

This is an exact finite result for one published code. No claim is made about every inequivalent ternary LCD \([24,6,12]_3\) code or about optimality of the higher generalized weights among all such codes. An unindexed computation of a monomially equivalent representative could contain the same invariants. The exhaustive computation is finite and reproducible; it is not a classification of arbitrary parameter families.

## References

1. Junmin An, Ji-Hoon Hong, Jon-Lark Kim, and Haeun Lim, *Shortest LCD embeddings of binary, ternary and quaternary linear codes*, arXiv:2601.20600v1, first public version 2026-01-28; DOI 10.3934/amc.2026048.
2. Junmin An, *Shortest LCD embeddings of binary, ternary and quaternary linear codes with dataset*, public companion repository, record `INDEX: 227` in `Data_for_LCD_codes_F2_F3_F4.txt`.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
4. Rodrigo San-José, *An Algorithm for Computing Generalized Hamming Weights and the Sage Package GHWs*, ACM Transactions on Mathematical Software 51 (2025), Article 26, DOI 10.1145/3773284.
5. Sascha Kurz, Ivan Landjev, and Assia Rousseva, *Optimal codes and arcs for the generalized Hamming weights*, 2026, DOI 10.15495/EPub_UBT_00008792.
