# A scalar Gaussian counterexample to convexity of the joint chance-constrained LCP feasible set
## Finding
For the joint chance-constrained linear complementarity model of Henrion--Schmidt, take dimension \(n=1\), deterministic \(M=1\), uncertainty \(q^{\xi}\sim\mathcal N(0,1)\), and probability level \(p=1/2\). Let \(F\) be the feasible set in variables \(z\ge0\) and \(\rho\ge0\) defined by \[\mathbb P\!\left(q^{\xi}+z\ge0,\;z(q^{\xi}+z)\le\rho\right)\ge\tfrac12.\] Then \(F\) is not convex. More precisely, \((0,0)\in F\), while for every \(z>0\) the smallest feasible relaxation is \[g(z)=z\left[z+\Phi^{-1}\!\left(\tfrac12+\Phi(-z)\right)\right],\] where \(\Phi\) is the standard normal distribution function. Since \(g(z)/z\to+\infty\) as \(z\downarrow0\) but \(g(z_0)/z_0\) is finite for every fixed \(z_0>0\), the line segment from \((0,0)\) to any boundary point \((z_0,g(z_0))\) leaves \(F\) for all sufficiently small positive interpolation factors. Thus the source model can have a nonconvex feasible set even with a positive-definite deterministic LCP matrix and Gaussian uncertainty. The claim is limited to this exact joint model at \(p=1/2\); it does not assert nonconvexity for \(p>1/2\).

## Assumptions and scope
Consider the joint model
\\[
 z\\ge0,\\qquad \\rho\\ge0,\\qquad \\mathbb P\\!\\left(q^{{\\xi}}+Mz\\ge0,\\;z(q^{{\\xi}}+Mz)\\le\\rho\\right)\\ge p.
\\]
Set \\(n=1\\), \\(M=1\\), \\(q^{{\\xi}}\\sim\\mathcal N(0,1)\\), and \\(p=1/2\\). These parameters are permitted by the source formulation: the matrix is deterministic and positive definite, the uncertainty is regular Gaussian, and the probability level belongs to the stated interval \\((0,1]\\). The conclusion concerns the global feasible set in \\((z,\\rho)\\); it does not address levels strictly above \\(1/2\\).

## Proof
At \\((z,\\rho)=(0,0)\\), the event reduces to \\(q^{{\\xi}}\\ge0\\), which has probability exactly \\(1/2\\). Hence \\((0,0)\\) is feasible.

Fix \\(z>0\\). The two random inequalities are equivalent to
\\[
 -z\\le q^{{\\xi}}\\le \\frac{\\rho}{z}-z.
\\]
Therefore the feasibility probability is
\\[
 \\Phi\\!\\left(\\frac{\\rho}{z}-z\\right)-\\Phi(-z).
\\]
Because \\(z>0\\), one has \\(0<\\Phi(-z)<1/2\\), so \\(1/2+\\Phi(-z)\\in(1/2,1)\\). Strict monotonicity of \\(\\Phi\\) shows that the least feasible relaxation is exactly
\\[
 g(z)=z\\left[z+\\Phi^{{-1}}\\!\\left(\\tfrac12+\\Phi(-z)\\right)\\right].
\\]
In particular, \\((z,g(z))\\) is feasible for every \\(z>0\\).

As \\(z\\downarrow0\\), continuity of \\(\\Phi\\) gives \\(1/2+\\Phi(-z)\\uparrow1\\). Hence
\\[
 \\Phi^{{-1}}\\!\\left(\\tfrac12+\\Phi(-z)\\right)\\longrightarrow+\\infty,
\\]
and consequently
\\[
 \\frac{{g(z)}}{z}=z+\\Phi^{{-1}}\\!\\left(\\tfrac12+\\Phi(-z)\\right)\\longrightarrow+\\infty.
\\]
Choose any fixed \\(z_0>0\\). The number \\(g(z_0)/z_0\\) is finite, so there exists \\(t\\in(0,1)\\) such that
\\[
 \\frac{{g(tz_0)}}{tz_0}>\\frac{{g(z_0)}}{z_0}.
\\]
Equivalently, \\(g(tz_0)>t g(z_0)\\). The two endpoints \\((0,0)\\) and \\((z_0,g(z_0))\\) are feasible, but their convex combination \\((tz_0,tg(z_0))\\) is not, because its relaxation lies strictly below the least feasible value \\(g(tz_0)\\). Thus \\(F\\) is not convex.

## Verification
The proof uses only the one-dimensional Gaussian CDF and its strict monotonicity. The endpoint \\((0,0)\\) is checked separately because the source notes that the joint probability function can be exceptional there. For \\(z>0\\), the interval event is obtained by dividing the complementarity inequality by the positive scalar \\(z\\), so no sign reversal or hidden branch is present. The inverse-CDF argument is valid because its argument lies strictly between \\(1/2\\) and \\(1\\).

As a non-proof numerical illustration, choosing \\((z,\\rho)=(1,1.41)\\) gives joint probability about \\(0.50044\\), whereas the one-tenth point \\((0.1,0.141)\\) gives about \\(0.44473\\). The analytical limit argument above, not these decimal evaluations, proves nonconvexity.

## Relationship to prior work
Henrion and Schmidt introduce the joint chance-constrained LCP model, prove continuity, compactness, existence, and differentiability properties, and prove convexity only for an equivalent formulation of the separate-chance model under Gaussian uncertainty and positive-semidefinite \\(M\\). Their conclusion explicitly leaves convexity of the joint feasible set as an open question. The present scalar construction gives a negative answer to universal convexity of that joint model.

Earlier chance-complementarity work in contact-rich control uses a different dynamic formulation and replaces the difficult joint constraints by conservative decompositions. Classical joint chance-constrained programming literature contains nonconcavity phenomena for other models, but those statements do not imply the source-specific complementarity construction above. The counterexample depends on the exact coupling of nonnegativity and relaxed complementarity in the joint LCP event.

## Limitations
The mechanism uses the canonical level \\(p=1/2\\) and the feasible exceptional point \\((0,0)\\). No claim is made that the same feasible set is nonconvex for every \\(p>1/2\\), or that nonconvexity persists after excluding a neighborhood of the origin. The finding is a global counterexample to universal convexity, not a characterization of all parameter regimes. It also does not alter the source's convexity result for the separate-chance formulation.

## References
René Henrion and Martin Schmidt, “Chance-Constrained Linear Complementarity Problems,” Optimization Online, first published 2026-03-03 and updated 2026-07-28, Optimization Online record 33820.

Yuki Shirai, Devesh K. Jha, Arvind U. Raghunathan, and Diego Romeres, “Chance-Constrained Optimization in Contact-rich Systems,” American Control Conference, 2023, DOI: 10.23919/ACC55779.2023.10156516.

Bruce L. Miller and Harvey M. Wagner, “Chance Constrained Programming with Joint Constraints,” Operations Research 13(6), 1965, DOI: 10.1287/opre.13.6.930.
