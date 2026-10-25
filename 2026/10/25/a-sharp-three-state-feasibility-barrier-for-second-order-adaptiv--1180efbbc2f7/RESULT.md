# A sharp three-state feasibility barrier for second-order adaptive SSPRK(3,3) weights

## Finding
Fix the three-stage SSPRK(3,3) stage matrix
\[
A=\begin{pmatrix}0&0&0\\1&0&0\\1/4&1/4&0\end{pmatrix},
\qquad c=(0,1,1/2)^{\mathsf T}.
\]
Retain its ordinary first- and second-order Runge--Kutta weight conditions while allowing the endpoint weights to depend on the step. Every such real weight vector is
\[
\widetilde b(v)=\left((1-v)/2,(1-v)/2,v\right)^{\mathsf T},\qquad v\in\mathbb R.
\]
For a real column-conservative Markov generator \(Q\), write the resulting one-step matrix as \(P_{h,v}(Q)\). Endpoint positivity means that this matrix is entrywise nonnegative, equivalently that it maps **every** nonnegative starting vector to a nonnegative vector. The weight-simplex requirement means \(\widetilde b(v)\ge0\), or \(0\le v\le1\).

**Sharp dimension contrast.** For every two-state continuous-time Markov generator \(Q\) and every step \(h\ge0\), there exists \(v\in[0,1]\) for which \(P_{h,v}(Q)\) is entrywise nonnegative and column stochastic. For the equal-rate three-state pure-birth generator
\[
Q_{\lambda}=\lambda\begin{pmatrix}-1&0&0\\1&-1&0\\0&1&0\end{pmatrix},\qquad\lambda>0,
\]
there exists such a weight vector if and only if \(0\le\lambda h\le4\). More strongly, if \(\lambda h>4\), **no real** second-order weight vector (even with negative components) gives a nonnegative endpoint from the first pure state. At \(\lambda h=4\), the sole feasible second-order weights are \((3/8,3/8,1/4)^{\mathsf T}\), and the complete endpoint matrix is the identity.

Thus three states are the minimum dimension for an unavoidable endpoint-positivity infeasibility in this adaptive-weight family. At its last feasible step the three-state method takes a physically stagnant step, although the exact birth process moves mass strictly forward.

