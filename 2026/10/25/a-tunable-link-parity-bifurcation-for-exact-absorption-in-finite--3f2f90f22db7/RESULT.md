# A tunable-link parity bifurcation for exact absorption in finite lossy quantum chains

## Finding

Consider an infinite incoming lead terminated by a finite, uniformly lossy tight-binding segment. A single tunable joining bond changes the number of band-center coherent-perfect-absorption (CPA) settings in a sharply parity-dependent way. The result gives the **complete classification in positive loss strength and joining-bond strength**, the unique critical coupling for an even-length termination, its large-length law, and a universal fourth-order loss-tolerance law at the critical coupling.

**Theorem.** Fix any integer \(n\ge 1\) and positive hopping, joining and loss parameters \(J,J_0,\gamma>0\). Set
\[
h=J_0/J,\qquad u=\operatorname{arsinh}(\gamma/(4J)),\]
and define, for \(u>0\),
\[
 b_n(u)=\begin{cases}
 \dfrac{\cosh(nu)}{\sinh((n+1)u)},&n\text{ odd},\\[4pt]
 \dfrac{\sinh(nu)}{\cosh((n+1)u)},&n\text{ even}.
 \end{cases}
\]
For a right-moving incident stationary wave of wave number \(k=\pi/2\) on the lossless lead, its reflection amplitude and reflected intensity are exactly
\[
 r_n=\frac{1-h^2b_n(u)}{1+h^2b_n(u)},\qquad
 R_n=|r_n|^2.
\]
The absorbed incident-flux fraction is \(1-R_n\), and is exactly one if and only if \(h^2b_n(u)=1\).

If \(n\) is odd, every \(h>0\) admits exactly one positive loss strength \(\gamma\) attaining perfect band-center absorption. If \(n\) is even, there is a unique \(u_n>0\) solving
\[
 n\coth(nu_n)=(n+1)\tanh((n+1)u_n),
\]
and the critical joining strength is
\[
 h_{\mathrm c}(n)=\left[\frac{\sinh(nu_n)}{\cosh((n+1)u_n)}\right]^{-1/2}>1.
\]
For \(0<h<h_{\mathrm c}(n)\), there is no positive loss setting with perfect band-center absorption; for \(h=h_{\mathrm c}(n)\), there is precisely one, at \(\gamma_{\mathrm c}=4J\sinh u_n\); for \(h>h_{\mathrm c}(n)\), there are precisely two distinct positive loss settings. In particular, a homogeneous joining bond \(J_0=J\) can never achieve band-center CPA with an even number of lossy sites, but a sufficiently strengthened joining bond restores CPA at two loss values.

Exactly at the even-length critical joining strength, the tuning response obeys the **universal quartic law**
\[
 R_n\bigl(h_{\mathrm c}(n),u_n+\delta\bigr)
 =\frac{(2n+1)^2}{16}\,\delta^4+O(\delta^5)
 \qquad (\delta\to0).
\]
The coordinate \(u=\operatorname{arsinh}(\gamma/(4J))\) is essential in this coefficient. Along even integers \(n\to\infty\),
\[
 h_{\mathrm c}(n)=1+\frac{\log(4n)+1}{4n}
  +O\left(\frac{(\log n)^2}{n^2}\right),\qquad
 \frac{\gamma_{\mathrm c}}J
 =\frac{2\log(4n)}n+O\left(\frac{\log n}{n^2}\right).
\]

## Assumptions and scope

The lossless lead has sites \(j\le0\), nearest-neighbor Hamiltonian hopping \(-J\), and zero on-site energies. The segment has sites \(1\le j\le n\), internal hopping \(-J\), uniform passive on-site potential \(-i\gamma/2\), no connection beyond site \(n\), and a single link \(-J_0\) joining sites \(0\) and \(1\). The single-particle time evolution is \(i\partial_t\psi=H\psi\). The loss normalization \(-i\gamma/2\) means that isolated-site probability decays at rate \(\gamma\). All conclusions concern monochromatic incidence at \(k=\pi/2\), i.e. lead energy \(E=-2J\cos k=0\); they are **not** assertions of perfect absorption of a broadband initial packet, arbitrary momentum, or of a finite-time readout. The unique scattered state exists for every strictly positive \(\gamma\), since the finite segment's shifted Hamiltonian has strictly positive imaginary part.

## Proof

