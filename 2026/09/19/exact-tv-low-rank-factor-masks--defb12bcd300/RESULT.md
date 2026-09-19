# Exact total-variation leakage of uniform low-rank factor masks

## Statement

Let \(q\) be a prime power and define
\[
p_{a,b}(q):=\prod_{j=0}^{a-1}(1-q^{j-b}).
\]
Thus \(p_{a,b}(q)\) is the probability that a uniformly random \(a\times b\) matrix over \(\mathbb F_q\), with \(a\le b\), has full row rank.

Let \(1\le k\le r<n\), let
\[
U\sim\mathrm{Unif}(\mathbb F_q^{k\times r}),\qquad
V\sim\mathrm{Unif}(\mathbb F_q^{r\times n})
\]
be independent, and put \(M=UV\). If \(Z\) is uniform on \(\mathbb F_q^{k\times n}\), then
\[
\boxed{
 d_{\mathrm{TV}}(M,Z)
 =p_{k,n}(q)\bigl(1-p_{k,r}(q)\bigr).
}
\]

More precisely, the point probability \(\Pr[M=A]\) depends only on \(d=\operatorname{rank}(A)\), is strictly decreasing as \(d\) increases, is strictly larger than \(q^{-kn}\) for every \(d<k\), and equals
\[
p_{k,r}(q)q^{-kn}<q^{-kn}
\]
for \(d=k\). Hence the full-row-rank matrices are exactly the deficit set against the uniform law, and the displayed total-variation formula is exact.

## Exact rank-likelihood formula

For a fixed \(A\in\mathbb F_q^{k\times n}\) of rank \(d\), let \({a\brack b}_q\) denote the Gaussian binomial coefficient. Then
\[
\Pr[UV=A]
=
q^{-kr}\sum_{s=d}^{k}
{k-d\brack s-d}_q
\left(\prod_{j=0}^{s-1}(q^r-q^j)\right)
q^{-sn}.
\tag{1}
\]
Indeed, condition on \(s=\operatorname{rank}(U)\). Its image is a uniformly random \(s\)-subspace of \(\mathbb F_q^k\). It contains the column space of \(A\) with probability
\[
\frac{{k-d\brack s-d}_q}{{k\brack s}_q},
\]
and, once this containment holds, each of the \(n\) equations \(Uv=A_{:,j}\) has exactly \(q^{r-s}\) solutions. Combining this with the standard count
\[
\#\{U:\operatorname{rank}(U)=s\}
={k\brack s}_q\prod_{j=0}^{s-1}(q^r-q^j)
\]
gives (1).

For fixed \(s\ge d+1\),
\[
{k-d\brack s-d}_q\ge {k-d-1\brack s-d-1}_q,
\]
with strict inequality when \(s<k\); moreover, the rank-\(d\) expression has the additional positive \(s=d\) summand. Thus the point mass in (1) strictly decreases with \(d\).

For a full-row-rank target \(A\), \(U\) must have rank \(k\). Conditional on that event, the linear map \(V\mapsto UV\) is surjective onto \(\mathbb F_q^{k\times n}\), so
\[
\Pr[UV=A]=p_{k,r}(q)q^{-kn}.
\tag{2}
\]

For any rank-deficient target, it is enough to retain only the contribution from \(\operatorname{rank}(U)=k-1\). The probability that a uniformly random \((k-1)\)-dimensional image contains a fixed rank-\(d\) column space is at least \({k\brack k-1}_q^{-1}\). Hence
\[
\Pr[UV=A]
\ge
\frac{\Pr[\operatorname{rank}(U)=k-1]}{{k\brack k-1}_q}
q^{-(k-1)n}.
\]
Relative to \(q^{-kn}\), the right side has ratio
\[
q^{n-r}p_{k-1,r}(q).
\]
Because \(n\ge r+1\) and
\[
p_{k-1,r}(q)
\ge 1-\sum_{j=0}^{k-2}q^{j-r}
>1-\frac{1}{q(q-1)},
\]
this ratio is strictly larger than \(1\). Thus every deficient-rank point is overweighted relative to uniform.

There are \(q^{kn}p_{k,n}(q)\) full-row-rank \(k\times n\) matrices. Summing their pointwise deficit from (2) gives exactly
\[
p_{k,n}(q)(1-p_{k,r}(q)),
\]
which proves the total-variation identity.

## Consequence for low-rank masking

