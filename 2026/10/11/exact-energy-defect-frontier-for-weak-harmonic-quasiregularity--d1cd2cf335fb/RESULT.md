# Exact energy–defect frontier for weak harmonic quasiregularity

## Finding

Fix
\[
K\ge1.
\]
A harmonic map
\[
f=h+\overline g
\]
is weakly \((K,K_0)\)-quasiregular when its Jacobian is nonnegative and
\[
\Lambda_f^2\le KJ_f+K_0,
\qquad
K_0\ge0,
\]
where
\[
\Lambda_f=|h'|+|g'|,
\qquad
J_f=|h'|^2-|g'|^2.
\]

Consider all coefficient pairs \((A,B)\) for which the pointwise estimate
\[
\Lambda_f^2
\le
A\bigl(|h'|^2+|g'|^2\bigr)+BK_0
\]
holds for every \(K_0\ge0\) and every weak harmonic \((K,K_0)\)-quasiregular map.

Put
\[
A_0(K)=\frac{2K^2}{K^2+1}.
\]
The complete admissible region is
\[
\left\{(A,B):A\ge2,\ B\ge0\right\}
\cup
\left\{(A,B):A_0(K)\le A\le2,\ B\ge B_K(A)\right\},
\]
where
\[
B_K(A)
=
\frac{A-\sqrt{A((K^2+1)A-2K^2)}}{K^2}.
\]
No finite value of \(B\) works when
\[
A<A_0(K).
\]

Every point on the curved boundary is attained by an affine harmonic map. In particular, the coefficient pair
\[
\left(
\frac{2K^2}{K^2+1},
\frac{2}{K^2+1}
\right)
\]
used in the recent sharp-constant paper is the left endpoint of a full exact energy–defect tradeoff, and
\[
(2,0)
\]
is the right endpoint.

## Assumptions and scope

The weak quasiregular class and notation are those of Chen, Huang, Jin and Li. Nonnegative Jacobian gives
\[
|h'|\ge|g'|.
\]
Define the minimal stretch
\[
\lambda_f=|h'|-|g'|.
\]
Then
\[
J_f=\Lambda_f\lambda_f
\]
and
\[
|h'|^2+|g'|^2
=
\frac{\Lambda_f^2+\lambda_f^2}{2}.
\]

The theorem classifies constants that work uniformly for every additive parameter \(K_0\ge0\). It is a local pointwise statement; it does not optimize the global Hardy-space constants proved in the source.

## Proof

Fix a point. If
\[
\Lambda_f=0,
\]
the desired estimate is automatic whenever \(B\ge0\). Assume henceforth that
\[
\Lambda_f>0
\]
and put
\[
x=\frac{\lambda_f}{\Lambda_f}\in[0,1],
\qquad
t=\frac{K_0}{\Lambda_f^2}.
\]
The weak quasiregular condition becomes
\[
1\le Kx+t,
\]
so the smallest permitted defect is
\[
t_{\min}(x)=\max\{0,1-Kx\}.
\]
The proposed energy–defect inequality is equivalent to
\[
1
\le
\frac A2(1+x^2)+Bt.
\]

First consider
\[
x\ge\frac1K.
\]
Here the class permits
\[
t=0.
\]
Thus a universal estimate requires
\[
1\le\frac A2\left(1+\frac1{K^2}\right),
\]
or equivalently
\[
A\ge A_0(K)=\frac{2K^2}{K^2+1}.
\]
This condition is also sufficient on the whole interval \(x\ge1/K\), because the energy factor \((1+x^2)/2\) is increasing there.

Now let
\[
0\le x<\frac1K.
\]
For nonnegative \(B\), the worst allowed value of \(t\) is
\[
t=1-Kx.
\]
Hence one needs
\[
B
\ge
\phi_A(x)
:=
\frac{1-\frac A2(1+x^2)}{1-Kx}.
\]
For
\[
A_0(K)\le A\le2,
\]
the derivative has the sign of
\[
AKx^2-2Ax+K(2-A).
\]
The unique maximizing critical point in \([0,1/K]\) is
\[
x_A
=
\frac{A-\sqrt{A((K^2+1)A-2K^2)}}{KA}.
\]
At that point the critical-point equation simplifies the value to
\[
\phi_A(x_A)
=
\frac{Ax_A}{K}
=
\frac{A-\sqrt{A((K^2+1)A-2K^2)}}{K^2}
=B_K(A).
\]
Therefore
\[
B\ge B_K(A)
\]
is necessary and sufficient throughout the curved regime.

