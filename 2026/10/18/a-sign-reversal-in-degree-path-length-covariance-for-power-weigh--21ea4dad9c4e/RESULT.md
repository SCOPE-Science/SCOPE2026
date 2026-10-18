# A sign reversal in degree–path-length covariance for power-weight recursive trees

## Finding

In a power-weight recursive tree, vertex \(j\ge2\) independently chooses its parent \(K_j\in\{1,\ldots,j-1\}\) with probability \(\Pr(K_j=k)=w_k/W_{j-1}\), where \(w_k=k^\alpha\), \(W_j=\sum_{k=1}^jw_k\), and \(\alpha\in\mathbb R\). Let \(D_j\) denote depth from vertex 1, \(T_n=\sum_{j=1}^nD_j\) the total path length, and \(R_{i,n}=\sum_{j=i+1}^n\mathbf1\{K_j=i\}\) the outdegree of vertex \(i\). Write \(p_j=w_j/W_j\) and \(W_\infty=\sum_{j\ge1}w_j\), allowing infinity and interpreting \(1/W_\infty=0\) in that case.

For **every** fixed \(i\ge1\) and real \(\alpha\), the limit exists and equals
\[
\boxed{C_i(\alpha):=\lim_{n\to\infty}\operatorname{Cov}\left(\frac{T_n-\mathbb ET_n}{n},R_{i,n}\right)=w_i\left[\sum_{j=i+1}^{\infty}\frac{w_j(p_j-p_i)}{W_{j-1}W_j}+\frac{1-p_i}{W_\infty}\right].}
\]
The series converges absolutely. This covariance exhibits a strict qualitative change at the summability boundary \(\alpha=-1\):

* For \(\alpha\ge-1\), \(C_i(\alpha)<0\) for every finite \(i\).
* For \(\alpha<-1\), \(C_1(\alpha)<0\), whereas \(C_i(\alpha)>0\) for all sufficiently large \(i\). Thus a genuine sign reversal occurs along vertex labels.

The large-label asymptotics are sharp:
\[
\boxed{C_i(\alpha)\sim\begin{cases}
-\dfrac{(\alpha+1)^2}{\alpha+2}\,i^{-2},&\alpha>-1,\\[4pt]
-\dfrac{1}{i^2(\log i)^2},&\alpha=-1,\\[4pt]
\dfrac{i^\alpha}{\zeta(-\alpha)},&\alpha<-1.
\end{cases}}
\]
In the illustrative linearly weighted model \(\alpha=1\), the complete profile simplifies to
\[
\boxed{C_i(1)=4i\left(\frac{\pi^2}{6}-H_i^{(2)}\right)+\frac2{i+1}-4,\qquad H_i^{(2)}=\sum_{k=1}^i k^{-2},}
\]
so \(C_1(1)=2\pi^2/3-7\), while \(i^2C_i(1)\to-4/3\).

## Assumptions and scope

Only independent parent choices with the precisely specified label-dependent weights are assumed. The statement concerns covariance at a fixed vertex label followed by tree size tending to infinity; large-label asymptotics are applied to this already-defined limiting covariance. There is no claim of uniformity when \(i\) grows simultaneously with \(n\). The normalization of total path length is \(n\); centering changes no covariance. The infinite-weight convention is defined explicitly above.

## Proof

