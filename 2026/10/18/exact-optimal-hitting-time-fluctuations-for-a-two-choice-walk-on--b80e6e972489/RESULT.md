# Exact optimal hitting-time fluctuations for a two-choice walk on a cycle

## Finding
For every simple cycle \(C_N\), \(N\ge3\), fix a target vertex. At each nonabsorbed step, two neighbours of the current vertex are sampled independently and uniformly **with replacement**, and a controller chooses one. Write \(d\in\{1,\ldots,R\}\) for the initial graph distance to the target and \(R=\lfloor N/2\rfloor\). The rule choosing the offered neighbour with smaller target distance minimizes expected hitting time among all adaptive controllers.

Define constants
\[
 A_N=\begin{cases}-1/(2\cdot3^{R-1}),&N=2R,\\-3^{-R},&N=2R+1,\end{cases}
 \qquad
 B_N=\begin{cases}(-4R-4+A_N)/3^{R-1},&N=2R,\\(-8R-11+2A_N)/3^R,&N=2R+1.\end{cases}
\]
For the hitting time \(T_{N,d}\) of this **mean-optimal rule**, its exact first two moments are
\[
 \mathbb E T_{N,d}=2d+A_N(3^d-1),
\]
\[
 \operatorname{Var}(T_{N,d})=6d-8A_Nd3^d+B_N(3^d-1)-A_N^2(3^d-1)^2.
\]
In particular, along **every** sequence \(N\to\infty\), \(1\le d_N\le\lfloor N/2\rfloor\), and \(d_N\to\infty\),
\[
 \frac{T_{N,d_N}-2d_N}{\sqrt{6d_N}}\ \xrightarrow{\mathrm d}\ \mathcal N(0,1),
 \qquad \operatorname{Var}(T_{N,d_N})=6d_N+O(1),
\]
where the remainder is uniform in both \(N\) and \(d_N\). At antipodal distance, the parity-sensitive boundary corrections satisfy
\[
\begin{aligned}
\mathbb E T_{2R,R}&=2R-\tfrac32+O(3^{-R}),
&\operatorname{Var}(T_{2R,R})&=6R-\tfrac{57}4+O(R3^{-R}),\\
\mathbb E T_{2R+1,R}&=2R-1+O(3^{-R}),
&\operatorname{Var}(T_{2R+1,R})&=6R-12+O(R3^{-R}).
\end{aligned}
\]
These asymptotics concern integers \(R\to\infty\). The formulas themselves apply to all admitted finite cycles.

## Assumptions and scope
The graph is the ordinary undirected loopless cycle on \(N\ge3\) vertices; a sampled pair of neighbours may repeat. Sampling is fresh and independent at every step. The controller may depend on the entire past. The target is fixed and hitting ends on first arrival. Optimality refers to **minimum expectation**; no optimality claim for variance, stochastic ordering or risk-sensitive objectives is made. Under the prescribed rule, the target distance is a Markov chain on \(\{0,\ldots,R\}\), absorbed at zero.

## Proof
**1. Distance dynamics and optimality.** For \(1\le j<R\), the smaller-distance proposal is available with probability \(3/4\), so the distance goes to \(j-1\) with probability \(3/4\) and to \(j+1\) with probability \(1/4\). At \(j=R\), both neighbours decrease the distance if \(N=2R\), whereas for \(N=2R+1\) the distance decreases with probability \(3/4\) and remains \(R\) otherwise. Let \(h_0=0\) and \(h_j=\mathbb E T_{N,j}\). The interior recurrence is \(4h_j=4+3h_{j-1}+h_{j+1}\). The outer boundary gives \(h_R=1+h_{R-1}\) for an even cycle and \(h_R=4/3+h_{R-1}\) for an odd cycle. Solving the recurrence gives \(h_j=2j+A_N(3^j-1)\). Its increments are \(2-3^{j-R}\) for even cycles and \(2-(2/3)3^{j-R}\) for odd cycles, both strictly positive on \(1\le j\le R\).

Consequently, at every possible mixed offer (one neighbour at smaller distance and one at larger distance) the prescribed move minimizes the expected continuation value \(h\); at an even antipode the two offered moves have the same continuation value. The function \(h\) satisfies the Bellman equations. For any adaptive controller, conditional expected \(h\) after its next move is no smaller than that for the prescribed rule; optional stopping applied to the finite-state hitting process shows \(\mathbb E T\ge h_d\). Every controller hits almost surely in finite mean, since a fixed positive-probability sequence of forced shortest-path moves reaches the target within \(R\) steps. The greedy-distance policy realizes equality.

