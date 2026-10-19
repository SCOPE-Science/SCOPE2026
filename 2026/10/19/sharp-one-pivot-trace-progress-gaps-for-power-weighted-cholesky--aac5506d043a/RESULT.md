# Sharp one-pivot trace-progress gaps for power-weighted Cholesky

## Finding

Let \(A\in\mathbb C^{n\times n}\) be a nonzero Hermitian positive-semidefinite matrix with every diagonal entry \(d_i=A_{ii}>0\). A pivot at coordinate \(i\) subtracts \(Ae_i e_i^*A/d_i\), whose **trace decrease** is \(g_i=(A^2)_{ii}/d_i\). For any real \(\beta\ge0\), choose coordinate \(i\) with probability \(d_i^\beta/\sum_j d_j^\beta\); write \(\Delta_\beta(A)\) for the expected trace decrease. Thus \(\beta=0\) is a uniform pivot, and \(\beta=1\) is the standard residual-diagonal rule of randomly pivoted Cholesky.

**Theorem (sharp rank-dependent gap and superlinear failure).** For every such \(A\) of rank \(r\ge1\),
\[
\frac{\Delta_0(A)}{\Delta_1(A)}\le\frac{1+\sqrt r}{2}.
\]
For each fixed integer \(r\ge2\), the constant is the exact supremum over matrices of rank \(r\) and arbitrary finite sizes. For rank one, the ratio equals one. Already in size three and rank two, uniform sampling strictly improves expected one-pivot trace decrease: \(\Delta_0=8/9\) and \(\Delta_1=13/15\). Such reversal is impossible in sizes one and two.

By contrast, for **every fixed real exponent** \(\beta>1\), the ratios \(\Delta_0(A)/\Delta_\beta(A)\) are unbounded even over real positive-semidefinite matrices of rank two and strictly positive diagonals. In an explicit family this ratio is asymptotic to an arbitrary growing parameter \(T\). In particular, the linear weighting exponent has a finite rank-two comparison guarantee that every superlinear exponent loses.

## Assumptions and scope

The update uses exact arithmetic and a single pivot. The random choice is made from all \(n\) initially positive diagonal entries, without rounding, prior pivots, or repeated sampling. The trace improvement is \(\operatorname{tr}(A)-\operatorname{tr}(A-Ae_ie_i^*A/d_i)\), not a norm of a solution vector. Singular positive-semidefinite matrices are admissible, as in the Nyström/partial-Cholesky setting. The rank may be smaller than the number of rows. The comparisons concern **one-step expected progress**, not the ratio of expected residual traces or a guarantee on later iterations.

## Proof

**Step 1: trace gain.** Since \(A\) is Hermitian and \(d_i>0\), \(g_i=\lVert Ae_i\rVert_2^2/d_i>0\). The first-step residual is positive semidefinite. The standard rule gives
\[
\Delta_1(A)=\sum_i\frac{d_i}{\operatorname{tr}A}\frac{(A^2)_{ii}}{d_i}
=\frac{\operatorname{tr}(A^2)}{\operatorname{tr}A}.
\]
Furthermore \(g_i=(A^{1/2}e_i)^*A(A^{1/2}e_i)/\lVert A^{1/2}e_i\rVert_2^2\le\lambda_1\), where \(\lambda_1>0\) is the largest eigenvalue. Hence \(\Delta_0(A)=n^{-1}\sum_i g_i\le\lambda_1\).

**Step 2: spectral rank envelope.** When \(r=1\), all nonzero \(g_i\) equal \(\lambda_1\), proving equality. For \(r\ge2\), list the positive eigenvalues \(\lambda_1\ge\cdots\ge\lambda_r>0\), put \(s=\sum_{j=2}^r\lambda_j/\lambda_1\), and apply Cauchy–Schwarz:
\[
\frac{\Delta_0(A)}{\Delta_1(A)}\le
\frac{1+s}{1+\sum_{j=2}^r(\lambda_j/\lambda_1)^2}
\le\frac{1+s}{1+s^2/(r-1)}.
\]
For \(0\le s\le r-1\), differentiation gives the unique maximizer \(s=\sqrt r-1\). Substitution yields exactly \((1+\sqrt r)/2\). This is a bound for all finite matrix sizes, independently of coherence or eigenvector orientation.

**Step 3: sharpness.** Fix \(r\ge2\), set \(t=1/(\sqrt r+1)\), and for positive integers \(N\) define
\[
A_N=\frac1N J_N\oplus t I_{r-1},
\]
where \(J_N\) is the all-ones matrix. Its positive eigenvalues are \(1,t,\ldots,t\), so \(\operatorname{rank}A_N=r\). All diagonal entries are positive. A pivot in the first block removes trace one; a pivot in a singleton block removes trace \(t\). Consequently
\[
\Delta_0(A_N)=\frac{N+(r-1)t}{N+r-1},\qquad
\Delta_1(A_N)=\frac{1+(r-1)t^2}{1+(r-1)t}.
\]
The ratio tends to \((1+\sqrt r)/2\) as \(N\to\infty\). Thus the universal constant cannot be reduced even though it need not be attained at finite \(N\).

