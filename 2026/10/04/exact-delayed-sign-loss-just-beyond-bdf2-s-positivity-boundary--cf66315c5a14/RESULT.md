# Exact delayed sign loss just beyond BDF2's positivity boundary
## Finding
Apply backward Euler once and then the standard constant-step BDF2 method to the positive scalar decay equation
\[
u'(t)=-\lambda u(t),\qquad u(0)=u_0>0,
\]
with \(\lambda>0\), step size \(h>0\), and \(r=h\lambda\). Write \(u_n=z_nu_0\). Then
\[
z_0=1,\qquad z_1=\frac{1}{1+r},\qquad (3+2r)z_n=4z_{n-1}-z_{n-2}\quad(n\ge2).
\]
The classical all-step positivity boundary \(r\le1/2\) is prior work. Above that boundary, the first negative BDF2 value has the exact index
\[
N_-(r)=\min\{n\in\mathbb N:n\theta(r)>\tfrac\pi2+\phi(r)\}
       =\left\lfloor\frac{\pi/2+\phi(r)}{\theta(r)}\right\rfloor+1,
\]
where
\[
\theta(r)=\arccos\!\left(\frac{2}{\sqrt{3+2r}}\right),\qquad
\phi(r)=\arctan\!\left(\frac{1}{(1+r)\sqrt{2r-1}}\right).
\]
Equivalently, for every \(r>1/2\), \(z_n\ge0\) for \(0\le n<N_-(r)\) and \(z_{N_-(r)}<0\).

The loss of positivity is therefore critically delayed near the known threshold:
\[
N_-(r)\sqrt{r-\tfrac12}\longrightarrow \pi\sqrt2
\qquad\text{as }r\downarrow\tfrac12.
\]
More precisely, if
\[
q(r)=\frac{\pi/2+\phi(r)}{\theta(r)},
\]
then
\[
q(r)=\pi\sqrt{\frac{2}{r-1/2}}-3+O\!\left(\sqrt{r-1/2}\right).
\]
Thus a step size only slightly beyond the positivity threshold can generate a long apparently positive transient before the first wrong-signed value.

## Assumptions and scope
The starter is one backward Euler step with the same constant step size \(h\). The recurrence is exact arithmetic for the scalar test equation. Positivity means \(u_n\ge0\) for positive \(u_0\). The result concerns sign preservation, not linear stability: BDF2 remains stable on the negative real axis even when positivity is eventually lost.

The finding is specifically the exact first-sign-loss index and its square-root divergence above the already-known boundary \(r=1/2\). The boundary itself, BDF2's general monotonicity coefficient, and the fact that large steps can spoil positivity are not claimed as new.

## Proof
Substitution of \(u_n=z_nu_0\) into backward Euler and BDF2 gives the stated recurrence. Its characteristic polynomial is
\[
(3+2r)\xi^2-4\xi+1=0.
\]

For \(0<r<1/2\), let \(s=\sqrt{1-2r}\). The roots are
\[
\xi_+=\frac{1}{2-s},\qquad \xi_- =\frac{1}{2+s}.
\]
Solving for the coefficients from \(z_0=1\) and \(z_1=1/(1+r)\) gives
\[
z_n=A_s(2-s)^{-n}-B_s(2+s)^{-n},
\]
where
\[
A_s=\frac{(2-s)(1+s)^2}{2s(3-s^2)},\qquad
B_s=\frac{(2+s)(1-s)^2}{2s(3-s^2)}.
\]
Both are positive and \(A_s-B_s=1\). Since \((2-s)^{-n}\ge(2+s)^{-n}\), every \(z_n\) is positive. At \(r=1/2\), the root is repeated and direct solution gives
\[
z_n=2^{-n}\left(1+\frac n3\right)>0.
\]
This reproduces the known sharp positivity side of the boundary.

