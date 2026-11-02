# Root-degree/path-length correlation phases in power-weight recursive trees

## Finding

Consider a labelled recursive tree in which every vertex \(j\geq2\) independently chooses a parent \(K_j\in\{1,\ldots,j-1\}\), with
\[
\Pr(K_j=i)=\frac{i^{\alpha}}{W_{j-1}},\qquad
W_k=\sum_{i=1}^k i^{\alpha},\qquad \alpha\in\mathbb R.
\]
Let \(R_n=\sum_{j=2}^n\mathbf1_{\{K_j=1\}}\) be the root's outdegree and \(T_n=\sum_{i=1}^nD_i\) the total path length, with \(D_1=0\) and \(D_j=1+D_{K_j}\). Define
\[
p_j=\frac{j^{\alpha}}{W_j},\quad q_j=\frac1{W_{j-1}}\ (j\ge2),\quad
b_j=\sum_{\ell=2}^{j-1}p_\ell,\quad
\sigma_\alpha^2=\lim_{n\to\infty}\frac{\operatorname{Var}(T_n)}{n^2}>0.
\]
The last positive limit is established for every fixed exponent in Gałązka–Wdowicka (2026).

**Exact covariance.** For every \(n\ge2\) and real \(\alpha\),
\[
\boxed{\operatorname{Cov}(R_n,T_n)
=-\sum_{j=3}^n q_j b_j\bigl[1+(n-j)p_j\bigr].}
\tag{1}
\]
It is strictly negative for \(n\ge3\). Each individual root-attachment indicator also has a strictly negative covariance with \(T_n\) when \(j\ge3\).

**Correlation phase diagram.** Put
\[
 m_\alpha=\sum_{j=3}^\infty q_jp_jb_j+
 \mathbf1_{\{\alpha<-1\}}\frac1{\zeta(-\alpha)}\sum_{\ell=2}^\infty p_\ell
 \in(0,\infty),
\tag{2}
\]
where both series converge. Then
\[
\frac{\operatorname{Cov}(R_n,T_n)}n\longrightarrow-m_\alpha.
\tag{3}
\]
Writing \(V_n=\operatorname{Var}(R_n)\), the exact identity \(V_n=\sum_{j=2}^nq_j(1-q_j)\) gives
\[
 V_n=\begin{cases}
 v_\alpha+o(1),\quad v_\alpha:=\sum_{j=2}^\infty q_j(1-q_j)\in(0,\infty),&\alpha>0,\\
 (1+o(1))\log n,&\alpha=0,\\
 (1+o(1))\frac{\alpha+1}{-\alpha}n^{-\alpha},&-1<\alpha<0,\\
 (1+o(1))n/\log n,&\alpha=-1,\\
 (1+o(1))q_\infty(1-q_\infty)n,&\alpha<-1,
\end{cases}
\quad q_\infty=\frac1{\zeta(-\alpha)}.
\tag{4}
\]
Consequently \(\operatorname{Corr}(R_n,T_n)\) tends to a **strictly negative constant** exactly for \(\alpha>0\):
\[
\boxed{\lim_{n\to\infty}\operatorname{Corr}(R_n,T_n)
=-\frac{m_\alpha}{\sigma_\alpha\sqrt{v_\alpha}},\qquad\alpha>0.}
\tag{5}
\]
For \(\alpha=0\) it is of negative order \((\log n)^{-1/2}\); for \(-1<\alpha<0\), of negative order \(n^{\alpha/2}\); for \(\alpha=-1\), of negative order \(\sqrt{\log n/n}\); and for \(\alpha<-1\), of negative order \(n^{-1/2}\). In particular the continuous-to-zero correlation transition lies at **uniform attachment**, rather than the \(\alpha=-1\) transition in the mean-depth scale.

