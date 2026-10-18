# Arithmetic parity protection and quartic relaxation in a telegraph-flux quantum ring

## Finding

**Theorem.** Let \(N\ge3\) be an integer, \(h\in\mathbb R\setminus\{0\}\), \(0<\theta<\pi\), and \(\lambda>0\). On \(\mathbb C^N\), let \(S|x\rangle=|x+1\pmod N\rangle\) and drive the nearest-neighbor ring with a stationary symmetric random telegraph process \(X_t\in\{+1,-1\}\), switching at rate \(\lambda\) in each direction, through
\[
H_{X_t}=h(e^{iX_t\theta}S+e^{-iX_t\theta}S^*).
\]
Start the walker in \(|0\rangle\), independently of the noise, and write \(p_x(t)=\mathbb E[|\langle x|U_X(t)|0\rangle|^2]\). Then:

1. For every **odd** \(N\), every position probability tends to \(1/N\). In particular, with
\[
 b_N=4|h\sin\theta|\sin\frac{\pi}{2N}\sin\frac{\pi}{N},\qquad
 \Delta_N=\lambda-\operatorname{Re}\sqrt{\lambda^2-b_N^2},
\]
using the principal square root, the *exact* return-probability logarithmic relaxation exponent is
\[
\limsup_{t\to\infty}\frac1t\log|p_0(t)-1/N|=-\Delta_N.
\]
Here \(\log0=-\infty\). At fixed \((h,\theta,\lambda)\) and odd \(N\to\infty\),
\[
\Delta_N\sim\frac{2\pi^4h^2\sin^2\theta}{\lambda N^4}.
\]
2. For every **even** \(N\), if \(\cos\theta\ne0\), the return probability does **not** converge: its asymptotic form contains a nonzero undamped Fourier component of frequency \(4h\cos\theta\). Nevertheless, every site probability has uniform *time Cesàro average* \(1/N\).
3. For every **even** \(N\) at the special phase \(\theta=\pi/2\), the pointwise site probabilities **do** converge but to the nonuniform law
\[
 p_x(\infty)=\frac1N-\frac{f_N}{N^2}+\frac{(-1)^x}{N}\mathbf1_{\{0,N/2\}}(x),
 \qquad f_N=\begin{cases}2,&4\mid N,\\0,&N\equiv2\pmod4.\end{cases}
\]
This specializes to zero antipodal probability when \(N\equiv2\pmod4\), and to an antipodal excess when \(4\mid N\).

This is one uniform finite-ring classification, including its odd-ring exact relaxation rate and its even-ring arithmetic boundary cases.

## Assumptions and scope

The site labels are \(x\in\mathbb Z/N\mathbb Z\); \(N\ge3\), so the two directed shifts describe the usual distinct edges of the cycle. The telegraph process is symmetric, **stationary at time zero**, continuous-time with mean holding time \(1/\lambda\), and globally shared by all bonds; the Peierls phase is \(+\theta\) or \(-\theta\) on **every** directed hopping bond simultaneously. This is **not** independent bond phase noise, position-projector dephasing, nor a discrete-time coined walk. The state in each noise realization evolves unitarily with the indicated piecewise-constant Hamiltonian. The field is neither measured nor conditioned on at readout. \(\theta=0\) and \(\theta=\pi\), when the environment does not modulate the Hamiltonian, are excluded. The conclusions about pointwise convergence concern site probabilities, not convergence of the full density matrix. Every \(p_x(t)\) is nonnegative and \(\sum_xp_x(t)=1\) by unitarity.

## Proof

**Step 1: exact telegraph coefficient.** Write \(a_k=2\pi k/N\) and take \(|k\rangle=N^{-1/2}\sum_xe^{ia_kx}|x\rangle\), so \(S|k\rangle=e^{-ia_k}|k\rangle\). All noise Hamiltonians commute and share this Fourier basis, with
\[
E_k(\sigma)=2h\cos\theta\cos a_k+2h\sigma\sin\theta\sin a_k.
\]
For ordered indices \(k,l\), set
\[
 A_{kl}=2h\cos\theta(\cos a_k-\cos a_l),\quad
 B_{kl}=2h\sin\theta(\sin a_k-\sin a_l).
\]
Since the initial momentum density matrix has every entry \(1/N\), Fourier inversion gives the **exact**, all-time formula
\[
 p_x(t)=\frac1{N^2}\sum_{k,l=0}^{N-1}e^{i(a_k-a_l)x-iA_{kl}t}\,q_{B_{kl}}(t), \tag{1}
\]
where \(q_b(t)=\mathbb E\exp(-ib\int_0^tX_s\,ds)\). Stationarity and the symmetric two-state generator yield the scalar initial-value problem \(q_b''+2\lambda q_b'+b^2q_b=0\), \(q_b(0)=1\), \(q_b'(0)=0\); hence
\[
 q_b(t)=e^{-\lambda t}\left(\cosh(t\mu_b)+\lambda\frac{\sinh(t\mu_b)}{\mu_b}\right),
 \quad\mu_b=\sqrt{\lambda^2-b^2}, \tag{2}
\]
with continuous value \(e^{-\lambda t}(1+\lambda t)\) at \(\mu_b=0\). For \(b\ne0\), \(q_b(t)\to0\) exponentially, possibly with a linear prefactor at the critically damped value; for \(b=0\), \(q_b(t)=1\). All \(k=l\) terms of (1) total \(1/N\).

