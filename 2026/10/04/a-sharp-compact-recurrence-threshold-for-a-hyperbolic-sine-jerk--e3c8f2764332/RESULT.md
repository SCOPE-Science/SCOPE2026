# A sharp compact-recurrence threshold for a hyperbolic-sine jerk flow
## Finding
Consider the symmetric hyperbolic-sine jerk flow
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=-a x-b^2y-cz+d\sinh x,
\]
with \(b>0\), \(c>0\), and \(d>0\). A compact invariant set not contained in the origin exists if and only if \(a>d\).

More explicitly, if \(a\le d\), every bounded forward trajectory converges to \((0,0,0)\); every bounded complete trajectory is identically \((0,0,0)\); and every compactly supported invariant probability measure is the point mass \(\delta_{(0,0,0)}\). If \(a>d\), there is a unique \(x_0>0\) with
\[
\frac{\sinh x_0}{x_0}=\frac ad,
\]
and \((x_0,0,0)\) and \((-x_0,0,0)\) are nonzero equilibria. Thus the threshold \(a=d\) is sharp for the existence of nontrivial compact recurrent dynamics.

## Assumptions and scope
The vector field is the symmetric family studied by Hu, Sang, and Wang after setting the symmetry-breaking parameter to zero. The assumptions here are \(b>0\), \(c>0\), \(d>0\), and arbitrary real \(a\). A “compact invariant set” means a compact set invariant under the full flow; hence every point in such a set lies on a bounded complete trajectory.

The conclusion is conditional on boundedness for individual forward trajectories. It does not claim that every solution is globally bounded, nor that the origin is Lyapunov stable throughout \(a\le d\). The source's local stability and bifurcation analysis is therefore logically distinct from the global bounded-recurrence statement proved here.

## Proof
Define
\[
P(x,y,z)=xz-\frac12y^2+cxy+\frac12b^2x^2.
\]
Differentiating along the flow gives
\[
\begin{aligned}
\dot P
&=y z+x\dot z-y z+c(y^2+xz)+b^2xy\\
&=-a x^2+c y^2+d\,x\sinh x\\
&=c y^2+(d-a)x^2+d\,x(\sinh x-x).
\end{aligned}
\]
For real \(x\),
\[
x(\sinh x-x)=\sum_{n=1}^\infty \frac{x^{2n+2}}{(2n+1)!}\ge0,
\]
with equality exactly at \(x=0\). Hence, when \(a\le d\),
\[
W:=\dot P\ge0,
\]
and \(W=0\) exactly when \(x=y=0\).

Let a forward trajectory be bounded. Then \(P(t)\) is bounded and nondecreasing, so it has a finite limit and
\[
\int_0^\infty W(t)\,dt<\infty.
\]
On a bounded trajectory, \(W(x(t),y(t))\) has bounded time derivative, because \(W\) is smooth and \(x,y,z\) remain bounded. Thus \(W\) is uniformly continuous. Barbalat's lemma gives \(W(t)\to0\). The strict zero set above then gives \(x(t)\to0\) and \(y(t)\to0\). Since \(z=\dot y\) and \(\dot z\) is bounded on the bounded trajectory, \(z\) is uniformly continuous; the standard derivative form of Barbalat's lemma applied to the convergent function \(y(t)\) yields \(z(t)\to0\). Therefore every bounded forward trajectory converges to the origin.

Now let a trajectory be bounded for all \(t\in\mathbb R\). The same argument at \(+\infty\) gives \(P(t)\to0\). Since \(P\) is bounded and nondecreasing, it also has a finite limit at \(-\infty\), and
\[
\int_{-\infty}^0 W(t)\,dt<\infty.
\]
Uniform continuity gives \(W(t)\to0\) as \(t\to-\infty\), hence \(x,y,z\to0\) there as well and \(P(t)\to0\). A nondecreasing function with equal limits \(0\) at both ends is constant, so \(W\equiv0\). Therefore \(x=y=0\), and \(z=\dot y=0\): the complete trajectory is the origin. It follows immediately that every compact invariant set is contained in the origin.

For a compactly supported invariant probability measure \(\mu\), invariance also gives the stationary coboundary identity
\[
0=\int \dot P\,d\mu=\int W\,d\mu.
\]
When \(a\le d\), nonnegativity forces \(x=y=0\) on the support; invariance then forces \(z=0\). Hence \(\mu=\delta_{(0,0,0)}\).

It remains to prove sharpness. For \(a>d\), equilibria satisfy \(y=z=0\) and
\[
d\sinh x=a x.
\]
For \(x>0\), set \(r(x)=\sinh x/x\). Then \(r(x)\to1\) as \(x\downarrow0\), \(r(x)\to\infty\) as \(x\to\infty\), and
\[
r'(x)=\frac{x\cosh x-\sinh x}{x^2}>0,
\]
because the numerator vanishes at \(0\) and has derivative \(x\sinh x>0\) for \(x>0\). Since \(a/d>1\), there is a unique \(x_0>0\) with \(r(x_0)=a/d\). Odd symmetry gives the second equilibrium at \(-x_0\), proving existence of nontrivial compact invariant sets.

## Verification
The accompanying `verify.py` symbolically differentiates \(P\), substitutes the vector field, and checks the exact factorization of \(\dot P\). It also checks the equilibrium residual at a symbolic root relation. The decisive recurrence argument is analytic: positivity of \(x(\sinh x-x)\), bounded monotonicity of \(P\), uniform continuity, and the sharp monotonicity of \(\sinh x/x\).

## Relationship to prior work
Hu, Sang, and Wang introduce this symmetric jerk family, derive its equilibria, and identify \(a=d\) as the pitchfork surface for \(d>0\); they also give local stability and Hopf conditions. Their source analysis is local/bifurcation-oriented. The present result uses an exact coboundary not used there to show that the same pitchfork surface is the exact global threshold for any nontrivial compact invariant dynamics.

A later paper by Li, Sang, Liu, Hu, Zhang, and Wang studies hidden chaotic dynamics in related jerk systems. Accessible publisher material and targeted searches did not reveal the compact-recurrence theorem above for this exact hyperbolic-sine family. Because the complete later full text was not available in the material inspected, that literature comparison retains a residual access risk.

published-finding corpus searches for the exact vector field, the threshold \(a=d\), invariant-measure formulations, and the displayed coboundary returned only analogous results for other flows, not an implication covering this theorem.

## Limitations
The theorem says nothing about the fate of unbounded trajectories. It does not classify the dynamics for \(a>d\) beyond proving that nonzero equilibria exist, and it does not establish chaos, periodic orbits, or attractors there. The novelty assessment is based on the inspected primary source, accessible material from the closest later paper, targeted web searches, and published-finding corpus searches; it is not a proof that no unindexed source contains an equivalent statement.

## References
1. X. Hu, B. Sang, and N. Wang, “The chaotic mechanisms in some jerk systems,” *AIMS Mathematics* 7(9) (2022), 15714–15740, DOI: 10.3934/math.2022861. Published June 24, 2022; a public preprint record for the same work was uploaded October 6, 2021.
2. C. Li, B. Sang, Y. Liu, X. Hu, X. Zhang, and N. Wang, “Some Jerk Systems with Hidden Chaotic Dynamics,” *International Journal of Bifurcation and Chaos* 33 (2023), DOI: 10.1142/S0218127423500694.