**Critical window and onset.** Allow the exponent to change with the tree size: for any real sequence \(\alpha_n\) with \(\alpha_n\log n\to\lambda\in\mathbb R\), construct the \(n\)-vertex tree using the *same* exponent \(\alpha_n\) at all its attachments. Set
\[
 F(\lambda)=\int_0^1e^{-\lambda s}\,ds
 =\begin{cases}(1-e^{-\lambda})/\lambda,&\lambda\ne0,\\1,&\lambda=0.\end{cases}
\]
Then
\[
\boxed{\begin{aligned}
\frac{V_n}{\log n}&\longrightarrow F(\lambda),\\
\frac{\operatorname{Cov}(R_n,T_n)}n&\longrightarrow-(\zeta(2)-1),\\
\frac{\operatorname{Var}(T_n)}{n^2}&\longrightarrow2-\zeta(2),\\
\sqrt{\log n}\operatorname{Corr}(R_n,T_n)
&\longrightarrow-\frac{\zeta(2)-1}{\sqrt{2-\zeta(2)}\sqrt{F(\lambda)}}.
\end{aligned}}
\tag{6}
\]
Moreover, as positive fixed exponents approach zero, the limiting negative correlation is born at a square-root rate:
\[
\boxed{\lim_{\alpha\downarrow0}\frac{1}{\sqrt\alpha}
\left(\lim_{n\to\infty}\operatorname{Corr}(R_n,T_n)\right)
=-\frac{\zeta(2)-1}{\sqrt{2-\zeta(2)}}.}
\tag{7}
\]
At the exact linear-weight point \(\alpha=1\), all constants simplify:
\[
 m_1=7-\frac{2\pi^2}{3},\quad
 v_1=14-\frac{4\pi^2}{3},\quad
 \sigma_1^2=8-\frac{2\pi^2}{3},\quad
 \lim_{n\to\infty}\operatorname{Corr}(R_n,T_n)
=-\sqrt{\frac{7-2\pi^2/3}{2(8-2\pi^2/3)}}
\approx-0.3846462124.
\tag{8}
\]

## Assumptions and scope

The parent choices are mutually independent and their probabilities depend on their labels, not on previously realized degrees. Distances are measured in edges from root vertex \(1\). The exact formula (1) and fixed-exponent results hold for every real \(\alpha\); the critical-window assertions (6) require \(\alpha_n\log n\) to converge to a *finite real number*. In each triangular row all weights are computed from the same value \(\alpha_n\). Correlation is defined for \(n\ge3\), when both statistics have positive variance. The classical constant \(\sigma_\alpha\) refers to the same power-weight model, not to binary-search-tree path length.

## Proof

**1. Local covariance and the finite identity.** Let \(\mathcal F_j\) be the parent-choice history through time \(j\), and define the weighted depth sum \(A_j=\sum_{i=1}^j i^\alpha D_i\). The attachment innovation
\[
\xi_j=D_{K_j}-\frac{A_{j-1}}{W_{j-1}}
\]
is a square-integrable martingale difference. The exact total-path-length decomposition from Gałązka–Wdowicka reads
\[
T_n-\mathbb ET_n=\sum_{j=2}^n\bigl[1+(n-j)p_j\bigr]\xi_j.
\tag{9}
\]
For \(I_j=\mathbf1_{\{K_j=1\}}\), independent parent choices and the martingale-difference property imply \(\operatorname{Cov}(I_j,\xi_k)=0\) when \(k\ne j\). For \(k<j\) this uses conditioning on \(\mathcal F_{j-1}\); for \(k>j\) it uses conditioning on \(\mathcal F_{k-1}\). At \(k=j\), since \(D_1=0\),
\[
\mathbb E(I_j\xi_j)=-q_j\,\mathbb E\frac{A_{j-1}}{W_{j-1}}
=-q_j\sum_{\ell=2}^{j-1}p_\ell=-q_jb_j.
\tag{10}
\]
The middle identity follows from the elementary depth-marginal formula \(\mathbb ED_i=\sum_{\ell=1}^{i-1}p_\ell\): weighting by \(i^\alpha/W_{j-1}\) and exchanging sums gives \(\sum_{\ell=2}^{j-1}p_\ell\). Note that \(\xi_2=0\). Summing the orthogonal-time covariances proves (1). Positivity of \(q_j,p_j,b_j\) gives the strict sign. The root indicators \(I_j\) are independent Bernoulli variables of parameters \(q_j\), proving the exact root-degree variance identity.

For additional structural intuition, force one vertex \(j\) to attach either to the root or to a weighted nonroot parent, coupling all other parent choices. The descendants of \(j\) are unchanged and their depths increase strictly in the latter tree. The expected final descendant count is \(1+(n-j)p_j\), providing a direct pathwise explanation of the multiplier in (1); the weighted descendant mass has conditional expectation \(j^\alpha W_t/W_j\) at time \(t\ge j\).

