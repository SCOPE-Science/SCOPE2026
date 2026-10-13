# Complete higher-support profile of the optimal quaternary self-orthogonal cyclic \([15,5,8]\) code
## Finding

Li, Cao, and Li's Example 4.9 contains an optimal quaternary Euclidean self-orthogonal cyclic code
\[
C
\]
with parameters
\[
[15,5,8]_4.
\]

For this exact code, the complete generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5)
=
(8,11,12,14,15).
\]

More strongly, the complete support-size distribution is determined in every subcode dimension. The notation \(w:N\) means that exactly \(N\) subcodes of the indicated dimension have support size \(w\).

For \(r=1\),
\[
8:15,\quad9:70,\quad11:90,\quad12:70,\quad13:90,\quad15:6.
\]

For \(r=2\),
\[
11:75,\quad12:255,\quad13:990,\quad14:2310,\quad15:2167.
\]

For \(r=3\),
\[
12:5,\quad13:90,\quad14:1080,\quad15:4622.
\]

For \(r=4\),
\[
14:15,\qquad15:326.
\]

For the unique five-dimensional subcode,
\[
15:1.
\]

Consequently, the generalized Hamming weights are attained by exactly
\[
15,\ 75,\ 5,\ 15,\ 1
\]
subcodes in dimensions \(1,\ldots,5\).

The one-dimensional spectrum also gives the ordinary weight enumerator
\[
1+45z^8+210z^9+270z^{11}+210z^{12}+270z^{13}+18z^{15}.
\]

## Assumptions and scope

Let
\[
\mathbb F_4=\{0,1,\omega,\omega^2\},
\qquad
\omega^2+\omega+1=0.
\]
The source uses
\[
q=4,\qquad m=2,\qquad n=4^2-1=15,
\]
with
\[
\Delta_1=\{0,3,6\},
\qquad
\Delta_2=\{1,2,5\}.
\]
The corresponding \(4\)-cyclotomic cosets modulo \(15\) give the defining-zero set
\[
R=
C_0\cup C_1\cup C_2\cup C_3\cup C_5\cup C_6
=
\{0,1,2,3,4,5,6,8,9,12\}.
\]

Using
\[
\mathbb F_{16}=\mathbb F_2[\beta]/(\beta^4+\beta+1)
\]
with primitive \(\beta\), identify
\[
\omega=\beta^5.
\]
Multiplying the root factors
\[
\prod_{i\in R}(x-\beta^i)
\]
gives the generator polynomial over \(\mathbb F_4\)
\[
g(x)
=
\omega+\omega^2x+x^2+\omega x^4+\omega^2x^5+\omega^2x^6+x^7+\omega x^9+x^{10}.
\]

The claim concerns this exact Euclidean self-orthogonal cyclic code. It does not assert that every quaternary \([15,5,8]\) code has the same higher-support profile.

## Proof

The displayed polynomial has degree \(10\) and divides
\[
x^{15}-1.
\]
Hence
\[
g(x),\ xg(x),\ldots,x^4g(x)
\]
form a cyclic generator matrix of rank \(5\).

A direct calculation over \(\mathbb F_4\) shows that all pairwise Euclidean inner products of these five rows vanish. Thus the reconstructed code is Euclidean self-orthogonal, independently matching the structural property in the source.

Enumerating all
\[
4^5=1024
\]
messages gives
\[
A_0=1,\quad
A_8=45,\quad
A_9=210,\quad
A_{11}=270,\quad
A_{12}=210,\quad
A_{13}=270,\quad
A_{15}=18.
\]
The smallest nonzero weight is \(8\), reproducing the source's published minimum-distance parameter.

Because the message-to-code map
\[
\mathbb F_4^5\longrightarrow C
\]
has rank \(5\), it is an isomorphism. Therefore \(r\)-dimensional code subcodes correspond bijectively to \(r\)-dimensional message subspaces.

Every message subspace has a unique reduced-row-echelon basis. The exact numbers of such subspaces are
\[
\left[{5\atop1}\right]_4=341,\qquad
\left[{5\atop2}\right]_4=5797,\qquad
\left[{5\atop3}\right]_4=5797,\qquad
\left[{5\atop4}\right]_4=341,\qquad
\left[{5\atop5}\right]_4=1.
\]
Thus there are
\[
12277
\]
positive-dimensional message subspaces.

