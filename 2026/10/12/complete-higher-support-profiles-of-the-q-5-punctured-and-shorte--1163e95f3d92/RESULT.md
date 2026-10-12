# Complete higher-support profiles of the \(q=5\) punctured and shortened two-zero codes
## Finding

Hernández and Vega's Example 2(b) starts from the cyclic code
\[
\mathcal C_{(20,13)}
\]
over \(\mathbb F_5\), then punctures and shortens one coordinate.

The punctured code
\[
\mathcal C_{(20,13)}^*
\]
has the published parameters
\[
[23,4,15]_5
\]
and published ordinary weight enumerator
\[
1+72z^{15}+36z^{16}+228z^{18}+80z^{19}+172z^{20}+24z^{21}+12z^{23}.
\]
Its complete subcode-support distributions are
\[
r=1:\quad 15:18,\ 16:9,\ 18:57,\ 19:20,\ 20:43,\ 21:6,\ 23:3,
\]
\[
r=2:\quad 19:5,\ 20:29,\ 21:136,\ 22:334,\ 23:302,
\]
\[
r=3:\quad 22:23,\ 23:133,
\]
and
\[
r=4:\quad 23:1.
\]
Thus
\[
(d_1,d_2,d_3,d_4)=(15,19,22,23),
\]
and the numbers of subcodes attaining these minima are
\[
18,\ 5,\ 23,\ 1.
\]

The shortened companion
\[
\mathcal C_{(20,13)*}
\]
has the published parameters
\[
[23,3,16]_5
\]
and published ordinary weight enumerator
\[
1+36z^{16}+60z^{19}+4z^{20}+24z^{21}.
\]
Its complete subcode-support distributions are
\[
r=1:\quad 16:9,\ 19:15,\ 20:1,\ 21:6,
\]
\[
r=2:\quad 20:1,\ 21:4,\ 22:12,\ 23:14,
\]
and
\[
r=3:\quad 23:1.
\]
Therefore
\[
(d_1,d_2,d_3)=(16,20,23),
\]
with minimizer multiplicities
\[
9,\ 1,\ 1.
\]

Here \(w:N\) means that exactly \(N\) subcodes of the indicated dimension have support size \(w\).

## Assumptions and scope

Use
\[
\mathbb F_{25}=\mathbb F_5[\gamma]/(\gamma^2+\gamma+2),
\]
where \(\gamma\) has multiplicative order \(24\). For the source parameters
\[
(q,e_1,e_2)=(5,5,13),
\]
the original cyclic code is represented by
\[
c(a,b)=\left(\operatorname{Tr}_{25/5}\left(a\gamma^{20i}+b\gamma^{13i}\right)\right)_{i=0}^{23},
\qquad a,b\in\mathbb F_{25}.
\]
This is exactly the Delsarte trace representation used in the source.

Puncturing is performed at coordinate \(i=0\). Because the original code is cyclic, puncturing at any one coordinate gives an equivalent code. Shortening is performed at the same coordinate by restricting to messages whose \(i=0\) coordinate is zero and then deleting that coordinate.

The claim concerns only these two \(q=5\) companion codes from Example 2(b). It does not claim an all-\(q\) closed formula for higher support distributions.

## Proof

Take the \(\mathbb F_5\)-basis
\[
1,\gamma
\]
of \(\mathbb F_{25}\). The four messages
\[
(1,0),\ (\gamma,0),\ (0,1),\ (0,\gamma)
\]
give a \(4\times24\) generator matrix for \(\mathcal C_{(20,13)}\).

The generator has rank \(4\). Enumerating its \(5^4\) messages gives exactly
\[
1+108z^{16}+288z^{19}+24z^{20}+192z^{21}+12z^{24},
\]
which is the ordinary weight enumerator published for the original cyclic code. This independently fixes the field, trace, exponent, and coordinate conventions.

