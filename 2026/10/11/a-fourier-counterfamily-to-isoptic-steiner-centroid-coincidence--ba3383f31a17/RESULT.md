# A Fourier counterfamily to isoptic Steiner-centroid coincidence
## Finding
There exists \(\varepsilon_0>0\) such that, for every real
\[
0<|\varepsilon|<\varepsilon_0,
\]
the support function
\[
p_\varepsilon(t)=1+\varepsilon\bigl(\cos(2t)+\cos(3t)\bigr)
\]
defines a smooth strictly convex oval \(C_\varepsilon\) whose Steiner centroid is the origin, while the Steiner centroid of its orthoptic is displaced:
\[
S(C_\varepsilon)=(0,0),
\qquad
S(C_{\varepsilon,\pi/2})
=
\bigl(2\varepsilon^2+O(\varepsilon^3),0\bigr).
\]
Consequently
\[
S(C_{\varepsilon,\pi/2})\ne S(C_\varepsilon)
\]
for all sufficiently small nonzero \(\varepsilon\).

This gives a negative answer to the open problem in Mozgawa's Mellish-generalization paper asking whether the Steiner centroids of an oval and any of its isoptics must coincide.

## Assumptions and scope
An oval is a simple closed \(C^2\) plane curve of positive curvature. Its support function is written in the normal angle \(t\). The Steiner centroid is the curvature centroid used in the cited isoptic literature:
\[
S(\Gamma)=
\frac{\int_\Gamma x\,\kappa\,ds}{\int_\Gamma\kappa\,ds}.
\]
For a positively oriented oval, \(\int_\Gamma\kappa\,ds=2\pi\).

The \(\alpha\)-isoptic is parametrized by the intersection of support lines whose outer normals differ by \(\alpha\). Thus \(\alpha=\pi/2\) gives the orthoptic. The result is perturbative; no largest admissible \(\varepsilon_0\) is claimed.

## Proof
Put
\[
f(t)=\cos(2t)+\cos(3t),
\qquad
p_\varepsilon(t)=1+\varepsilon f(t).
\]
Its radius-of-curvature density is
\[
p_\varepsilon(t)+p_\varepsilon''(t)
=
1-3\varepsilon\cos(2t)-8\varepsilon\cos(3t).
\]
Hence
\[
p_\varepsilon+p_\varepsilon''>0
\]
whenever
\[
|\varepsilon|<\frac1{11},
\]
so \(p_\varepsilon\) defines a smooth strictly convex oval.

Write
\[
e_t=(\cos t,\sin t),
\qquad
n_t=(-\sin t,\cos t).
\]
The support parametrization is
\[
x_\varepsilon(t)=p_\varepsilon(t)e_t+p_\varepsilon'(t)n_t.
\]
For normal-angle parametrization, the Steiner-centroid formula is
\[
S(C_\varepsilon)=\frac1{2\pi}\int_0^{2\pi}x_\varepsilon(t)\,dt.
\]
Because \(p_\varepsilon\) has no first Fourier harmonic, the integral vanishes:
\[
S(C_\varepsilon)=(0,0).
\]

For \(\alpha=\pi/2\), the published isoptic formula reduces to
\[
z_\varepsilon(t)
=
p_\varepsilon(t)e_t+
p_\varepsilon\!\left(t+\frac\pi2\right)n_t.
\]
Set
\[
q_\varepsilon(t)
=
p_\varepsilon\!\left(t+\frac\pi2\right)
=
1+\varepsilon g(t),
\qquad
g(t)=-\cos(2t)+\sin(3t).
\]
At \(\varepsilon=0\),
\[
z_0(t)=e_t+n_t,
\]
a circle of radius \(\sqrt2\). Therefore, by \(C^2\)-continuity, there exists
\[
\varepsilon_0\in\left(0,\frac1{11}\right)
\]
such that the orthoptic is itself a positively curved regular oval whenever
\[
|\varepsilon|<\varepsilon_0.
\]

