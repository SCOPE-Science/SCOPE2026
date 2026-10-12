# Complete higher-support profile of the Gold-type binary \([119,8,56]\) code
## Finding

Xiang and Song's Example 1 gives a binary Gold-type defining-set code with parameters
\[
[119,8,56]_2
\]
and ordinary weight enumerator
\[
1+136z^{56}+119z^{64}.
\]

For that exact code, the complete generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8)
=
(56,84,100,108,112,116,118,119).
\]

More strongly, the complete support-size distribution is determined in every subcode dimension. The notation \(w:N\) means that exactly \(N\) subcodes of the indicated dimension have support size \(w\).

For \(r=1\),
\[
56:136,\qquad64:119.
\]

For \(r=2\),
\[
84:1632,\qquad88:4284,\qquad92:3808,\qquad96:1071.
\]

For \(r=3\),
\[
100:14280,\qquad104:56406,\qquad108:25704,\qquad112:765.
\]

For \(r=4\),
\[
108:10710,\quad110:45696,\quad112:87975,\quad114:45696,\quad116:10710.
\]

For \(r=5\),
\[
112:765,\qquad114:25704,\qquad116:56406,\qquad118:14280.
\]

For \(r=6\),
\[
116:1071,\qquad117:3808,\qquad118:4284,\qquad119:1632.
\]

For \(r=7\),
\[
118:119,\qquad119:136.
\]

For the unique eight-dimensional subcode,
\[
119:1.
\]

Consequently, the generalized-weight minima are attained by exactly
\[
136,\ 1632,\ 14280,\ 10710,\ 765,\ 1071,\ 119,\ 1
\]
subcodes in dimensions \(1,\ldots,8\), respectively.

## Assumptions and scope

Use the source field model
\[
\mathbb F_{256}=\mathbb F_2[\alpha]/(\alpha^8+\alpha^4+\alpha^3+\alpha^2+1),
\]
where \(\alpha\) is primitive. Put
\[
a_1=\alpha^{17},
\qquad
a_2=\alpha.
\]
Since \(a_1\in\mathbb F_{16}\setminus\mathbb F_2\) and \(a_2\notin\mathbb F_{16}\), this is the first instance in the source's Example 1 and falls under its two-weight Theorem 3.5.

With the absolute trace
\[
\operatorname{Tr}(u)=u+u^2+\cdots+u^{128},
\]
define
\[
D=
\left\{
x\in\mathbb F_{256}^*:
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

The claim concerns this exact source representative. It does not assert that every binary \([119,8,56]\) code has this complete support profile.

## Proof

Direct evaluation of the two trace equations gives
\[
|D|=119.
\]
Using the polynomial basis
\[
1,\alpha,\ldots,\alpha^7
\]
for \(\mathbb F_{256}/\mathbb F_2\), evaluate the eight corresponding codewords
\[
(\operatorname{Tr}(\alpha^i x))_{x\in D},
\qquad 0\le i<8.
\]
They have binary rank \(8\), so the message map
\[
\mathbb F_2^8\longrightarrow C_D
\]
is an isomorphism.

Before computing higher-dimensional invariants, enumerate all
\[
2^8=256
\]
messages. The exact ordinary weight distribution is
\[
A_0=1,\qquad A_{56}=136,\qquad A_{64}=119,
\]
reproducing the source's Example 1 and fixing the field, trace, and defining-set conventions.

Every \(r\)-dimensional code subcode therefore corresponds uniquely to an \(r\)-dimensional message subspace. Every message subspace has a unique reduced-row-echelon basis. The exact numbers of such subspaces in dimensions \(1,\ldots,8\) are
\[
255,\ 10795,\ 97155,\ 200787,\ 97155,\ 10795,\ 255,\ 1.
\]
Their total is
\[
417198.
\]

For a basis
\[
u_1,\ldots,u_r
\]
of a message subspace, the support of the generated code subcode is
\[
\operatorname{Supp}(c(u_1))\cup\cdots\cup\operatorname{Supp}(c(u_r)).
\]
Indeed, a coordinate vanishes on the entire generated subcode if and only if it vanishes on every basis word.

Thus exact enumeration of all \(417198\) positive-dimensional message subspaces exhausts all code subcodes. Counting each support union gives precisely the distributions stated in the Finding. Taking the minimum support in each dimension gives
\[
(56,84,100,108,112,116,118,119).
\]

This is a finite exhaustive proof for the exact source code. No sampling, partial enumeration, or extrapolation is used.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It implements
\[
\mathbb F_{256}=\mathbb F_2[\alpha]/(\alpha^8+\alpha^4+\alpha^3+\alpha^2+1),
\]
checks that \(\alpha\) has multiplicative order \(255\), verifies
\[
\alpha^{17}\in\mathbb F_{16}\setminus\mathbb F_2,
\]
constructs the defining set from the two source trace equations, and checks
\[
|D|=119.
\]

The verifier forms the eight evaluation rows, checks rank \(8\), verifies pairwise Euclidean self-orthogonality, and reproduces the published ordinary enumerator
\[
1+136z^{56}+119z^{64}.
\]

It then enumerates every binary subspace of the eight-dimensional message space exactly once in reduced-row-echelon form. In each dimension it checks the census size against the Gaussian binomial coefficient and compares the full support histogram with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Xiang and Song construct the code from a Gold-type function. Their Theorem 3.5 determines the two-weight family, and Example 1 explicitly gives this \([119,8,56]_2\) member and its ordinary weight enumerator. Their article contains no generalized-Hamming-weight or subcode-support computation for the family.

Weight hierarchies of several other defining-set families have been studied extensively. In particular, Qiao and Du determine complete hierarchies for a different family whose defining sets live in a product field geometry; their full text contains neither the parameter \(119\) nor the present Gold-type \(x^{17}\) specialization. General defining-set formulas similarly reduce generalized weights to subspace-intersection extrema but do not evaluate the present code's complete support distribution.

Complete subcode-support distributions are strictly finer than a generalized-weight hierarchy. Focused searches using the exact source, the parameters, the ordinary enumerator, the Gold-type defining equations, the resulting hierarchy, and support-distribution terminology did not locate a prior statement of the spectra above.

## Limitations

The result is a complete finite census for the first \(m=8\) code in Example 1. It does not provide a closed higher-support formula for all even \(m\) in Theorem 3.5.

The support census classifies subcodes by support size, not by automorphism-group orbit.

The parameters, self-orthogonality, minimality, and ordinary weight enumerator are prior work. Only the higher-dimensional support spectra, generalized Hamming hierarchy, and exact minimizer multiplicities are claimed as new.

An equivalent presentation in an unindexed database or older two-weight-code classification could contain the same finite invariants; no such support-distribution statement was located in the inspected sources.

## References

1. Can Xiang and Yishan Song, *Binary self-orthogonal codes with few weights*, Advances in Mathematics of Communications 23 (2026), 146--156, DOI 10.3934/amc.2026017.
2. Xingbin Qiao and Xiaoni Du, *Weight distributions and weight hierarchies of a class of binary linear codes with a few weights*, Advances in Mathematics of Communications 19 (2025), 245--258, DOI 10.3934/amc.2023056.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