Define \(\mathcal F_j=\sigma(K_2,\ldots,K_j)\) and the martingale difference \(\xi_j=D_j-\mathbb E[D_j\mid\mathcal F_{j-1}]\). The depth mean is \(m_j:=\mathbb ED_j=\sum_{k<j}p_k\), obtained recursively because \(m_j=1+\sum_{k<j}w_km_k/W_{j-1}\). The exact total-path-length innovation representation, also established in the motivating literature, is
\[
T_n-\mathbb ET_n=\sum_{j=2}^n\bigl(1+(n-j)p_j\bigr)\xi_j.
\tag{1}
\]
To verify (1) independently, let \(Y_{j,n}\) be the impact of the parent choice at arrival \(j\) on future expected depth sums. Conditional on \(\mathcal F_j\), the difference from \(\mathcal F_{j-1}\) is a multiple of \(\xi_j\). The propagation coefficient for each later vertex \(k>j\) equals \(p_j\): replacing the depth of vertex \(j\) by one additional unit changes the mean depth of vertex \(k\) by \(w_j/W_{k-1}\) plus its descendants' contributions, satisfying \(u_{k+1}=u_k(1+p_k)\) for the weighted aggregate. Using \(W_k=W_{k-1}(1+p_k/(1-p_k))\) yields total propagated expected effect \((n-j)p_j\). More directly, the conditional expected depth increment at step \(k\) is \(1+\sum_{r<k}w_rD_r/W_{k-1}\); its weighted-depth sum evolves by multiplication with \(W_k/W_{k-1}\), giving contribution \(p_j\) to each later expected increment. The sum therefore gives (1).

For \(j>i\), put \(I_{j,i}=\mathbf1\{K_j=i\}\). Direct conditioning on the parent gives
\[
\operatorname{Cov}(\xi_j,I_{j,i})=\frac{w_i}{W_{j-1}}(1+m_i-m_j)
=\frac{w_i}{W_{j-1}}\left(1-\sum_{k=i}^{j-1}p_k\right).
\tag{2}
\]
For distinct arrival times, all cross-covariances between innovations and parent indicators vanish by the martingale property and independence of future parent variables. Hence, exactly at finite \(n\),
\[
\operatorname{Cov}\left(\frac{T_n-\mathbb ET_n}{n},R_{i,n}\right)
=w_i\sum_{j=i+1}^n\left[p_j+\frac{1-jp_j}{n}\right]\frac{1-\sum_{k=i}^{j-1}p_k}{W_{j-1}}.
\tag{3}
\]
In particular, this identity can be checked without asymptotic reasoning.

Write \(a_j=w_j/(W_{j-1}W_j)=W_{j-1}^{-1}-W_j^{-1}\). The main summand in (3) uses \(p_j/W_{j-1}=a_j\). Since \(a_j\ge0\), \(\sum_{j>i}a_j\le1/W_i\), and \(\sum_{k=i}^{j-1}p_k\) grows at most logarithmically when \(\alpha\ge-1\) (and remains bounded when \(\alpha<-1\)), this main series converges absolutely. Rearrange the double sum using
\[
\sum_{j=k+1}^\infty a_j=\frac1{W_k}-\frac1{W_\infty},\qquad
\frac{p_k}{W_k}=a_k(1-p_k).
\]
The main series becomes
\[
w_i\left[\sum_{j>i}a_j(p_j-p_i)-\frac{\sum_{k=i}^\infty p_k-p_i}{W_\infty}\right],
\]
where the second term is understood by taking finite partial sums first when \(W_\infty=\infty\), in which case it vanishes. For \(\alpha<-1\), the correction term in (3) tends, by Cesàro averaging, to
\[
\frac{w_i}{W_\infty}\left(1-\sum_{k=i}^\infty p_k\right),
\]
because \(jp_j\to0\). When \(\alpha>-1\), the summand \((1-jp_j)(1-\sum_{k=i}^{j-1}p_k)/W_{j-1}\to0\), and at \(\alpha=-1\) it is \(O((\log\log j)/\log j)\to0\). Thus its Cesàro average tends zero. Combining all pieces gives exactly the displayed formula for \(C_i(\alpha)\).

For every fixed real \(\alpha\), \(p_j\) is strictly decreasing in \(j\). If \(\alpha\le0\), observe that \(p_j^{-1}=\sum_{k\le j}(j/k)^{-\alpha}\) strictly increases. If \(\alpha>0\), use the layer-cake identity
\[
\frac1{p_j}=\sum_{k\le j}\left(\frac kj\right)^\alpha
=\alpha\int_0^1t^{\alpha-1}\bigl(j-\lfloor jt\rfloor\bigr)\,dt;
\]
the counting function of the integers \(k\le j\) satisfying \(k/j>t\) increases from \(j\) to \(j+1\) at every \(t\), and strictly on a set of positive measure. Therefore the integral strictly increases.