Consider the Low-Rank Factors mask from Cohen--D'Oliveira--Sprintson: for uniform \(A\in\mathbb F_q^{n\times n}\), independently sample
\[
R=UV,
\qquad U\in\mathbb F_q^{n\times r},\quad V\in\mathbb F_q^{r\times n},
\]
with all factor entries uniform and independent, and upload \(X=A+R\). For a row set \(T\subseteq[n]\) of size \(k\le r\), their proof observes that
\[
d_{\mathrm{TV}}(P_{A_T,X},P_{A_T}P_X)
=d_{\mathrm{TV}}(R_T,\mathrm{Unif}(\mathbb F_q^{k\times n})).
\]
Since \(R_T=U_TV\) with \(U_T\) uniform in \(\mathbb F_q^{k\times r}\), the exact leakage is therefore
\[
\boxed{
 d_{\mathrm{TV}}(P_{A_T,X},P_{A_T}P_X)
 =p_{k,n}(q)(1-p_{k,r}(q)).
}
\tag{3}
\]
The same identity holds for any \(k\) columns by transposition.

The motivating paper proves the upper bound
\[
d_{\mathrm{TV}}\le 1-p_{k,r}(q)\le \frac{q^{k-r}}{q-1}.
\]
Equation (3) shows that the first bound loses exactly the factor \(p_{k,n}(q)\), and that the second is order-tight uniformly in the allowed dimensions for fixed \(q\).

## Sharp rank-surplus threshold

For fixed \(q\), set
\[
c_q^{(2)}:=\prod_{\ell=2}^{\infty}(1-q^{-\ell})>0.
\]
Since \(n>r\ge k\),
\[
p_{k,n}(q)\ge c_q^{(2)}.
\]
Also
\[
q^{k-1-r}
\le 1-p_{k,r}(q)
<\frac{q^{k-r}}{q-1}.
\]
Consequently
\[
\boxed{
 c_q^{(2)}q^{k-1-r}
 \le
 d_{\mathrm{TV}}(P_{A_T,X},P_{A_T}P_X)
 <
 \frac{q^{k-r}}{q-1}.
}
\tag{4}
\]
Thus, for fixed field size, Low-Rank Factors protect \(k\) rows with vanishing total-variation leakage if and only if the rank surplus \(r-k\to\infty\). A bounded surplus cannot give asymptotically vanishing leakage.

For example, when \(q=2\), \(k=r\to\infty\), and \(n-r\to\infty\), (3) tends to
\[
1-\prod_{\ell=1}^{\infty}(1-2^{-\ell})
=0.7112119049\ldots.
\]
So increasing the mask rank together with the number of protected rows does not by itself produce asymptotic individual security; an increasing surplus of mask rank over protected-row count is necessary.

## Context and significance

Cohen, D'Oliveira and Sprintson prove approximate row/column individual security for Low-Rank Factors and obtain the bound \(q^{k-r}/(q-1)\). Their proof already isolates the full-row-rank event of \(U_T\), but only uses it to construct a coupling upper bound. The rank-likelihood calculation above determines the sign of every pointwise deviation from uniform, turning that coupling bound into an exact distance and a matching converse. It therefore identifies the precise security threshold in the parameter \(r-k\).

The underlying rank counts and Gaussian-binomial identities are standard finite-field linear algebra; no novelty is claimed for those ingredients in isolation. The contribution is the exact product-law total-variation identity in this masking regime and its individual-security consequences.

## Limitations

The result concerns independent uniformly sampled factors and uniform inputs, exactly as in the Low-Rank Factors part of the motivating individual-security theorem. It does not give an exact total-variation law for uniform rank-ball masks, arbitrary nonuniform factor distributions, or nonuniform/correlated inputs. Total variation is only one leakage criterion; the exact maximal-correlation result of the motivating paper is a different statement. The formula also assumes \(k\le r<n\); other rectangular regimes have different support geometry.

## Verification

`artifacts/verify_exact_tv.py` exhaustively enumerates several small prime-field instances, forms every factor product, and checks the exact total-variation identity, the full-rank point-mass ratio, and the fact that every deficient-rank point is at least as likely as under the uniform law. `artifacts/verification.txt` records the executed output. The general result is proved analytically above and does not depend on the finite checks.

## References

1. A. Cohen, R. G. L. D'Oliveira, A. Sprintson, *Low-Rank Masking for Single-Server Matrix Multiplication*, arXiv:2609.18876 (2026). https://arxiv.org/abs/2609.18876
2. S. Yang, T. Honold, *Good Random Matrices over Finite Fields*, Advances in Mathematics of Communications 6(2):203--227 (2012), arXiv:1008.3408. https://arxiv.org/abs/1008.3408
