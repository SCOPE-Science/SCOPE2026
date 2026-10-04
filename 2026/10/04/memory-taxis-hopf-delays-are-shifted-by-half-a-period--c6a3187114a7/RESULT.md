# Memory-taxis Hopf delays are shifted by half a period
## Finding
For the memory-based prey-taxis predator–prey system of Liu and Tan, the delayed taxis term has the opposite modal sign from the one printed in their characteristic equation. For every nonzero Neumann eigenmode \(k\), let \(-\Delta\phi_k=\mu_k\phi_k\) with \(\mu_k>0\). The source gives \(a_{12}<0\), taxis sensitivity \(\chi>0\), and coexistence predator density \(v_*>0\). Define
\[
S_k=-a_{12}\chi v_*\mu_k>0.
\]
Then the characteristic equation implied by the source linearization is
\[
\lambda^2+P_k\lambda+Q_k+S_k e^{-\lambda\tau}=0.
\]
The source instead prints the delayed coefficient as \(R_k=a_{12}\chi v_*\mu_k=-S_k<0\) in Eqs. (4.5)–(4.6).

The squared frequency equation is unaffected because it contains only \(S_k^2\). The phase condition is not. If \(P_k>0\) and \(\omega_k>0\) is a candidate Hopf frequency, the correct delay sequence is
\[
\tau_{k,j}=\frac{2j\pi+\arccos((\omega_k^2-Q_k)/S_k)}{\omega_k},\qquad j=0,1,2,\ldots.
\]
The source's printed Eq. (4.18) is exactly \(\pi/\omega_k\) larger on the corresponding branch. Hence the printed analytical Hopf-delay locations, the minimum threshold assembled from them in Eq. (4.21), and calculations anchored to those printed locations are shifted by half a period.

## Assumptions and scope
The statement concerns a positive spatially homogeneous coexistence equilibrium of source system (1.1), a nonzero Neumann mode \(k\) with \(\mu_k>0\), and the source signs \(a_{12}<0\), \(\chi>0\), and \(v_*>0\). The explicit delay formula additionally uses the source's trace assumption \(P_k>0\) and a positive candidate frequency \(\omega_k\) satisfying the squared frequency equation. No assertion is made for the zero mode, where the taxis coefficient vanishes.

The finding is a local spectral correction. It does not claim that a particular numerical simulation in the article is false, does not rederive the nonlinear Hopf normal form, and does not classify global dynamics.

## Proof
The source expands the taxis term as
\[
-\chi\nabla\!\cdot\!\bigl(v\nabla u(t-\tau)\bigr)
=-\chi v_*\Delta \widetilde u(t-\tau)+\text{quadratic terms},
\]
and therefore writes the linearized taxis matrix with lower-left entry \(-\chi v_*\). On a Neumann eigenfunction satisfying \(\Delta\phi_k=-\mu_k\phi_k\), this linear term becomes
\[
-\chi v_*\Delta\bigl(\widetilde u_k(t-\tau)\phi_k\bigr)
=+\chi v_*\mu_k\widetilde u_k(t-\tau)\phi_k.
\]
Thus the modal linear system has the form
\[
\dot u_k=(a_{11}-d_1\mu_k)u_k+a_{12}v_k,
\]
\[
\dot v_k=\bigl(a_{21}+\chi v_*\mu_k\mathcal D_\tau\bigr)u_k+(a_{22}-d_2\mu_k)v_k,
\]
where \(\mathcal D_\tau u_k(t)=u_k(t-\tau)\). Substituting \(e^{\lambda t}\) and taking the determinant gives
\[
(\lambda+d_1\mu_k-a_{11})(\lambda+d_2\mu_k-a_{22})
-a_{12}\bigl(a_{21}+\chi v_*\mu_k e^{-\lambda\tau}\bigr)=0.
\]
With the source definitions of \(P_k\) and \(Q_k\), this is
\[
\lambda^2+P_k\lambda+Q_k-a_{12}\chi v_*\mu_k e^{-\lambda\tau}=0,
\]
so the delayed coefficient is \(S_k=-a_{12}\chi v_*\mu_k>0\). This also agrees with the source's zero-delay determinant Eq. (4.9), which adds \(\chi|a_{12}|v_*\mu_k\).

