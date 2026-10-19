# Exact thermal entanglement-memory frontier in a center-damped three-spin XX chain

## Finding

Consider the three-qubit nearest-neighbor XX chain with a positive-rate local lowering and raising channel at its middle site. For **every** initial density operator, the long-time state exists and retains exactly one parameter of the initial condition: its weight in the antisymmetric end-spin sector. The stationary state and the end-spin concurrence are explicit.

Let \(q=\gamma_+/\gamma_->0\), \(Z=1+q+q^2\), and \(w=\operatorname{tr}(P_-\rho(0))\), where \(P_-\) projects the two end spins onto their singlet. With the notation defined below, the full three-spin limit is

\[
\rho_\infty = \left[w|S\rangle\langle S|+(1-w)\frac{|00\rangle\langle00|+q|T\rangle\langle T|+q^2|11\rangle\langle11|}{Z}\right]_{13}\otimes\tau_2(q).
\]

Its end-spin Wootters concurrence is

\[
\boxed{C_\infty(w,q)=\max\left\{0,w-\frac{3(1-w)q}{1+q+q^2}\right\}}.
\]

In particular, the *complete sharp survival boundary* for end-spin entanglement is

\[
\boxed{C_\infty>0\quad\Longleftrightarrow\quad w>\frac{3q}{1+4q+q^2}}.
\]

For the fully separable initial state \(|100\rangle\), the antisymmetric weight is \(w=1/2\), and

\[
\boxed{C_\infty=\frac{(1-q)^2}{2(1+q+q^2)}}.
\]

Thus for a positive-temperature local thermal ratio \(q=e^{-\beta\omega}\in(0,1)\), positive asymptotic end-spin entanglement is created from a product state, even though both local upward and downward jumps are present. At \(q=1\) this particular initial state instead yields zero concurrence. For small \(\beta\omega>0\), the concurrence is asymptotic to \((\beta\omega)^2/6\).

## Assumptions and scope

All Hilbert spaces are complex, with basis \(|0\rangle,|1\rangle\). Number, raising, and lowering operators on site \(j\in\{1,2,3\}\) are \(n_j=|1\rangle_j\langle1|\), \(s_j^+=|1\rangle_j\langle0|\), and \(s_j^-=|0\rangle_j\langle1|\). Fix \(J\in\mathbb R\setminus\{0\}\), \(\omega\in\mathbb R\), and \(\gamma_-,\gamma_+>0\). The dynamics is the finite-dimensional GKSL semigroup \(\exp(t\mathcal L)\) with

\[
H=\omega\sum_{j=1}^3n_j+J\sum_{j=1}^2(s_j^+s_{j+1}^-+s_j^-s_{j+1}^+),\qquad
\mathcal L(\rho)=-i[H,\rho]+\gamma_-\mathcal D[s_2^-](\rho)+\gamma_+\mathcal D[s_2^+](\rho),
\]

where \(\mathcal D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2\). The real frequency and coupling may have either sign; the two jump rates are strictly positive. The theorem does **not** include the singular zero-pumping point \(\gamma_+=0\).

On end sites \(1,3\), write \(|S\rangle=(|10\rangle-|01\rangle)/\sqrt2\), \(|T\rangle=(|10\rangle+|01\rangle)/\sqrt2\), and \(\tau_2(q)=(|0\rangle\langle0|+q|1\rangle\langle1|)/(1+q)\) on the middle qubit. The tensor product labelled \((13)\otimes2\) means the natural embedding into sites \(1,2,3\) obtained by permuting factors, not a reordering of the physical sites. Let \(F\) interchange the two end spins, \(P_-= (I-F)/2\), and \(P_+=(I+F)/2\), with identity on site \(2\). The singlet-weight \(w\) is a number in \([0,1]\).

## Proof

