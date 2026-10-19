# Resonant ninth-order energy drift and a Riccati slow-time law for nonlinear RK325

## Finding
Consider the nonlinear planar rotation
\[
 \dot U=(a+b\|U\|_2^2)JU,\qquad
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad a>0,\ b<0.
\]
Its exact energy \(\mathcal E(U)=\|U\|_2^2/2\) is constant. Apply the explicit three-stage Runge--Kutta scheme
\[
 k_1=F(U_n),\quad k_2=F(U_n+hk_1/2),\quad k_3=F(U_n+hk_2),\qquad
 U_{n+1}=U_n+\frac h4(k_1+2k_2+k_3).
\]
This is the nonlinear RK325 tableau from Liu--Brio's revised arXiv manuscript [1, version 2]. Set \(r_n=\|U_n\|_2^2\). For every fixed \(r>0\) with \(w=a+br\ne0\), the exact one-step radial change satisfies
\[
 r_{n+1}-r_n=\frac{r w^4(a+2br)^2}{64}h^6+O(h^8),\qquad r_n=r.
\]
The leading coefficient is positive except at the single nonstationary positive radius \(r_\star=-a/(2b)\). At this radius \(w_\star=a/2\) and the first nonzero increment is instead
\[
 r_{n+1}-r_\star=\frac{r_\star}{1024}(h w_\star)^{10}+O(h^{12}).
\]
Thus the local energy error of RK325 has order nine at a unique nonstationary amplitude, whereas its generic order is five. The other exceptional positive radius \(-a/b\) has zero vector field and is stationary, not an energy-accuracy resonance.

