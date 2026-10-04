# Higher-support geometry of the displayed ternary code C3,2
## Finding

For the specific ternary LCD code \(C_{3,2}\) displayed by An--Hong--Kim--Lim with parameters
\[
[23,5,12]_3,
\]
the generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5)=(12,17,19,21,23).
\]
The complete support-size spectra of its \(r\)-dimensional subcodes are
\[
\begin{array}{c|l}
r&\text{support size : number of subcodes}\\
1&12:6,\ 13:16,\ 14:27,\ 15:22,\ 16:17,\ 17:13,\ 18:9,\ 19:3,\ 20:5,\ 21:3\\
2&17:13,\ 18:69,\ 19:224,\ 20:309,\ 21:250,\ 22:244,\ 23:101\\
3&19:1,\ 20:28,\ 21:202,\ 22:428,\ 23:551\\
4&21:1,\ 22:21,\ 23:99\\
5&23:1.
\end{array}
\]
The generator-column multiset has exactly one repeated projective point: coordinates \(7\) and \(22\) are proportional. Hence
\[
d(C_{3,2}^{\perp})=2,
\]
and the dual has exactly two weight-\(2\) words.

## Assumptions and scope

The \(5\times23\) generator matrix is used exactly as printed in the source, over \(\mathbb F_3\), with the Euclidean inner product. For an \(r\)-dimensional subcode \(D\),
\[
d_r=\min_{\dim D=r}|\operatorname{Supp}(D)|.
\]
The result concerns this particular displayed code, not all \(38\) inequivalent \([23,5,12]_3\) LCD codes reported by the source.

## Proof

The displayed matrix has rank \(5\), and its Euclidean Gram matrix has rank \(5\), confirming the LCD property. Every \(r\)-dimensional subcode is the image of a unique \(r\)-dimensional subspace of \(\mathbb F_3^5\). Enumerating all reduced-row-echelon representatives gives
\[
121,\ 1210,\ 1210,\ 121,\ 1
\]
subspaces in dimensions \(1,2,3,4,5\). Direct union-of-support computation gives the spectra above, whose minima are
\[
12,\ 17,\ 19,\ 21,\ 23.
\]

Projectively canonicalizing the \(23\) generator columns gives \(22\) points. The only repeated point occurs at coordinates \(7\) and \(22\), where
\[
G_{\ast,22}=2G_{\ast,7}.
\]
Thus the dual contains a weight-\(2\) relation, while no zero column exists, so no dual word has weight \(1\). The unique repeated pair has a one-dimensional relation space, yielding exactly two nonzero weight-\(2\) dual words.

As a consistency check, exhaustive enumeration of all \(3^5\) codewords gives
\[
1+12z^{12}+32z^{13}+54z^{14}+44z^{15}+34z^{16}+26z^{17}+18z^{18}+6z^{19}+10z^{20}+6z^{21}.
\]
MacWilliams transformation starts
\[
1+2z^2+22z^3+650z^4+4574z^5+\cdots.
\]

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs the published matrix, verifies its rank and LCD Gram rank, enumerates all \(3^5\) codewords, and enumerates every subspace of \(\mathbb F_3^5\) in reduced row-echelon form.

All \(2663\) nonzero-dimensional subcodes are checked. The replay verifies every support-size count above, the generalized Hamming weights, the unique repeated projective column pair, and the first six dual weight coefficients by MacWilliams transformation. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary paper introduces the displayed \(C_{3,2}\) as a new ternary LCD \([23,5,12]_3\) code and prints its generator matrix. It does not state generalized Hamming weights or a dimension-by-dimension subcode-support census.

The associated public representative dataset records ordinary weight distributions and dual weight distributions as signatures for \([23,5,12]_3\) representatives. Those spectra are therefore not claimed as new here. The inspected dataset does not record generalized Hamming weights or complete support histograms by subcode dimension.

Focused searches for the named code, exact parameters, the hierarchy \((12,17,19,21,23)\), and equivalent projective/higher-support formulations found no prior same-object statement. General generalized-weight theory supplies definitions and projective interpretations, but not these exact values for this matrix.

## Limitations

This is an exact finite result for the displayed matrix only, not a classification of the \(38\) inequivalent codes with the same parameters.

Ordinary weight and dual-weight distributions are consistency checks rather than novelty claims because related signatures already occur in the public companion dataset.

No claim is made that this generalized Hamming hierarchy uniquely determines the code's equivalence class.

## References

1. Junmin An, Ji-Hoon Hong, Jon-Lark Kim, and Haeun Lim, *Shortest LCD embeddings of binary, ternary and quaternary linear codes*, arXiv:2601.20600v1; DOI 10.3934/amc.2026048.
2. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
3. Public data accompanying the first reference, `many_shortest_lcd_bklc_representatives.txt`.
