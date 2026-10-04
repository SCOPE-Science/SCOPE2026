# A two-step Q-linear law and a sharp one-step normal threshold for GDPolyak on quartic Rosenbrock ravines

## Finding
For every \(a>0\), consider
\[
f_a(x,y)=x^4+a(y-x^2)^2,
\]
whose minimizer is the origin, and Algorithm 1 of Davis--Drusvyatskiy--Jiang with the exact optimal value \(f^*=0\). Set the short gradient-descent stepsize to the reciprocal normal curvature
\[
h=\frac{1}{2a}.
\]
Write \(n=y-x^2\). For any fixed \(C>0\), there is \(\delta>0\) such that every start satisfying \(0<|x_0|<\delta\) and \(|n_0|\le Cx_0^2\) has the following local behavior.

With two short steps per epoch, followed by one Polyak step, the method is Q-linearly convergent for every \(a>0\). If \((\widetilde x_m,\widetilde y_m)\) denotes the state after the two short steps and immediately before the Polyak step, then
\[
\frac{\widetilde y_m-\widetilde x_m^2}{\widetilde x_m^4}\to\frac{4}{a},\qquad
\frac{|\widetilde x_{m+1}|}{|\widetilde x_m|}\to\frac34,
\]
and therefore
\[
\frac{\|\widetilde z_{m+1}\|_2}{\|\widetilde z_m\|_2}\to\frac34,
\qquad
\frac{f_a(\widetilde z_{m+1})}{f_a(\widetilde z_m)}\to\left(\frac34\right)^4=\frac{81}{256}.
\]
The same distance and objective ratios hold at the epoch boundaries after the Polyak steps.

The one-short-step block has an exact complementary normal-mode law. For the epoch-boundary scaled normal coordinate
\[
u_m=\frac{y_m-x_m^2}{x_m^2},
\]
whenever \(u_m\) stays bounded,
\[
u_{m+1}=\frac{8a}{9}u_m-\frac19+O(x_m^2),
\qquad
x_{m+1}=\frac34x_m+O(x_m^3).
\]
Thus the ravine-scaled normal mode is locally attracting exactly for \(0<a<9/8\), with limiting value \(u_*=-1/(9-8a)\); at \(a=9/8\) the leading map has unit multiplier and nonzero drift, and for \(a>9/8\) its finite fixed point is repelling. In particular, the nonconvex quartic used numerically in the 2026 follow-up is orthogonally equivalent to the case \(a=1/2\), where the normal multiplier is \(4/9\); the original Rosenbrock benchmark has \(a=10\), where two curvature-matched short steps remove this one-step normal instability and still give the exact tangential factor \(3/4\).

## Assumptions and scope
The result concerns the explicit two-variable quartic family above and the known-optimum GDPolyak update. It is local: the initial point must lie in a fixed parabolic wedge \(|y-x^2|\le Cx^2\) and sufficiently near the origin. The short step is fixed at \(h=1/(2a)\). The sharp threshold \(a=9/8\) describes attraction of the scaled normal coordinate for the one-short-step block; it is not claimed to be an if-and-only-if criterion for Euclidean convergence from arbitrary starts. The two-short-step conclusion is robust for every fixed \(a>0\) within the stated local wedge.

## Proof
The gradient is
\[
\nabla f_a(x,y)=\bigl(4x^3-4axn,\;2an\bigr),\qquad n=y-x^2.
\]
For one short step with \(h=1/(2a)\), the new vertical coordinate is exactly \(y^+=x^2\), while
\[
x^+=x\left(1+2n-\frac{2x^2}{a}\right).
\]
Consequently the new normal residual satisfies the exact identity
\[
n^+=-4x^2n+\frac{4}{a}x^4-4x^2\left(n-\frac{x^2}{a}\right)^2.
\]
If \(n=ux^2\) with bounded \(u\), then
\[
x^+=x\bigl(1+O(x^2)\bigr),\qquad
n^+=x^4\left(\frac4a-4u\right)+O(x^6).
\]
Applying the same short step once more to a state with normal residual \(O(x^4)\) gives
\[
n^{++}=\frac4a(x^{++})^4+O((x^{++})^6).
\]
Thus two short steps reset the leading normal coefficient to \(4/a\), independently of the incoming bounded scaled normal coordinate.

