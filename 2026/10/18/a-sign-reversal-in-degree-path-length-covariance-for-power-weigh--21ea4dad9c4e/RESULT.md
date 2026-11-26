# A sign reversal in degree–path-length covariance for power-weight recursive trees

## Finding

In a power-weight recursive tree, vertex \(j\ge2\) independently chooses its parent \(K_j\in\{1,\ldots,j-1\}\) with probability \(w_k/W_{j-1}\), where \(w_k=k^\alpha\), \(W_j=\sum_{k=1}^j w_k\), and \(\alpha\in\mathbb R\). Let \(D_j\) be the depth of vertex \(j\) from vertex 1, \(T_n=\sum_{j=1}^nD_j\) the total path length, and \(R_{i,n}=\sum_{j=i+1}^n\mathbf 1\{K_j=i\}\) the outdegree of vertex \(i\). Define \(p_j=w_j/W_j\), \(a_j=W_{j-1}^{-1}-W_j^{-1}\) for \(j\ge2\), and \(W_\infty=\sum_{j\ge1}w_j\), with \(1/W_\infty=0\) when this sum diverges.

For every fixed \(i\ge1\) and \(\alpha\in\mathbb R\), the limit exists and is
\[
C_i(\alpha):=\lim_{n\to\infty}\operatorname{Cov}\left(\frac{T_n-\mathbb ET_n}{n},R_{i,n}\right)
=w_i\left[\sum_{j>i}a_j(p_j-p_i)+\frac{1-p_i}{W_\infty}\right].
\]
The series is absolutely convergent. For \(\alpha\ge-1\) every \(C_i(\alpha)<0\). For \(\alpha<-1\), \(C_1(\alpha)<0\) but \(C_i(\alpha)>0\) for all sufficiently large \(i\). The large-label equivalents are
\[
C_i(\alpha)\sim\begin{cases}
-\dfrac{(\alpha+1)^2}{\alpha+2}\,i^{-2}, & \alpha>-1,\\[4pt]
-\dfrac1{i^2(\log i)^2},& \alpha=-1,\\[4pt]
\dfrac{i^\alpha}{\zeta(-\alpha)}, &\alpha<-1.
\end{cases}
\]
In particular, with \(H_i^{(2)}=\sum_{k=1}^ik^{-2}\),
\[
C_i(1)=4i\left(\frac{\pi^2}6-H_i^{(2)}\right)+\frac2{i+1}-4.
\]
Thus \(C_1(1)=2\pi^2/3-7\) and \(i^2C_i(1)\to-4/3\).

## Assumptions and scope

The weights are label-dependent and the parent choices are independent. The covariance limit takes \(n\to\infty\) with \(i\) fixed; the large-label equivalents concern this already-defined limiting profile, not sequences \(i=i(n)\). Centering does not change covariance.

## Proof

Let \(\mathcal F_j=\sigma(K_2,\ldots,K_j)\), and put \(A_j=\sum_{r\le j}w_rD_r/W_j\). Conditional on \(\mathcal F_{j-1}\), the mean depth of vertex \(j\) is \(1+A_{j-1}\). Consequently the depth innovation \(\xi_j=D_j-1-A_{j-1}\) is a martingale difference, and the identity
\[
A_j=(1-p_j)A_{j-1}+p_j D_j=A_{j-1}+p_j(1+\xi_j)
\]
with \(A_1=0\) gives \(\mathbb E D_j=\sum_{k<j}p_k\) (here \(p_1=1\)) and
\[
T_n-\mathbb ET_n=\sum_{j=2}^n[1+(n-j)p_j]\xi_j. \tag{1}
\]
The coefficient in (1) comprises the arrival's own innovation and \(p_j\xi_j\) in each subsequent expected depth. For \(j>i\) and \(I_{j,i}=\mathbf 1\{K_j=i\}\), conditioning on \(\mathcal F_{j-1}\) gives
\[
\operatorname{Cov}(\xi_j,I_{j,i})=\frac{w_i}{W_{j-1}}(1+\mathbb ED_i-\mathbb ED_j)=\frac{w_i}{W_{j-1}}B_j,
\qquad B_j=1-\sum_{k=i}^{j-1}p_k.
\]
Cross terms vanish: earlier indicators are measurable before the innovation, and later choices are independent of it. Dividing (1) by \(n\) now gives the finite covariance divided by \(w_i\) as
\[
\sum_{j=i+1}^n a_j B_j+\frac1n\sum_{j=i+1}^n (1-jp_j)\frac{B_j}{W_{j-1}}. \tag{2}
\]

To track the endpoint term, use the finite identity \(\sum_{j=k+1}^n a_j=1/W_k-1/W_n\). Interchanging only finite sums in the first term of (2) gives
\[
\begin{aligned}
\sum_{j=i+1}^n a_j B_j
&=(1-p_i)(1/W_i-1/W_n)-\sum_{k=i+1}^n p_k(1/W_k-1/W_n)\\
&=\sum_{j=i+1}^n a_j(p_j-p_i)+\frac{\sum_{k=i+1}^n p_k}{W_n}, \tag{3}
\end{aligned}
\]
where \(p_k/W_k=a_k(1-p_k)\). The sign of the endpoint term in (3) is positive. Since \(\sum_{j>i}a_j\le1/W_i\) and \(0<p_j\le1\), the displayed difference series converges absolutely.

