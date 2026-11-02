# A sharp invariant-box coupling budget for logistic threshold networks

## Finding
For the logistic threshold network with centered stimulus, there is an explicit, dimension-independent and exactly sharp **invariant-box** coupling budget. Below it, every binary assignment of low or high activity to each block has its own certified positive-volume basin containing exactly one exponentially stable equilibrium, without equitable partition assumptions. Sharpness here means sharpness of the stated boxes for **all** admissible matrices, not a maximal multistability threshold.

## Assumptions and scope
Let \(N\ge m\ge2\). Partition \(\{1,\ldots,N\}\) into nonempty blocks \(C_1,\ldots,C_m\). Let \(W\in[0,1]^{N\times N}\) satisfy \(\sum_jW_{ij}=1\), with no symmetry, primitivity, equitability, or regularity assumption. Let \(\beta>4\), \(F(s)=(1+e^{-s})^{-1}\), and consider
\[
 \dot x_i=-x_i+F\!\left(\beta\left[\sum_jW_{ij}x_j-\tfrac12\right]\right),\qquad i=1,\ldots,N.
\]
All initial conditions lie in \([0,1]^N\). Define the maximal cross-block row mass
\[
 \varepsilon=\max_{a}\max_{i\in C_a}\sum_{j\notin C_a}W_{ij}.
\]
Put \(t=\sqrt{1-4/\beta}\), \(b=(1-t)/2\), and
\[
 E_\beta=\frac{t-(1-t^2)\operatorname{artanh}(t)}{1+t}
 =\frac{\tfrac12-b+\beta^{-1}\log[b/(1-b)]}{1-b}.
\]
Both \(b\in(0,1/2)\) and \(E_\beta\in(0,1)\). For each \(\sigma\in\{L,H\}^m\), define \(I_L=[0,b]\), \(I_H=[1-b,1]\), and \(Q_\sigma=\prod_{a=1}^m\prod_{i\in C_a}I_{\sigma_a}\).

**Theorem.** For every admissible \(N,m,W,\beta\), if \(\varepsilon<E_\beta\), every \(Q_\sigma\) is forward invariant and supports exactly one interior equilibrium \(x_\sigma^*\), to which all its initial states converge with the explicit estimate
\[
 \|x(t)-x_\sigma^*\|_\infty\le e^{-c_\beta(\varepsilon)t}\|x(0)-x_\sigma^*\|_\infty,
 \quad c_\beta(\varepsilon)=1-\beta F'\!\left(\beta[b+(1-b)\varepsilon-\tfrac12]\right)>0.
\]
In particular there are at least \(2^m\) distinct locally exponentially attracting equilibria with disjoint positive-volume guaranteed basins. For any \(E_\beta<\varepsilon'\le1\), some two-node row-stochastic network with two singleton blocks and cross-block row mass exactly \(\varepsilon'\) fails forward invariance of the corresponding low/high box. Moreover \(E_\beta\sim(\beta-4)^{3/2}/12\) as \(\beta\downarrow4\), while \(E_\beta\to1/2\) as \(\beta\to\infty\).

## Proof
**1. Critical scalar identities.** Since \(\beta b(1-b)=1\), writing \(\ell=\log[b/(1-b)]<0\) gives \(\beta(b-1/2)<\ell\). Indeed \(\ell=-2\operatorname{artanh}(t)\), and \(\beta(1/2-b)=2t/(1-t^2)>2\operatorname{artanh}(t)\), because the derivative of \(t/(1-t^2)-\operatorname{artanh}(t)\) is \(2t^2/(1-t^2)^2>0\) and its value at zero is zero. Hence \(E_\beta>0\), with \(E_\beta<1\) immediate from the equivalent formula (the numerator is below \(1-b\)).

**2. Strict inward vector fields.** For any point in \(Q_\sigma\), and any node \(i\) assigned low, the input average satisfies
\[
 \sum_jW_{ij}x_j\le b(1-\varepsilon_i)+\varepsilon_i\le b+(1-b)\varepsilon,
 \quad \varepsilon_i=\sum_{j\notin C_a}W_{ij}.
\]
Set \(z=\beta[b+(1-b)\varepsilon-1/2]\). The strict budget is equivalent to \(z<\ell<0\); hence \(F(z)<F(\ell)=b\). At a low upper face \(x_i=b\), \(\dot x_i\le F(z)-b<0\), while at \(x_i=0\) the derivative is positive. For a high node, the average is at least \((1-b)(1-\varepsilon_i)\ge1-b-(1-b)\varepsilon\), and the response at its lower face exceeds \(F(-z)=1-F(z)>1-b\). At \(x_i=1\), the derivative is negative. Thus each coordinate points strictly inward on all faces. The usual first-exit argument proves forward invariance and even that equilibria cannot occur on its boundary.