The resonance governs a previously unquantified long-time transition. Write \(H=ha/2\), initialize \(r_0=r_\star\), and set
\[
 y_n=H^{-2}(r_n/r_\star-1),\qquad \tau_n=nH^8.
\]
For every \(T<128\), as \(h\to0^+\),
\[
 \max_{0\le n\le\lfloor T/H^8\rfloor}\left|y_n-
 \frac{\tau_n}{1024-8\tau_n}\right|=O_T(H^2).
\]
The rescaled radial energy defect therefore evolves according to the nonconstant Riccati law \(y'= (8y+1)^2/1024\), \(y(0)=0\), on the long step-count scale \(n\asymp h^{-8}\), i.e. physical times of scale \(h^{-7}\). The pole at scaled time \(128\) belongs to the limiting differential equation: no finite-step numerical blow-up at that point is asserted.

## Assumptions and scope
All data are real, \(a>0\), \(b<0\), \(h>0\), and arithmetic is exact. The method has a constant timestep and its three stages are the stated nonlinear RK325 stages. The special initial radius is \(r_\star=-a/(2b)>0\). No angular phase estimate is claimed. The asymptotic estimate is uniform on every compact scaled-time interval \([0,T]\) strictly before \(128\); it does not assert convergence at or beyond the limiting pole. For generic fixed radii the remainder is pointwise in \(r\), not a uniform statement through \(w=0\).

## Proof
**1. Exact radial polynomial.** Rotational equivariance lets us take the input state \(U=(\sqrt r,0)\). At \(w=a+br\ne0\), define \(t=hw\) and \(q=br/w\). In units where the initial radius is one, set
\[
 B=1+qt^2/4,\quad X_3=1-t^2B/2,\quad Y_3=-tB,
 \quad C=1+q(X_3^2+Y_3^2-1),
\]
\[
 X=1-t^2B(1+C)/4,\qquad Y=-t(1+2B+CX_3)/4,
 \qquad Q(t,q)=X^2+Y^2.
\]
These are the exact normalized three stage positions and the normalized output. In particular, for every nonzero \(w\), \(r_{n+1}=r_n Q(hw,br/w)\). The expressions are polynomials in \(t,q\), with no truncation or division involved once \(t,q\) are defined.

**2. Energy cancellation and its uniqueness.** Expanding this finite polynomial yields the exact coefficients
\[
 Q(t,q)-1=\frac{(q+1)^2}{64}t^6
 -\frac{q(q+1)(2q+1)}{128}t^8
 +\frac{q(9q+8)}{1024}t^{10}+O(t^{12}).
\]
The coefficients at orders two and four vanish identically; all odd powers vanish. Substituting \(q=br/(a+br)\) yields the stated generic leading coefficient \(rw^4(a+2br)^2/64\). Since \(r>0\), \(w\ne0\), and \(a>0,b<0\), this coefficient vanishes exactly when \(r=r_\star=-a/(2b)\), namely \(q=-1\). At \(q=-1\), the coefficients at orders six and eight vanish, while the coefficient at order ten becomes \(1/1024\), proving exact local ninth-order energy accuracy. At \(a+br=0\), \(F(U)=0\), so the algorithm fixes the state identically; that is a separate trivial stationarity case.

**3. Uniform slow-scale consistency.** For \(r=r_\star(1+H^2y)\), one has exactly
\[
 w=(a/2)(1-H^2y),\quad t=H(1-H^2y),\quad
 q=-\frac{1+H^2y}{1-H^2y}.
\]
Substitute these identities into the exact polynomial \(rQ(t,q)\). On every bounded interval of \(y\), elementary expansion (or exact symbolic polynomial arithmetic) gives, uniformly,
\[
 \frac{r_{n+1}-r_n}{r_\star}
 =H^{10}\frac{(8y+1)^2}{1024}+O(H^{12}),
\]
so the rescaled recurrence satisfies
\[
 y_{n+1}=y_n+H^8 f(y_n)+O(H^{10}),
 \qquad f(y)=(8y+1)^2/1024.
\]
This uniform estimate follows from an analytic expression whose only possible denominator is \(1-H^2y\), bounded away from zero on fixed bounded \(y\)-sets for small enough \(H\). This also independently identifies the coefficient in the squared-radius layer.

**4. Long-time convergence.** The solution of \(y'=f(y)\), \(y(0)=0\), is
\[
 y(\tau)=\frac{\tau}{1024-8\tau},\qquad 0\le\tau<128.
\]
For fixed \(T<128\), this solution and its derivative are bounded on \([0,T]\). Choose a bounded interval containing its image in its interior. On that interval \(f\) is Lipschitz, with Lipschitz constant independent of \(H\). Comparing the recurrence with the exact flow on each time interval of length \(H^8\), the one-step discrepancy is \(O(H^{10})+O(H^{16})\). Discrete Gronwall for \(\lfloor T/H^8\rfloor\) steps gives an \(O_T(H^2)\) uniform error; the bound closes the bootstrap that all numerical \(y_n\) remain within the chosen interval. Thus the asserted convergence and its rate hold up to every \(T<128\), including the floor endpoint.

## Verification
The standalone `verify.py` reproduces the complete polynomial coefficients at powers six, eight, ten and twelve by exact symbolic arithmetic, proves the critical tenth-order coefficient, confirms the uniform-layer coefficient by a symbolic limit, and performs twelve exact rational comparisons between direct Cartesian RK325 updates and the radial polynomial. Direct floating-point integrations at decreasing \(h\) additionally approach the explicit Riccati law; these are illustrations, not a proof of its infinite-time-in-steps asymptotics.

## Relationship to prior work
Liu and Brio's preprint [1] was first publicly posted on 2024-05-08. **Its original 2024 version studies linear skew-symmetric systems only.** The nonlinear RK325 tableau and fifth-order generic nonlinear energy analysis appear in the later revision posted 2026-05-10 [1, version 2], Section 3.1, equations (72)--(76). Their published construction and generic fifth-order accuracy are prior work, not contributions here. The present finding is the amplitude-specific order-nine cancellation plus a matched, nontrivial \(h^{-8}\)-step Riccati energy-drift limit; neither conclusion occurs in the inspected relevant sections or nonlinear examples. It uses the earliest public date of the manuscript as its source date, **not** the date of the nonlinear revision; the chronological distinction is explicit so that the two are not conflated. Background literature on energy-preserving and relaxation Runge--Kutta methods [2] concerns different integrators and does not entail this specific defect law.

## Limitations
The classification only concerns the specified one-parameter cubic amplitude-frequency rotation and the particular three-stage tableau. The limiting pole does not establish actual divergence of the discrete radius. No global-in-time boundedness, absolute stability, nonlinear symplecticity, phase error control, extension to other Runge--Kutta schemes, or convergence at the Riccati pole is proved. The source manuscript's original 2024 posting does not contain the nonlinear method, which was disclosed in the 2026 revision; this bibliographic distinction remains important to chronology and priority. Publication novelty beyond the literature inspected is not independently established.

## References
[1] J. Liu and M. Brio, *Energy-superconvergent Runge--Kutta Time Discretizations*, arXiv:2405.05448v1 (first public posting 2024-05-08); revised as *Energy-superconvergent Explicit Runge--Kutta Time Discretizations*, arXiv:2405.05448v2 (2026-05-10), Section 3.1. https://arxiv.org/abs/2405.05448 ; https://arxiv.org/html/2405.05448v2.

[2] D. I. Ketcheson, *Relaxation Runge--Kutta Methods: Conservation and Stability for Inner-Product Norms*, SIAM Journal on Numerical Analysis 57 (2019), 2850--2870. https://doi.org/10.1137/19M1263662.