**2. The fixed-exponent covariance coefficient.** Rewrite the positive quantity on the right of (1), divided by \(n\), as
\[
\sum_{j=3}^n q_jp_jb_j+
\frac1n\sum_{j=3}^nq_jb_j(1-jp_j).
\tag{11}
\]
For \(\alpha>-1\), standard integral estimates give \(p_j\sim(1+\alpha)/j\), \(q_j\asymp j^{-1-\alpha}\), and \(b_j=O(\log j)\). For \(\alpha=-1\), \(p_j=1/(jH_j)\), \(q_j=1/H_{j-1}\), \(b_j=O(\log\log(j+1))\). For \(\alpha<-1\), \(p_j=O(j^\alpha)\), \(q_j\to q_\infty\), and \(b_j\to\sum_{\ell=2}^\infty p_\ell\). In each case \(\sum_{j=3}^\infty q_jp_jb_j<\infty\). Also \(jp_j\) is bounded for every fixed exponent. Therefore the Cesàro term in (11) vanishes for \(\alpha\ge-1\), because \(q_jb_j\to0\); for \(\alpha<-1\) its limit is \(q_\infty\sum_{\ell=2}^\infty p_\ell\). This proves (2)--(3) with strictly positive coefficient.

**3. Root-degree variance and correlation.** The integral estimate \(W_j\sim j^{1+\alpha}/(1+\alpha)\) for \(\alpha>-1\) gives \(q_j\sim(1+\alpha)j^{-1-\alpha}\). Summation yields finite variance for \(\alpha>0\), logarithmic growth for \(\alpha=0\), and \((1+\alpha)n^{-\alpha}/(-\alpha)\) for \(-1<\alpha<0\). At \(\alpha=-1\), \(q_j=1/H_{j-1}\), so \(V_n\sim n/\log n\). Below \(-1\), \(q_j\to q_\infty\in(0,1)\), yielding \(V_n\sim q_\infty(1-q_\infty)n\). The cited path-length theorem yields \(\operatorname{Var}(T_n)/n^2\to\sigma_\alpha^2>0\); division of (3) by the standard deviations proves all rates and (5).

**4. Uniform critical-window control.** For \(|\alpha|\le1/2\), integral comparison of the power sum, uniformly in \(\alpha\), gives constants independent of \(j,\alpha\) such that
\[
p_j\le\frac Cj,\qquad
q_j\le Cj^{-1-\alpha},\qquad
q_jp_jb_j\le C\frac{\log(j+1)}{j^{3/2}}.
\tag{12}
\]
For fixed \(j\) the terms are continuous in \(\alpha\), so dominated convergence yields
\(\sum_{j\ge3}q_jp_jb_j\to \zeta(2)-1\) as \(\alpha\to0\). The remaining Cesàro term in (11) vanishes uniformly when \(\alpha\to0\): the bound \(q_jb_j\le Cj^{-1/2}\log(j+1)\) gives \(n^{-1}\sum_{j\le n}q_jb_j=O(n^{-1/2}\log n)\), and \(jp_j\le C\). Hence the covariance limit in (6).

The same uniform power-sum bound improves to
\[
q_j=(1+\alpha)j^{-1-\alpha}\bigl(1+O(j^{-1/2})\bigr)
\quad (|\alpha|\le1/2),
\tag{13}
\]
with a uniform remainder. For \(\alpha_n\log n\to\lambda\), taking logarithmically spaced Riemann sums,
\[
\frac1{\log n}\sum_{j=2}^nq_j
=\frac{1+o(1)}{\log n}\sum_{j=2}^n\frac{e^{-\alpha_n\log j}}j
\longrightarrow\int_0^1e^{-\lambda s}\,ds.
\]
The sums of \(q_j^2\) are uniformly bounded for sufficiently large \(n\), proving the first limit in (6).

For the path-length variance, the exact orthogonal-innovation formula is
\[
\frac{\operatorname{Var}(T_n)}{n^2}
=\sum_{j=2}^n\left[p_j+\frac{1-jp_j}{n}\right]^2 v_j,
\qquad v_j=\mathbb E\xi_j^2.
\tag{14}
\]
The innovation-variance recurrence \(v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j)\), \(v_2=0\), implies \(v_j\le C\log(j+1)\) uniformly for \(|\alpha|\le1/2\). Since \(p_j\le C/j\) and \(|1-jp_j|\le C\), the infinite series \(\sum_{j\ge2}p_j^2v_j\) is dominated by \(C\sum_{j\ge2}\log(j+1)/j^2\), independently of \(\alpha\). In (14), the tail beyond \(n\) and all finite-size corrections tend to zero uniformly, the latter bounded by \(O(\log(n+1)/n)\). By fixed-index continuity of \(p_j,v_j\) at \(\alpha=0\), the limit is the known uniform value \(2-\zeta(2)\). This proves the third and fourth limits in (6).

