# Sharp cubic purity leakage and phase tracking for two-phonon dressed dark qubits

## Finding
Consider a bosonic oscillator with number operator \(n=b^\dagger b\), \(\omega,\gamma>0\), fixed squeezing \(r>0\), and a real \(C^3\) jump phase \(\phi(t)\) near \(t=0\). For the time-local equation
\[
\dot\rho=-i\omega[n,\rho]+\gamma\bigl(L(t)\rho L(t)^\dagger-\tfrac12\{L(t)^\dagger L(t),\rho\}\bigr),\qquad L(t)=\cosh r\,b^2-e^{i\phi(t)}\sinh r\,b^{\dagger 2},
\]
write \(z=\tanh^2r\), \(\lambda=e^{i\phi(0)}\tanh r\), and \(\Omega=\phi'(0)+4\omega\). Define
\[
F_+(z)={}_2F_1(1/4,1/2;3/4;z),\quad F_-(z)={}_2F_1(1/2,3/4;5/4;z),
\]
and normalized dark states
\[
|D_+\rangle=F_+(z)^{-1/2}\sum_{j=0}^\infty\lambda^j\sqrt{\frac{(1/4)_j(1/2)_j}{(3/4)_j j!}}\,|4j\rangle,
\]
\[
|D_-\rangle=F_-(z)^{-1/2}\sum_{j=0}^\infty\lambda^j\sqrt{\frac{(1/2)_j(3/4)_j}{(5/4)_j j!}}\,|4j+1\rangle.
\]
These dark states are the dressed pair identified in Buza–Toroš (2026). The new assertion is the **exact first nonzero loss-of-purity coefficient** for every encoded initial pure state \(|\psi\rangle=\alpha|D_+\rangle+\beta|D_-\rangle\), \(|\alpha|^2+|\beta|^2=1\):
\[
\boxed{1-\operatorname{Tr}\rho(t)^2=\frac{2\gamma\Omega^2}{3(1-z)}\bigl(|\alpha|^2B_+(z)+|\beta|^2B_-(z)\bigr)t^3+o(t^3),}
\]
where primes denote derivatives with respect to \(z\) and
\[
B_+(z)=\frac{16z^2F_+''(z)+12zF_+'(z)}{F_+(z)},\qquad B_-(z)=\frac{16z^2F_-''(z)+20zF_-'(z)}{F_-(z)}.
\]
For every finite \(r>0\) these coefficients are strictly positive. Thus an initially dark encoded pure state loses purity at cubic, not linear or quadratic, order whenever \(\Omega\ne0\), regardless of its logical Bloch state.

The same calculation identifies the exact phase-matching condition. If \(\phi(t)=\phi(0)-4\omega t\) for all \(t\) on an interval, the entire two-dimensional dressed dark sector is transported by the free oscillator unitary without dissipation; conversely, this freely transported sector is pointwise in the kernel of \(L(t)\) only if \(e^{i(\phi(t)+4\omega t)}=e^{i\phi(0)}\). More generally the cubic coefficient vanishes exactly when \(\phi'(0)=-4\omega\), without claiming absence of higher-order loss for other phase profiles.

In the sequential strong-squeezing limit (first the \(t\downarrow0\) coefficient at fixed \(r\), then \(r\to\infty\)), the leading coefficient becomes independent of \(\alpha,\beta\):
\[
B_\pm(z)\sim\frac{16}{(1-z)^2\log(1/(1-z))},\qquad
\frac{2\gamma\Omega^2B_\pm(z)}{3(1-z)}\sim\frac{\gamma\Omega^2}{12r}e^{6r}.
\]

## Assumptions and scope
The result is about the stated single-mode time-local GKSL model (including a deliberately time-dependent phase), not a new microscopic derivation of a gravitational environment. The Fock operators obey \([b,b^\dagger]=1\); \(r,\omega,\gamma\) are fixed positive real constants. The initial density is a rank-one projector onto an arbitrary normalized vector in the source's two-dimensional dressed dark space. The phase is real \(C^3\) near zero; no small-squeezing assumption is imposed. The initial states have exponential Fock tails at each finite \(r\), giving all polynomial number moments needed for the Taylor argument. For a global statement about phase tracking, use any conservative well-posed solution of the stated master equation; the displayed unitary trajectory directly solves it on the indicated interval.

## Proof
**1. Kernel and moment functions.** From \((b^2-\lambda b^{\dagger2})|D\rangle=0\), coefficient matching yields \(c_2=c_3=0\) and
\[
c_{k+4}=\lambda\sqrt{\frac{(k+1)(k+2)}{(k+3)(k+4)}}c_k,\qquad k\ge0.
\]
This decouples the two possible seeds at occupations \(0\) and \(1\) and gives precisely the two hypergeometric series above. Because \(|\lambda|<1\), they converge with all finite number moments. Their supports lie in distinct residue classes modulo four and are orthogonal. The source's dark-sector construction supplies the motivation; the recurrence here fixes the normalization used for the new coefficient. For any encoded vector \(\psi\), \(b^2\psi\) has support only in residues \(2,3\pmod4\) and is therefore orthogonal to \(\psi\). Directly differentiating the positive series yields
\[
\|b^2\psi\|^2=|\alpha|^2B_+(z)+|\beta|^2B_-(z),
\]
since the factors \((4j)(4j-1)\) and \((4j+1)(4j)\) equal \(16j(j-1)+12j\) and \(16j(j-1)+20j\), respectively. The \(j=1\) terms prove strict positivity for \(z>0\).

**2. Cubic purity lemma.** Let \(P=|\psi\rangle\langle\psi|\) and let a differentiable GKSL trajectory start at \(P\) with \(L(0)\psi=0\). Put \(U(t)=e^{-iHt}\), \(\widetilde L(t)=U(t)^\dagger L(t)U(t)\), and \(v=\widetilde L'(0)\psi\). The no-jump branch is pure; its leading one-jump complement, to order \(t^3\), is
\[
\gamma\int_0^t s^2\,|Qv\rangle\langle Qv|\,ds
=\frac{\gamma t^3}{3}|Qv\rangle\langle Qv|,\quad Q=I-P.
\]
Indeed \(\widetilde L(s)\psi=s v+O(s^2)\), no-jump deviations first affect this amplitude at order \(s^2\), and two-jump contributions are higher order. Consequently the purity of the mixture satisfies
\[
1-\operatorname{Tr}\rho(t)^2=\frac{2\gamma}{3}\|Qv\|^2t^3+o(t^3).
\]
Equivalently, differentiating the GKSL equation three times gives \((\operatorname{Tr}\rho^2)'(0)=(\operatorname{Tr}\rho^2)''(0)=0\) and \((\operatorname{Tr}\rho^2)'''(0)=-4\gamma\|Qv\|^2\). This identity is algebraic in finite dimension and applies here by approximating on finite Fock sections while controlling the requisite polynomial moments using the exponential initial tails. The expansion is at each fixed finite squeezing parameter; no uniform-in-squeezing Taylor remainder is asserted.

**3. Rotating-frame derivative.** For \(H=\omega n\), canonical commutation gives
\[
\widetilde L(t)=e^{-2i\omega t}\cosh r\bigl[b^2-e^{i(\phi(t)+4\omega t)}\tanh r\,b^{\dagger2}\bigr].
\]
Since \(b^2\psi=e^{i\phi(0)}\tanh r\,b^{\dagger2}\psi\), differentiating at zero gives \(v=-i\Omega\cosh r\,b^2\psi\). Section 1 gives \(Qv=v\), so inserting its norm into Section 2 yields the boxed cubic law. If \(\phi(t)+4\omega t\) is constant modulo \(2\pi\), then \(\widetilde L(t)\psi=0\) for every dark \(\psi\), proving the asserted exact unitary preservation. Conversely, because \(r>0\) and \(b^{\dagger2}D_+\ne0\), pointwise annihilation of the freely transported dark sector forces the same phase equality.

**4. Strong-squeezing coefficient.** Both hypergeometric functions are zero-balanced: their upper parameters sum to the lower parameter. Their positive series, or the zero-balanced continuation formula, gives
\[
F_\pm(z)=c_\pm\log\frac{1}{1-z}+O(1),\quad F_\pm'(z)\sim\frac{c_\pm}{1-z},\quad F_\pm''(z)\sim\frac{c_\pm}{(1-z)^2},
\]
where \(c_\pm>0\). The \(F''\) terms therefore dominate both \(B_\pm\), with the same leading asymptotic. Finally \(1-z=\operatorname{sech}^2r\sim4e^{-2r}\), giving the stated \(e^{6r}/r\) coefficient.

## Verification
The self-contained program `verify_phase_leakage.py` (Python; dependencies NumPy and mpmath) constructs finite Fock sections directly, checks both kernel recurrences, computes the third purity derivative by differentiating finite-dimensional GKSL superoperators, and independently matches the analytic coefficient. It checks exact chirp tracking in finite sections and tests both hypergeometric-moment formulas plus their strong-squeezing asymptotics. Running it from this package reported **418 successful finite and special-function assertions**. A finite section and a set of numerical tests cannot prove the infinite-dimensional claim; the proof above supplies its recurrence, purity expansion and limit arguments.

## Relationship to prior work
Buza and Toroš (arXiv:2608.07257v1, §5 and Supplemental F3) derive the squeezed two-phonon jump, the same two dark states and the crucial qualitative caveat that the free oscillator Hamiltonian fails to preserve the dressed dark sector unless the squeezed correlations have a phase reference. Those statements are prior art, not the claimed advance. The finding here evaluates the precise leading cubic purity leakage for arbitrary encoded superpositions and phase velocities, identifies its explicit hypergeometric number moments, and proves its divergent universal strong-squeezing asymptotic. General treatments of Lindbladian decoherence-free subspaces and time-dependent subspace tracking (Albert et al.; Wu et al.) establish broader geometry and control principles; they do not provide the evaluated explicit model-specific coefficient in the material inspected. The exact phase-chirp identity is included to interpret the coefficient, not claimed as a general new decoherence-free control principle.

## Limitations
The coefficient is local at time zero and requires \(r>0\) fixed during the short-time expansion. The large-squeezing limit is taken **after** extracting the coefficient, not jointly with \(t\to0\). At exact first-order phase matching, higher-order phase mismatch can still cause purity loss unless the full phase profile tracks exactly. The model assumes an ideal time-dependent squeezed-jump phase; experimental ability to control gravitational bath squeezing or its phase is not established. No long-time mixing or measured graviton-decoherence rate is inferred. The source's two dark states and general qualitative phase-reference warning are established prior results. General quantum-trajectory theory may offer an alternate derivation of the cubic lemma; novelty is restricted to the full explicit specialization, logical-state dependence and squeezing asymptotic.

## References
1. G. K. Buza and M. Toroš, *The small effect of graviton-induced decoherence*, arXiv:2608.07257v1 (first public 2026-08-07), §5 and Supplemental F3, https://arxiv.org/html/2608.07257v1 .
2. V. V. Albert, B. Bradlyn, M. Fraas and L. Jiang, *Geometry and Response of Lindbladians*, Physical Review X **6**, 041031 (2016), https://doi.org/10.1103/PhysRevX.6.041031 .
3. S. L. Wu et al., *Adiabatic Decoherence-Free Subspaces and its Shortcuts*, arXiv:1705.01695, https://arxiv.org/abs/1705.01695 .
4. S. L. Wu et al., *Engineering of Quantum State by Time-Dependent Decoherence-Free Subspaces*, arXiv:1502.07967, https://arxiv.org/abs/1502.07967 .
