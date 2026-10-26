# A sharp finite-epoch sampling reversal in strongly convex-concave descent-ascent

## Finding
Consider simultaneous stochastic gradient descent-ascent (SGDA), using exactly two successive component evaluations, on the average of the two quadratic saddle objectives
\[
f_1(x,y)=\frac a2x^2-\frac b2y^2,\qquad
f_2(x,y)=\frac a2x^2-\frac b2y^2+cxy,
\]
where \(0<a<b\) and \(c\ne0\). Both components and their average are strongly convex in \(x\) and strongly concave in \(y\); the common unique saddle is the origin. Use the *same* step size \(h>0\) in descent and ascent. Let \(R_{\rm RR}(z;h)\) be the expected squared Euclidean distance to the saddle after processing each component once in a uniformly random order; let \(R_{\rm IID}(z;h)\) be the same quantity after two independent uniform component selections, with replacement, starting from \(z=(x,y)^\mathsf T\).

For every \(h>0\) and every \(z\in\mathbb R^2\), the exact difference is
\[
\boxed{R_{\rm IID}(z;h)-R_{\rm RR}(z;h)=
\frac{c^2h^3}{4}\left[
\left(\bigl(2a(b-a)+c^2\bigr)h-2(b-a)\right)x^2
+\left(2(b-a)(1-bh)+c^2h\right)y^2\right].}
\]
In particular, within \(0<h<1/b\), the coefficient of \(y^2\) is strictly positive, while the coefficient of \(x^2\) changes sign exactly at
\[
\boxed{h_*=\frac{2(b-a)}{2a(b-a)+c^2}.}
\]
Thus, if \(h<h_*\), reshuffling has **larger** two-update squared error for the initial direction \(z=(1,0)^\mathsf T\), but **smaller** error for \(z=(0,1)^\mathsf T\). When \(h_*<1/b\) (equivalently \(c^2>2(b-a)^2\)), reshuffling weakly dominates IID for **every** initial vector exactly on \(h_*\le h<1/b\), with strict dominance away from the first coordinate axis at equality. Below \(h_*\), neither strategy uniformly dominates across initial directions. At every fixed \(a<b\) and \(c\ne0\), failure of reshuffling domination occurs for arbitrarily small \(h>0\), despite each component having the same saddle.

The phenomenon occurs with strictly contracting component steps and within the standard SGDA component-Lipschitz step restriction. For \(a=1\), \(b=3/2\), \(c=2\), the sharp crossover is \(h_*=1/5\). The diagonal risk-difference matrices \(\mathcal D(h)\), defined by \(R_{\rm IID}-R_{\rm RR}=z^\mathsf T\mathcal D(h)z\), satisfy
\[
\mathcal D(1/10)=\operatorname{diag}(-1/2000,1/800),\quad
\mathcal D(1/5)=\operatorname{diag}(0,3/250),\quad
\mathcal D(1/4)=\operatorname{diag}(1/256,13/512).
\]
At both \(h=1/10\) and \(h=1/4\), the two individual update maps are strict Euclidean contractions. Consequently *smaller* admissible steps allow a directional reshuffling disadvantage, while a *larger* admissible step restores reshuffling dominance for every initial vector in the same fixed problem.

## Assumptions and scope
All statements concern exact arithmetic, real scalar decision variables \(x\) (minimized) and \(y\) (maximized), two fixed components, one two-evaluation epoch, no regularization, and simultaneous descent-ascent with a common positive step size. Sampling choices are uniform: reshuffling chooses the two orders with probability \(1/2\) each, while IID chooses each of four ordered pairs with probability \(1/4\). The expected loss is the **squared Euclidean distance to the common saddle**, not the signed saddle objective, duality gap, asymptotic rate, or expected norm without squaring. The displayed identities hold for all positive \(h\); the claimed sharp ordering interpretation is restricted to \(0<h<1/b\). No assumption of commutation or normality is made.

## Proof
Put \(\delta=b-a>0\), \(u=1-ah\), \(v=1-bh\), and \(t=ch\). Because descent is in \(x\) and ascent in \(y\), the two simultaneous update matrices are
\[
P=\begin{pmatrix}u&0\\0&v\end{pmatrix},\qquad
Q=\begin{pmatrix}u&-t\\t&v\end{pmatrix}.
\]
In particular, the skew signs in \(Q\) are essential; replacing them by equal signs would describe minimization rather than a saddle operator.

For a given starting vector \(z\), the two risks are the exact finite expectations
\[
R_{\rm RR}=\frac12\left(\|PQz\|_2^2+\|QPz\|_2^2\right),
\qquad
R_{\rm IID}=\frac14\left(\|P^2z\|_2^2+\|Q^2z\|_2^2+\|PQz\|_2^2+\|QPz\|_2^2\right).
\]
The order in each matrix product is immaterial to these expectations because both orders occur equally often. Therefore \(R_{\rm IID}-R_{\rm RR}=z^\mathsf T\mathcal D z\), where
\[
4\mathcal D=(P^2)^\mathsf TP^2+(Q^2)^\mathsf TQ^2-(PQ)^\mathsf T(PQ)-(QP)^\mathsf T(QP).
\]
Direct multiplication gives the exact cancellation of both off-diagonal entries and the diagonal entries
\[
4\mathcal D_{11}=2t^2u(v-u)+t^4,\qquad
4\mathcal D_{22}=2t^2v(u-v)+t^4.
\]
Since \(u-v=\delta h\), substituting \(t=ch\), \(u=1-ah\), and \(v=1-bh\) yields precisely the boxed risk identity. If \(0<h<1/b\), then \(v>0\), so \(4\mathcal D_{22}=2c^2h^3\delta v+c^4h^4>0\). Meanwhile \(\mathcal D_{11}\) changes sign once, from negative to positive, at \(h=h_*\). Hence the all-directions Loewner comparison \(\mathcal D\succeq0\) holds precisely for \(h\ge h_*\) inside that interval. Algebraically, \(h_*<1/b\) if and only if \(c^2>2\delta^2\); when the inequality fails, the all-directions crossover lies outside the stated step interval.

