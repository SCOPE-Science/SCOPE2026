# Sublattice-selective absorption laws for odd dimerized quantum chains

## Finding

For an open Su–Schrieffer–Heeger (SSH) chain with \(2m+1\) sites, \(m\ge2\), two strictly positive alternating hopping amplitudes \(a,b\), and arbitrary strictly positive absorbing strengths, the asymptotic capture probability is determined exactly by the absorber sublattice and a finite arithmetic or trigonometric condition. Label the \(m+1\) majority-sublattice sites \(A_1,\ldots,A_{m+1}\) and the \(m\) minority-sublattice sites \(B_1,\ldots,B_m\), with hoppings \(a\) between \(A_j,B_j\) and \(b\) between \(B_j,A_{j+1}\). Set \(n=m+1\).

**Minority-sublattice monitoring.** For any nonempty set \(S\subseteq\{1,\ldots,m\}\) of lossy \(B\)-sites, put
\[
 g=\gcd\bigl(n,\{j:j\in S\}\bigr).
\]
The nondecaying subspace has dimension \(2g-1\); equivalently, the absorbing subspace has dimension \(2(n-g)\). For every initially occupied \(B_x\), \(1\le x\le m\), the exact eventual absorption probability is
\[
 \boxed{P_{\mathrm{abs}}(B_x)=1-\frac{g}{n}\mathbf 1_{\{g\nmid x\}}.}
\]
This probability is independent of both positive hopping strengths, their ratio, the number of monitored sites beyond their common gcd, and the positive absorbing rates. When \(g=1\), every \(B\)-localized excitation is eventually absorbed and the **only** surviving eigenstate is the chiral zero mode on the \(A\)-sublattice. In that case an initial \(A_x\) has survival probability
\[
 \boxed{P_{\mathrm{surv}}(A_x)=\frac{(a/b)^{2(x-1)}}{\sum_{h=0}^{m}(a/b)^{2h}}.}
\]
For general \(g\), a closed finite sum for all \(A\)-initial states is given below.

**Single majority-sublattice absorber.** With one lossy site \(A_j\), \(1\le j\le n\), set \(\theta_\ell=\pi\ell/n\) and define
\[
 \mathcal R_j(a,b)=\bigl\{\ell\in\{1,\ldots,m\}:a\sin(j\theta_\ell)+b\sin((j-1)\theta_\ell)=0\bigr\}.
\]
The nondecaying dimension is \(2|\mathcal R_j(a,b)|\); the absorbing dimension is \(2m+1-2|\mathcal R_j(a,b)|\). At \(j=1\) or \(j=n\), all initial states are absorbed for every \(a,b>0\). At every interior \(j\), complete absorption fails only at the **finite, explicit** positive ratios
\[
 \frac ba=-\frac{\sin(j\pi\ell/n)}{\sin((j-1)\pi\ell/n)}>0,
 \qquad 1\le\ell\le m,
\]
with zero denominators excluded. Each index \(\ell\) realizing the chosen ratio contributes exactly a pair of surviving modes with energies of opposite sign; if several ratios coincide, their contributions add. In particular, a loss at \(A_2\) in an eleven-site chain has two dark modes when \(b/a=\sqrt3\), but none at nearby nonresonant ratios. These exact infinite-time changes do not assert finite-time discontinuities.

For the maximally mixed single-particle input, the absorption probability in either setting is its absorbing dimension divided by \(2m+1\). All conclusions hold for arbitrary positive absorbing strengths.

## Assumptions and scope

Work in the single-excitation Hilbert space \(\mathcal H=\mathbb C^{m+1}\oplus\mathbb C^m\) with orthonormal site basis \(A_1,\ldots,A_n,B_1,\ldots,B_m\). Define the real \(n\times m\) matrix \(T\) by \(T_{j,j}=a\), \(T_{j+1,j}=b\), all other entries zero, and
\[
 H=\begin{pmatrix}0&T\\T^{\!*}&0\end{pmatrix},\qquad
 K=H-i\sum_{s\in\mathcal S}\gamma_s|s\rangle\langle s|,
 \qquad \gamma_s>0.
\]
Here \(\mathcal S\) is precisely the specified monitoring set, not both settings simultaneously. For a normalized initial density matrix \(\rho\), define total no-detection survival by
\[
 S_\rho(t)=\operatorname{Tr}(e^{-itK}\rho e^{itK^{\!*}}),\qquad
 P_{\mathrm{abs}}(\rho)=1-\lim_{t\to\infty}S_\rho(t).
\]
All statements concern finite \(m\), strictly positive \(a,b\) and absorber strengths, and the infinite-time limit. They do not assume a topological bulk phase: the zero mode follows from sublattice imbalance and chiral symmetry.

## Proof

