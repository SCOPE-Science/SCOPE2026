# Deflation-history contamination can make weighted-mass ACA arbitrarily suboptimal

## Statement

Loe, Huang, and Needell (2026) propose, for a symmetric positive-semidefinite matrix, the weighted-mass diagonal ACA score
\[
m_i(A,R)=\sum_{j\in\mathcal N_i}(R_{jj}A_{ji})^2,
\]
where \(R\) is the current ACA residual while the correlation factor \(A_{ji}\) is taken from the original matrix. Their stated convention is self-containing in the one-neighbor case: when \(\ell=1\), the score uses \(R_{ii}A_{ii}\). The rule is presented as a problem-dependent proxy rather than a generally convergent method.

The mixed use of the current residual and the original matrix creates a deflation-history dependence. In fact, it can force a pivot whose one-step Frobenius improvement is arbitrarily worse than another available diagonal pivot, even when the component responsible for the stale correlation has already been removed exactly.

### Theorem 1 — unbounded rank-two approximation factor

For every integer \(N\ge 2\), there is a positive-semidefinite matrix \(A_N\in\mathbb R^{(N+2)\times(N+2)}\) such that weighted-mass diagonal ACA selects two pivots whose Frobenius residual is \(N\), whereas another legal two-pivot diagonal ACA approximation has Frobenius residual \(1\). This holds for every collection of self-containing neighborhoods \(\mathcal N_i\), independently of their sizes or geometry.

More explicitly, let the indices be \(q\), a good set \(G\) of cardinality \(N\), and a bad index \(b\). Let
\[
R_N=0\oplus J_N\oplus[1],\qquad J_N=\mathbf 1\mathbf 1^\top,
\]
and put \(s=N^{1/4}\) and
\[
v_N=(2s,0_G,s)^\top,\qquad A_N=R_N+v_Nv_N^\top.
\]
Then \(A_N\succeq0\). Weighted-mass ACA selects \(q\) first and \(b\) second. After those two updates,
\[
\|R^{(2)}_{\rm WM}\|_F=N.
\]
If the same first pivot \(q\) is followed instead by any \(g\in G\), then
\[
\|R^{(2)}_{q,g}\|_F=1.
\]
Consequently the weighted-mass rank-two residual is at least a factor \(N\) larger than the best rank-two diagonal ACA residual.

The comparison with the unconstrained best rank-two approximation is also explicit. The nonzero spectrum of \(A_N\) consists of the eigenvalue \(N\) from \(J_N\) and the two eigenvalues of
\[
\begin{pmatrix}
4\sqrt N&2\sqrt N\\
2\sqrt N&1+\sqrt N
\end{pmatrix}.
\]
Hence the optimal rank-two Frobenius error is
\[
\lambda_-(N)=\frac{5\sqrt N+1-\sqrt{25N-6\sqrt N+1}}{2}\longrightarrow\frac45,
\]
so
\[
\frac{\|R^{(2)}_{\rm WM}\|_F}{\|A_N-(A_N)_2\|_F}
=\frac{N}{\lambda_-(N)}\sim\frac54N.
\]

## Proof

The only nonzero entries coupling \(q\) or \(b\) to the rest are
\[
(A_N)_{qq}=4\sqrt N,\qquad
(A_N)_{qb}=2\sqrt N,\qquad
(A_N)_{bb}=1+\sqrt N,
\]
while the \(G\times G\) block is \(J_N\).

Initially the current residual equals \(A_N\). Because every neighborhood contains its own candidate,
\[
m_q\ge (A_{qq}A_{qq})^2=A_{qq}^4=256N^2.
\]
For the bad index, only \(q\) and \(b\) can contribute, so
\[
m_b\le (A_{qq}A_{qb})^2+A_{bb}^4
=64N^2+(1+\sqrt N)^4
\le 80N^2,
\]
where \(1+\sqrt N\le2\sqrt N\). For any \(g\in G\), at most the \(N\) entries of the all-ones block contribute, each by one, so \(m_g\le N\). Thus \(q\) is the unique first pivot.

Since \(R_Ne_q=0\) and \(A_N(:,q)=v_N(v_N)_q\), the first diagonal ACA update removes the added rank-one term exactly:
\[
A_N-\frac{A_N(:,q)A_N(q,:)}{(A_N)_{qq}}
=R_N+v_Nv_N^\top-v_Nv_N^\top
=R_N.
\]
At this state the source score still uses the original \(A_N\). The bad candidate therefore has
\[
m_b\ge (R_{bb}A_{bb})^2=(1+\sqrt N)^2>N,
\]
whereas every good candidate satisfies \(m_g\le N\). Thus \(b\) is the unique second pivot for every self-containing neighborhood system.

Pivoting \(b\) removes only the scalar \([1]\), leaving \(J_N\), whose Frobenius norm is \(N\). Pivoting any \(g\in G\) instead removes \(J_N\) exactly and leaves only \([1]\), whose Frobenius norm is \(1\). This proves the rank-two factor.

The rank-two SVD formula follows because the matrix is a direct sum of \(J_N\) and the displayed \(2\times2\) block. Its smaller eigenvalue is \(\lambda_-(N)\), and a one-term expansion of the square root gives \(\lambda_-(N)\to4/5\).

