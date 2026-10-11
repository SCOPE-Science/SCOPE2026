# Sharp extinction and persistence at the homogeneous max-plus border collision

## Finding
Consider the continuous piecewise-linear map
\[
F_{T,D}(x,y)=\bigl(y+\max(0,Tx),-\max(0,Dx)\bigr),
\qquad (x,y)\in\mathbb R^2,\quad T\ge0,\quad D>0.
\]
This is the zero-input, or border, slice of the generalized max-plus oscillator of Ohmori and Yamazaki. Write \(\Delta=T^2-4D\). For an initial state \(z\), define its **exact extinction time**
\[
\tau(z)=\inf\{n\in\mathbb Z_{\ge0}:F_{T,D}^{\,n}(z)=(0,0)\},
\qquad\inf\varnothing=\infty.
\]
The following statements form a complete global classification of finite-step extinction for this family.

**Oscillatory regime.** If \(\Delta<0\), let \(\theta=\arccos(T/(2\sqrt D))\in(0,\pi/2]\). Every state reaches the origin, and the **least uniform annihilation exponent** is exactly
\[
\boxed{\min\{N\ge0:F_{T,D}^{\,N}\equiv(0,0)\}
=2+\left\lceil\frac\pi\theta\right\rceil.}
\]
Thus the global uniform extinction index is an integer staircase in the positive-branch rotation angle. At fixed \(T>0\), as \(4D-T^2\downarrow0\) from positive values,
\[
N(T,D)=\frac{\pi T}{\sqrt{4D-T^2}}+O(1).
\]

**Critical and overdamped regimes.** If \(\Delta\ge0\), put
\[
\lambda_+=\frac{T+\sqrt\Delta}{2}>0.
\]
Exactly the following initial points never reach the origin in finite time:
\[
\boxed{\mathcal P_{T,D}=
\{(x,y):x>0,\ y\ge-\lambda_+x\}
\;\cup\;\{(x,y):x\le0,\ y>0\}.}
\]
This describes persistence of a strictly positive first coordinate, not necessarily divergence: persistent orbits can converge asymptotically to the origin without ever reaching it.

For \(x>0\) and \(y<-\lambda_+x\), define the positive distance parameter \(\delta=-(y+\lambda_+x)>0\). Then extinction occurs at the **exact** time
\[
\boxed{\tau(x,y)=\begin{cases}
2+\left\lceil\dfrac{\lambda_+x}{\delta}\right\rceil,
&\Delta=0,\\[2mm]
2+\left\lceil\dfrac{\log(1+(\lambda_+-\lambda_-)x/\delta)}{\log(\lambda_+/\lambda_-)}\right\rceil,
&\Delta>0,
\end{cases}}
\]
where \(\lambda_-=(T-\sqrt\Delta)/2>0\) in the second line. For \(x\le0,y\le0\), extinction takes at most two iterates. Therefore the map is uniformly nilpotent **if and only if** \(T^2<4D\), while the extinction time on the extinct side of the persistent-cone boundary diverges algebraically in \(\delta^{-1}\) at the repeated-root threshold and logarithmically in \(\delta^{-1}\) above it.

## Assumptions and scope
The parameters \(T\) and \(D\) are fixed real numbers with \(T\ge0\) and \(D>0\). All initial conditions in the full plane \(\mathbb R^2\) are included, including the switching line \(x=0\), on which \(\max(0,Tx)=\max(0,Dx)=0\). The time \(\tau\) counts applications of the original map from iteration zero; an initial point already at the origin has \(\tau=0\). The formulas concern **exact finite-time arrival**, not the possibly slower asymptotic attraction of a persistent orbit. The case \(D=0\) is not asserted.

## Proof
### 1. Reset reduction
For \(x\le0\), one application gives \(F(x,y)=(y,0)\). If also \(y\le0\), a second application gives \((0,0)\). If \(y>0\), the next state is \((y,0)\), entering the positive half-plane.

