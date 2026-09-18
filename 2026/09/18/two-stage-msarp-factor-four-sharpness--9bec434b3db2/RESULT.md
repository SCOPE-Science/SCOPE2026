# The factor four is sharp for two-stage adaptive randomized pivoting

## Result

Consider the two-stage version of multi-stage adaptive randomized pivoting (MSARP) of Grigori and Xue, with one column selected at each stage. Let the exact rank-two right singular subspace be
\[
V=[a,b]\in\mathbb R^{3\times 2},\qquad [a,b,c]\in O(3),
\]
and assume every coordinate of \(c\) is nonzero. The first stage samples one index from the projection DPP with kernel \(aa^T\); the second stage samples one more index from the conditional projection DPP associated with \(VV^T\).

Define
\[
r_i:=\frac{a_i^2}{a_i^2+b_i^2}=\frac{a_i^2}{1-c_i^2}.
\]
If \(L\in\{1,2,3\}\) denotes the unique omitted column after the two selections, then
\[
\boxed{
\Pr(L=\ell)=c_\ell^2\sum_{i\ne \ell}r_i.
}
\]
Consequently, for the family
\[
A_{\eta}=\operatorname{diag}(2,1,\eta)[a,b,c]^T,
\qquad 0<\eta<1,
\]
whose optimal rank-two Frobenius error is \(\eta^2\), the expected squared error of the MSARP oblique interpolant is exactly
\[
\boxed{
\frac{\mathbb E\|A_\eta-A_\eta(:,U)V(U,:)^{-T}V^T\|_F^2}
{\|A_\eta-(A_\eta)_2\|_F^2}
=2\sum_{i=1}^3 r_i.
}
\]
Moreover,
\[
2\sum_i r_i\le 4,
\]
and the constant 4 is a supremum. Thus the factor \((1+1)(1+1)=4\) in Theorem 3.3 of Grigori--Xue is sharp already for two one-column stages and a \(3\times3\) matrix.

The same constant remains sharp for the actual column-subset approximation obtained by orthogonally projecting onto the selected columns. If
\[
\mathcal E_{\rm MS}(A_\eta)
:=\mathbb E\|A_\eta-A_\eta(:,U)A_\eta(:,U)^\dagger A_\eta\|_F^2,
\]
then
\[
\boxed{
\sup_{\eta,a,b,c}
\frac{\mathcal E_{\rm MS}(A_\eta)}{\|A_\eta-(A_\eta)_2\|_F^2}=4.
}
\]
In contrast, one-shot rank-two ARP on the same exact subspace has universal factor 3, and on the same sharpness family its orthogonal CSS error approaches factor 3. Hence there are matrices for which
\[
\frac{\mathcal E_{\rm MS}}{\mathcal E_{\rm one-shot}}
\longrightarrow \frac43.
\]
Thus the extra multiplicative penalty caused by preserving an earlier pivot is not merely an artifact of analyzing an oblique interpolant: it survives asymptotically for the optimal orthogonal projection onto the selected columns.

## Context

Grigori and Xue introduce conditional DPP augmentation and MSARP for incremental column subset selection. Their Theorem 3.3 gives, for two stages of sizes \(k\) and \(p\),
\[
\mathbb E\|A-A(:,U)V(U,:)^{-T}V^T\|_F^2
\le (1+k)(1+p)\|A-AVV^T\|_F^2.
\]
For unit-size stages this is a factor 4, while one-shot ARP with total target rank two has factor 3. The paper proves tightness of its conditional bound in Theorem 3.2 for a prescribed initial subset, but does not establish sharpness of the joint two-stage MSARP law. It also reports experiments in which MSARP and one-shot ARP have comparable orthogonal-projection error.

The result above resolves this worst-case distinction for the first nontrivial incremental case: the factor 4 cannot be uniformly replaced by a smaller constant, even if performance is evaluated using the best orthogonal projection onto the selected columns rather than the oblique surrogate appearing in Theorem 3.3.

## Proof

### 1. Exact omission law for two one-column stages

The first projection DPP has rank-one kernel \(aa^T\), so
\[
\Pr(S=\{i\})=a_i^2.
\]
For the second stage the full rank-two projection kernel is
\[
K=VV^T=aa^T+bb^T=I-cc^T.
\]
Conditioning on the inclusion of \(i\), the probability of selecting \(j\ne i\) is the diagonal of the rank-one Schur-complement kernel,
\[
\Pr(T=\{j\}\mid S=\{i\})
=K_{jj}-\frac{K_{ji}^2}{K_{ii}}
=\frac{\det K[\{i,j\},\{i,j\}]}{K_{ii}}.
\]
Let \(\ell\) be the remaining index. Since \(K=I-cc^T\),
\[
\det K[\{i,j\},\{i,j\}]
=1-c_i^2-c_j^2=c_\ell^2,
\qquad
K_{ii}=1-c_i^2.
\]
Therefore
\[
\Pr(S=i,T=j)
=a_i^2\frac{c_\ell^2}{1-c_i^2}
=r_i c_\ell^2.
\]
Summing over the two possible first-stage indices gives
\[
\Pr(L=\ell)=c_\ell^2\sum_{i\ne\ell}r_i.
\]
Normalization follows directly:
\[
\sum_\ell \Pr(L=\ell)
=\sum_i r_i(1-c_i^2)
=\sum_i a_i^2=1.
\]

