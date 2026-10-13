# Exact group-invertible rank enumerator in \(T_n(\mathbb F_q)\)

## Finding

For every prime power \(q\), every \(n\ge 1\), and every \(0\le r\le n\), the number of group-invertible matrices of rank \(r\) in the upper-triangular algebra \(T_n(\mathbb F_q)\) is
\[
G_{n,r}(q)=\binom nr (q-1)^r q^{\binom n2-\binom{n-r}2}.
\]
More finely, fix the complete diagonal of an upper-triangular matrix, with exactly \(k\) prescribed zero diagonal positions and prescribed nonzero values at the other \(n-k\) positions. Exactly
\[
q^{\binom n2-\binom k2}
\]
strictly-upper-triangular fillings make the matrix group invertible, independently of the locations of the \(k\) zeros. Consequently
\[
\#\{A\in T_n(\mathbb F_q):A^\#\text{ exists}\}
=\sum_{r=0}^n\binom nr(q-1)^r q^{\binom n2-\binom{n-r}2}.
\]
Here group invertibility is equivalent over a field to \(\operatorname{rank}(A^2)=\operatorname{rank}(A)\); for upper-triangular \(A\), it is also equivalent to \(\operatorname{rank}(A)\) being exactly the number of nonzero diagonal entries.

The fixed-diagonal statement is the structural core: the number of admissible completions depends only on how many diagonal entries are zero, not on where those zeros occur or on the chosen nonzero diagonal values.

## Assumptions and scope

