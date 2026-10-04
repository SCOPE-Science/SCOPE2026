# One-sided grazing instability and logarithmically corrected escape in a large-hysteresis return map
## Finding
Consider the planar switched system
\[
X^+=(a_1,b_1x),\qquad X^-=(a_2,b_2),
\]
with switching lines \(y=\pm\mu\). Assume
\[
\mu>0,\qquad b_2>0,\qquad a_1b_1>0,\qquad a_1a_2<0,
\]
and impose the boundary relation
\[
a_2^2b_1\mu=a_1b_2^2.
\]
For the Poincaré map on the upper switching line, set
\[
A=\frac{2a_2\mu}{b_2},\qquad \rho=|A|,\qquad s=\operatorname{sgn}(A).
\]
Then \(x^*=A\) is the singular boundary fixed point where the upper leg is tangent to the lower switching line. It is a genuine periodic orbit, not a zero-time algebraic artifact.

On the returning side of the section, parameterized by \(x=A+s u\) with \(u\ge0\), the first-return map becomes exactly
\[
u^+=\sqrt{u(u+2\rho)}.
\]
Consequently the boundary cycle is one-sided repelling. For every \(u_0>0\), if
\[
u_{n+1}=\sqrt{u_n(u_n+2\rho)},
\]
then there is a finite constant \(C(u_0,\rho)\) such that
\[
u_n=\rho n-\frac{\rho}{2}\log n+C(u_0,\rho)+o(1)
\qquad(n\to\infty).
\]
Thus the singular grazing boundary has a universal linear escape rate \(\rho\) with a universal negative logarithmic correction \(-\rho\log n/2\).

## Assumptions and scope
The result concerns the affine large-hysteresis model and its first-return map from Carvalho, Serantola, and Rangel, arXiv:2609.08974v1. The sign assumptions select the two parameter cases in which the singular boundary point corresponds to a positive-time periodic trajectory: \(a_1\) and \(b_1\) have the same sign, while \(a_2\) has the opposite sign, and \(b_2>0\).

The equality
\[
a_2^2b_1\mu=a_1b_2^2
\]
is exactly the boundary condition excluded from the differentiable fixed-point stability argument in the source. No claim is made for other parameter cases, for nonlinear perturbations of the vector fields, or for stochastic perturbations.

## Proof
The source gives the return map
\[
P(x)=A-\frac1{b_1}\sqrt{R(x)},\qquad
R(x)=b_1\bigl(b_1x^2-4a_1\mu\bigr),
\]
with \(A=2a_2\mu/b_2\). Under the boundary equality,
\[
R(A)=0.
\]
At \(x=A\), the source's upper-flight formula gives
\[
t_+=-\frac{A}{a_1}>0
\]
because \(a_1a_2<0\). The upper leg reaches \((0,-\mu)\), where \(X^+\) is tangent to the lower switching line since its vertical component is \(b_1x=0\). The lower constant field returns to \((A,\mu)\) after
\[
t_-=\frac{2\mu}{b_2}>0.
\]
Hence \(x=A\) represents a genuine grazing periodic orbit.

Since \(a_1b_1>0\) and \(a_1a_2<0\), one has \(s=-\operatorname{sgn}(b_1)\). Put \(x=A+s u\), where \(u\ge0\) is signed distance into the returning branch. Because \(|A|=\rho\),
\[
R(A+s u)=b_1^2u(2\rho+u).
\]
Therefore
\[
P(A+s u)-A
=-\operatorname{sgn}(b_1)\sqrt{u(2\rho+u)}
=s\sqrt{u(2\rho+u)},
\]
which proves the exact scalar recurrence
\[
u_{n+1}=\sqrt{u_n(u_n+2\rho)}.
\]

For \(u_n>0\),
\[
u_{n+1}^2-u_n^2=2\rho u_n>0,
\]
so \(u_{n+1}>u_n\). A finite positive limit would contradict the recurrence, hence \(u_n\to\infty\). Moreover,
\[
u_{n+1}-u_n
=\frac{2\rho}{\sqrt{1+2\rho/u_n}+1}
\longrightarrow \rho.
\]
Thus \(u_n/n\to\rho\) by Stolz-Cesàro.