### 2. Exact oblique error

Write
\[
A_\eta=
\begin{bmatrix}
2a^T\\
b^T\\
\eta c^T
\end{bmatrix}.
\]
For a final two-element set \(U\), the interpolant
\(A_\eta(:,U)V(U,:)^{-T}V^T\) reproduces the first two rows exactly because they lie in the row span of \(V^T\). If \(\ell\) is the omitted coordinate, the residual of the last row vanishes on \(U\) and differs from \(c^T\) by a vector in \(\operatorname{span}\{a,b\}\). Hence that residual is a multiple of \(e_\ell^T\). Its inner product with \(c\) equals 1, so the residual is exactly \(e_\ell^T/c_\ell\). Thus
\[
\|A_\eta-A_\eta(:,U)V(U,:)^{-T}V^T\|_F^2
=\frac{\eta^2}{c_\ell^2}.
\]
Because the optimal rank-two error is \(\eta^2\), averaging with the omission law yields
\[
\frac{\mathbb E\|A_\eta-A_\eta(:,U)V(U,:)^{-T}V^T\|_F^2}{\eta^2}
=\sum_\ell\sum_{i\ne\ell}r_i
=2\sum_i r_i.
\]

To bound this quantity, set
\[
s_i:=\frac{b_i^2}{a_i^2+b_i^2}=1-r_i.
\]
Since \(a_i^2+b_i^2=1-c_i^2\le1\),
\[
s_i\ge b_i^2.
\]
Therefore \(\sum_i s_i\ge\sum_i b_i^2=1\), so \(\sum_i r_i\le2\) and the factor is at most 4.

### 3. A family approaching four

For \(M>0\), define
\[
D_M=2M^2+1,\qquad E_M=M^2+1,
\]
\[
a_M=\frac{(1,M,M)^T}{\sqrt{D_M}},\qquad
b_M=\frac{(M,-1,0)^T}{\sqrt{E_M}},
\]
\[
c_M=\frac{(M,M^2,-(M^2+1))^T}{\sqrt{D_ME_M}}.
\]
These vectors form an orthonormal basis. Their three ratios are
\[
r_1=\frac{E_M}{E_M+M^2D_M},\qquad
r_2=\frac{M^2E_M}{M^2E_M+D_M},\qquad
r_3=1.
\]
Hence
\[
2(r_1+r_2+r_3)\longrightarrow4
\qquad(M\to\infty).
\]
This proves sharpness of the factor 4 for the original oblique MSARP bound.

### 4. Sharpness survives orthogonal CSS projection

Let \(G=A_\eta^TA_\eta\). If the final selected set contains all columns except \(\ell\), the squared residual of the optimal orthogonal projection is the scalar Schur complement
\[
E_\ell=\frac1{(G^{-1})_{\ell\ell}}.
\]
Since
\[
G^{-1}=\frac14 aa^T+bb^T+\eta^{-2}cc^T,
\]
we obtain
\[
\boxed{
\frac{E_\ell}{\eta^2}
=
\frac1{c_\ell^2+\eta^2b_\ell^2+(\eta^2/4)a_\ell^2}.
}
\]
Therefore
\[
R_{\rm MS}(\eta)
:=\frac{\mathcal E_{\rm MS}(A_\eta)}{\eta^2}
=
\sum_{\ell=1}^3
\frac{c_\ell^2\sum_{i\ne\ell}r_i}
{c_\ell^2+\eta^2b_\ell^2+(\eta^2/4)a_\ell^2}.
\]
For fixed \((a,b,c)\) with nonzero \(c_\ell\),
\[
R_{\rm MS}(\eta)\longrightarrow2\sum_i r_i
\qquad(\eta\downarrow0).
\]
The orthogonal CSS error is no larger than the corresponding oblique interpolation error, so Theorem 3.3 supplies the upper bound 4. The family in the previous section, followed by \(\eta\downarrow0\), attains this bound arbitrarily closely. Hence the sharp uniform constant for this two-stage orthogonal CSS problem is also 4.

