# Exact self-commutator variation and critical polar defect of weighted harmonic Bergman monomial shifts

## Finding
For every real \(\alpha>-1\) and integer \(n\ge1\), consider the harmonic Bergman compression \(T_{\alpha,n}=P_{h,\alpha}M_{z^n}|_{H^2_{h,\alpha}}\). Put
\[
m_j=\frac{\Gamma(j+1)\Gamma(\alpha+2)}{\Gamma(j+\alpha+2)}\quad(j\ge0),\qquad v_r=\frac{m_n^2}{m_rm_{n-r}}\quad(0\le r<n).
\]
The self-commutator \(C_{\alpha,n}=T_{\alpha,n}^*T_{\alpha,n}-T_{\alpha,n}T_{\alpha,n}^*\) is self-adjoint and trace class, with
\[
\boxed{\operatorname{Tr}(C_{\alpha,n})=0,\qquad \|C_{\alpha,n}\|_{S_1}=2\sum_{r=0}^{n-1}(1-v_r).}
\]
The trace norm increases strictly with \(\alpha\), tends to zero as \(\alpha\downarrow-1\), and tends to \(2n\) as \(\alpha\to\infty\). In particular,
\[
\boxed{\|C_{0,n}\|_{S_1}=\frac{n(5n+1)}{3(n+1)}.}
\]
The positive polar defect \(Q_{\alpha,n}=I-|T_{\alpha,n}|\) is compact and satisfies, for finite \(p>0\),
\[
Q_{\alpha,n}\in S_p\ \Longleftrightarrow\ p>1,\qquad
\boxed{\lim_{N\to\infty}N s_N(Q_{\alpha,n})=n(\alpha+1)},
\]
where singular values are decreasing and indexed from one. Therefore its logarithmic singular-value sum obeys
\[
\boxed{\lim_{N\to\infty}\frac{\sum_{j=1}^N s_j(Q_{\alpha,n})}{\log N}=n(\alpha+1).}
\]
These formulas describe the precise trace-class nonnormality and critical weak-trace-class polar deviation of the monomial Toeplitz family.

## Assumptions and scope
The unit disk \(\mathbb D\) carries probability measure \(dA_\alpha=(\alpha+1)(1-|z|^2)^\alpha\,dA\), with \(dA=\pi^{-1}dxdy\). The space \(H^2_{h,\alpha}\) is the closure in \(L^2(dA_\alpha)\) of complex-valued harmonic polynomials, and \(P_{h,\alpha}\) is its orthogonal projection. The Toeplitz symbol is exactly \(z^n\), and the assertions cover all \(n\ge1\) and every \(\alpha>-1\), not arbitrary polynomial symbols. Trace norms and Schatten ideals refer to operators on the complex Hilbert space \(H^2_{h,\alpha}\).

## Proof
**1. Orthogonal monomial compression.** Radial integration gives \(\int_\mathbb D|z|^{2j}dA_\alpha=m_j\), hence the family
\[
e_k=\begin{cases}z^k/\sqrt{m_k}&k\ge0,\\\overline z^{-k}/\sqrt{m_{-k}}&k<0\end{cases}\qquad(k\in\mathbb Z)
\]
is a complete orthonormal basis (the constant is counted once). Angular orthogonality implies \(T_{\alpha,n}e_k=w_k e_{k+n}\), with all weights positive and
\[
w_k^2=\begin{cases}
 m_{k+n}/m_k,&k\ge0,\\
 m_j/m_{j-n},&k=-j,\ j\ge n,\\
 m_n^2/(m_jm_{n-j}),&k=-j,\ 1\le j<n.
\end{cases}
\]
For the bridge case, the sole nonzero angular projection is onto \(z^{n-j}\), with coefficient \(m_n/\sqrt{m_jm_{n-j}}\). This independently verifies the nontrivial middle coefficient.

**2. Unique valleys of squared weights.** The moments obey \(m_{j+1}/m_j=(j+1)/(j+\alpha+2)\), strictly increasing in \(j\). Consequently the sequence \(\log m_j\) is strictly convex. Fix a residue \(r\in\{0,\ldots,n-1\}\) and follow the weight squares indexed \(k=r+qn\) as \(q\) runs through all integers. For \(k\ge0\), \(w_k^2\) increases with \(k\), and for \(k\le-n\) it decreases with \(k\). The bridge weight at \(k=r-n\) is \(v_r\). Convexity gives \(m_n^2\le m_r m_{2n-r}\) and \(m_n^2\le m_{n-r}m_{n+r}\), proving \(v_r\le w_{r-2n}^2\) and \(v_r\le w_r^2\). Thus every bi-infinite residue chain decreases from the limit one to exactly \(v_r\) and rises to the limit one. At \(r=0\) the adjacent positions \(k=-n\) and \(k=0\) share the minimum; otherwise it is unique.

