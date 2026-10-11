# Exact threshold drift fixes the positive-quadrant saddle-node orientation
## Finding
Consider the continuous two-patch population model
\[
\dot x_1=-(1+D_1)x_1+D_2x_2,\qquad
\dot x_2=x_2\left(1-x_2-\frac{m}{x_2+a}\right)+D_1x_1-D_2x_2.
\]
Write \(A=1+D_1\) and \(q=1-D_2/A\). Assume \(D_1,D_2,a>0\), \(0<a<q\), and place the system at the critical value \(m=aq\). Define
\[
U(x_1,x_2)=\frac{D_1}{A}x_1+x_2.
\]
Then every classical solution satisfies the exact identity
\[
\dot U=\frac{x_2^2(q-a-x_2)}{x_2+a}.
\]
In particular, no nonzero solution in the nonnegative quadrant converges to \(E_0=(0,0)\). Moreover, the center direction at \(E_0\) points into the positive quadrant and is forward-time repelling. If \(u\) is a center coordinate normalized by \(x_2=u+O(u^2)\), then
\[
\dot u=\kappa u^2+O(u^3),\qquad
\kappa=\frac{A^2(q-a)}{a(A^2+D_1D_2)}>0.
\]
Thus the critical origin is not attracting from the biologically relevant positive side. The sign is important because the source obtains its displayed saddle-node normal form only after a negative rescaling of time; that rescaling reverses forward-time stability.

## Assumptions and scope
The statement concerns the printed continuous model with \(D_1,D_2,a>0\), \(q=1-D_2/(1+D_1)\), \(0<a<q\), and \(m=aq\). The restriction \(0<a<q\) is the parameter regime in which the source's Theorem 2.3(ii) places the origin at the critical boundary while retaining a positive equilibrium. No claim is made for \(a\ge q\), for the positive saddle-node \(E_3\) at \(m=m^*\), or for discrete patch models.

## Proof
At \(m=aq\), direct differentiation of \(U\) gives
\[
\begin{aligned}
\dot U
&=\frac{D_1}{A}\bigl(-Ax_1+D_2x_2\bigr)
+x_2\left(1-x_2-\frac{aq}{x_2+a}\right)+D_1x_1-D_2x_2\\
&=x_2\left(q-x_2-\frac{aq}{x_2+a}\right)
=\frac{x_2^2(q-a-x_2)}{x_2+a}.
\end{aligned}
\]
Suppose a nonzero nonnegative solution converged to \(E_0\). Positivity of the off-diagonal couplings implies \(x_2(t)>0\) for all sufficiently large \(t\). Since \(q-a>0\), convergence would also give \(x_2(t)<q-a\) eventually. The identity would then make \(U(t)>0\) nondecreasing for all sufficiently large \(t\), contradicting \(U(t)\to0\).

The Jacobian at the origin is
\[
J_0=\begin{pmatrix}
-A&D_2\\
D_1&-D_1D_2/A
\end{pmatrix}.
\]
It has eigenvalues \(0\) and \(-(A+D_1D_2/A)\). A right zero eigenvector is \(v=(D_2/A,1)^T\), which lies strictly inside the positive cone. A left zero eigenvector is \(w=(D_1/A,1)^T\). The only quadratic term contributing along \(v\) is in the second component and has coefficient \((q-a)/a\). Normalizing the center amplitude by \(x_2=u+O(u^2)\), projection with \(w\) yields
\[
\kappa=\frac{(q-a)/a}{w^Tv}
=\frac{A^2(q-a)}{a(A^2+D_1D_2)}>0.
\]
Hence positive \(u\) moves away from the origin in forward physical time.

The source introduces a new time variable with a strictly negative proportionality factor before assigning the saddle-node stability type. A negative time change preserves orbit geometry but reverses attraction and repulsion. The positive sign of \(\kappa\), together with the exact \(U\)-identity, fixes the forward-time orientation without relying on nomenclature.

## Verification
The algebra was independently recomputed from the printed vector field. The cancellation of all linear terms in \(\dot U\) uses only \(m=aq\) and \(q=1-D_2/A\). The zero eigenvectors satisfy \(J_0v=0\) and \(w^TJ_0=0\) exactly, and projection of the quadratic term gives the displayed positive coefficient. For the source's Figure 1(b) parameters \(D_1=0.6\), \(D_2=0.5\), \(a=0.18\), one obtains \(q=0.6875\), \(m=0.12375\), \(q-a=0.5075\), and \(\kappa\approx2.5236985237>0\); the plotted arrows on the positive center branch point away from the origin, consistent with the calculation.

## Relationship to prior work
Chen, Liu, and Chen introduce the model, identify the zero eigenvalue at \(m=a(1-D_2/(1+D_1))\), and label \(E_0\) an attracting saddle-node. In their reduction they explicitly replace physical time by a negative multiple of time before applying the saddle-node classification. Their later Corollary 2.1 instead treats \(E_0\) as unstable in the first quadrant and concludes global attraction of the positive equilibrium at the same threshold. The exact \(U\)-identity and positive center coefficient above reconcile the forward-time phase portrait with that corollary: the positive center branch is repelling, while any attracting parabolic side lies outside the biologically relevant positive branch. Exact-title, DOI, model-equation, threshold, time-reversal, center-manifold, and weighted-coordinate searches found no prior statement of this identity or the positive-quadrant orientation correction.

## Limitations
The result is a forward-time local-orientation and exclusion statement at one critical surface. It does not re-prove the source's full global theorem, classify the entire center manifold, or analyze the distinct saddle-node \(E_3\) at \(m=m^*\). The term “attracting saddle-node” can be used differently across texts; the invariant content established here is narrower and unambiguous: the center branch that enters the nonnegative quadrant has positive quadratic drift and no nonzero nonnegative trajectory converges to the origin.

## References
L. Chen, T. Liu, and F. Chen, “Stability and bifurcation in a two-patch model with additive Allee effect,” *AIMS Mathematics* 7 (2022), 536–551, DOI 10.3934/math.2022034. The publisher records publication on 14 October 2021 and lists Mathematics Subject Classification 34C25, 92D25, 34D20, 34D40.
