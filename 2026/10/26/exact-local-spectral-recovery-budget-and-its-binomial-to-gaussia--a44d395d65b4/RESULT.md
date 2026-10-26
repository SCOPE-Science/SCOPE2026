# Exact local spectral-recovery budget and its binomial-to-Gaussian crossover for damped qubits

## Finding
For the homogeneous amplitude-damping and dephasing Lindblad family below, the smallest **generic local-identifiability budget** for the two unknown positive rates from the sorted real nonzero Liouvillian spectrum has an exact closed form for every number \(n\ge1\) of qubits. Put \(r=\gamma_\phi/\gamma_1\) and \(q=\tfrac12+2r\). Outside the finitely many tie lines \(q\in\{1,\ldots,n\}\), the minimal prefix length is
\[
 k_{\mathrm{loc}}(n,r)=
 \begin{cases}
 2n+1,&0<r<\tfrac14,\\
 1+\displaystyle\sum_{j=1}^{n}\binom nj\mathbf 1_{\{j<q\}},&r>\tfrac14.
 \end{cases}
\]
Here *local identifiability* means that the mapping from the two rates to the first \(k\) ordered real decay eigenvalues is injective on some neighborhood of the given pair; the least such \(k\) is reported. Eigenvalues are counted with algebraic multiplicity, the unique zero steady mode is removed, and the remaining eigenvalues are sorted by decreasing real part. The imaginary spectral coordinates and mode labels are not supplied. For the non-tie parameters above the least locally identifying prefix is also exactly the least prefix whose local Jacobian has rank two.

For the physically motivated fixed rate rectangle \(0.005\le\gamma_1,\gamma_\phi\le0.05\), the **sharp maximum** of this local budget over non-tie parameters, for every \(n\ge3\), is
\[
 K_n=1+\sum_{j=1}^{\min\{n,20\}}\binom nj
 =\begin{cases}2^n,&3\le n\le20,\\
 1+\sum_{j=1}^{20}\binom nj,&n\ge21.
 \end{cases}
\]
It is attained at \(\gamma_1=0.005\), \(\gamma_\phi=0.05\). In particular, although the maximal budget equals \(2^n\) through \(n=20\), it grows only as \(K_n\sim n^{20}/20!\) when \(n\to\infty\) on this fixed rectangle. No claim is made here that a linear regression trained across parameter values attains this local exact bound.

A separate sharp **moving-ratio crossover** holds. If \(r_n>1/4\), every \(q_n=\tfrac12+2r_n\) avoids the tie integers, and
\[
 r_n=\frac{n-1}{4}+\frac{z\sqrt n}{4}+o(\sqrt n),
\]
then for every fixed real \(z\),
\[
 \frac{k_{\mathrm{loc}}(n,r_n)}{2^n}\longrightarrow
 \Phi(z)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{z}e^{-t^2/2}\,dt.
\]
The crossover is from a vanishing to a full fraction of the \(2^n\) population-scale budget when the dephasing-to-damping ratio passes \(n/4\). This is a spectral-prefix statement, not a dynamical relaxation-time theorem.

## Assumptions and scope
Let \(n\ge1\) and let each site have computational states \(|0\rangle\) (unexcited) and \(|1\rangle\) (excited). On \((\mathbb C^2)^{\otimes n}\) consider
\[
 H=\frac\omega2\sum_{\ell=1}^n\sigma_\ell^z
   +J\sum_{1\le\ell<m\le n}\sigma_\ell^z\sigma_m^z,
\]
with arbitrary fixed real \(\omega,J\), and the trace-preserving Lindblad generator
\[
 \mathcal L(\rho)=-i[H,\rho]
 +\sum_{\ell=1}^n\gamma_1\mathcal D[\sigma_\ell^-](\rho)
 +\sum_{\ell=1}^n\gamma_\phi\mathcal D[\sigma_\ell^z](\rho),
 \qquad
 \mathcal D[A](\rho)=A\rho A^\dagger-\frac12\{A^\dagger A,\rho\},
\]
where both \(\gamma_1>0\) and \(\gamma_\phi>0\), and \(\sigma^-|1\rangle=|0\rangle\). Reversing the common convention for the computational basis merely relabels bitstrings and does not change the eigenvalue multiset. The parameter-identification problem knows \(n\) and the model class but not the two rates; it observes only real parts, sorted with multiplicities, not the physical eigenmode labels. It is local and exact, with no measurement noise.