**1. Exact orthonormal spectrum.** Put \(\theta_\ell=\pi\ell/n\) for \(1\le\ell\le m\). Because
\[
 T^{\!*}T=(a^2+b^2)I_m+ab\,\operatorname{adj}(P_m),
\]
the normalized eigenvectors on the \(B\)-sublattice and their positive eigenvalues are
\[
 v_{\ell,x}=\sqrt{\frac2n}\sin(x\theta_\ell),\quad 1\le x\le m;\qquad
 E_\ell=\sqrt{a^2+b^2+2ab\cos\theta_\ell}>0.
\]
The \(E_\ell\) are pairwise distinct, since \(ab>0\) and the cosine is strictly decreasing on \((0,\pi)\). Let \(u_\ell=Tv_\ell/E_\ell\), so \(\|u_\ell\|=1\) and
\[
 u_{\ell,x}=\sqrt{\frac2n}\,\frac{a\sin(x\theta_\ell)+b\sin((x-1)\theta_\ell)}{E_\ell},\quad 1\le x\le n,
\]
where \(\sin(0)=\sin(n\theta_\ell)=0\). The normalized eigenvectors of \(H\) at \(\pm E_\ell\) are \((u_\ell,\pm v_\ell)/\sqrt2\). The remaining normalized zero eigenvector is \((w,0)\), where
\[
 w_x=\frac{(-a/b)^{x-1}}{\sqrt{\sum_{h=0}^m(a/b)^{2h}}},\qquad 1\le x\le n.
\]
Indeed, \(T^{\!*}w=0\), and \(\operatorname{rank}T=m\). Thus these \(2m+1\) vectors form a complete orthonormal eigenbasis.

**2. Capture equals the visible spectral projector.** Let \(\mathcal D\) be the span of eigenvectors of \(H\) vanishing at every lossy site, and let \(Q\) be its orthogonal projector. Every vector in \(\mathcal D\) has zero dissipator, so \(K|_{\mathcal D}=H|_{\mathcal D}\); moreover \(\mathcal D\) reduces both \(H\) and the nonnegative loss matrix. For any eigenpair \(Kz=\lambda z\) on \(\mathcal D^\perp\), taking the imaginary part of its quadratic form gives
\[
 \operatorname{Im}\lambda=-\frac{\sum_{s\in\mathcal S}\gamma_s|\langle s|z\rangle|^2}{\|z\|^2}.
\]
Equality to zero would make \(z\) a loss-free eigenvector of \(H\), contradicting its position in \(\mathcal D^\perp\). Hence all eigenvalues on \(\mathcal D^\perp\) have strictly negative imaginary part. Finite-dimensional Jordan theory makes its semigroup decay exponentially. Therefore
\[
 \lim_{t\to\infty}S_\rho(t)=\operatorname{Tr}(Q\rho),\qquad
 P_{\mathrm{abs}}(\rho)=1-\operatorname{Tr}(Q\rho).
\]
This proves the asserted independence of the strictly positive absorber rates. For any pure localized state, the dark overlap is the sum of squared components in the orthonormal dark eigenvectors.

**3. Monitoring only \(B\)-sites.** The zero eigenvector \((w,0)\) vanishes on all \(B\)-sites. Each pair \(\pm E_\ell\) is invisible precisely when \(\sin(j\pi\ell/n)=0\) for all \(j\in S\), or equivalently \(n\mid j\ell\) for all \(j\in S\). Bézout's identity reduces these simultaneous divisibilities to \((n/g)\mid\ell\). Exactly \(g-1\) indices in \(\{1,\ldots,m\}\) obey this condition, namely \(\ell_t=tn/g\) for \(1\le t<g\). The dark dimension is therefore \(1+2(g-1)=2g-1\).

At \(B_x\), the zero eigenvector has no amplitude, whereas the two dark states at \(\pm E_{\ell_t}\) together contribute \(|v_{\ell_t,x}|^2\). Consequently,
\[
 P_{\mathrm{surv}}(B_x)=\frac2n\sum_{t=1}^{g-1}\sin^2\!\left(\frac{\pi tx}{g}\right)
 =\begin{cases}0,&g\mid x,\\ g/n,&g\nmid x,\end{cases}
\]
where the last equality follows by summing the finite geometric progression of the nontrivial \(g\)th roots of unity. This yields the stated exact sitewise absorption law. At any \(A_x\), the general dark-weight formula is
\[
 P_{\mathrm{surv}}(A_x)=|w_x|^2+
 \sum_{t=1}^{g-1}|u_{\ell_t,x}|^2.
\]
In particular, \(g=1\) leaves only the normalized zero mode, giving the claimed closed geometric formula.

