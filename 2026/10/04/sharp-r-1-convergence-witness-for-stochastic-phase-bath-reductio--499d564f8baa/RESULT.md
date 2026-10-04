# Sharp \(R^{-1}\) convergence witness for stochastic-phase bath reduction
## Finding
For the two-site, zero-hopping, one-mode Holstein pure-dephasing instance of the stochastic-phase bath reduction in arXiv:2609.28318v1, with equal site energies, initial electronic state \((|1\rangle+|2\rangle)/\sqrt2\), oscillator frequency \(\omega>0\), coupling \(g\neq0\), inverse temperature \(\beta>0\), and \(a=g^2(1-\cos(\omega t))\), the exact independent-bath coherence is \(L_\infty=e^{-2a\coth(\beta\omega/2)}\), while the phase-averaged \(R\)-bath coherence is exactly \(L_R=L_\infty I_0(2a\,\operatorname{csch}(\beta\omega/2)/R)^R\). Hence the trace-norm reduced-state error equals \(L_R-L_\infty>0\) whenever \(t\notin 2\pi\mathbb Z/\omega\), and \[\lim_{R\to\infty}R\,\|\rho_s^{(R)}(t)-\rho_s(t)\|_{\mathrm{tr}}=e^{-2a\coth(\beta\omega/2)}a^2\operatorname{csch}^2(\beta\omega/2)>0.\] Therefore the source paper's general fixed-time \(O(R^{-1})\) convergence rate is asymptotically sharp even for two sites and a single thermal mode; in this witness the finite-\(R\) method under-dephases, while the zero-temperature boundary is exact for every \(R\).

## Assumptions and scope
Consider the unitary stochastic-phase construction of Huang, Lin, and Xie for a two-site Holstein model. Set all hopping amplitudes to zero and take equal site energies, so only pure dephasing remains. Each original site has one independent bosonic mode of frequency \(\omega>0\) and dimensionless coupling \(g\neq0\). The bath is thermal at inverse temperature \(\beta>0\), and the electronic initial state is \((|1\rangle+|2\rangle)/\sqrt2\). The stochastic-phase approximation uses \(R\ge1\) shared copies of that mode with the source normalization \(g/\sqrt R\) and independent uniform phases.

Define
\[
a=g^2(1-\cos(\omega t)),\qquad c=\coth(\beta\omega/2),\qquad s=\operatorname{csch}(\beta\omega/2).
\]
The claim concerns the unitary thermal-bath realization only. It does not address the coupled-Lindblad compression error or models with hopping.

## Proof
For one oscillator let \(H(c_0)=\omega b^\dagger b+\omega(c_0 b^\dagger+c_0^*b)\). The displacement identity gives
\[
e^{-itH(c_0)}=e^{i|c_0|^2(\omega t-\sin\omega t)}D(c_0(e^{-i\omega t}-1))e^{-i\omega t b^\dagger b}.
\]
For a thermal oscillator state, \(\operatorname{Tr}(\rho_\beta D(z))=\exp[-|z|^2c/2]\).

In the exact two-bath model, the coherence \(|1\rangle\langle2|\) compares a shifted oscillator against an unshifted one in bath 1 and the reverse comparison in bath 2. Their opposite dynamical phases cancel, and the two thermal overlap factors multiply to
\[
L_\infty=e^{-2ac}.
\]

For one shared bath copy, write the site phases as \(r_j=e^{i\theta_j}\) and \(\Delta=\theta_1-\theta_2\). The two couplings have equal modulus \(g/\sqrt R\), so their individual displacement phases cancel. The remaining coherence factor from that copy is
\[
\exp\left[-\frac{2ac}{R}(1-\cos\Delta)+i\frac{2a}{R}\sin\Delta\right].
\]
Averaging the independent uniform phase difference uses
\[
\frac1{2\pi}\int_0^{2\pi}e^{A\cos\theta+iB\sin\theta}\,d\theta
=I_0(\sqrt{A^2-B^2}),
\]
with \(A=2ac/R\) and \(B=2a/R\). Since \(c^2-1=s^2\), the mean factor of one shared copy is
\[
e^{-2ac/R}I_0(2as/R).
\]
The \(R\) shared copies are independent, hence
\[
L_R=e^{-2ac}I_0(2as/R)^R=L_\infty I_0(2as/R)^R.
\]

The electronic populations remain \(1/2\). Thus the exact and phase-averaged reduced states differ only in the two off-diagonal entries, each by \((L_R-L_\infty)/2\), and their trace-norm distance is \(|L_R-L_\infty|\). For finite \(\beta\), \(s>0\); if \(a>0\), then \(I_0(2as/R)>1\), so the stochastic-phase state has strictly larger coherence and therefore under-dephases.

Finally, \(I_0(z)=1+z^2/4+O(z^4)\), so
\[
R\log I_0(2as/R)=\frac{a^2s^2}{R}+O(R^{-3}).
\]
Therefore
\[
L_R-L_\infty=\frac{e^{-2ac}a^2s^2}{R}+O(R^{-2}),
\]
which proves the stated positive limit. At zero temperature, \(s=0\), and the same exact formula gives \(L_R=L_\infty\) for every \(R\).

## Verification
The accompanying `verify.py` evaluates the closed form, checks the uniform-phase integral directly by deterministic quadrature, verifies strict under-dephasing for several finite \(R\), and numerically confirms the asymptotic coefficient. These finite computations are consistency checks; the proof is the displacement-operator calculation above.

## Relationship to prior work
Huang, Lin, and Xie prove that the phase-averaged stochastic-phase approximation reproduces the two-point bath correlation matrix for every \(R\) and that its reduced-state error is bounded by \(A_t/R\), uniformly in system size. Their End Matter derives the rate from repeated auxiliary-channel assignments in Wick pairings. The paper does not give a matching lower bound or a pure-dephasing closed form. The result here supplies an explicit thermal witness showing that the \(R^{-1}\) exponent cannot be improved in general.

General open-system error-bound papers based on differences of Gaussian bath correlation functions establish upper stability estimates for bath perturbations; they do not cover this finite-\(R\) phase average, whose averaged environment is non-Gaussian despite having the correct two-point correlations.

## Limitations
The witness has no electronic hopping and uses one thermal oscillator per site before compression. It proves sharpness of the source theorem's dependence on \(R\), not sharpness of its prefactor \(A_t\), and it does not imply that every observable or every physical parameter regime exhibits \(R^{-1}\) error. The exact cancellation at zero temperature is specific to this pure-dephasing witness and is not asserted for general stochastic-phase dynamics.

## References
1. Z. Huang, L. Lin, and P. Xie, “Scalable simulation of non-Markovian quantum transport by stochastic-phase bath reduction,” arXiv:2609.28318v1, first submitted 2026-09-23.
2. Z. Huang, Y. Zhu, G. Park, and L. Lin, “Unified analysis of non-Markovian open quantum systems in Gaussian environment using superoperator formalism,” arXiv:2411.08741.
3. K. Liu and J. Lu, “Error Bounds for Open Quantum Systems with Harmonic Bosonic Bath,” Quantum 9, 1896 (2025), doi:10.22331/q-2025-10-28-1896.
