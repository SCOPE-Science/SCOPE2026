# Complete higher-support profile of the Gold-type \([51,8,20]\) self-orthogonal code
## Finding

Xiang and Song's Example 1 contains the binary self-orthogonal code
\[
C_D
\]
with parameters
\[
[51,8,20]_2
\]
and ordinary weight enumerator
\[
1+34z^{20}+102z^{24}+102z^{28}+17z^{32}.
\]

Its complete generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8)
=
(20,30,38,42,46,48,50,51).
\]

More strongly, the complete support-size distribution is known in every subcode dimension. The notation \(w:N\) means that exactly \(N\) subcodes have support size \(w\).

For \(r=1\),
\[
20:34,\quad24:102,\quad28:102,\quad32:17.
\]

For \(r=2\),
\[
30:34,\quad32:238,\quad34:986,\quad36:1955,\quad38:2890,\quad40:2873,\quad42:1462,\quad44:289,\quad46:68.
\]

For \(r=3\),
\[
38:323,\quad40:3417,\quad42:14280,\quad44:32130,\quad46:34119,\quad48:11832,\quad50:1054.
\]

For \(r=4\),
\[
\begin{aligned}
42&:17,\quad43:731,\quad44:2482,\quad45:8092,\quad46:20264,\\
47&:37978,\quad48:52649,\quad49:46988,\quad50:25279,\quad51:6307.
\end{aligned}
\]

For \(r=5\),
\[
46:510,\quad47:2482,\quad48:11067,\quad49:27132,\quad50:36074,\quad51:19890.
\]

For \(r=6\),
\[
48:85,\quad49:1020,\quad50:4182,\quad51:5508.
\]

For \(r=7\),
\[
50:51,\quad51:204,
\]
and for \(r=8\),
\[
51:1.
\]

Thus the numbers of subcodes attaining the generalized Hamming weights are
\[
34,\ 34,\ 323,\ 17,\ 510,\ 85,\ 51,\ 1.
\]

## Assumptions and scope

Use the finite-field realization printed in Example 1,
\[
\mathbb F_{256}
=
\mathbb F_2[\alpha]/(\alpha^8+\alpha^4+\alpha^3+\alpha^2+1).
\]
The source takes
\[
m=8,\qquad e=4,\qquad a_1=\alpha,\qquad a_2=\alpha^2
\]
in its Theorem 3.6 family. Hence
\[
2^e+1=17
\]
and the defining set is
\[
D=
\left\{
x\in\mathbb F_{256}^{*}:
\operatorname{Tr}(a_1x^{17})=0,\
\operatorname{Tr}(a_2x^{17})=0
\right\}.
\]
The binary code is
\[
C_D=
\left\{
(\operatorname{Tr}(bx))_{x\in D}:b\in\mathbb F_{256}
\right\}.
\]

The claim concerns this exact published Example 1 code. It does not assert that every code in Theorem 3.6 has the same higher-support profile.

## Proof

The defining polynomial makes \(\alpha\) primitive, so
\[
1,\alpha,\ldots,\alpha^7
\]
is an \(\mathbb F_2\)-basis of the message field. Direct evaluation of the two trace conditions gives
\[
|D|=51.
\]

Using the eight basis messages produces an \(8\times51\) binary generator matrix of rank \(8\). Enumerating all \(256\) messages gives
\[
A_0=1,\quad
A_{20}=34,\quad
A_{24}=102,\quad
A_{28}=102,\quad
A_{32}=17,
\]
exactly reproducing the source's published weight enumerator. This anchors the finite-field convention, trace implementation, defining set, and coordinate order to the published code before any higher-dimensional quantity is used.

Because the message-to-code map has rank \(8\), its restriction gives a bijection between \(r\)-dimensional message subspaces and \(r\)-dimensional code subcodes. Every message subspace has a unique reduced-row-echelon basis. The exact numbers of such subspaces for \(r=1,\ldots,8\) are
\[
255,\ 10795,\ 97155,\ 200787,\ 97155,\ 10795,\ 255,\ 1.
\]
Their sum is
\[
417198.
\]

