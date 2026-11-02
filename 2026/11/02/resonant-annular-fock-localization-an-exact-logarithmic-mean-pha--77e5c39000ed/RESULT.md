# Resonant annular Fock localization: an exact logarithmic-mean phase boundary and angular cusp

## Finding
In the Gaussian analytic Bargmann–Fock space, the highest eigenvalue of annular localization is simple except on an explicitly parametrized countable collection of curves. On such curves it has multiplicity two, and a fixed-area angular corrugation of the outer boundary produces a sharp first-order cusp controlled **only** by the first angular Fourier coefficient.

Let \(0<s<t\), \(A_{s,t}=\{z\in\mathbb C:s<|z|^2<t\}\), and \(\Lambda(s,t)\) denote the norm of Toeplitz localization by \(\mathbf1_{A_{s,t}}\). Put
\[
L(s,t)=\frac{t-s}{\log(t/s)}.
\]
If \(L(s,t)\notin\mathbb N\), the largest eigenvalue is simple and occurs at monomial degree \(\lfloor L(s,t)\rfloor\). If \(L(s,t)=m\in\mathbb N\), the largest eigenvalue occurs **exactly twice**, at degrees \(m-1\) and \(m\). For any \(m\ge1\), these resonances form the unique smooth curve \(t=t_m(s)>s\) with \(0<s<m\).

For real \(h\in C^2(\mathbb T)\) of angular mean zero, define the exactly area-preserving annular deformation
\[
A_\varepsilon=\left\{re^{i\theta}:s<r^2<t+\varepsilon h(\theta)\right\},\qquad
\widehat h_k=\frac1{2\pi}\int_0^{2\pi}h(\theta)e^{-ik\theta}\,d\theta.
\]
For sufficiently small real \(\varepsilon\), at every resonance \(L(s,t)=m\) the **optimized** localization norm satisfies
\[
\boxed{\ \|T_{A_\varepsilon}\|=\Lambda(s,t)+\gamma_m(t)|\widehat h_1|\,|\varepsilon|+O_{s,t,h}(\varepsilon^2),\quad
\gamma_m(t)=\frac{e^{-t}t^{m-1/2}}{\sqrt{(m-1)!m!}}.\ }
\]
Off the resonance curves, \(\|T_{A_\varepsilon}\|=\Lambda(s,t)+O_{s,t,h}(\varepsilon^2)\). Thus a zero-mean shape path has a nonzero first-order cusp **if and only if** the unperturbed top eigenvalue is double and \(\widehat h_1\ne0\). In particular, at a resonance \(h(\theta)=\cos\theta\) raises the optimal concentration to first order for both signs of the deformation, with coefficient \(\gamma_m(t)/2\).

## Assumptions and scope
The Hilbert space consists of entire functions square integrable under \(\pi^{-1}e^{-|z|^2}dA(z)\), with orthonormal basis \(e_n(z)=z^n/\sqrt{n!}\). For a bounded measurable region \(E\), \(T_E=P\mathbf1_E|_{\mathcal F^2}\) is the positive compact Toeplitz localization operator. All statements hold for every real \(s,t\) with \(0<s<t\), every fixed real \(C^2\) mean-zero angular profile, and sufficiently small positive or negative \(\varepsilon\). The error term is for fixed parameters and profile; no uniform assertion is made along a varying resonance curve or for rough profiles.

## Proof
1. **Complete radial spectrum.** Rotational symmetry diagonalizes \(T_{A_{s,t}}\) in the displayed monomial basis. Its eigenvalues, with multiplicity, are
\[
\lambda_n(s,t)=\frac1{n!}\int_s^t e^{-u}u^n\,du
=e^{-s}\sum_{j=0}^n\frac{s^j}{j!}-e^{-t}\sum_{j=0}^n\frac{t^j}{j!},\quad n\ge0.
\]
All eigenvalues are positive, tend to zero, and their adjacent difference has the exact sign formula
\[
\lambda_{n+1}-\lambda_n=\frac{e^{-s}s^{n+1}-e^{-t}t^{n+1}}{(n+1)!},\qquad
\operatorname{sgn}(\lambda_{n+1}-\lambda_n)=\operatorname{sgn}(L(s,t)-n-1).
\]
Consequently the spectral sequence grows strictly until the index specified in the finding and decreases strictly afterward, with exactly one adjacent tie when \(L\) is an integer. Nonadjacent ties below the top do not affect this classification. For fixed \(s>0\), the logarithmic mean is continuous and strictly increasing in \(t>s\), with limits \(s\) and \(+\infty\) as \(t\downarrow s\) and \(t\to\infty\). This gives one resonant \(t_m(s)\) precisely for \(0<s<m\).