Now consider a pre-Polyak state with
\[
n=cx^4+O(x^6),
\]
where \(c\) is bounded. The Polyak stepsize \(\alpha=f_a/\|\nabla f_a\|_2^2\) has expansion
\[
\alpha=\frac{1}{16x^2}\left[1+\left(2ac-\frac{a^2c^2}{4}\right)x^2+O(x^4)\right].
\]
Writing the post-Polyak point as \((X,Y)\) and \(N=Y-X^2\), direct substitution yields
\[
X=\frac34x+O(x^3),
\qquad
N=\left(\frac7{16}-\frac{ac}{8}\right)x^2+O(x^4).
\]
Since two short steps give \(c=4/a+O(x^2)\), this becomes
\[
\frac{N}{X^2}=-\frac19+O(x^2).
\]
The post-Polyak state therefore returns to a bounded parabolic wedge. The next pair of short steps resets the pre-Polyak normal coefficient to \(4/a+O(x^2)\), and the epoch map obeys
\[
x_{m+1}=\frac34x_m+O(x_m^3).
\]
After shrinking the neighborhood if necessary, this is a contraction, so the iterates remain in the wedge and converge to the origin. Dividing by \(x_m\) gives the Q-factor \(3/4\). At pre-Polyak states, \(y=x^2+O(x^4)\), hence \(\|z\|_2=|x|(1+O(x^2))\) and \(f_a(z)=x^4(1+O(x^4))\), which gives the displayed norm and objective ratios. The same argument applies to epoch-boundary states because their scaled normal coordinate converges to a finite limit.

For one short step, the pre-Polyak normal coefficient is instead
\[
c=\frac4a-4u+O(x^2).
\]
Combining this with the post-Polyak expansion gives
\[
u^+=\frac{7-2ac}{9}+O(x^2)=\frac{8a}{9}u-\frac19+O(x^2).
\]
Its linear multiplier is \(8a/9\). When \(0<a<9/8\), the affine leading map is a contraction with fixed point \(u_*=-1/(9-8a)\), while the perturbation \(O(x_m^2)\) is summable because \(|x_m|\) contracts asymptotically by \(3/4\). At \(a=9/8\) the leading map is \(u\mapsto u-1/9\); for \(a>9/8\), the finite fixed point has multiplier larger than one. This proves the stated sharp normal-mode threshold.

## Verification
The accompanying `verify.py` evaluates the exact gradient, the curvature-matched short step, and the Polyak step without using any asymptotic formulas. For the reflected 2026 nonconvex quartic \(a=1/2\) with one short step, it checks convergence of the scaled normal coordinate to \(-1/5\) and of the epoch ratio to \(3/4\). For the original Rosenbrock coefficient \(a=10\) with two short steps, it checks convergence of the pre-Polyak coefficient to \(2/5\), the post-Polyak scaled normal coordinate to \(-1/9\), and the epoch ratio to \(3/4\). These numerical checks replay the algebraic asymptotics; they are not used as proof.

## Relationship to prior work
Davis, Drusvyatskiy, and Jiang introduced GDPolyak as an alternation of \(K\) fixed short gradient steps and one Polyak step. Their canonical motivating example is \(x^4+10(y-x^2)^2\); their displayed experiment uses \(K=100\) and short stepsize \(0.0125\). Their general theorem proves a nearly linear local rate with the bound depending on \(\min\{K,I\}\), and obtains \(O(\log^2(1/\varepsilon))\) oracle complexity by choosing both \(K\) and the number of epochs proportional to \(\log(1/\varepsilon)\). With fixed \(K=2\), that generic bound alone does not imply convergence to arbitrary accuracy.

The 2026 follow-up by Davis and Drusvyatskiy gives a shorter Lyapunov proof under convexity and proposes a more adaptive rule. Its publicly rendered Figure 3 also reports a numerical GDPolyak baseline with short stepsize \(1\) and block length \(1\) on the nonconvex quartic \(\tfrac12(v+u^2)^2+u^4\), which is the present family with \(a=1/2\) after the orthogonal reflection \(y=-v\). The present calculation supplies an exact explanation of that one-step numerical stability through the multiplier \(4/9\), and at the same time identifies the sharp normal-mode boundary \(a=9/8\) and proves that two curvature-matched short steps recover a strict Q-linear law for every \(a>0\). No exact statement of these constants or this threshold was located in the inspected sources or targeted searches.

## Limitations
The theorem is model-specific and local. It does not assert that two short steps suffice for general fourth-order-growth objectives, nor that \(h=1/(2a)\) is globally safe. The one-step threshold is a threshold for the ravine-scaled normal mode, not a global convergence classification. A verified full PDF of the April 2026 follow-up could not be obtained through the available open and institutional routes; its abstract and publicly rendered figures were inspected, so an unobserved derivation in that manuscript remains a literature risk. Search failure is not treated as proof of historical priority.

## References
1. D. Davis, D. Drusvyatskiy, and L. Jiang, “Gradient descent with adaptive stepsize converges (nearly) linearly under fourth-order growth,” *Mathematical Programming* (2025), DOI: 10.1007/s10107-025-02290-5; arXiv:2409.19791.
2. D. Davis and D. Drusvyatskiy, “A short proof of near-linear convergence of adaptive gradient descent under fourth-order growth and convexity,” arXiv:2604.13393 (2026).
