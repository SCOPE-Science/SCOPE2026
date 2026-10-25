# A quadratic birth-horizon for degree–depth covariance in random recursive trees

## Finding
Let \(T_n\) be a uniform random recursive tree on birth labels \(1,\ldots,n\), and let \(D_i\) be the number of children of vertex \(i\) and \(H_j\) the depth of vertex \(j\). For every integer \(n\ge2\) and all \(1\le i,j\le n\),
\[
\operatorname{Cov}(D_i,H_j)=
\begin{cases}
0,&i\ge j,\\[2pt]
\displaystyle \frac{i-1}{i^2}-\sum_{s=i+1}^{j-1}\frac1{s^2},&i<j.
\end{cases}
\]
The empty sum is zero. In particular, for every \(i<j<n\),
\[
\operatorname{Cov}(D_i,H_{j+1})-\operatorname{Cov}(D_i,H_j)=-\frac1{j^2}.
\]
Thus the cross-covariance decreases strictly with the target's birth label at a rate independent of the source's label. For the root \(i=1\), it vanishes at \(j=2\) and is negative for \(j\ge3\). For each \(i\ge2\), it starts positive at \(j=i+1\), changes to nonpositive exactly once, and thereafter is strictly negative. Define \(J_i\) to be the first integer \(j\ge i+1\) at which the covariance is nonpositive (taking any \(n\ge j\)). Then \(J_i\) exists and
\[
J_i=2i^2-\frac{2i}{3}+O(1)\quad(i\to\infty).
\]
For example, \(J_2=8\), \(J_3=17\), and \(J_4=31\). A possible exact zero at the transition is not excluded; the single-crossing statement concerns signs before and after \(J_i\).

## Assumptions and scope
Start with vertex \(1\). For every integer \(t\ge2\), independently choose its parent \(P_t\) uniformly from \(\{1,\ldots,t-1\}\). Attach vertex \(t\) to \(P_t\). The depth \(H_j\) is the number of edges on the path from \(j\) to the root, with \(H_1=0\). The outdegree \(D_i=\sum_{t=i+1}^n\mathbf 1\{P_t=i\}\). All covariances are population covariances under this distribution, not estimates. The formula is exact for every finite \(n\) and does not depend on \(n\) beyond \(n\ge j\). It is not an assertion of independence or of a sign for the undirected degree.

## Proof
**Expected depth.** Independent uniform attachments and \(H_t=1+H_{P_t}\) give \(\mathbb E H_t=H_{t-1}^{(1)}:=\sum_{r=1}^{t-1}1/r\). To avoid ambiguity, write \(h_m:=\sum_{r=1}^m1/r\), so \(\mathbb E H_t=h_{t-1}\) and \(h_0=0\). This follows by induction from \(\mathbb E H_t=1+(t-1)^{-1}\sum_{r<t}\mathbb E H_r\).

**Single-parent influence.** Fix \(i<t\le j\). The event that \(j\) descends from \(t\) is determined by parent choices later than \(t\), so it is independent of \(P_t\) and of the tree on birth labels up to \(t\). Its probability is \(q_{t,j}=1\) for \(j=t\), and \(q_{t,j}=1/t\) for \(j>t\). The latter value follows by induction: for \(j>t\), the probability equals the average of the corresponding ancestor indicators over potential parents in \(\{1,\ldots,j-1\}\), whose expected sum is \((j-1)/t\). Resampling only \(P_t\) changes \(H_j\) exclusively when \(j\) descends from \(t\); on that event the change is the change in \(H_t\). Consequently,
\[
\operatorname{Cov}(\mathbf1\{P_t=i\},H_j)
=\frac{q_{t,j}}{t-1}\bigl(1+h_{i-1}-h_{t-1}\bigr).
\]
Indeed \(\mathbb E[H_t\mid P_t=i]=1+h_{i-1}\), and \(\mathbb E H_t=h_{t-1}\). This uses the independent-parent construction; in particular the descendant indicator does not depend on \(P_t\).

