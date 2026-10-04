# Spectral asymmetry in an optimal quaternary quasi-cyclic LCP
## Finding

Consider the length-\(14\), dimension-\(9\) quasi-cyclic linear complementary pair \((C,D)\) over
\[
\mathbb F_4=\mathbb F_2(\omega),\qquad \omega^2+\omega+1=0,
\]
listed in Table 1 of Abdukhalikov, Ho, Ling, and Verma.  The source gives the security parameter
\[
d_{\mathrm{LCP}}=\min\{d(C),d(D^\perp)\}=4.
\]

For this exact row, both security-side codes are \([14,9,4]_4\), but their complete Hamming spectra are different.  The code \(C\) has
\[
\begin{aligned}
W_C(z)={}&1+42z^4+630z^5+2121z^6+6888z^7+19845z^8+38052z^9\\
&+58338z^{10}+61992z^{11}+48048z^{12}+21462z^{13}+4725z^{14},
\end{aligned}
\]
whereas
\[
\begin{aligned}
W_{D^\perp}(z)={}&1+231z^4+2394z^6+8064z^7+18543z^8+37632z^9\\
&+59388z^{10}+61824z^{11}+47817z^{12}+21504z^{13}+4746z^{14}.
\end{aligned}
\]

Their generalized Hamming-weight hierarchies are also different:
\[
(d_1,\ldots,d_9)(C)=(4,6,7,9,10,11,12,13,14),
\]
and
\[
(d_1,\ldots,d_9)(D^\perp)=(4,6,7,8,10,11,12,13,14).
\]

Thus \(C\) and \(D^\perp\) are not monomially equivalent.  In particular, the published row has equal optimal minimum-distance security on its two sides while exhibiting different higher support geometry.

## Assumptions and scope

The source identifies index-\(2\) quasi-cyclic codes of length \(2m\) with submodules of
\[
R^2,\qquad R=\mathbb F_4[x]/(x^m-1).
\]
For the Table 1 row with \(n=14\), one has \(m=7\).  We use the source generators
\[
C=\left\langle (g_{11},g_{12}),(0,g_{22})\right\rangle_R
\]
with
\[
g_{11}=x+1,\qquad
g_{12}=x^3+\omega^2x+\omega,\qquad
g_{22}=x^4+x^3+x^2+1,
\]
and
\[
D=\left\langle (f_{11},f_{12}),(0,f_{22})\right\rangle_R
\]
with
\[
f_{11}=f_{12}=x^3+x^2+1,\qquad
f_{22}=x^6+x^5+x^4+x^3+x^2+x+1.
\]

The dual \(D^\perp\) is the ordinary Euclidean dual over \(\mathbb F_4\).  Generalized Hamming weights use the standard support-union definition: \(d_r(E)\) is the minimum coordinate-support size of an \(r\)-dimensional subcode of \(E\).

## Proof

Cyclically shifting the two \(R\)-module generators through the seven positions in each block gives ordinary \(\mathbb F_4\)-generator matrices. Exact row reduction gives
\[
\dim_{\mathbb F_4}C=9,\qquad
\dim_{\mathbb F_4}D=5,
\]
and the stacked generator matrix of \(C+D\) has rank \(14\).  Hence the reconstructed codes form a complementary pair.  Solving the Euclidean orthogonality equations for \(D\) gives
\[
\dim_{\mathbb F_4}D^\perp=9.
\]

Each of \(C\) and \(D^\perp\) has exactly
\[
4^9=262144
\]
codewords. Exhaustive enumeration gives the two displayed weight enumerators, whose coefficients each sum to \(262144\).  Their first nonzero term occurs at weight \(4\), reproducing the source security value.

For generalized Hamming weights, let \(G\) be a full-rank \(9\times14\) generator matrix and let \(I\subseteq\{1,\ldots,14\}\).  The dimension of the subcode supported inside \(I\) is
\[
9-\operatorname{rank}(G_{\overline I}),
\]
where \(G_{\overline I}\) denotes the restriction to columns outside \(I\).  Exhausting all \(2^{14}\) coordinate subsets therefore determines every generalized Hamming weight exactly.  This calculation gives the two displayed hierarchies.

A monomial transformation preserves Hamming weights of every codeword and preserves generalized Hamming weights.  Since the ordinary weight enumerators already differ, and independently the fourth generalized Hamming weights are \(9\) and \(8\), the two security-side codes cannot be monomially equivalent.

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs \(\mathbb F_4\) as \(\mathbb F_2[\omega]/(\omega^2+\omega+1)\), rebuilds the two quasi-cyclic codes from the six printed generator polynomials, and verifies the dimensions and the complementary-pair rank condition.

It then constructs \(D^\perp\) by exact finite-field nullspace calculation, enumerates all \(4^9\) words in each \(9\)-dimensional code, and compares their complete weight distributions with `artifacts/certificate.json`. Finally it exhausts all \(2^{14}\) coordinate subsets and recomputes both generalized Hamming-weight hierarchies from restricted-column ranks. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary paper constructs quasi-cyclic and quasi-twisted LCPs and reports this row because its security parameter \(4\) meets the best-known minimum distance for a quaternary code of the same length and dimension. It does not state the complete weight enumerators or generalized Hamming-weight hierarchies for this row.

Earlier work of Carlet, Güneri, Özbudak, Özkaya, and Solé already showed that, unlike constacyclic and two-dimensional cyclic LCPs, general quasi-cyclic LCPs need not have \(C\) equivalent to \(D^\perp\). Thus non-equivalence in the abstract is not new here. The new content is the exact invariant fingerprint of this recent optimal-security row: equal minimum distances coexist with sharply different low-weight multiplicities and different fourth generalized Hamming weight.

A separate published quaternary construction also attains \([14,9,4]_4\), confirming that the parameter set itself is not novel. No inspected source or targeted search stated the two spectra or the two generalized-weight hierarchies above for this LCP.

## Limitations

This is an exact finite classification of two codes in one published LCP row; it is not a classification of all quaternary \([14,9,4]_4\) codes or of all quasi-cyclic LCPs.

Different weight enumerators prove that \(C\) and \(D^\perp\) are not monomially equivalent, but the result does not determine their full automorphism groups or their equivalence classes among all quaternary codes with the same parameters.

The computation uses the generator-polynomial convention printed in the primary paper and the standard realization of \(\mathbb F_4\). The nontrivial field automorphism exchanges \(\omega\) and \(\omega^2\) and preserves every Hamming-support invariant reported here.

## References

1. Kanat Abdukhalikov, Duy Ho, San Ling, and Gyanendra K. Verma, *Linear Complementary Pairs of Quasi-Cyclic and Quasi-Twisted Codes*, arXiv:2504.15231v1, 21 April 2025; Advances in Mathematics of Communications, DOI 10.3934/amc.2026036.
2. Claude Carlet, Cem Güneri, Ferruh Özbudak, Buket Özkaya, and Patrick Solé, *On Linear Complementary Pairs of Codes*, IEEE Transactions on Information Theory 64 (2018), 6583--6589, DOI 10.1109/TIT.2018.2796125.
3. *Quaternary conjucyclic codes with an application to EAQEC codes*, Advances in Mathematics of Communications, DOI 10.3934/amc.2024008.
