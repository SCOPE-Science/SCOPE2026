# Exact line-search deadlock in rapid gradient descent for low-rank recovery
## Finding

The rapid-gradient line search of Zhang--Wang--Zhu can fail to possess any nonzero acceptable step, even for a one-dimensional rank-one recovery problem.

Consider
\[
F(u,v)=\frac12(uv-\rho)^2,
\]
with scalar target
\[
0<\rho<\rho_\star,
\qquad
\rho_\star=\left(\frac{5184}{83521}\right)^{1/3}.
\]
Choose
\[
u=\left(\frac{17\rho}{6}\right)^2,
\qquad
v=\left(\frac{17\rho}{12}\right)^2.
\]
Both factors are positive. Therefore the source rapid gradient, specialized from its diagonal-quarter-power formula, is
\[
G_u=u\sqrt v-\rho v,
\qquad
G_v=v\sqrt u-\rho u.
\]
At the displayed point this becomes
\[
G_u=\frac{2023}{216}\rho^3,
\qquad
G_v=-\frac{2023}{864}\rho^3.
\]
These two components are nonzero and have opposite signs.

Nevertheless, for every
\[
\alpha\ne0,
\]
one has the strict reverse of the source acceptance test:
\[
F(u+\alpha G_u,v+\alpha G_v)>F(u,v).
\]
In particular, Algorithm 1 Step 3 cannot find any
\[
\alpha\in[-1,0)\cup(0,1]
\]
satisfying its required monotone inequality.

The obstruction is not caused by a large step. The rapid direction is first-order tangent to the current objective level set and has the wrong second-order curvature. Thus arbitrarily small positive and negative steps both increase the objective.

For a fully rational witness, take
\[
\rho=\frac14,
\qquad
u=\frac{289}{576},
\qquad
v=\frac{289}{2304}.
\]
Then
\[
G_u=\frac{2023}{13824},
\qquad
G_v=-\frac{2023}{55296},
\]
and the same strict increase holds for every nonzero real \(\alpha\).

Because the source prescribes an initial step parameter strictly larger than its fallback threshold, this witness reaches the rapid-gradient branch at the first iteration. The fallback to the true gradient is therefore not reached: a previous accepted small step does not exist yet.

A minimal well-definedness repair is to fall back immediately to the true negative gradient whenever the rapid direction fails a strict descent test, or whenever the rapid line search fails to return a nonzero decreasing step.

## Assumptions and scope

The example uses the source objective and its rapid-gradient formula exactly in the case
\[
m=n=r=1.
\]
The scalar target is positive and the factors are positive, so the quarter power of the scalar diagonal term has no sign ambiguity:
\[
(v^2)^{1/4}=\sqrt v,
\qquad
(u^2)^{1/4}=\sqrt u.
\]

The claim concerns Lemma 1 and the well-definedness of Step 3 of Algorithm 1. It does not assert that every initialization fails, nor that a version with an immediate true-gradient safeguard cannot converge.

The source objective is written as one half of the squared Frobenius residual and its gradient formula is the corresponding gradient. Multiplying the objective by a positive constant would not change the strict line-search obstruction.

No global smoothness assumption is needed for the counterexample. The failure occurs algebraically at the very first rapid-gradient line search.

## Proof

Write the scalar residual as
\[
R=uv-\rho.
\]
At
\[
u=\frac{289}{36}\rho^2,
\qquad
v=\frac{289}{144}\rho^2,
\]
the source rapid-gradient components are
\[
G_u=u\sqrt v-\rho v
=\frac{2023}{216}\rho^3
\]
and
\[
G_v=v\sqrt u-\rho u
=-\frac{2023}{864}\rho^3.
\]
A direct calculation gives
\[
vG_u+uG_v=0.
\]
Since
\[
\nabla F(u,v)=R(v,u),
\]
the directional derivative is exactly
\[
\nabla F(u,v)^{\mathsf T}G
=R(vG_u+uG_v)
=0.
\]
Thus this is not a strict descent direction.

