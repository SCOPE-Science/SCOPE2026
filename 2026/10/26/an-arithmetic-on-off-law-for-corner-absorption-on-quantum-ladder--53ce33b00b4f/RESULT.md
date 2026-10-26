# An arithmetic on-off law for corner absorption on quantum ladders

## Finding
For every integer \(n\ge2\), a quantum particle evolving by the **unweighted adjacency** Hamiltonian of the two-leg ladder \(P_n\square P_2\) has either no dark modes or exactly one dark mode when a positive absorbing sink acts at a corner. The distinction is the arithmetic condition
\[
\dim\mathcal D_n=\begin{cases}1,&3\mid(n+1),\\0,&3\nmid(n+1).\end{cases}
\]
Hence the absorbing (bright) subspace has dimension \(2n-\dim\mathcal D_n\). The result is valid for every fixed positive sink strength.

When \(p=n+1\) is divisible by three, the sole dark mode has energy zero and can be chosen real with components
\[
\phi(x,1)=\frac{\sin(\pi x/3)-\sin(2\pi x/3)}{\sqrt{2p}},\qquad
\phi(x,2)=\frac{-\sin(\pi x/3)-\sin(2\pi x/3)}{\sqrt{2p}},\quad 1\le x\le n.
\]
For a localized initial excitation at \((x,y)\), the final survival probability equals \(|\phi(x,y)|^2\) in that case and zero otherwise. More explicitly, it is \(3/(2p)\) on row one when \(x\equiv2,4\pmod6\), and on row two when \(x\equiv1,5\pmod6\); it vanishes at all other sites. For a maximally mixed initial state the survival probability is \(1/(2n)\) if \(3\mid p\) and zero otherwise.

## Assumptions and scope
The vertex set is \(\{(x,y):1\le x\le n,\ y\in\{1,2\}\}\). The graph has horizontal edges \((x,y)\!\sim\!(x+1,y)\) and rung edges \((x,1)\!\sim\!(x,2)\). Every edge has hopping amplitude one, and there are no on-site potentials. Let \(A\) denote its \(2n\)-by-\(2n\) real symmetric adjacency matrix. The absorbing dynamics are
\[
\psi(t)=\exp(-itH_\gamma)\psi(0),\qquad H_\gamma=A-\frac{i\gamma}{2}|c\rangle\langle c|,\quad c=(1,1),\quad \gamma>0.
\]
Survival means the squared norm \(\|\psi(t)\|^2\) for a pure state, or the trace of the evolved density operator for a mixed state. The dark space is the largest \(A\)-invariant subspace contained in the orthogonal complement of \(|c\rangle\).

## Proof
**1. Product spectrum.** Set \(p=n+1\). Because \(A=A(P_n)\otimes I_2+I_n\otimes A(P_2)\), the normalized path eigenfunctions and eigenvalues are
\[
u_j(x)=\sqrt{\frac2p}\sin\left(\frac{\pi jx}{p}\right),\qquad
\lambda_j=2\cos\left(\frac{\pi j}{p}\right),\qquad 1\le j\le p-1.
\]
The rung factors are \(v_+=(1,1)/\sqrt2\) and \(v_-=(1,-1)/\sqrt2\), with energies \(+1\) and \(-1\). Consequently the product states \(u_j\otimes v_\pm\) have energies \(\lambda_j\pm1\). Every such state has nonzero amplitude at the corner, since \(\sin(\pi j/p)\ne0\). Within each rung band the energies are strictly decreasing in \(j\); a degeneracy can only be a cross-band equality \(\lambda_j-\lambda_k=2\), where \(j<k\).

**2. The only possible degeneracy.** Let \(\zeta=e^{\pi i/p}\), a primitive \(2p\)-th root, and write \(m_j=2p/\gcd(2p,j)\) for the multiplicative order of \(\zeta^j\). Here \(m_j\ge3\) because \(1\le j<p\). Taking the normalized field trace from \(\mathbb Q(\zeta)\) to \(\mathbb Q\) gives the standard Ramanujan-sum identity
\[
\frac{\operatorname{Tr}(\zeta^j)}{[\mathbb Q(\zeta):\mathbb Q]}=\frac{\mu(m_j)}{\varphi(m_j)}.
\]
Since \(\lambda_j=\zeta^j+\zeta^{-j}\), the proposed equation \(\lambda_j-\lambda_k=2\) therefore implies
\[
\frac{\mu(m_j)}{\varphi(m_j)}-\frac{\mu(m_k)}{\varphi(m_k)}=1.
\]
For integer \(m\ge3\), the rational quantity \(\mu(m)/\varphi(m)\) lies in \([-1/2,1/2]\). Equality at \(+1/2\) occurs only for \(m=6\); equality at \(-1/2\) only for \(m=3\). Indeed \(\varphi(m)\ge2\), and the only cases with \(\varphi(m)=2\) are \(m\in\{3,4,6\}\), of which the squarefree choices give the stated values. Thus \(m_j=6\), \(m_k=3\). In the permitted index range, these equalities force \(j=p/3\) and \(k=2p/3\), necessarily with \(3\mid p\). Conversely, for these indices \(\lambda_j=1\) and \(\lambda_k=-1\), so the two opposite rung bands coincide at energy zero. There is precisely one two-dimensional eigenspace, and all other eigenspaces are one-dimensional.

