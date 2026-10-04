# Exact stationary height defect and a negative-slab recurrence obstruction in the Dadras–Momeni flow
## Finding
Consider the Dadras–Momeni system
\[
\dot x=y-ax+byz,\qquad
\dot y=cy-xz+z,\qquad
\dot z=dxy-mz,
\]
with
\[
a,b,c,d,m>0.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the heightwise conditional law
\[
\mathbb E_\mu[xy\mid z]=\frac{m}{d}z
\]
and the exact stationary height defect
\[
\mathbb E_\mu\!\left[\left(z+\frac{1}{2b}\right)^2\right]
=
\frac{1}{4b^2}
+
\frac{ad}{bm}\,\mathbb E_\mu[x^2].
\]

Hence
\[
\mathbb E_\mu\!\left[\left(z+\frac{1}{2b}\right)^2\right]
\ge
\frac{1}{4b^2},
\]
and equality holds if and only if \(\mu\) is the Dirac measure at the origin.

Therefore every compact invariant probability measure other than the origin measure assigns positive mass to
\[
\{z<-1/b\}\cup\{z>0\}.
\]
Equivalently, no nontrivial compact recurrent statistical state is contained in the closed negative slab
\[
-\frac1b\le z\le0.
\]
In particular every nonconstant periodic orbit leaves this slab.

For the standard parameter choice
\[
(a,b,c,d,m)=\left(3,\frac{27}{10},\frac{17}{10},2,9\right),
\]
the defect becomes
\[
\mathbb E_\mu\!\left[\left(z+\frac5{27}\right)^2\right]
=
\frac{25}{729}
+
\frac{20}{81}\mathbb E_\mu[x^2],
\]
so every nontrivial compact recurrent state visits
\[
z<-\frac{10}{27}
\qquad\text{or}\qquad
z>0.
\]

## Assumptions and scope
The theorem concerns Borel probability measures invariant under the flow and supported on compact invariant subsets of \(\mathbb R^3\). Compact support guarantees integrability of the polynomial generator identities used below. The periodic-orbit conclusion concerns a nonconstant classical periodic solution.

The equations are the standard Dadras–Momeni family introduced in the 2009 multi-scroll paper. Later reproductions use the same five-parameter polynomial vector field. The parameter \(c\) does not enter the defect identity; positivity of \(c\) is retained because it includes the standard chaotic parameter regime while keeping the theorem aligned with the published family.

## Proof
For a compactly supported invariant probability measure and any continuously differentiable test function \(h\),
\[
\int Lh\,d\mu=0,
\]
where \(L\) is the flow generator.

Take a test function depending only on \(z\). Then
\[
Lh(z)=h'(z)(dxy-mz).
\]
On the compact \(z\)-range, every continuous function is the derivative of a continuously differentiable function. Therefore
\[
\int \phi(z)(dxy-mz)\,d\mu=0
\]
for every continuous \(\phi\), which is exactly
\[
\mathbb E_\mu[dxy-mz\mid z]=0.
\]
Since \(d>0\),
\[
\mathbb E_\mu[xy\mid z]=\frac md z.
\]

Two polynomial generator identities give the global defect. First,
\[
L(z^2)=2dxyz-2mz^2,
\]
so invariance yields
\[
d\,\mathbb E_\mu[xyz]=m\,\mathbb E_\mu[z^2].
\]
Second,
\[
L(x^2)=2xy-2ax^2+2bxyz,
\]
hence
\[
a\,\mathbb E_\mu[x^2]
=
\mathbb E_\mu[xy]+b\,\mathbb E_\mu[xyz].
\]
Using the conditional law and the \(z^2\) identity gives
\[
a\,\mathbb E_\mu[x^2]
=
\frac md\left(\mathbb E_\mu[z]+b\,\mathbb E_\mu[z^2]\right).
\]
Equivalently,
\[
\mathbb E_\mu[z+bz^2]
=
\frac{ad}{m}\mathbb E_\mu[x^2].
\]
Completing the square yields
\[
\mathbb E_\mu\!\left[\left(z+\frac{1}{2b}\right)^2\right]
=
\frac{1}{4b^2}
+
\frac{ad}{bm}\mathbb E_\mu[x^2].
\]

Because \(a,b,d,m>0\), equality in the lower bound is equivalent to
\[
\mathbb E_\mu[x^2]=0.
\]
Then the support of \(\mu\) lies in \(x=0\). Every complete trajectory in this compact invariant support has \(x(t)\equiv0\), so
\[
0=\dot x=y(1+bz)
\]
and
\[
\dot z=-mz.
\]
If \(z\) were not identically zero, the complete solution
\[
z(t)=z(0)e^{-mt}
\]
would be unbounded backward in time, contradicting compactness. Hence \(z\equiv0\), and then \(\dot x=y\) forces \(y\equiv0\). Thus the support is the origin. Conversely the origin measure clearly attains equality.

For every other invariant measure the defect is strict:
\[
\mathbb E_\mu\!\left[\left(z+\frac{1}{2b}\right)^2\right]
>
\frac{1}{4b^2}.
\]
On the slab \(-1/b\le z\le0\), however,
\[
\left|z+\frac{1}{2b}\right|\le\frac{1}{2b}.
\]
If the measure assigned zero mass to the complement of the slab, its squared defect could not exceed \(1/(4b^2)\). Therefore the complement
\[
\{z<-1/b\}\cup\{z>0\}
\]
has positive measure.

The normalized orbit measure of a nonconstant periodic orbit is compactly supported, invariant, and is not the origin measure. The periodic orbit must therefore contain a point outside the closed slab.

## Verification
The accompanying checker uses exact rational sparse-polynomial arithmetic. It verifies
\[
Lz=dxy-mz,
\]
\[
L(z^2)=2dxyz-2mz^2,
\]
\[
L(x^2)=2xy-2ax^2+2bxyz,
\]
and the combined pointwise certificate
\[
\frac d2L(x^2)-Lz-\frac b2L(z^2)
=
mz+bmz^2-adx^2.
\]
The stored checker output is `VERIFY_OK`.

The conditional-expectation step is an exact consequence of invariance against arbitrary functions of \(z\), not a finite numerical experiment. The equality classification uses only compact support and invariance of the support under a continuous flow.

## Relationship to prior work
Dadras and Momeni introduced the system to obtain two-, three-, and four-scroll chaotic attractors and studied its equilibria and numerical dynamics through time histories, phase diagrams, Poincaré maps, bifurcation diagrams, and Lyapunov exponents. A later same-object study by Saberi Nik, Van Gorder, and Gambino addresses optimal control, adaptive synchronization, and hyperchaotification. A later numerical-analysis paper uses the Dadras–Momeni equations as an ODE-solver test problem.

The present statement has a different quantifier and implication: it constrains every compactly supported invariant probability measure of the uncontrolled five-parameter flow. Targeted semantic searches for the Dadras–Momeni system together with invariant measures, stationary balances, conditional moments, height defects, recurrence slabs, and equivalent formulations returned no same-object theorem implying the conditional law or the completed-square defect. The closest indexed results concern stationary balance laws for different polynomial flows and do not reduce to the Dadras–Momeni vector field.

## Limitations
The theorem concerns compact invariant measures and periodic orbits. It does not prove the existence of chaotic attractors, classify all unbounded trajectories, or determine how often a recurrent trajectory lies outside the slab.

The conclusion is a one-sided exclusion: a nontrivial recurrent state must visit \(z<-1/b\) or \(z>0\), but the theorem does not require both alternatives for every ergodic component.

The original 2009 paper was available in this inspection through its abstract and bibliographic metadata rather than complete full text. The 2015 same-object control paper was likewise inspected at abstract and metadata level because full text was not accessible. These are retained as bibliographic access risks, and no whole-document noncoverage claim is made for either source. Targeted searches can also miss differently phrased or unindexed results.

## References
1. S. Dadras and H. R. Momeni, “A novel three-dimensional autonomous chaotic system generating two, three and four-scroll attractors,” Physics Letters A 373, 3637–3642 (2009), DOI 10.1016/j.physleta.2009.07.088.
2. H. Saberi Nik, R. A. Van Gorder, and G. Gambino, “The chaotic Dadras–Momeni system: control and hyperchaotification,” IMA Journal of Mathematical Control and Information 33, 497–518 (2016), DOI 10.1093/imamci/dnu050; first published online 2015-01-27.
3. D. Butusov et al., “Adaptive Stepsize Control for Extrapolation Semi-Implicit Multistep ODE Solvers,” Mathematics 9, 950 (2021), DOI 10.3390/math9090950.
4. B. Ulmann, “Four times chaos,” Analog Computer Applications, Issue 46 (2024), which reproduces the Dadras equations and bibliographic issue date of the 2009 source.