If \(\alpha>-1\), write \(\beta=\alpha+1\). Then \(W_j\sim j^\beta/\beta\), \(p_j\sim\beta/j\), and \(B_j=O(1+\log j)\) at fixed \(i\). If \(\alpha=-1\), \(W_j=H_j\sim\log j\), \(p_j=1/(jH_j)\), and \(B_j=O(1+\log\log j)\). In each case the endpoint term in (3) tends to zero and the summand in the Cesàro term of (2) tends to zero, so its average also tends to zero. If \(\alpha<-1\), \(p_j=O(j^\alpha)\), so \(jp_j\to0\) and \(B_j\to 1-\sum_{k=i}^\infty p_k\). The Cesàro term tends to \((1-\sum_{k=i}^\infty p_k)/W_\infty\); adding the endpoint term of (3) gives \((1-p_i)/W_\infty\). This yields the asserted limit in all cases.

For \(\alpha\le0\), \(p_j^{-1}=\sum_{k\le j}(k/j)^\alpha\) strictly increases since each old summand is nondecreasing and there is a new positive summand. For \(\alpha>0\),
\[
p_j^{-1}=\alpha\int_0^1 t^{\alpha-1}(j-\lfloor jt\rfloor)\,dt.
\]
The count \(j-\lfloor jt\rfloor\) is nondecreasing in \(j\) since \(\lfloor(j+1)t\rfloor-\lfloor jt\rfloor\le1\) for \(0\le t\le1\); it increases strictly on an interval of positive length near zero. Thus \(p_j\) is strictly decreasing for all real \(\alpha\), and every term of the difference series is negative. This proves the negative sign for \(\alpha\ge-1\) and for the root for all \(\alpha\). For \(\alpha<-1\), the series is bounded in absolute value by \(p_i(1/W_i-1/W_\infty)=o(1)\), while the endpoint term tends to \(1/W_\infty>0\). This proves eventual positivity and the third equivalent since \(W_\infty=\zeta(-\alpha)\). For example at \(\alpha=-2,i=2\), \(p_i=1/5\), \(W_i=5/4\), and \(W_\infty\le2\) by integral comparison: the bracket in the limit is at least \(-p_i/W_i+(1-p_i)/2=6/25>0\).

For \(\alpha>-1\), \(a_j\sim\beta^2j^{-\beta-1}\), so
\[
\sum_{j>i}a_jp_j\sim \frac{\beta^3}{\beta+1}\,i^{-\beta-1},\qquad
p_i\sum_{j>i}a_j=\frac{p_i}{W_i}\sim\beta^2i^{-\beta-1}.
\]
Subtracting the unequal leading coefficients and multiplying by \(w_i=i^{\beta-1}\) proves the first equivalent. At \(\alpha=-1\), \(a_jp_j=O(j^{-2}(\log j)^{-3})\), hence \(w_i\sum_{j>i}a_j p_j=O(i^{-2}(\log i)^{-3})\). The leading term \(-w_i p_i/W_i=-1/(i^2H_i^2)\) gives the second equivalent. Finally for \(\alpha=1\), \(a_jp_j=8/[j(j-1)(j+1)^2]=2/(j-1)-8/j+6/(j+1)+4/(j+1)^2\). Summing and subtracting \(p_i/W_i\), then multiplying by \(i\), gives the stated harmonic expression.

## Verification

The finite identities (2)–(3) are exactly reproducible with `python3 verify_limit.py`: 90 comparisons with direct enumeration of independent parent choices for \(n=2,\ldots,6\) and \(\alpha\in\{-3,-2,-1,0,1,2\}\), testing (3) separately. The calculation also checks the exact rational constants of the explicit sign-reversal example. The general signed limit, asymptotics and other conclusions are analytical, not consequences of the finite check. The original `verify.py` tests the finite covariance and some consequences of the linear-weight special case, but does not test the boundary step (3).

## Relationship to prior work

The path-length innovation structure is a starting point, not the new claim: Gałązka and Wdowicka give (1) in Theorem 5.2, Eq. (26). Sénizergues studies geometry and degree/profile asymptotics for broader weighted recursive-tree models. The exact negative root-attachment covariance in uniform recursive trees [3] covers the special case \((\alpha,i)=(0,1)\), not the profile over nonroot labels. The fixed-label mixed covariance evaluated here includes the surviving endpoint correction when the total weight is finite. That term, not a change in the sign of the difference series, produces the sign reversal for summable power weights.

## Limitations

This is not a model with attachment probabilities depending on current degrees. No simultaneous growing-label limit, unique sign-change location or joint distribution is asserted. Literature comparisons concern the inspected results, not exhaustive historical priority.

## References

1. M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1.
2. L. Sénizergues, *Geometry of weighted recursive and affine preferential attachment trees*, arXiv:1904.07115.
3. *Root attachments have an exact negative path-length profile in random recursive trees*, October 4, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-root-attachments-have-an-exact-negative-path-length-profile-in-r--3b3e0426b1ba.
