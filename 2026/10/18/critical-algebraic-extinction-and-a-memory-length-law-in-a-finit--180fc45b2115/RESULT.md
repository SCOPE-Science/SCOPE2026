# Critical algebraic extinction and a memory-length law in a finite-memory fractional logistic map

## Finding
Fix an integer \(M\ge1\) and a fractional order \(0<q\le1\). Set
\[
g_j(q)=(-1)^j\binom qj,\qquad T_M(q)=\sum_{j=0}^M g_j(q),\qquad r_c=1+T_M(q).
\]
Consider the exact finite-memory Grünwald--Letnikov logistic recurrence
\[
x_{n+1}=r x_n(1-x_n)-x_n-\sum_{j=1}^{M}g_j(q)x_{n+1-j},
\qquad n\ge0.
\]
Define \(p_1=q+T_M(q)\) and \(p_j=-g_j(q)\) for \(2\le j\le M\), and \(\delta=p_1/r_c\). **Theorem.** At the exact neutral threshold \(r=r_c\), every initial history satisfying \(0<x_{-M+1},\ldots,x_0<\delta\) generates a globally defined trajectory with \(0<x_n<\delta\) for every \(n\ge1\), and
\[
\boxed{\lim_{n\to\infty}n x_n=\frac{\tau_M(q)}{r_c}},
\qquad \tau_M(q)=\sum_{j=1}^M j p_j.
\]
For \(0<q<1\), these constants are explicitly
\[
T_M(q)=\frac{\Gamma(M+1-q)}{\Gamma(1-q)\Gamma(M+1)},
\qquad
\tau_M(q)=T_M(q)\left(1+\frac{qM}{1-q}\right).
\]
For \(q=1\), one has \(T_M(1)=0\), \(r_c=1\), and \(\tau_M(1)=1\) at every \(M\). In particular,
\[
\lim_{N\to\infty}\frac{\sum_{n=1}^{N}x_n}{\log N}
=\frac{\tau_M(q)}{r_c}.
\]
For every fixed \(0<q<1\), the leading critical amplitude grows with memory as
\[
\boxed{\frac{\tau_M(q)}{r_c}\sim
\frac{q}{\Gamma(2-q)}M^{1-q}\quad(M\to\infty).}
\]
The \(n\to\infty\) limit is taken at each fixed finite \(M\); the result does not claim a uniform joint-in-\(n,M\) asymptotic.

## Assumptions and scope
The recurrence is the finite-window convolution in the cited 2026 source, not an infinite-memory Caputo model. A generalized binomial coefficient is \(\binom q0=1\) and \(\binom qj=q(q-1)\cdots(q-j+1)/j!\) for \(j\ge1\). All histories are real and strictly positive. For \(0<q<1\), the signs are \(g_1=-q\) and \(g_j<0\) for all \(j\ge2\); consequently \(p_j>0\) for all \(1\le j\le M\). At \(q=1\) the delayed coefficients except the first vanish. No assertion is made about arbitrary initial histories or other parameter ranges.

## Proof
**1. Renewal reduction and the positivity domain.** The generalized-binomial identity gives
\[
T_M(q)=(-1)^M\binom{q-1}{M}
=\frac{\Gamma(M+1-q)}{\Gamma(1-q)\Gamma(M+1)}>0
\]
for \(0<q<1\). Since \(g_1=-q\), at \(r=r_c\) the recurrence rearranges exactly to
\[
x_{n+1}=\sum_{j=1}^{M}p_jx_{n+1-j}-r_cx_n^2,
\qquad \sum_{j=1}^{M}p_j=1.
\tag{1}
\]
For \(M=1\) the sum is simply \(p_1=1\). If all current history values lie strictly between \(0\) and \(\delta=p_1/r_c\), then the first contribution \(p_1x_n-r_cx_n^2=x_n(p_1-r_cx_n)\) is strictly positive, all other summands are nonnegative, and the upper bound from (1) is strictly less than \(\sum_jp_j\delta=\delta\). Thus the open history cube is forward invariant by induction.

**2. An exact descending renewal mass.** First suppose \(0<q<1\). Write \(X_n=(x_n,x_{n-1},\ldots,x_{n-M+1})^{\mathsf T}\), and let \(P\) be the \(M\times M\) companion stochastic matrix whose first row is \((p_1,\ldots,p_M)\) and whose lower subdiagonal is all ones. Then
\[
X_{n+1}=PX_n-r_cx_n^2e_1.
\]
For \(k=0,\ldots,M-1\), set \(w_k=\sum_{j=k+1}^M p_j\), so \(w_0=1\), \(w_k>0\), \(w^{\mathsf T}P=w^{\mathsf T}\), and \(\sum_{k=0}^{M-1}w_k=\sum_{j=1}^M jp_j=\tau_M\). Define \(E_n=w^{\mathsf T}X_n\). The exact identity
\[
E_{n+1}=E_n-r_cx_n^2
\tag{2}
\]
shows \(E_n>0\) and \(\sum_{n=0}^{\infty}x_n^2\le E_0/r_c<\infty\). Thus \(x_n\to0\), every finite lag tends to zero, and \(E_n\to0\). Since every \(w_k>0\), all coordinates satisfy \(\|X_n\|\le C E_n\) with a finite constant depending on \(q,M\) and the chosen norm.