Set \(v_n=u_n/\rho\). Then
\[
v_{n+1}=\sqrt{v_n^2+2v_n}
\]
and, as \(v\to\infty\),
\[
\sqrt{v^2+2v}-v
=1-\frac1{2v}+O(v^{-2}).
\]
The exact increment is smaller than \(1\) and, for large \(v\), is at least \(1-C/v\). Together with \(v_n/n\to1\), summation yields
\[
v_n=n+O(\log n).
\]
Now define
\[
w_n=v_n-n+\frac12\log n.
\]
Using the preceding expansion and
\[
\frac12\log\left(1+\frac1n\right)
=\frac1{2n}+O(n^{-2}),
\]
one obtains
\[
w_{n+1}-w_n
=\frac1{2n}-\frac1{2v_n}+O(n^{-2})
=O\!\left(\frac{\log n}{n^2}\right).
\]
The last series is summable, so \(w_n\) converges to a finite constant. Rescaling by \(\rho\) proves
\[
u_n=\rho n-\frac{\rho}{2}\log n+C(u_0,\rho)+o(1).
\]

## Verification
The boundary reduction was checked directly from the source formulas for the flight time, return point, return map, and boundary condition. Symbolic expansion of the exact normalized increment
\[
\sqrt{v^2+2v}-v
\]
gives
\[
1-\frac1{2v}+\frac1{2v^2}+O(v^{-3}),
\]
consistent with the proof. The asymptotic argument uses the exact recurrence, not numerical trajectory fitting.

The singular point is tested as a positive-time orbit by the two explicit flight times before any stability conclusion is drawn. This avoids treating a merely algebraic fixed point of a formula as a physical return orbit.

## Relationship to prior work
Carvalho, Serantola, and Rangel derive the exact return map and identify the singular condition \(R(x^*)=0\), stating that stability there requires separate analysis because the derivative test fails. Their subsequent generic phase-space discussion does not derive the signed-distance recurrence or any iteration-rate law at the singular boundary.

Square-root singularities of grazing Poincaré maps are classical. Avrutin, Dutta, Schanz, and Banerjee analyze one-dimensional piecewise-smooth maps with square-root singularities and their bifurcations, while Simpson, Hogan, and Kuske describe the Nordmark square-root normal form near regular grazing. Those works explain why square-root stretching is structurally natural, but the inspected material does not state the exact recurrence
\[
u^+=\sqrt{u(u+2\rho)}
\]
for this large-hysteresis model or the escape law
\[
u_n=\rho n-\frac{\rho}{2}\log n+O(1).
\]

## Limitations
The statement is restricted to the singular boundary of the affine two-field model and to the returning side of the Poincaré section. The constant \(C(u_0,\rho)\) is proved to exist but is not expressed in closed form. The result does not assert persistence of the logarithmic correction under nonlinear perturbations, smoothing of the switching law, noise, or changes of switching convention.

The literature comparison cannot exclude an equivalent calculation hidden in unindexed nonsmooth-dynamics literature. General square-root grazing theory is therefore a residual originality risk, although the exact model-specific recurrence and logarithmically corrected escape law were not found in the checked sources.

## References
1. T. Carvalho, L. Serantola, B. S. Rangel, “Limit Sets and Global Bifurcation Structure in Planar Control Models with Large Hysteresis,” arXiv:2609.08974v1, 2026.
2. V. Avrutin, P. S. Dutta, M. Schanz, S. Banerjee, “Influence of a square-root singularity on the behaviour of piecewise smooth maps,” Nonlinearity 23 (2010), 445–463, doi:10.1088/0951-7715/23/2/012.
3. D. J. W. Simpson, S. J. Hogan, R. Kuske, “Stochastic Regular Grazing Bifurcations,” SIAM Journal on Applied Dynamical Systems 12 (2013), doi:10.1137/120884286.
