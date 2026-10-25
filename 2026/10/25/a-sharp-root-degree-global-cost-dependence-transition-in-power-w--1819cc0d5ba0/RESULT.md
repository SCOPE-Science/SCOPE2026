# A sharp root-degree/global-cost dependence transition in power-weight recursive trees

## Finding
Consider the random recursive tree on labels \(1,\ldots,n\), where each vertex \(j\ge 2\) independently chooses its parent \(K_j<j\) with probability proportional to the deterministic positive weight \(w_i=i^{\alpha}\) of candidate parent \(i\), with fixed \(\alpha\in\mathbb R\). Let \(T_n=\sum_{j=1}^n D_j\) be total root-to-vertex depth and \(R_n=\sum_{j=2}^n\mathbf1_{\{K_j=1\}}\) be root outdegree. The known path-length limit \(L_\alpha=\lim_{n\to\infty}(T_n-\mathbb ET_n)/n\) exists in \(L^2\).

There is a **sharp joint-law transition at \(\alpha=0\)**:

* If \(\alpha\le 0\), writing \(s_n^2=\operatorname{Var}(R_n)\), one has \(s_n\to\infty\) and
\[
\left(\frac{T_n-\mathbb ET_n}{n},\frac{R_n-\mathbb ER_n}{s_n}\right)
\Longrightarrow (L_\alpha,G),
\]
where \(G\) is standard normal and **independent** of \(L_\alpha\).
* If \(\alpha>0\), then \(R_n\to R_\infty\) almost surely and in \(L^2\), the pair converges in \(L^2\) to \((L_\alpha,R_\infty)\), and \(\operatorname{Cov}(L_\alpha,R_\infty)=-C_\alpha<0\). Therefore its limiting coordinates are **not independent**.

The negative covariance is exactly computable at every finite size. For \(W_j=\sum_{i=1}^ji^\alpha\), put \(p_j=j^\alpha/W_j\), \(q_j=1/W_{j-1}\) (\(j\ge2\)), and \(b_j=\sum_{i=2}^{j-1}p_i\) (empty sum zero). Then for \(n\ge2\),
\[
\operatorname{Cov}(T_n,R_n)=-\sum_{j=2}^nq_j[1+(n-j)p_j]b_j.
\]
In particular this covariance is strictly negative for every \(n\ge3\), and \(\operatorname{Cov}(T_n,R_n)/n\to-C_\alpha<0\), where the convergent explicit constant is
\[
C_\alpha=\sum_{j=2}^\infty q_jp_jb_j+
\mathbf1_{\{\alpha<-1\}}\frac{1}{\zeta(-\alpha)}\sum_{i=2}^\infty p_i.
\]
For linear weights \(\alpha=1\), the new joint calculation simplifies to
\[
\operatorname{Cov}(L_1,R_\infty)=-\left(7-\frac{2\pi^2}{3}\right),\qquad
\operatorname{Var}(R_\infty)=14-\frac{4\pi^2}{3},
\]
so the population linear-regression coefficient of \(L_1\) on \(R_\infty\) is exactly \(-1/2\).

## Assumptions and scope
Parent choices at distinct arrival times are independent; each vertex has exactly one parent except root \(1\). The parameter \(\alpha\) is fixed (not allowed to depend on \(n\)). The root outdegree counts children, not the graph-theoretic degree of an unrooted abstract tree, although these coincide for the root. The limit \(L_\alpha\) is the univariate centered path-length martingale limit, whose existence and nondegeneracy follow from Gałązka–Wdowicka (2026), Theorem 6.2, since \(p_j=O(1/j)\) for all fixed \(\alpha\). Independence in the first assertion concerns the **limiting variables**, not finite-size independence. The covariance formula is valid more generally for any positive deterministic label weights, with the corresponding \(p_j,q_j,b_j\).

