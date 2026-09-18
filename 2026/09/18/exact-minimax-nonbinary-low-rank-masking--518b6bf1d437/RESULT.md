# Exact minimax maximal correlation for low-rank matrix masking

## Result

Let \(\mathcal M_{d,e}=\mathbb F_q^{d\times e}\), with \(2\le d\le e\), and let \(A\) be uniform on \(\mathcal M_{d,e}\). Fix \(1\le r<d\), and define
\[
\Lambda_{d,e,r}(q)
=\frac{q^{d+e-r}-q^d-q^e+1}{(q^d-1)(q^e-1)}.
\]
Consider observations
\[
X=L(A+K)R,
\]
where \((L,R,K)\) is independent of \(A\), \(L\in\mathrm{GL}_d(q)\), \(R\in\mathrm{GL}_e(q)\), and \(\operatorname{rank}K\le r\) almost surely.

**Theorem.** If either \(q\ge3\), or \(q=2\) and \(d<e\), then
\[
\inf \rho_{\mathrm m}(A;X)=\Lambda_{d,e,r}(q),
\]
where the infimum ranges over all distributions of \((L,R,K)\) satisfying the conditions above. The infimum is attained with \(L=I_d\), \(R=I_e\), and \(K\) uniform over the matrices of rank exactly \(r\).

In particular, for every nonbinary finite field, every \(n\ge2\), and every \(1\le r<n\), uniform exact-rank masking is exactly minimax for a uniform \(n\times n\) input:
\[
\boxed{
\inf \rho_{\mathrm m}(A;L(A+K)R)
=\frac{q^{2n-r}-2q^n+1}{(q^n-1)^2}
}.
\]
This remains true when secret invertible left and right transformations are allowed.

For the single-server matrix-multiplication setting of Cohen--D'Oliveira--Sprintson, taking two independent exact-rank masks gives the same maximal correlation against the complete view \((X,Y,XY)\) as against one upload, so the same exact optimum applies to independent uniform square inputs.

## Proof

### 1. A universal lower bound, including secret invertible transformations

For a matrix \(M\in\mathcal M_{d,e}\), write
\[
g(M)=|\ker M|=q^{e-\operatorname{rank}M}.
\]
Since left and right multiplication by invertible matrices preserves rank,
\[
g(X)=g(A+K)
\]
pointwise, regardless of the distribution of \(L,R\).

Regard a matrix \(A\) as a uniformly random linear map \(\mathbb F_q^e\to\mathbb F_q^d\). Direct counting gives
\[
\mathbb E g(A)=1+\frac{q^e-1}{q^d}
\]
and
\[
\operatorname{Var}(g(A))
=\frac{(q^d-1)(q^e-1)(q-1)}{q^{2d}}.
\]
For fixed \(K\) of rank \(t\), expand
\[
\mathbb E[g(A)g(A+K)]
=\sum_{v,w\in\mathbb F_q^e}
\Pr(Av=0,\ Aw=-Kw).
\]
If \(v,w\) are linearly independent, the probability is \(q^{-2d}\). If \(v,w\ne0\) are dependent, writing \(w=cv\), the two equations are consistent exactly when \(v\in\ker K\), and then the probability is \(q^{-d}\). Separating these cases yields
\[
\operatorname{Cov}(g(A),g(A+K))
=\frac{q-1}{q^{2d}}
\left(q^{d+e-t}-q^d-q^e+1\right).
\]
Averaging over random \(K\) therefore gives
\[
\operatorname{Corr}(g(A),g(X))
=
\frac{q^d\,\mathbb E[q^{e-\operatorname{rank}K}]-q^d-q^e+1}
{(q^d-1)(q^e-1)}.
\]
Because \(\operatorname{rank}K\le r\),
\[
\mathbb E[q^{e-\operatorname{rank}K}]\ge q^{e-r},
\]
and hence
\[
\rho_{\mathrm m}(A;X)
\ge \operatorname{Corr}(g(A),g(X))
\ge \Lambda_{d,e,r}(q).
\]
The numerator is positive for \(r<d\le e\), so no absolute-value issue arises.