## Proof
**1. Actual Liouvillian spectrum.** Label computational states by bitstrings \(u,v\in\{0,1\}^n\), let \(|u|\) denote Hamming weight and \(d(u,v)\) their Hamming distance, and let \(E_u\) be the real diagonal energy of \(|u\rangle\). In the matrix-unit basis \(|u\rangle\langle v|\), the jump term \(\sigma^-_\ell\rho\sigma^+_\ell\) strictly reduces \(|u|+|v|\) by two whenever nonzero. Therefore the full superoperator is triangular after ordering by total excitation content. Its complete spectrum, with algebraic multiplicity, is
\[
 \lambda_{uv}=-i(E_u-E_v)-\frac{\gamma_1}{2}(|u|+|v|)-2\gamma_\phi d(u,v).
 \tag{1}
\]
For \(u=v=0\), this gives the unique zero eigenvalue. For every other pair the real part is strictly negative. Thus there is one and only one steady spectral mode to remove. Notice that \(\omega,J\) affect only imaginary parts and cannot alter the real-part ordering.

**2. The first coherence and population layers.** Write the nonnegative decay as \(d_{uv}=-\operatorname{Re}\lambda_{uv}\). Population pairs \(u=v\) with \(|u|=j\ge1\) have exactly \(\binom nj\) modes at decay \(j\gamma_1\), independently of \(\gamma_\phi\). Among off-diagonal pairs, \(d(u,v)\ge1\) and \(|u|+|v|\ge d(u,v)\), so
\[
 d_{uv}\ge d(u,v)(\gamma_1/2+2\gamma_\phi).
\]
Equality at the minimum \(\alpha=\gamma_1/2+2\gamma_\phi\) occurs precisely for the \(2n\) ordered vacuum--one-excitation pairs. Any other coherence has strictly larger decay. The first dephasing-sensitive spectral coordinate consequently follows exactly those population modes with \(j\gamma_1<\alpha\), provided \(\alpha/\gamma_1=q\) is not an integer in \(\{1,\dots,n\}\). This gives its exact index
\[
 K_{\mathrm{coh}}=1+\sum_{j=1}^{n}\binom nj\mathbf1_{\{j<q\}}.
 \tag{2}
\]
If \(q>1\), the first nonsteady eigenvalue is a population at decay \(\gamma_1\). Every prefix shorter than (2) is locally independent of \(\gamma_\phi\), hence not locally injective in both rates. The prefix of length (2) contains both the population decay \(\gamma_1\) and the first-coherence decay \(\alpha\); its two rate gradients \((1,0)\) and \((1/2,2)\) have determinant \(2\). Thus that length is both necessary and sufficient for local identifiability.

If \(q<1\), the first \(2n\) modes are all vacuum--one-excitation coherences, every one with decay \(\alpha\). The next mode is a population with decay \(\gamma_1\): other coherences have decay at least \(\min\{2\alpha,\alpha+\gamma_1\}>\gamma_1\), since \(\alpha>\gamma_1/2\). Hence the first \(2n\) coordinates depend on only the single linear combination \(\alpha\), but the \((2n+1)\)-st recovers the independent rate \(\gamma_1\). This proves both branches of the claimed minimal generic budget. The excluded equality lines admit coincident populations and coherences, for which a tie-ordering convention and one-sided analysis would be necessary; none is asserted.

**3. The exact fixed-rectangle maximum.** On \([0.005,0.05]^2\), the ratio satisfies \(1/10\le r\le10\) and so \(7/10\le q\le41/2\). For \(r>1/4\), formula (2) increases monotonically as \(q\) crosses successive positive integers and its maximum occurs at \(q=41/2\), giving \(1+\sum_{j=1}^{\min(n,20)}\binom nj\). For \(r<1/4\), the budget is \(2n+1\), which does not exceed that expression for \(n\ge3\). The corner \((0.005,0.05)\) is off every tie line and attains the bound. For \(n\le20\), the binomial theorem gives exactly \(2^n\); for \(n\ge21\), the upper summation limit remains 20 and the leading term of the resulting degree-20 polynomial is \(n^{20}/20!\). The first strict reduction below \(2^n\) occurs at \(n=21\), where the budget is \(2^{21}-1\).

