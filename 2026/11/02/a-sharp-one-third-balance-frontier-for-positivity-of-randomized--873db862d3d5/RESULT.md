# A sharp one-third balance frontier for positivity of randomized SDIRK Markov steps

## Finding
Consider the two-stage singly diagonally implicit Runge--Kutta family with Butcher matrix and weights
\[
 A_x=\begin{pmatrix}x&0\\1-2x&x\end{pmatrix},
 \qquad b=(1/2,1/2)^\mathsf T,
 \qquad X\sim\mathrm{Uniform}[1/2,1].
\]
At each step, sample a fresh independent copy of \(X\). Apply the method to the row-probability equation \(p'=pQ\), with irreducible two-state generator
\[
 Q=\begin{pmatrix}-a&a\\b&-b\end{pmatrix},\qquad a,b>0.
\]
Write \(z=h(a+b)>0\) and \(m=\min(a,b)/(a+b)\in(0,1/2]\). Let \(P_m(z)\) be the probability that the *one-step matrix*, not merely the image of a particular initial distribution, is entrywise nonnegative. Its row sums always equal one.

If \(m=1/2\), then \(P_m(z)=1\) for all \(z>0\). Otherwise define the universal-success threshold
\[
 z_0(m)=\frac{2}{1-2m}.
\]
For \(0<m<1/3\), additionally define the zero-success threshold
\[
 z_1(m)=\frac{1+m+\sqrt{(1-m)(3-m)}}{1-3m}.
\]
Then the *entire* one-step positivity law is
\[
 P_m(z)=\begin{cases}
 1,&0<z\le z_0(m),\\[2pt]
 0,&0<m<1/3\ \text{and }z\ge z_1(m),\\[2pt]
 2m+\dfrac2z-\sqrt{\dfrac{2(1-m)((1-2m)z-2)}z},&\text{otherwise}.
 \end{cases}
\]
Here the final case only applies when \(m<1/2\) and \(z>z_0(m)\), and, if \(m<1/3\), also \(z<z_1(m)\). In particular, the stiff-step limiting success probability is
\[
 \lim_{z\to\infty}P_m(z)
 =\max\!\left\{0,\,2m-\sqrt{2(1-m)(1-2m)}\right\},
\]
which is strictly positive **if and only if** \(m>1/3\), equivalently \(\max(a,b)<2\min(a,b)\). At the boundary \(m=1/3\), success is possible for every finite \(z\) but its probability tends to zero as \(z\to\infty\).

The onset of nonstochastic updates is non-Lipschitz. For every fixed \(0<m<1/2\), as \(z\downarrow z_0(m)\) from above,
\[
 1-P_m(z)=(1-2m)\sqrt{1-m}\,\sqrt{z-z_0(m)}
 +O(z-z_0(m)).
\]
For a fixed finite \(z>z_0(m)\), independent random tableau draws produce a geometrically distributed first nonstochastic one-step matrix and infinitely many such matrices almost surely. **Nevertheless**, the cumulative numerical transition matrix from time zero is entrywise strictly positive after a deterministic, finite number of steps that is uniform over all sequences of tableau draws.

## Assumptions and scope
The generator is autonomous, irreducible, and two-state; the method uses the same random parameter in both stages of each step, with independent parameters across steps. A stochastic numerical step means an entrywise nonnegative row-stochastic matrix. The time step \(h>0\) is fixed across repeated steps, and all identities are in exact arithmetic. A negative entry in a one-step matrix does not imply a negative solution for every particular initial probability vector. Strict positivity of cumulative matrices is distinct from strict positivity of each instantaneous factor.

## Proof
**1. Rational stability function.** For scalar decay \(y'=-\lambda y\) put \(z=h\lambda>0\). Solving the two lower-triangular stage equations yields the exact multiplier
\[
 r_x(z)=1-z(1/2,1/2)(I+zA_x)^{-1}(1,1)^\mathsf T
 =\frac{1+(2x-1)z+(x^2-2x+1/2)z^2}{(1+xz)^2}.
\]
Direct differentiation and factorization give, for \(z>0\) and \(1/2\le x\le1\),
\[
 \frac{\partial r_x(z)}{\partial z}
 =\frac{-1+(1-3x)z}{(1+xz)^3}<0,
 \qquad
 \frac{\partial r_x(z)}{\partial x}
 =\frac{z^3(2x-1)}{(1+xz)^3}\ge0.
\]
Both inequalities are strict away from the relevant parameter boundary. Moreover,
\[
 1-r_x(z)=\frac{z+(2x-1/2)z^2}{(1+xz)^2}>0,
 \quad
 1+r_x(z)=\frac{2+(4x-1)z+2(x-1/2)^2z^2}{(1+xz)^2}>0.
\]
Therefore \(-1<r_x(z)<1\) at every finite positive step.

**2. Exact matrix positivity test.** Let \(\lambda=a+b\), \(\pi=(b,a)/\lambda\), and \(\Pi=\mathbf1\pi\). Then \(\Pi^2=\Pi\), \(Q=-\lambda(I-\Pi)\), and rational functional calculus gives
\[
 M_x(z)=\Pi+r_x(z)(I-\Pi)
 =\begin{pmatrix}
 \pi_1+\pi_2r_x(z)&\pi_2(1-r_x(z))\\
 \pi_1(1-r_x(z))&\pi_2+\pi_1r_x(z)
 \end{pmatrix}.
\]
The off-diagonal entries are positive and both row sums are one. The two diagonal inequalities are together equivalent to
\[
 r_x(z)\ge -\frac{m}{1-m}. \tag{1}
\]
This reduction is specific to two states; the scalar sign condition \(r_x(z)\ge0\) is a different, stronger requirement.

**3. Complete random-draw classification.** At the two ends of the uniform tableau interval,
\[
 r_{1/2}(z)=\frac{2-z}{2+z},\qquad
 r_1(z)=\frac{1+z-z^2/2}{(1+z)^2}.
\]
The first reaches the level in (1) exactly at \(z=z_0(m)\) for \(m<1/2\). By monotonicity in \(x\), all draws work up to that step. The second satisfies (1) exactly when
\[
 1+(1+m)z+\frac{3m-1}{2}z^2\ge0. \tag{2}
\]
When \(m<1/3\), this concave quadratic has precisely one positive zero, \(z_1(m)\), and no draws work beyond it. When \(m\ge1/3\), it stays positive at every finite \(z\), so some draws always work.

For an intermediate step, equality in (1) becomes a quadratic equation in \(x\):
\[
 z^2x^2+[2z-2(1-m)z^2]x
 +1-(1-m)z+\frac{1-m}{2}z^2=0.
\]
Its discriminant is \(2(1-m)z^3((1-2m)z-2)\). The larger root is
\[
 x_*(z,m)=1-m-\frac1z
 +\sqrt{\frac{(1-m)((1-2m)z-2)}{2z}}.
\]
At \(z=z_0(m)\), it equals \(1/2\). In the open intermediate regime it lies in \((1/2,1)\), while the other root lies below \(1/2\). Monotonicity shows that exactly the draws \(X\ge x_*\) pass (1). Since \(X\) is uniform on an interval of length \(1/2\),
\[
 P_m(z)=2(1-x_*(z,m)),
\]
which yields the stated formula including both endpoint branches.

**4. Sharp critical limits.** Let \(\epsilon=z-z_0(m)>0\). In the formula for \(P_m\), the square-root term is
\[
 \sqrt{\frac{2(1-m)(1-2m)\epsilon}{z_0(m)+\epsilon}}
 =(1-2m)\sqrt{1-m}\,\sqrt\epsilon+O(\epsilon^{3/2}),
\]
whereas \(2m+2/(z_0+\epsilon)=1+O(\epsilon)\). This proves the square-root onset. Taking \(z\to\infty\) in the intermediate expression gives \(2m-\sqrt{2(1-m)(1-2m)}\). It is positive exactly when \(3m>1\), since squaring the two positive sides of the defining inequality cancels the quadratic terms. For \(m<1/3\), the zero-success branch instead applies for large \(z\). The balanced case is already unconditional by (1) and \(r_x(z)>-1\).

**5. Repeated independent steps and cumulative recovery.** For a fixed \(z>z_0(m)\) with \(m<1/2\), the failure probability \(1-P_m(z)\) is strictly positive. Fresh independent draws make the first failed one-step matrix geometric and imply infinitely many failed one-step matrices almost surely. On the other hand, the accumulated \(n\)-step map is exactly
\[
 M_{X_1}(z)\cdots M_{X_n}(z)
 =\Pi+\left(\prod_{j=1}^n r_{X_j}(z)\right)(I-\Pi).
\]
Set \(q(z)=\max\{|r_{1/2}(z)|,|r_1(z)|\}<1\). Monotonicity of \(r_x\) shows \(|r_x(z)|\le q(z)\). For every integer \(n\) satisfying
\[
 q(z)^n<\frac{m}{1-m},
\]
the product multiplier lies strictly between \(-m/(1-m)\) and \(m/(1-m)\), so all four entries of the accumulated matrix are strictly positive. This bound holds for *every* draw sequence, even if some individual steps are nonstochastic.

## Verification
Run `python verify.py` with Python 3 and the standard library. The checker forms the stages directly for rational two-state generators and rational tableau choices, compares them exactly with the projector expression, verifies row sums and the precise nonnegativity criterion, checks rational critical endpoints, and compares the analytical probability against deterministic uniform midpoint counts over a range of positive rates and time steps. One successful replay performed 4,703 supplementary checks. The exact statements over continuous parameter ranges, unbounded time steps, and infinitely many draws follow from the proofs above, not from the finite checker.

## Relationship to prior work
Eisenmann, Jans, Kruse and Podhaisky (2026, arXiv:2607.18928, Sections 3 and 5) introduce this randomized SDIRK family, establish algebraic/A-stability, and give its general scalar stability function. Those facts are prior work and are used here. Their numerical experiments and appendix concern convergence and integration error rather than matrix stochasticity for two-state generators.

The fixed-parameter scalar sign-reversal law and its binomial/Poisson consequences for this same tableau have also been studied separately. Such scalar sign probabilities test \(r_x(z)<0\), whereas stochasticity of an irreducible two-state update has the different balance-dependent threshold (1). That earlier scalar law does not state the \(m=1/3\) stiff success frontier, the exact positive-stochastic probability for arbitrary rate imbalance, or the recurrent-one-step/eventually-positive-product dichotomy.

Previously published analyses of Crank--Nicolson on Markov generators include a return-resolvent criterion and the fact that balanced two-state chains are its only nontrivial unconditionally positive irreducible examples. Those results apply to the \(x=1/2\) endpoint here, not to the full randomized family. The two-midpoint-step SSP-SDIRK2(2) method has a distinct rational stability function and unconditional two-state endpoint positivity; that does not imply this theorem either.

Horváth (1998, 2005) develops general Runge--Kutta positivity radii and invariant-cone theory. Bochacik, Przybyłowicz and collaborators (2024/2025) analyze probabilistic stability of different randomized implicit methods. The present claim is a fixed-generator, parameter-averaged exact law rather than a uniform positivity-radius theorem. Broader older literature could contain an implicit equivalent; the historical-priority comparison is not exhaustive.

## Limitations
The conclusion classifies the exact two-state linear Markov endpoint matrices only. It neither asserts stage positivity nor extends the probability law to three or more states, nonlinear systems, time-varying generators, or numerical roundoff. Individual nonstochastic steps can still map some particular probability vectors to nonnegative vectors. The cumulative recovery is specific to fixed finite \(z>0\) and positive rates; it does not supply a uniform recovery time as \(z\to\infty\), nor imply that every intermediate numerical probability is physical. General positivity and absolute-monotonicity theory is a continuing historical originality risk.

## References
1. M. Eisenmann, M. Jans, R. Kruse, H. Podhaisky, *Error Bound and Stability Analysis for a Randomized Singly Diagonally Implicit Runge--Kutta Method*, arXiv:2607.18928v1, first public July 21, 2026. https://arxiv.org/abs/2607.18928
2. T. Bochacik, P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge--Kutta schemes*, arXiv:2404.19059, 2024; BIT Numerical Mathematics 65 (2025). https://arxiv.org/abs/2404.19059
3. Z. Horváth, *Positivity of Runge--Kutta and diagonally split Runge--Kutta methods*, Applied Numerical Mathematics 28 (1998), 309--326. https://doi.org/10.1016/S0168-9274(98)00050-6
4. Z. Horváth, *On the positivity step size threshold of Runge--Kutta methods*, Applied Numerical Mathematics 53 (2005), 341--356. https://doi.org/10.1016/j.apnum.2004.08.026
