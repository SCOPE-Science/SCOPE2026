# Complete higher-support profile of a projective minimal binary \([24,6,10]\) trace code
## Finding

For the \(m=3\), \(d=1\) member of the binary trace-code family \(C_{D_1}\) of Liao, Zhang, and Zheng, let
\[
D_1=
\{(x,y)\in\mathbb F_8^*\times\mathbb F_8:
\operatorname{Tr}_{8/2}(x^2y+xy+x)=0\}.
\]
The resulting code has the published parameters
\[
[24,6,10]_2
\]
and ordinary weight enumerator
\[
1+24z^{10}+12z^{12}+24z^{14}+3z^{16}.
\]

Its complete generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5,d_6)
=
(10,15,19,21,23,24).
\]

More strongly, the complete support-size distributions of its subcodes are as follows. The notation \(w:N\) means that exactly \(N\) subcodes of the indicated dimension have support size \(w\).

For \(r=1\),
\[
10:24,\qquad 12:12,\qquad 14:24,\qquad 16:3.
\]

For \(r=2\),
\[
15:32,\quad16:72,\quad17:96,\quad18:172,\quad19:96,\quad20:138,\quad21:32,\quad22:12,\quad24:1.
\]

For \(r=3\),
\[
19:144,\quad20:114,\quad21:576,\quad22:288,\quad23:240,\quad24:33.
\]

For \(r=4\),
\[
21:32,\qquad22:180,\qquad23:288,\qquad24:151.
\]

For \(r=5\),
\[
23:24,\qquad24:39.
\]

For the unique six-dimensional subcode,
\[
24:1.
\]

Thus the generalized Hamming weights are attained by exactly
\[
24,\ 32,\ 144,\ 32,\ 24,\ 1
\]
subcodes in dimensions \(1,\ldots,6\), respectively.

## Assumptions and scope

Use
\[
\mathbb F_8=\mathbb F_2[\alpha]/(\alpha^3+\alpha+1)
\]
and
\[
\operatorname{Tr}_{8/2}(u)=u+u^2+u^4.
\]
For the source construction with \(m=3\) and \(d=1\), define
\[
D_1=
\{(x,y)\in\mathbb F_8^*\times\mathbb F_8:
\operatorname{Tr}_{8/2}(x^2y+xy+x)=0\}.
\]
For \(a,b\in\mathbb F_8\), the codeword is
\[
c_{a,b}
=
\bigl(\operatorname{Tr}_{8/2}(a x y+b x)\bigr)_{(x,y)\in D_1}.
\]

The claim concerns this exact source member. It does not assert the same complete support distribution for every member of the general family.

## Proof

Direct evaluation of the trace condition gives
\[
|D_1|=24.
\]
Choose the six-dimensional binary message basis
\[
(1,0),\quad(\alpha,0),\quad(\alpha^2,0),\quad
(0,1),\quad(0,\alpha),\quad(0,\alpha^2).
\]
Evaluation on the \(24\) points of \(D_1\) produces a binary generator matrix \(G\) of rank \(6\).

Before computing higher-dimensional invariants, enumerate all
\[
2^6=64
\]
messages. The resulting ordinary weight distribution is
\[
A_0=1,\qquad A_{10}=24,\qquad A_{12}=12,\qquad A_{14}=24,\qquad A_{16}=3,
\]
which exactly reproduces the source table and fixes the finite-field and trace conventions.

Because the message map is an isomorphism
\[
\mathbb F_2^6\longrightarrow C_{D_1},
\]
\(r\)-dimensional code subcodes correspond bijectively to \(r\)-dimensional message subspaces. Every binary message subspace has a unique reduced-row-echelon basis. The exact numbers of \(r\)-subspaces are
\[
63,\ 651,\ 1395,\ 651,\ 63,\ 1
\]
for \(r=1,\ldots,6\), respectively, for a total of
\[
2824
\]
positive-dimensional subspaces.

If
\[
u_1,\ldots,u_r
\]
is a message-subspace basis, then the support of the corresponding code subcode is exactly
\[
\operatorname{Supp}(u_1G)\cup\cdots\cup\operatorname{Supp}(u_rG).
\]
A coordinate is absent from that union exactly when all basis words vanish there, equivalently when every word of the generated subcode vanishes there.

Therefore exhaustive reduced-row-echelon enumeration of all \(2824\) message subspaces gives every code subcode exactly once. Counting each support union yields the six distributions in the Finding, and taking the minimum in each dimension gives
\[
(10,15,19,21,23,24).
\]

This is an exhaustive finite proof for the stated code; no sampling or incomplete search is used.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It implements arithmetic in
\[
\mathbb F_8=\mathbb F_2[\alpha]/(\alpha^3+\alpha+1),
\]
constructs \(D_1\) from its trace equation, forms the six generator rows, checks rank \(6\), and reproduces the published ordinary enumerator.

The script then enumerates every positive-dimensional subspace of \(\mathbb F_2^6\) exactly once in reduced-row-echelon form. For each basis it computes the union of the corresponding codeword supports and compares the complete histogram with `artifacts/certificate.json`.

The checked subspace totals are
\[
63,\ 651,\ 1395,\ 651,\ 63,\ 1,
\]
and successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article proves that this \(D_1\) construction yields projective minimal four-weight binary codes and gives, for \(m=3\), the \([24,6,10]_2\) example with the ordinary enumerator above. It does not determine generalized Hamming weights or complete subcode-support distributions.

Recent work on complete subcode-support weight distributions treats several few-weight optimal families built from simplex, modified Solomon--Stiffler, and simplex-complement constructions. No exact specialization to this trace-defined \([24,6,10]_2\) code was found.

The parameter triple does not identify the code. A previously classified binary self-orthogonal \([24,6,10]\) code has ordinary enumerator
\[
1+18z^{10}+28z^{12}+12z^{14}+3z^{16}+2z^{18},
\]
which differs from the exact source enumerator here. It therefore cannot be equivalent to this code.

Focused searches using the exact parameters, the source construction, the ordinary enumerator, the hierarchy
\[
(10,15,19,21,23,24),
\]
and subcode-support terminology found no prior complete higher-support profile for this exact object.

## Limitations

The result is a complete finite census for the \(m=3\), \(d=1\) member only. It does not supply a closed higher-support formula for arbitrary \(m\) or \(d\).

The census classifies subcodes by support size, not by automorphism-group orbit.

The source's projectivity, minimality, parameters, and ordinary enumerator are prior work. Only the higher-dimensional support spectra, generalized Hamming hierarchy, and exact minimizer multiplicities are claimed as new.

An unindexed computation or differently presented equivalent code could contain the same finite profile, although no such coverage was located in the searches performed.

## References

1. Qunying Liao, Zhaohui Zhang, and Peipei Zheng, *Several classes of three-weight or four-weight linear codes*, arXiv:2511.01309v1, first public version 3 November 2025; Journal of the Korean Mathematical Society 63 (2026), 493--508, DOI 10.4134/JKMS.j240479.
2. Xu Pan, Hao Chen, Hongwei Liu, and Shengwei Liu, *Optimal Few-SSW Linear Codes and Their Subcode Support Weight Distributions*, IEEE Transactions on Information Theory 71 (2025), 1028--1042, DOI 10.1109/TIT.2024.3519672; arXiv:2408.10005.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
