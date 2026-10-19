# Sharp phase-uniform fixed-point multiplicity threshold for the saturating Ikeda map

## Finding
For every \(0<u<1\) consider the complex-plane diffeomorphism
\[
I_{u,\eta,\kappa}(z)=1+u z\exp\!\left(i\left[\kappa-\frac{\eta}{1+|z|^2}\right]\right),
\qquad z\in\mathbb C,
\]
with real nonlinear phase coefficient \(\eta\) and phase offset \(\kappa\). Define
\[
 v_*(u)=\frac{\sqrt{(2+u^2)^2+32u^2}-(2+u^2)}2,
 \quad t_*(u)=1+u^2-v_*(u),
\]
\[
\boxed{\ E(u)=\frac{(1+t_*(u))^2}{\sqrt{4u^2-v_*(u)^2}}\ }.
\]
The following is a sharp, parameter-wide fixed-point multiplicity transition.

**Uniform uniqueness.** For every \(\kappa\in\mathbb R\), if \(|\eta|<E(u)\), the map has exactly one fixed point in \(\mathbb C\).

**Achievable multiplicity.** For every \(|\eta|>E(u)\), some \(\kappa\in\mathbb R\) makes the map have at least three distinct fixed points. The threshold \(E(u)\) is therefore the exact infimum of nonlinear phase strength at which an appropriate phase offset can produce multiple fixed points. It is not just a sufficient contraction bound.

For orientation, \(E(1/5)\approx9.632666335688\), \(E(1/2)\approx3.361751062772\), and \(E(9/10)\approx1.724719567145\).

## Assumptions and scope
The forcing amplitude is exactly one, \(0<u<1\), and \(\eta,\kappa\) are unrestricted reals. The fixed-point count is of distinct complex points, not stable fixed points or attractors. The assertions use strict inequalities and do not classify the equality case \(|\eta|=E(u)\). Negative \(\eta\) follows from complex conjugation with reversal of \(\kappa\).

## Proof
Let \(r=|z|\). For a given \(r>0\), a fixed point is necessarily
\[
z=\bigl(1-u e^{i\theta(r)}\bigr)^{-1},\qquad
\theta(r)=\kappa-\eta/(1+r^2).
\]
Thus fixed points correspond bijectively to positive roots of
\[
F(r)=r^2\bigl(1+u^2-2u\cos\theta(r)\bigr)-1=0.
\]
Every root lies in the compact interval \(r_-=(1+u)^{-1}\le r\le r_+=(1-u)^{-1}\). Moreover \(F(r_-)\le0\) and \(F(r_+)\ge0\), so some fixed point always exists. At each root,
\[
F'(r)=\frac2r+\frac{4u\eta r^3\sin\theta(r)}{(1+r^2)^2}.
\]
If \(F'(r)\le0\) at a root, necessarily \(\eta\ne0\) and \(\sin\theta\ne0\). Put \(t=r^{-2}\). From the root equation,
\[
\cos\theta=\frac{1+u^2-t}{2u},\quad
(1-u)^2\le t\le(1+u)^2.
\]
Consequently nonpositive derivative requires
\[
|\eta|\ge M_u(t):=
\frac{(1+t)^2}{\sqrt{4u^2-(1+u^2-t)^2}},
\qquad (1-u)^2<t<(1+u)^2.
\]
The function \(M_u\) tends to infinity at both endpoints. Its logarithmic derivative has the sign of
\[
Q(t)=8u^2-v^2-(2+u^2)v,\qquad v=1+u^2-t.
\]
The quadratic equation \(v^2+(2+u^2)v-8u^2=0\) has exactly one root in \((-2u,2u)\): its positive root \(v_*(u)\). Its other root is less than \(-2u\). Therefore \(M_u\) decreases to the unique global minimum \(E(u)=M_u(t_*)\) and then increases.

If \(|\eta|<E(u)\), every zero of \(F\) is simple with positive derivative. A continuous differentiable function with \(F(r_-)\le0\), \(F(r_+)\ge0\) cannot have two distinct positive-derivative zeros without an intervening zero of nonpositive derivative. (The endpoint cases obey the same one-sided crossing argument.) Hence there is exactly one fixed point for every phase.

Conversely fix \(|\eta|>E(u)\) and let \(r_0=t_*^{-1/2}\). Set \(v=v_*(u)\) and choose an angle \(\theta_0\) satisfying
\[
\cos\theta_0=v/(2u),\qquad
\sin\theta_0=-\operatorname{sgn}(\eta)\sqrt{1-v^2/(4u^2)}.
\]
Choose \(\kappa=\theta_0+\eta/(1+r_0^2)\). The scalar equation has a root at \(r_0\) and
\[
F'(r_0)=\frac2{r_0}\left(1-\frac{|\eta|}{E(u)}\right)<0.
\]
The endpoint signs ensure a root strictly on each side of this negative-crossing root, except possibly at a boundary radius, which itself represents a distinct root. Indeed an arbitrarily small phase perturbation, preserving the negative-crossing root by the implicit-function theorem, makes the endpoint signs strict. Hence some phase produces at least three distinct roots and therefore three distinct fixed points. This completes both statements. \(\square\)

## Verification
Run `python3 verify.py` after installing the packages in `requirements.txt`. The script checks the derivative reduction and optimizing quadratic exactly with SymPy, then constructs an explicit negative-crossing fixed point above the threshold at three values of \(u\), finds three distinct numerical scalar roots in each case, and samples 27 phase values below threshold for each case. The numerical tests are not used to establish the quantified theorem; the preceding proof treats every admissible parameter.

## Relationship to prior work
Ikeda's 1979 optical-cavity article explains multiple-valued stationary responses with an absorber and a more elaborate dynamical constitutive relation, rather than giving this exact phase-uniform threshold for the stated rational-phase plane map. Osipenko's 2007 *Dynamical Systems, Graphs, and Algorithms*, chapter 16, uses precisely the rational-phase Ikeda map and discusses fixed-point and attractor multiplicity through numerical parameter illustrations, but its retrieved analytical introduction and illustrative cases do not supply the above global offset-uniform radical threshold. Prior literature already establishes the existence of multiple fixed points; the contribution here is the exact minimizing shear and sharp universal existence/uniqueness divide. The 2007 chapter was not inspected in its entirety, a residual priority risk rather than proof of noncoverage.

## Limitations
Uniqueness of a fixed point does not establish its dynamical stability or global attraction. The conclusion above threshold is existence of a suitable phase with **at least** three fixed points, not an exact maximum for every phase. The equality case is deliberately excluded. A related uninspected derivation in historical optical bistability literature cannot be ruled out by the searches performed. No independent audit is claimed.

## References
1. K. Ikeda, “Multiple-valued stationary state and its instability of the transmitted light by a ring cavity system,” *Optics Communications* **30** (1979), 257–261, DOI: `10.1016/0030-4018(79)90090-7`. Full text: `https://bdt.semi.ac.cn/download/0.5763648799957831.pdf`.
2. G. Osipenko, *Dynamical Systems, Graphs, and Algorithms*, Lecture Notes in Mathematics **1889**, Springer (2007), Chapter 16, pp. 197–218. DOI: `10.1007/3-540-35593-6`.
3. K. Ikeda, H. Daido and O. Akimoto, “Optical turbulence: chaotic behavior of transmitted light from a ring cavity,” *Physical Review Letters* **45** (1980), 709–712. DOI: `10.1103/PhysRevLett.45.709`.
