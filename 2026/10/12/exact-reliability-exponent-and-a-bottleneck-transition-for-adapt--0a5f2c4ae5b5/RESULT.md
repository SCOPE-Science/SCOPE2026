# Exact reliability exponent and a bottleneck transition for adaptive single-copy stabilizer learning
## Finding
For the exact adaptive single-copy stabilizer learner of Bittel, Eisert, Gong, Mele, and Schatzki, define \(F_n(T)\) as the worst-case probability that the state returned after \(T\) adaptive rounds differs from the unknown pure \(n\)-qubit stabilizer state. For every fixed \(x>2\), set \(T_n=\lfloor xn\rfloor\). Then
\[
\lim_{n\to\infty}-\frac{1}{n}\log F_n(T_n)=I(x),
\]
with natural logarithms and
\[
I(x)=
\begin{cases}
(x-1)\log\!\left(\dfrac{2(x-1)}{x}\right)+\log\!\left(\dfrac{2}{x}\right),&2<x\le3,\\[4pt]
x\log\!\left(\dfrac43\right)-\log 2,&x\ge3.
\end{cases}
\]
The worst case is attained by stabilizer states whose diagonal stabilizer subspace is trivial, including \(\lvert+\rangle^{\otimes n}\). Because the algorithm consumes \(N=2T+1\) copies, the reliability mechanism changes at asymptotic copy ratio \(N/n=6\).

For \(2<x<3\), failure is a collective slowdown of the many stages whose geometric success probabilities tend to \(1/2\). For \(x>3\), the least costly rare-event strategy keeps the bulk at the boundary tilt corresponding to three rounds per unresolved dimension and puts every additional linear delay into the final codimension-one stage, whose success probability is \(1/4\). The two branches meet with the same first derivative at \(x=3\), but the second branch is linear.

## Assumptions and scope
The statement concerns Algorithm 1 in arXiv:2610.02031v1, exact learning of pure qubit stabilizer states, and a deterministic round budget \(T\). It is a reliability law for that algorithm, not a lower bound for all adaptive single-copy learners and not an improvement of the paper's fixed-confidence leading constant. The rate uses natural logarithms. A geometric random variable counts the successful round and therefore has support \(\{1,2,\ldots\}\).

## Proof
Let \(r\) be the codimension of the current diagonal stabilizer subspace. The source proves that a round decreases \(r\) by exactly one with probability
\[
p_r=\frac{1-2^{-r}}{2},
\]
and otherwise leaves \(r\) unchanged. Hence, starting from \(r=n\), the stopping time is exactly
\[
\tau_n=\sum_{r=1}^n G_r,
\qquad G_r\sim\operatorname{Geom}(p_r)
\]
with independent summands. States with trivial initial diagonal stabilizer subspace start at \(r=n\), while every other stabilizer state starts at a smaller codimension and is stochastically easier. If \(\tau_n>T\), the transformed state is not a computational-basis state, so the final basis measurement cannot make the returned basis state equal to that transformed state. Thus
\[
F_n(T)=\Pr(\tau_n>T).
\]

Write \(a=\log(4/3)\), separate the final bottleneck \(G_1\), and put \(S_n=\sum_{r=2}^nG_r\). For fixed \(\theta<\log(8/5)\), summability of \(2^{-r}\) gives
\[
\lim_{n\to\infty}\frac1n\log\mathbb E e^{\theta S_n}
=\Lambda(\theta)
=\log\!\left(\frac{e^\theta}{2-e^\theta}\right).
\]
The Legendre saddle for a mean value \(x>2\) is
\[
\theta_x=\log\!\left(\frac{2(x-1)}{x}\right).
\]
For \(2<x\le3\), one has \(\theta_x\le a\). Chernoff's bound gives the upper exponent, while exponential tilting of \(S_n\) at \(\theta_x\), whose tilted variance is of order \(n\), gives the matching lower exponent. Substitution yields
\[
I_0(x)=x\theta_x-\Lambda(\theta_x)
=(x-1)\log\!\left(\frac{2(x-1)}x\right)+\log\!\left(\frac2x\right).
\]

The full moment generating function is restricted by \(G_1\), since \(p_1=1/4\) and its domain ends at \(a=\log(4/3)\). Therefore for \(x\ge3\), taking \(\theta\uparrow a\) in the Chernoff bound gives
\[
\liminf_{n\to\infty}-\frac1n\log F_n(\lfloor xn\rfloor)
\ge xa-\Lambda(a)=x\log\!\left(\frac43\right)-\log2.
\]
For the reverse inequality, force \(S_n\) into a width-\(o(n)\) neighborhood of \(3n\) and independently require \(G_1\) to supply the remaining \((x-3)n+o(n)\) rounds. The bulk event costs \(I_0(3)=3a-\log2\), and the geometric tail of \(G_1\) costs \((x-3)a\). Their sum is exactly \(xa-\log2\). This also proves the formula at \(x=3\).

The first branch has derivative \(\theta_x\), so its derivative at \(x=3\) is \(a\), matching the slope of the linear branch. This identifies the transition as a change in the dominant rare-event mechanism rather than a cusp.

## Verification
The analytic argument verifies the exact stopping-time law, the limiting log moment generating function, the Legendre saddle, the bottleneck boundary, and the matching lower construction. A standalone standard-library checker recomputes the branch matching and evaluates exact finite-\(n\) stopping-time tails by dynamic programming for representative linear budgets. These finite calculations corroborate the asymptotic proof and are not used as a substitute for it.

## Relationship to prior work
Bittel et al. prove the exact stage probabilities and independent-geometric stopping-time representation, then invoke a general geometric-sum concentration inequality to obtain a sufficient high-probability runtime. They do not state an exact large-deviation exponent, the piecewise reliability law above, or the codimension-one bottleneck transition. Janson gives general explicit tail bounds for sums of geometric variables rather than this sharp application-specific exponent. Montanaro's Bell-sampling learner uses coherent two-copy measurements, while Chang et al. give sample-optimal stabilizer learning with unrestricted measurements; these are different measurement models and do not imply the reliability law for the adaptive single-copy algorithm.

## Limitations
The theorem evaluates the failure exponent of one specified exact learner. It does not prove that the exponent is optimal among adaptive single-copy protocols, does not lower the algorithm's fixed-confidence leading copy constant, and does not address tolerant learning. The originality comparison is necessarily subject to the possibility of a differently indexed general triangular-array large-deviation theorem that could subsume the probabilistic calculation abstractly; no inspected source supplied the stated stabilizer-learning specialization or its bottleneck interpretation.

## References
1. L. Bittel, J. Eisert, W. Gong, A. A. Mele, and L. Schatzki, “Adaptivity is all you need: Optimal stabilizer learning using just single-copy measurements,” arXiv:2610.02031v1, first submitted 2026-10-01.
2. S. Janson, “Tail bounds for sums of geometric and exponential variables,” arXiv:1709.08157v1.
3. A. Montanaro, “Learning stabilizer states by Bell sampling,” arXiv:1707.04012.
4. H.-C. Chang et al., “Sample-optimal learning of stabilizer states,” arXiv:2609.10974v1.