**3. Exact contraction in each box.** On the low-coordinate input range the logistic derivative satisfies \(F'(s)\le F'(z)\), since \(s\le z<0\) and \(F'\) increases there. On the high-coordinate range \(s\ge-z>0\), symmetry gives the identical upper bound. Thus for \(T(x)_i=F(\beta[(Wx)_i-1/2])\) and any \(x,y\in Q_\sigma\), the segment between them remains in the box and
\[
 \|T(x)-T(y)\|_\infty\le L\|x-y\|_\infty,\qquad L=\beta F'(z)<\beta b(1-b)=1.
\]
The strict face bounds ensure \(T(Q_\sigma)\subset\operatorname{int}Q_\sigma\), and the Banach fixed-point theorem supplies a unique interior equilibrium \(x_\sigma^*\). Two ODE solutions in the same box satisfy the upper-Dini derivative estimate \(D^+\|x(t)-y(t)\|_\infty\le-(1-L)\|x(t)-y(t)\|_\infty\), obtained from the coordinate variation-of-constants equation; Grönwall proves the stated rate. In fact small neighborhoods of the interior fixed points remain in their boxes, establishing local exponential stability in the full state space. Disjointness follows from the coordinate gap \(1-2b=t>0\) between low and high intervals for at least one entire block.

**4. Sharp canonical-box limit.** Given \(E_\beta<\varepsilon'\le1\), take two singleton blocks and
\[
 W=\begin{pmatrix}1-\varepsilon'&\varepsilon'\\0&1\end{pmatrix},\qquad x=(b,1)\in Q_{(L,H)}.
\]
For its first coordinate, \(\dot x_1=F(\beta[b+(1-b)\varepsilon'-1/2])-b>0\), since \(\varepsilon'>E_\beta\); the trajectory immediately leaves \(Q_{(L,H)}\). This proves the claimed universal box-threshold optimality, **not** the failure of other invariant sets or equilibria above it.

**5. Coupling-limit scales.** Taylor's theorem gives \(t-(1-t^2)\operatorname{artanh}(t)=(2/3)t^3+O(t^5)\) and \(t=\sqrt{(\beta-4)/\beta}\), yielding the \((\beta-4)^{3/2}/12\) asymptotic; the limit as \(\beta\to\infty\) follows from \((1-t^2)\operatorname{artanh}(t)\to0\).

## Verification
The package contains \(\texttt{verification.py}\), using only the Python standard library. Run \(\texttt{python3 verification.py}\). It checks row sums, cross-block masses, scalar identities for nine feedback strengths, strictly positive contraction rates below the budget, the outward derivative above the budget, cusp asymptotics, and the existence of four distinct numerically computed box equilibria in a directed non-equitable example. These computations corroborate, but cannot replace, the quantified analytic proof.

For \(\beta=8\), \(E_8\approx0.15606521549378\), \(b\approx0.14644660940673\). With blocks \(\{1,2\}\), \(\{3,4\}\), take
\[
 W=\begin{pmatrix}.80&.05&.10&.05\\.05&.81&.01&.13\\.06&.04&.75&.15\\.11&.02&.12&.75\end{pmatrix}.
\]
Its within-block leakage values are \(0.15,0.14,0.10,0.13\): the partition is non-equitable and the maximum leakage is \(0.15<E_8\). The four attracting equilibria have distinct certified boxes; the universal contraction bound for these boxes is \(c_8(0.15)\approx0.02906696217\).

## Relationship to prior work
Boudourides (2026) studies this threshold-network family, proving persistence of combinatorial attractor configurations under sufficiently weak interblock coupling for equitable partitions, with small non-equitable perturbations. Its published arguments do not provide this dimension-independent, explicit all-row leakage budget, nor the strictly invariant full-dimensional basins or the sharpness assertion for these canonical boxes. In particular, our assumption is on individual cross-block row totals, with **no** restrictions on intrablock topology or deviations from equitability. The underlying inward-box and contraction techniques are standard; the contribution claimed is their precise quantitative combination and boundary for this model. General steep-sigmoid stability and coupled-network contraction literature is relevant but does not, in the inspected material, imply the exact formula and universal canonical-box sharpness. This is a literature-bounded originality assessment, not a proof of absolute priority.

## Limitations
The theorem guarantees **at least** \(2^m\) attracting equilibria and the displayed basins; it does not classify all equilibria or trajectories outside the boxes. Sharpness is exclusively for the universal forward invariance of these specific boxes and **does not** assert a sharp multistability threshold. The center input is fixed to \(-\beta/2\) and the response is logistic; other sigmoids and arbitrary stimuli are not covered. General contraction lemmas and prior steep-sigmoid results may furnish alternative proofs; complete historical priority has not been independently audited.

## References
1. M. Boudourides, “Collective Hysteresis and Multistability in Threshold Networks,” arXiv:2609.10580v1, 2026-09-05. https://arxiv.org/abs/2609.10580
2. W. Duncan, T. Gedeon, H. Kokubu, K. Mischaikow and H. Oka, “Equilibria and Their Stability in Networks with Steep Sigmoidal Nonlinearities,” arXiv:2103.17184; SIAM Journal on Applied Dynamical Systems (2021), DOI 10.1137/21M1398331. https://arxiv.org/abs/2103.17184
3. Q.-C. Pham and J.-J. E. Slotine, “Stable Concurrent Synchronization in Dynamic System Networks,” arXiv:q-bio/0510051 (2005). https://arxiv.org/abs/q-bio/0510051
4. S. Gaubert and Z. Qu, “Dobrushin Ergodicity Coefficient for Markov Operators on Cones, and Beyond,” arXiv:1302.5226 (2013). https://arxiv.org/abs/1302.5226
