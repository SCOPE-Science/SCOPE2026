# An exact Pontryagin curvature obstruction to greedy Kuramoto synchronization

## Finding
For three identical all-to-all Kuramoto oscillators with an instantaneous Euclidean control budget, greedy order-parameter ascent is strictly slower than an admissible minimum-time control from an open dense set of regular configurations, for every nonnegative coupling \(K\) and every positive power \(P\), provided the synchronization threshold is sufficiently close above the initial order parameter. More precisely, put \(f(\theta)=|\frac13\sum_{j=1}^{3}e^{i\theta_j}|^2\), \(g=\nabla f\), and \(H=\nabla^2f\). At any state with \(g\ne0\) and \(g\times Hg\ne0\), greedy control is not minimum-time for all sufficiently nearby larger target values of \(\sqrt f\). The set of such initial states is open dense in the phase three-torus. At the explicit state \(\theta^\circ=(0,\pi/2,2\pi/3)\), the failure has the exact nonvanishing certificate
\[
 g(\theta^\circ)\times H(\theta^\circ)g(\theta^\circ)=-\frac{3+\sqrt3}{729}(1,1,1).
\]
This is an analytic, parameter-uniform obstruction, not a calculation of the optimal control or of the numerical improvement in arrival time.

## Assumptions and scope
There are exactly three identical phase oscillators, with phases \(\theta\in\mathbb T^3\) and measurable controls \(u(t)\in\mathbb R^3\) satisfying \(\|u(t)\|_2\le\sqrt P\) almost everywhere, where \(P>0\). Their dynamics are
\[
\dot\theta_i=\frac K3\sum_{j=1}^{3}\sin(\theta_j-\theta_i)+u_i,\qquad K\ge0.
\]
For a target \(r_\star\in(0,1)\), arrival time is the first time \(r(\theta)=\sqrt{f(\theta)}\ge r_\star\). The greedy law at regular states is \(u_{\rm gr}=\sqrt P\,g/\|g\|_2\); it is equivalent to ascending \(r\), since \(\nabla r=g/(2r)\) when \(r>0\). No assertion is made for remote target values or at singular states \(g=0\).

## Proof
Write \(U=\sqrt P>0\) and \(c=3K/2\). Elementary differentiation yields
\[
 f(\theta)=\frac{3+2\sum_{i<j}\cos(\theta_i-\theta_j)}9,\qquad
 g_i=\frac29\sum_j\sin(\theta_j-\theta_i),\qquad \dot\theta=cg+u.
\]
On a regular greedy segment the state therefore satisfies \(\dot\theta=(c+U/\|g\|)g\), with \(\dot f=c\|g\|^2+U\|g\|>0\). Standard ODE continuity gives, for each regular initial condition, a small positive target increment that is reached by the greedy flow without encountering \(g=0\).

Suppose such a greedy segment is minimum-time. The smooth autonomous minimum-time problem with compact ball-valued controls satisfies the Pontryagin maximum principle, including the abnormal case. There is a nowhere-zero absolutely continuous adjoint \(p(t)\) satisfying \(\dot p=-cH(\theta(t))p\). Pointwise maximization of \(p\cdot u\) on the Euclidean ball gives uniquely \(u=Up/\|p\|\). Because this equals greedy, \(p=\lambda g\) for some positive scalar \(\lambda(t)\). Taking the derivative along the greedy trajectory gives
\[
 \lambda' g+\lambda(c+U/\|g\|)Hg=-c\lambda Hg,
\]
thus
\[
 \lambda'g+\lambda(2c+U/\|g\|)Hg=0.
\]
Since \(2c+U/\|g\|>0\), necessarily \(Hg\) is collinear with \(g\) at every point of the segment, including its initial point. Hence \(g\times Hg\ne0\) contradicts minimum-time optimality. The existence of some minimum-time control follows from compactness of the torus, uniform speed bounds, convex compact control ball, affine control dependence, and an already feasible greedy trajectory; any infimizing sequence admits a uniformly convergent state subsequence with a weakly convergent bounded-control limit. Thus exclusion of greedy from the minimizers implies strict suboptimality, not merely absence of a formal multiplier.

For the exact witness, direct trigonometric differentiation at \(\theta^\circ=(0,\pi/2,2\pi/3)\) gives
\[
 f(\theta^\circ)=\frac{2+\sqrt3}9,\quad
 g(\theta^\circ)=\frac19(2+\sqrt3,-1,-1-\sqrt3),
\]
\[
 H(\theta^\circ)g(\theta^\circ)=\frac1{81}(3+2\sqrt3,-3,-2\sqrt3).
\]
The displayed cross product follows. Its components are nonzero. Each component of \(g\times Hg\) is a real-analytic function on connected \(\mathbb T^3\). A nontrivial real-analytic function has a zero set with empty interior, so the nonzero locus of this cross product is open dense. At every point of that locus \(g\ne0\), proving the stated generic result.

## Verification
The accompanying `verify.py` symbolically differentiates the exact trigonometric objective, verifies the drift-gradient normalization and witness vector identities, and verifies the nonzero cross product. Its execution succeeds with Python 3 and SymPy. The topological density step uses the standard identity theorem for real-analytic functions; no finite numerical sampling is used to infer density or optimality.

## Relationship to prior work
O'Keeffe, *Learning to Synchronize in Minimum Time*, arXiv:2608.10354v1 (first posted 11 August 2026), Sections II, III and VII, defines this controlled Kuramoto model, proves the greedy gradient-flow identity, and reports numerical dynamic-programming evidence of greedy suboptimality for three and four oscillators. It already identifies qualitative generic failure of greedy ascent; that qualitative observation is not claimed as new here. The present contribution is the explicit Pontryagin curvature criterion, exact symbolic three-oscillator witness, open-dense analytic deduction, and proof uniform over all \(K\ge0\) and \(P>0\) for nearby target levels. Standard Pontryagin necessary conditions and real-analytic zero-set facts are used as established theory rather than novel lemmas.

## Limitations
This gives a necessary obstruction and strict nonoptimality, not the optimal policy, a positive quantified arrival-time gap, or a global statement for an arbitrary prescribed distant synchronization target. The target increment may depend on the initial configuration, coupling, and power. The statement is about three identical all-to-all oscillators and an instantaneous \(\ell^2\) control ball, not arbitrary oscillator networks. The motivating paper already suggests generic failure; independent historical-priority review of similar control-geometric criteria remains appropriate.

## References
1. K. P. O'Keeffe, *Learning to Synchronize in Minimum Time*, arXiv:2608.10354v1, 11 August 2026, https://arxiv.org/html/2608.10354v1 .
2. L. S. Pontryagin et al., *The Mathematical Theory of Optimal Processes*, standard maximum-principle formulation for minimum-time controlled ODEs.