**Step 1: Exact lead reflection from the finite lossy Green function.** Write \(H_n=-J A(P_n)-i\gamma I_n/2\) for the isolated segment and \(g_n(E)=\langle 1|(E-H_n)^{-1}|1\rangle\). For \(0<k<\pi\), put \(E=-2J\cos k\) and \(\psi_j=e^{ikj}+r_ne^{-ikj}\) on \(j\le0\). Eliminating the segment via its resolvent gives the exact lead equation
\[
 (E-J_0^2g_n(E))(1+r_n)=-J(e^{-ik}+r_ne^{ik}).
\]
Since \(E=-J(e^{ik}+e^{-ik})\), this yields
\[
 r_n(k)=-\frac{Je^{ik}+J_0^2g_n(E)}{Je^{-ik}+J_0^2g_n(E)}.
\]
Every positive \(\gamma\) makes this expression nonsingular for real interior-band \(k\). The outgoing incident-flux ratio is \(|r_n(k)|^2\). Conservation with absorption follows by summing the stationary discrete continuity equation over the lossy segment: the incoming minus outgoing lead flux equals \(\gamma\sum_{j=1}^n|\psi_j|^2\).

**Step 2: Explicit imaginary resolvent at the band center.** At \(E=0\), write \(y=\gamma/(2J)=2\sinh u\). Direct Schur complementation of the tridiagonal matrix \(i\gamma I_n/2+J A(P_n)\) gives
\[
 g_n(0)=-\frac{i}{J}b_n,\qquad b_0=0,\qquad b_n=\frac1{y+b_{n-1}}.
\]
With continuants \(P_0=1\), \(P_1=y\), and \(P_m=yP_{m-1}+P_{m-2}\), one has \(b_n=P_{n-1}/P_n\). Their roots are \(e^u\) and \(-e^{-u}\), so
\[
 P_m=\frac{e^{(m+1)u}-(-1)^{m+1}e^{-(m+1)u}}{2\cosh u}.
\]
Separating the parity of \(m\) proves the displayed hyperbolic formulas. At \(k=\pi/2\), substituting \(g_n(0)\) into the reflection formula proves \(r_n=(1-h^2b_n)/(1+h^2b_n)\) and the exact CPA criterion.

**Step 3: All positive solution counts.** If \(n\) is odd, \(b_n(u)=\cosh(nu)/\sinh((n+1)u)\) strictly decreases from \(+\infty\) to zero. Indeed,
\[
 \partial_u\log b_n=n\tanh(nu)-(n+1)\coth((n+1)u)<-1.
\]
Thus the equation \(b_n=h^{-2}\) has exactly one solution for each \(h>0\).

If \(n\) is even, \(b_n(u)=\sinh(nu)/\cosh((n+1)u)\) tends to zero at both ends and has logarithmic derivative
\[
 L_n'(u)=n\coth(nu)-(n+1)\tanh((n+1)u),
\]
whose derivative is strictly negative,
\[
 L_n''(u)=-n^2\operatorname{csch}^2(nu)
 -(n+1)^2\operatorname{sech}^2((n+1)u)<0.
\]
The first derivative decreases from \(+\infty\) to \(-1\), hence vanishes at precisely one positive \(u_n\). This is the strict, nondegenerate global maximum. Moreover \(b_n(u)<1\), since \(\sinh(nu)<\cosh((n+1)u)\). Intersecting its unimodal graph with the horizontal level \(h^{-2}\) yields exactly the asserted zero/one/two classification, including equality.

**Step 4: Universality of the quartic loss tolerance.** At \(u=u_n\), set \(T=n\coth(nu_n)=(n+1)\tanh((n+1)u_n)\). Hyperbolic identities imply the exact cancellation
\[
 -L_n''(u_n)
 =n^2[\coth^2(nu_n)-1]
 +(n+1)^2[1-\tanh^2((n+1)u_n)]
 =(n+1)^2-n^2=2n+1.
\]
Because \(h_{\mathrm c}^2b_n(u_n)=1\), Taylor's theorem gives
\[
 h_{\mathrm c}^2b_n(u_n+\delta)
 =1-\frac{2n+1}{2}\delta^2+O(\delta^3),
\]
so \(r_n=(2n+1)\delta^2/4+O(\delta^3)\). Squaring proves the quartic law. The coefficient is positive at every even length; no higher-order cancellation occurs.

**Step 5: Finite-length asymptotics.** For even \(n\), define \(a_n=e^{-2nu_n}\) and \(c_n=e^{-2u_n}\). The critical-point equation is exactly
\[
 1=(2n+1)a_n(1+c_n)-a_n^2c_n.
\]
It forces \(a_n=\Theta(n^{-1})\), hence \(u_n=(\log n)/(2n)+O(n^{-1})\) and \(c_n\to1\). Substituting back yields
\[
 a_n=\frac1{4n}\left[1+O\left(\frac{\log n}{n}\right)\right],\quad
 u_n=\frac{\log(4n)}{2n}+O\left(\frac{\log n}{n^2}\right).
\]
Using the exact stable form
\[
 b_n(u_n)=e^{-u_n}\frac{1-a_n}{1+a_nc_n}
 =1-\frac{\log(4n)+1}{2n}
 +O\left(\frac{(\log n)^2}{n^2}\right),
\]
and expanding \(h_{\mathrm c}=b_n(u_n)^{-1/2}\) and \(4\sinh u_n\) proves both large-length formulas.

