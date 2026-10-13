# Flux-resonant dark survival for two-trap quantum cycles

## Finding
For a coherent continuous-time walker on a magnetic cycle with two absorbing vertices, the exact surviving fraction at arbitrarily late times depends only on the cycle size, absorber separation, magnetic flux, and starting vertex. It is **independent of the two positive (possibly unequal) absorption strengths**. Apart from the two flux values \(\alpha=0\) and \(\alpha=\tfrac12\) modulo one, the survival fraction vanishes at every initial vertex. At the resonant fluxes it is a finite arithmetic staircase determined by two greatest common divisors.

Specifically, let \(n\ge3\), choose an integer separation \(1\le d\le n-1\), and put
\[
g=\gcd(n,2d),\qquad h=\gcd(n,d).
\]
At **zero flux**, the dark-space dimension is \(m_0=\lfloor(g-1)/2\rfloor\), and for every site \(j\in\{0,\ldots,n-1\}\),
\[
s_j(0)=\begin{cases}\dfrac{g}{2n},&g\nmid 2j,\\[3pt]0,&g\mid2j.\end{cases}
\]
At **half a flux quantum**, the dark-space dimension is \(m_{1/2}=\lfloor h/2\rfloor\) when \(n/h\) is odd (and zero otherwise). Thus a nonzero dark space requires both \(n/h\) odd and \(h\ge2\). When \(n/h\) is odd and \(n\) is odd,
\[
s_j(\tfrac12)=\begin{cases}\dfrac{h}{2n},&h\nmid j,\\[3pt]0,&h\mid j.\end{cases}
\]
When \(n/h\) is odd and \(n\) is even (necessarily \(h\) even),
\[
s_j(\tfrac12)=\begin{cases}
0,&j\equiv0\pmod h,\\[3pt]
\dfrac hn,&j\equiv h/2\pmod h,\\[3pt]
\dfrac h{2n},&\text{otherwise}.
\end{cases}
\]
If \(n/h\) is even, half-flux survival is zero. Every other flux yields zero survival. For a uniformly sampled nonabsorbing input vertex, the averaged limiting survival is \(m_\alpha/(n-2)\), with the dimension in the applicable case and zero otherwise.

## Assumptions and scope
Let the Hilbert space be \(\mathbb C^n\) with orthonormal site vectors \(|j\rangle\), indices taken modulo \(n\). The Hermitian nearest-neighbor Hamiltonian is
\[
H_\alpha=\sum_{j=0}^{n-1}\left[e^{-2\pi i\alpha/n}|j+1\rangle\langle j|+e^{2\pi i\alpha/n}|j\rangle\langle j+1|\right].
\]
The no-capture effective Hamiltonian with continuous local absorption is
\[
K_\alpha=H_\alpha-i\left(\gamma_0|0\rangle\langle0|+\gamma_d|d\rangle\langle d|\right),\qquad\gamma_0,\gamma_d>0.
\]
For each initial site \(j\), its survival norm is \(S_j(t)=\|e^{-itK_\alpha}|j\rangle\|^2\). The theorem concerns its limit \(s_j(\alpha)=\lim_{t\to\infty}S_j(t)\), not a finite-time approximation. Flux \(\alpha\) is physically periodic modulo integers. The two absorbers occupy distinct vertices, and all hopping magnitudes are one.

## Proof
**Dissipative spectral reduction.** Write \(\Gamma=\gamma_0|0\rangle\langle0|+\gamma_d|d\rangle\langle d|\). For any solution of \(\dot\psi=-iK_\alpha\psi\),
\[
\frac{d}{dt}\|\psi(t)\|^2=-2\gamma_0|\psi_0(t)|^2-2\gamma_d|\psi_d(t)|^2\le0.
\]
If \(K_\alpha v=\lambda v\) with \(\operatorname{Im}\lambda=0\), taking the imaginary part of \(\langle v,K_\alpha v\rangle\) forces \(v_0=v_d=0\); therefore \(H_\alpha v=\lambda v\). Conversely an eigenvector of \(H_\alpha\) vanishing at both traps is a nondissipating eigenvector of \(K_\alpha\). The span \(\mathcal D_\alpha\) of these eigenvectors is reducing for both \(K_\alpha\) and its adjoint, because \(\Gamma\) annihilates it. On its orthogonal complement all eigenvalues of \(K_\alpha\) have strictly negative imaginary part. In finite dimensions, the complementary exponential decays to zero, even when Jordan blocks occur. Consequently
\[
s_j(\alpha)=\langle j|P_{\mathcal D_\alpha}|j\rangle.
\]
In particular, the limit is independent of the positive values of \(\gamma_0\) and \(\gamma_d\).