**5. Emergence from the positive phase.** Uniform domination in (12) implies \(m_\alpha\to m_0=\zeta(2)-1\) as \(\alpha\downarrow0\). The argument for (14) gives \(\sigma_\alpha^2\to 2-\zeta(2)\). Moreover \(q_j\sim(1+\alpha)j^{-1-\alpha}\) and uniformly summable \(q_j^2\) imply \(\alpha v_\alpha\to1\) as \(\alpha\downarrow0\). Substitute these limits into (5) to obtain (7).

**6. Linear weights.** At \(\alpha=1\), \(q_j=2/[j(j-1)]\), \(p_j=2/(j+1)\), and \(b_j=2\sum_{k=3}^j1/k\). Exchanging absolutely convergent sums gives
\[
m_1=8\sum_{k=3}^\infty\frac1k\sum_{j=k}^\infty\frac1{(j-1)j(j+1)}
=4\sum_{k=3}^\infty\frac1{k^2(k-1)}=7-4\zeta(2).
\]
Likewise \(v_1=\sum_{j\ge2}2/[j(j-1)]-4\sum_{j\ge2}1/[j^2(j-1)^2]=14-8\zeta(2)=2m_1\). The source's evaluation \(\sigma_1^2=8-4\zeta(2)\) completes (8).

## Verification

The standalone Python program `verify.py` exhaustively enumerates all labelled parent-choice sequences through order \(8\) for each of the rational power exponents \(-2,-1,0,1,2\). It compares exact rational moments against (1), the independent-Bernoulli root-degree variance and the innovation-based total-path-length variance, also confirming that the enumerated probability sums are one. It performs two further deterministic finite-size numerical checks of the coefficients in (8). The program reports 177 passed assertions across 35 exact finite models and two numerical checks. The analytical arguments above, not the finite enumerations or convergence experiments, establish the infinite and triangular asymptotics.

Run with `python verify.py` using Python's standard library. Numerical convergence checks use an absolute error tolerance of \(10^{-5}\); they are not interval certificates for the infinite limit.

## Relationship to prior work

Gałązka and Wdowicka (2026) prove the path-length innovation decomposition, the fixed-exponent path-length variance limit for all real power exponents, and the linear-weight coefficient. Their full paper's scope and statement do not include root outdegree, its covariance with total path length, a change of correlation phase at uniform attachment, or a triangular critical window. Those source results are taken as prior inputs, not represented as new. Lyon and Mahmoud (2020) analyze outdegrees, leaves and insertion depth for linear-weight attachment; their published article's sections do not state the joint root-degree/total-path-length covariance. The classical uniform recursive-tree analysis of Dobrow and Fill (1999) concerns path length and its limit.

A previously published result for **uniform** recursive trees gives the exact negative root-attachment/path-length covariance, its stochastic-order coupling and a vanishing logarithmic correlation. Its \(\alpha=0\) claim is deliberately treated here as prior; the present contribution is the all-exponent phase diagram, the persistent-correlation formula, the explicit linear-weight constant and the \(\alpha\log n\) critical crossover. Separately, a prior finite-horizon optimization of newest-vertex conditional depth variance under arbitrary weights concerns an entirely different statistic and does not imply the joint covariance phase transition. These comparisons do not prove exhaustive historical priority.

## Limitations

The results assume independent parent choices with positive deterministic *label* weights and make no claim for degree-dependent preferential attachment. The critical-window theorem requires a finite \(\lambda\) and says nothing about exponents approaching zero with an unbounded product \(\alpha_n\log n\). The exact covariance is elementary given the already-published martingale representation; its significance here is as the input to the quantitative correlation phase diagram, not as an independently large theorem. Previously published weighted-tree joint-statistic methods could conceivably contain implicit corollaries; no comprehensive historical uniqueness assertion or independent audit is made.

## References

1. M. Gałązka and H. Wdowicka, “Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations,” arXiv:2610.00614v1, first posted 2026-09-30. https://arxiv.org/html/2610.00614v1
2. M. R. Lyon and H. M. Mahmoud, “Trees grown under young-age preferential attachment,” *Journal of Applied Probability* 57 (2020), 911–927. https://doi.org/10.1017/jpr.2020.49
3. M. Lyon and H. M. Mahmoud, “Insertion depth in power-weight trees,” *Information Processing Letters* 176 (2022), 106227. https://doi.org/10.1016/j.ipl.2021.106227
4. R. P. Dobrow and J. A. Fill, “Total path length for random recursive trees,” *Combinatorics, Probability and Computing* 8 (1999), 317–333. https://doi.org/10.1017/S0963548399003855
5. “Root attachments have an exact negative path-length profile in random recursive trees,” published mathematical research note (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-root-attachments-have-an-exact-negative-path-length-profile-in-r--3b3e0426b1ba