For \(r>1/2\), set
\[
\rho=(3+2r)^{-1/2},\qquad
\cos\theta=\frac{2}{\sqrt{3+2r}},\qquad
\sin\theta=\frac{\sqrt{2r-1}}{\sqrt{3+2r}}.
\]
The characteristic roots are \(\rho e^{\pm i\theta}\), with \(0<\theta<\pi/2\). Matching the starter gives
\[
z_n=\rho^n\left[\cos(n\theta)+\beta\sin(n\theta)\right],
\qquad
\beta=\frac{1}{(1+r)\sqrt{2r-1}}.
\]
With \(\phi=\arctan\beta\), this becomes
\[
z_n=\rho^n\sqrt{1+\beta^2}\,\cos(n\theta-\phi).
\]
Because \(-\phi\in(-\pi/2,0)\) and each increment in phase is \(\theta\in(0,\pi/2)\), the first negative value occurs exactly when
\[
n\theta-\phi>\frac\pi2.
\]
This is the stated formula for \(N_-(r)\), including the case when equality occurs at an integer index: equality gives \(z_n=0\), so negativity begins at the following index.

Finally put \(r=1/2+\varepsilon\). Elementary expansions give
\[
\theta=\sqrt{\varepsilon/2}+O(\varepsilon^{3/2}),
\qquad
\phi=\frac\pi2-3\sqrt{\varepsilon/2}+O(\varepsilon^{3/2}).
\]
Hence
\[
q(r)=\frac{\pi/2+\phi}{\theta}
=\pi\sqrt{\frac{2}{\varepsilon}}-3+O(\sqrt\varepsilon).
\]
Since \(N_-(r)=\lfloor q(r)\rfloor+1\), multiplication by \(\sqrt\varepsilon\) yields the claimed limit \(\pi\sqrt2\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic for the BDF2 recurrence. It checks the critical formula \(z_n=2^{-n}(1+n/3)\), verifies exact first-negative indices for representative supercritical rational values, and checks positivity on a finite rational grid below the threshold. It separately compares the closed phase formula with recurrence signs away from floating-point boundary ambiguities and numerically confirms convergence of \(N_-(r)\sqrt{r-1/2}\) toward \(\pi\sqrt2\).

These finite checks corroborate indexing and algebra. The all-parameter statements are proved above and do not rely on numerical enumeration.

## Relationship to prior work
Hundsdorfer, Ruuth, and Spiteri analyze monotonicity-preserving linear multistep methods together with starting procedures. Their implicit two-step section identifies the familiar implicit BDF2 method and gives the sharp monotonicity threshold coefficient \(1/2\); the same report explicitly notes backward Euler as a suitable starting procedure. Therefore the boundary \(r\le1/2\) is prior-covered and excluded from the novelty claim.

Hundsdorfer's earlier BDF2-blend report studies positivity for linear systems with suitable starters and explains that standard implicit BDF2 loses monotonicity for large steps. It supplies the same broader mechanism but does not state the exact first-negative index or the near-threshold delay law above in the inspected positivity sections.

Targeted searches for BDF2 positivity, nonoscillatory behavior, complex characteristic roots, sign changes, and backward-Euler starts located stability and positivity-threshold discussions but no statement equivalent to the exact phase formula for \(N_-(r)\) or the limit \(N_-(r)\sqrt{r-1/2}\to\pi\sqrt2\).

## Limitations
The result is for a scalar constant-coefficient decay mode with a backward-Euler starter and fixed step size. It does not claim the same first-failure law for variable-step BDF2, other starters, nonlinear equations, or coupled systems. The exact phase law concerns positivity only; it is not an instability threshold.

The originality search cannot exclude an equivalent formula in older specialist literature on multistep oscillations or root geometry that is not indexed by the terminology searched. The known monotonicity threshold is intentionally treated as prior work.

## References
1. W. Hundsdorfer, S. J. Ruuth, and R. J. Spiteri, *Monotonicity-Preserving Linear Multistep Methods*, CWI Report MAS-R0210, April 30, 2002; later SIAM Journal on Numerical Analysis 41(2), 605--623, DOI: 10.1137/S0036142902406326.
2. W. Hundsdorfer, *Partially Implicit BDF2 Blends for Convection Dominated Flows*, CWI Report MAS-R9831, 1998; later SIAM Journal on Numerical Analysis 38(6), 1763--1783, DOI: 10.1137/S0036142999364741.