**Degeneracies and dark waves.** The orthonormal plane waves \(v_k(j)=n^{-1/2}e^{2\pi i kj/n}\) diagonalize \(H_\alpha\), with eigenvalues
\[
E_k(\alpha)=2\cos\left(\frac{2\pi(k+\alpha)}n\right),\qquad 0\le k<n.
\]
Distinct eigenvalues coincide exactly when \(k+k'+2\alpha\equiv0\pmod n\). Thus degeneracy requires \(2\alpha\) integral. When the spectrum is simple, each eigenvector has nonzero amplitude on every site, so \(\mathcal D_\alpha=\{0\}\).

At \(\alpha=0\), the nontrivial eigenspace pairs are \((k,n-k)\). The unique normalized vector in such a pair vanishing at site zero is
\[
u_k(j)=\sqrt{\frac2n}\sin\!\left(\frac{2\pi kj}n\right).
\]
The second absorber is dark exactly when \(n\mid2kd\), equivalently \((n/g)\mid k\). For \(1\le k<n/2\), these are \(k=tn/g\), where \(t=1,\dots,\lfloor(g-1)/2\rfloor\). The dark dimension is therefore \(m_0\) as stated, and
\[
s_j(0)=\frac2n\sum_{t=1}^{\lfloor(g-1)/2\rfloor}\sin^2\!\left(\frac{2\pi tj}{g}\right).
\]
Pairing a sine term with its reflection and summing the finite geometric progression gives \(\sum_t\sin^2(2\pi tj/g)=g/4\) when \(g\nmid2j\), and zero otherwise, proving the zero-flux formula.

At \(\alpha=\tfrac12\), eigenspace pairs have indices \((k,n-1-k)\); after multiplication by a site-dependent unit phase, the unique vector null at site zero has amplitudes
\[
u_k(j)=\sqrt{\frac2n}\sin\!\left(\frac{\pi(2k+1)j}n\right).
\]
Its amplitude vanishes at the second trap if and only if \(n\mid d(2k+1)\), that is, \((n/h)\mid(2k+1)\). This has solutions only if \(n/h\) is odd. In that case, write \(2k+1=(n/h)t\), where \(t\) runs over the odd integers \(1\le t<h\). There are \(\lfloor h/2\rfloor\) such terms, and
\[
s_j(\tfrac12)=\frac2n\sum_{\substack{1\le t<h\\t\text{ odd}}}\sin^2\!\left(\frac{\pi tj}{h}\right).
\]
For odd \(h\), the sum equals \(h/4\) unless \(h\mid j\), when it is zero. For even \(h\), it equals zero at \(j\equiv0\pmod h\), \(h/2\) at \(j\equiv h/2\pmod h\), and \(h/4\) otherwise. These are the claimed half-flux values. The exceptional one-dimensional eigenspaces at \(\alpha=0\) or \(\alpha=\tfrac12\) cannot be dark because their plane waves are nonzero at every vertex.

**Averaging.** Both trap sites have zero overlap with the dark projector; its trace is \(m_\alpha\). Therefore
\[
\frac1{n-2}\sum_{j\ne0,d}s_j(\alpha)=\frac{\operatorname{tr}P_{\mathcal D_\alpha}}{n-2}=\frac{m_\alpha}{n-2}.
\]
This proves every case, including the flux boundaries and unequal positive absorber strengths.

## Verification
The accompanying `verify.py` forms the Hermitian tight-binding matrix directly for all \(3\le n\le24\), all allowed \(d\), and fluxes \(0\), \(\tfrac12\), and \(0.113\). It reconstructs the undamped projector independently from matrix eigenspaces and null spaces of the two-site amplitude restrictions, then checks its dimension and every diagonal against the formulas: 825 independent configurations. Seven further checks evaluate the full non-Hermitian matrix exponential at late finite times, including unequal absorber strengths. Executing `python3 verify.py` with NumPy and SciPy prints `VERIFY_OK independent_eigenspaces= 825 matrix_semigroups= 7 trapping_formula=passed`. These finite calculations test the formulas; the proof above covers every integer size, separation, positive rate pair, and real flux.

## Relationship to prior work
Agliari, Mülken, and Blumen [1] introduce finite-ring trapping with non-Hermitian absorbing potentials, derive the general spectral framework, and calculate first-order decay shifts for arbitrary trap placements at zero magnetic flux. Their degenerate perturbation formula already contains the zero-flux dark-mode condition implicitly; that general framework and its basic implication are not claimed as new here. The contribution assessed here is the **complete exact two-absorber magnetic-flux classification, all starting-site survival probabilities, the exceptional half-flux three-level spatial profile, and rate independence** for every finite cycle.

Zimborás and collaborators [2] study time-reversal-breaking/chiral quantum transport and interference on rings, but their analyzed transport observables and sinks do not supply the present two-absorber asymptotic projection law. The later work on locally monitored chiral cycles [3] analyzes one stroboscopically monitored target, spectral dark-state constructions, and period-dependent degeneracies; its single-detector sampling protocol differs mathematically from continuous absorption at two distinct vertices. The general dark-state projection principle is shared, but the arithmetic two-target condition and source-resolved plateau are not supplied by that analysis. An equivalent treatment in other spectral-network or quantum-transport literature remains possible.

## Limitations
The model requires a uniform nearest-neighbor cycle with exactly two fixed sites of strictly positive absorption strength. The result is an infinite-time survival limit only: it provides no uniform relaxation-time bound near resonant flux. The flux discontinuity therefore does not imply a discontinuity at finite observation time. It does not treat decoherence, extra absorbers, long-range hopping, nonlinear interactions, or stochastic measurement protocols. Numerical finite-size confirmation is not an infinite proof, and published-priority status remains subject to independent verification.

## References
[1] E. Agliari, O. Mülken, A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288v1, first public 2009-03-19. https://arxiv.org/html/0903.3288v1

[2] Z. Zimborás et al., *Quantum Transport Enhancement by Time-Reversal Symmetry Breaking*, arXiv:1208.4049. https://ar5iv.labs.arxiv.org/html/1208.4049

[3] *Optimal quantum transport on a ring via locally monitored chiral quantum walks*, arXiv:2507.10669v3. https://arxiv.org/html/2507.10669v3