**Step 2: arithmetic of the protected modes.** For \(k\ne l\), the equation \(B_{kl}=0\) says \(\sin a_k=\sin a_l\), equivalently \(a_k+a_l\equiv\pi\pmod{2\pi}\), or \(2(k+l)\equiv N\pmod{2N}\). No distinct solutions exist when \(N\) is odd. For even \(N\), put \(K=N/2\); the protected off-diagonal indices are precisely \(l\equiv K-k\pmod N\) with \(l\ne k\). Thus all off-diagonal contributions decay for odd \(N\), proving uniform position convergence. For even \(N\), the protected part of (1) is
\[
 F_x(t)=\frac1{N^2}\sum_{\substack{k\ne l\\k+l\equiv K\ (\mathrm{mod}\,N)}}
 e^{i(a_k-a_l)x-iA_{kl}t}.
 \tag{3}
\]
The difference \(p_x(t)-1/N-F_x(t)\) decays exponentially for every fixed even \(N\).

**Step 3: even-ring alternatives.** When \(\cos\theta\ne0\), a protected pair has \(A_{k,K-k}=4h\cos\theta\cos a_k\). The unordered pair \(\{0,K\}\) produces an undamped term \(2N^{-2}\cos(4h\cos\theta\,t)\) in \(F_0(t)\). No other protected pair has the same nonzero absolute frequency, because \(|\cos a_k|<1\) for \(k\notin\{0,K\}\). Therefore \(F_0\) is a nonconstant finite trigonometric polynomial and cannot converge. All protected *off-diagonal* pairs have nonzero \(A_{kl}\) when \(\cos\theta\ne0\): \(A_{kl}=0\) would require \(\cos a_k=0\), which forces \(k=l\) in the protected relation. Their Cesàro averages vanish, proving Cesàro uniformity.

At \(\theta=\pi/2\), all \(A_{kl}=0\). The full protected ordered-pair sum including its fixed points is
\[
 \sum_{k=0}^{N-1}e^{i(a_k-a_{K-k})x}=(-1)^x\sum_{k=0}^{N-1}e^{4\pi ikx/N}
 =N(-1)^x\mathbf1_{\{0,N/2\}}(x).
\]
The involution \(k\mapsto K-k\pmod N\) has \(f_N=2\) fixed points if \(4\mid N\), and none if \(N\equiv2\pmod4\). Removing those fixed points and dividing by \(N^2\) proves the displayed limiting law.

**Step 4: sharp odd-ring rate.** For odd \(N\), factorization gives
\[
 |\sin a_k-\sin a_l|=2\left|\sin\frac{\pi(k-l)}N\right|\left|\cos\frac{\pi(k+l)}N\right|.
\]
For distinct indices the first factor has minimum \(\sin(\pi/N)\). Because \(N\) is odd, the second has minimum \(\sin(\pi/(2N))\). Both lower bounds are simultaneously attained by adjacent sites in momentum space nearest to the maximum or minimum of the sampled sine dispersion: one of the adjacent integer pairs straddling \(N/4\) or \(3N/4\) gives the required compatible parities. Thus
\[
\min_{k\ne l}|B_{kl}|=4|h\sin\theta|\sin\frac\pi{2N}\sin\frac\pi N=b_N.\tag{4}
\]
By (2), a nonzero frequency difference \(b\) has exponential decay exponent \(\Gamma(b)=\lambda-\operatorname{Re}\sqrt{\lambda^2-b^2}\). This is nondecreasing in \(|b|>0\), so every summand of \(p_0(t)-1/N\) is \(O((1+t)e^{-\Delta_Nt})\).