## Verification

The accompanying `verify_bridge_absorption.py` (Python 3 with NumPy) runs **813 finite checks** and prints `PASS`. It independently assembles and solves the finite segment plus interface scattering equations rather than only replaying the continued fraction, verifies conservation of incoming flux against reflected plus absorbed flux, checks all closed-form Green-function identities through 18 segment sites, independently resolves even critical points and both strong-link CPA branches, and checks the length asymptotics at several large even sizes. The critical quartic coefficient is verified by exact derivative identities in the proof; finite Taylor samples provide optional numerical corroboration. These tests do not certify uncountably many parameters or the large-length limit, which are covered by the proof.

Representative examples: \(n=2\) gives \(h_{\mathrm c}=\sqrt2\), \(\gamma_{\mathrm c}/J=2\); \(n=4\) gives approximately \(h_{\mathrm c}=1.2462046544\), \(\gamma_{\mathrm c}/J=1.3300366\). With the homogeneous link \(h=1\), the odd-length examples \(n=1,3,5\) instead have unique perfect-absorption loss ratios approximately \(2,1.13968058,0.83256708\), respectively.

## Relationship to prior work

Mercado-Gutiérrez and collaborators (arXiv:2608.06189, first public posting August 6, 2026) use this lead/finite-loss-segment scattering framework with **three** lossy sites and a tunable interface bond. Their main results identify near-perfect absorption and study a finite-device and momentum-averaged optimization. The present result treats **all** positive absorber lengths, fixes the band-center incident energy, and classifies every positive loss-setting solution as the joining bond varies; it does not claim their Hamiltonian or scattering formalism as new.

Longhi, *Algebraic Absorption in Non-Hermitian Photonic Lattices* (Photonics 13, 574, June 11, 2026), independently gives a parity obstruction for **homogeneous joining bonds**: his equations (35)–(37) rule out band-center CPA for even-length uniformly lossy segments and give one odd-length matching equation. The present theorem explicitly acknowledges those facts as established. Its additional conclusion is that varying one interface hopping produces an **exact threshold and pair creation of band-center zeros for every even length**, together with a universal quartic tuning law and the logarithmic large-length coupling threshold. These are not consequences of the homogeneous-bond conclusion without a new transfer calculation.

Jin and Song, *Wave emission and absorption at spectral singularities* (arXiv:1611.00572), demonstrate one-port loss matching for a single terminal lossy resonator. Chong, Ge, Cao and Stone, *Coherent Perfect Absorbers: Time-reversed Lasers* (arXiv:1003.4968), establish the general real-axis scattering-zero mechanism. Neither supplies the parameter-count bifurcation for a variable joining bond and a uniform segment of arbitrary length. The terminology and single-port CPA mechanism are prior knowledge.

## Limitations

This is an exact stationary monochromatic result at one energy, not a broadband optimization. It assumes a uniform passive on-site loss along the terminating segment, no gain, nearest-neighbor real positive hoppings, a single lead and one tunable joining bond; adding disorder, different site losses, a second lead, or a real detuning is not covered. The even-length logarithmic asymptotics apply only as even \(n\to\infty\). Numerical diagnostics supplement but do not replace the analytic proof. The novelty assessment is best-knowledge, not an independent claim of global literature priority.

## References

1. E. D. Mercado-Gutiérrez et al., *Quantum transport in a non-Hermitian 1D synthetic lattice: from quantum Zeno reflection to near-perfect absorption*, arXiv:2608.06189, initially posted 2026-08-06. https://arxiv.org/abs/2608.06189
2. S. Longhi, *Algebraic Absorption in Non-Hermitian Photonic Lattices*, Photonics **13** (2026), 574, doi:10.3390/photonics13060574. https://doi.org/10.3390/photonics13060574
3. L. Jin and Z. Song, *Wave emission and absorption at spectral singularities*, arXiv:1611.00572. https://arxiv.org/abs/1611.00572
4. Y. D. Chong, L. Ge, H. Cao and A. D. Stone, *Coherent Perfect Absorbers: Time-reversed Lasers*, Phys. Rev. Lett. **105** (2010), 053901. https://arxiv.org/abs/1003.4968