2. **Trace-norm differentiability under shape deformation.** The coherent-state integral representation
\[
T_E=\int_E |k_z\rangle\langle k_z|\,\frac{dA(z)}\pi,
\qquad k_z(w)=e^{w\overline z-|z|^2/2}
\]
shows that \(\varepsilon\mapsto T_{A_\varepsilon}\) is twice continuously differentiable in trace norm: in the squared radial variable \(u\), the integrand and its derivatives are smooth bounded trace-class-valued maps on a fixed compact strip surrounding \(u=t\). In particular, differentiating the exact monomial matrix integral is justified. With the matrix convention \(\langle T e_k,e_j\rangle\),
\[
\langle T'_{A_\varepsilon}|_{\varepsilon=0} e_k,e_j\rangle
=\frac{e^{-t}t^{(j+k)/2}}{\sqrt{j!k!}}\,\widehat h_{k-j}.
\]
The exact Euclidean area is \(\pi(t-s)+\pi\varepsilon\widehat h_0=\pi(t-s)\).

3. **Top eigenvalue perturbation.** Outside resonance the isolated top eigenspace is one-dimensional. Its derivative is the diagonal first variation, zero because \(\widehat h_0=0\), giving the quadratic remainder. At \(L(s,t)=m\), the isolated two-dimensional top eigenspace is \(\operatorname{span}\{e_{m-1},e_m\}\). The compression of the first variation to this eigenspace is
\[
\begin{pmatrix}
0&\gamma_m(t)\widehat h_1\\
\gamma_m(t)\overline{\widehat h_1}&0
\end{pmatrix},
\qquad
\gamma_m(t)=e^{-t}t^{m-1/2}/\sqrt{(m-1)!m!}.
\]
Its eigenvalues are \(\pm\gamma_m(t)|\widehat h_1|\). By standard perturbation of an isolated finite-multiplicity selfadjoint spectral cluster, the two eigenvalue branches have the expansions \(\Lambda(s,t)\pm\varepsilon\gamma_m(t)|\widehat h_1|+O(\varepsilon^2)\). For positive and negative \(\varepsilon\) the larger branch switches, yielding the asserted \(|\varepsilon|\)-cusp. If \(\widehat h_1=0\), both first-order branch derivatives vanish and the norm differs only by \(O(\varepsilon^2)\).

## Verification
The standalone checker `CHECK.py` evaluates the resonance equation, the radial eigenvalue sequence, and the top eigenvalue of finite angularly perturbed localization matrices. It compares the observed one-sided slopes at four distinct resonances with \(\gamma_m(t)/2\) for \(h(\theta)=\cos\theta\). The finite-matrix experiments corroborate, rather than establish, the exact infinite-dimensional expansion. The analytic proof uses the explicit spectral gap and trace-norm perturbation of the coherent-state integral, and does not rely on a truncation threshold.

## Relationship to prior work
The spectral integral for radial masks is a classical consequence of Daubechies' time-frequency localization theorem. Svela's 2024 work extends the corresponding diagonalization to Reinhardt masks and other windows; in particular, annuli belong to its radial-mask class. Gómez, Guerra, Ramos and Tilli establish a sharp Faber–Krahn stability theorem for Gaussian STFT concentration about a disk. The current statement does **not** claim radial diagonalization or general operator perturbation theory as new: its distinct content is the complete logarithmic-mean resonance classification and the exact first-harmonic cusp coefficient for area-preserving *nonradial* annular deformations. The primary source's radial-mask hypothesis does not cover these deformations. Generic perturbation theory provides the splitting mechanism but does not by itself supply the resonance loci or their explicit compressed boundary matrices.

## Limitations
The local expansion is limited to a fixed annulus and bounded smooth angular perturbations of its **outer** boundary; the case of simultaneous inner/outer corrugation would require an additional term. This is a local spectral-sensitivity statement, not a global optimality assertion about annuli. No independent mathematical validation has been performed. Earlier specialized treatments of nonradial perturbations of resonant Gaussian localization operators could affect historical priority.

## References
- E. A. T. Svela, *Extensions of Daubechies' theorem: Reinhardt domains, Hagedorn wavepackets and mixed-state localization operators*, 2024, arXiv:2410.18769 (first public 2024-10-24), particularly Proposition 5.5 and Section 5.2.
- J. Gómez, A. Guerra, J. P. G. Ramos, P. Tilli, *Stability of the Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2307.09304 (first public 2023-07-18); *Inventiones Mathematicae* 236 (2024), Section 5.
- A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031 (first public 2021-02-03).
- I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Trans. Inf. Theory 34 (1988), 605–612.
