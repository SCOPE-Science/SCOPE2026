# Sharp mean-square stability frontier for two-node stochastic heat splitting

## Finding
Consider the two-node heat operator and independent multiplicative Brownian noises defined below. A nonnegativity-preserving exponential noise-then-heat Lie–Trotter discretization has the exact mean-square one-step amplification factor
\[
\Lambda(h)=\frac{e^{-2ah}}{2}\Bigl[A(1+E)+\sqrt{A^2(E-1)^2+4EB^2}\Bigr],\qquad A=\frac{1+e^{-4bh}}2,\quad B=\frac{1-e^{-4bh}}2,\quad E=e^{\sigma^2h}.
\]
Its long-time mean-square stability condition is exactly \(\sigma^2<s_*(h)\), where
\[
s_*(h)=2a+\frac1h\log\frac{1-e^{-2ah}A}{A-e^{-2ah}e^{-4bh}}.
\]
In contrast, the corresponding continuous-time semidiscrete stochastic heat equation is exponentially mean-square stable exactly when
\[
\sigma^2<s_c=\frac{2a(a+2b)}{a+b}.
\]
For every \(a,b>0\), the numerical method is stable for *every* positive timestep exactly when \(\sigma^2\le 2a\), while the exact equation is stable for the strictly larger range \(\sigma^2<s_c\). In particular every variance \(2a<\sigma^2<s_c\) yields a continuously mean-square-stable problem for which the positive numerical method becomes mean-square unstable at sufficiently large steps.

## Assumptions and scope
Take \(a,b>0\), \(\sigma\ge0\), \(h>0\), and independent standard Brownian motions \(W_1,W_2\). For deterministic \(x_0\in\mathbb R^2\), define
\[
dX=LX\,dt+\sigma\operatorname{diag}(X_1,X_2)\,dW,\quad L=\begin{pmatrix}-(a+b)&b\\b&-(a+b)\end{pmatrix},\quad X(0)=x_0.
\]
Write \(t=e^{-2ah}\), \(q=e^{-2bh}\). The numerical method is
\[
Y_{n+1}=P_hD_nY_n,\quad P_h=e^{hL}=e^{-ah}\begin{pmatrix}(1+q)/2&(1-q)/2\\(1-q)/2&(1+q)/2\end{pmatrix},
\]
\[
D_n=\operatorname{diag}\bigl(e^{\sigma\Delta W_{1,n}-\sigma^2h/2},e^{\sigma\Delta W_{2,n}-\sigma^2h/2}\bigr),\quad \Delta W_{i,n}\sim N(0,h)\ \text{independently}.
\]
Here exponential mean-square stability means \(\mathbb E\|X(t)\|_2^2\to0\) exponentially, respectively \(\mathbb E\|Y_n\|_2^2\to0\) geometrically, for *all* deterministic initial vectors. Stability assertions at equality are excluded. The method preserves componentwise nonnegativity almost surely for all timesteps and all nonnegative data, independently of its mean-square stability.

## Proof
**Discrete second moments.** Because each noise multiplier has mean \(1\), second moment \(E=e^{\sigma^2 h}\), and independent cross moment \(1\), the noise step sends a covariance \(C\) to the matrix whose diagonal entries are multiplied by \(E\) and off-diagonal entries are unchanged. Let \(u=(\mathbb EY_1^2+\mathbb EY_2^2)/2\) and \(v=\mathbb EY_1Y_2\). A direct multiplication by \(P_h\) gives the *exact*, closed even-moment evolution
\[
\binom{u'}{v'}=t\begin{pmatrix}AE&B\\BE&A\end{pmatrix}\binom uv,
\quad A=\frac{1+q^2}2,\ B=\frac{1-q^2}2.
\]
The odd diagonal-moment difference \(\mathbb EY_1^2-\mathbb EY_2^2\) has multiplier \(tEq\). The even block has positive entries and positive eigenvalues (its determinant is \(t^2Eq^2\)); its Perron eigenvalue is \(\Lambda(h)\) as displayed. Since \(A\ge q\), the Perron eigenvalue is at least \(tEA\ge tEq\), so the spectral radius of the complete three-dimensional covariance map is exactly \(\Lambda(h)\). For \(\Lambda<1\), every covariance decays geometrically. For \(\Lambda\ge1\), choose \(Y_0=(1,1)\): its even moments \(u=v=1\) project nontrivially on the positive Perron eigenvector, so the expected squared norm does not decay. This proves the if-and-only-if condition for arbitrary deterministic initial data.

**Sharp variance cutoff.** The even block is nonnegative and its Perron eigenvalue increases strictly with \(E\) (for \(h>0\)); at \(E=1\), \(\Lambda=t<1\). The characteristic equation at eigenvalue one is
\[
0=\det\left(I-t\begin{pmatrix}AE&B\\BE&A\end{pmatrix}\right)=1-tA-tE(A-tq^2).
\]
The unique positive crossover is therefore
\[
E_*=\frac{1-tA}{t(A-tq^2)},\qquad s_*(h)=\frac{\log E_*}{h}=2a+\frac1h\log\frac{1-tA}{A-tq^2}.
\]
Both numerator and denominator are positive. Moreover \((1-tA)-(A-tq^2)=B(1-t)>0\), whence \(s_*(h)>2a\) for every finite \(h>0\). Taking \(h\to\infty\), \(t,q\to0\) gives \(s_*(h)=2a+(\log2)/h+o(h^{-1})\). Thus \(\sigma^2\le2a\) is necessary and sufficient for stability for *all* timesteps (the equality case is stable at each finite step because \(s_*(h)>2a\)). For \(\sigma^2>2a\), sufficiently large steps cross the cutoff.

