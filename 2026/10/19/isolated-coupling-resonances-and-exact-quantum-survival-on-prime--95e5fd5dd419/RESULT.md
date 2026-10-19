# Isolated coupling resonances and exact quantum survival on prime-prism ladders

## Finding

Let \(p\ge 3\) be any odd prime and let \(c_j=\cos(2\pi j/p)\), for \(0\le j\le(p-1)/2\). Define the exceptional positive coupling set
\[
\mathcal R_p(g)=\big\{|g|(c_a-c_b):0\le a<b\le(p-1)/2\big\},\qquad g\in\mathbb R\setminus\{0\}.
\]
All the members of this set are distinct, so \(|\mathcal R_p(g)|=(p^2-1)/8\). A continuous-time quantum walk on two identically coupled \(p\)-cycles joined by rungs of strength \(t>0\), starting at one endpoint of a rung and irreversibly absorbed at its other endpoint, has infinite-time survival probability
\[
S_p(g,t)=\begin{cases}
\frac{4}{3p},&t=|g|(c_0-c_b),\ 1\le b\le(p-1)/2,\\[2mm]
\frac{2}{p},&t=|g|(c_a-c_b),\ 1\le a<b\le(p-1)/2,\\[2mm]
0,&t\notin\mathcal R_p(g).
\end{cases}
\]
In particular, the unweighted prism with \(t=|g|\) has perfect absorption from the opposite end of that rung for every odd prime \(p\). The result holds at every strictly positive sink rate.

## Assumptions and scope

The Hilbert space is \(\mathbb C^p\otimes\mathbb C^2\) with basis \(|j,\ell\rangle\), \(j\in\mathbb Z/p\mathbb Z\), \(\ell\in\{0,1\}\). Let \(A_p\) denote the adjacency matrix of the undirected cycle, with \(A_p|j\rangle=|j-1\rangle+|j+1\rangle\). The Hermitian hopping Hamiltonian is
\[
H=gA_p\otimes I_2+tI_p\otimes \sigma_x,
\]
where \(g\ne0\) is real and \(t>0\). Put \(|s\rangle=|0,0\rangle\) (sink), \(|v\rangle=|0,1\rangle\) (initial state). For every \(\kappa>0\) define
\[
H_{\mathrm{eff}}=H-\frac{i\kappa}{2}|s\rangle\langle s|,
\qquad S_p(g,t)=\lim_{u\to\infty}\|e^{-iuH_{\mathrm{eff}}}|v\rangle\|^2.
\]
This no-jump norm represents remaining, unabsorbed probability. This is a statement about one excitation, homogeneous real cycle hopping, a uniform rung coupling, one localized irreversible sink, and a fixed opposite-rung initial position. No equality is claimed for general system sizes, other starts or detectors, disorder, stroboscopic detection, or finite-time absorption rates.

## Proof

**1. The sink-orthogonal spectral reduction.** For any finite-dimensional Hermitian \(H\) and one sink \(|s\rangle\), let \(P_E\) be the orthogonal projector to the eigenspace of energy \(E\). The dark subspace is
\[
\mathcal D=\bigoplus_{E\in\operatorname{spec}H}\bigl(\operatorname{ran}P_E\cap|s\rangle^\perp\bigr).
\]
It reduces \(H\), and the non-Hermitian sink term annihilates it. Its orthogonal complement also reduces \(H_{\mathrm{eff}}\). If an eigenvector \(w\) of the restriction to \(\mathcal D^\perp\) had an eigenvalue with zero imaginary part, then
\[
\operatorname{Im}\langle w,H_{\mathrm{eff}}w\rangle=-\frac\kappa2|\langle s,w\rangle|^2=0,
\]
so \(\langle s,w\rangle=0\) and \(Hw=Ew\) for real \(E\), contradicting \(w\perp\mathcal D\). Every eigenvalue of this finite restriction therefore has strictly negative imaginary part; Jordan polynomial factors cannot prevent its exponential decay. Thus \(S_p(g,t)=\|P_{\mathcal D}v\|^2\). In terms of \(w_E=P_Es\), the complementary bright projection on each eigenspace is the line through \(w_E\), when nonzero. Consequently
\[
1-S_p(g,t)=\sum_{E:w_E\ne0}\frac{|\langle s,P_Ev\rangle|^2}{\langle s,P_Es\rangle}.
\tag{1}
\]