Differentiate
\[
z_\varepsilon=p_\varepsilon e_t+q_\varepsilon n_t.
\]
Then
\[
z_\varepsilon'
=
B_\varepsilon e_t+C_\varepsilon n_t,
\]
where
\[
B_\varepsilon=p_\varepsilon'-q_\varepsilon=-1+\varepsilon b,
\qquad
C_\varepsilon=p_\varepsilon+q_\varepsilon'=1+\varepsilon c,
\]
with
\[
b=f'-g,\qquad c=f+g'.
\]
For a regular positively oriented parametrization,
\[
\kappa_\varepsilon|z_\varepsilon'|
=
\frac{[z_\varepsilon',z_\varepsilon'']}{|z_\varepsilon'|^2}
=
1+
\frac{B_\varepsilon C_\varepsilon'-C_\varepsilon B_\varepsilon'}
{B_\varepsilon^2+C_\varepsilon^2}.
\]
Expanding gives
\[
\kappa_\varepsilon|z_\varepsilon'|
=
1+\varepsilon u_1+\varepsilon^2u_2+O(\varepsilon^3),
\]
where
\[
u_1=-\frac{b'+c'}2
\]
and
\[
u_2=
\frac{bc'-cb'+(b'+c')(c-b)}2.
\]

Also write
\[
z_\varepsilon=z_0+\varepsilon z_1,
\qquad
z_1=fe_t+gn_t.
\]
The Steiner centroid of the orthoptic is therefore
\[
S(C_{\varepsilon,\pi/2})
=
\frac1{2\pi}
\int_0^{2\pi}
z_\varepsilon
\bigl(1+\varepsilon u_1+\varepsilon^2u_2+O(\varepsilon^3)\bigr)\,dt.
\]
Exact trigonometric integration gives
\[
\frac1{2\pi}\int_0^{2\pi}z_0\,dt=(0,0),
\]
\[
\frac1{2\pi}\int_0^{2\pi}(z_1+z_0u_1)\,dt=(0,0),
\]
and
\[
\frac1{2\pi}\int_0^{2\pi}(z_1u_1+z_0u_2)\,dt=(2,0).
\]
Thus
\[
S(C_{\varepsilon,\pi/2})
=
\bigl(2\varepsilon^2+O(\varepsilon^3),0\bigr).
\]
The vanishing second coordinate is also forced by reflection symmetry because \(p_\varepsilon\) is even. The first coordinate is nonzero for every sufficiently small nonzero \(\varepsilon\), which proves the counterexample.

## Verification
The supplied `verify.py` replays the perturbation symbolically. It checks the source curvature density, the shifted support
\[
g(t)=-\cos(2t)+\sin(3t),
\]
the original zero Steiner centroid, and the exact second-order centroid integrals.

The checker returns zero constant and linear coefficients and the exact quadratic coefficient
\[
(2,0).
\]
The infinite-family sign is not inferred from finite sampling. Strict convexity of the source follows from the displayed \(1/11\) bound, while positive curvature of the orthoptic for sufficiently small \(\varepsilon\) follows from continuity at the circular case.

## Relationship to prior work
Mozgawa's Mellish-generalization paper develops generalized constant-width curves through isoptics. It explicitly states as an open problem whether the Steiner centroids of an oval and any of its isoptics coincide. Its preceding theorem proves coincidence only when the chosen isoptic is a circle.

The later Cieślak--Mozgawa paper classifies curves having a circle as an isoptic and again invokes the earlier theorem identifying that circle center with the original oval's Steiner centroid. That circular-isoptic classification does not cover the noncircular orthoptics in the present family.

Targeted searches for Steiner-centroid coincidence, orthoptic centroid displacement, support-function counterexamples, and the displayed two-mode perturbation did not locate a covering result.

## Limitations
The result is local in \(\varepsilon\); no largest admissible value of \(\varepsilon_0\) is claimed.

Only the orthoptic angle
\[
\alpha=\frac\pi2
\]
is used. The result does not classify which other isoptic angles preserve or move the Steiner centroid.

The proof gives the leading displacement
\[
2\varepsilon^2
\]
but not a closed form for the centroid at finite \(\varepsilon\).

An unindexed later note could contain another resolution of the same open problem; no such statement was found in the materially inspected primary paper, its most directly relevant follow-up, or the targeted searches.

## References
1. W. Mozgawa, *Mellish theorem for generalized constant width curves*, Aequationes Mathematicae 89 (2015), 1095--1105. DOI: 10.1007/s00010-014-0321-3. Published online 2014-11-27.
2. W. Cieślak and W. Mozgawa, *On curves with circles as their isoptics*, Aequationes Mathematicae 96 (2022), 653--667. DOI: 10.1007/s00010-021-00828-4. Published online 2021-06-28.
3. W. Cieślak, A. Miernowski, and W. Mozgawa, *Isoptics of a closed strictly convex curve*, Lecture Notes in Mathematics 1481 (1991), 28--35.
