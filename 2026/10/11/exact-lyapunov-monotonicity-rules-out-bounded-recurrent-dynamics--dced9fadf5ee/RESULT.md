# Exact Lyapunov monotonicity rules out bounded recurrent dynamics on the line-equilibrium slice of a 5D segmented disc dynamo
## Finding
Consider the five-dimensional system introduced by Bao, Chen, Liu, and Deng,
\[
\begin{aligned}
\dot x&=r(y-x)+k_1u,\\
\dot y&=mx-(1+m)y+xz+v,\\
\dot z&=g(mx^2+1-(1+m)xy)-k_2-k_3z,\\
\dot u&=k_4xy-k_5u,\\
\dot v&=k_6x+xz-u.
\end{aligned}
\]
On the line-equilibrium slice \(k_1=0\), \(k_2=g>0\), and \(k_3=k_4=k_5=0\), with \(r>0\), \(m>0\), and arbitrary real \(k_6\), define
\[
H(x,z)=z+\frac{g(1+m)}{2r}x^2.
\]
Then every classical solution satisfies
\[
\dot H=-g x^2.
\]
Hence every bounded forward solution converges to one equilibrium \((0,0,z_\infty,0,0)\). Equivalently, this parameter slice has no non-equilibrium compact recurrent dynamics. Moreover, the compactly supported invariant probability measures are exactly the probability measures supported on the equilibrium line
\[
\mathcal E=\{(0,0,z,0,0):z\in\mathbb R\}.
\]

For the parameters used in the source's line-equilibrium example,
\[
(m,r,g,k_6)=\left(\frac{11}{10},\frac{61}{10},12,-100\right),
\]
so
\[
H=z+\frac{126}{61}x^2,\qquad \dot H=-12x^2.
\]
Therefore the bounded-looking trajectory initialized at \((21,1/10,1,0,0)\) cannot approach a non-equilibrium chaotic attractor of the exact differential equation. The other initial condition used for the reported hyperchaotic case, \((0,0,0,0,0)\), is itself a point of \(\mathcal E\), so its exact trajectory is constant.

At that origin the Jacobian has characteristic polynomial
\[
\chi(\lambda)=\frac{\lambda^2}{10}\left(10\lambda^3+82\lambda^2+61\lambda+6100\right).
\]
Its three nonzero roots are approximately
\[
-11.9566842997,\qquad 1.87834214986\pm6.89124944793i.
\]
Thus the two positive finite-time growth rates reported from the stationary initial condition are consistent with transverse variational instability of the equilibrium; they are not evidence of hyperchaotic state-space motion from that initial condition.

## Assumptions and scope
The conclusion concerns the exact autonomous ODE on the stated parameter slice. The forward-convergence statement assumes the solution is defined and bounded for all \(t\ge0\). It does not assert that every initial condition is bounded. The invariant-measure statement assumes a compactly supported invariant Borel probability measure. No conclusion here is made about parameter choices away from \(k_1=0\), \(k_2=g\), and \(k_3=k_4=k_5=0\).

## Proof
On the stated slice,
\[
\dot z=gmx^2-g(1+m)xy,\qquad \dot x=r(y-x).
\]
Therefore
\[
\begin{aligned}
\dot H
&=gmx^2-g(1+m)xy+\frac{g(1+m)}{r}x\dot x\\
&=gmx^2-g(1+m)xy+g(1+m)x(y-x)\\
&=-gx^2.
\end{aligned}
\]

Let a forward solution be bounded. Then \(H(t)\) is decreasing and bounded below, hence converges, and
\[
\int_0^\infty x(t)^2\,dt<\infty.
\]
Boundedness of the full trajectory makes \(\dot x=r(y-x)\) bounded, so \(x\) is uniformly continuous. Barbalat's lemma gives \(x(t)\to0\). Since \(z=H-g(1+m)x^2/(2r)\), also \(z(t)\to H_\infty\).

