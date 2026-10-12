# Arithmetic loss-pattern classification and survival plateaux in odd dissipative SSH chains

## Finding

Fix an integer \(M\geq 1\). Consider an open Su–Schrieffer–Heeger (SSH) chain of \(2M+1\) one-particle sites, with alternating hopping strengths \(a,b>0\). Choose a nonempty set \(S\subseteq\{1,\ldots,M\}\) of lossy even sites \(2k\), with arbitrary local loss rates \(\gamma_k>0\) for \(k\in S\). Define the arithmetic invariant
\[
 g=\gcd\bigl(M+1,\{k:k\in S\}\bigr).
\]
The exact number of one-particle modes unaffected by the losses is
\[
 \boxed{\dim\mathcal D=2g-1.}
\]
The modes have the simple real energies \(0\) and
\[
 \boxed{E_j^{\pm}=\pm\sqrt{a^2+b^2+2ab\cos(\pi j/g)},\qquad 1\leq j<g.}
\]
In particular, the protected zero-energy boundary mode is the *only* loss-free energy eigenmode exactly when \(g=1\). Every pattern with \(g>1\) additionally retains \(g-1\) nonzero-frequency pairs, so that boundary-state selection by dissipation need not be unique and coherent oscillations can survive.

For an initial excitation localized at even site \(2\ell\), \(1\leq\ell\leq M\), let \(P_{\mathrm{surv}}(t)\) be the probability that the excitation has not been lost by time \(t\). Its exact long-time limit is
\[
 \boxed{\lim_{t\to\infty}P_{\mathrm{surv}}(t)=
 \begin{cases}
 0,&g\mid\ell,\\[2pt]
 \dfrac{g}{M+1},&g\nmid\ell.
 \end{cases}}
\]
Both the number of dark modes and these survival plateaux are independent of the positive hopping strengths and positive loss rates. The long-time *density matrix* itself need not converge when \(g>1\); the displayed limit concerns the total one-particle survival probability.

## Assumptions and scope

Use the orthonormal one-excitation basis \(\{|j\rangle:1\leq j\leq 2M+1\}\). The Hermitian Hamiltonian is
\[
 H=\sum_{u=1}^{M}\bigl(a|2u-1\rangle\langle 2u|+b|2u\rangle\langle 2u+1|+\mathrm{h.c.}\bigr).
\]
The no-jump single-particle amplitude \(\psi(t)\) obeys
\[
 \psi(t)=e^{tG}\psi(0),\qquad
 G=-iH-\tfrac12\Gamma,\qquad
 \Gamma=\sum_{k\in S}\gamma_k|2k\rangle\langle2k|.
\]
This is the one-particle restriction of the zero-temperature particle-loss Lindblad equation with jumps \(\sqrt{\gamma_k}\,|\mathrm{vac}\rangle\langle2k|\). For a unit one-particle initial state, the total excitation-survival probability is \(P_{\mathrm{surv}}(t)=\|\psi(t)\|^2\). Define \(\mathcal D\) as the span of energy eigenvectors \(H\phi=E\phi\) satisfying \(\Gamma\phi=0\). Only the stated finite, nonempty loss patterns and strictly positive \(a,b,\gamma_k\) are asserted; adding gain, dephasing, coherent disorder, many-particle interactions, or loss on odd sites is outside the theorem.

## Proof

**1. Clean spectral resolution.** Order sites by sublattice, with \(M+1\) odd-site coordinates (A) and \(M\) even-site coordinates (B). Then
\[
 H=\begin{pmatrix}0&T^\dagger\\T&0\end{pmatrix},\qquad
 T_{u,u}=a,\quad T_{u,u+1}=b,\qquad 1\leq u\leq M,
\]
with all other entries of \(T\) zero. Consequently \(TT^\dagger\) is an \(M\times M\) Jacobi matrix with diagonal \(a^2+b^2\) and off-diagonal \(ab>0\). For every \(1\leq r\leq M\), its normalized eigenvector and eigenvalue are
\[
 v_r(k)=\sqrt{\frac{2}{M+1}}\sin\!\left(\frac{\pi rk}{M+1}\right),\qquad
 \lambda_r=a^2+b^2+2ab\cos\!\left(\frac{\pi r}{M+1}\right)>0.
\]
The \(\lambda_r\) are pairwise distinct. The two normalized \(H\)-eigenvectors with energies \(\pm\sqrt{\lambda_r}\) have B-sublattice components \(\pm v_r/\sqrt2\), and therefore each has B-site weight \(|v_r(k)|^2/2\). A further normalized zero eigenvector, unique because \(T\) has rank \(M\), has zero B components and A-site amplitudes proportional to \(( -a/b)^{u-1}\), \(1\leq u\leq M+1\).

**2. Exact dark-mode count.** A nonzero-energy clean eigenvector vanishes at the lossy site \(2k\) exactly when
\[
 \sin\!\left(\frac{\pi rk}{M+1}\right)=0
 \quad\Longleftrightarrow\quad (M+1)\mid rk.
\]
It vanishes at *every* site in \(S\) if and only if \(r\) is divisible by \((M+1)/g\). One direct proof is to set \(N=M+1\) and use Bézout's identity for \(g=\gcd(N,k_1,\ldots,k_t)\): the congruences \(rk_i\equiv0\pmod N\) imply \(rg\equiv0\pmod N\), equivalent to \(N/g\mid r\); the converse is immediate because \(g\mid k_i\). There are exactly \(g-1\) such integers \(r\) in \(\{1,\ldots,M\}\), namely \(r=(N/g)j\), \(1\leq j<g\). Their energy pairs and the unique zero mode give the announced dimension and energy list.