## Proof
**1. Exact cross-covariance.** Let \(\mathcal F_j=\sigma(K_2,\ldots,K_j)\), \(A_j=\sum_{i\le j}w_iD_i\), and \(\xi_j=D_j-1-A_{j-1}/W_{j-1}\). The published exact martingale-innovation representation (Gałązka–Wdowicka, Theorem 5.2) gives
\[
T_n-\mathbb ET_n=\sum_{j=2}^n[1+(n-j)p_j]\xi_j.
\]
Let \(I_j=\mathbf1_{\{K_j=1\}}\). For \(k<j\), \(\mathbb E(\xi_jI_k)=0\) because \(I_k\) is \(\mathcal F_{j-1}\)-measurable and \(\mathbb E(\xi_j\mid\mathcal F_{j-1})=0\). For \(k>j\), \(I_k\) is independent of \(\mathcal F_j\) and \(\mathbb E\xi_j=0\), so again the covariance is zero. Finally, \(I_j=1\) forces \(D_j=1\), whence
\[
\mathbb E(\xi_jI_j)=q_j\left(1-\mathbb ED_j\right)
=-q_jb_j.
\]
The last identity uses the standard depth-mean formula \(\mathbb ED_j=1+\sum_{i=2}^{j-1}p_i\). Summation gives the finite-size identity. For \(j=3\), \(q_jp_jb_j>0\), which makes the covariance strictly negative for \(n\ge3\).

**2. Linear asymptotic covariance.** Rearranging the exact identity yields
\[
-\frac{\operatorname{Cov}(T_n,R_n)}{n}=
\frac1n\sum_{j=2}^nq_jb_j
+\sum_{j=2}^n(1-j/n)q_jp_jb_j.
\]
For \(\alpha>-1\), the estimates \(q_j=O(j^{-\alpha-1})\), \(p_j=O(j^{-1})\), and \(b_j=O(\log j)\) make \(q_jp_jb_j\) summable, while \(q_jb_j\to0\). At \(\alpha=-1\), \(q_j=O(1/\log j)\), \(p_j=O(1/(j\log j))\), and \(b_j=O(\log\log j)\) give the same two conclusions. For \(\alpha<-1\), the summability of \(p_j\), the convergence \(q_j\to1/\zeta(-\alpha)\), and boundedness of \(b_j\) imply summability of \(q_jp_jb_j\) and \(q_jb_j\to\zeta(-\alpha)^{-1}\sum_{i\ge2}p_i\). Cesàro convergence for the first term and dominated convergence for the second establish the stated \(C_\alpha\). It is positive because the summand at \(j=3\) is positive.

**3. Root-degree limit and independence.** The variables \(I_j\) are mutually independent Bernoulli variables with probabilities \(q_j\), so \(s_n^2=\sum_{j=2}^nq_j(1-q_j)\). If \(\alpha>0\), then \(\sum_jq_j<\infty\), hence \(R_n\to R_\infty\) in \(L^2\) and almost surely by the Bernoulli-sum convergence theorem. The \(L^2\) convergence of centered \(T_n/n\) and the covariance limit above give \(\operatorname{Cov}(L_\alpha,R_\infty)=-C_\alpha\ne0\). If \(\alpha\le0\), then \(s_n^2\to\infty\): \(q_j\sim (1+\alpha)j^{-1-\alpha}\) for \(-1<\alpha\le0\) (at zero this gives \(1/j\)); \(q_j\sim1/\log j\) at \(\alpha=-1\); and \(q_j\to1/\zeta(-\alpha)\in(0,1)\) below \(-1\). Since all Bernoulli summands are bounded, Lindeberg's theorem implies \((R_n-\mathbb ER_n)/s_n\Rightarrow G\). To prove **joint** independence, fix \(m\). The contribution to this normalized sum from \(j\le m\) tends to zero; its remaining summands are independent of \(\mathcal F_m\), and their normalized sum has the same standard-normal limit. Hence the Gaussian limit is independent of every bounded \(\mathcal F_m\)-measurable variable. Approximate any bounded function of \(L_\alpha\), which is measurable with respect to \(\sigma(\bigcup_m\mathcal F_m)\), by its conditional expectation given \(\mathcal F_m\), first letting \(n\to\infty\) and then \(m\to\infty\). This proves the independent joint limit. Slutsky's theorem replaces \(L_\alpha\) by its \(L^2\)-convergent centered-path-length approximants.