**3. Total variation gives the exact commutator norm.** The commutator is diagonal:
\[
C_{\alpha,n}e_k=(w_k^2-w_{k-n}^2)e_k.
\]
The absolute sum along each residue chain equals the descending variation \(1-v_r\) plus the ascending variation \(1-v_r\); it is summable. Hence \(C_{\alpha,n}\in S_1\) and its total trace is the telescoped difference of equal endpoint limits, zero. Summing residues yields the first formula. Differentiating \(\log v_r\) with respect to \(\alpha\) gives
\[
\frac{d}{d\alpha}\log v_r=\psi(\alpha+r+2)+\psi(\alpha+n-r+2)-2\psi(\alpha+n+2)<0,
\]
since the digamma function \(\psi\) is strictly increasing and \(r,n-r\le n\), with at least one strict inequality. Every \(v_r\) decreases strictly from one to zero over the parameter interval. For \(\alpha=0\), substitution \(m_j=1/(j+1)\) and summation of the quadratic polynomial \((r+1)(n-r+1)\) yields the rational closed form.

**4. Exact polar-defect ideal threshold.** Since all weights are positive and bounded by one, \(|T_{\alpha,n}|e_k=w_k e_k\); therefore \(Q_{\alpha,n}e_k=(1-w_k)e_k\). For either tail \(k\to+\infty\) or \(k\to-\infty\), the moment-ratio formula is a product of \(n\) factors \(j/(j+\alpha+1)\), and expansion gives
\[
1-w_k=\frac{n(\alpha+1)}{2|k|}+O(|k|^{-2}).
\]
There are exactly two tails, each with one basis index per integer, so the number of singular values exceeding \(t\) is \(n(\alpha+1)t^{-1}+O(1)\) as \(t\downarrow0\). Inverting this counting asymptotic gives \(s_N(Q_{\alpha,n})=n(\alpha+1)/N+O(N^{-2})\), hence the asserted weak-trace-class coefficient, harmonic logarithmic sum and sharp \(S_p\) criterion. The finitely many bridge weights do not affect these limits.

## Verification
The accompanying `verify_harmonic.py` uses exact rational moment arithmetic for seven weights and fifteen monomial degrees, checks independently computed angular Gram coefficients against all three shift-weight branches, and verifies monotonicity and valley positions for 840 residue chains. It confirms sixty rational unweighted trace-norm identities and checks tail coefficients numerically for four weights and four degrees at two large indices. The script prints its precise finite check totals upon successful completion. None of the finite computations replaces the proof for arbitrary real \(\alpha\), arbitrary degree or infinite ideal thresholds.

## Relationship to prior work
Huang, Wang and Zhao (first publicly posted 2026-10-07, arXiv:2610.09638v1) study the spectral structure and Weyl theorem for general analytic-polynomial Toeplitz symbols on the unweighted harmonic Bergman space. Their spectral picture does not state these exact trace-class commutator norms or the weighted critical polar-defect singular-value coefficient. Guo and Zheng (2002) establish essential spectral structure, compact commutator ideals and invertibility of monomial harmonic Bergman Toeplitz operators, but the explicit quantified trace norm and weighted weak-Schatten profile are not obtained by their stated results. Nishio and Tanaka (2017) study radial-measure harmonic Bergman operators with radial symbols, rather than the analytic angular monomial family studied here. These differences concern mathematical implications, not merely terminology.

## Limitations
The theorem covers monomial symbols, not arbitrary polynomials; it does not claim novelty for the known spectral circle or monomial invertibility. The trace norm is for the *self-commutator*, whereas the weak-Schatten limit is for the *polar defect*; these are different operators. A 2021 related Wang–Zhao spectral paper was not fully inspected in this comparison, and some historical weighted-shift literature may contain equivalent diagonal formulas. Priority remains subject to broader independent literature checking. No independent scientific audit has been performed.

## References
1. M. Huang, J. Wang, X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638v1 (first public 2026-10-07), https://arxiv.org/abs/2610.09638.
2. K. Guo, D. Zheng, *Toeplitz algebra and Hankel algebra on the harmonic Bergman space*, J. Math. Anal. Appl. **276** (2002), 213–230, https://math.vanderbilt.edu/zhengd/HankelA.pdf.
3. K. Nishio, Y. Tanaka, *Harmonic Bergman kernels and Toeplitz operators on the ball with radial measures*, Revue Roumaine Math. Pures Appl. **62** (2017), https://imar.ro/journals/Revue_Mathematique/pdfs/2017/1/8.pdf.