For one-shot rank-two ARP, the projection-DPP law omits coordinate \(\ell\) with probability \(c_\ell^2\). Thus
\[
R_{\rm one}(\eta)
=
\sum_{\ell=1}^3
\frac{c_\ell^2}
{c_\ell^2+\eta^2b_\ell^2+(\eta^2/4)a_\ell^2}
\longrightarrow3.
\]
Combining the two limits gives the asymptotic \(4/3\) separation.

## Exact finite witness

A fully explicit orthogonal frame is obtained by normalizing
\[
a=(1,80,50)^T,\qquad
b=(80,-1,0)^T,\qquad
c=(50,4000,-6401)^T.
\]
The squared norms are
\[
\|a\|^2=8901,\qquad
\|b\|^2=6401,\qquad
\|c\|^2=56975301=8901\cdot6401,
\]
and all pairwise dot products vanish. For the normalized frame,
\[
2\sum_i r_i
=\frac{9337421015152404}{2334477669788101}
\approx3.999790246869209.
\]
Taking \(\eta=10^{-4}\) gives a full-rank matrix with distinct singular values \(2,1,10^{-4}\). Exact rational evaluation gives
\[
R_{\rm MS}\approx3.999334648800255,
\qquad
R_{\rm one}\approx2.999772172529846,
\]
so
\[
\frac{R_{\rm MS}}{R_{\rm one}}
\approx1.333212797099665.
\]
The accompanying verification script reproduces these values using exact rational arithmetic.

## Relation to prior work

Cortinovis and Kressner introduced adaptive randomized pivoting and proved the one-shot \((k+1)\) expected Frobenius guarantee. Epperly identified ARP with projection-DPP/volume sampling and emphasized that the one-shot factor \(k+1\) matches the classical worst-case existence barrier for interpolative column/row selection.

Grigori and Xue introduced conditional DPP augmentation and MSARP. Their Theorem 3.2 proves that the one-step conditional estimate of Theorem 3.1 is tight for a prescribed initial subset. The result here is different: the initial pivot is itself random under the first ARP stage, and the complete joint two-stage law is analyzed. The construction shows that averaging over the first stage does not remove the product-factor loss. It further shows that replacing the analyzed oblique interpolant by the best orthogonal projection onto the selected columns does not restore the one-shot constant.

To the best of our knowledge, the sharp factor-four statement for two-stage MSARP, its exact three-coordinate omission law, and the asymptotic \(4/3\) separation from one-shot ARP have not previously been stated.

## Limitations

The sharpness sequence becomes increasingly ill-conditioned: the normalized benchmark is the rank-two tail energy \(\eta^2\), and approaching factor 4 uses \(\eta\to0\) after choosing a highly unbalanced singular-vector frame. Thus the result is a uniform worst-case obstruction and does not imply that MSARP is typically worse than one-shot ARP on well-conditioned data.

The analysis is restricted to two stages of sizes \(1+1\). It does not prove that the full product factor \(\prod_i(1+k_i)\), or the \(2^t\) factor for more than two unit-size stages, is sharp. It also does not contradict the empirical observation that MSARP and one-shot ARP can behave similarly on the tested data sets.

The construction assumes exact dominant right singular vectors and exact arithmetic, matching the clean theoretical setting of the cited MSARP bound. It does not address approximate subspace construction, finite precision, Nyström-specific structure, or fixed-precision stopping.

## Reproducibility

`artifacts/verify_msarp_sharpness.py` uses only Python's standard-library `fractions.Fraction`. It checks the exact orthogonal witness, the two-stage omission probabilities, the exact oblique factor, and the finite full-rank orthogonal-CSS comparison. `artifacts/verified_output.txt` records its output.

## References

1. L. Grigori and Z. Xue, *Incremental Column Subset Selection via Conditional Determinantal Point Processes*, arXiv:2609.20556v1, 2026. https://arxiv.org/abs/2609.20556v1
2. A. Cortinovis and D. Kressner, *Adaptive randomized pivoting for column subset selection, DEIM, and low-rank approximation*, arXiv:2412.13992; SIAM Journal on Matrix Analysis and Applications, 2026. https://arxiv.org/abs/2412.13992
3. E. N. Epperly, *Adaptive randomized pivoting and volume sampling*, arXiv:2510.02513, 2025--2026. https://arxiv.org/abs/2510.02513
4. A. Deshpande and L. Rademacher, *Efficient Volume Sampling for Row/Column Subset Selection*, FOCS 2010. https://doi.org/10.1109/FOCS.2010.38
5. A. Belhadji, R. Bardenet, and P. Chainais, *A Determinantal Point Process for Column Subset Selection*, JMLR 21 (2020), 1--62. https://jmlr.org/papers/v21/19-080.html
