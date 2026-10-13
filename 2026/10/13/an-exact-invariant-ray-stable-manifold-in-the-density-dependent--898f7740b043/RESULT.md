# An exact invariant-ray stable manifold in the density-dependent ratio predator-prey model

## Finding

Consider
\[
x'=x\left(1-x-\frac{s y}{x+y}\right),\qquad
y'=b y\left(-d-r y+\frac{x}{x+y}\right),
\]
with positive parameters. On
\[
br(b-1-bd)+(s-1-bd)=0,
\]
the ray
\[
\mathcal L=\{(x,y):y=x/(br),\ x>0\}
\]
is exactly invariant.

Define
\[
\kappa=1-\frac{s}{1+br}
=\frac{b[br-d(1+br)]}{1+br}.
\]
On the ray,
\[
x'=x(\kappa-x).
\]
If \(\kappa>0\), every positive point on \(\mathcal L\) converges to
\[
E_{\mathcal L}=(\kappa,\kappa/(br)).
\]

The tangent eigenvalue is
\[
-\kappa,
\]
and the transverse eigenvalue is
\[
\lambda_\perp
=
\frac{b[d+r-2br(1-d)]}{1+br}.
\]
Thus, if \(\lambda_\perp>0\), the equilibrium is a hyperbolic saddle and \(\mathcal L\) is its positive stable manifold.

For the exact source-compatible choice
\[
b=\frac15,\qquad d=\frac1{20},\qquad r=\frac12,\qquad s=\frac{1091}{1000},
\]
the source's two-positive-equilibria assumptions hold. The saddle is
\[
E_1=\left(\frac9{1100},\frac9{110}\right),
\]
its exact stable manifold is
\[
y=10x,
\]
and its eigenvalues are
\[
-\frac9{1100},\qquad \frac{18}{275}.
\]
The second positive equilibrium is
\[
E_2=\left(\frac{7371}{28100},\frac{1539}{2810}\right),
\]
and it satisfies the source's local-attractor sign condition.

## Assumptions and scope

All parameters are positive and the state lies in the positive quadrant. The invariant-ray result assumes
\[
br(b-1-bd)+(s-1-bd)=0.
\]
The stable-manifold conclusion additionally assumes
\[
\kappa>0,\qquad \lambda_\perp>0.
\]

The stable manifold is identified inside the positive quadrant. No claim is made that this ray is the entire global boundary between every attraction basin.

## Proof

Set
\[
u=\frac yx.
\]
For \(x,y>0\),
\[
\frac{u'}u
=
\frac{y'}y-\frac{x'}x
=
\frac{(b-1-bd)+(s-1-bd)u}{1+u}
+x(1-br u).
\]
At
\[
u_0=\frac1{br},
\]
the second term vanishes. The first term vanishes exactly when
\[
br(b-1-bd)+(s-1-bd)=0.
\]
Hence \(u'=0\) on \(u=u_0\), proving invariance of \(\mathcal L\).

On \(\mathcal L\),
\[
\frac{s y}{x+y}=\frac{s}{1+br},
\]
so
\[
x'=x(\kappa-x).
\]
For \(\kappa>0\), the positive logistic flow converges to \(\kappa\), and therefore every positive ray point converges to \(E_{\mathcal L}\).

In \((x,u)\) coordinates the linearization at
\[
(\kappa,1/(br))
\]
is triangular. The tangent eigenvalue is the logistic derivative \(-\kappa\). Differentiating the ratio equation transversely and using the parameter relation gives
\[
\lambda_\perp
=
\frac{b[d+r-2br(1-d)]}{1+br}.
\]
If \(\lambda_\perp>0\), the equilibrium is a saddle. The invariant ray is tangent to the one-dimensional stable eigenspace and every positive point on it converges to the saddle, so uniqueness of the local stable manifold identifies the ray with the positive stable manifold.

For the rational witness,
\[
br=\frac1{10},\qquad
b-1-bd=-\frac{81}{100},\qquad
s-1-bd=\frac{81}{1000},
\]
so the invariant relation holds. Moreover,
\[
\kappa=\frac9{1100},\qquad
\lambda_\perp=\frac{18}{275}.
\]

The source's two-positive-equilibria inequalities hold exactly:
\[
\frac{20}{19}
<
\frac{1091}{1000}
<
\frac{881}{760},
\qquad
\frac{31639}{20000}<2.
\]
The two equilibrium ratios are
\[
10,\qquad \frac{190}{91},
\]
which give the stated \(E_1\) and \(E_2\).

## Verification

The bundled `verify.py` uses exact symbolic arithmetic. It verifies the invariant-ray parameter relation, \(\kappa\), \(\lambda_\perp\), both positive equilibria, the source-regime inequalities, and the exact Jacobian at \(E_1\).

The checker obtains
\[
J(E_1)=
\begin{pmatrix}
\frac{248}{3025}&-\frac{1091}{121000}\\
\frac{20}{121}&-\frac{299}{12100}
\end{pmatrix},
\]
with exact eigenvalues
\[
-\frac9{1100},\qquad \frac{18}{275}.
\]
It also verifies that the source's local stability coefficient at \(E_2\) is positive.

The general theorem is analytic; no finite numerical experiment is used to infer it.

## Relationship to prior work

Jiang, She, and Ruan give the global phase-plane analysis of this density-dependent mortality model. In their two-positive-equilibria regime the smaller positive equilibrium is a saddle, and they identify parameter regimes with two attractors.

A direct predecessor by Jiang, She, Feng, and Zheng studies the related ratio-dependent predator-prey core and its local bifurcations but does not provide this invariant-ray formula.

Later slow-fast work by Chowdhury, Petrovskii, and Banerjee uses the same underlying ratio-dependent structure and explicitly discusses trajectories passing near a saddle stable manifold. That treatment is numerical and slow-fast; it does not give this exact straight stable manifold for the unscaled system.

The new content is the exact parameter surface, invariant ray, logistic reduction, transverse eigenvalue, and a rational witness inside the motivating source's bistable regime.

## Limitations

The straight stable manifold occurs on a codimension-one parameter surface.

The result identifies the complete positive stable manifold of the saddle but does not prove that it is the entire global boundary between all attraction basins.

The source's broader global phase portrait is not re-evaluated.

## References

1. X. Jiang, Z. She, S. Ruan, “Global dynamics of a predator-prey system with density-dependent mortality and ratio-dependent functional response,” Discrete and Continuous Dynamical Systems - B 25 (2020), 2293–2310. DOI: 10.3934/dcdsb.2020041.
2. X. Jiang, Z. She, W. Feng, J. Zheng, “Bifurcation Analysis of a Predator–Prey System with Ratio-Dependent Functional Response,” International Journal of Bifurcation and Chaos 27 (2017), 1750222. DOI: 10.1142/S0218127417502224.
3. P. R. Chowdhury, S. Petrovskii, M. Banerjee, “Effect of Slow–Fast Time Scale on Transient Dynamics in a Realistic Prey-Predator System,” Mathematics 10 (2022), 699. DOI: 10.3390/math10050699.