For a basis
\[
u_1,\ldots,u_r
\]
of a message subspace, the support of the corresponding code subcode is exactly
\[
\operatorname{Supp}(c(u_1))
\cup\cdots\cup
\operatorname{Supp}(c(u_r)).
\]
Indeed, a coordinate vanishes on the whole subcode if and only if it vanishes on every basis word. Hence taking the bitwise union of the \(r\) basis supports computes the subcode support without approximation.

The exhaustive census evaluates this union for every one of the \(417198\) positive-dimensional message subspaces. The resulting histograms are exactly those in the Finding section. Taking the smallest support in each dimension yields
\[
(20,30,38,42,46,48,50,51).
\]

This is an exhaustive finite proof for the stated code: no sampling, timeout inference, or incomplete search is used.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It reconstructs \(\mathbb F_{256}\) from
\[
X^8+X^4+X^3+X^2+1,
\]
checks that the residue class of \(X\) has multiplicative order \(255\), implements the absolute trace by repeated squaring, and reconstructs the published defining set with \(a_1=\alpha\), \(a_2=\alpha^2\).

The verifier checks
\[
|D|=51,\qquad \dim C_D=8,
\]
and exactly reproduces
\[
1+34z^{20}+102z^{24}+102z^{28}+17z^{32}.
\]

It then enumerates every positive-dimensional subspace of \(\mathbb F_2^8\) once in reduced-row-echelon form, checks the expected Gaussian-binomial count in each dimension, computes every support union, and compares the full histogram with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article constructs self-orthogonal codes from the Gold-type function
\[
x\longmapsto x^{2^{m/2}+1}
\]
and determines their ordinary weight distributions. Example 1 explicitly gives the \([51,8,20]_2\) code and the four nonzero ordinary weights. The full text contains no generalized-Hamming-weight, weight-hierarchy, or subcode-support result.

Several nearby papers do determine weight hierarchies for other defining-set constructions. Qiao and Du study a cyclotomic family whose defining set lives in a product of finite fields and whose hierarchy is controlled by different exponential-sum parameters. Meng, Liu, Liu, Wang, and Zheng study two other self-orthogonal defining-set families and explicitly restrict their hierarchy theorems to those constructions. Li, Chen, and Qu provide a general defining-set formula and then solve selected Bent and Semi-Bent families; that framework does not by itself evaluate the maximization needed for the present intersection of two Gold trace-zero conditions, and it does not provide a complete subcode-support distribution.

Exact searches for the parameters
\[
[51,8,20]_2,
\]
the hierarchy
\[
(20,30,38,42,46,48,50,51),
\]
the published ordinary enumerator, and Gold-type higher-support terminology located no prior statement of this hierarchy or of the complete support spectra above.

## Limitations

The result is an exact finite classification for one highlighted code. It is not a closed formula for all even \(m\) in Theorem 3.6.

The complete support distribution is stronger than the generalized Hamming hierarchy but does not classify subcodes up to the automorphism group.

Generic defining-set formulas for generalized Hamming weights remain applicable in principle; the new content is the fully evaluated hierarchy and complete subcode-support census for this exact Gold-type example.

An unindexed computation or unpublished dataset could contain the same finite census; no such source was found in the inspected literature.

## References

1. Can Xiang and Yishan Song, *Binary self-orthogonal codes with few weights*, Advances in Mathematics of Communications 23 (2026), 146--156, DOI 10.3934/amc.2026017.
2. Kangquan Li, Hao Chen, and Longjiang Qu, *Generalized hamming weights of linear codes from cryptographic functions*, Advances in Mathematics of Communications 16 (2022), 859--877, DOI 10.3934/amc.2022081.
3. Xingbin Qiao and Xiaoni Du, *Weight distributions and weight hierarchies of a class of binary linear codes with a few weights*, Advances in Mathematics of Communications 19 (2025), 245--258, DOI 10.3934/amc.2023056.
4. Kunyi Meng, Chao Liu, Heguo Liu, Xiaoqiang Wang, and Dabin Zheng, *The weight distributions and weight hierarchies of two classes of self-orthogonal codes*, Advances in Mathematics of Communications 23 (2026), 127--145, DOI 10.3934/amc.2026016.
5. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
