# The optimal quinary self-orthogonal cyclic \([24,3,19]\) code is projective three-weight
## Finding

For the quinary self-orthogonal cyclic code of length \(24\) whose defining set is
\[
R=\{0,1,\ldots,17,20,21,22\}\subset\mathbb Z_{24},
\]
equivalently the optimal \([24,3,19]_5\) code in Example 4.13 of Li–Cao–Li, the exact Hamming weight enumerator is
\[
W_C(z)=1+96z^{19}+24z^{20}+4z^{24}.
\]
Its generalized Hamming weight hierarchy is
\[
(d_1,d_2,d_3)=(19,23,24).
\]
Moreover, after quotienting minimum words by nonzero scalar multiplication, the \(24\) distinct minimum supports have \(5\)-point complements forming one full cyclic orbit.

## Assumptions and scope

The code is the specific cyclic code in the cited source with \(q=5\), \(m=2\), and defining set
\[
\left(\bigcup_{w\in\Delta_1\cup\Delta_2}C_w^{(5,24)}\right)
\cup C_9^{(5,24)}\cup C_{13}^{(5,24)}\cup C_{14}^{(5,24)},
\]
where
\[
\Delta_1=\{0,4,8,12\},\qquad
\Delta_2=\{1,2,3,6,7\}.
\]
Taking the \(5\)-cyclotomic closures modulo \(24\) gives exactly
\[
R=\{0,1,\ldots,17,20,21,22\}.
\]

Generalized Hamming weights use the standard definition
\[
d_r(C)=\min_{\substack{D\le C\\ \dim D=r}}|\operatorname{Supp}(D)|.
\]

## Proof

Work in \(\mathbb F_{25}=\mathbb F_5(u)\) with \(u^2=3\). The element
\[
\alpha=1+u
\]
has multiplicative order \(24\). Multiplying the linear factors \(x-\alpha^r\) over all \(r\in R\) gives a polynomial fixed by the Frobenius map and therefore lying in \(\mathbb F_5[x]\):
\[
\begin{aligned}
g(x)=\;&4+4x^2+x^3+4x^4+2x^5+3x^6+3x^7+x^8+3x^{10}+4x^{11}\\
&+3x^{12}+x^{13}+4x^{14}+3x^{15}+3x^{16}+4x^{17}+x^{19}+x^{20}+x^{21}.
\end{aligned}
\]
Direct polynomial division verifies
\[
g(x)\mid x^{24}-1.
\]
Hence \(g(x)\) generates the source cyclic code and has degree \(21\), so the dimension is \(3\).

The three rows \(g(x),xg(x),x^2g(x)\), read as length-\(24\) vectors, have zero pairwise Euclidean inner products over \(\mathbb F_5\). Thus the reconstructed code is self-orthogonal, independently checking the structural property asserted by the source.

Exhausting all \(5^3=125\) messages gives exactly
\[
A_0=1,\qquad A_{19}=96,\qquad A_{20}=24,\qquad A_{24}=4,
\]
and no other weights. In particular \(d_1=19\), agreeing with the published optimum.

For \(d_2\), let \(G\) be the \(3\times24\) generator matrix whose rows are the three shifts above. Every column is nonzero, and no two columns are proportional over \(\mathbb F_5\). Thus the \(24\) columns define \(24\) distinct points of \(\mathrm{PG}(2,5)\). The column-subspace characterization gives
\[
d_2=24-\max_P m(P),
\]
where \(m(P)\) is the multiplicity of a projective column point. Since every multiplicity is \(1\),
\[
d_2=24-1=23.
\]
All columns are nonzero, so \(d_3=24\). Hence
\[
(d_1,d_2,d_3)=(19,23,24).
\]

Finally, the \(96\) minimum words split into scalar classes of size \(4\), giving \(24\) minimum supports. Taking complements, one representative is
\[
B=\{0,1,3,11,20\}.
\]
The \(24\) translates
\[
B+t\pmod{24},\qquad 0\le t<24,
\]
are all distinct and exhaust the \(24\) minimum-support complements. Thus the minimum supports form one full orbit under cyclic coordinate shift.

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs \(\mathbb F_{25}\), confirms that \(\alpha=1+u\) has order \(24\), rebuilds the defining set from the source cyclotomic representatives, forms the generator polynomial from its roots, verifies that all coefficients lie in \(\mathbb F_5\), and checks divisibility by \(x^{24}-1\).

It then forms the \(3\times24\) generator matrix, checks rank \(3\) and self-orthogonality, exhausts all \(125\) codewords, reproduces the complete weight enumerator, verifies projectivity of the \(24\) generator columns, derives the generalized Hamming weights, and checks the single cyclic orbit of minimum-support complements. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Li, Cao, and Li construct two classes of self-orthogonal cyclic codes. Their Example 4.13 records this quinary code with parameters \([24,3,19]\), marks it optimal, and gives the defining cyclotomic set, but does not state its complete weight enumerator or generalized Hamming weight hierarchy.

The result above sharpens the published parameter triple in two independent directions. The weight enumerator shows that the code is a three-weight code with only weights \(19\), \(20\), and \(24\). The generalized hierarchy shows that it is projective and that every two-dimensional subcode already occupies at least \(23\) coordinates. The minimum words additionally collapse to a single cyclic support orbit.

Exact-parameter, weight-enumerator, generalized-Hamming-weight, three-weight, and Griesmer-code searches found no source stating these invariants for the source code.

## Limitations

The finding concerns this explicit optimal quinary cyclic code only. It does not classify all quinary \([24,3,19]\) codes, nor prove that every optimal code with these parameters is equivalent to the source construction. The literature comparison is best-of-search: an equivalent code may have had the same enumerator computed under another presentation or in an unindexed table.

## References

1. Ping Li, Qicai Cao, and Fulin Li, *The construction of two classes of self-orthogonal cyclic codes*, Advances in Mathematics of Communications 25 (2026), 44–59, DOI 10.3934/amc.2026041, first public online version 2026-05-06.
2. F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977.
3. V. K. Wei, *Generalized Hamming Weights for Linear Codes*, IEEE Transactions on Information Theory 37 (1991), 1412–1418.