**3. No hidden undamped non-Hermitian modes.** For every eigenpair \(G\phi=z\phi\), taking the real part of its inner product yields the exact dissipativity identity
\[
 \operatorname{Re}z=-\frac{\langle\phi,\Gamma\phi\rangle}{2\|\phi\|^2}\leq0.
\]
Equality holds exactly when \(\Gamma\phi=0\), because every \(\gamma_k>0\); then \(H\phi\) is an energy eigenvector. Conversely all vectors in the listed energy eigenbasis are undamped \(G\)-eigenvectors. The dark subspace reduces both the self-adjoint \(H\) and \(\Gamma\), hence also \(G\): the orthogonal complement has no eigenvalues with zero real part. Because it is finite dimensional, its semigroup tends to zero, including when defective Jordan blocks occur. Thus
\[
 \lim_{t\to\infty}\|e^{tG}\psi\|^2=\|P_{\mathcal D}\psi\|^2
\]
for every one-particle initial state \(\psi\), with \(P_{\mathcal D}\) the orthogonal projector onto \(\mathcal D\).

**4. Exact localized-source plateau.** A source on B site \(2\ell\) is orthogonal to the zero boundary mode. The two normalized \(\pm\sqrt{\lambda_r}\) eigenvectors together contribute \(|v_r(\ell)|^2\) to its squared dark-projection norm. Substituting \(r=(N/g)j\) gives
\[
 \big\|P_{\mathcal D}|2\ell\rangle\big\|^2
 =\frac{2}{N}\sum_{j=1}^{g-1}\sin^2\!\left(\frac{\pi j\ell}{g}\right).
\]
If \(g\mid\ell\), each summand vanishes. Otherwise \(\sum_{j=1}^{g-1}\cos(2\pi j\ell/g)=-1\) by the nontrivial \(g\)-th roots-of-unity sum, so the sine-square sum is \(g/2\). This proves the two survival values and completes the proof.

## Verification

The standalone file `artifacts/verify.py` recomputes the clean eigenvectors and eigenvalues, tests the arithmetic dark-mode count and survival projectors, checks the undamped spectrum of the non-Hermitian generator with nonuniform positive loss rates, and checks long-time matrix exponentials. It uses Python 3, NumPy, and SciPy. Executing `python artifacts/verify.py` returns `VERIFY_OK 2343 clean-spectrum, dark-space, survival, and non-Hermitian checks`. These finite numerical tests are reproducibility checks only; the proof above covers every allowed \(M\), loss set, and positive continuous parameter.

For example, on \(11\) sites (\(M=5\)), loss only at B position \(k=2\) gives \(g=\gcd(6,2)=2\). There are exactly three dark modes, with energies \(0\) and \(\pm\sqrt{a^2+b^2}\). Sources at \(k=1,3,5\) have survival plateau \(1/3\), whereas those at \(k=2,4\) have zero plateau. A loss at \(k=1\) instead gives \(g=1\), with only the zero boundary mode surviving.

## Relationship to prior work

Wang and Zhang [1] establish an exact single-loss non-Hermitian reduction for an even-length SSH chain with an odd-sublattice impurity, together with a general clean-eigenvector nodal criterion and dissipative-rate asymptotics. The nodal criterion itself is not asserted here as new. Yang, Molignini, and Bergholtz [2] establish boundary-state preparation for odd SSH chains, studying a loss at the first B site and uniform B-sublattice loss, including the protected zero-energy boundary state. Their more general discussion observes that B-sublattice loss preserves that boundary state but does not give the arithmetic classification of additional nonzero-energy modes for arbitrary sparse B-site patterns. Thiel and collaborators [3] provide a broader spectral framework for dark states in detection problems but not the exact continuous-loss SSH multi-trap dimension and initial-site survival plateaux of this result. The contribution here is the all-pattern gcd count, its complete clean-energy list, and the rate-independent residue-class survival law; it is not a claim to have discovered the general dark-state mechanism.

## Limitations

The theorem is strictly a finite-size, one-excitation, ideal Markovian particle-loss result with homogeneous alternating nonzero hoppings and loss only on selected even sites. It does not imply protection under generic hopping disorder, boundary detuning, dephasing, gain, interactions, or imperfectly placed loss. It is not a lower bound for the relaxation *rate*: every complement mode can decay arbitrarily slowly as the rates or couplings vary. The total survival probability converges, but the surviving excited dark sectors can rotate forever, so pointwise occupations and coherences need not converge. An exact or implication-equivalent formulation hidden in differently indexed dark-state spectral literature remains a residual originality risk.

## References

[1] Y. T. Wang and X. Z. Zhang, “From local weight selection to Zeno slowdown in an open Su-Schrieffer-Heeger chain with a single local loss,” arXiv:2607.10218v1 (first public July 11, 2026); *Physical Review A* **114**, 012457 (2026), doi:10.1103/99h3-p7rj.

[2] F. Yang, P. Molignini, and E. J. Bergholtz, “Dissipative boundary state preparation,” arXiv:2305.00031, *Physical Review Research* **5**, 043229 (2023), doi:10.1103/PhysRevResearch.5.043229.

[3] F. Thiel and collaborators, “Dark states of quantum search cause imperfect detection,” *Physical Review Research* **2**, 043107 (2020), doi:10.1103/PhysRevResearch.2.043107.
