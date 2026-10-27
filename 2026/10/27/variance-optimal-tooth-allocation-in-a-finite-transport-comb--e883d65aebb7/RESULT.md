# Variance-optimal tooth allocation in a finite transport comb

## Finding

Consider a finite comb with backbone vertices \(b_0,b_1,\ldots,b_N\), \(N\ge2\), and one reflecting linear tooth of length \(\ell_i\in\mathbb Z_{\ge0}\) attached to each \(b_i\), \(0\le i<N\). Every edge carries transition rate one in each direction. A continuous-time random walker starts at \(b_0\) and is absorbed at \(b_N\); write \(T\) for the absorption time. Define
\[
 m_i=i+1+\sum_{j=0}^{i}\ell_j,\quad q(L)=\frac{L(L+1)(2L+1)}3,\quad S_N=\sum_{k=1}^N k^{-1/2}.
\]
The exact first two cumulants are
\[
 \mathbb ET=\sum_{i=0}^{N-1}m_i,
 \qquad
 \operatorname{Var}(T)=\sum_{i=0}^{N-1}(2(N-i)-1)m_i^2+\sum_{i=0}^{N-1}(N-i)q(\ell_i).
\]
At a fixed total tooth budget \(M=\sum_i\ell_i\), the **globally optimal variance** satisfies, for every fixed \(N\ge2\) as \(M\to\infty\),
\[
 \min_{\ell\in\mathbb Z_{\ge0}^{N},\ \sum\ell_i=M}\operatorname{Var}(T)
 =\frac{2M^3}{3S_N^2}+O_N(M^2).
\]
Every sequence of exact integer minimizers obeys the **unique asymptotic allocation law**
\[
 \frac{\ell_i}{M}\longrightarrow\frac{(N-i)^{-1/2}}{S_N}\qquad(0\le i<N).
\]
Concentrating all teeth at the backbone site nearest the target uniquely minimizes the mean, but yields variance \(2M^3/3+O_N(M^2)\), so its variance-to-optimum ratio tends to \(S_N^2>1\). In particular, large-budget variance minimization requires teeth at *every* backbone site; minimizing the mean and minimizing the variance are incompatible.

The two-edge backbone (the smallest nontrivial case) also has a complete **finite-budget** classification. For \(N=2\), let \(x=\ell_0\), \(\ell_1=M-x\), with \(0\le x\le M\) integral. The unique variance minimizer is
\[
 x_*(M)=\max\!\left\{0,\left\lceil\frac{\sqrt{32M^2+112M+92}-4M-14}{4}\right\rceil\right\}.
\]
It is \(x_*=0\) exactly for \(M=0,1,2\), and \(x_*\ge1\) for every \(M\ge3\). Thus at the sharp budget \(M=3\) the optimum moves away from the mean-optimal all-near-target arrangement: its variance falls from \(56\) to \(51\), while its mean increases from \(6\) to \(7\), in unit inverse-edge-rate time.

## Assumptions and scope

All tooth lengths count *edges* (equivalently additional vertices), and a zero length means no tooth. Teeth do not touch one another. The target \(b_N\) has no tooth and terminates the backbone. "Unit edge rate" means that for each neighboring vertex the jump clock has rate one, so a vertex of degree \(d\) has exponential holding time with mean \(1/d\). The finite graph ensures almost-sure absorption and finite moments of all orders. No drift, resetting, additional traps, or rate heterogeneity is assumed. The asymptotic is for fixed \(N\) and integer \(M\to\infty\), not a joint limit.

## Proof

**First-passage factorization.** Let \(\tau_i\) be the time required to go from \(b_i\) to \(b_{i+1}\) on its first visit to \(b_i\). The path from the starting vertex to the target visits \(b_0,b_1,\ldots,b_N\) in that order; the strong Markov property makes the consecutive \(\tau_i\) independent, with \(T=\sum_{i=0}^{N-1}\tau_i\). Set \(f_i(s)=\mathbb E\exp(-s\tau_i)\).