**3. Corner cancellation and normalization.** At the collision, the two normalized product eigenvectors are \(u_{p/3}\otimes v_-\) and \(u_{2p/3}\otimes v_+\). They have the same nonzero corner amplitude and are orthogonal. Their difference divided by \(\sqrt2\) is the normalized vector \(\phi\) displayed above, satisfying \(A\phi=0\) and \(\langle c,\phi\rangle=0\). A generic linear combination in this eigenspace has nonzero corner amplitude, so this is the unique dark direction. Without collision, no eigenvector vanishes at \(c\). Since a Hermitian invariant subspace decomposes into eigenvectors, these observations exhaust the dark space.

**4. Absorption and location.** The operator \(H_\gamma\) leaves both the dark space and its orthogonal complement invariant, since both are \(A\)-reducing and \(|c\rangle\) lies in the bright complement. If \(H_\gamma w=zw\), then \(\operatorname{Im}(z)\|w\|^2=-(\gamma/2)|\langle c,w\rangle|^2\le0\). Equality forces \(\langle c,w\rangle=0\), so \(w\) is an \(A\)-eigenvector and belongs to the dark space. Therefore every bright eigenvalue has strictly negative imaginary part, and its finite-dimensional exponential decays, even in the presence of Jordan blocks. The dark component is stationary at energy zero. Thus \(\lim_{t\to\infty}\|\psi(t)\|^2=\|\Pi_{\mathcal D_n}\psi(0)\|^2\). Evaluating the two sine values modulo six yields the stated sitewise probabilities. Finally, for a maximally mixed initial density \(I_{2n}/(2n)\), survival is \(\operatorname{Tr}(\Pi_{\mathcal D_n})/(2n)\).

## Verification
The standalone program `verify_ladder.py` uses SymPy exact polynomial gcds and independent NumPy diagonalizations. It tests \(n=2,\ldots,50\) by the exact gcd of the two rung-shifted path characteristic polynomials, and \(n=2,\ldots,21\) by adjacency eigenspace ranks and local projection probabilities at several positive absorption strengths. An actual execution returned `ALL_CHECKS_PASSED 1124`. These finite checks corroborate the algebraic trace argument; the infinite family is proved in the preceding section.

## Relationship to prior work
Volta, Mülken and Blumen (arXiv:quant-ph/0610212, 2006) separate product spectra of finite rectangles and examine long-time **unitary** transition statistics under their graph-Laplacian convention. Their source supplies geometric context but does not address absorbing-corner projections or the adjacency-specific three-divisibility rule. Agliari, Mülken and Blumen (arXiv:0903.3288, 2009) analyze irreversible quantum trapping on finite **rings**, using a non-Hermitian sink formalism and identifying trap-invisible states. Darázs and collaborators (arXiv:1405.5078, 2014) consider traps on **Sierpinski fractals**. Razzoli, Paris and Bordone (arXiv:2011.13794, 2020) develop graph-spectral/Krylov approaches for transport efficiency in other graph families. The standard spectral and dark-state principles are not presented as new; the contribution assessed here is the complete arithmetic classification and its explicit source-position pattern for single-corner adjacency ladders.

## Limitations
This theorem assumes equal unit adjacency hopping, two legs, a single corner sink with \(\gamma>0\), and no dephasing. It does **not** apply verbatim to the combinatorial graph-Laplacian Hamiltonian, whose boundary degree terms differ, nor to weighted rungs, non-corner traps, several simultaneous sinks, interacting particles, or mean absorption times. Possible implication from a more general published spectral/controllability result remains a historical-priority risk. Numerical checking alone does not certify novelty or prove the all-length theorem.

## References
1. A. Volta, O. Mülken and A. Blumen, *Quantum transport on two-dimensional regular graphs*, arXiv:quant-ph/0610212 (first submitted 2006-10-25), https://arxiv.org/abs/quant-ph/0610212.
2. E. Agliari, O. Mülken and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288 (first submitted 2009-03-19), https://arxiv.org/abs/0903.3288.
3. Z. Darázs et al., *Transport properties of continuous-time quantum walks on Sierpinski fractals*, arXiv:1405.5078 (first submitted 2014-05-20), https://arxiv.org/abs/1405.5078.
4. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794 (first submitted 2020-11-27), https://arxiv.org/abs/2011.13794.