For \(x>0\), the branch is linear with matrix
\[
A=\begin{pmatrix}T&1\\-D&0\end{pmatrix}.
\]
As long as the first coordinate remains strictly positive, the first coordinates satisfy the scalar recurrence
\[
x_{n+2}=Tx_{n+1}-Dx_n,\qquad x_1=Tx_0+y_0.
\]
Let \(k\ge1\) be the **first** index for which \(x_k\le0\), following a run beginning with \(x_0>0\). The preceding value is \(x_{k-1}>0\), hence \(y_k=-Dx_{k-1}<0\). Consequently
\[
F(x_k,y_k)=(y_k,0)\ne(0,0),\qquad
F^2(x_k,y_k)=(0,0).
\]
The extinction time is therefore exactly \(k+2\); equality \(x_k=0\) does not alter this count. If there is no such \(k\), every iterate remains on the positive branch and cannot equal the origin.

### 2. Oscillatory regime and sharp uniform index
Suppose \(T^2<4D\). Let \(\rho=\sqrt D\) and \(\theta=\arccos(T/(2\rho))\). Then \(0<\theta\le\pi/2\), and the scalar recurrence has characteristic roots \(\rho e^{\pm i\theta}\). For any \(x_0>0\) there exist \(C>0\) and \(0<\phi<\pi\) such that, up to the first nonpositive value,
\[
x_n=C\rho^n\sin(\phi+n\theta).
\]
Because the angular increment does not exceed \(\pi/2\), an orbit cannot skip the nonpositive half of a sine period. The first \(n\ge1\) satisfying \(\phi+n\theta\ge\pi\) occurs no later than \(m=\lceil\pi/\theta\rceil\), and its sine is nonpositive. Thus this positive run has its first exit by step \(m\), and reset completes by step \(m+2\).

If \(x_0\le0<y_0\), the initial step gives \((y_0,0)\). Writing its first-coordinate sequence after this step, one has, until exit,
\[
x_{1+j}=y_0\rho^j\frac{\sin((j+1)\theta)}{\sin\theta},
\qquad j\ge0.
\]
The first nonpositive value occurs at \(j=m-1\), or at absolute time \(m\), and again the origin is reached by time \(m+2\). The remaining initial states vanish within two steps. Hence \(F^{m+2}\equiv0\).

To prove the exponent **minimal**, choose \(0<\phi<\pi-(m-1)\theta\), and set
\[
x_0=\sin\phi,
\qquad y_0=\rho\sin(\phi+\theta)-T\sin\phi.
\]
For this state \(x_n=\rho^n\sin(\phi+n\theta)>0\) for \(0\le n<m\), whereas \(x_m<0\). Its state at time \(m+1\) equals \((-Dx_{m-1},0)\ne0\); it first vanishes at time \(m+2\). Therefore no smaller uniform exponent exists. Finally, for fixed \(T>0\), the elementary expansion \(\arccos(T/(2\sqrt D))\sim\sqrt{4D-T^2}/T\) gives the displayed divergence of \(N\).

### 3. Repeated positive root
Suppose \(\Delta=0\). Let \(\lambda=T/2=\sqrt D\). If \(x_0>0\), put \(s=y_0+\lambda x_0\). The positive-branch recurrence has the exact solution
\[
x_n=\lambda^n\left(x_0+\frac{ns}{\lambda}\right).
\]
If \(s\ge0\), all these coordinates are positive, giving persistence. If \(s=-\delta<0\), the first nonpositive coordinate occurs at
\[
k=\left\lceil\frac{\lambda x_0}{\delta}\right\rceil.
\]
The reset reduction proves the critical extinction-time formula, including integral threshold cases exactly.

### 4. Distinct positive roots
Suppose \(\Delta>0\). Then \(0<\lambda_-<\lambda_+\). With \(s=y_0+\lambda_+x_0\), set \(G=\lambda_+-\lambda_->0\) and \(q=\lambda_-/\lambda_+\in(0,1)\). The positive-branch first coordinate is
\[
x_n=\lambda_+^n\left[\frac{s}{G}(1-q^n)+x_0q^n\right].
\]
For \(s\ge0\) both terms in brackets are nonnegative and the second is strictly positive, so the orbit persists. If \(s=-\delta<0\), the first nonpositive coordinate is characterized by
\[
q^k\le\frac{\delta}{Gx_0+\delta},
\quad\text{or}\quad
k=\left\lceil\frac{\log(1+Gx_0/\delta)}{\log(\lambda_+/\lambda_-)}\right\rceil.
\]
The two-step reset yields the exact overdamped extinction-time formula.