## Mechanism: the score is not a function of the current residual

The obstruction is structural. Let \(R\succeq0\) satisfy \(Re_q=0\), and let \(v_q\ne0\). Define
\[
A=R+vv^\top.
\]
A diagonal ACA pivot at \(q\) removes \(vv^\top\) exactly and leaves the same current residual \(R\), regardless of the other entries of \(v\). Nevertheless the next weighted-mass score is
\[
m_i(A,R)=\sum_{j\in\mathcal N_i}
\bigl(R_{jj}(R_{ji}+v_jv_i)\bigr)^2,
\]
which generally varies with the already-deflated vector \(v\). Two approximation histories that arrive at the same residual can therefore induce different subsequent scores.

In the family above this stale component is not asymptotically large. Indeed,
\[
\|v_Nv_N^\top\|_2=\|v_N\|_2^2=5\sqrt N,
\qquad
\|R_N\|_2=N,
\]
so
\[
\frac{\|v_Nv_N^\top\|_2}{\|R_N\|_2}=\frac5{\sqrt N}\to0.
\]
The same ratio tends to zero in Frobenius norm. Thus an already removed component that is asymptotically negligible relative to the surviving residual can still determine the next weighted-mass pivot through the use of original-matrix correlations.

## Exact one-step Frobenius benchmark

For a current symmetric residual \(R\), a diagonal pivot \(p\) with \(a=R_{pp}>0\) and \(c=R(:,p)\) produces
\[
R^+=R-\frac{cc^\top}{a}.
\]
Direct expansion gives the exact one-step Frobenius decrease
\[
\Delta_p
=\|R\|_F^2-\|R^+\|_F^2
=\frac{2}{a}c^\top Rc-\frac{\|c\|_2^4}{a^2}.
\]
This identity is a standard rank-one norm expansion and is used here only as a benchmark, not as an originality claim.

For \(R_N\), a good pivot has \(\Delta_g=N^2\), while the bad pivot has \(\Delta_b=1\). Thus the weighted-mass rule can select a pivot whose exact one-step Frobenius gain is only \(1/N^2\) of the available gain.

## Residual-consistent alternatives

The obstruction comes specifically from mixing \(R_{jj}\) with the stale entry \(A_{ji}\). Replacing the latter by the current residual entry,
\[
\widetilde m_i(R)=\sum_{j\in\mathcal N_i}(R_{jj}R_{ji})^2,
\]
makes the score a function of the current approximation state and therefore removes this deflation-history dependence. With full neighborhoods, the counterexample gives \(\widetilde m_g=N\) and \(\widetilde m_b=1\), so the residual-consistent version chooses a good pivot. This observation is not a general convergence theorem for \(\widetilde m_i\); local neighborhoods can still omit globally useful correlations.

The exact gain \(\Delta_p\) is another residual-state-invariant target, but evaluating it for every candidate requires substantially more global residual information than the inexpensive weighted-mass proxy. The counterexample therefore identifies a design tradeoff rather than a cost-free universal replacement.

## Scope and limitations

The family is synthetic and positive semidefinite but singular. It is not shown to arise from the radial-basis Galerkin stiffness matrices used in the motivating experiments. The result therefore does not contradict the reported empirical performance of weighted-mass pivoting on those problems. It establishes a worst-case obstruction for the algorithm as stated on general positive-semidefinite inputs.

The counterexample concerns approximation quality at a prescribed rank. The constructed matrix has rank three, and after the bad second pivot a third good pivot removes the remaining \(J_N\) block exactly; the theorem is not a claim of asymptotic nonconvergence.

The theorem uses the self-containing neighborhood convention, which is the convention indicated by the source paper's description of the \(\ell=1\) case. No claim is made here for a self-excluding variant.

## Reproducibility

`artifacts/verify_counterexample.py` constructs the matrices directly, executes the weighted-mass score with full neighborhoods, performs the ACA updates, and compares the selected residual with a good second pivot and the best rank-two SVD error. `artifacts/verification_output.txt` records representative outputs.

## References

1. T. Loe, L. Huang, D. Needell, *A Geometric View of Adaptive Cross Approximation via Exterior Algebra*, arXiv:2609.17947v1, 2026. https://arxiv.org/abs/2609.17947
2. Y. Chen, E. N. Epperly, J. A. Tropp, R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, Communications on Pure and Applied Mathematics 78 (2025), 995–1041. https://doi.org/10.1002/cpa.22234
3. S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, arXiv:2404.11487, 2024. https://arxiv.org/abs/2404.11487
4. S. Massei, *Some algorithms for maximum volume and cross approximation of symmetric semidefinite matrices*, BIT Numerical Mathematics 62 (2022), 195–220. https://doi.org/10.1007/s10543-021-00872-1
5. H. Harbrecht, M. Peters, R. Schneider, *On the low-rank approximation by the pivoted Cholesky decomposition*, Applied Numerical Mathematics 62 (2012), 428–440. https://doi.org/10.1016/j.apnum.2011.10.001
