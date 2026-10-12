# Flag-sensitive rank-one twisted Cholesky zero fibers
## Finding
Let \(q\) be an odd prime power, let \(\chi\) be the quadratic character of \(\mathbf F_q\), and let
\[
G=\operatorname{diag}(g_1,\ldots,g_n),\qquad g_i\in\mathbf F_q^\times.
\]
Write \(T_n(\mathbf F_q)\) for the upper triangular matrices and define
\[
N_1(G)=\#\{U\in T_n(\mathbf F_q):\operatorname{rank}U=1,\ U^{\mathsf T}GU=0\}.
\]
Then
\[
N_1(G)=nq^{n-1}-\frac{q^n-1}{q-1}+(q-1)\sum_{m=1}^{\lfloor n/2\rfloor}
\chi\!\left((-1)^m\prod_{i=1}^{2m}g_i\right)q^{n-m-1}.
\]
Therefore the first nonzero-rank stratum of the twisted zero fiber depends on the quadratic discriminants of the even-dimensional prefix restrictions of \(G\), rather than on the global Witt type alone.

A smallest explicit flag-sensitivity witness occurs over \(\mathbf F_3\):
\[
G_1=\operatorname{diag}(1,1,1,2),\qquad
G_2=\operatorname{diag}(1,2,1,1).
\]
The two forms are permutation-congruent, hence globally isometric and of the same Witt type, but
\[
N_1(G_1)=44,\qquad N_1(G_2)=80.
\]
Thus any rank recurrence for twisted triangular zero fibers that is meant to respect the fixed upper-triangular flag needs flag-relative data; global Witt type by itself cannot determine even the rank-one count.

## Assumptions and scope
The field has odd order. The displayed closed formula is proved for nondegenerate diagonal forms relative to the standard coordinate flag. The obstruction to global-Witt-type classification is already decisive in that class because the two exhibited diagonal Gram matrices are globally isometric.

No claim is made here for higher-rank strata, for arbitrary non-diagonal Gram matrices, or for characteristic two.

## Proof
Every rank-one matrix can be written as \(U=xy^{\mathsf T}\) with nonzero \(x,y\in\mathbf F_q^n\), and each rank-one matrix has exactly \(q-1\) such factorizations, obtained by \(x\mapsto\lambda x\), \(y\mapsto\lambda^{-1}y\).

Put \(k=\max\operatorname{supp}(x)\) and \(\ell=\min\operatorname{supp}(y)\). Then \(xy^{\mathsf T}\) is upper triangular if and only if \(k\le\ell\). Also
\[
U^{\mathsf T}GU=(x^{\mathsf T}Gx)yy^{\mathsf T},
\]
so, because \(y\ne0\), the twisted zero condition is equivalent to \(x^{\mathsf T}Gx=0\).

For \(0\le k\le n\), let \(Z_k\) be the number of zeros in \(\mathbf F_q^k\) of the nondegenerate prefix quadratic form
\[
Q_k(z)=\sum_{i=1}^k g_i z_i^2,
\]
with \(Z_0=1\). The number of isotropic \(x\) with \(\max\operatorname{supp}(x)=k\) is \(Z_k-Z_{k-1}\). For a fixed \(\ell\), the number of nonzero \(y\) with \(\min\operatorname{supp}(y)=\ell\) is \((q-1)q^{n-\ell}\). Summing over \(\ell\ge k\) and dividing by the \(q-1\) scalar factorizations gives
\[
N_1(G)=\sum_{k=1}^n (Z_k-Z_{k-1})\frac{q^{n-k+1}-1}{q-1}.
\]
Summation by parts yields
\[
N_1(G)=Z_n-\frac{q^n-1}{q-1}+\sum_{k=1}^{n-1}q^{n-k}Z_k.
\]
For odd \(q\), the standard zero count for a nondegenerate quadratic form gives
\[
Z_k=
\begin{cases}
q^{k-1},&k\text{ odd},\\
q^{k-1}+(q-1)\chi\!\left((-1)^{k/2}\prod_{i=1}^k g_i\right)q^{(k-2)/2},&k\text{ even}.
\end{cases}
\]
Substitution produces the stated closed formula.

For the explicit \(\mathbf F_3\) pair, the common baseline is
\[
4\cdot3^3-\frac{3^4-1}{3-1}=68.
\]
For \(G_1\), the two even-prefix characters are both \(-1\), so the correction is \(2(-3^2-3)=-24\), giving \(44\). For \(G_2\), they are \(+1\) and \(-1\), so the correction is \(2(3^2-3)=12\), giving \(80\).

## Verification
The accompanying `verify.py` exhaustively enumerates all upper triangular matrices for the two \(4\times4\) examples over \(\mathbf F_3\), checks rank and the equation \(U^{\mathsf T}GU=0\), and recovers \(44\) and \(80\). It also checks the formula against direct enumeration in several smaller standard-form cases. The verifier ends with `VERIFY_OK`.

The exhaustive checks are finite corroboration only. The all-
\(n\), all-odd-prime-power statement is proved by the factorization-and-quadratic-zero-count argument above.

## Relationship to prior work
Wu and Zhou determine the rank distribution of the untwisted zero fiber \(U^{\mathsf T}U=0\) over every finite field and explicitly leave the twisted problem \(U^{\mathsf T}GU=0\) for a nondegenerate symmetric form \(G\) as an open direction, asking how the recurrence depends on Witt type. Their Lemma 6.5 records the standard finite-field zero count for nondegenerate quadratic forms, which is used above.

The present rank-one formula is not a specialization of their untwisted recurrence unless the twist can be removed by a flag-preserving square-root change of coordinates. The \(\mathbf F_3\) pair shows a stronger obstruction: two globally isometric forms can have different twisted triangular rank-one counts solely because their coefficients occur in a different order along the fixed flag.

## Limitations
Only the rank-one stratum is classified. Higher ranks involve interactions among totally isotropic subspaces and the fixed flag, and the displayed prefix-character formula does not by itself provide a full recurrence. For a general non-diagonal \(G\), leading principal restrictions can be degenerate even when \(G\) is nondegenerate, so additional invariants may be necessary.

A residual literature risk remains because classical work on isotropic flags may encode an equivalent rank-one count under different terminology; targeted searches did not locate such a formula for this twisted upper-triangular fiber.

## References
1. H. Wu and K. Zhou, *Singular Cholesky Fibers over Finite Fields*, arXiv:2609.00533v1, 2026. In particular Lemma 6.5 and Conclusion, item (v). https://arxiv.org/abs/2609.00533
2. R. Lidl and H. Niederreiter, *Finite Fields*, 2nd ed., Cambridge University Press, 1997. The quadratic zero-count result used by Wu and Zhou is cited there as Theorems 6.26 and 6.27.
3. J. MacWilliams, *Orthogonal matrices over finite fields*, American Mathematical Monthly 76 (1969), 152–164. https://doi.org/10.1080/00029890.1969.12000160
