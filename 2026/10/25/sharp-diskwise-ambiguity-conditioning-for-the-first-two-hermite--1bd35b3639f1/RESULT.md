# Sharp diskwise ambiguity conditioning for the first two Hermite windows

## Finding

For each \(R>0\), let \(D_R=\{(x,\omega)\in\mathbb R^2:\pi(x^2+\omega^2)\le R\}\). Write \(h_0(t)=2^{1/4}e^{-\pi t^2}\), \(h_1(t)=2\sqrt\pi\,t h_0(t)\), and use the centered ambiguity function
\[
\mathcal A g(x,\omega)=\int_{\mathbb R}g(t+x/2)\overline{g(t-x/2)}e^{-2\pi i\omega t}\,dt.
\]
For a power split \(0\le w\le1\), consider the linear two-channel map on \(L^2(D_R)\):
\[
T_{R,w}\Phi=\left(\sqrt{1-w}\,\overline{\mathcal A h_0}\,\Phi,\;\sqrt w\,\overline{\mathcal A h_1}\,\Phi\right).
\]
Its exact squared lower bound is
\[
\mu_R(w)=\inf_{\Phi\ne0}\frac{\|T_{R,w}\Phi\|_2^2}{\|\Phi\|_2^2}
=\min_{0\le s\le R}e^{-s}\bigl[1+w s(s-2)\bigr].
\]
The maximum \(M(R)=\max_{0\le w\le1}\mu_R(w)\) and **all** optimal allocations are:

- If \(0<R<2\), only \(w=0\) is optimal and \(M(R)=e^{-R}\).
- If \(R=2\), exactly \(0\le w\le1/2\) are optimal and \(M(2)=e^{-2}\).
- If \(R>2\), there is exactly one optimum \(w_*(R)\in(1/2,1)\). Let \(u_R\in(0,1)\) be the unique solution of
\[
2(1-u_R)e^{R-2+u_R}=(R-1)^2+1-u_R^2.
\]
Then
\[
w_*(R)=\frac1{2-u_R^2},\qquad
M(R)=e^{-R}\bigl[1+w_*(R)R(R-2)\bigr]
=\frac{2(1-u_R)e^{u_R-2}}{2-u_R^2}.
\]

The optimal weight is strictly increasing on \((2,\infty)\), with the sharp limiting laws
\[
\begin{aligned}
w_*(2+t)&=\tfrac12+\tfrac{t^2}{16}+O(t^3)\quad(t\downarrow0),\\
1-w_*(R)&=(R-1)^2e^{1-R}\bigl[1+O(R^2e^{-R})\bigr]\quad(R\to\infty),\\
M(R)&=e^{-R}(R-1)^2\bigl[1+O(R^2e^{-R})\bigr]\quad(R\to\infty).
\end{aligned}
\]
Since \(\|T_{R,w}\|=1\), the least achievable inverse norm on the range is exactly \(M(R)^{-1/2}\). Relative to the Gaussian-only inverse norm \(e^{R/2}\), the optimal two-window design improves the amplification factor asymptotically by \(R\).

## Assumptions and scope

Both Hermite functions have unit \(L^2(\mathbb R)\) norm, the Fourier exponential is \(e^{-2\pi i\omega t}\), and \(R\) is **\(\pi\) times squared physical time-frequency radius**, not physical radius itself. The two output channels are measured in the direct-sum \(L^2(D_R)\) norm; their precisions or data weights sum to one. The domain comprises arbitrary complex \(L^2\) ambiguity-field values on the disk. The result concerns this exact linear inversion stage, not the full nonlinear signal phase-retrieval problem.

## Proof

**1. Exact radial multiplier.** Direct Gaussian integration, or the Hermite–Laguerre ambiguity identity, gives \(\mathcal A h_0=e^{-s/2}\) and \(\mathcal A h_1=e^{-s/2}(1-s)\) for \(s=\pi(x^2+\omega^2)\). Hence
\[
\|T_{R,w}\Phi\|_2^2=\int_{D_R}e^{-s}\bigl[1+w s(s-2)\bigr]|\Phi|^2.
\]
The continuous radial multiplier attains its essential infimum in every small positive-area neighborhood of any minimizer, including the boundary, proving the displayed sharp lower bound. Moreover \(|\mathcal A h_j(x,\omega)|\le\|h_j\|_2^2=1\) by Cauchy–Schwarz, and both are one at the origin. Therefore \(\|T_{R,w}\|=1\).

**2. Before the critical radius.** On \(0<s<2\), \(s(s-2)<0\), so any \(w>0\) decreases the multiplier at the endpoint whenever \(R<2\). The Gaussian \(w=0\) has minimum \(e^{-R}\), establishing unique optimality. At \(R=2\), the multiplier equals \(e^{-2}\) at \(s=2\), for every \(w\). Its derivative is
\[
\frac{d}{ds}F_w(s)=e^{-s}\{ -1+w[2-(s-2)^2]\}.
\]
For \(0\le w\le1/2\) it is nonpositive throughout, giving equality; for \(w>1/2\) it has a strict local minimum inside \((1,2)\) below \(e^{-2}\). This proves the entire equality classification at \(R=2\).

