# Complete higher-support profile of the new optimal \([96,6,48]\) Gray-image code
## Finding

Yadav, Tiwari, and Sarma's Example 4.4 gives a binary three-weight Gray-image code
\[
\Phi(C_D)
\]
with parameters
\[
[96,6,48]_2
\]
from
\[
q=2,\qquad m=3,\qquad A=\{1,2\},\qquad B=\{1,3\}.
\]

Its complete generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5,d_6)
=
(48,72,84,90,94,96).
\]

More strongly, the complete support-size distribution of subcodes is as follows. The notation \(w:N\) means that exactly \(N\) subcodes of the indicated dimension have support size \(w\).

For one-dimensional subcodes,
\[
48:58,\qquad 56:4,\qquad 64:1.
\]

For two-dimensional subcodes,
\[
72:504,\qquad 76:112,\qquad 80:33,\qquad 88:2.
\]

For three-dimensional subcodes,
\[
84:736,\qquad 86:448,\qquad 88:182,\qquad 92:28,\qquad 96:1.
\]

For four-dimensional subcodes,
\[
90:128,\qquad 91:256,\qquad 92:204,\qquad 94:56,\qquad 96:7.
\]

For five-dimensional subcodes,
\[
94:40,\qquad 95:16,\qquad 96:7.
\]

For the six-dimensional subcode,
\[
96:1.
\]

The one-dimensional line is exactly the ordinary weight enumerator already published in Example 4.4. The higher-dimensional distributions are the new part.

## Assumptions and scope

Let
\[
R=\mathbb F_2+u\mathbb F_2,\qquad u^2=0.
\]
For \(S\subseteq\{1,2,3\}\), let \(\Delta_S\) be the binary coordinate subspace supported on \(S\). The source uses
\[
D=(\Delta_A+u\Delta_B)^c\subset R^3.
\]

Write
\[
d=d_1+ud_2,\qquad v=a+ub.
\]
The Gray map used by the source turns the coordinate inner product into the two binary coordinates
\[
\langle b,d_1\rangle+\langle a,d_2\rangle
\]
and
\[
\langle a+b,d_1\rangle+\langle a,d_2\rangle.
\]

Identify the message space with
\[
V=\mathbb F_2^3\oplus\mathbb F_2^3
\cong\mathbb F_2^6
\]
in the order \((a,b)\).

## Proof

For a defining-set element \((d_1,d_2)\), the two Gray generator columns are
\[
(d_2,d_1)
\]
and
\[
(d_1+d_2,d_1).
\]
Both transformations of \((d_1,d_2)\) are invertible on \(\mathbb F_2^6\).

Since \(D\) is the complement of
\[
\Delta_A\times\Delta_B,
\]
the first \(48\)-column block is
\[
V\setminus S_1,
\qquad
S_1=\Delta_B\times\Delta_A,
\]
and the second \(48\)-column block is
\[
V\setminus S_2,
\qquad
S_2=
\{(d_1+d_2,d_1):d_1\in\Delta_A,\ d_2\in\Delta_B\}.
\]
Thus
\[
\dim S_1=\dim S_2=4.
\]

A vector \((x,y)\) lies in \(S_1\cap S_2\) exactly when
\[
x\in\Delta_B,\qquad
y\in\Delta_A\cap\Delta_B.
\]
Therefore
\[
\dim(S_1\cap S_2)
=
|B|+|A\cap B|
=
2+1
=
3.
\]

Let \(U\le V\) be the \(r\)-dimensional message subspace of an \(r\)-dimensional code subcode and put
\[
W=U^\perp,\qquad h=\dim W=6-r.
\]
A generator column is zero on all of \(U\) precisely when that column lies in \(W\). Set
\[
a=\dim(W\cap S_1),\qquad
b=\dim(W\cap S_2).
\]
The numbers of zero coordinates in the two column blocks are
\[
2^h-2^a
\]
and
\[
2^h-2^b,
\]
respectively. Hence the support size is exactly
\[
|\operatorname{Supp}(U)|
=
96-2^{h+1}+2^a+2^b
=
96-2^{7-r}+2^a+2^b.
\]

Grassmann's inequality gives
\[
a,b\ge\max(0,h+4-6)
=
\max(0,4-r).
\]
These two bounds are simultaneously attainable for every \(r\). For example, using six-bit row vectors in the coordinate order above, annihilator bases can be chosen as
\[
\begin{array}{c|l}
r&\text{basis of }W\\
\hline
1&000001,\ 000010,\ 000100,\ 001000,\ 110000\\
2&000001,\ 000010,\ 000100,\ 101000\\
3&000001,\ 000010,\ 100100\\
4&100001,\ 000010\\
5&100001\\
6&\varnothing.
\end{array}
\]
For each row,
\[
\dim(W\cap S_1)=\dim(W\cap S_2)=\max(0,4-r).
\]

