# Complete monomial hull spectrum of the \([6,3,3]_8\) extension in Example 5.6
## Finding

For the \([6,3,3]_8\) code \(C_{\mathrm{ex}}\) in Example 5.6 of Bhowmick–Dalai–Mesnager, among the
\[
7^5=16807
\]
normalized diagonal scalings
\[
(1,a_2,\ldots,a_6)\in(\mathbb F_8^\times)^6,
\]
exactly \(14685\), \(2091\), and \(31\) yield Euclidean hull dimensions \(0\), \(1\), and \(2\), respectively, and none yields hull dimension \(3\).

Consequently the attainable Euclidean hull dimensions in the entire monomial equivalence class are exactly
\[
\{0,1,2\},
\]
so the maximal Euclidean hull dimension is \(2\). In particular, no monomially equivalent code is self-dual.

## Assumptions and scope

The field is
\[
\mathbb F_8=\mathbb F_2(\omega),\qquad \omega^3+\omega+1=0.
\]
The code is the explicit extension printed in Example 5.6, with generator matrix
\[
G=\begin{pmatrix}
1&0&0&1&\omega^5&\omega^5\\
0&1&0&\omega&\omega^4&\omega^6\\
0&0&1&\omega^4&\omega&\omega^5
\end{pmatrix}.
\]
The source states that this is a \([6,3,3]_8\) code with one-dimensional Euclidean hull.

A monomial transformation consists of independent nonzero coordinate scalings followed by a coordinate permutation. The claim concerns Euclidean hull dimensions throughout the full monomial equivalence class of this fixed code.

## Proof

For a full-rank \(k\times n\) generator matrix \(H\), the Euclidean hull dimension is
\[
\dim\operatorname{Hull}(H)=k-\operatorname{rank}(HH^T).
\]
This is the rank criterion used in the source paper.

Let
\[
D=\operatorname{diag}(a_1,\ldots,a_6),\qquad a_i\in\mathbb F_8^\times,
\]
and let \(P\) be a permutation matrix. A generator matrix for an arbitrary monomial equivalent code is \(GDP\). Since \(PP^T=I\),
\[
(GDP)(GDP)^T=GD^2G^T.
\]
Thus the permutation has no effect on the Gram rank. Multiplying all \(a_i\) by one common nonzero scalar also does not change the code, because a linear code is closed under global scalar multiplication. Hence every diagonal-scaling class has a representative with \(a_1=1\), and it is enough to enumerate the \(7^5\) vectors
\[
(1,a_2,\ldots,a_6)\in(\mathbb F_8^\times)^6.
\]

Exact enumeration gives the Gram-rank distribution
\[
\begin{array}{c|ccc}
\dim\operatorname{Hull}&0&1&2\\ \hline
\#\text{ normalized scalings}&14685&2091&31.
\end{array}
\]
No scaling has hull dimension \(3\). Explicit witnesses are
\[
(1,1,1,1,1,\omega),\qquad
(1,1,1,1,1,1),\qquad
(1,1,1,\omega^5,\omega^5,\omega^2)
\]
for hull dimensions \(0\), \(1\), and \(2\), respectively.

Because every monomial transformation reduces to one of these diagonal cases for Gram rank, the attainable hull dimensions are exactly \(\{0,1,2\}\). Since the code has length \(6\) and dimension \(3\), hull dimension \(3\) would mean Euclidean self-duality. Its absence proves that no monomially equivalent code is self-dual.

As an independent identity check on the reconstructed object, exhaustive enumeration of the original \(8^3=512\) codewords gives
\[
W_C(z)=1+7z^3+84z^4+189z^5+231z^6,
\]
recovering minimum distance \(3\) and the source parameters.

## Verification

`artifacts/verify.py` uses only the Python standard library. It implements \(\mathbb F_8\) from \(\omega^3+\omega+1=0\), reconstructs the exact matrix above, verifies rank \(3\), the source's one-dimensional hull, and the complete baseline weight distribution.

It then exhausts every normalized diagonal scaling, computes the exact rank of each \(3\times3\) Euclidean Gram matrix over \(\mathbb F_8\), reproduces the profile \((14685,2091,31,0)\), and checks all three explicit witnesses in `artifacts/certificate.json`. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Bhowmick, Dalai, and Mesnager study low-dimensional Euclidean hulls over binary extension fields and use Example 5.6 to construct the displayed \([6,3,3]_8\) one-dimensional-hull code from a \([5,2,4]_8\) LCD code. Their paper states the hull dimension for the displayed representative but does not give the complete hull behavior of all monomially equivalent representatives.

Chen introduced the hull-variation problem and the maximal hull dimension as an invariant under code equivalence. The present calculation resolves that invariant for the explicit Example 5.6 code and, more strongly, gives the complete normalized diagonal hull profile. Exact searches for the source example, its parameters, maximal-hull terminology, and the profile counts did not locate this classification in the inspected literature or research records.

## Limitations

The multiplicities \(14685\), \(2091\), and \(31\) count normalized coordinate-scaling parameters, not necessarily pairwise inequivalent codes after quotienting by the full monomial automorphism group. The invariant conclusion that the attainable hull dimensions are exactly \(\{0,1,2\}\), and hence that the maximal hull dimension is \(2\), is unaffected by such duplication.

The finding concerns this specific \([6,3,3]_8\) code. It does not classify all near-MDS \([6,3,3]_8\) codes or all codes arising from the extension construction.

## References

1. Sanjit Bhowmick, Deepak Kumar Dalai, and Sihem Mesnager, *On construction of linear (Euclidean) hull codes over finite extensions binary fields*, arXiv:2511.18779v1, first public version 2025-11-24; Designs, Codes and Cryptography 94 (2026), article 10, DOI 10.1007/s10623-025-01757-y.
2. Hao Chen, *On the Hull-Variation Problem of Equivalent Linear Codes*, IEEE Transactions on Information Theory 69 (2023), 2911–2922, DOI 10.1109/TIT.2023.3234249.
