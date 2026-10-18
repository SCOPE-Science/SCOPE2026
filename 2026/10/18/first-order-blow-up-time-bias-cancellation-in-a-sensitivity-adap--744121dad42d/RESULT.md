# First-order blow-up-time bias cancellation in a sensitivity-adaptive Euler scheme

## Finding
For a sensitivity-adaptive forward Euler estimator of finite-time blow-up, the signed time error on the scalar quadratic growth model has a computable leading constant. If \(\varepsilon\downarrow0\) while the initial value \(x_0>0\) and algorithm parameter \(k>1\) remain fixed, then
\[
\bar\tau-\tau=\varepsilon\left(\sqrt{\frac{2}{kx_0}}-1\right)+O_{x_0,k}(\varepsilon^{3/2}),
\qquad \tau=\frac1{x_0}.
\]
At the same time, the number of forward Euler steps satisfies
\[
N=\frac{2\sqrt{2k/x_0}}{\varepsilon}+O_{x_0,k}(\varepsilon^{-1/2}).
\]
Consequently, for each \(0<x_0<2\) the unique fixed admissible choice \(k_*=2/x_0>1\) cancels the \(\varepsilon\)-order bias and gives \(\lvert\bar\tau-\tau\rvert=O_{x_0}(\varepsilon^{3/2})\) at the same first-order work scaling. If \(x_0\ge2\), no fixed \(k>1\) cancels this coefficient.

## Assumptions and scope
Consider the one-dimensional autonomous ODE and blow-up time
\[
x'(t)=x(t)^2,\quad x(0)=x_0>0,\qquad \tau=1/x_0.
\]
Given \(\varepsilon>0\), set the stopping threshold \(r=1/\varepsilon\), and choose a fixed \(k>1\). Starting at \(x_0\), repeat exactly
\[
h_j=\frac{\varepsilon}{\sqrt{2\min\{kx_j,r\}}},\qquad
x_{j+1}=x_j+h_jx_j^2,\qquad t_{j+1}=t_j+h_j,
\]
until the first index \(N\) with \(x_N\ge r\). Set \(\bar\tau=t_N\). Assume \(\varepsilon\) sufficiently small that \(x_0<r/k\). The method is exactly Algorithm 1 of Hoel and Meo (2026) in its quadratic specialization with \(F(b(x))=1/x\). The claims are asymptotic statements for fixed \(x_0,k\), not uniform claims when parameters vary with \(\varepsilon\).

## Proof
**Step 1: reciprocal telescoping identity.** Since the update is \(x_{j+1}=x_j(1+h_jx_j)\), exact arithmetic gives
\[
h_j-\left(\frac1{x_j}-\frac1{x_{j+1}}\right)=\frac{h_j^2x_j}{1+h_jx_j}.
\]
Summing, and writing \(D_j=h_j^2x_j/(1+h_jx_j)\), yields
\[
\bar\tau-\tau=-\frac1{x_N}+\sum_{j=0}^{N-1}D_j.
\tag{1}
\]
Every \(D_j\) is nonnegative. The final reciprocal represents the tail of the exact blow-up integral.

**Step 2: uncapped steps.** Let \(J\) be the first index with \(x_J\ge r/k\), so \(j<J\) has \(kx_j<r\). Put \(a=\varepsilon/\sqrt{2k}\) and \(y_j=x_j^{-1/2}\). Then
\[
x_{j+1}=x_j(1+a\sqrt{x_j}),\qquad y_{j+1}=y_j(1+a/y_j)^{-1/2}.
\]
For \(j<J\), the uniform bound \(0<a/y_j\le\sqrt{\varepsilon/2}\) holds. Taylor's formula with a uniform remainder therefore yields
\[
y_j-y_{j+1}=\frac a2\bigl(1+O(\sqrt\varepsilon)\bigr).
\tag{2}
\]
The relative overshoot of the crossing step is \(1+O(\sqrt\varepsilon)\), so \(y_J=O(\sqrt\varepsilon)\). Summing (2), first using its positive lower bound to obtain \(J=O(\varepsilon^{-1})\), and then substituting this bound into the remainder, gives
\[
J=\frac{2\sqrt{2k/x_0}}{\varepsilon}+O_{x_0,k}(\varepsilon^{-1/2}).
\tag{3}
\]
For each uncapped step, the exact numerator is \(h_j^2x_j=\varepsilon^2/(2k)\), while the denominator is \(1+O(\sqrt\varepsilon)\). Thus
\[
\sum_{j<J}D_j=\frac{\varepsilon^2}{2k}J+O(\varepsilon^{3/2})
=\varepsilon\sqrt{\frac{2}{kx_0}}+O_{x_0,k}(\varepsilon^{3/2}).
\tag{4}
\]