**2. Two Fourier bands and collision formula.** Define \(f_k=p^{-1/2}\sum_{j=0}^{p-1}e^{2\pi ikj/p}|j\rangle\) and \(|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2\). The normalized eigenvectors \(f_k\otimes|\pm\rangle\) have energies
\[
E_{k,\pm}=2g\cos(2\pi k/p)\pm t.
\]
At each energy \(E\) let \(m_E^\pm\) count the momentum eigenvectors of the indicated sign having energy \(E\); these counts include both \(k\) and \(p-k\) when distinct. Because \(\langle s,f_k\otimes|\pm\rangle=1/\sqrt{2p}\) and \(\langle v,f_k\otimes|\pm\rangle=\pm1/\sqrt{2p}\),
\[
\langle s,P_Es\rangle=\frac{m_E^++m_E^-}{2p},\qquad
\langle s,P_Ev\rangle=\frac{m_E^+-m_E^-}{2p}.
\]
Substitute in (1), using \(\sum_E(m_E^++m_E^-)/(2p)=1\), to obtain the exact nonnegative overlap identity
\[
S_p(g,t)=\frac2p\sum_{E:m_E^++m_E^->0}\frac{m_E^+m_E^-}{m_E^++m_E^-}.
\tag{2}
\]
A term is positive precisely when the two parity bands share an energy. For \(t>0\) this occurs precisely when \(t=|g|(c_a-c_b)\) with \(0\le a<b\le (p-1)/2\), because the strictly decreasing cosine levels \(c_j\) describe all cycle energies, once the sign of \(g\) and the parity-band ordering are accounted for.

**3. Prime-order uniqueness of cosine gaps.** Suppose rational \(a_0,\dots,a_m\), where \(m=(p-1)/2\), obey \(a_0+\sum_{j=1}^m a_j c_j=0\). Let \(\zeta=e^{2\pi i/p}\). Multiplying by two gives a polynomial vanishing at \(\zeta\):
\[
F(X)=2a_0+\sum_{j=1}^m a_j(X^j+X^{p-j}).
\]
Since the minimal polynomial of the primitive prime-order root \(\zeta\) over \(\mathbb Q\) is \(\Phi_p(X)=1+X+\cdots+X^{p-1}\), of degree \(p-1\), the polynomial \(F\), whose degree is at most \(p-1\), is a rational scalar multiple \(q\Phi_p\). Comparing coefficients shows every rational relation on \((c_0,c_1,\ldots,c_m)\) is a multiple of \((1/2,1,\ldots,1)\). In particular, a rational relation whose coordinate sum is zero must be trivial, because \(1/2+m=p/2\ne0\).

If \(c_a-c_b=c_c-c_d\), then \(e_a-e_b-e_c+e_d\) is a zero-sum rational relation of the above kind and must vanish coordinatewise. For strict pairs \(a<b\), \(c<d\), equality of these coefficient vectors forces \(a=c\) and \(b=d\). Hence all positive gaps are distinct. There are \(\binom{m+1}{2}=(p^2-1)/8\) of them.

**4. Exact trapped weights.** At a fixed exceptional coupling, Step 3 guarantees that exactly one pair of distinct cosine levels collides across the two parity bands. A level \(c_j\) has momentum multiplicity \(\mu_0=1\) if \(j=0\), and \(\mu_j=2\) if \(1\le j\le m\). Equation (2) therefore consists of one nonzero term, equal to
\[
\frac2p\frac{\mu_a\mu_b}{\mu_a+\mu_b}
=\begin{cases}\frac{4}{3p},&a=0,\\[1mm]\frac2p,&1\le a<b.\end{cases}
\]
At other positive couplings there are no cross-band collisions, so (2) vanishes. Finally, an equation \(c_a-c_b=1=c_0\) would yield the nonzero rational relation \(e_a-e_b-e_0\) among the cosine levels. This vector is not proportional to \((1/2,1,\ldots,1)\) (for \(a=0\), it has only one nonzero coordinate; for \(a>0\), it has both positive and negative coordinates). It is therefore impossible. Thus \(t=|g|\) lies outside the exceptional set. The classification follows.