For a basis
\[
u_1,\ldots,u_r
\]
of a message subspace, the support of the corresponding code subcode is exactly
\[
\operatorname{Supp}(u_1G)\cup\cdots\cup\operatorname{Supp}(u_rG).
\]
A coordinate is absent from this union if and only if it vanishes on every basis word, which is equivalent to vanishing on the entire generated subcode.

Exhaustive enumeration of all \(12277\) message subspaces therefore visits every nonzero-dimensional code subcode exactly once. Counting these support unions gives the complete spectra in the Finding. Their minima are
\[
(8,11,12,14,15).
\]

This is an exact finite proof for the stated code; no sampling or incomplete search is used.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It constructs \(\mathbb F_{16}\), verifies that the chosen \(\beta\) has order \(15\), embeds \(\mathbb F_4\) as
\[
\{0,1,\beta^5,\beta^{10}\},
\]
and rebuilds \(g(x)\) from the ten published defining zeros.

It checks
\[
g(x)\mid x^{15}-1,
\]
constructs the five shifted generator rows, verifies rank \(5\) and Euclidean self-orthogonality, and enumerates all \(1024\) codewords.

It then generates every subspace of \(\mathbb F_4^5\) exactly once in reduced-row-echelon form. For each basis it computes the union of basis-word supports, checks the Gaussian-binomial census in every dimension, and compares the resulting complete histograms with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article constructs the cyclic family and publishes the optimal parameters \([15,5,8]_4\). Its full text contains no generalized-Hamming-weight result and no subcode-support distribution for this example.

Bouyukliev and Östergård classify small optimal self-orthogonal codes over \(\mathbb F_3\) and \(\mathbb F_4\). Their quaternary table is for Hermitian self-orthogonality, whereas the present cyclic code is Euclidean self-orthogonal and is not Hermitian self-orthogonal in the displayed generator model. Their article also contains no generalized-Hamming-weight terminology. Thus that classification neither identifies the present Euclidean code by higher-support data nor supplies the spectra above.

Li's 2017 weight-hierarchy theorem for a family of cyclic codes with an arbitrary number of nonzeros requires all parity-check zeros to have the same minimal-polynomial degree \(m\). The parity-check zero set of the present code is
\[
\{7,10,11,13,14\}
=
C_7\cup C_{10}\cup C_{11},
\]
where
\[
|C_7|=2,\qquad |C_{10}|=1,\qquad |C_{11}|=2.
\]
Hence its degree-uniformity hypothesis fails, so that theorem does not evaluate this hierarchy.

Pan, Chen, Liu, and Liu determine complete subcode-support distributions for several simplex-based Griesmer, modified Solomon--Stiffler, and related constructions. Their full text contains no \([15,5,8]\) occurrence and does not identify this cyclic code as one of the solved families.

Focused searches using the exact parameters, defining-set description, ordinary enumerator, hierarchy
\[
(8,11,12,14,15),
\]
and subcode-support terminology found no prior complete higher-support profile for this exact code.

## Limitations

The result is a complete finite classification for the \(q=4,m=2\) source example, not a closed formula for every member of the Li--Cao--Li cyclic families.

The census classifies subcodes by support size, not by automorphism-group orbit.

The source's construction, Euclidean self-orthogonality, and optimal \([15,5,8]_4\) parameters are prior work. The new content is the complete subcode-support distribution, the generalized Hamming hierarchy, the exact minimizer multiplicities, and the ordinary enumerator as its one-dimensional specialization.

An older equivalent presentation or unpublished database entry could contain the same higher-support data; no such coverage was found in the inspected literature and exact searches.

## References

1. Ping Li, Qicai Cao, and Fulin Li, *The construction of two classes of self-orthogonal cyclic codes*, Advances in Mathematics of Communications 25 (2026), 44--59, DOI 10.3934/amc.2026041.
2. Iliya Bouyukliev and Patric R. J. Östergård, *Classification of Self-Orthogonal Codes over \(\mathbb F_3\) and \(\mathbb F_4\)*, SIAM Journal on Discrete Mathematics 19 (2005), 363--370, DOI 10.1137/S0895480104441085.
3. Shuxing Li, *The weight hierarchy of a family of cyclic codes with arbitrary number of nonzeroes*, Finite Fields and Their Applications 45 (2017), 355--371, DOI 10.1016/j.ffa.2017.01.002.
4. Xu Pan, Hao Chen, Hongwei Liu, and Shengwei Liu, *Optimal Few-SSW Linear Codes and Their Subcode Support Weight Distributions*, IEEE Transactions on Information Theory 71 (2025), 1028--1042, DOI 10.1109/TIT.2024.3519672; arXiv:2408.10005.
5. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
