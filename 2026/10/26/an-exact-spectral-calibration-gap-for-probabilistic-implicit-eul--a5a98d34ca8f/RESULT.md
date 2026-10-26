# An exact spectral calibration gap for probabilistic implicit Euler under a linear constraint

## Finding

A single scalar variance scale cannot in general calibrate both independent dynamic modes of a constrained probabilistic implicit-Euler solver, even in the zero-mesh limit. The discrepancy has an exact closed form, and there is a nontrivial resonance at which two unequal decay rates *can* share the same leading calibration scale.

Fix \(T>0\), \(N\in\mathbb{N}\) with \(N\ge1\), \(h=T/N\), and \(\lambda_1,\lambda_2>0\). For each mode define
\[
q_j=(1+\lambda_jh)^{-1},\quad
E_j=q_j^N-(1+\lambda_jh/2)^{-2N},\quad
a_j=h^3q_j^2\frac{1-q_j^{2N}}{1-q_j^2},\quad r_j=\frac{E_j^2}{a_j}.
\]
The two terminal scalar Gaussian Bhattacharyya distances, summed over the dynamic coordinates, have the *unique* best common squared noise scale
\[
\boxed{\sigma_*^2=\sqrt{r_1r_2}}
\]
and the exact best attainable sum
\[
\boxed{D_{\min}(h)=\log\cosh\left(\tfrac14\log\frac{r_1}{r_2}\right)}.
\]
In particular, this quantity is strictly positive precisely when \(r_1\ne r_2\).

As \(h\downarrow0\) with \(Nh=T\),
\[
\boxed{r_j\longrightarrow R_T(\lambda_j):=\frac{\lambda_j^5T^2}{8(e^{2\lambda_jT}-1)}}.
\]
The function \(R_T(\lambda)\) has exactly one positive maximizer at \(\lambda=x_*/T\), where \(x_*\) is the unique positive root of
\[
5(1-e^{-2x})=2x,\qquad x_*=2.4825571158721381518\ldots.
\]
Thus, in the fine-mesh limit, a lower-rate mode below \(x_*/T\) has exactly one *different* higher-rate partner above \(x_*/T\) with zero mismatch; otherwise, equality of the two limiting calibration ratios is not automatic. In the concrete three-state system with \(T=1\), \(\lambda_1=1\) and \(\lambda_2=10\),
\[
\lim_{h\downarrow0}D_{\min}(h)=1.0006207612009762861\ldots>0.
\]
The positive lower bound applies also to any additive nonnegative calibration objective that includes these two terminal marginal distances.

## Assumptions and scope

Consider the real, linear, index-two semi-explicit differential-algebraic system
\[
\dot u(t)+Au(t)+B^{\mathsf T}\ell(t)=0,\qquad Bu(t)=0,
\]
with \(A=\operatorname{diag}(\lambda_1,\lambda_2,1)\), \(B=(0,0,1)\), and consistent initial value \(u(0)=(1,1,0)^{\mathsf T}\). The multiplier \(\ell\) enforces the constraint. Its dynamic kernel \(\ker B\) has exactly two coordinates.

At each step introduce independent standard normal random variables \(Z_{n,j}\), and use the *right-hand-side-forced*, structure-preserving probabilistic implicit Euler step
\[
\begin{pmatrix}I+hA&hB^{\mathsf T}\\B&0\end{pmatrix}
\begin{pmatrix}U_{n+1}\\\ell_{n+1}\end{pmatrix}
=
\begin{pmatrix}U_n+\sigma h^{3/2}(Z_{n,1},Z_{n,2},0)^{\mathsf T}\\0\end{pmatrix},
\quad\sigma>0.
\]
This is precisely the location and order of the dynamic forcing in the probabilistic implicit-Euler family described in the cited work. The result addresses exact arithmetic, fixed final time, common scalar \(\sigma\), independent Gaussian forcing in the *two* dynamic coordinates, and step-doubling indicators at the final time; it does not claim to optimize a whole-trajectory likelihood.

For each coordinate \(j\in\{1,2\}\), the target Gaussian is \(\mathcal N(q_j^N,E_j^2)\), and the numerical marginal is \(\mathcal N(q_j^N,\sigma^2a_j)\). Their distance is the standard Bhattacharyya distance, measured in natural logarithm units.

## Proof

**1. Dynamic recursion and nondegenerate indicator.** The algebraic equation fixes \(U_{n,3}=0\). In the other two coordinates the saddle-point step becomes
\[
U_{n+1,j}=q_jU_{n,j}+q_j\sigma h^{3/2}Z_{n,j}.
\]
Its mean at the last node is \(q_j^N\). Its variance is a geometric sum,
\[
\operatorname{Var}(U_{N,j})=\sigma^2h^3q_j^2\sum_{k=0}^{N-1}q_j^{2k}
=\sigma^2a_j.
\]
The half-step deterministic propagation gives \((1+\lambda_jh/2)^{-2N}\). Since \((1+x/2)^2>1+x\) for \(x>0\), we have \(E_j>0\), whence \(a_j,r_j>0\).