Delete coordinate \(0\). The resulting \(4\times23\) generator has rank \(4\) and its ordinary enumerator is exactly
\[
1+72z^{15}+36z^{16}+228z^{18}+80z^{19}+172z^{20}+24z^{21}+12z^{23},
\]
matching the source punctured code.

For shortening, impose the single linear condition that coordinate \(0\) vanish. Its solution space in the four-dimensional message space has dimension \(3\). Evaluating a basis of that kernel and then deleting coordinate \(0\) gives a \(3\times23\) generator whose ordinary enumerator is
\[
1+36z^{16}+60z^{19}+4z^{20}+24z^{21},
\]
again exactly matching the source.

Because both evaluation maps have full message rank, message subspaces correspond bijectively to code subcodes. The numbers of positive-dimensional subspaces of \(\mathbb F_5^4\) are
\[
156,\ 806,\ 156,\ 1,
\]
while those of \(\mathbb F_5^3\) are
\[
31,\ 31,\ 1.
\]
Every such subspace has a unique reduced-row-echelon basis.

For a basis \(u_1,\ldots,u_r\), the support of the generated subcode is exactly
\[
\operatorname{Supp}(c(u_1))\cup\cdots\cup\operatorname{Supp}(c(u_r)).
\]
Thus exhaustive RREF enumeration gives every support size and multiplicity without sampling. The resulting histograms are exactly those stated in the Finding, and their minima give the two generalized Hamming-weight hierarchies.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It constructs \(\mathbb F_{25}\), verifies that \(\gamma\) has order \(24\), implements the trace \(\operatorname{Tr}_{25/5}\), and reconstructs the source trace generator. It checks the original, punctured, and shortened ordinary weight enumerators against the published values.

It then enumerates all
\[
1119
\]
positive-dimensional subspaces of the punctured code's message space and all
\[
63
\]
positive-dimensional subspaces of the shortened code's message space. Each full support histogram is compared with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article determines the ordinary weight distributions of the two-zero cyclic family and of its punctured and shortened companions. Example 1(b) gives the original \([24,4,16]_5\) cyclic code; Theorem 7 gives general puncturing and shortening formulas; Example 2(b) explicitly records the two \(q=5\) companion codes and their ordinary enumerators. The paper contains no generalized-Hamming-weight or subcode-support distribution analysis.

Pan, Chen, Liu, and Liu develop the modern subcode-support-weight-distribution framework and determine complete distributions for several distance-optimal families built from modified Solomon--Stiffler codes and simplex-complement constructions. Their public full preprint defines the same invariant and gives the general column-incidence formula, but an exact full-text search contains no \([23,4,15]\) instance, and their listed constructions are different from this punctured two-zero cyclic code.

The exact parameter searches \([23,4,15]_5\) and \([23,3,16]_5\), searches by the ordinary enumerators, and searches by the source notation \(\mathcal C_{(20,13)}\) found no prior complete higher-support profile for these two companions.

## Limitations

The result is a complete finite census for the \(q=5\) punctured/shortened pair only. It is not a formula for all odd \(q\) in Theorem 7.

The source's ordinary weight enumerators and code parameters are prior work. The new content is only the higher-dimensional support spectra, generalized Hamming weights, and extremal multiplicities.

The broad SSWD literature contains many code families and duality formulas, so a differently presented equivalent code remains a residual literature risk. No exact parameter or enumerator match was found in the inspected sources.

## References

1. Félix Hernández and Gerardo Vega, *Few-weight linear codes and their application to secret sharing*, Applicable Algebra in Engineering, Communication and Computing, published 30 September 2026, DOI 10.1007/s00200-026-00758-1.
2. Xu Pan, Hao Chen, Hongwei Liu, and Shengwei Liu, *Optimal Few-SSW Linear Codes and Their Subcode Support Weight Distributions*, IEEE Transactions on Information Theory 71 (2025), 1028--1042, DOI 10.1109/TIT.2024.3519672; arXiv:2408.10005.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