**2. Exact variance.** Write \(s_j=\mathbb E[T_{N,j}^2]\). The first-step identity in the interior is \(s_j=1+2\mathbb E[h_{J_1}]+\mathbb E[s_{J_1}]\), equivalently \(s_j-\frac34s_{j-1}-\frac14s_{j+1}=2h_j-1\). A particular solution together with its homogeneous correction is
\[
 s_j=4j^2+6j-4A_Nj3^j-4A_Nj+B_N(3^j-1).
\]
This satisfies \(s_0=0\). At an even antipode, \(T_{N,R}=1+T_{N,R-1}'\) in distribution, so \(s_R-s_{R-1}=1+2h_{R-1}\). At an odd antipode, the initial waiting time to decrease to \(R-1\) is geometric with success probability \(3/4\), hence has first moment \(4/3\), second moment \(20/9\), and \(s_R-s_{R-1}=20/9+(8/3)h_{R-1}\). These two equations yield exactly the stated constants \(B_N\). Subtracting \(h_j^2\) gives the variance formula.

**3. Uniform Gaussian limit.** For \(0<z<1\), let \(F_j(z)=\mathbb E[z^{T_{N,j}}]\). The interior recurrence is \(F_j=z(3F_{j-1}+F_{j+1})/4\), with \(F_0=1\) and the boundary equation \(F_R=b_N(z)F_{R-1}\), where \(b_{2R}(z)=z\) and \(b_{2R+1}(z)=3z/(4-z)\). Define
\[
 \lambda(z)=\frac{2-\sqrt{4-3z^2}}z,\qquad
 \Lambda(z)=\frac{2+\sqrt{4-3z^2}}z,\qquad
 \eta_N(z)=\left(\frac{\lambda(z)}{\Lambda(z)}\right)^{R-1}
 \frac{b_N(z)-\lambda(z)}{\Lambda(z)-b_N(z)}.
\]
Solving the two-root recurrence gives the **exact** transform
\[
 F_d(z)=\frac{\lambda(z)^d+\eta_N(z)\Lambda(z)^d}{1+\eta_N(z)}.
\]
Each term analytically continues to a fixed complex neighbourhood of \(z=1\). There \(\lambda(1)=1\), \(\Lambda(1)=3\), \(b_N(1)=1\), and \(|\lambda/\Lambda|\) is uniformly less than one. Moreover \(b_N-\lambda=O(z-1)\) and \(\Lambda-b_N\) stays bounded away from zero. Since \(d\le R\), it follows with constants **independent of** \(N,d\) that
\[
 \log F_d(e^u)=d\log\lambda(e^u)+O(|u|),\qquad
 \log\lambda(e^u)=2u+3u^2+O(u^3)
\]
for sufficiently small complex \(u\), with an analytic remainder uniformly bounded on a fixed disk. Taking \(u=it/\sqrt{6d}\) proves convergence of centered characteristic functions to \(e^{-t^2/2}\). Analytic differentiation of the same expansion also yields \(\operatorname{Var}T_{N,d}=6d+O(1)\) uniformly; equivalently, uniform boundedness follows directly from the finite variance formula by setting \(k=R-d\) and observing \(k3^{-k}\) is bounded. Finally, inserting \(d=R\) into both exact moments yields the two displayed parity corrections.

## Verification
Run `python verify.py` in a directory containing this document and the checker. The checker independently builds the finite distance-chain rational transition matrix, solves first- and second-moment systems by exact Gaussian elimination, compares every state with the formulas, and compares probability-generating functions at several rational \(z\). It also enumerates all deterministic proposal responses on small cycles to confirm the Bellman inequalities directly. All infinite-index assertions in the theorem follow from the displayed recurrences and analytic transform; numerical tests alone are not used as proofs.

## Relationship to prior work
Georgakopoulos, Haslegrave, Sauerwald and Sylvester [1] introduced the controlled two-proposal walk, proved polynomial-time computability of expected-hitting-time optimizers, and established order-sharp hitting-time bounds on tori, including \(\Theta(\operatorname{diam}G)\). Its full arXiv exposition treats general bounds and optimization but does **not state** the explicit cycle-distance moments, parity boundary corrections, or uniform Gaussian law derived here. In its hardness argument it does use the basic \(3/4\) direction preference, which is acknowledged as background. The \(\varepsilon\)-biased walk of Haslegrave, Sauerwald and Sylvester [2] allows free choice with a fixed probability instead of choosing between two sampled neighbours: it is a related but distinct transition mechanism. Classical biased birth-death walk recurrences underlie the calculation; they are not asserted new.

## Limitations
Priority is based on the inspected sources and targeted searches, not an exhaustive survey of earlier birth-death or controlled-walk literature. A previously published equivalent closed-form expression or a general formula immediately implying all of these exact statements could supersede the novelty claim. The CLT holds for the **mean-optimal distance-greedy policy**, and does not describe all nonoptimal controllers. No assertion is made about minimizing variance or tail probabilities among controllers. The method uses degree two and does not extend automatically to arbitrary graphs.

## References
[1] A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170, first posted 2019-11-12; *Combinatorics, Probability and Computing* 31 (2022), 73–100, DOI: 10.1017/S0963548321000183.

[2] J. Haslegrave, T. Sauerwald and J. Sylvester, *Time Dependent Biased Random Walks*, arXiv:2006.02475, first posted 2020-06-03; *ACM Transactions on Algorithms* 18(2) (2022), DOI: 10.1145/3498848.