**1. Two explicit stationary sectors.** Let \(N=\sum_j n_j\). Since \([H,N]=0\), the strictly positive matrix \(\rho_*=q^N/(1+q)^3\) commutes with \(H\). Its middle-site factor is \(\tau_2(q)\), which obeys \(\gamma_-\mathcal D[s^-](\tau_2)+\gamma_+\mathcal D[s^+](\tau_2)=0\), so \(\mathcal L(\rho_*)=0\). The end-spin swap commutes with \(H\), the two middle jump operators, and \(q^N\). Consequently,

\[
\rho_{\pm}=\frac{P_{\pm}q^NP_{\pm}}{\operatorname{tr}(P_{\pm}q^N)}
\]

are stationary states with \(\operatorname{tr}(P_\pm\rho_\pm)=1\). The end-spin antisymmetric sector has basis \(|S\rangle\) and the symmetric sector has basis \(|00\rangle,|T\rangle,|11\rangle\). Tracing \(\rho_\pm\) over the center immediately yields the two states displayed in the finding.

**2. Exhaustion of the stationary and peripheral observables.** Suppose the adjoint generator has an eigenoperator \(X\ne0\) with \(\mathcal L^*(X)=i\nu X\), \(\nu\in\mathbb R\). The Lindblad carré-du-champ identity reads

\[
\mathcal L^*(X^\dagger X)-\mathcal L^*(X^\dagger)X-X^\dagger\mathcal L^*(X)
=\sum_{\eta\in\{-,+\}}\gamma_\eta[s_2^\eta,X]^\dagger[s_2^\eta,X].
\]

The trace of its left side against faithful \(\rho_*\) vanishes: the first term by stationarity and the remaining terms because the imaginary eigenvalues cancel. Both coefficients on the right are strictly positive. Faithfulness implies \([s_2^-,X]=[s_2^+,X]=0\). Since these two matrices generate the entire middle-site matrix algebra, \(X=Y_{13}\otimes I_2\).

Now the adjoint eigen-equation reduces to \(i[H,X]=i\nu X\). Define the collective end-spin ladder operators \(S^\pm=s_1^\pm+s_3^\pm\). The Hamiltonian hopping terms containing the middle site are \(J(S^+s_2^-+S^-s_2^+)\). Comparing coefficients of the linearly independent middle-site matrices \(s_2^+\), \(s_2^-\), and \(I_2\) in the commutator forces \([Y,S^+]=[Y,S^-]=0\), because \(J\ne0\). The end-spin Hilbert space is the direct sum of one spin-zero singlet and one irreducible spin-one triplet under these collective operators. By the elementary commutant theorem for inequivalent irreducible summands, \(Y\) is a scalar on each summand; hence \(X\in\operatorname{span}\{P_-,P_+\}\). Both projectors commute with \(H\), so \(\nu=0\).

Thus the adjoint generator has no nonzero purely imaginary eigenvalues, and its zero eigenspace is exactly \(\operatorname{span}\{P_-,P_+\}\). In finite dimensions a trace-preserving completely positive semigroup is uniformly bounded in trace norm on Hermitian matrices (and hence in a fixed operator norm on the whole matrix space). Therefore it admits no Jordan blocks on the imaginary axis. Every remaining generator eigenvalue has strictly negative real part; accordingly \(\lim_{t\to\infty}e^{t\mathcal L}\rho(0)\) exists for every initial density matrix. Duality fixes the sector weights \(w=\operatorname{tr}(P_-\rho(0))\) and \(1-w\). Together with the stationary \(\rho_\pm\), this uniquely yields \(\rho_\infty=w\rho_-+(1-w)\rho_+\).

**3. Exact concurrence and threshold.** Set \(b=(1-w)q/Z\). In the ordered end-spin computational basis \((|00\rangle,|01\rangle,|10\rangle,|11\rangle)\), the reduced limit has diagonal entries \(((1-w)/Z,(b+w)/2,(b+w)/2,(1-w)q^2/Z)\). Its only off-diagonal entry is \(\rho_{01,10}= (b-w)/2\) and its conjugate. The standard two-qubit \(X\)-state concurrence formula gives