## Assumptions and scope
We use the column-vector convention \(p'=Qp\): off-diagonal entries of \(Q\) are nonnegative and \(\mathbf 1^{\mathsf T}Q=0\). The baseline tableau is the classical explicit SSPRK(3,3) with the fixed stages above; only the endpoint weights are adapted. The retained order conditions are \(\mathbf1^{\mathsf T}\widetilde b=1\) and \(c^{\mathsf T}\widetilde b=1/2\). They mean formal order at least two for each *fixed* selected weight vector; no third-order condition is imposed. The statement concerns one-step endpoint nonnegativity, not the positivity of intermediate stages, global errors for large steps, stability of a varying-step algorithm, or an error-tolerance acceptance rule.

The three-state threshold is dimensionless: \(z=\lambda h\). For two states the rates may be unequal, zero, or both zero. All assertions use exact arithmetic; matrix inequalities are entrywise.

## Proof
**1. Weight family and stability polynomial.** The first two order conditions give
\[
\widetilde b_1+\widetilde b_2+\widetilde b_3=1,
\qquad \widetilde b_2+\widetilde b_3/2=1/2,
\]
so \(\widetilde b_1=\widetilde b_2=(1-v)/2\) and \(\widetilde b_3=v\). The stage matrix satisfies \(A^3=0\), \(\widetilde b^{\mathsf T}A\mathbf1=1/2\), and \(\widetilde b^{\mathsf T}A^2\mathbf1=v/4\). Therefore every endpoint map in the family has stability polynomial
\[
R_v(\zeta)=1+\zeta+\frac{\zeta^2}{2}+\frac{v\zeta^3}{4},
\qquad P_{h,v}(Q)=R_v(hQ).
\]

**2. Every two-state generator is feasible at every step.** Write
\[
Q=\begin{pmatrix}-a&b\\a&-b\end{pmatrix},\qquad a,b\ge0.
\]
If \(a+b=0\), the numerical map is the identity. Otherwise set \(s=h(a+b)\), and define the stationary projector
\[
\Pi=\frac{1}{a+b}\begin{pmatrix}b&b\\a&a\end{pmatrix}.
\]
Since \(Q=-(a+b)(I-\Pi)\), the exact polynomial identity
\[
P_{h,v}(Q)=\Pi+R_v(-s)(I-\Pi)
=R_v(-s)I+[1-R_v(-s)]\Pi
\]
holds. Both \(I\) and \(\Pi\) are nonnegative column-stochastic matrices, so it is enough to arrange \(0\le R_v(-s)\le1\).

For \(0\le s<2\), take \(v=0\): then \(R_v(-s)=1-s+s^2/2\in[1/2,1]\). For \(s\ge2\), take
\[
v(s)=\frac{4(1-s+s^2/2)}{s^3}.
\]
The numerator is positive, \(v(2)=1/2\), and
\[
v'(s)=-\frac{2((s-2)^2+2)}{s^4}<0.
\]
Thus \(0<v(s)\le1/2\), and substitution yields \(R_{v(s)}(-s)=0\). The numerical step is then exactly \(\Pi\). In both ranges \(0\le v\le1\) and the endpoint is nonnegative for all nonnegative inputs.

**3. Sharp three-state feasibility.** With \(z=\lambda h\), elementary matrix multiplication yields
\[
P_{h,v}(Q_\lambda)=
\begin{pmatrix}
A_z&0&0\\ B_z&A_z&0\\ C_z&1-A_z&1
\end{pmatrix},
\]
where
\[
\begin{aligned}
A_z&=1-z+z^2/2-vz^3/4,\\
B_z&=z-z^2+3vz^3/4,\\
C_z&=z^2/2-vz^3/2.
\end{aligned}
\]
For \(z>0\), endpoint positivity applied to the first pure state requires both \(B_z\ge0\) and \(C_z\ge0\). These inequalities respectively imply
\[
v\ge\frac{4(z-1)}{3z^2},\qquad v\le\frac1z.
\]
If \(z>4\), the lower bound exceeds the upper bound by \((z-4)/(3z^2)>0\). Hence no real weight satisfying the order-two conditions can produce a positive endpoint, regardless of any sign restrictions on the weights.

For \(0\le z\le1\), choose \(v=0\). Directly, \(A_z=1-z+z^2/2\ge0\), \(B_z=z(1-z)\ge0\), \(C_z=z^2/2\ge0\), and \(1-A_z=z-z^2/2\ge0\).

For \(1<z\le4\), choose
\[
v=\frac{4(z-1)}{3z^2}\in[0,1/3].
\]
Then
\[
B_z=0,\quad
A_z=\frac{z^2-4z+6}{6}=\frac{(z-2)^2+2}{6}>0,\quad
C_z=\frac{z(4-z)}6=1-A_z\ge0.
\]
All endpoint entries are nonnegative and the column sums equal one, so every nonnegative input is mapped to a nonnegative input. The weights lie in the simplex. At \(z=4\), the two necessary bounds coincide at \(v=1/4\), making the weight vector unique; substitution gives \(A_z=1\), \(B_z=C_z=0\), hence \(P_{h,1/4}(Q_\lambda)=I\).

**4. The boundary is genuine stagnation.** For the first pure state \(e_1\), the exact evolution at \(t=h>0\) is
\[
e^{hQ_\lambda}e_1=\left(e^{-z},\,z e^{-z},\,1-(1+z)e^{-z}\right)^{\mathsf T}.
\]
Its second coordinate is strictly positive for \(z>0\), while at the feasible numerical boundary \(z=4\) the entire endpoint is \(e_1\). Thus the identity step is not exact equilibration; it is a sharp positivity/accuracy tradeoff.

## Verification
The self-contained `verify.py` uses `fractions.Fraction` to reconstruct \(R_v(hQ)\) from powers of the actual two- and three-state generators. It checks the displayed three-state matrix formula, endpoint positivity at rational points on both sides of the threshold, identity at \(z=4\), and the two-state stationary-projector formula for representative reducible and irreducible chains. Execute `python verify.py` from the extracted files; success prints `VERIFY_OK`. These finite tests corroborate the algebra, but the for-all-steps and for-all-generators assertions follow from the inequalities and projector identity above, not from the tests.

## Relationship to prior work
Nüßlein, Ranocha, and Ketcheson (2020/2021) introduce endpoint weight adaptation with linear order constraints, include this SSPRK(3,3) tableau in their two-state Example I, and explain that feasibility of the positivity linear program is not guaranteed. Their Example I derives the one-dimensional weight family at one specified two-state step, but does not give the all-two-state versus three-state sharp feasibility theorem or the unavoidable infeasibility for \(z>4\) even with unrestricted real weights.

Horváth (2005) studies positivity thresholds for fixed Runge--Kutta schemes and invariant cones. Its general worst-case positivity-radius statements concern a different quantifier order: a fixed tableau across problems and steps, rather than *existence of step-dependent weights for this fixed stage matrix on a specified Markov generator*. Thus its worst-case threshold theory does not imply the feasibility interval above.

Higueras, Ketcheson, and Kocsis (2015/2018) optimize downwind-operator perturbations and absolute-monotonicity radii. Their perturbations modify operator evaluations; they do not classify the scalar endpoint-weight family for the pure-birth generator. A separate public exact result for a *two-stage implicit* SSP-SDIRK scheme also has a two-state/three-state contrast and a threshold of \(4\), but its rational stability function and fixed weights are different; equality of the number \(4\) does not imply this explicit adaptive-weight claim.

## Limitations
The claims concern the feasible *constraint set*, not a guarantee that a particular linear-program objective, error estimator, or step-acceptance tolerance will choose the exhibited weights. Some large-step stage vectors can be negative even when the endpoints are nonnegative; the generator is linear so the stage evaluations remain well-defined. The order-two constraints do not guarantee useful accuracy for large steps: the three-state endpoint freezes at its sharp boundary, and the displayed two-state construction equilibrates in one step for sufficiently large steps. No assertions are made for nonlinear kinetics, time-dependent generators, higher-order adaptation, or numerical roundoff. Closely related older positivity-threshold literature may contain unindexed specializations; distinct mechanisms have been compared, but absolute priority is not asserted.

## References
1. S. Nüßlein, H. Ranocha and D. I. Ketcheson, *Positivity-Preserving Adaptive Runge--Kutta Methods*, arXiv:2005.06268v1, publicly posted 13 May 2020; *Communications in Applied Mathematics and Computational Science* 16 (2021), 155--179. https://arxiv.org/abs/2005.06268
2. Z. Horváth, *On the positivity step size threshold of Runge--Kutta methods*, *Applied Numerical Mathematics* 53 (2005), 341--356. https://doi.org/10.1016/j.apnum.2004.08.026
3. I. Higueras, D. I. Ketcheson and T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge--Kutta method*, arXiv:1505.04024 (2015); *Journal of Scientific Computing* 76 (2018), 1337--1369. https://arxiv.org/abs/1505.04024
4. *Two-state immunity and three-state sharpness for endpoint positivity of SSP-SDIRK2(2)*, publicly indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-two-state-immunity-and-three-state-sharpness-for-endpoint-positi--46bf11cc19c7