**Step 3: capped steps and terminal overshoot.** Since \(k>1\) is fixed and the crossing overshoot in Step 2 is only relative \(O(\sqrt\varepsilon)\), the crossing state satisfies \(x_J<r\) once \(\varepsilon\) is sufficiently small. For \(J\le j<N\), the cap is active: \(h_j=\varepsilon^{3/2}/\sqrt2\). As \(r/k\le x_j<r\), we have \(0<h_jx_j\le\sqrt{\varepsilon/2}\). The reciprocal drop in each such step is
\[
\frac1{x_j}-\frac1{x_{j+1}}=\frac{h_j}{1+h_jx_j}\ge\frac{\varepsilon^{3/2}}{2\sqrt2}
\]
for sufficiently small \(\varepsilon\). The reciprocal distance between \(x_J\) and the threshold is no more than \(k\varepsilon\); hence \(N-J=O_k(\varepsilon^{-1/2})\). Because \(0\le D_j\le(\varepsilon^3/2)r=\varepsilon^2/2\),
\[
\sum_{J\le j<N}D_j=O_k(\varepsilon^{3/2}).
\tag{5}
\]
The last Euler update begins below \(r\) and can overshoot it by at most the factor \(1+h_{N-1}r\le1+\sqrt{\varepsilon/2}\), so \(r\le x_N\le r(1+\sqrt{\varepsilon/2})\). Consequently
\[
x_N^{-1}=\varepsilon+O(\varepsilon^{3/2}).
\tag{6}
\]
Combining (1), (4), (5), and (6) proves the signed bias expansion; combining (3) and the capped-step count proves the cost expansion.

**Step 4: the unique cancellation.** The leading bias coefficient is strictly decreasing in \(k>1\) and vanishes precisely when \(k=2/x_0\). This lies in the permitted range exactly for \(x_0<2\). For fixed parameters away from cancellation the coefficient is nonzero, so the error has exact first-order asymptotics. At cancellation only the displayed upper bound \(O(\varepsilon^{3/2})\) is established, not a nonzero limit of the rescaled error. \(\square\)

## Verification
The accompanying standalone `verify.py` uses Python's standard library. It tests the exact reciprocal one-step identity with rational arithmetic and compares direct evaluations of the specified stopping algorithm at decreasing tolerances for several initial values and parameter choices, including the cancelling choices. Run it with `python verify.py`. These finite computations check implementation and examples; the universal statements follow from the proof above.

## Relationship to prior work
Hoel and Meo (2026), Algorithm 1 and Theorem 1, establish a general sensitivity-based adaptive blow-up estimator with an \(O(\varepsilon)\) time-error bound and \(O(\varepsilon^{-1})\) cost. Their Section 4.2 experiments use this quadratic model at \(x_0=1/2\) and \(k=1.1\). The present specialization retains precisely their stopping rule and step formula but obtains the signed leading error coefficient and identifies an admissible parameter giving faster error decay at no change in the leading cost order. Classical numerical blow-up-time analyses using time transformations, fixed steps, or rescaling do not by themselves state this particular coefficient for the sensitivity-adaptive rule. The new result does not assert that the underlying method, standard reciprocal substitutions, or classical Euler error expansions are new.

## Limitations
The order improvement is proved only on the positive scalar quadratic ODE, for known fixed initial state and the exact terminal threshold. It is not uniform in \(x_0\) or in \(k\) and does not claim improved rates for general nonlinear vector fields, noisy evaluations, finite-precision implementations, or an exact nonzero \(\varepsilon^{3/2}\) coefficient. The tuned parameter may be large when \(x_0\) is small.

## References
1. H. Hoel and J. V. Meo, *A priori adaptive numerical methods for estimating blow-up times of autonomous ODEs*, arXiv:2603.12957v1 (2026), https://arxiv.org/html/2603.12957v1, especially Algorithm 1, Theorem 1, and Section 4.2.
2. A. M. Stuart and M. S. Floater, *On the computation of blow-up*, IMA Journal of Numerical Analysis **10** (1990), 169–193; a time-transformation method discussed in reference 1.
3. C.-H. Cho and J.-S. Wu, *On the convergence of the numerical blow-up time for a rescaling algorithm*, Numerical Algorithms (2024); a rescaling approach discussed in reference 1.