\[
C_\infty=2\max\left\{0,\left|\frac{b-w}{2}\right|-\sqrt{\frac{1-w}{Z}\frac{(1-w)q^2}{Z}}\right\}
=\max\{0,|w-b|-2b\}=\max\{0,w-3b\}.
\]

The last equality follows by considering \(w\ge b\) and \(w<b\) separately, noting that the latter branch cannot be positive. Rearrangement gives the strict boundary \(w>3q/(1+4q+q^2)\). The basis state \(|100\rangle\) has end overlap \(|\langle S|10\rangle|^2=1/2\), so substitution gives \((1-q)^2/[2(1+q+q^2)]\). Taylor expansion at \(q=e^{-\beta\omega}\to1\) yields the stated quadratic high-temperature behavior. All formulas hold at positive \(q\), including \(q=1\).

## Verification

The attached standalone `check.py` requires NumPy and SciPy and is executable as `python check.py`. It constructs the full \(64\times64\) superoperator with column-major vectorization, compares its two-dimensional peripheral kernel against the predicted stationary sectors, verifies direct stationarity for several positive rate ratios, checks the predicted concurrence across twenty-one initial singlet weights at each ratio, and tests long-time propagation for a separable localized excitation. It reports 306 passing numerical assertions. These finite-dimensional checks independently test normalizations, matrix order and coefficient factors; they do not replace the analytical spectral-exhaustion argument for every positive parameter.

## Relationship to prior work

Çakmak, Sümer, Campbell and Karpat, *Synchronization in a dissipative quantum many-body system* (arXiv:2604.18707, first public 20 April 2026), derive dark-mode and edge-concurrence results for loss-only XX chains. Their discussion of finite-temperature raising jumps correctly states that the noiseless-vector subspace disappears. The present theorem does not contradict that statement: it concerns two mixed stationary sectors protected by **end-swap strong symmetry**, not a Hilbert-space decoherence-free vector subspace. It additionally determines the complete finite-positive-rate stationary limit and its sharp end-concurrence threshold, which is not stated there.

Buča and Prosen (arXiv:1203.0943) establish the general strong-symmetry mechanism for multiple stationary states. That general structural principle, the collective singlet/triplet decomposition and Wootters' concurrence formula are not claimed as original. Huang, Guo and Yi (arXiv:0908.0592) analyze three-spin XX nonequilibrium entanglement with baths coupled at chain ends using a different dissipative model. Their stationary-state formulas do not imply this center-only local-jump singlet-weight law by an identified reduction. The novelty claim is specifically the exact **positive-thermal-pumping, center-only, arbitrary-initial-state entanglement-memory frontier** and the product-state generation formula.

## Limitations

This result is for precisely three spins, mirror-symmetric nonzero hopping and a local middle-spin raising/lowering GKSL generator. It assumes strictly positive rates and does not include the zero-pumping boundary; the limits of state manifolds need not commute with that singular limit. It does not claim an exact global Gibbs thermalization model, robustness to unequal end couplings, collective noise, general chains, or a finite-time entanglement-formation bound. A strong-symmetry fixed-point theorem may provide a broader formal route to the stationary classification; the novelty is restricted to the explicit spin model, convergence and concurrence frontier.

## References

- B. Çakmak, K. Sümer, S. Campbell and G. Karpat, *Synchronization in a dissipative quantum many-body system*, arXiv:2604.18707, version 1 posted 20 April 2026; version 2 full text https://arxiv.org/html/2604.18707v2.
- B. Buča and T. Prosen, *A note on symmetry reductions of the Lindblad equation: transport in constrained open spin chains*, arXiv:1203.0943, https://arxiv.org/html/1203.0943v3.
- X. L. Huang, J. L. Guo and X. X. Yi, *Nonequilibrium thermal entanglement in three-qubit XX model*, arXiv:0908.0592, https://arxiv.org/abs/0908.0592.
- W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, Phys. Rev. Lett. 80 (1998), 2245–2248; https://doi.org/10.1103/PhysRevLett.80.2245.