The omega-limit set is nonempty, compact, and invariant. The function \(H\) is constant there, so \(\dot H=-gx^2=0\) forces \(x=0\) throughout the omega-limit set. Invariance then forces successively \(y=0\) from \(\dot x=ry\), \(v=0\) from \(\dot y=v\), and \(u=0\) from \(\dot v=-u\). Thus the omega-limit set is contained in \(\mathcal E\). Because \(z(t)\to H_\infty\), the omega-limit set is the singleton \((0,0,H_\infty,0,0)\), proving convergence.

For a compactly supported invariant probability measure \(\mu\), invariance gives
\[
0=\int L H\,d\mu=-g\int x^2\,d\mu.
\]
Hence \(x=0\) on the support. The support is invariant; the same successive tangency conditions imply \(y=v=u=0\) there. Thus \(\operatorname{supp}\mu\subseteq\mathcal E\). Conversely, every probability measure supported on the equilibrium line is invariant.

At the source parameters, direct substitution gives \(g(1+m)/(2r)=126/61\). Linearizing at the origin and taking the determinant of \(\lambda I-J\) yields the displayed characteristic polynomial. Its numerical roots give the stated transverse growth rates.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to verify the coefficient \(126/61\), the cancellation yielding \(\dot H=-12x^2\), and the full characteristic polynomial at the published parameters. It also computes the three nonzero roots by an independent dependency-free Durand–Kerner iteration and checks them against the displayed numerical values. Running

`python verify.py`

prints `VERIFY_OK` when all checks pass.

The convergence and invariant-measure arguments are analytic consequences of the exact identity; finite numerical integration is not used as a proof of asymptotic behavior.

## Relationship to prior work
Bao, Chen, Liu, and Deng introduce the exact five-dimensional system, identify the line-equilibrium parameter set, and present a bounded-looking chaotic trajectory and a hyperchaotic case on the parameter choice used above. Their full article also reports the finite-time local Lyapunov exponents quoted in the finding. The inspected article does not state the monotone quantity \(H\), the bounded-orbit convergence theorem, or the invariant-measure classification proved here.

Jafari and Sprott show that line equilibria can coexist with chaos in other quadratic flows, so the mere presence of an equilibrium line does not imply this result. The obstruction here comes from the specific exact identity \(\dot H=-gx^2\). A related 2019 segmented-disc-dynamo article by Liu, Bao, Chen, and Deng studies a different five-dimensional vector field; its conclusions do not imply the identity for the system considered here.

## Limitations
The theorem does not establish boundedness for arbitrary initial data, does not classify unbounded trajectories, and does not address the source's other parameter regimes. A finite-time numerical computation started at an unstable equilibrium can report positive variational growth rates even though the state trajectory is constant; the result here distinguishes those tangent-space rates from recurrent state-space dynamics. The literature comparison cannot exclude an unindexed or otherwise undiscovered prior statement of the same identity, although the source itself, closely related same-author work, general line-equilibrium literature, and targeted published-result searches were inspected.

## References
1. J. Bao, D. Chen, Y. Liu, and H. Deng, “Coexisting hidden attractors in a 5D segmented disc dynamo with three types of equilibria,” *Discrete and Continuous Dynamical Systems - B* 24 (2019), 6053–6069. DOI: 10.3934/dcdsb.2019130. Earliest verified public date: 2019-07-17.
2. S. Jafari and J. C. Sprott, “Simple chaotic flows with a line equilibrium,” *Chaos, Solitons & Fractals* 57 (2013), 79–84. DOI: 10.1016/j.chaos.2013.08.018.
3. Y. Liu, J. Bao, D. Chen, and H. Deng, “Multistability and bifurcations in a 5D segmented disc dynamo with a curve of equilibria,” *Advances in Difference Equations* 2019, 345 (2019). DOI: 10.1186/s13662-019-2284-0.
