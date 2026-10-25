# Sharp equilibrium-ratio maximum-principle frontier for two-cell Patankar–Runge–Kutta diffusion

## Finding

For the original two-stage, second-order modified Patankar–Runge–Kutta (MPRK) update on any irreducible two-state conservative linear diffusion, **unconditional preservation of the equilibrium-weighted upper maximum principle holds if and only if the larger equilibrium mass is at most the inverse golden ratio**:
\[
\max\{\pi_1,\pi_2\}\le\rho:=\frac{\sqrt5-1}{2}.
\]
If the larger equilibrium mass exceeds \(\rho\), strictly positive initial data and a finite positive step exist for which
\[
\max_i\frac{x_i^+}{\pi_i}>\max_i\frac{x_i}{\pi_i},
\]
even though the update preserves mass, strict positivity and the exact equilibrium. The result gives a sharp two-cell range-preservation criterion for Chang–Cooper spatial discretizations advanced by this MPRK method. The usual continuous-time Markov flow and implicit Euler preserve this equilibrium-ratio maximum for all equilibrium masses and all positive times or steps.

In addition, for each non-equilibrium input, the signed error amplification factor is a **strictly decreasing function of the dimensionless time step**, from \(1\) to an explicit negative limit. Crossing equilibrium under very large steps is thus not the same as violating the weighted maximum principle: the latter needs sufficiently asymmetric equilibrium masses.

## Assumptions and scope

Let \(a,b>0\), \(Q=\begin{psmallmatrix}-a&b\\a&-b\end{psmallmatrix}\), and \(\pi=(p,q)^{\mathsf T}\), where \(p=b/(a+b)\), \(q=a/(a+b)=1-p\). Start from \(x=(u,1-u)^{\mathsf T}\), with \(0<u<1\). Put \(s=h(a+b)>0\). For the conservative production rates \(p_{12}(x)=b x_2\) and \(p_{21}(x)=a x_1\), take the **specific original Heun-based MPRK** stage and step
\[
 y=(I-hQ)^{-1}x,\qquad
 x^+=\left[I-\frac h2 Q\operatorname{diag}\left(1+\frac{x_1}{y_1},1+\frac{x_2}{y_2}\right)\right]^{-1}x.
\]
The quotient is componentwise. This is the stage/endpoint prescription of the source's second-order MPRK equations, not a claim about arbitrary members of the larger MPRK family.

For a two-node Chang–Cooper no-flux spatial grid with constant positive diffusion and constant drift, the interfacial flux equals \(A x_2-B x_1\) with \(A,B>0\) and \(A/B=e^{\lambda}\), where \(\lambda\) is the interfacial drift-to-diffusion ratio. Therefore \(p=A/(A+B)=1/(1+e^{-\lambda})\) ranges through all \((0,1)\). After absorbing the cell size in the rates, the theorem applies to every such two-cell semidiscretization.

Define the equilibrium-weighted upper maximum \(\mathcal M_\pi(x)=\max\{x_1/p,x_2/q\}\). The assertion is uniform over *all* \(a,b>0\), every strictly positive unit-mass input \(x\), and *every finite* \(h>0\). The sharpness statement asserts existence, not violation at every input or step.

## Proof

**Step 1: exact reduction.** Write \(\delta=u-p\in(-p,q)\). The first stage is
\[
 y_1=p+\frac{\delta}{1+s},\qquad y_2=q-\frac{\delta}{1+s}.
\]
Set \(r_i=1+x_i/y_i\). Conservation of the endpoint system and direct elimination give
\[
 x_1^+=\frac{u+(s/2)p r_2}{1+(s/2)(q r_1+p r_2)},\qquad x_2^+=1-x_1^+.
\]
For \(\delta\ne0\) define \(R(s,p,u)=(x_1^+-p)/\delta\). Put
\[
 B=1+\frac{(q-p)\delta}{pq},\qquad E=\frac{u(1-u)}{pq}.
\]
Notice \(E>0\), \(B-E=\delta^2/(pq)\ge0\), hence \(B>0\). Algebraic cancellation yields
\[
 R(s,p,u)=\frac{N(s)}{D(s)},\qquad
 N(s)=2(E+Bs)+s(1+s)(2-s),
\]
\[
 D(s)=(s^2+2s+2)(E+Bs)+s(1+s)(s+2)>0.
\]
The same formula extends continuously to \(\delta=0\) as a local error amplification factor. The equilibrium itself is fixed.

**Step 2: strictly monotone amplification.** Exact polynomial multiplication gives \(N'D-ND'=-H\), where
\[
\begin{aligned}
H={}&(3B+E+4)s^4+(4B^2+12B+4E+8)s^3\\
&+(4B^2+8BE+8B+12E+4)s^2\\
&+(8BE+4E^2+8E)s+4E^2.
\end{aligned}
\]
Every coefficient is strictly positive. Thus \(\partial_s R=-H/D^2<0\) for \(s>0\). Directly,
\[
 R(0,p,u)=1,\qquad
 \lim_{s\to\infty}R(s,p,u)=-\frac{1}{1+B}
 =-\frac{1}{2+(q-p)\delta/(pq)}<0.
\]
For each non-equilibrium input, there is exactly one positive step at which the iterate first crosses equilibrium.

