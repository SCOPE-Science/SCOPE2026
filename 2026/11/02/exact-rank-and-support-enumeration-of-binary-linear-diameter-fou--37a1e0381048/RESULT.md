# Exact rank-and-support enumeration of binary linear diameter-four anticodes

## Finding

Let \(\mathbb F_2\) be the binary field. For each integer \(n\ge0\), let \(B_{n,k}\) count the \(k\)-dimensional linear subspaces \(C\le\mathbb F_2^n\) with Hamming diameter at most four. Then

\[
 B_{n,k}=\sum_{s=0}^{7}a_{s,k}\binom{n}{s}\quad(0\le k\le4),\qquad B_{n,k}=0\quad(k>4),
\]

where \(a_{s,k}\) counts admissible codes having **exactly** \(s\) occupied coordinates and dimension \(k\) on a fixed labelled \(s\)-element support. Their complete values are:

| \(s\) | \(k=0\) | \(k=1\) | \(k=2\) | \(k=3\) | \(k=4\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 2 | 0 | 1 | 1 | 0 | 0 |
| 3 | 0 | 1 | 4 | 1 | 0 |
| 4 | 0 | 1 | 13 | 11 | 1 |
| 5 | 0 | 0 | 25 | 55 | 11 |
| 6 | 0 | 0 | 15 | 75 | 10 |
| 7 | 0 | 0 | 0 | 30 | 0 |

In particular, the exact total number for every \(n\ge0\) is

\[
 \boxed{\left|\mathcal L_2(n,4)\right|=
 1+\binom{n}{1}+2\binom{n}{2}+6\binom{n}{3}+26\binom{n}{4}
 +91\binom{n}{5}+100\binom{n}{6}+30\binom{n}{7}.}
\]

The leading term is \(n^7/168\). Among codes with seven occupied coordinates, all have dimension three and are the binary seven-coordinate simplex code up to coordinate permutation: there are precisely \(30\) labelled copies on each seven-element coordinate set.

## Assumptions and scope

Coordinates are labelled and subspaces are distinguished as actual subsets of \(\mathbb F_2^n\), not modulo permutations or code equivalence. The zero subspace is included. The diameter of a linear subspace is \(\max_{c\in C}\operatorname{wt}(c)\), because differences of its elements range over all of \(C\). The inequality is **at most** four. A coordinate lies in \(\operatorname{supp}(C)\) when some codeword has a nonzero entry there. In the displayed formula, \(\binom{n}{s}=0\) when \(s>n\). The proof and the table apply for every finite \(n\ge0\), including \(n<4\).

## Proof

**1. Finite support and rank.** Let \(k=\dim C\). In a reduced row-echelon generator matrix, summing all \(k\) rows produces a codeword with a nonzero entry in every pivot column, so \(k\le4\). On its exact support of size \(s\), a full-support \(k\)-dimensional binary code has a generator matrix with no zero column. Each nonzero column contributes exactly \(2^{k-1}\) ones among all \(2^k\) codewords. Since the zero codeword has weight zero and the other \(2^k-1\) words each have weight at most four,

\[
 s2^{k-1}=\sum_{c\in C}\operatorname{wt}(c)\le4(2^k-1).
\]

For \(1\le k\le4\), this yields \(s\le8-2^{3-k}\), and in particular \(s\le7\). For \(k=0\), only the zero code with \(s=0\) occurs. Thus all admissible subspaces are completely controlled by the finite parameters \(0\le k\le4\), \(0\le s\le7\).

**2. Exact finite formula for every entry.** Fix \(s\ge1\), \(1\le k\le\min\{s,4\}\). For every nonzero binary column vector \(v\in\mathbb F_2^k\), let \(m_v\) be its multiplicity in a generator matrix. Define \(\mathscr M_{s,k}\) to consist of multiplicity vectors satisfying

\[
 \sum_{v\ne0}m_v=s,\qquad
 \operatorname{span}\{v:m_v>0\}=\mathbb F_2^k,\qquad
 \sum_{\substack{v\ne0\\u\cdot v=1}}m_v\le4\quad
 \text{for every }0\ne u\in\mathbb F_2^k.
\]

These conditions say exactly that the generator has full column support, rank \(k\), and no codeword heavier than four. Every admissible multiplicity vector specifies \(s!/\prod_{v\ne0}m_v!\) ordered generator matrices. Each \(k\)-dimensional row space has precisely

\[
 |\operatorname{GL}(k,2)|=\prod_{i=0}^{k-1}(2^k-2^i)
\]

ordered bases, which act freely on its full-rank generators. Hence the exact, finite identity

\[
 a_{s,k}=
 \frac{1}{|\operatorname{GL}(k,2)|}
 \sum_{(m_v)\in\mathscr M_{s,k}}
 \frac{s!}{\prod_{v\ne0}m_v!}.
\]

Evaluation of this fully specified finite integer sum for every pair \((s,k)\) in the proven ranges produces the displayed table. The supplied `verify.py` carries out the complete finite evaluation by this multiset method and independently by a direct exhaustive enumeration of all reduced row-echelon subspace bases. Both procedures enumerate the entirety of their provably finite parameter spaces; neither uses sampling or a numerical tolerance. The exact coefficients, rather than just sampled totals at selected lengths, form the computational certificate.

**3. All lengths.** Each code has a unique exact support \(S\subseteq[n]\). Puncturing outside \(S\) gives a unique full-support code on the \(s=|S|\) labelled coordinates of \(S\), and conversely each such code extends uniquely by zeros. Thus the number of dimension-\(k\), support-\(s\) codes in \(\mathbb F_2^n\) is \(a_{s,k}\binom{n}{s}\). Sum over \(s\) and over \(k\) to obtain the two asserted polynomial formulas for **all** \(n\).

**4. The seven-coordinate boundary is the simplex class.** Suppose a full-support code has \(s=7\) and every nonzero word weighs at most four. The weight sum \(7\cdot2^{k-1}\le4(2^k-1)\) rules out \(k=1,2\). If \(k=4\), the fifteen nonzero word weights \(w_u\) have sum \(56\). Put \(\delta_u=4-w_u\); each is an integer from zero to three because a nonzero codeword cannot have weight zero, and \(\sum\delta_u=4\). Therefore \(\sum\delta_u^2\le10\) and

\[
 \sum_{u\ne0}w_u^2=
 15\cdot16-8\cdot4+\sum_{u\ne0}\delta_u^2\le218.
\]

But seven nonzero generator columns yield \(\sum w_u^2=224+8E\ge224\), where \(E\) counts equal pairs of columns: each single column contributes eight across nonzero row combinations, each pair of distinct columns contributes four, and each equal pair contributes eight to their product sum. Contradiction. Hence \(k=3\). Equality in the weight-sum bound now forces each of seven nonzero codewords to have weight four. The Walsh transform of the multiplicity vector on \(\mathbb F_2^3\) gives for each \(u\ne0\)

\[
 \sum_{v\ne0}m_v(-1)^{u\cdot v}=7-2\cdot4=-1,
\]

while its zero-frequency sum is seven. Fourier inversion therefore forces \(m_v=1\) for all seven nonzero \(v\), the seven-column binary simplex code. Conversely that generator has every nonzero word of weight four. Ordered permutations of its seven distinct generator columns give \(7!\) full-rank matrices, and each three-dimensional row space is represented \(|\operatorname{GL}(3,2)|=168\) times. Therefore there are exactly \(7!/168=30\) such labelled codes.

## Verification

The attached `verify.py` uses only Python's standard library. Execute `python3 verify.py` in the directory containing this file; the terminal must end in `VERIFY_OK`. Its first algorithm lists every \(s\)-column reduced row-echelon generator for \(s=0,\ldots,7\), \(k=0,\ldots,4\), computes the complete row space, rejects any word of weight above four, and tests full coordinate support. Its second algorithm independently lists the multisets of nonzero \(k\)-bit generator columns, checks span and all nonzero row-combination weights, applies the multinomial multiplicity, and divides by \(|\operatorname{GL}(k,2)|\). It asserts equality with every displayed table entry, not just totals, and checks the total polynomial at ten specified lengths. Completed execution returned `VERIFY_OK`; both algorithms agreed for all \(8\cdot5\) support-rank cells.

An elementary length-five cross-check is available without enumeration: all \(374\) subspaces of \(\mathbb F_2^5\) are allowed except those containing the all-one vector, which is the unique word heavier than four; the excluded subspaces are in bijection with the \(67\) subspaces of its four-dimensional quotient, leaving \(374-67=307\), as in the formula.

## Relationship to prior work

Horlemann and Ravi (arXiv:2610.31618v1, first submitted October 22, 2026) prove fixed-diameter polynomiality for linear anticodes, their general support decomposition, and asymptotic bounds. Their Proposition 4.3 involves **unevaluated** full-support coefficients \(a_q(s,d)\), and their Theorem 4.6 does not provide the exact binary diameter-four rank/support table. The support decomposition and linearity bounds are credited, not claimed new here. Their simplex construction also makes a seven-coordinate example natural; the exact exhaustiveness, rank refinement, and count \(30\) are the additional assertions.

Di Giusto, Gorla, and Ravagnani (arXiv:2512.17542v1, Theorem 2.20) classify optimal binary linear anticodes with dimension equal to maximum weight, including some four-dimensional boundary classes. Such a classification alone does not enumerate every lower-dimensional code of maximum weight at most four, and no all-dimension coefficient table was found in the inspected relevant text. Ravagnani (arXiv:1410.7207) provides earlier theory of optimal anticodes and generalized weights, not an identified covering all-rank enumeration. The prior exact diameter-three enumeration is a different parameter regime and does not imply these coefficients.

## Limitations

This is an exact theorem for **binary linear** anticodes with maximum Hamming distance at most four, not for nonlinear anticodes, larger diameters, or nonbinary fields. The finite coefficient table is computer-assisted, with exact standalone exhaustive procedures and a finite identity justifying completeness; no claim of a symbolic hand derivation of every coefficient is made. Novelty comparisons with accessible sources leave a residual possibility of a differently titled prior exact enumeration. Independent assessment has not been performed.

## References

1. A.-L. Horlemann and A. Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, arXiv:2610.31618v1 (October 22, 2026), especially Proposition 4.3, Theorem 4.6 and Remark 4.8. https://arxiv.org/html/2610.31618v1
2. A. Di Giusto, E. Gorla and A. Ravagnani, *A distance-free approach to generalized weights*, arXiv:2512.17542v1 (December 19, 2025), especially Theorem 2.20. https://arxiv.org/pdf/2512.17542
3. A. Ravagnani, *Generalized weights: an anticode approach*, Journal of Pure and Applied Algebra 220 (2016), 1946–1962, arXiv:1410.7207. https://arxiv.org/abs/1410.7207