**3. Asymptotic equilibration of the lag coordinates.** Every \(p_j>0\); in particular \(p_1>0\), so the finite stochastic companion matrix \(P\) is primitive and
\[
P^k\longrightarrow \Pi={\bf1}\,w^{\mathsf T}/\tau_M
\quad(k\to\infty).
\]
For fixed \(k\), iteration and the bound \(x_{n+i}\le E_{n+i}\le E_n\) imply
\[
X_{n+k}=P^kX_n+O_k(E_n^2),
\quad E_{n+k}=E_n+O_k(E_n^2).
\]
As \(n\to\infty\), division by \(E_n\) and \(\|X_n\|/E_n\le C\) give
\[
\limsup_{n\to\infty}
\frac{\|X_{n+k}-E_{n+k}{\bf1}/\tau_M\|}{E_n}
\le C\|P^k-\Pi\|.
\]
Letting \(k\to\infty\) proves
\[
\lim_{n\to\infty}\frac{x_n}{E_n}=\frac1{\tau_M}.
\tag{3}
\]
The shift of indices by the fixed \(k\) causes no issue because \(E_{n+k}/E_n\to1\), already established.

**4. Exact critical rate and cumulative load.** By (2)--(3),
\[
\frac1{E_{n+1}}-\frac1{E_n}
=\frac{r_c(x_n/E_n)^2}{E_{n+1}/E_n}
\longrightarrow\frac{r_c}{\tau_M^2}.
\]
Taking arithmetic means of the reciprocal increments yields
\(E_n\sim \tau_M^2/(r_c n)\). Equation (3) then yields \(x_n\sim\tau_M/(r_c n)\), including the positive universal prefactor independent of initial history inside the invariant cube. Summing this asymptotic, or applying Stolz--Cesàro, gives \(\sum_{n=1}^N x_n\sim (\tau_M/r_c)\log N\).

For \(q=1\), the recurrence is exactly \(x_{n+1}=x_n-x_n^2\) regardless of \(M\), with \(0<x_0<1\). Monotone convergence to zero and
\(x_{n+1}^{-1}-x_n^{-1}=1/(1-x_n)\to1\)
give \(nx_n\to1\), and the harmonic-sum conclusion follows.

**5. Explicit memory prefactor.** The generalized-binomial telescoping identity and \(j\binom qj=q\binom{q-1}{j-1}\) yield
\[
\sum_{j=1}^{M}j[-g_j(q)]=\frac{qM}{1-q}T_M(q).
\]
Using \(p_1=q+T_M\), one obtains \(\tau_M=T_M[1+qM/(1-q)]\). For fixed \(0<q<1\), the standard gamma ratio satisfies \(T_M\sim M^{-q}/\Gamma(1-q)\), hence
\[
\tau_M\sim\frac{q}{(1-q)\Gamma(1-q)}M^{1-q}
=\frac{q}{\Gamma(2-q)}M^{1-q},
\qquad r_c=1+T_M\longrightarrow1,
\]
which proves the last assertion. \(\square\)

## Verification
A standalone standard-library Python verifier is included as `verify_critical_gl.py`. It checks exact rational identities for 45 combinations of \(q\) and \(M\), the discrete renewal-mass identity on six trajectories with up to 150,000 steps, their finite-time proximity to the asymptotic coefficient, and the large-memory gamma law in three representative cases. Its numerical trajectory tests are finite experiments and are not substitutes for the analytic proof. The proof itself uses exact positivity, finite-state Perron--Frobenius mixing, and elementary reciprocal increments; no external theorem checker or independent audit is claimed.

## Relationship to prior work
Dong, Li, Li and Xie (preprint posted 20 July 2026, equations (1)--(5), sections 3--5) define the same finite-memory GL map and analyze its fixed-point flip boundary and later period doublings. The present theorem concerns a different natural threshold: the neutral zero fixed point, not the nonzero fixed point's \(-1\) multiplier. Its exact global-on-a-positive-cube \(1/n\) law and memory-dependent coefficient are not stated in the inspected source. Edelman's 2022 full-text analysis treats fixed-point stability and algebraic convergence in different, infinite-history generalized fractional maps, not the finite-window renewal identity here. Bouzeraa, Bououden and Abdelouahab (2023) study finite-memory fractional logistic maps and report numerical bifurcation/chaos; their full article was not accessible for decisive whole-document comparison, so possible earlier coverage is an explicit residual risk.

## Limitations
The theorem holds for each finite \(M\) and strictly positive sufficiently small histories at the **exact neutral threshold**. It neither classifies all positive histories nor the dynamics beyond that threshold. The asymptotic memory-length law is an iterated-limit coefficient, not uniform control when \(M\) grows together with iteration count. Existing general center-manifold or nonlinear-renewal theorems could potentially imply parts of the result, and a complete priority assessment requires independent bibliographic review, especially of inaccessible older finite-memory articles. No independent audit has been performed.

## References
1. Z. Dong, H. Li, S. Li, Y. Xie, *Memory-Dependent Shifts of the Period-Doubling Cascade in the Finite-Memory Grünwald--Letnikov Fractional Logistic Map*, first posted 2026-07-20, https://www.preprints.org/manuscript/202607.1375 ; journal version DOI https://doi.org/10.3390/math14173032.
2. M. Edelman, *Stability of Fixed Points in Generalized Fractional Maps of the Orders \(0<\alpha<1\)*, arXiv:2209.01719 (2022), https://arxiv.org/html/2209.01719v1.
3. S. E. I. Bouzeraa, R. Bououden, M. S. Abdelouahab, *Fractional logistic map with fixed memory length*, *International Journal of General Systems* 52 (2023), 653--663, DOI https://doi.org/10.1080/03081079.2023.2201001.
