# Complete subcode-support distribution of the optimal \([24,4,15]_3\) defining-set code
## Finding

Meng, Liu, Liu, Wang, and Zheng give in Examples 3.4 and 3.8 the ternary defining-set code
\[
C_{D_1}
\]
with parameters
\[
[24,4,15]_3.
\]
The source gives its ordinary weight enumerator
\[
1+16z^{15}+54z^{16}+8z^{18}+2z^{24}
\]
and its generalized Hamming-weight hierarchy
\[
(d_1,d_2,d_3,d_4)=(15,21,23,24).
\]

The complete subcode-support distributions are as follows. The notation \(w:N\) means that exactly \(N\) subcodes of the indicated dimension have support size \(w\).

For one-dimensional subcodes,
\[
15:8,\qquad16:27,\qquad18:4,\qquad24:1.
\]

For two-dimensional subcodes,
\[
21:80,\qquad22:36,\qquad24:14.
\]

For three-dimensional subcodes,
\[
23:24,\qquad24:16.
\]

For the unique four-dimensional subcode,
\[
24:1.
\]

Thus the generalized Hamming weights are attained by exactly
\[
8,\qquad80,\qquad24,\qquad1
\]
subcodes in dimensions \(1,2,3,4\), respectively.

## Assumptions and scope

Use
\[
\mathbb F_{27}=\mathbb F_3[\alpha]/(\alpha^3+2\alpha+1).
\]
The source construction with
\[
q=3,\qquad m=z=3,\qquad s=1
\]
has defining set
\[
D_1=\{(x,1):x\in\mathbb F_{27}\setminus\mathbb F_3\}.
\]
The code is
\[
C_{D_1}
=
\left\{
\bigl(\operatorname{Tr}_{27/3}(ax)+b\bigr)_{x\in\mathbb F_{27}\setminus\mathbb F_3}
:
a\in\mathbb F_{27},\ b\in\mathbb F_3
\right\}.
\]

The claim concerns this exact example. It does not assert a closed subcode-support distribution for every member of either general family in the source.

## Proof

The polynomial
\[
X^3+2X+1
\]
has no root in \(\mathbb F_3\), so it defines \(\mathbb F_{27}\). The set
\[
\mathbb F_{27}\setminus\mathbb F_3
\]
has \(24\) elements.

Take the message basis
\[
(1,0),\quad(\alpha,0),\quad(\alpha^2,0),\quad(0,1)
\]
of the four-dimensional \(\mathbb F_3\)-message space. Evaluating these four messages on the \(24\) coordinates gives a generator matrix of rank \(4\).

Enumerating all
\[
3^4=81
\]
messages gives
\[
A_0=1,\qquad
A_{15}=16,\qquad
A_{16}=54,\qquad
A_{18}=8,\qquad
A_{24}=2,
\]
exactly reproducing the published weight enumerator. This fixes the finite-field and trace conventions before any higher-dimensional census is used.

Because the evaluation map has rank \(4\), \(r\)-dimensional message subspaces correspond bijectively to \(r\)-dimensional code subcodes. Every message subspace has a unique reduced-row-echelon basis. The numbers of such subspaces are
\[
\left[{4\atop1}\right]_3=40,\qquad
\left[{4\atop2}\right]_3=130,\qquad
\left[{4\atop3}\right]_3=40,\qquad
\left[{4\atop4}\right]_3=1.
\]

For a basis
\[
u_1,\ldots,u_r
\]
of a message subspace, the support of the generated code subcode is exactly
\[
\operatorname{Supp}(c(u_1))\cup\cdots\cup\operatorname{Supp}(c(u_r)).
\]
A coordinate is absent from this union precisely when every basis word vanishes there, which is equivalent to every word in the generated subcode vanishing there.

Exact enumeration of all \(211\) positive-dimensional message subspaces therefore exhausts all code subcodes. The resulting support histograms are precisely the four distributions stated above. Their minima are
\[
15,\qquad21,\qquad23,\qquad24,
\]
which independently reproduces the hierarchy already proved in the source.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It implements arithmetic in
\[
\mathbb F_3[X]/(X^3+2X+1),
\]
the absolute trace to \(\mathbb F_3\), and the defining-set evaluation map. It checks length \(24\), dimension \(4\), and the published ordinary weight enumerator.

It then generates every subspace of \(\mathbb F_3^4\) exactly once in reduced-row-echelon form. For each basis it computes the union of the corresponding codeword supports. The dimension totals are checked against the Gaussian binomial coefficients
\[
40,\quad130,\quad40,\quad1,
\]
and the complete histograms are compared with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article determines both the ordinary weight distribution and generalized Hamming-weight hierarchy of this code. Examples 3.4 and 3.8 state the \([24,4,15]_3\) parameters, the ordinary enumerator, and the hierarchy \((15,21,23,24)\). It does not count how many subcodes have each support size.

Pan, Chen, Liu, and Liu develop subcode-support weight distributions for several Griesmer and modified Solomon--Stiffler constructions. Their explicit families are built from simplex matrices by deleting or repeating specified projective subspaces, and their public full text contains no \([24,4,15]_3\) instance. The present defining set is instead the affine slice
\[
\{(x,1):x\in\mathbb F_{27}\setminus\mathbb F_3\}.
\]
No exact-parameter occurrence or implication from their displayed families was found.

A separate classification literature contains other ternary \([24,4,15]\) codes, so the parameter triple alone does not identify this object. The claim is tied to the exact source defining set and is not a statement about every ternary \([24,4,15]\) code.

Focused searches using the exact parameters, the exact hierarchy, the source family, and subcode-support terminology found no prior complete support distribution for this code.

## Limitations

This is a complete finite census for one highlighted optimal example, not a general formula for all parameter choices in the source.

The result classifies subcodes by support size, not by automorphism-group orbit.

The published generalized Hamming weights themselves are prior work; only the complete multiplicities and nonminimal support layers are claimed as new.

An unindexed computation could contain the same finite census, although no such source was located in the searches performed.

## References

1. Kunyi Meng, Chao Liu, Heguo Liu, Xiaoqiang Wang, and Dabin Zheng, *The weight distributions and weight hierarchies of two classes of self-orthogonal codes*, Advances in Mathematics of Communications 23 (2026), 127--145, DOI 10.3934/amc.2026016.
2. Xu Pan, Hao Chen, Hongwei Liu, and Shengwei Liu, *Optimal Few-SSW Linear Codes and Their Subcode Support Weight Distributions*, IEEE Transactions on Information Theory 71 (2025), 1028--1042, DOI 10.1109/TIT.2024.3519672.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
