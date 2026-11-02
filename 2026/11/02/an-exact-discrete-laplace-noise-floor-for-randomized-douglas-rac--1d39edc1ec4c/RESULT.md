# An exact discrete-Laplace noise floor for randomized Douglas–Rachford on inconsistent rows

## Finding

For every \(0<q<1\) and \(d>0\), let \(c=\sqrt{2q/(1-q)}\), and apply the two-reflection, row-norm-sampled randomized Douglas–Rachford method with relaxation \(1/2\) to
\[
A=\begin{pmatrix}1&0\\1&0\\0&c\end{pmatrix},\qquad b=\begin{pmatrix}0\\d\\0\end{pmatrix}.
\]
The matrix has full column rank two, the equations are inconsistent, and their unique ordinary least-squares minimizer is \(z_\star=(d/2,0)^{\mathsf T}\). Two ordered rows are sampled **independently with replacement** at every step, with probabilities \(((1-q)/2,(1-q)/2,q)\), matching the squared row norms. Let \(Z_n=(X_n,Y_n)\) be the iterate from any deterministic \(Z_0\in\mathbb R^2\).

Define \(\theta=2q(1-q)\) and
\[
\rho_q=\frac{\sqrt{1+q}-\sqrt{2q}}{\sqrt{1+q}+\sqrt{2q}}\in(0,1).
\]
There is a unique invariant probability \(\pi_q\) on \(\mathbb R^2\). Its full law is the shifted symmetric two-sided geometric law
\[
\pi_q\bigl(\{((k+1)d,0)\}\bigr)
=\pi_q\bigl(\{(-kd,0)\}\bigr)
=\frac{1-\rho_q}{2}\rho_q^k,
\qquad k=0,1,2,\ldots.
\]
In particular, \(\mathbb E_{\pi_q}Z=z_\star\), and \(\operatorname{Var}_{\pi_q}(X)=d^2/(4q)\). For all \(n\geq0\),
\[
\begin{aligned}
\mathbb E(X_n-d/2)&=(1-\theta)^n(X_0-d/2),\\
\mathbb E\|Z_n-z_\star\|_2^2&=(1-\theta)^n\|Z_0-z_\star\|_2^2
+\frac{d^2}{4q}\bigl(1-(1-\theta)^n\bigr),\\
\|\mathcal L(Z_n)-\pi_q\|_{\rm TV}&\leq(1-\theta)^n.
\end{aligned}
\]
The stationary first-coordinate characteristic function, centered at the least-squares solution, is exactly
\[
\mathbb E_{\pi_q}\exp\bigl(it(X/d-1/2)\bigr)
=\frac{2q\cos(t/2)}{2q+(1-q)\sin^2(t/2)},\qquad t\in\mathbb R.
\]
The weak singular-sampling limit is a continuous Laplace law:
\[
\frac{\sqrt q}{d}(X-d/2)\;\xRightarrow[q\downarrow0]{\pi_q}\;
{\rm Laplace}\bigl(0,1/(2\sqrt2)\bigr).
\]
For comparison, the original method's one-reflection specialization, the randomized Kaczmarz method sampled by the **same row-norm weights**, has limiting Euclidean least-squares error \(d^2/4\); the two-reflection method has limiting error \(d^2/(4q)\). Thus the precise stationary mean-square error inflation is \(1/q\), arbitrarily large while \(A\) remains full column rank for each \(q>0\).

## Assumptions and scope

Work in exact arithmetic. The rows are \(a_0=(1,0)\), \(a_1=(1,0)\), \(a_2=(0,c)\), with targets \((0,d,0)\). Since \(\|A\|_F^2=2+c^2=2/(1-q)\), squared-row-norm probabilities are \(p_0=p_1=(1-q)/2\) and \(p_2=q\). Write \(P_j\) for orthogonal projection onto \(H_j=\{z:a_j^{\mathsf T}z=b_j\}\) and \(R_j=2P_j-I\) for its affine reflection. Given independent row indexes \(I_n,J_n\), also independent across steps, define
\[
Z_{n+1}=\tfrac12\bigl(Z_n+R_{J_n}R_{I_n}Z_n\bigr).
\]
This is precisely the \(r=2\), \(\alpha=1/2\) no-momentum specialization of the cited source's algorithm. Total variation means \(\sup_B|\mu(B)-\nu(B)|\). All moments and probabilities are over the row draws, with deterministic initial state. The Laplace distribution above has density \(\exp(-|s|/b)/(2b)\) with \(b=1/(2\sqrt2)\).