The residual along the line is exactly quadratic:
\[
\begin{aligned}
R(\alpha)
&=(u+\alpha G_u)(v+\alpha G_v)-\rho\\
&=R+\alpha(vG_u+uG_v)+\alpha^2G_uG_v\\
&=R+C\alpha^2,
\end{aligned}
\]
where
\[
C=G_uG_v
=-\frac{4092529}{186624}\rho^6<0.
\]
The initial residual is
\[
R
=\frac{83521}{5184}\rho^4-\rho
=\rho\left(\frac{83521}{5184}\rho^3-1\right).
\]
The assumed range \(0<\rho<\rho_\star\) makes
\[
R<0.
\]
Therefore, for every \(\alpha\ne0\),
\[
R(\alpha)=R+C\alpha^2<R<0.
\]
Consequently
\[
|R(\alpha)|>|R|
\]
and hence
\[
F(u+\alpha G_u,v+\alpha G_v)
=\frac12R(\alpha)^2
>\frac12R^2
=F(u,v).
\]
This proves failure not merely for the source interval but for every nonzero real step.

The true gradient is nonzero because
\[
R<0,
\qquad
u>0,
\qquad
v>0.
\]
Hence an immediate fallback to
\[
-\nabla F(u,v)
\]
would supply a genuine descent direction. The obstruction is therefore specific to the rapid-direction branch and its delayed safeguard logic.

## Verification

The standalone script `artifacts/verify_line_search_deadlock.py` uses exact rational arithmetic for the witness \(\rho=1/4\). It verifies the source rapid-gradient components, zero first directional derivative, negative residual, negative quadratic line coefficient, and the exact positive polynomial for the objective increase.

It also symbolically checks the parameterized family and the threshold
\[
\rho_\star=\left(\frac{5184}{83521}\right)^{1/3}.
\]
The universal claim for all nonzero real steps is proved analytically above; finite numerical sampling is not used as a substitute for that argument.

## Relationship to prior work

The primary paper explicitly notes that its rapid approximation need not be a descent direction, but Algorithm 1 still requires Step 3 to find a nonzero step with nonincreasing objective, and Lemma 1 claims such a step exists. Its fallback to the exact negative gradient is activated only after a previously selected step becomes sufficiently small. The family above shows a different failure mode: at the very first rapid-gradient call, no nonzero acceptable step exists at all.

Prior analyses of asymmetric low-rank factorization study the same product objective with the true gradient. Ye--Du emphasize factor unbalancedness and analyze vanilla gradient descent through trajectory control. Ma--Li--Chi analyze balancing-free true-gradient descent for matrix sensing under spectral initialization and restricted-isometry structure. Neither inspected line of work uses the rapid direction of the 2026 paper or implies the exact tangential no-step family above.

Targeted searches using the primary article identifier, the rapid-gradient formula, line-search existence, zero directional derivative, and low-rank factor aliases did not locate a published correction or an equivalent counterexample.

## Limitations

The construction is scalar and deliberately targets the well-definedness claim of the rapid-gradient branch. It does not establish failure on generic high-dimensional random initializations.

The witness is a codimension-one directional degeneracy, although it belongs to a continuous one-parameter family in the target \(\rho\). Perturbations can change the first directional derivative and therefore require a separate robustness analysis.

The proposed immediate fallback is a well-definedness safeguard, not a complete replacement convergence theorem for the rapid method.

## References

1. Y. Zhang, P. Wang, D. Zhu, *Rapid Gradient Descent Method for Low-Rank Matrix Recovery*, Mathematics 14(2), 343, 20 January 2026. DOI: 10.3390/math14020343.
2. T. Ye, S. S. Du, *Global Convergence of Gradient Descent for Asymmetric Low-Rank Matrix Factorization*, arXiv:2106.14289, 2021.
3. C. Ma, Y. Li, Y. Chi, *Beyond Procrustes: Balancing-Free Gradient Descent for Asymmetric Low-Rank Matrix Sensing*, IEEE Transactions on Signal Processing 69, 2021. DOI: 10.1109/TSP.2021.3051425.
