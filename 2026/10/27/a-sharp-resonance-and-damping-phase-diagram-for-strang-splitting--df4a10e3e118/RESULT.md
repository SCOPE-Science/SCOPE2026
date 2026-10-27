# A sharp resonance and damping phase diagram for Strang splitting of a partially damped oscillator

## Finding
For a two-dimensional damped oscillator with dissipation acting in only one coordinate, exact rotation/damping Strang splitting is passive for every positive step. Nevertheless, infinitely many step sizes have a nondecaying mode although the exact differential equation is exponentially stable. The complete spectral phase diagram, the optimal damping-rate plateau, and two distinct sharp quadratic near-resonance laws are given below.

Let \(\rho\) denote spectral radius and \(\|\cdot\|_2\) Euclidean operator norm. With \(\alpha=\gamma h/2\) and \(t=|\cos(\omega h)|\cosh\alpha\), the sharp formula is
\[
\rho(S_h)=e^{-\alpha}\begin{cases}1,&t\le1,\\t+\sqrt{t^2-1},&t>1.\end{cases}
\]
The method is asymptotically stable precisely when \(\sin(\omega h)\ne0\). In particular, for \(h_m=m\pi/\omega\) with integer \(m\ge1\), its nondecaying mode persists under unlimited iterations.

## Assumptions and scope
Fix arbitrary \(\omega,\gamma>0\) and \(h>0\). Set
\[
J=\omega\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad R=\gamma\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad \dot z=(J-R)z.
\]
The numerical one-step map is the exact symmetric composition
\[
S_h=e^{-hR/2}\,e^{hJ}\,e^{-hR/2}.
\]
The quadratic energy is \(H(z)=\|z\|_2^2/2\). All claims are exact-arithmetic statements for this split and these matrices. Rotating the rank-one dissipation axis by a fixed orthogonal similarity gives the same classification.

## Proof
**Exact continuous stability.** The characteristic polynomial of \(J-R\) is \(\lambda^2+\gamma\lambda+\omega^2\). As \(\gamma,\omega>0\), both characteristic roots have strictly negative real parts, including the repeated-root case, so all exact trajectories decay exponentially.

**Split matrix and spectrum.** Put \(r=e^{-\alpha}\), \(c=\cos(\omega h)\), and \(s=\sin(\omega h)\). Direct multiplication gives
\[
S_h=\begin{pmatrix}r^2c&-rs\\rs&c\end{pmatrix},\quad
\det S_h=r^2,\quad\operatorname{tr}S_h=(1+r^2)c=2r\cosh(\alpha)c.
\]
Its two eigenvalues are the roots of \(\lambda^2-(1+r^2)c\lambda+r^2=0\). If \(|c|\cosh\alpha\le1\), the roots are conjugate or equal, both of modulus \(r\). Otherwise they are real and their largest modulus is \(r(t+\sqrt{t^2-1})\). This proves the stated exact spectral-radius formula, including its equality case. At the discriminant-zero boundary, the repeated eigenvalue may have a Jordan block; the radius describes the asymptotic \(n\)-th-root rate, not a uniform bound by \(C\rho(S_h)^n\) there.

**Passivity versus asymptotic stability.** Both dissipative half-step factors have operator norm one, and the rotation has norm one, so \(\|S_h\|_2\le1\) for all \(h>0\). If \(s\ne0\), this is strict: norm equality throughout the product would force the initial vector to lie in \(\ker R=\operatorname{span}(e_2)\) and its rotated image also to lie in that same line, impossible when \(s\ne0\). Hence \(\rho(S_h)<1\). When \(s=0\), the rotation is \(\pm I\) and \(S_h=\pm\operatorname{diag}(r^2,1)\); the undamped \(e_2\) mode has eigenvalue \(\pm1\). Thus \(\rho(S_h)<1\) exactly off the resonant steps, while the original continuous flow is stable at all parameter values.

**Optimal phases and narrowing.** Since \(\det S_h=r^2>0\), the spectral radius is at least \(r\). The exact formula shows that equality holds precisely on \(|c|\le\operatorname{sech}\alpha\), an interval centered at \(\pi/2\) modulo \(\pi\) of angular width \(2\arcsin(\operatorname{sech}\alpha)\). As \(\alpha\to\infty\), \(\operatorname{sech}\alpha=2e^{-\alpha}+O(e^{-3\alpha})\) and \(\arcsin x=x+O(x^3)\), proving the width \(4e^{-\alpha}+O(e^{-3\alpha})\).