Substitution gives
\[
d_r=
96-2^{7-r}+2^{1+\max(0,4-r)},
\]
hence
\[
(d_1,\ldots,d_6)
=
(48,72,84,90,94,96).
\]

For the complete distributions, every subspace of \(\mathbb F_2^6\) in dimensions \(1,\ldots,6\) was enumerated exactly once by its reduced-row-echelon basis. The numbers inspected are
\[
63,\ 651,\ 1395,\ 651,\ 63,\ 1,
\]
respectively, totaling
\[
2824.
\]
For every subspace, the support was computed twice: directly from the \(96\) reconstructed generator columns and from the intersection formula above. The two calculations agree identically and yield the stated spectra.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It reconstructs all
\[
64-16=48
\]
elements of \(D\), forms both Gray columns for each, and checks that the resulting \(6\times96\) generator has rank \(6\). The ordinary codeword census is verified to be
\[
1+58z^{48}+4z^{56}+z^{64},
\]
which exactly matches the source's Example 4.4.

The script independently constructs \(S_1\) and \(S_2\), verifies
\[
(\dim S_1,\dim S_2,\dim(S_1\cap S_2))=(4,4,3),
\]
and checks the support formula for every message subspace.

It then enumerates all \(2824\) positive-dimensional subspaces of \(\mathbb F_2^6\), compares the direct support histogram with the recorded certificate, and checks the hierarchy
\[
(48,72,84,90,94,96).
\]

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article determines the Lee and ordinary Hamming weight distributions of its Gray-image families. Example 4.4 states the \([96,6,48]_2\) parameters, ordinary three-weight enumerator, and distance optimality. The article contains no generalized-Hamming-weight or subcode-support analysis.

Pan, Chen, Liu, and Liu determine complete subcode-support distributions for several modified Solomon--Stiffler families. Their principal Griesmer construction begins with repeated simplex generators and deletes projective subspaces from a strictly nested chain
\[
U_1\subset U_2\subset\cdots\subset U_s
\]
with strictly increasing dimensions. The present generator has two deleted binary \(4\)-spaces \(S_1,S_2\) with
\[
\dim(S_1\cap S_2)=3,
\]
so they are distinct and non-nested. In the equivalent two-simplex-copy description, both deleted sets contain \(15\) nonzero vectors; matching that length would require two deleted \(4\)-spaces, which violates the strict-dimension condition of that construction.

Recent antiGriesmer work develops subcode-support distributions for simplex complementary and related optimal codes. Its publicly available abstract emphasizes projective codes and simplex complementary constructions. The present generator is nonprojective: among its \(56\) distinct nonzero binary columns, \(40\) occur twice and \(16\) occur once. Exact parameter and hierarchy searches did not identify this \([96,6,48]_2\) code in that literature.

The online optimal-code table confirms that minimum distance \(48\) is optimal for binary length \(96\), dimension \(6\), but a parameter table does not determine generalized Hamming weights or subcode-support multiplicities.

## Limitations

The complete census is for the specific Example 4.4 code with
\[
q=2,\quad m=3,\quad A=\{1,2\},\quad B=\{1,3\}.
\]
No general closed formula for all Gray images in Theorem 4.3 is claimed.

The four-dimensional and five-dimensional spectra contain odd support sizes because the two deleted column sets overlap nontrivially; this is a feature of the reconstructed generator multiset, not a statement about all members of the source family.

The comparison with the 2026 antiGriesmer paper is based on its public abstract and indexed descriptions rather than a full-text theorem-by-theorem comparison. No exact same-parameter coverage was located, but this remains a residual literature risk.

## References

1. Ankit Yadav, Akanksha Tiwari, and Ritumoni Sarma, *Linear Codes over \(\mathbb F_q+u\mathbb F_q\) associated with Simplicial Complexes, Their Gray Images, and Subfield Codes*, arXiv:2609.11783v1, 10 September 2026.
2. Xu Pan, Hao Chen, Hongwei Liu, and Shengwei Liu, *Optimal Few-SSW Linear Codes and Their Subcode Support Weight Distributions*, IEEE Transactions on Information Theory, DOI 10.1109/TIT.2024.3519672.
3. Conghui Xie, Hao Chen, Cunsheng Ding, and Chengju Li, *AntiGriesmer Bounds, Optimal Codes, and Their Subcode Support Weight Distributions*, IEEE Transactions on Information Theory 72 (2026), 2133--2143, DOI 10.1109/TIT.2026.3665706.
4. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