**3. The two competing minima.** For \(R>2\), every \(0\le w\le1/2\) yields a decreasing multiplier and endpoint minimum \(B_R(w)=e^{-R}[1+wR(R-2)]\), strictly increasing with \(w\). For \(w>1/2\), put \(u=\sqrt{2-1/w}\in(0,1)\). The derivative has the sign of \(u^2-(s-2)^2\); its only internal local minimum occurs at \(s=2-u\), with value
\[
A(w)=\frac{2(1-u)e^{u-2}}{2-u^2}.
\]
Over the entire interval \([0,R]\), the minimum is exactly \(\min\{A(w),B_R(w)\}\). Indeed the other critical point \(s=2+u\) is a maximum, \(F_w(0)=1\), and \(F_w(2)=e^{-2}>A(w)\). The inner minimum \(A(w)\) decreases strictly on \((1/2,1)\): at its minimizer the derivative with respect to \(w\) is \(e^{-(2-u)}(2-u)(-u)<0\). Meanwhile \(B_R\) increases strictly. At \(w=1/2\), \(A=e^{-2}>B_R\), since \(e^t>1+t+t^2/2\) for \(t=R-2>0\). At \(w=1\), \(A=0<B_R\). Thus their unique crossing is the unique global optimum. Substituting \(w=1/(2-u^2)\) yields the stated implicit equation and value of \(M\).

**4. Root uniqueness and monotonicity.** Let
\[
H(R,u)=2(1-u)e^{R-2+u}-[(R-1)^2+1-u^2].
\]
For \(R>2\), \(H(R,0)>0\), \(H(R,1)<0\), and \(\partial_uH=2u(1-e^{R-2+u})<0\) for \(0<u<1\). Thus \(u_R\) is well defined and unique. On the root, \(\partial_RH=(R-2)^2-u_R^2\). If \(R\ge3\) this is positive. If \(2<R<3\), let \(t=R-2\in(0,1)\); the inequality \((1-t)e^{2t}<1+t\), equivalent to \(t<\operatorname{artanh}(t)\), implies \(H(R,t)<0\), so \(u_R<t\) and again \(\partial_RH>0\). Implicit differentiation shows \(u_R'>0\); so \(w_*' >0\).

**5. Sharp asymptotics.** With \(t=R-2\), the relation \(H(R,u_R)=0\) and \(0<u_R<t\) imply \(u_R/t\to1/2\): divide its Taylor expansion by \(t^3\) to obtain \(1/3-c^2-2c^3/3=0\), whose sole root in \([0,1]\) is \(c=1/2\). The derivative at this root is nonzero, yielding \(u_R=t/2+O(t^2)\) and hence \(w_*=1/2+t^2/16+O(t^3)\). As \(R\to\infty\), the root relation forces \(u_R\to1\). Writing \(q=1-u_R\) gives
\[
2q e^{R-1-q}=(R-1)^2+2q-q^2,
\]
so \(q=\tfrac12(R-1)^2e^{1-R}[1+O(R^2e^{-R})]\). Expanding \(w_*=(1+2q-q^2)^{-1}\) and substituting into \(M=e^{-R}[1+w_*R(R-2)]\) completes the proof.

## Verification

The standalone standard-library program `check.py` corroborates the two equal active minima, the strict optimality against a grid of alternative allocations, the threshold, monotonicity and asymptotic regimes. It passed 1,698 deterministic numerical assertions for radii from \(0.1\) through \(20\). For example, at \(R=3\) the optimizer is approximately \(0.546009071464\) and the sharp squared lower bound approximately \(0.131339641279\). The proof above, not finite sampling, establishes all statements for every real \(R>0\).

## Relationship to prior work

Alaifari and Yang (arXiv:2410.05486, first public 2024-10-07) provide the Hermite–Laguerre ambiguity identity and study multiwindow spectrogram reconstruction by combining annular stability sets. Their construction does not determine the budget-constrained two-channel \(L^2\) multiplier condition number, its exact optimal allocation, or the critical radius. Grohs, Liehr and Rathmair (arXiv:2207.10620) establish sampled multiwindow *uniqueness* using linear combinations of Gaussian and first-Hermite windows; their statements do not imply this continuous two-channel minimax conditioning law. Comparisons with searched published mathematical records likewise identified no containing claim. A full historical novelty guarantee is not asserted.

## Limitations

The sharp constant applies to the unrestricted linear multiplication map on \(L^2(D_R)\); actual ambiguity functions of signals form a constrained nonlinear subset, so the theorem does not give a sharp global nonlinear phase-retrieval stability constant. It assumes exactly two fixed normalized windows and a unit sum of channel precision weights; optimized windows of other orders or different noise covariance models may outperform this design. No performance claim outside \(D_R\) follows. The historical-priority assessment is best-knowledge and not independent verification.

## References

1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486, first posted 2024-10-07; especially §2.2 (Hermite–Laguerre identity and stability sets) and §3.2 (multiwindow stability).
2. P. Grohs, L. Liehr and M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620, first posted 2022-07-21; especially §1.1 (Gaussian–Hermite window combinations and lattice uniqueness).