**Step 3: sharp weighted maximum criterion.** For \(\delta>0\), the initial maximum is \(1+\delta/p\). By \(R\le1\), the first updated ratio cannot exceed it. The second updated ratio is \(1-\delta R/q\), which exceeds the original maximum precisely if \(-R>q/p\). Strict monotonicity in \(s\) shows that this happens at some finite \(s>0\) if and only if
\[
 \frac1{2+(q-p)\delta/(pq)}>\frac qp.
\]
If \(p\ge q\), the left-hand side increases with \(\delta\in(0,q)\), and its supremum, as \(\delta\uparrow q\), is \(p\). Hence such a positive \(\delta\) exists exactly when \(p>q/p\), equivalently \(p^2+p-1>0\), or \(p>\rho\). If \(p<q\), the left-hand side is at most \(1/2\), whereas \(q/p>1\), so there is no violation for \(\delta>0\). Interchanging the two coordinates covers \(\delta<0\) and yields the criterion \(q>\rho\). Thus the update preserves \(\mathcal M_\pi\) for every input and positive step if and only if \(\max(p,q)\le\rho\). Equality produces no strict violation because the critical supremum is approached only at an excluded zero coordinate and infinite time step.

**Step 4: strict interior witness.** Take \(p=3/4\), \(q=1/4\), \(u=9/10\), \(s=10\) (so \(a=1/4,b=3/4,h=10\)). Then
\[
 y=(42/55,13/55),\qquad
 x^+=(15134/21985,6851/21985),
\]
and, exactly,
\[
 \mathcal M_\pi(x)=6/5,\qquad
 \mathcal M_\pi(x^+)=27404/21985>6/5.
\]
All states have strictly positive entries, and all fractions are exact.

## Verification

Run `python3 verify_mprk_bound.py` with the Python standard library. It formally checks the polynomial identity for \(N'D-ND'\) coefficient by coefficient using a multivariate sparse polynomial representation. It independently reconstructs the rational update and amplification formula for 5920 positive rational parameter combinations and checks the strictly interior rational witness. The universal inequalities in this theorem follow from Steps 2–3, **not** from this finite parameter grid. All packaged paths refer to files in this result.

## Relationship to prior work

Bartel, Lampert and Ranocha (arXiv:2404.07641v1, Section 3) combine Chang–Cooper spatial discretization with the original MPRK scheme, proving positivity and conservation and motivating preservation of stationary states; they do not assert the above equilibrium-weighted maximum criterion. Kopecz and Meister (arXiv:1702.04589v1, Section 1) give the same original second-order MPRK construction and its order/positivity properties. Torlo, Öffner and Ranocha (arXiv:2108.07347v5, Sections 3–4 and Appendix) study two-state Patankar oscillations and give a general rational endpoint representation; their sharp oscillation-free step bound is different from this **all-step weighted maximum principle classification**. Their known equilibrium-crossing phenomenon and explicit scheme formulas are not claimed as new. Izgin, Kopecz and Meister (arXiv:2202.11649) investigate local stability of MPRK families, not a global equilibrium-ratio maximum bound.

A general rational formula for the same endpoint is prior work and is sufficient input for an independent algebraic derivation. The assessed new mathematical statement is the complete universal golden-ratio mass frontier and its global step-size comparison. A logically equivalent formulation hidden in other Patankar literature cannot be ruled out.

## Limitations

The proof is for the specified second-order, two-stage original MPRK method and two-dimensional conservative linear systems, not for general nonlinear Chang–Cooper semidiscretizations, more than two cells, or every method labeled MPRK. The upper maximum \(\mathcal M_\pi\) is equilibrium-relative; it is not ordinary componentwise positivity, mass conservation or the separate no-equilibrium-overshoot property. The theorem establishes no new global convergence rate or entropy theorem. The limiting examples use finite positive steps and strictly positive initial data; the zero-coordinate and infinite-step cases are limits only. Publication priority remains subject to wider specialist literature review.

## References

1. H. Bartel, J. Lampert, H. Ranocha, *Structure-Preserving Numerical Methods for Fokker–Planck Equations*, arXiv:2404.07641v1 (first posted 2024-04-11), Section 3; also v3 for clarified stage notation. https://arxiv.org/html/2404.07641v1
2. D. Torlo, P. Öffner, H. Ranocha, *Issues with Positivity-Preserving Patankar-type Schemes*, arXiv:2108.07347v5 (first posted 2021-08-16), Sections 3–4 and supplementary Section 2. https://arxiv.org/html/2108.07347v5
3. S. Kopecz, A. Meister, *On order conditions for modified Patankar–Runge–Kutta schemes*, arXiv:1702.04589v1 (first posted 2017-02-15), Sections 1–3. https://arxiv.org/html/1702.04589v1
4. T. Izgin, S. Kopecz, A. Meister, *On the Stability of Unconditionally Positive and Linear Invariants Preserving Time Integration Schemes*, arXiv:2202.11649 (first posted 2022-02-23). https://arxiv.org/abs/2202.11649
