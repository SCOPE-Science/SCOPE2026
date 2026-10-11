# A monotone coboundary excludes recurrent chaos on the line-equilibrium slice of a 5D segmented disc dynamo
## Finding
Consider the printed five-dimensional system
\[
\begin{aligned}
\dot x&=r(y-x)+k_1u,\\
\dot y&=mx-(1+m)y+xz+v,\\
\dot z&=g(mx^2+1-(1+m)xy)-k_2-k_3z,\\
\dot u&=k_4xy-k_5u,\\
\dot v&=k_6x+xz-u.
\end{aligned}
\]
On the natural line-equilibrium slice
\[
r>0,\qquad m>0,\qquad g>0,\qquad k_1=0,\qquad k_2=g,\qquad k_3=0,
\]
with \(k_4,k_5,k_6\in\mathbb R\) arbitrary, define
\[
H(x,z)=z+\frac{g(1+m)}{2r}x^2.
\]
Then every trajectory satisfies the exact monotonicity identity
\[
\dot H=-g x^2.
\]
Therefore every compactly supported invariant probability measure is supported on
\[
\mathcal L=\{(0,0,z,0,0):z\in\mathbb R\},
\]
and every recurrent point lies on \(\mathcal L\). In particular this slice has no nonconstant periodic, quasiperiodic, chaotic, or hyperchaotic recurrent state.

For the line-equilibrium parameters used in Section 2.3 of the source,
\[
(m,r,g,k_1,k_2,k_3,k_4,k_5,k_6)=(1.1,6.1,12,0,12,0,0,0,-100),
\]
the law becomes
\[
H=z+\frac{126}{61}x^2,\qquad \dot H=-12x^2.
\]
Thus the reported chaotic and hyperchaotic recurrent attractors on that parameter slice are incompatible with the printed differential equations. The source's initial condition \((0,0,0,0,0)\) is exactly a point of the equilibrium line, so its exact trajectory is constant.

## Assumptions and scope
The claim concerns the autonomous differential equations printed as system (2.2) in Bao, Chen, Liu, and Deng. The assumptions are exactly \(r>0\), \(m>0\), \(g>0\), \(k_1=0\), \(k_2=g\), and \(k_3=0\). No sign or size restriction is needed on \(k_4\), \(k_5\), or \(k_6\).

A recurrent point means a point returning arbitrarily close to itself along a sequence of positive times. An invariant probability measure is assumed compactly supported so that the generator identity for the polynomial observable \(H\) is immediate. The conclusion concerns recurrence for the exact continuous-time vector field; it does not identify which numerical mechanism produced the figures in the source.

## Proof
Because \(k_1=0\),
\[
\dot x=r(y-x),
\]
and because \(k_2=g\) and \(k_3=0\),
\[
\dot z=g\bigl(mx^2-(1+m)xy\bigr).
\]
Hence
\[
\begin{aligned}
\dot H
&=g\bigl(mx^2-(1+m)xy\bigr)
  +\frac{g(1+m)}r x\,r(y-x)\\
&=g\bigl(mx^2-(1+m)xy+(1+m)xy-(1+m)x^2\bigr)\\
&=-g x^2.
\end{aligned}
\]
This proves the exact coboundary identity.

Let \(\mu\) be a compactly supported invariant probability measure. Invariance gives
\[
0=\int \dot H\,d\mu=-g\int x^2\,d\mu.
\]
Since \(g>0\), one has \(x=0\) on the support of \(\mu\). The support of an invariant measure is invariant under the flow. Along an orbit contained in \(x=0\), the first equation gives \(y=0\); the second then gives \(v=0\); and the fifth gives \(u=0\). The remaining coordinate \(z\) is constant. Thus
\[
\operatorname{supp}\mu\subseteq\mathcal L.
\]
Conversely, every probability measure supported on \(\mathcal L\) is invariant because every point of \(\mathcal L\) is an equilibrium. This completely classifies compactly supported invariant probability measures on the slice.

Now let \(p\) be recurrent. Since \(H\) is nonincreasing and continuous, recurrence forces \(H(\phi_{t_n}p)\to H(p)\) along return times \(t_n\to\infty\). But
\[
H(p)-H(\phi_t p)=g\int_0^t x(s)^2\,ds
\]
is nondecreasing in \(t\). Its value must therefore be zero for every \(t\ge0\), so \(x(t)=0\) for all \(t\ge0\). The same equation-by-equation argument gives \(y=v=u=0\), hence \(p\in\mathcal L\).

## Verification
The package includes `verify.py`, a standard-library exact polynomial checker. It expands the two terms in \(\dot H\) on the stated slice and verifies coefficient-by-coefficient that the remainder is exactly \(-g x^2\). It also verifies the rational source coefficient \(g(1+m)/(2r)=126/61\) and confirms that the published initial condition \((0,0,0,0,0)\) has zero vector field at the published line-equilibrium parameters.

The proof does not infer infinite-time recurrence from a finite simulation. The invariant-measure conclusion is analytic and exact.

## Relationship to prior work
Bao, Chen, Liu, and Deng introduce the exact system, identify the slice \(k_1=0\), \(k_2=g\), \(k_3=0\) as having the equilibrium line \(\mathcal L\), and in Section 2.3 report chaotic and hyperchaotic attractors for \((1.1,6.1,12,0,12,0,0,0,-100)\). Their analysis does not state the monotone observable \(H\), the compact-invariant-measure classification, or the recurrence exclusion proved here.

A closely related 2019 open-access segmented-disc-dynamo paper by Bao and Liu studies a different five-dimensional extension and a different line-equilibrium regime. Its equations and parameter roles do not specialize to the present vector field, so its bifurcation and multistability results do not imply the identity above.

General Lyapunov and invariance principles explain how a strict monotone observable constrains recurrence once such an observable is known; they do not supply this source-specific cancellation or its contradiction with the published line-equilibrium examples.

## Limitations
The recurrence exclusion is restricted to \(k_1=0\), \(k_2=g\), \(k_3=0\), with \(g>0\). It does not assess the paper's other parameter regimes, its Hopf or pitchfork calculations away from this slice, or the validity of attractors reported for parameters outside the slice.

The result does not prove that every bounded complete orbit is an equilibrium; gradient-like heteroclinic behavior is not excluded by the measure argument alone. The proved statements are the exact monotonicity identity, support classification of compact invariant probability measures, and exclusion of non-equilibrium recurrent points.

## References
1. J. Bao, D. Chen, Y. Liu, H. Deng, “Coexisting hidden attractors in a 5D segmented disc dynamo with three types of equilibria,” *Discrete and Continuous Dynamical Systems - B* 24 (2019), 6053–6069. DOI: 10.3934/dcdsb.2019130.
2. J. Bao, Y. Liu, “Multistability and bifurcations in a 5D segmented disc dynamo with a curve of equilibria,” *Advances in Difference Equations* 2019, Article 345. DOI: 10.1186/s13662-019-2284-0.