**4. Linear-weight constant.** For \(\alpha=1\), \(p_j=2/(j+1)\), \(q_j=2/[j(j-1)]\), and \(b_j=2\sum_{i=2}^{j-1}(i+1)^{-1}\). Absolute convergence allows swapping sums and using \(\sum_{j=i+1}^\infty1/[j(j-1)(j+1)]=1/[2i(i+1)]\), yielding
\[
C_1=4\sum_{i=2}^\infty\frac1{i(i+1)^2}
=7-4\zeta(2)=7-\frac{2\pi^2}{3}.
\]
Likewise \(\mathbb ER_\infty=\sum_{j\ge2}2/[j(j-1)]=2\), and \(\operatorname{Var}(R_\infty)=2-4\sum_{j\ge2}[j(j-1)]^{-2}=14-8\zeta(2)=14-4\pi^2/3\). The covariance-to-variance ratio is \(-1/2\).

## Verification
The accompanying `verify.py` enumerates all weighted independent parent configurations and computes their probabilities as rational numbers for \(n=2,\ldots,7\) and \(\alpha\in\{-2,-1,0,1,2\}\). Its independently evaluated covariance agrees exactly with the derived closed sum. Additional exact-rational series and root-degree identities give 259 checks in total. Execute `python3 verify.py` with the Python standard library. The recorded output is `verification_output.txt`. The mathematical proof is infinite and analytic; finite enumeration alone does not establish it.

## Relationship to prior work
Gałązka–Wdowicka, arXiv:2610.00614v1 (first posted 2026-09-30), proves the univariate martingale limit and the innovation identity used as inputs, but does not determine the joint path-length/root-degree limit or the sharp \(\alpha=0\) dependence transition. Lyon–Mahmoud (2020) obtains outdegree and insertion-depth marginal results in the linear-weight model, not their joint law with total path length. Sénizergues (2019/2021) studies weighted-tree degree and profile limits and provides powerful background, without an identified statement of the present cross-covariance or independence transition. A separately published uniform-recursive-tree result already establishes the **\(\alpha=0\) finite covariance**; that special case is *not* claimed as new. The present contribution is the all-power joint dependence classification, including a nonzero finite-degree limiting covariance and its explicit linear-weight regression constant.

## Limitations
The assertion is for deterministic power weights and the specified independent-parent model, not general degree-reinforced preferential attachment. It gives joint convergence at the stated two-dimensional marginal level, not a functional process-level theorem, a conditional distribution formula, or an independence rate. The exact covariance identity for general deterministic weights is supporting machinery, not a claim that all such weights exhibit the power-law transition. Bibliographic priority remains subject to possible stronger historical results on joint degree/profile martingales; the main original paper and closest model papers were checked, but literature searches cannot establish uniqueness.

## References
1. M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1, first posted 2026-09-30, https://arxiv.org/html/2610.00614v1.
2. M. R. Lyon and H. M. Mahmoud, *Trees Grown Under Young-Age Preferential Attachment*, Journal of Applied Probability 57 (2020), 911–927, https://doi.org/10.1017/jpr.2020.49.
3. D. Sénizergues, *Geometry of Weighted Recursive and Affine Preferential Attachment Trees*, arXiv:1904.07115, https://arxiv.org/abs/1904.07115.
4. *Root attachments have an exact negative path-length profile in random recursive trees*, published research finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-root-attachments-have-an-exact-negative-path-length-profile-in-r--3b3e0426b1ba (uniform-weight result; available summary inspected).