## Proof

**1. Complete pair classification.** The three reflections are
\[
R_0(x,y)=(-x,y),\quad R_1(x,y)=(2d-x,y),\quad R_2(x,y)=(x,-y).
\]
There are three exhaustive types of ordered index pairs: with probability \((1-q)^2\), both rows have horizontal normal, and the step is \((x+dS,y)\), where \(\Pr(S=-1)=\Pr(S=1)=1/4\) and \(\Pr(S=0)=1/2\); with probability \(\theta=2q(1-q)\), exactly one is row 2, giving \((0,0)\) or \((d,0)\) with equal conditional probability; with probability \(q^2\), both are row 2 and the step is the identity. These identities follow by direct composition of the displayed affine reflections. In particular, a mixed-type pair coalesces all starting states and subsequent steps preserve the lattice \(d\mathbb Z\times\{0\}\).

**2. Geometric coupling and invariant law.** Independently sample one stationary candidate and one arbitrary starting state, then use the same ordered row pairs. At the first mixed-type pair they become identical, regardless of earlier positions, and remain identical. The probability of no such pair in \(n\) steps is \((1-\theta)^n\). To construct the invariant candidate explicitly, let \(\rho\in(0,1)\) solve
\[
\frac{(1-\rho)^2}{\rho}=\frac{8q}{1-q}.
\]
This quadratic has the displayed unique positive solution \(\rho_q\). The off-center lattice balance equation for the proposed mass \(\pi(k)\), \(k\in\mathbb Z\), is
\[
0=\frac{(1-q)^2}{4}\bigl(\pi(k-1)-2\pi(k)+\pi(k+1)\bigr)
-\theta\pi(k),\qquad k\notin\{0,1\}.
\]
The ratio condition verifies it for both geometric tails. At the two central sites, the extra reset inflow is \(\theta/2\) per site; direct substitution of \(\pi(0)=\pi(1)=(1-\rho_q)/2\) verifies the balance there as well. The geometric series normalizes total probability to one. Therefore the displayed \(\pi_q\) is invariant, and the preceding coupling proves uniqueness and the total-variation estimate.

**3. Mean and mean-square identities.** Put \(U_n=X_n-d/2\). Conditioning on the three pair types yields exactly
\[
\begin{aligned}
\mathbb E(U_{n+1}\mid Z_n)&=(1-\theta)U_n,\\
\mathbb E(U_{n+1}^2\mid Z_n)&=(1-\theta)U_n^2+\frac{d^2(1-q)}{2},\\
\mathbb E(Y_{n+1}^2\mid Z_n)&=(1-\theta)Y_n^2.
\end{aligned}
\]
Indeed, horizontal/horizontal pairs add variance \(d^2(1-q)^2/2\), and mixed pairs add \(d^2\theta/4\), totaling \(d^2(1-q)/2\). Solving the affine second-moment recurrence and adding the second-coordinate term gives the displayed finite-time formula, with fixed point \(d^2(1-q)/(2\theta)=d^2/(4q)\). The same recursion at stationarity proves the stated variance and mean.

**4. Exact distribution and singular limit.** Summation of the geometric law gives
\[
\begin{aligned}
\varphi_q(t)
&=(1-\rho_q)\operatorname{Re}\frac{e^{it/2}}{1-\rho_q e^{it}}
=\frac{(1-\rho_q)^2\cos(t/2)}{1-2\rho_q\cos t+\rho_q^2}\\
&=\frac{2q\cos(t/2)}{2q+(1-q)\sin^2(t/2)}.
\end{aligned}
\]
For every fixed real \(t\), replacing \(t\) by \(t\sqrt q\) and taking \(q\downarrow0\) yields \((1+t^2/8)^{-1}\). This is the characteristic function of the centered Laplace distribution of scale \(1/(2\sqrt2)\); the continuity theorem proves weak convergence. The stationary variance \(d^2/(4q)\) is consistent with this limit after scaling.