If \(\alpha\ge-1\), then \(W_\infty=\infty\), so each summand in \(C_i(\alpha)\) is negative. For \(\alpha<-1\), \(p_1=1\) forces \(C_1<0\); as \(i\to\infty\), \(p_i\to0\) and
\[
\left|\sum_{j>i}a_j(p_j-p_i)\right|\le p_i\left(\frac1{W_i}-\frac1{W_\infty}\right)=o(1),
\]
whereas \((1-p_i)/W_\infty\to1/W_\infty>0\). This proves eventual positivity and the third asymptotic.

If \(\alpha>-1\), put \(\beta=\alpha+1\), so \(W_j\sim j^\beta/\beta\), \(p_j\sim\beta/j\), and \(a_j\sim\beta^2j^{-\beta-1}\). A Riemann-sum limit then gives
\[
\lim_{i\to\infty}i^2C_i=\beta^3\int_1^\infty u^{-\beta-1}\left(\frac1u-1\right)du=-\frac{\beta^2}{\beta+1}.
\]
At \(\alpha=-1\), \(W_i=H_i\), \(p_i=1/(iH_i)\), and the exact rearrangement is
\[
C_i=\frac1i\left[-\frac{p_i}{W_i}+\sum_{j>i}a_jp_j\right].
\]
The first term is \(-1/(i^2H_i^2)\) and the remaining term is \(O(i^{-2}(\log i)^{-3})\), proving the stated critical asymptotic. For \(\alpha=1\), \(W_j=j(j+1)/2\), \(p_j=2/(j+1)\); partial fractions and \(\sum_{j>i}j^{-2}=\pi^2/6-H_i^{(2)}\) give the displayed harmonic formula. This completes the proof.

## Verification

The accompanying `verify.py` computes exact finite covariances using two independent methods: exhaustive enumeration of every parent-choice sequence and the martingale formula (3). It checks five integer exponents, tree orders 3 through 7 and every eligible fixed vertex, totaling 100 exact rational identities. It independently checks 99 strict analytic-profile inequalities, four asymptotic trend tolerances, and one exact root constant: 204 deterministic assertions total. These finite computations are corroboration, not a proof of limits for arbitrary real exponents; those are established in the proof.

## Relationship to prior work

Gałązka and Wdowicka's *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations* (arXiv:2610.00614v1, 2026-09-30) studies this same weighted model and supplies the total-path-length martingale framework. Its inspected main theorems address path length and its fluctuations, not the mixed fixed-vertex outdegree covariance or its sign change. Sénizergues' *Geometry of weighted recursive and affine preferential attachment trees* (arXiv:1904.07115) studies degree/profile asymptotics without identifying this mixed cost covariance. Previous work on root attachment versus total path length in **uniform** random recursive trees establishes a negative covariance at \(\alpha=0\), including a stronger stochastic comparison in that special case, but does not imply the \(\alpha<-1\) sign reversal and three-regime formula. The present theorem uses the known martingale expansion but evaluates the previously unreported joint observable.

## Limitations

The statement addresses label-weighted independent parent selections, not preferential attachment to *current degrees* or dependent-parent models. The terminal covariance can change sign only after the stated order of limits, and no uniqueness of the location of the sign change is claimed. The analysis does not yield the complete joint distribution, or a uniform limit as the measured vertex moves with tree size. General joint generating-function or martingale theories not identified in the searched literature may imply some portions; independent priority assessment remains outstanding.

## References

1. M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1, first posted September 30, 2026.
2. L. Sénizergues, *Geometry of weighted recursive and affine preferential attachment trees*, arXiv:1904.07115, 2019/2021.
3. *Root attachments have an exact negative path-length profile in random recursive trees*, public mathematical result, October 4, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-root-attachments-have-an-exact-negative-path-length-profile-in-r--3b3e0426b1ba.