This argument is a rectangular extension of the kernel-count converse used for square matrices by Cohen--D'Oliveira--Sprintson. It also shows that the first, exact lower-bound expression continues to hold at \(r=n-1\) in the square case; the restriction \(r\le n-2\) in their stated theorem is needed for their subsequent simplification to \(q^{-r}/2\), not for the kernel-count inequality itself.

### 2. Exact-rank masking attains the lower bound

Now let \(K\) be uniform over the rank-\(r\) matrices. On the additive group \(\mathcal M_{d,e}\), fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\) and write
\[
\chi_H(M)=\psi\!\left(\sum_{i,j}H_{ij}M_{ij}\right).
\]
For uniform \(A\), the conditional-expectation operator of the additive channel \(A\mapsto A+K\) is diagonal in these characters, so
\[
\rho_{\mathrm m}(A;A+K)
=\max_{H\ne0}|\mathbb E\chi_H(K)|.
\]
This is the same Fourier diagonalization used in the square case by Cohen--D'Oliveira--Sprintson.

The rank-\(r\) matrices are the distance-\(r\) relation of the bilinear-forms association scheme \(H_q(d,e)\). Consequently, if \(s=\operatorname{rank}H\), then
\[
\sum_{\operatorname{rank}K=r}\chi_H(K)=B_r(s),
\]
where \(B_r(s)\) is the bilinear-forms eigenvalue and \(B_r(0)=C_{d,e}(r)\) is the number of rank-\(r\) matrices. Thus
\[
|\mathbb E\chi_H(K)|=\frac{|B_r(s)|}{C_{d,e}(r)}.
\]
Cioabă--Gupta, Theorem 4.3, proves for \(q\ge3\) that
\[
|B_r(0)|>|B_r(1)|>|\cdots|>|B_r(d)|.
\]
Their Theorem 4.6 proves the same strict magnitude monotonicity for \(q=2\) when \(e\ge d+1\). Hence, in exactly the parameter range of the theorem, the largest nonconstant Fourier coefficient has rank \(s=1\).

It remains to evaluate that coefficient. For rank-one \(H=uv^T\) with \(u\ne0\), \(v\ne0\),
\[
\chi_H(K)=\psi(u^T Kv).
\]
For a uniform rank-\(r\) matrix \(K\), its kernel is a uniform \((e-r)\)-subspace, so
\[
p_0:=\Pr(Kv=0)=\frac{q^{e-r}-1}{q^e-1}.
\]
Conditional on \(Kv\ne0\), left-invariance makes \(Kv\) uniform on \(\mathbb F_q^d\setminus\{0\}\). Therefore
\[
\mathbb E\chi_H(K)
=p_0-\frac{1-p_0}{q^d-1}
=\frac{q^{d+e-r}-q^d-q^e+1}{(q^d-1)(q^e-1)}
=\Lambda_{d,e,r}(q).
\]
Combining this equality with the universal lower bound proves the theorem.

## Consequences for the square masking problem

Cohen--D'Oliveira--Sprintson prove for square matrices that their Low-Rank Factors method has maximal correlation exactly \(q^{-r}\), while Low-Rank Ball has maximal correlation at most \(q^{-r}\), and they prove the converse
\[
\rho_{\mathrm m}\ge
\frac{q^{2n-r}-2q^n+1}{(q^n-1)^2}
\]
for \(r\le n-2\), concluding that their two methods are within a factor of two of optimum. The exact-rank shell above attains that lower bound for every \(q\ge3\) and every \(r<n\), so the nonbinary factor-two gap closes exactly.

The improvement is strict at every finite parameter:
\[
\Lambda_{n,n,r}(q)<q^{-r}.
\]
It is also strictly better than uniform rank-ball masking. The rank ball is a positive mixture of exact-rank shells \(t=0,\ldots,r\), and its rank-one Fourier coefficient is the corresponding weighted average of \(\Lambda_{n,n,t}(q)\). Since \(\Lambda_{n,n,t}(q)\) is strictly decreasing in \(t\), this average is strictly larger than \(\Lambda_{n,n,r}(q)\).