**Exact covariance.** When \(i\ge j\), \(D_i\) uses only parent choices after time \(i\) and is independent of \(H_j\). When \(i<j\), all arrivals later than \(j\) contribute zero covariance, so summing the single-parent influence gives
\[
C_i(j):=\operatorname{Cov}(D_i,H_j)
=\sum_{t=i+1}^{j-1}\frac{1+h_{i-1}-h_{t-1}}{t(t-1)}
+\frac{1+h_{i-1}-h_{j-1}}{j-1}.
\]
At \(j=i+1\), this equals \((i-1)/i^2\). Put \(a_t=1+h_{i-1}-h_{t-1}\). Since \(a_{j+1}=a_j-1/j\), subtracting the two consecutive displayed sums gives \(C_i(j+1)-C_i(j)=-1/j^2\). Induction yields the asserted exact formula for all \(i<j\).

**Sharp sign horizon.** Define \(Q_m:=\sum_{s=m}^{\infty}s^{-2}\) and \(\delta_i:=Q_{i+1}-(i-1)/i^2\). Then for \(i<j\), \(C_i(j)=Q_j-\delta_i\). The integral bound \(Q_{i+1}>1/(i+1)>(i-1)/i^2\) shows \(\delta_i>0\). Since \(Q_j\) decreases strictly to zero, \(C_i(j)\) eventually becomes negative. For \(i\ge2\), \(C_i(i+1)=(i-1)/i^2>0\), giving exactly one sign transition in the stated sense. For \(i=1\), \(C_1(2)=0\) and strict decrements give \(C_1(j)<0\) for \(j\ge3\).

For the asymptotic location, the standard Euler–Maclaurin expansion of the absolutely convergent reciprocal-square tail gives
\[
Q_{i+1}=\frac1i-\frac1{2i^2}+\frac1{6i^3}+O(i^{-5}),\qquad
\delta_i=\frac1{2i^2}+\frac1{6i^3}+O(i^{-5}),
\]
while \(Q_j=1/j+O(j^{-2})\). Strict monotonicity first yields \(J_i\sim2i^2\). Substitution of \(j=2i^2-(2/3)i+v\) with bounded \(v\) gives
\[
Q_j-\delta_i=\frac{13/72-v/4}{i^4}+O(i^{-5}).
\]
Taking two fixed values of \(v\) on opposite sides of \(13/18\) and using monotonicity traps \(J_i\) between their neighboring integers. Hence \(J_i=2i^2-(2/3)i+O(1)\). This proves the assertions without assuming the numerical data extend to infinity.

## Verification
The accompanying standard-library script `verify.py` enumerates every independent parent sequence for \(2\le n\le9\), computes the observed degree/depth cross-covariance by exact rational arithmetic, and checks every matrix entry against the formula. It additionally verifies the universal decrement and the finite transition property for \(2\le i\le30\). The exact finite checks supplement, but do not replace, the proof of the unrestricted identities and asymptotics.

## Relationship to prior work
Eslava's work on high-degree vertices in random recursive trees [1] established conditional and limiting behavior of depths of selected vertices. Lodewijks [2] derived joint asymptotic laws for degree, depth, labels, and distances, including prescribed-label vertices (Theorem 2.6 and Section 6). These results motivate asking what *finite-size* cross-dependence remains between two distinct, birth-labeled vertices. The exact pairwise covariance and its label-universal decrement do not follow from a joint weak limit alone. This proof treats the full labeled cross-moment matrix directly and identifies a quadratic sign horizon.

## Limitations
The result concerns uniform recursive trees and the rooted child count, not general increasing-tree growth rules. It measures covariance rather than full conditional stochastic order, and the root's zero at \(j=2\) is degenerate because that depth is deterministic. The exact-zero cases at the nonroot transition have not been classified. The two cited sources do not, in the inspected material, state these exact formulas; an implicit equivalent in older literature remains a priority risk. No independent mathematical audit has been performed.

## References
[1] Laura Eslava, *Depth of vertices with high degree in random recursive trees*, arXiv:1611.07466 (first public submission 2016-11-22), https://arxiv.org/abs/1611.07466.

[2] Bas Lodewijks, *On joint properties of vertices with a given degree or label in the random recursive tree*, arXiv:2204.09032 (first public submission 2022-04-19), https://arxiv.org/abs/2204.09032.
