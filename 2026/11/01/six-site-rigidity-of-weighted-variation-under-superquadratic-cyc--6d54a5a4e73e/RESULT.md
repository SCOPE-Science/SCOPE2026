# Six-site rigidity of weighted variation under superquadratic cyclic heat

## Finding
For every integer \(n\ge3\) and real exponent \(p>2\), consider the graph \(p\)-heat flow on the unit-conductance cycle \(C_n\) with counting-measure vertex masses. Give its edges independent strictly positive *variation weights* \(w_0,\ldots,w_{n-1}\), which do not change the heat conductances. With
\[
J_w(u)=\sum_{i=0}^{n-1}w_i|u_{i+1}-u_i|,
\]
the following dichotomy is exact:
\[
\boxed{n\ge6:\quad J_w(u(t))\le J_w(u(0))\text{ for all }u(0),\,t\ge0
\iff w_0=\cdots=w_{n-1}.}
\]
For a nonconstant weight vector on any cycle of length at least six, there is an initial real signal for which \(J_w(u(t))>J_w(u(0))\) at every sufficiently small positive time.

The length threshold is sharp: for each fixed \(p>2\) and each \(n=3,4,5\), all sufficiently small perturbations of the uniform positive weights remain contractive. In particular, when \(p=3\), weights \((1,3/2,1,3/2,1)\) on \(C_5\) yield strict instantaneous variation decrease at every nonconstant initial signal. At the linear exponent \(p=2\), the alternating six-cycle weights \((1,3/2,1,3/2,1,3/2)\) are also contractive; the superquadratic rigidity is therefore a genuine change in the generator, not merely a graph-size statement.

## Assumptions and scope
Cycles are simple, with vertex indices taken modulo \(n\), \(n\ge3\). There are unit vertex masses, unit heat conductances, positive edge-variation weights, arbitrary real-valued initial vertex data, and a fixed \(p>2\). Write \(\Phi(a)=|a|^{p-2}a\), \(q=p-1>1\). The globally defined flow is
\[
\dot u_i=\Phi(u_{i+1}-u_i)+\Phi(u_{i-1}-u_i).
\]
Its edge increments \(x_i=u_{i+1}-u_i\) satisfy both \(\sum_i x_i=0\) and
\[
\dot x_i=\Phi(x_{i-1})+\Phi(x_{i+1})-2\Phi(x_i).
\]
Conversely, every real zero-sum edge vector is the increment vector of a periodic vertex signal. The vector field is locally Lipschitz for \(p>2\); the maximum principle bounds all solutions, hence they exist globally. For a locally Lipschitz path, \(D^+\) denotes its upper right time derivative.

## Proof
**1. Uniform weights contract.** For any time, choose \(s_i=\operatorname{sgn}(x_i)\) if \(x_i\ne0\) and \(s_i=\operatorname{sgn}(\dot x_i)\) if \(x_i=0\), with any \(s_i\in[-1,1]\) allowed when both vanish. Then \(D^+\sum_i|x_i|=\sum_i s_i\dot x_i\). Cyclic summation by parts yields
\[
\sum_i s_i\dot x_i=-\sum_i (s_{i+1}-s_i)(\Phi(x_{i+1})-\Phi(x_i))\le0,
\]
since both \(s_i\) and \(\Phi(x_i)\) are nondecreasing functions of \(x_i\) in the pairwise comparison sense. Multiplication by a common positive weight preserves the inequality. Integrating the Dini inequality establishes contraction at all times.

**2. Sparse dipoles impose paired harmonicity.** Fix \(n\ge6\), and abbreviate
\[
d_j=w_{j-1}+w_{j+1}-2w_j,\qquad k=j+3\pmod n.
\]
The three-index neighborhoods of \(j\) and \(k\) are disjoint. Start with an edge vector having \(x_j=1\), \(x_k=-1\), and all other coordinates zero. It is zero-sum. At time zero, the two active edges have derivatives \(-2\) and \(+2\), and the four distinct adjacent zero edges have derivatives of absolute value \(1\). Therefore the exact right variation derivative is
\[
D^+J_w=d_j+d_{j+3}.
\]
Universal contraction forces \(d_j+d_{j+3}\le0\) for every \(j\). Summing over all \(j\) gives zero, because \(\sum_jd_j=0\); consequently
\[
d_j+d_{j+3}=0\quad\text{for every }j.
\]

**3. Superquadratic sparsity forces separate harmonicity.** Suppose some \(d_j\ne0\). Select \(a,b\in\{0,1}\) so that \(d_j(b-a)>0\), and let \(\varepsilon>0\) be small. Form a zero-sum increment vector with
\[
x_j=1-a\varepsilon,\quad x_{j-1}=a\varepsilon,\quad
x_k=-(1-b\varepsilon),\quad x_{k-1}=-b\varepsilon,
\]
and all other coordinates zero. Take a subgradient sign vector which is positive throughout \(\{j-1,j,j+1\}\) and negative throughout \(\{k-1,k,k+1\}\); these sets are disjoint. The right derivative of \(J_w\) is at least its evaluation against this valid subgradient. Using the edge equation, the contributions of the large coordinates are \(d_j(1-a\varepsilon)^q\) and \(d_k(1-b\varepsilon)^q\), while the remaining nonzero-flux contributions are \(O(\varepsilon^q)\). Since \(d_k=-d_j\) and \(q>1\), the resulting lower bound is
\[
q\,d_j(b-a)\varepsilon+O(\varepsilon^2)+O(\varepsilon^q)>0
\]
for sufficiently small \(\varepsilon\). This contradicts contraction. Hence \(d_j=0\) for all \(j\). The only periodic solutions of \(w_{j-1}+w_{j+1}=2w_j\) are constant positive vectors. The dipole or its perturbation also furnishes strict instantaneous amplification whenever weights are nonuniform; continuity implies increase for small positive time.