Exact-rank masks can be sampled with the same standard factorization machinery used in the cited masking paper: multiply independent uniformly sampled full-rank \(d\times r\) and \(r\times e\) factors. Every rank-\(r\) matrix has the same number of such factorizations. The cited rejection-sampling method costs \(O((d+e)r^2)\) expected field operations offline; the matrix-multiplication encoding/decoding cost remains in the same \(O(n^2r)\) regime in the square protocol.

## Binary-square exception

The proof deliberately does not claim the binary square case \(q=2,d=e\). The spectral exception is real: Brouwer--Cioabă--Ihringer--McGinnis, Lemma 7.4, shows that for \(r=d-1\),
\[
\frac{|B_r(2)|}{|B_r(1)|}
=\frac{2^{d-1}+1}{2^{d-1}-1}>1.
\]
Thus uniform exact-rank masking does not attain the rank-one lower bound in that boundary case, and the shell argument cannot establish minimaxity there. The present result does not determine the exact binary-square optimum.

## Reproducibility

`artifacts/verify_bilinear_spectrum.py` evaluates the exact integer bilinear-forms eigenvalue formula, the rank counts, and \(\Lambda_{d,e,r}(q)\). It checks 532 eligible tuples over \(q\in\{3,4,5,7\}\) and binary nonsquare rectangles, verifies rank-one spectral dominance and the strict improvement over \(q^{-r}\), and separately reproduces a binary-square spectral exception. `artifacts/verification.txt` is the corresponding output.

The computation is a finite consistency check; the theorem is proved analytically above.

## Literature context and originality boundary

The motivating preprint by Cohen, D'Oliveira and Sprintson (arXiv:2609.18876v1, 16 September 2026) formulates the rank-constrained maximal-correlation problem, proves the exact lower-bound expression used above for square matrices with \(r\le n-2\), and gives the \(q^{-r}\) achievability bound for rank-ball and factor masks. It does not state the exact-rank-shell minimax theorem.

The spectral input is classical association-scheme information rather than a new eigenvalue theorem. Brouwer, Cioabă, Ihringer and McGinnis describe the bilinear-forms scheme and its eigenvalues, and Cioabă--Gupta prove the strict magnitude ordering needed here. The new contribution claimed here is the connection of that spectrum to rank-constrained masking, the exact shell achievability/minimax statement, and the rectangular kernel-count extension.

Exact and synonymous searches for exact-rank masks, rank shells, maximal correlation, bilinear-forms spectra, and the motivating arXiv identifier did not locate an earlier statement of this minimax result. The motivating paper is very recent, so simultaneous or not-yet-indexed work remains a material originality risk. Originality is therefore claimed only **to the best of our knowledge**.

## Limitations

- The exact achievability theorem covers \(q\ge3\), plus binary nonsquare rectangles. It does not settle the binary square case.
- Inputs are uniform and masks/secret transforms are input-independent.
- The privacy metric is maximal correlation; no differential-privacy conclusion follows from this theorem.
- No uniqueness of the optimal masking distribution is claimed.
- The result is not an independent validation of the cited papers' broader claims.

## References

1. Alejandro Cohen, Rafael G. L. D'Oliveira, Alex Sprintson, *Low-Rank Masking for Single-Server Matrix Multiplication*, arXiv:2609.18876v1 (2026). https://arxiv.org/abs/2609.18876
2. Sebastian M. Cioabă, Himanshu Gupta, *On the eigenvalues of Grassmann graphs, Bilinear forms graphs and Hermitian forms graphs*, arXiv:2102.10155 (2021), especially Theorems 4.3 and 4.6. https://arxiv.org/abs/2102.10155
3. Andries E. Brouwer, Sebastian M. Cioabă, Ferdinand Ihringer, Matt McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, Journal of Combinatorial Theory, Series B 133 (2018), 88--121, especially Section 7 and Lemma 7.4. https://arxiv.org/abs/1709.09011