At any non-target backbone vertex, conditioning on its competing unit-rate edge clocks gives the exact renewal identity
\[
 f_i(s)^{-1}=1+s+\mathbf1_{i>0}(1-f_{i-1}(s))
 +\mathbf1_{\ell_i>0}(1-g_{\ell_i}(s)),
\]
where \(g_L(s)\) is the transform for the first return to the tooth base from its first vertex, on a tooth of length \(L\). The identity follows directly by solving \((s+d)f=1+f\sum h\) for the first step, where the distinguished forward neighbor contributes \(1\) and each other neighbor contributes its first-return transform \(h\). In particular, \(f_i(0)=g_L(0)=1\).

**Tooth moments.** On the length-\(L\) tooth, let \(U_j\) be the mean time to reach its base from depth \(j\), with \(U_0=0\). The continuous-time Poisson equations are \(2U_j-U_{j-1}-U_{j+1}=1\) for \(1\le j<L\) and \(U_L-U_{L-1}=1\). Their unique solution is \(U_j=j(2L+1-j)/2\), so \(-g_L'(0)=U_1=L\). If \(V_j\) is the corresponding raw second moment, then \(2V_j-V_{j-1}-V_{j+1}=2U_j\) and \(V_L-V_{L-1}=2U_L\), with \(V_0=0\). Summing the first differences yields
\[
 g_L''(0)=V_1=2\sum_{j=1}^{L}U_j
 =\frac{L(L+1)(2L+1)}3=q(L).
\]
These equations remain valid with \(L=0\) when the absent-tooth contribution is set to zero.

**Cumulants.** Differentiating the reciprocal transform at \(s=0\) gives \(\mathbb E\tau_0=1+\ell_0\) and recursively \(\mathbb E\tau_i=1+\mathbb E\tau_{i-1}+\ell_i=m_i\). Writing \(v_i=\operatorname{Var}(\tau_i)=(\log f_i)''(0)\), differentiating twice gives
\[
 v_0=m_0^2+q(\ell_0),\qquad
 v_i=v_{i-1}+m_{i-1}^2+m_i^2+q(\ell_i)\quad(i\ge1).
\]
Indeed for \(f=1/D\), \((\log f)''(0)=D'(0)^2-D''(0)\), and each backward-return second moment is \(v_{i-1}+m_{i-1}^2\). Summing the independent \(\tau_i\) variances and collecting coefficients of each \(m_i^2\) and \(q(\ell_i)\) proves the stated exact formula and the mean formula.

**Global asymptotic optimization.** Put \(w_i=N-i>0\). Since \(q(L)=(2/3)L^3+L^2+L/3\), all omitted terms in the variance are nonnegative, and therefore
\[
 \operatorname{Var}(T)\ge\frac23\sum_iw_i\ell_i^3
 \ge\frac{2M^3}{3(\sum_iw_i^{-1/2})^2}
 =\frac{2M^3}{3S_N^2}.
\]
The second inequality is Hölder, with equality over the nonnegative real simplex only for \(\ell_i/M=w_i^{-1/2}/S_N\). Rounding these real numbers to nonnegative integers with total \(M\) introduces a coordinate error bounded by a constant depending on \(N\), and therefore changes the cubic sum by \(O_N(M^2)\). Since every \(m_i=O_N(M)\), the remaining squared terms and the lower-degree terms of \(q\) are also \(O_N(M^2)\). This proves matching upper and lower bounds. On the compact unit simplex, the strictly convex function \(\sum_iw_i p_i^3\) has the stated unique minimizer, and the uniform \(O_N(1/M)\) normalized remainder implies convergence of *every* integer minimizer. The exact mean identity has coefficients \(N-i\), uniquely smallest at \(i=N-1\); that placement has the claimed cubic variance coefficient. This proves the mean–variance conflict.

**Two-tooth finite classification.** For \(N=2\), the exact formula becomes
\[
 V_M(x)=3(1+x)^2+(M+2)^2+2q(x)+q(M-x).
\]
The forward difference is
\[
 V_M(x+1)-V_M(x)=2x^2+(4M+14)x+13-2M^2.
\]
For integers \(M,x\), this difference is odd, hence never zero; it increases strictly with \(x\ge0\). Its real root is \((\sqrt{32M^2+112M+92}-4M-14)/4\), so the first nonnegative integer with positive difference is exactly \(x_*(M)\), proving unique optimality. The initial difference is \(13-2M^2\): it is positive for \(M\le2\) and negative for \(M\ge3\), establishing the sharp finite threshold. Evaluating \(M=3\) yields the displayed numbers.

## Verification

The included `verify.py` independently forms and solves the finite killed-generator linear systems for the first and second absorption-time moments using exact rational arithmetic. It checks the closed formulas for 169 distinct combs with one to four backbone edges and small tooth lengths; all comparisons were exact equalities. It also exhaustively verifies the unique two-tooth minimizer formula for each budget \(0\le M\le40\) and compares the three-tooth optimal allocations with the asymptotic profile at budgets 40, 80 and 160. These finite checks corroborate but do **not** replace the infinite-budget proof above.

## Relationship to prior work

Méndez, Iomin, Campos and Horsthemke (2015, arXiv:1509.01670) treat mesoscopic transport on combs through effective branch waiting-time transforms, concentrating on diffusion scaling and mean waiting times. Rebenshtok and Barkai (2013/2014, arXiv:1402.0171) derive tooth first-passage generating functions for occupation-time statistics. Illien and Bénichou (2016, arXiv:1602.03477) derive propagators and first-passage relations for combs, including homogeneous finite teeth. Earlier general tree first-passage moment methods, notably Bapat (2011), are a foundation for exact moment calculations. The specific statement here is a **fixed-total-tooth-budget optimization of exit-time variance**, its all-budget two-tooth threshold, and the unique inverse-square-root spatial allocation law for arbitrary fixed backbone length. It does not assert priority for the general renewal equations, the one-dimensional tooth moments, or general tree first-passage moment formulae.

## Limitations

The time scale is fixed by unit *edge* rates, which differs from discrete-time neighbor-uniform walks and from fixed total jump-rate conventions. Optimization applies to variance, not a stochastic ordering of full exit-time distributions. At finite budgets the general \(N\)-tooth integer minimizer need not be unique; only its limiting proportions are classified. The expansion's remainder is for fixed \(N\). Full-text access to some general tree hitting-time literature was incomplete, leaving a residual priority risk for independently derived corollaries; the explicit optimization is not known to be asserted there on the inspected evidence. No experimental validation or independent audit is claimed.

## References

1. V. Méndez, A. Iomin, D. Campos, W. Horsthemke, *Mesoscopic description of random walks on combs*, arXiv:1509.01670v1 (first public 2015-09-05); Phys. Rev. E 92, 062112 (2015).
2. A. Rebenshtok, E. Barkai, *Occupation times on a comb with ramified teeth*, arXiv:1402.0171v1 (2014), Phys. Rev. E 88, 052126 (2013).
3. P. Illien, O. Bénichou, *Propagators of random walks on comb lattices of arbitrary dimension*, arXiv:1602.03477 (2016), J. Phys. A: Math. Theor. 49, 265001 (2016).
4. R. B. Bapat, *On the first passage time of a simple random walk on a tree*, Statistics & Probability Letters 81, 1552–1558 (2011), doi:10.1016/j.spl.2011.05.017.
5. S. Sasom, V. Hengpunya, *Random Walks on Quasi-One-Dimensional Lattices*, J. Stat. Phys. 190, 102 (2023), doi:10.1007/s10955-023-03113-7.
