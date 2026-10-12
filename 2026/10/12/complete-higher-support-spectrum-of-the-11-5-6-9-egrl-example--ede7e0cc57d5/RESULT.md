# Complete higher-support spectrum of the \([11,5,6]_9\) EGRL example
## Finding

For the explicit code in Liang--Liao Example 6.1, let \(N_r(s)\) denote the number of \(r\)-dimensional subcodes whose union of coordinate supports has size \(s\). The code has parameters
\[
[11,5,6]_9.
\]
Its complete higher-support spectra are
\[
\begin{aligned}
N_1&=\{6:28,\ 7:190,\ 8:610,\ 9:1755,\ 10:2780,\ 11:2018\},\\
N_2&=\{8:165,\ 9:4510,\ 10:72567,\ 11:528000\},\\
N_3&=\{9:55,\ 10:8910,\ 11:596277\},\\
N_4&=\{10:11,\ 11:7370\},\\
N_5&=\{11:1\}.
\end{aligned}
\]
Therefore the generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5)=(6,8,9,10,11),
\]
and the numbers of subcodes attaining these five minima are respectively
\[
(28,165,55,11,1).
\]
The generalized hierarchy itself is a standard consequence of the NMDS condition and is not the originality claim here. The new finite invariant is the complete dimension-by-dimension support census, including the minimizing-subcode multiplicities.

## Assumptions and scope

The calculation uses exactly the \(5\times11\) generator matrix printed in Example 6.1 of Liang--Liao. The field is realized as
\[
\mathbb F_9=\mathbb F_3[\omega]/(\omega^2-\omega-1).
\]
The source specifies only that \(\omega\) is primitive. In this realization the four primitive elements are \(\omega^e\) with \(e\in\{1,3,5,7\}\). The complete computation is repeated for all four choices, and the spectra above are unchanged.

No assertion is made for every code in the EGRL family or for every \([11,5,6]_9\) code. The statement concerns the displayed Example 6.1 construction, with the primitive-element ambiguity checked explicitly.

## Proof

Let \(G\) be the displayed full-rank generator matrix and let \(U\leq\mathbb F_9^5\) be an \(r\)-dimensional message subspace. The corresponding subcode is
\[
UG=\{uG:u\in U\}.
\]
If \(B=(u_1,\ldots,u_r)\) is any basis of \(U\), then a coordinate belongs to the support of \(UG\) exactly when at least one of the basis words \(u_iG\) is nonzero in that coordinate. Hence
\[
|\operatorname{Supp}(UG)|
=\left|\operatorname{Supp}(u_1G)\cup\cdots\cup\operatorname{Supp}(u_rG)\right|.
\]
Every \(r\)-dimensional subspace of \(\mathbb F_9^5\) has a unique reduced-row-echelon basis matrix. Enumerating those matrices therefore counts every subcode exactly once. The required numbers of subspaces are the Gaussian binomial coefficients
\[
\binom{5}{1}_9=7381,\quad
\binom{5}{2}_9=605242,\quad
\binom{5}{3}_9=605242,\quad
\binom{5}{4}_9=7381,\quad
\binom{5}{5}_9=1.
\]
For each reduced-row-echelon basis, direct coordinatewise multiplication by \(G\) gives the support union. Tallying those unions yields exactly the five spectra in the finding.

As a source-anchor check, enumerating all \(9^5\) messages reproduces the published ordinary weight enumerator
\[
1+224z^6+1520z^7+4880z^8+14040z^9+22240z^{10}+16144z^{11}.
\]
Dividing each nonzero coefficient by \(8\) gives the \(r=1\) support counts above, as required because each one-dimensional subcode contains exactly \(8\) nonzero words.

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs \(\mathbb F_9\), the printed generator, all \(9^5\) codewords, and every message subspace in unique reduced-row-echelon form. It checks the published ordinary weight enumerator first, then the five complete subcode-support spectra and their Gaussian-binomial totals.

The entire verification is repeated for all four primitive choices \(\omega^e\), \(e\in\{1,3,5,7\}\). A successful replay ends with `VERIFY_OK`.

## Relationship to prior work

Liang and Liao introduce the EGRL construction, prove the relevant family is NMDS, and completely determine its ordinary codeword weight distribution. Their Example 6.1 prints the \([11,5,6]_9\) generator and its ordinary weight enumerator. Full-text searches of the primary manuscript locate no discussion of generalized Hamming weights, subcodes, or a weight hierarchy beyond ordinary codeword supports.

Classical generalized-weight theory characterizes the generalized Hamming hierarchy of NMDS codes, so the sequence \((6,8,9,10,11)\) is not presented as new. That theory does not determine how many subcodes have each possible support size. The complete spectra above refine both the NMDS hierarchy and the source's ordinary weight enumerator by recording higher-dimensional support incidence.

Focused searches for the exact parameters, EGRL/Roth--Lempel aliases, generalized-Hamming terminology, the number \(165\) of minimum-support two-dimensional subcodes, and the full support-spectrum formulation found no prior statement of these multiplicities. The closest published research-record item concerns Galois hull dimensions of full-field generalized Roth--Lempel codes, a different invariant that does not imply the subcode-support census.

## Limitations

This is an exact finite classification for one newly displayed EGRL code, not a closed formula for the entire EGRL family. It does not classify the equivalence class of the code among all \([11,5,6]_9\) NMDS codes.

An unindexed historical computation for an equivalent code could in principle contain the same support census. The searches performed did not locate such a computation. The ordinary weight enumerator and the generalized Hamming hierarchy are explicitly excluded from the originality claim.

## References

1. Zhonghao Liang and Qunying Liao, *The extended code for a class of generalized Roth-Lempel codes and their properties*, arXiv:2508.12302v1, first public 17 August 2025; Discrete Mathematics 349 (2026), 115084, DOI 10.1016/j.disc.2026.115084.
2. G. Viswanath and B. Sundar Rajan, *Matrix characterization of linear codes with arbitrary Hamming weight hierarchy*, Linear Algebra and its Applications 412 (2006), 396--407, DOI 10.1016/j.laa.2005.07.008.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