To establish **equality** in the logarithmic exponent, not merely an upper bound: if \(b_N<\lambda\), the minimal-\(|b|\) terms have positive real leading coefficients \((1+\lambda/\sqrt{\lambda^2-b_N^2})/2\), so their coefficient of \(e^{-\Delta_Nt}\) is a nonzero finite trigonometric polynomial (its value at time zero is positive). All terms with larger \(|b|\) have strictly faster exponential decay. A nonzero finite trigonometric polynomial has positive mean-square and hence a positive limsup in absolute value. If \(b_N=\lambda\), the \(t e^{-\lambda t}\) coefficient from minimal-\(|b|\) terms is likewise a nonzero trigonometric polynomial. If \(b_N>\lambda\), all off-diagonal terms have exactly the common exponential envelope \(e^{-\lambda t}\) multiplying a nonzero finite trigonometric polynomial (evaluate its prefactor at \(t=0\), where it equals \(1-1/N\)). These three cases prove the stated limsup equality. Finally, \(b_N\sim 2\pi^2|h\sin\theta|/N^2\); for large odd \(N\), \(b_N<\lambda\) and rationalization yields \(\Delta_N=b_N^2/(\lambda+\sqrt{\lambda^2-b_N^2})\sim b_N^2/(2\lambda)\), giving the quartic law.

## Verification

The standalone script `verify_flux.py` independently constructs the doubled classical-environment Liouville generator on the site basis and compares its matrix-exponential position probabilities against (1)–(2), at multiple ring sizes, Peierls phases and times; it also checks the exact even-ring limiting law, the arithmetic minimum in (4), and the large-odd-ring quartic constant. Run `OPENBLAS_NUM_THREADS=1 python verify_flux.py` after installing the versions or compatible APIs in `requirements.txt`. The self-contained proof above, rather than finite test ranges, establishes the statements for all admissible parameters. The zero/noise-free endpoint \(\sin\theta=0\), nonstationary initial telegraph distributions, finite-sample mixing-time bounds and general graph extensions are not established.

## Relationship to prior work

Kendon and Tregenna, *Decoherence can be useful in quantum walks* (arXiv:quant-ph/0209005, first posted 2002-08-31), study **coined discrete-time** walks with coin/position noise, including cycles; their averaging method and model do not imply the continuous-time common Peierls-flux dichotomy. Solenov and Fedichkin (arXiv:quant-ph/0506096) and Fedichkin, Solenov and Tamon (arXiv:quant-ph/0509163) analyze **independently monitored sites** on continuous-time cycles, a different noise coupling. Chandrashekar, Srikanth and Banerjee (arXiv:quant-ph/0607188) study discrete-time coin symmetries and phase-flip channels on cycles. Wold et al. (arXiv:1206.2174) treat classical random telegraph dephasing of a qubit, providing the telegraph stochastic ingredient, not an arithmetic ring classification. Asapanna et al. (arXiv:2510.16204) identify bulk decoherence-free momentum subspaces in a **periodically driven discrete-step photonic lattice**, a related physical mechanism but not the present continuous-time finite-ring exact criterion or quartic rate. Standard commuting-Hamiltonian and Fourier-diagonalization methods are prior techniques and are not claimed as new. The contribution assessed here is their exact combination for globally switched Peierls phases, including the odd/even/fourfold pointwise-limit classification and the sharp \(N^{-4}\) relaxation exponent.

## Limitations

The exact relaxation exponent describes the ultimate long-time decay of the return probability for **fixed** odd \(N\); the quartic law is the subsequent \(N\to\infty\) asymptotic. It does **not** independently establish an \(N^4\) finite-accuracy total-variation mixing time at a fixed error tolerance, because prefactors and transient oscillations also matter. Noise is spatially perfectly correlated, stationary, symmetric and Markovian; independent or spatially varying bond noise can remove the protected modes. The initial walker is localized and decoupled from the initial noise, and a quantum coherent initial momentum state may behave differently. Related general spectral-dephasing principles might permit derivation of parts of the theorem; full publication-priority and independent scientific audit have not been performed.

## References

1. V. Kendon and B. Tregenna, *Decoherence can be useful in quantum walks*, arXiv:quant-ph/0209005 (2002), https://arxiv.org/abs/quant-ph/0209005.
2. D. Solenov and L. Fedichkin, *Continuous-time Quantum Walks on a Cycle Graph*, arXiv:quant-ph/0506096 (2005), https://arxiv.org/abs/quant-ph/0506096.
3. L. Fedichkin, D. Solenov and C. Tamon, *Mixing and Decoherence in Continuous-Time Quantum Walks on Cycles*, arXiv:quant-ph/0509163 (2005), https://arxiv.org/abs/quant-ph/0509163.
4. C. M. Chandrashekar, R. Srikanth and S. Banerjee, *Symmetries and noise in quantum walk*, arXiv:quant-ph/0607188 (2006), https://arxiv.org/abs/quant-ph/0607188.
5. H. J. Wold, H. Brox, Y. M. Galperin and J. Bergli, *Decoherence of a qubit due to a quantum fluctuator or to a classical telegraph noise*, arXiv:1206.2174 (2012), https://arxiv.org/abs/1206.2174.
6. R. Asapanna, C. Hainaut, A. Amo and Á. Gómez-León, *Decoherence-free subspaces in the noisy dynamics of discrete-step quantum walks in a photonic lattice*, arXiv:2510.16204 (2025), https://arxiv.org/abs/2510.16204.