**2. Exact global minimization.** The Bhattacharyya distance of two one-dimensional Gaussians with the same mean and strictly positive variances \(v,w\) is
\[
D_B(v,w)=\frac12\log\frac{v+w}{2\sqrt{vw}}
=\frac12\log\cosh\left(\frac12\log\frac{v}{w}\right).
\]
Writing \(s=\sigma^2>0\) and \(v=\log s\), the sum of both distances is
\[
F(v)=\frac12\sum_{j=1}^2\log\cosh\left(\frac{v-\log r_j}{2}\right).
\]
Direct differentiation gives
\[
F'(v)=\frac14\sum_{j=1}^2\tanh\left(\frac{v-\log r_j}{2}\right),\qquad
F''(v)=\frac18\sum_{j=1}^2\operatorname{sech}^2\left(\frac{v-\log r_j}{2}\right)>0.
\]
The unique stationary point, and hence the unique global minimizer, is \(v=(\log r_1+\log r_2)/2\); substitution proves both boxed formulas. If a larger calibration objective adds nonnegative distances at other times, its infimum is at least this terminal lower bound.

**3. Fine-mesh limit.** Taylor expansion of the elementary logarithm gives, with \(h=T/N\),
\[
q_j^N=e^{-\lambda_jT}\left(1+\frac12\lambda_j^2Th+O(h^2)\right),\qquad
(1+\lambda_jh/2)^{-2N}=e^{-\lambda_jT}\left(1+\frac14\lambda_j^2Th+O(h^2)\right).
\]
Therefore \(E_j=e^{-\lambda_jT}\lambda_j^2Th/4+O(h^2)\). Using the exact simplification
\[
a_j=h^2\frac{1-q_j^{2N}}{2\lambda_j+\lambda_j^2h},
\]
we obtain \(a_j=h^2(1-e^{-2\lambda_jT})/(2\lambda_j)+O(h^3)\), and division yields \(r_j\to R_T(\lambda_j)\). Continuity of \(\log\cosh\) proves the limiting mismatch formula even when the optimal scale depends on \(h\).

**4. Exact spectral resonance.** Set \(x=\lambda T\), so \(R_T(\lambda)=x^5/[8T^3(e^{2x}-1)]\). Its logarithmic derivative has the sign of \(g(x)=5(1-e^{-2x})-2x\). For \(x>0\), \(g'(x)=10e^{-2x}-2\) strictly decreases from \(8\) to \(-2\), while \(g(0)=0\) and \(g(x)\to-\infty\). Hence exactly one positive zero \(x_*\) exists; \(R_T\) is strictly increasing before it and strictly decreasing afterward, with limits zero at both ends. For each value strictly between zero and the maximum there are exactly two distinct rates giving that value, one on either side of \(x_*/T\). These, and only these unequal-rate pairs, have zero *limiting* mismatch.

**5. Concrete obstruction.** At \(T=1\), \(\lambda_1=1\), \(\lambda_2=10\), the exact ratio formula gives
\[
R_1(1)=\frac1{8(e^2-1)},\quad R_1(10)=\frac{10^5}{8(e^{20}-1)}.
\]
These values are unequal and yield \(\log\cosh(\tfrac14\log[R_1(1)/R_1(10)])=1.000620761200976\ldots\). This establishes a strictly positive fine-grid mismatch despite both the probabilistic and deterministic errors converging to zero.

## Verification

Run the accompanying standalone Python 3 script with `python verify_calibration.py`. It checks the finite-step variance recursion against the closed formula using *exact fractions*, tests the optimizer identity and perturbations, and checks high-precision limits and the critical spectral root. The recorded run reports `VERIFY_OK 894`. These finite checks support the derivation; strict convexity, infinite-mesh convergence, and the unique critical root are proved above and are not inferred from sampling.

## Relationship to prior work

Altmann and Moradi introduced the constrained probabilistic implicit Euler update and a global scalar noise-scale calibration based on componentwise Gaussian Bhattacharyya distances (2024 arXiv first posting; published 2025). Conrad, Girolami, Särkkä, Stuart and Zygalakis introduced a general probabilistic numerical calibration with the same class of distance (2016 online publication). Both constructions and the general Gaussian distance identity are credited as prior art. Neither of the two inspected papers states the present exact two-mode terminal optimal scale, the positive mismatch persisting under temporal refinement, or the nonmonotone iso-calibration spectrum. The new result is a method-specific calculation and boundary of the *single shared scalar noise scale*, not a new probabilistic-integrator construction.

## Limitations

The theorem requires two independently forced eigenmodes, diagonal positive damping, fixed final time and start, a standard half-step deterministic indicator, and a single positive scalar scale. Anisotropic noise covariances (explicitly allowed as a broader possibility in earlier work) can match both marginal variances and therefore evade this scalar obstruction. The optimal \(\sigma\) for the two terminal coordinates is not generally optimal for the full time-series criterion. The quantified distance compares two *reference Gaussian marginals*, not the exact solution distribution. Numerical values and the verification script do not constitute independent validation. Generic results on Gaussian divergence minimization could be mathematically equivalent to the convex scalar step even when not stated in the numerical-analysis literature.

## References

1. R. Altmann and A. Moradi, *Probabilistic time integration for semi-explicit PDAEs*, arXiv:2406.07220 (first posted 2024-06-11); *Statistics and Computing* 35, Article 16 (2025), doi:10.1007/s11222-024-10543-0. Sections 4.1 and 5 supply the stochastic step and calibration objective.
2. P. R. Conrad, M. Girolami, S. Särkkä, A. M. Stuart and K. C. Zygalakis, *Statistical analysis of differential equations: introducing probability measures on numerical solutions*, online 2016, *Statistics and Computing* 27 (2017), 1065–1082, doi:10.1007/s11222-016-9671-0. Section 3.1 and note 6 discuss the shared calibration scale and the broader covariance option.