## Verification

The standalone script `verify.py` builds the full real symmetric adjacency Hamiltonian, groups its eigenvalues numerically, evaluates the bright-space projection independently of the analytical Fourier-count formula, and also propagates selected non-Hermitian sink evolutions directly. Run `python verify.py` after installing packages listed in `requirements.txt`. On the described test environment it printed:

`VERIFY_OK dense_spectral_cases=212 nonhermitian_checks=6 max_dense_error=4.996e-15`

The tests include both signs of cycle hopping, all predicted exceptional couplings for primes through \(17\), four nonexceptional couplings per prime, and several direct loss dynamics. Tolerance-based finite tests cannot establish uniqueness of the cosine gaps for all primes; Step 3 supplies the exact proof. Convergence of direct propagations is checked only at listed finite times, not used as a proof of infinite-time decay.

## Relationship to prior work

Krovi and Brun [1] relate dark subspaces of quantum walks to graph symmetries and degenerate spectra. Novo and collaborators [2] prove an invariant-subspace method for localized quantum transport sinks, and Razzoli, Paris and Bordone [3] apply that method to particular graph families. Thiel and collaborators [4] give a general bright-projector detection formula for repeated measurements, which is a related but distinct measurement protocol. Xu [5] analyzes coherent transport and traps on four-regular long-range interacting cycles. Mareš and collaborators [6] investigate coined and percolated Grover walks on an open ladder. None of these inspected sources states the parameter-complete prime-prism resonance set or its exact two-value trapped fractions.

The contribution is not a new generic dark-projector principle: that principle is prior work. The new mathematical content is the all-prime isolation and count of rung-coupling resonances, their exact state-specific survival weights, and the nonresonant unweighted-prism corollary, obtained from the interplay of two Fourier bands and prime cyclotomic independence. The cited general spectral formulas make the special-model calculation possible but do not themselves evaluate its exceptional parameter set.

## Limitations

This theorem is exact only for odd prime cycle size, the two-layer Cartesian prism with homogeneous real edge weights within and between layers, a single opposite-rung source/sink pair, and any positive sink strength. It does not determine the width of finite-time resonance peaks or a finite-time mixing or capture time. The nonzero survival probability is discontinuous as a function of coupling in the infinite-time limit; this says nothing about finite-observation robustness. The result does not claim that no earlier literature implies the classification indirectly, and no independent scientific audit has been performed.

## References

[1] H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094 (first publicly posted 2006-06-10); *Physical Review A* **74**, 042334 (2006). https://arxiv.org/abs/quant-ph/0606094

[2] L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (2014); *Scientific Reports* **5**, 13304 (2015). https://arxiv.org/abs/1412.7209

[3] L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794 (2020). https://arxiv.org/abs/2011.13794

[4] F. Thiel, I. Mualem, D. Meidan, E. Barkai and D. A. Kessler, *Dark states of quantum search cause imperfect detection*, arXiv:1906.08112 (2019). https://arxiv.org/abs/1906.08112

[5] X.-P. Xu, *Coherent exciton transport and trapping on long-range interacting cycles*, arXiv:0812.3452 (2008); *Physical Review E* **79**, 011117 (2009). https://arxiv.org/abs/0812.3452

[6] J. Mareš, J. Novotný, M. Štefaňák and I. Jex, *A counterintuitive role of geometry in transport by quantum walks*, arXiv:1908.10173 (2019); *Physical Review A* **101**, 032113 (2020). https://arxiv.org/abs/1908.10173