**4. Gaussian onset fraction.** In the moving-ratio window, \(q_n=n/2+z\sqrt n/2+o(\sqrt n)\). Formula (2), divided by \(2^n\), is the binomial probability
\[
 2^{-n}\sum_{1\le j<q_n}\binom nj
 =\Pr\{1\le B_n<q_n\},\qquad B_n\sim\operatorname{Bin}(n,1/2),
\]
up to the negligible \(2^{-n}\) term from the initial \(+1\) in (2). The classical de Moivre--Laplace central limit theorem, with variance \(n/4\), gives \(\Phi(z)\), regardless of rounding as long as the tie planes are avoided. For \(r_n/n\to c\ne1/4\), standard binomial tail concentration gives a limiting fraction 0 when \(c<1/4\) and 1 when \(c>1/4\). This completes the proof.

## Verification
A standalone `verify.py` independently enumerates all bitstring-pair decay slopes using exact rational arithmetic for 69 non-tie pairs with \(1\le n\le8\), checks that the analytic threshold is the first prefix with a rank-two rate Jacobian, checks 67 exact fixed-rectangle maxima for \(3\le n\le69\), and compares direct Lindblad superoperator eigenvalues with (1) for \(n=1,2,3\) to numerical precision. The latter comparison assembles the Hamiltonian, dephasing and jump matrices rather than assuming the spectral formula as input. It also prints finite-size diagnostics of the Gaussian window. The infinite-size claims follow from the analytic counting and central-limit proof, not from those finite checks. Run with `python verify.py` (NumPy optional for the direct superoperator checks; standard-library rational checks always run).

## Relationship to prior work
Ji and Chakraborty, *A Spectral Identifiability Threshold for Dissipative Rate Recovery from Truncated Liouvillian Spectra*, arXiv:2608.29302v1 (29 August 2026), derive (1), exhibit the population-blind and coherence-bearing sectors, derive the extreme requirements \(k\ge2n+1\) and \(k\ge2^n\) in the relevant parameter regimes, and measure estimator performance for \(n=3,4,5,6\). Those spectral formulas, sector observations, and extreme threshold mechanisms are **not** claimed as new. The present result supplies the complete *pointwise, generic, locally sufficient and necessary* prefix classification, the sharp rate-rectangle cutoff at \(n=21\), and the binomial/Gaussian scaling law not stated in their paper. It does not replace their global regression experiments. Torres, *Closed form solution of Lindblad master equations without gain*, arXiv:1403.3686v2 (2014), provides a general solution framework for loss and dephasing with no gain; the spectral-solvability mechanism itself is likewise known. The ranked identification problem and its combinatorial cutoff are distinct from the eigensystem reconstruction studied there.

## Limitations
The result applies only to this diagonal-Hamiltonian, locally and homogeneously damped/dephased \(n\)-qubit family, with positive rates and mode multiplicities retained. It is **local** identifiability, not global uniqueness across arbitrary disconnected parameter cells, not statistical estimability under noisy, finite-shot spectra, and not a theorem about the accuracy of a shared trained regressor. Equality lines \(q\in\{1,\dots,n\}\) are omitted because real-part sorting has ties of distinct physical type. Additional Hamiltonian terms not diagonal in the computational basis can change the spectrum. General spectral results may provide a different route to the same counting formulas; no literature-wide originality certification is claimed.

## References
1. Y. Ji and S. Chakraborty, *A Spectral Identifiability Threshold for Dissipative Rate Recovery from Truncated Liouvillian Spectra*, arXiv:2608.29302v1, first publicly submitted 29 August 2026. https://arxiv.org/abs/2608.29302
2. J. M. Torres, *Closed form solution of Lindblad master equations without gain*, Physical Review A 89, 052133 (2014), arXiv:1403.3686v2. https://arxiv.org/abs/1403.3686