For the rational example, insert \((a,b,c)=(1,3/2,2)\) into the two diagonal formulas. The resulting values are stated in the finding. The operator matrices are \(A=\operatorname{diag}(1,3/2)\) and \(B=\begin{psmallmatrix}1&2\\-2&3/2\end{psmallmatrix}\). The Frobenius bound \(\max(\|A\|_2,\|B\|_2)\le\max(\|A\|_F,\|B\|_F)=\sqrt{45}/2<4\) proves that both displayed steps satisfy the conventional source restriction \(h<1/l\), with \(l=\max(\|A\|_2,\|B\|_2)\). Moreover at \(h=1/4\), the squared-norm defects \(I-P^\mathsf TP\) and \(I-Q^\mathsf TQ\) are positive definite: the former is diagonal with entries \(7/16\) and \(39/64\), while the latter equals \(\begin{psmallmatrix}3/16&1/16\\1/16&23/64\end{psmallmatrix}\), whose leading principal minor and determinant are positive. At \(h=1/10\), the defects are likewise positive definite: \(I-P^\mathsf TP=\operatorname{diag}(19/100,111/400)\) and \(I-Q^\mathsf TQ=\begin{psmallmatrix}3/20&1/100\\1/100&19/80\end{psmallmatrix}\). This certifies that no unstable component update is needed for the reversal.

## Verification
The standalone `verify.py` derives the complete symbolic risk-difference matrix independently from the four path products, compares it with the closed form, and also checks the same identity using rational arithmetic on an independent collection of parameter tuples. It checks the three exact example values and positive definiteness of the individual contraction defects. Execute `python verify.py` with Python 3 and SymPy. The script reports 191 rational assertions in addition to the universal symbolic identity. The algebraic proof above—not finite sampling—establishes the universal claim.

## Relationship to prior work
Das, Schölkopf, and Muehlebach (2022, arXiv:2206.02953) analyze SGDA with reshuffling on strongly convex-strongly concave finite sums, using the same simultaneous component update rule; their main results provide multi-epoch convergence-rate bounds, not an exact comparison between the **two** sampling laws after **two** component evaluations. Cho and Yun (2022, arXiv:2210.05995) analyze asymptotic complexity of SGDA with shuffling, including broader PŁ structures, but do not state this finite-horizon risk matrix or crossover. Emmanouilidis, Vidal, and Loizou (2024, arXiv:2403.07148) analyze **stochastic extragradient**, which evaluates an extrapolated operator and is a different update map. De Sa (2020) constructs larger symmetric-matrix counterexamples to noncommutative reshuffling inequalities, and separately treats small-step superiority for symmetric loss Hessians; those hypotheses exclude the nonsymmetric descent-ascent operator here. Liu (2026, arXiv:2606.32005) establishes rate domination for convex minimization with symmetric gradient operators, not a pointwise saddle-game comparison. This finding does not claim the general observation that reshuffling can sometimes underperform is new; its target is the exact two-component saddle-specific sign matrix and sharp step-size crossover under individually contractive updates.

## Limitations
No conclusion is claimed for longer horizons, different gradient ascent/descent step sizes, constrained games, arbitrary nonlinear objectives, or more than two components. The family assumes a common saddle and identical diagonal curvatures across components, with only the bilinear coupling differing. Expected Euclidean squared saddle error is not a global minimax performance ordering. Literature priority of equivalent specialized calculations outside the inspected materials remains uncertain, and independent validation has not been performed.

## References
- Aniket Das, Bernhard Schölkopf, and Michael Muehlebach, *Sampling without Replacement Leads to Faster Rates in Finite-Sum Minimax Optimization*, arXiv:2206.02953, first submitted 2022-06-07, sections 3 and Appendix C. https://arxiv.org/abs/2206.02953
- Hanseul Cho and Chulhee Yun, *SGDA with shuffling: faster convergence for nonconvex-PŁ minimax optimization*, arXiv:2210.05995, first submitted 2022-10-12. https://arxiv.org/abs/2210.05995
- Konstantinos Emmanouilidis, René Vidal, and Nicolas Loizou, *Stochastic Extragradient with Random Reshuffling: Improved Convergence for Variational Inequalities*, arXiv:2403.07148, first submitted 2024-03-11. https://arxiv.org/abs/2403.07148
- Christopher M. De Sa, *Random Reshuffling is Not Always Better*, NeurIPS 2020, pp. 1–11. https://proceedings.neurips.cc/paper_files/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Paper.pdf
- Zijian Liu, *Random Reshuffling Dominates Stochastic Gradient Descent*, arXiv:2606.32005, first submitted 2026-06-30. https://arxiv.org/abs/2606.32005