**Continuous second moments.** Itô's formula gives the even-moment generator
\[
\frac{d}{dt}\binom uv=\begin{pmatrix}-2(a+b)+\sigma^2&2b\\2b&-2(a+b)\end{pmatrix}\binom uv.
\]
Its largest eigenvalue is \(\mu=-2(a+b)+\sigma^2/2+\sqrt{\sigma^4/4+4b^2}\). The odd diagonal-moment generator has eigenvalue \(-2(a+b)+\sigma^2\le\mu\). Therefore all moments decay exponentially if and only if \(\mu<0\), equivalent upon squaring the boundary equation to \(\sigma^2<2a(a+2b)/(a+b)\). The strict inequality \(s_c>2a\) follows from \(b>0\). The small-step covariance expansion also gives \(s_*(h)\to s_c\), as expected, but that consistency does not extend stability to arbitrary large steps.

**Explicit two-node finite-element witness.** On \([0,1]\) take piecewise-linear Dirichlet finite elements with uniform nodes \(0,1/3,2/3,1\). Lumped mass is \(I/3\), stiffness is \(\begin{psmallmatrix}6&-3\\-3&6\end{psmallmatrix}\), and hence the lumped heat generator is \(L=\begin{psmallmatrix}-18&9\\9&-18\end{psmallmatrix}\), namely \(a=b=9\). Two orthonormal, nonoverlapping continuous spatial noise shapes are \(e_i(x)=\sqrt{45/2}\max\{1-15|x-i/3|,0\}\) for \(i=1,2\): each has \(L^2\)-norm one, and their nodal values are diagonal of magnitude \(\sqrt{45/2}\). With multiplicative coefficient \(f(z)=z\), variance is \(\sigma^2=45/2=22.5\). Smooth nonnegative initial profile \(u_0(x)=(9/2)x(1-x)\) has nodal vector \((1,1)\). The continuous semidiscrete mean-square exponent is approximately \(-3.5235424529<0\), while the positive numerical method has \(\Lambda(1/9)\approx0.9038448037<1\) and \(\Lambda(2/9)\approx1.3687455446>1\). This supplies one fixed finite-element system and fixed Brownian forcing for which increasing the time step destroys exponential mean-square stability without ever destroying pathwise positivity.

## Verification
The standalone `verify.py` re-evaluates the moment map from explicit covariance basis matrices and compares its full numerical spectral radius with the closed Perron formula in 576 parameter combinations. It additionally checks the strict finite-step variance criterion, small- and large-step cutoff asymptotics, and the exact nodal finite-element example at two step sizes; its reproducible stdout is embedded as `check_output.txt`. These computations cross-check the algebra but do not replace the proof. Python dependencies: `numpy` and `mpmath`.

## Relationship to prior work
Hearder, Le Bris and Djurdjevac (2026) introduce and analyze the fully discrete nonnegativity-preserving mass-lumped FEM stochastic heat splitting motivating this two-node specialization; their moment bounds concern finite time intervals. Earlier nonnegative stochastic heat discretizations, including Bréhier, Cohen and Ulander (2024) and the 2025 precursor, also analyze positivity and moment behavior. The present contribution is specifically an *exact long-time mean-square stability frontier as a function of step size* for this natural finite-dimensional model and its sharp separation from finite-step positivity and continuous-time stability. This does not imply global long-time properties of arbitrary finite-element meshes or nonlinear stochastic heat equations.

## Limitations
The closed formula requires two symmetric interior nodes, Dirichlet heat dynamics, independent spatial Brownian modes, linear multiplicative coefficient, and the specified noise-then-heat ordering. It proves mean-square rather than almost-sure stability, and the unstable-step conclusion concerns asymptotic repetition rather than fixed-horizon convergence. The spatial noise witness uses compactly supported continuous functions and is an exact nodal semidiscretization; no claim is made for extra spatial regularity assumptions not specified here. Possible equivalent formulas in older general splitting/stability literature remain an originality risk; independent review is outstanding.

## References
- O. Hearder, C. Le Bris, A. Djurdjevac, *A Fully Discrete Nonnegativity-Preserving FEM for a Stochastic Heat Equation*, arXiv:2602.16508 (initially public 2026-02-18), especially numerical splitting and finite-horizon moment sections.
- Earlier stochastic-heat positivity-preserving discretization, arXiv:2502.16854 (2025), for related splitting and moment estimates.
- C.-E. Bréhier, D. Cohen, J. Ulander, positivity-preserving Lie–Trotter discretizations for the stochastic heat equation, *ESAIM: Mathematical Modelling and Numerical Analysis* (2024), for prior nonnegativity and finite-time moment estimates.