Finally, when \(x_0\le0<y_0\), the next state is \((y_0,0)\), for which the positive-root coefficient \(s=\lambda_+y_0>0\); it therefore persists. When \(x_0\le0,y_0\le0\), extinction occurs within two steps, by Step 1. This proves the claimed global persistence set and completes the trichotomy.

## Verification
The accompanying standalone program `check_exact.py` uses exact rational arithmetic to reconstruct the map, check global finite-time collapse on several underdamped parameter slices and rational initial grids, exhibit witnesses attaining the proposed sharp exponents, and test exact critical/overdamped extinction times at parameter choices with rational characteristic roots. It prints `EXACT_RATIONAL_REGRESSION_OK` on success. These finite checks do **not** prove the universal theorem; Steps 1–4 supply its proof for all real parameters and initial conditions. To rerun, use `python3 check_exact.py` with Python 3 and no third-party dependencies.

## Relationship to prior work
Ohmori and Yamazaki [1] introduce the generalized max-plus family, the positive and negative branch matrices, and the connection to the border-collision normal form. In [1, §3.2 and §4], the main dynamical cases take nonzero forcing \(B=\pm1\), and [1, §5.3] identifies \(B=0\) as the border-collision parameter. The present result addresses the **unforced map itself**, gives an all-initial-condition classification, and determines the **smallest** annihilating iterate in the oscillatory regime and the exact lifetimes next to its persistent boundary. These conclusions do not follow merely from the existence of a spiral branch or from the periods of nonzero-forcing cycles.

Ohmori and Yamazaki [2] explicitly obtain an at-most-four-step reset on the older negative-feedback slice \(T=0\) with \(B<0\); the \(T=0\) four-step behavior is thus a familiar limiting special case, not asserted as novel in isolation. Yamazaki and Ohmori [3, Eq. (11)] already formulate the two-independent-parameter generalized family (public 5 December 2023), leaving its dynamics for later work; their analyzed cases concern nonzero-forcing Sel'kov cycles and phase-locking delays, not homogeneous full-plane extinction. Their logarithmic bottleneck **parameter** law concerns a different nonzero-forcing phase-drift mechanism, not the exact initial-condition extinction time derived here. Simpson [4] studies precisely the broader two-dimensional zero-determinant border-collision normal form and notes in §4.1 that the zero-forcing case is a special case **outside the scope** of that analysis. The present full classification concerns the additional degenerate subfamily \(\tau_L=\delta_L=\mu=0\), \(\tau_R=T\), \(\delta_R=D\), and gives finite-time rather than just asymptotic or bifurcation-type data.

## Limitations
The claims concern the exact piecewise-linear unforced model with \(D>0\); no robustness under smoothing, nonzero forcing, random perturbations, or delayed feedback is asserted. The underdamped result is a **uniform finite-time** law; the critical/overdamped result distinguishes exact persistence from convergence in norm. The external literature comparison does not settle every possible historical priority issue.

## References
1. Shousuke Ohmori and Yoshihiro Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230v1, first public 9 February 2024; later *Journal of Mathematical Physics* **65** (2024), 082705, DOI 10.1063/5.0203186. https://arxiv.org/abs/2402.06230
2. Shousuke Ohmori and Yoshihiro Yamazaki, *Dynamical properties of discrete negative feedback models*, arXiv:2305.05908v1 (2023). https://arxiv.org/abs/2305.05908
3. Yoshihiro Yamazaki and Shousuke Ohmori, *Ultradiscretization in discrete limit cycles of tropically discretized and max-plus Sel'kov models*, arXiv:2312.13292v1 (2023). https://arxiv.org/abs/2312.13292
4. David J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1 (2024), especially §4.1. https://arxiv.org/abs/2408.04790
5. Soumitro Banerjee and Celso Grebogi, *Border collision bifurcations in two-dimensional piecewise smooth maps*, *Physical Review E* **59** (1999), 4052–4061, DOI 10.1103/PhysRevE.59.4052 (background classification).