**4. Why five vertices are different.** At uniform weights, step 1 gives nonpositive \(D^+J\). Equality requires that at each adjacent pair with unequal values \(x_i\ne x_{i+1}\), the associated signs \(s_i,s_{i+1}\) agree. Any nonconstant zero-sum \(x\) contains a strictly positive and a strictly negative coordinate. Equality would require those two indices to be at graph distance at least three: an adjacent pair contradicts the sign condition, and a distance-two pair either has a nonzero sign crossing or a zero whose subgradient sign would have to be both positive and negative. Every pair of vertices on \(C_n\) for \(3\le n\le5\) is at distance at most two. Hence \(D^+J<0\) for every nonzero zero-sum \(x\).

For each fixed \(p>2\) and \(3\le n\le5\), normalize \(\sum_i|x_i|=1\). The normalized zero-sum set is compact, and the right derivative of unweighted variation is upper semicontinuous in \(x\) (at vanishing coordinates, the absolute-value term is the upper envelope of its neighboring sign choices). Its maximum is therefore \(-\eta_{n,p}<0\). If \(\max_i|w_i-1|\le\delta\), the weighted derivative differs from the unweighted derivative by at most \(\delta\sum_i|\dot x_i|\le4n\delta\) on this set. Taking \(\delta<\eta_{n,p}/(4n)\) proves strict instantaneous decrease for every nonzero gradient, and homogeneity and integration give global contraction. This ball of weights contains nonuniform vectors.

**5. Exact five-vertex and linear contrasts.** For \(p=3\), fix a sign vector \(s_i\in\{-1,1}\) containing both signs. Normalize the positive and negative masses of \(x\) to one each. On each sign chamber the variation derivative is \(\sum_i c_i r_i^2\) with \(r_i\ge0\), \(c_i=s_i(w_{i-1}s_{i-1}+w_{i+1}s_{i+1})-2w_i\). On a simplex the maximum of \(\sum c_i r_i^2\) equals \(\max_i c_i\) if some coefficient is nonnegative and equals \(-1/\sum_i(-c_i)^{-1}\) if all are negative. Applying this exact formula to all thirty nonconstant signs of \(C_5\) with \(w=(1,3/2,1,3/2,1)\) yields maximum \(-1/4\), so contraction holds. For \(p=2\), the same sign-chamber optimization is linear; on \(C_6\) with alternating weights \((1,3/2)\), its maximum over all sixty-two signs is exactly zero, establishing the stated linear comparison. All enumerations are reproducible with the attached rational-arithmetic script.

## Verification
The standalone `verification/check_cycle_pheat.py` uses exact fractions. It checks 48,530 zero-sum integer-gradient instances of the uniform \(p=3\) contraction statement on cycles of lengths three through eight, with strict negativity on lengths three through five. It also evaluates every nonconstant sign chamber exactly for the weighted five-cycle \(p=3\) and the alternating six-cycle at \(p=2\) and \(p=3\). For the six-cycle with \(p=3\), the increment vector \((-\varepsilon,-(1-\varepsilon),0,0,1,0)\) has the exact positive right derivative \(2\varepsilon-3\varepsilon^2\) for \(0<\varepsilon<2/3\). The general theorem follows from steps 1–4, not the finite tests.

## Relationship to prior work
Mugnolo's 2012 work develops nonlinear graph \(p\)-heat semigroups, positivity, and contraction in vertex sequence norms; Hua and Mugnolo's 2014 work gives further regularity and long-time theory for such graph flows. Vertex \(\ell^q\) contractivity does not settle weighted \(\ell^1\) variation of their *edge gradients*. The present result classifies the latter property above the precise six-edge threshold. The sign-chamber comparison independently confirms a nonuniform six-cycle contractive example at the linear exponent, while demonstrating that superquadratic generators rule it out.

## Limitations
Only unit heat conductances and vertex masses, strictly positive independent variation weights, simple cycles, and exponents \(p>2\) are covered. The result does not classify nonuniform weights at \(n\le5\), treat \(1<p<2\), or address non-cycle graphs, weighted heat conductances, two-input Lipschitz constants, or exact worst-case positive-time amplification. The originality assessment has residual risk from older work on weighted dissipativity of nonlinear diffusion equations, particularly if formulated in edge variables rather than graph-variation language.

## References
- D. Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, first posted 2012-07-09, arXiv:1207.1996 (https://arxiv.org/abs/1207.1996). Material inspected: article text, introduction and nonlinear semigroup theorems.
- B. Hua and D. Mugnolo, *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs*, first posted 2014-10-06, arXiv:1410.1584 (https://arxiv.org/abs/1410.1584). Material inspected: original PDF, introduction, graph operator definition and main theorems.