**Sharp near-resonance rates.** Fix \(h_m=m\pi/\omega\), integer \(m\ge1\); write \(\delta=\omega(h-h_m)\), \(r_m=e^{-\gamma h_m/2}\). For sufficiently small \(|\delta|\), the eigenvalues remain real and the root of largest modulus, after removing \((-1)^m\), solves
\[
\lambda^2-(1+r^2)\cos\delta\,\lambda+r^2=0,\qquad r=e^{-\gamma h/2}.
\]
At \(\delta=0\) its dominant root is one, simple because \(r_m<1\). Implicit differentiation, or substitution of \(\lambda=1-a\delta^2+O(\delta^3)\), yields \(a=(1+r_m^2)/(2(1-r_m^2))=\coth(\gamma h_m/2)/2\). (Variations of \(r\) modify this coefficient only at cubic order.) Hence
\[
1-\rho(S_h)=\tfrac12\coth(\gamma h_m/2)\,\omega^2(h-h_m)^2+O(|h-h_m|^3).
\]
Independently, the squared singular values of \(S_h\) are the roots of \(\mu^2-T\mu+r^4=0\), with
\[
T=\operatorname{tr}(S_h^{\mathsf T}S_h)=2r^2+(1-r^2)^2\cos^2\delta.
\]
At resonance the larger root is one and the smaller is \(r_m^4\). Expanding the larger root gives \(1-[{(1-r_m^2)}/{(1+r_m^2)}]\delta^2+O(\delta^3)\). Taking its positive square root proves
\[
1-\|S_h\|_2=\tfrac12\tanh(\gamma h_m/2)\,\omega^2(h-h_m)^2+O(|h-h_m|^3).
\]
Both coefficients are strictly positive and therefore sharp.

## Verification
The accompanying standalone `verify.py` uses only Python's standard library and can be executed with `python verify.py`. It checks the determinant, matrix eigenvalues, singular values and spectral-radius formulas on deterministic parameter grids, confirms the phase plateau, and compares both near-resonance coefficients with direct spectral calculations. It reports `VERIFICATION_OK 248 deterministic assertions`. Exact symbolic identities and the proof above, not finite tests, establish the universally quantified claims.

## Relationship to prior work
Blanes, Casas and Murua's splitting survey establishes the basic Strang construction, discusses stability polynomials and oscillatory-step resonances, and explains why preserving structure need not guarantee unrestricted stability. Mönch and Marheineke study splitting for linear port-Hamiltonian systems, prove discrete dissipation inequalities and include a damped oscillator test, but do not state the present complete discrete asymptotic-stability classification or its quadratic near-resonance coefficients. Achleitner, Arnold and Jüngel analyze hypocoercivity and Runge–Kutta strong stability rather than this exact subflow composition. Classical sampling and observability ideas offer an alternative explanation of the undamped resonant mode and are not claimed as new. The contribution assessed here is the exact, parameter-uniform coupled phase diagram and quantitative spectral/operator-norm critical laws, not the Strang scheme or the general existence of aliasing phenomena.

## Limitations
The theorem is for the real two-dimensional linear oscillator with one rank-one dissipative axis and exact symmetric subflows. It does not prove an analogous statement for multidegree networks, high-order splittings, stiff PDE discretizations, arbitrary damping ranks, inexact exponentials or floating-point arithmetic. Related specialized formulae could exist beyond the material compared; publication priority has not been independently established. At the discriminant-zero curve, the spectral radius is an asymptotic rate and should not be misread as a finite-iterate bound without a Jordan prefactor.

## References
1. S. Blanes, F. Casas and A. Murua, *Splitting Methods for differential equations*, arXiv:2401.01722 (initial public submission 3 January 2024), *Acta Numerica* (2024), DOI 10.1017/S0962492923000077. Primary MSC2020 includes 65L05.
2. M. Mönch and N. Marheineke, *Commutator-based operator splitting for linear port-Hamiltonian systems*, arXiv:2405.17106 (initial public submission 27 May 2024).
3. F. Achleitner, A. Arnold and A. Jüngel, *Hypocoercivity for Linear ODEs and Strong Stability for Runge--Kutta Methods*, arXiv:2310.19758 (2023).
4. M. Mönch and N. Marheineke, *Fourth-order force-gradient splitting for linear port-Hamiltonian systems*, *Proceedings in Applied Mathematics and Mechanics* (first online 7 October 2024), DOI 10.1002/pamm.202400132.