**Step 4: smallest finite reversal.** In dimension two, write \(A=\begin{psmallmatrix}a&c\\\overline c&b\end{psmallmatrix}\) with \(a,b>0\), \(ab\ge|c|^2\). Direct substitution gives
\[
\Delta_1-\Delta_0
=\frac{(a-b)^2}{2(a+b)}\left(1-\frac{|c|^2}{ab}\right)\ge0.
\]
Dimension one gives equality. In dimension three choose \(A=\tfrac12J_2\oplus[2/3]\); its three gains are \(1,1,2/3\). Thus \(\Delta_0=8/9\), while diagonal weighting gives \(\Delta_1=13/15\). The ratio is \(40/39>1\).

**Step 5: every superlinear weighting can fail arbitrarily.** Fix real \(\beta>1\). Choose \(q>(\beta+1)/(\beta-1)\), set \(m_T=\lceil T^q\rceil\), and let
\[
B_T=\frac{T}{m_T}J_{m_T}\oplus[1],\qquad T\to\infty.
\]
This is rank two with positive diagonals. The first block contains \(m_T\) coordinates, each of gain \(T\); the last coordinate has gain one. Uniform sampling yields
\[
\Delta_0(B_T)=\frac{m_T T+1}{m_T+1}\sim T.
\]
The aggregate \(\beta\)-weight of the first block is \(h_T=T^\beta m_T^{1-\beta}=O(T^{\beta-q(\beta-1)})\). The strict condition on \(q\) implies \(Th_T\to0\), hence
\[
\Delta_\beta(B_T)=\frac{T h_T+1}{h_T+1}\to1,
\qquad \frac{\Delta_0(B_T)}{\Delta_\beta(B_T)}\sim T\to\infty.
\]
Every limit follows from these explicit finite-dimensional formulas, rather than from simulation.

## Verification

The standalone Python 3 program `verify.py` uses exact rational arithmetic. Run `python verify.py` without third-party packages. It verifies the explicit three-by-three example; 1,022 sampled rational two-by-two positive-semidefinite cases; 176 directly constructed finite block matrices; six perfect-square-rank sharpness profiles; and superlinear examples with integer exponents two through four. The infinite-rank and real-exponent statements are supplied by the proof, not inferred from the finite checks.

## Relationship to prior work

Chen, Epperly, Tropp, and Webber [1] define residual-diagonal RPCholesky and establish the exact expected residual identity \(A-A^2/\operatorname{tr}A\) along with multi-step low-rank error bounds. That identity supplies the baseline trace-gain expression in Step 1 but **does not by itself state the sharp uniform-pivot comparison, its minimal dimension, or the superlinear-exponent counterexample**. Steinerberger [2] explicitly considers the Gibbs power family and proves a Frobenius-oriented guarantee for exponent two; its experiments sometimes favor uniform pivots, but no rank-two diverging trace-progress comparison or sharp rank envelope appears in its result. Epperly, Tropp, and Webber [3] develop a rejection-sampling implementation of the same pivot distribution, rather than a different one-step uniform comparison.

## Limitations

This is a first-pivot trace-progress statement. It does not establish a corresponding \(\sqrt r\)-factor for whole-run error or show that repeated superlinear pivoting is universally inferior. The counterexamples use singular kernel matrices; they do not prove the same unbounded behavior for fixed-size positive-definite inputs. The theorem makes no uniform comparison claim for exponents strictly between zero and one. The sharp constant is a supremum over growing matrix sizes. A separately indexed 2026 analysis of RPCholesky [4] was located by abstract but its full text was inaccessible during this comparison, leaving a residual risk of unobserved equivalent statements. The literature search cannot establish global uniqueness.

## References

[1] Y. Chen, E. N. Epperly, J. A. Tropp, R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503, first submitted 2022-07-13, Sections 2.3 and 5 and Appendix C.

[2] S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, arXiv:2404.11487, first submitted 2024-04-17, Sections 1–3.

[3] E. N. Epperly, J. A. Tropp, R. J. Webber, *Embrace rejection: Kernel matrix approximation by accelerated randomly pivoted Cholesky*, arXiv:2410.03969, first submitted 2024-10-04, Sections 2 and 4.

[4] E. N. W. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm*, arXiv:2608.20633, first submitted 2026-08-21; abstract located, full text not inspected.