Let \(q\) be a prime power and let \(T_n(\mathbb F_q)\) denote the algebra of upper-triangular \(n	imes n\) matrices. A matrix \(A\) is group invertible if there is a unique matrix \(A^\#\) satisfying
\[
AA^\#A=A,\qquad A^\#AA^\#=A^\#,\qquad AA^\#=A^\#A.
\]
Over a field, the group inverse exists exactly when \(\operatorname{rank}(A^2)=\operatorname{rank}(A)\). If \(A\) is upper triangular and has exactly \(k\) zero diagonal entries, then zero has algebraic multiplicity \(k\) in the characteristic polynomial. Group invertibility is therefore equivalent to zero being semisimple, hence to \(\dim\ker A=k\), or equivalently
\[
\operatorname{rank}A=n-k.
\]
Thus the problem is to count upper-triangular fillings that attain the minimum rank forced by the nonzero diagonal entries.

The zero matrix is included: it is group invertible with group inverse zero and contributes the \(r=0\) term.

## Proof

Fix a diagonal pattern with exactly \(k\) zeros and fix every nonzero diagonal value. Let \(f(n,k)\) be the number of choices of entries strictly above the diagonal for which the resulting matrix has rank exactly \(n-k\). We prove
\[
f(n,k)=q^{\binom n2-\binom k2}.
\]
The expression is independent of the locations of the zeros; this follows from a recursion on the final diagonal entry.

Write
\[
A=\begin{pmatrix}B&v\0&a\end{pmatrix},
\]
where \(B\in T_{n-1}(\mathbb F_q)\), \(v\in\mathbb F_q^{n-1}\), and \(a\) is the last prescribed diagonal entry.

If \(a
e0\), elementary row operations using the last row clear \(v\), so
\[
\operatorname{rank}A=\operatorname{rank}B+1.
\]
All \(q^{n-1}\) vectors \(v\) are allowed, and the first \(n-1\) diagonal positions still contain \(k\) zeros. Hence
\[
f(n,k)=q^{n-1}f(n-1,k).
\]
Using the induction hypothesis gives
\[
q^{n-1}q^{\binom{n-1}2-\binom k2}=q^{\binom n2-\binom k2}.
\]

If \(a=0\), the first \(n-1\) diagonal positions contain \(k-1\) zeros. Their minimum possible rank is \(n-k\). The full block matrix has this same rank exactly when \(B\) has rank \(n-k\) and the added column \(v\) belongs to \(\operatorname{im}B\). For each admissible \(B\), its image has dimension \(n-k\), so there are exactly \(q^{n-k}\) choices for \(v\). Therefore
\[
f(n,k)=q^{n-k}f(n-1,k-1)
=q^{n-k}q^{\binom{n-1}2-\binom{k-1}2}
=q^{\binom n2-\binom k2}.
\]
The initial case \(f(0,0)=1\) completes the induction.

Now set \(r=n-k\). There are \(\binom nr\) ways to choose the nonzero diagonal positions and \((q-1)^r\) ways to choose their nonzero values. Multiplication by the fixed-diagonal count gives
\[
G_{n,r}(q)=\binom nr(q-1)^r q^{\binom n2-\binom{n-r}2}.
\]
Summing over \(r\) yields the total count.

## Verification

The standalone `verify.py` independently enumerates every upper-triangular matrix and tests the criterion \(\operatorname{rank}(A^2)=\operatorname{rank}(A)\). It verifies the complete rank distribution for \(q=2\) through \(n=5\), for \(q=3\) through \(n=4\), for \(q=5\) through \(n=3\), and for the non-prime field \(\mathbb F_4\) through \(n=3\). It also verifies both induction recurrences algebraically for several field orders and dimensions.

The finite enumeration is a consistency check only. The theorem for all prime powers and all dimensions follows from the rank characterization and the two exact recurrences above.

## Relationship to prior work

Mary studies group inverses in semigroups and rings and records that for a Dedekind-finite coefficient ring, the group inverse of an upper-triangular matrix, when it exists in the full matrix ring, is again upper triangular. Finite fields are Dedekind-finite, so group invertibility here is intrinsic to the triangular algebra as well as to the ambient matrix algebra. That paper concerns reverse-order laws and structural conditions, not finite-field enumeration.

Hartwig and Shoaf give necessary and sufficient conditions for group and Drazin inverses of bidiagonal and triangular Toeplitz matrices over arbitrary rings. Their preliminary lemma also relates existence of a group inverse to equivalence of a matrix with its square, and they explicitly note the field case. Their triangular Toeplitz family is a special structured subfamily and does not imply the rank-stratified count for all of \(T_n(\mathbb F_q)\).

Meyer and Rose treat indices and Drazin inverses of block triangular matrices and give an explicit block formula. This is broader structural machinery but does not enumerate finite-field triangular matrices by group-invertibility rank. Standard similarity-class enumerations of all matrices likewise do not directly dominate the present result, because belonging to \(T_n(\mathbb F_q)\) is not invariant under arbitrary conjugacy.

## Limitations

The count concerns the ordinary group inverse, equivalently Drazin index at most one in the matrix setting. It does not enumerate higher Drazin indices, prescribe the group inverse itself, or refine by Jordan form away from the zero primary component. The proof uses only finite-field linear algebra and therefore does not claim the same numerical formula over general finite rings.

A residual literature risk remains that an older semigroup-enumeration source may count the same elements under terminology such as “group elements,” “completely regular elements,” or “index-one elements.” Targeted searches under these aliases, together with direct inspection of the most relevant triangular generalized-inverse sources, did not locate a covering formula.

## References

1. X. Mary, “Reverse Order Law for the Group Inverse in Semigroups and Rings,” *Communications in Algebra* 43 (2015), 2492–2508. DOI: 10.1080/00927872.2014.900562. Published online 2015-04-17.
2. R. E. Hartwig and J. Shoaf, “Group inverses and Drazin inverses of bidiagonal and triangular Toeplitz matrices,” *Journal of the Australian Mathematical Society* 24 (1977), 10–34. DOI: 10.1017/S1446788700020036.
3. C. D. Meyer Jr. and N. J. Rose, “The Index and the Drazin Inverse of Block Triangular Matrices,” *SIAM Journal on Applied Mathematics* 33 (1977), 1–7. DOI: 10.1137/0133001.