Set \(\lambda=i\omega\). The correct real and imaginary equations are
\[
\omega^2-Q_k=S_k\cos(\omega\tau),\qquad P_k\omega=S_k\sin(\omega\tau).
\]
Squaring and adding yields the same quartic frequency equation as in the source because \(S_k^2=R_k^2\). Since \(P_k>0\), \(S_k>0\), and \(\omega>0\), the sine is positive, so the relevant phase lies in \((2j\pi,(2j+1)\pi)\). Therefore
\[
\tau_{k,j}=\frac{2j\pi+\arccos((\omega_k^2-Q_k)/S_k)}{\omega_k}.
\]
The source uses \(R_k=-S_k\) and the branch
\[
\tau^{\mathrm{print}}_{k,j}=\frac{2(j+1)\pi-\arccos((\omega_k^2-Q_k)/R_k)}{\omega_k}.
\]
Using \(\arccos(-c)=\pi-\arccos(c)\) gives
\[
\tau^{\mathrm{print}}_{k,j}=\tau_{k,j}+\frac{\pi}{\omega_k},
\]
which is the claimed half-period shift.

## Verification
The accompanying `verify.py` reconstructs the modal determinant with exact rational coefficients and confirms that its delayed coefficient is \(-a_{12}\chi v_*\mu_k\), while the printed coefficient has the opposite sign. It also evaluates a generic admissible phase relation and checks numerically that the corrected delay has zero characteristic residual while the printed branch differs by \(\pi/\omega\).

As an independent algebraic cross-check, Song, Peng, and Zhang's 2021 memory-diffusion derivation uses the same lower-left memory matrix and obtains a determinant term with \(-d_{21}v_*a_{12}e^{-\lambda\tau}\mu_k\), matching the sign above.

## Relationship to prior work
Liu and Tan explicitly derive the linear taxis term \(-\chi v_*\Delta\widetilde u(t-\tau)\) and the negative lower-left taxis matrix, but Eqs. (4.5)–(4.6) then assign the opposite sign to the scalar delayed coefficient. Their next subsection, Eq. (4.9), returns to the determinant with the correct positive contribution at zero delay. The present finding isolates this internal sign inconsistency and propagates it through the Hopf phase condition.

Song, Peng, and Zhang (2021), cited by Liu and Tan for memory-delay Hopf analysis, contains the generic determinant sign consistent with the corrected formula. That earlier work does not identify the Liu–Tan source-specific sign inconsistency or state the exact half-period correction to Liu and Tan's Eq. (4.18).

Searches of the exact title, DOI, sign aliases, Hopf-delay aliases, and correction/erratum terms did not locate a published correction or a published-finding corpus finding covering this source-specific statement. A prior finding in the same local ledger concerns a different coexistence-existence shortcut in Liu and Tan's Theorem 3.1 and neither implies nor is implied by this spectral correction.

## Limitations
The frequency polynomial is unchanged because the sign disappears after squaring, so this result does not reject the candidate frequencies themselves. It corrects the phase and therefore the analytical delay locations. The nonlinear simulations, reported stability map, and normal-form coefficients were not independently rerun here; any conclusion depending on a printed critical delay must be rechecked at the corrected location rather than being declared false automatically.

No claim is made that this source-specific correction is a new general theory of memory diffusion; the generic modal determinant structure already appears in prior literature.

## References
1. Dazhuo Liu and Xuewen Tan, *Memory-based prey-taxis and environmental stress shape spatiotemporal predator-prey dynamics*, AIMS Mathematics 11(6), 17880–17916 (2026), DOI 10.3934/math.2026729.
2. Yongli Song, Yahong Peng, and Tonghua Zhang, *The spatially inhomogeneous Hopf bifurcation induced by memory delay in a memory-based diffusion system*, Journal of Differential Equations 300, 597–624 (2021), DOI 10.1016/j.jde.2021.08.010; arXiv:2104.00330.