**4. Monitoring one \(A\)-site.** The zero mode has \(w_j\ne0\) for every \(a,b>0\) and \(1\le j\le n\), so it is always absorbed. A nonzero-energy pair is dark exactly when its common \(A_j\)-component \(u_{\ell,j}\) vanishes. Its explicit expression in step 1 gives the set \(\mathcal R_j(a,b)\) and its dimension count. The two sines \(\sin(j\theta_\ell)\) and \(\sin((j-1)\theta_\ell)\) cannot both vanish for \(0<\theta_\ell<\pi\): their difference would force \(\theta_\ell\) to be an integer multiple of \(\pi\). Thus all allowed nontrivial zero conditions determine a single positive ratio \(b/a\) in the displayed finite list. At \(j=1\), the \(A_1\)-component is \(a\sin\theta_\ell\ne0\); at \(j=n\), the \(A_n\)-component is \(b\sin(m\theta_\ell)\ne0\). Finally, with \(m=5,j=2\), the index \(\ell=5\) has \(\theta_5=5\pi/6\) and requires \(b/a=-\sin(5\pi/3)/\sin(5\pi/6)=\sqrt3\). This establishes the isolated nonuniform dimerization resonance as well as the general characterization.

## Verification

The independent spectral checker in `verify.py` builds the site Hamiltonian directly from its hopping pattern. It compares numerical eigenvector support with the dark-dimension formulas; computes every \(B\)-site capture probability from spectral projectors; checks representative non-Hermitian loss spectra; and tests exact integer characteristic-polynomial gcds in the eleven-site \(b/a=\sqrt3\) example. It uses only dependencies specified in `requirements.txt` and reports the case counts and tolerances on execution. An analytical proof, not finite testing, supplies the universal quantifiers.

## Relationship to prior work

The SSH model and its open-chain spectra are classical. Sirker, Maiti, Konstantinidis and Sedlmayr (arXiv:1406.7832, first public version 2014-06-30) establish explicit odd-chain eigenvalue/eigenvector formulas in an entanglement and fidelity setting. Their spectral data are treated here as antecedent, not a new result. Poli and collaborators (arXiv:1407.3703; *Nature Communications* 2015) demonstrate preservation of a sublattice-confined defect state under opposite-sublattice losses, establishing the qualitative mode-selection mechanism. More recently, Wang and Zhang (arXiv:2607.10218; *Physical Review A* 2026) treat a single local loss on an even-site SSH chain using non-Hermitian resolvents and Chebyshev determinants; their exact dark-mode criterion is explicitly acknowledged.

The present mathematical assertion concerns the **odd-length** chain's evaluated monitoring-site gcd law, the exact coupling-independent sitewise absorption probabilities for arbitrary nonempty sets of minority-sublattice monitors, and the finite ratio catalog for a single majority-sublattice monitor. In contrast, the cited antecedents concern clean eigenvectors, qualitative sublattice protection, or even-length loss spectra rather than these evaluated odd-chain absorption observables. The full arXiv HTML of Sirker et al. was inspected, especially Section 2.2 and the stated fidelity and entanglement results; it does not discuss absorbers, monitor-set arithmetic or sitewise capture. A broader implication from other unlocated work is a remaining publication-priority risk, and independent priority verification is not claimed.

## Limitations

The statement assumes a finite open odd chain with positive nearest-neighbor alternating hopping, Markovian imaginary-site absorption, no onsite disorder or dephasing, and the specified monitoring patterns. The mathematical claims are about the strict infinite-time limit; small nonzero perturbations can destroy isolated accidental dark pairs without making finite-time observables discontinuous. The chiral zero mode exists from bipartite imbalance, not only in a nontrivial topological bulk phase. Rates of convergence, interacting particles, disorder robustness, and arbitrary mixed-sublattice monitor sets are not classified here. The derivation is self-contained, but priority over unidentified equivalent literature is unverified.

## References

1. J. Sirker, M. Maiti, N. P. Konstantinidis, and N. Sedlmayr, “Boundary Fidelity and Entanglement in the symmetry protected topological phase of the SSH model,” arXiv:1406.7832 (first public version 2014-06-30); *Journal of Statistical Mechanics: Theory and Experiment* P10032 (2014). https://arxiv.org/abs/1406.7832
2. C. Poli, M. Bellec, U. Kuhl, F. Mortessagne, and H. Schomerus, “Selective enhancement of topologically induced interface states in a dielectric resonator chain,” arXiv:1407.3703 (2014); *Nature Communications* **6**, 6710 (2015). https://doi.org/10.1038/ncomms7710
3. Y. T. Wang and X. Z. Zhang, “From local weight selection to Zeno slowdown in an open Su-Schrieffer-Heeger chain with a single local loss,” arXiv:2607.10218 (2026); *Physical Review A* **114**, 012457 (2026). https://doi.org/10.1103/99h3-p7rj