**5. The matched Kaczmarz comparison.** For \(r=1\) and \(\alpha=1/2\), the step is the projection \(P_{I_n}\). With probability \(1-q\), this resets \(X\) to \(0\) or \(d\) equally, and with probability \(q\), it leaves \(X\) unchanged (but resets \(Y\) to zero). Consequently
\[
\mathbb E[(X_{n+1}-d/2)^2\mid X_n]
=q(X_n-d/2)^2+(1-q)d^2/4.
\]
Its stationary first-coordinate law is the symmetric two-point mixture at \(0,d\) and its stationary full squared error is \(d^2/4\). Dividing the two stationary errors gives the exact factor \(1/q\). Each \(q\in(0,1)\) retains full column rank and has a strictly positive mixed-pair coalescence probability, so this is a genuine conditioning/sampling phenomenon, not rank loss at any fixed parameter.

## Verification

The included standard-library `verification/verify.py` reconstructs the nine ordered reflection pairs from the three original affine reflections. It uses exact rational arithmetic on four rational sampling profiles and checks conditional first and second moments as well as 12 exact finite-time distribution updates per profile. It separately checks the closed-form characteristic function against the two-sided geometric series, stationary second moments, and the Laplace rescaling limit numerically. Running `python verification/verify.py` prints `VERIFY_OK` with counts. The finite checks support the stage classification; the all-parameter identities and weak limit are proved above, not inferred from finite tests.

## Relationship to prior work

Han, Su and Xie [1] introduced the sampled two-reflection method for consistent linear systems. The sampling and algorithm specialization are theirs, and their results for consistent systems are not claimed anew. Their concluding discussion explicitly identifies inconsistent linear systems as an extension to explore. Luke [2] studies general Markov/invariant-measure theory for randomized **blockwise** Douglas–Rachford and notes that stochastic maps may have no common fixed point; thus invariant-distribution analysis for randomized splitting is prior work. Its algorithm updates separable coordinate blocks, whereas [1]'s method composes two independently chosen hyperplane reflections, and [2] does not provide this three-row geometric law or sharp comparison with one-reflection randomized Kaczmarz. Bauschke and Moursi [3] study general **deterministic** Douglas–Rachford for inconsistent optimization problems, which is distinct from row-resampling noise; the existence of a general inconsistent-DR theory is not claimed anew. Guo and colleagues [4] study enhanced row sampling for randomized DR in the consistent linear-system regime. The ordinary geometric renewal/resolvent identity and Laplace limit theorem used in the proof are classical probabilistic tools; the method-specific exact transition law, the mean-square inflation factor, and their singular-sampling implication are the assessed contribution.

## Limitations

The theorem is specific to three affine constraints in two variables, row-norm sampling **with replacement**, two reflections per step, relaxation \(1/2\), and exact arithmetic. It does not assert a universal instability result for all inconsistent systems or alternative sampling/correction schemes. The almost-sure iterates continue fluctuating at fixed \(q>0\); only their laws and specified moments converge. As \(q\downarrow0\), the third row tends to zero and uniform conditioning is lost, though each fixed \(q>0\) system remains full column rank. The result is a best-knowledge method-specific contribution, not an assertion that geometric-reset random-walk theory or general invariant-measure theory is new. Independent external priority verification has not been performed.

## References

1. D. Han, Y. Su and J. Xie, *Randomized Douglas-Rachford methods for linear systems: Improved accuracy and efficiency*, arXiv:2207.04291 (first public 9 July 2022), https://arxiv.org/abs/2207.04291.
2. D. R. Luke, *Convergence in Distribution of Randomized Algorithms: The Case of Partially Separable Optimization*, arXiv:2310.20397 (first public 31 October 2023), https://arxiv.org/abs/2310.20397.
3. H. H. Bauschke and W. M. Moursi, *On the Douglas–Rachford Algorithm for Solving Possibly Inconsistent Optimization Problems*, Math. Oper. Res. 49 (2024), 58–77; published online March 2023, https://doi.org/10.1287/moor.2022.1347.
4. Y. Guo et al., *Enhanced randomized Douglas-Rachford method: Improved probabilities and adaptive momentum*, arXiv:2506.10261 (2025), https://arxiv.org/abs/2506.10261.