At
\[
A=A_0(K),
\]
one has
\[
x_A=\frac1K,
\qquad
B_K(A)=\frac{2}{K^2+1}.
\]
At
\[
A=2,
\]
one has
\[
x_A=0,
\qquad
B_K(A)=0.
\]
For
\[
A\ge2,
\]
the elementary inequality
\[
|h'|^2+|g'|^2
\ge
\frac{\Lambda_f^2}{2}
\]
already proves the estimate with
\[
B=0.
\]

It remains to prove sharpness.

If
\[
A<A_0(K),
\]
choose an affine map with constant stretches satisfying
\[
\frac{\lambda_f}{\Lambda_f}=\frac1K
\]
and take
\[
K_0=0.
\]
Then the weak quasiregular condition is an equality and
\[
\frac{\Lambda_f^2}{|h'|^2+|g'|^2}
=A_0(K),
\]
so no choice of \(B\) can repair the failed energy coefficient.

For
\[
A_0(K)\le A\le2,
\]
fix \(L>0\) and define the affine harmonic map by the constant derivatives
\[
h'
=
\frac{L(1+x_A)}2,
\qquad
g'
=
\frac{L(1-x_A)}2.
\]
Set
\[
K_0=L^2(1-Kx_A).
\]
Then
\[
\Lambda_f=L,
\qquad
\lambda_f=Lx_A,
\]
and
\[
\Lambda_f^2=K\Lambda_f\lambda_f+K_0.
\]
Thus the defining weak quasiregular inequality is saturated. The equality
\[
B_K(A)=\phi_A(x_A)
\]
then shows that the proposed energy–defect estimate is also saturated. Every point of the frontier is therefore an actual affine extremal.

Finally, a universally admissible pair must satisfy
\[
B\ge0,
\]
because the zero map belongs to the class for every \(K_0>0\). This completes the classification.

## Verification

The primary paper was inspected through its definition of weak harmonic \((K,K_0)\)-quasiregularity and the proof step in which it derives
\[
\Lambda_f^2
\le
\frac{2K^2}{K^2+1}
\bigl(|h'|^2+|g'|^2\bigr)
+
\frac{2K_0}{K^2+1}.
\]
That inequality is exactly the left endpoint of the frontier above.

The optimization is one-dimensional after the scale-free substitution
\[
x=\lambda_f/\Lambda_f.
\]
The derivative of \(\phi_A\) and the simplification of its critical value were checked symbolically and then reconstructed algebraically in the proof. The sharpness witnesses are affine, so there is no hidden approximation or limiting argument.

The broader literature inspected for harmonic quasiregular maps concerns conjugate-function, Riesz, Kolmogorov, Zygmund, or boundary-growth estimates. Those results use the same distortion class or the homogeneous \(K_0=0\) subclass, but they do not state this complete local coefficient tradeoff.

## Relationship to prior work

Chen, Huang, Jin and Li introduce the weak harmonic \((K,K_0)\)-quasiregular framework in their sharp-constant analysis and derive the particular coefficient pair
\[
\left(
\frac{2K^2}{K^2+1},
\frac{2}{K^2+1}
\right)
\]
as a local estimate used downstream in Hardy-space arguments. Their stated goals are global sharp-constant problems, and no full energy-versus-defect coefficient region is given.

Chen and Kalaj study the same inhomogeneous quasiregular class in conjugate-function problems. Their results are global Riesz-, Kolmogorov-, and Zygmund-type statements rather than a pointwise Pareto optimization of the local differential inequality.

Earlier work of Kalaj treats the homogeneous harmonic quasiregular case and global Riesz/Kolmogorov inequalities. It does not contain the additive \(K_0\) coefficient tradeoff.

The present classification shows that the source coefficient pair is not an isolated algebraic choice: it is one extremal endpoint of a continuous, sharp frontier joining it to the defect-free Euclidean bound.

## Limitations

The theorem optimizes only inequalities linear in the two quantities
\[
|h'|^2+|g'|^2
\quad\text{and}\quad
K_0.
\]
It does not claim optimal constants for nonlinear combinations or for global Hardy-space estimates.

The result is planar and harmonic, using the two singular values
\[
\Lambda_f
\quad\text{and}\quad
\lambda_f.
\]
No higher-dimensional analogue is asserted.

## References

1. S. Chen, M. Huang, L. Jin and Q. Li, *Sharp constant problems for harmonic mappings*, arXiv:2609.33159v1, 2026.
2. S. Chen and D. Kalaj, *Conjugate type properties of harmonic \((K,K')\)-quasiregular mappings*, arXiv:2509.17578v1, 2025.
3. D. Kalaj, *Riesz and Kolmogorov inequality for harmonic quasiregular mappings*, Journal of Mathematical Analysis and Applications 542 (2025), Article 128767. DOI: 10.1016/j.jmaa.2024.128767.
