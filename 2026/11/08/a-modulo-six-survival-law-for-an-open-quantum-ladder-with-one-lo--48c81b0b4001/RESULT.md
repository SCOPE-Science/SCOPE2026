# A modulo-six survival law for an open quantum ladder with one lossy corner

## Finding
Let \(G_n=P_2\square P_n\) be the open ladder with two rows and \(n\ge2\) columns. For the uniform-adjacency tight-binding Hamiltonian and a positive irreversible loss at the top-left corner, launch a single excitation at the diagonally opposite bottom-right corner. Its exactly asymptotic survival probability is
\[
\boxed{\lim_{t\to\infty}\|e^{-itH_\gamma}|b,n\rangle\|^2=\begin{cases}\dfrac{3}{2(n+1)},&n\equiv5\pmod 6,\\[2pt]0,&n\not\equiv5\pmod 6.\end{cases}}
\]
This holds for every loss strength \(\gamma>0\). The loss-free adjacency operator has exactly one corner-dark eigenmode if \(n\equiv2\pmod3\), and none otherwise. When \(n\equiv2\pmod6\), the dark mode exists but the diagonally opposite starting corner is orthogonal to it; when \(n\equiv5\pmod6\), its overlap is exactly \(3/[2(n+1)]\) in probability.

## Assumptions and scope
Label the two rows \(a,b\) and the columns \(1,\ldots,n\). All edges (horizontal and vertical) carry unit real hopping, and all onsite energies are zero. Write
\[
A_n=A(P_2)\otimes I_n+I_2\otimes A(P_n),\quad H_\gamma=A_n-i\gamma|a,1\rangle\langle a,1|,\quad\gamma>0.
\]
The initial unit vector is \(|b,n\rangle\), and \(\psi(t)=e^{-itH_\gamma}|b,n\rangle\), for real \(t\ge0\). The model is a finite-dimensional continuous-time, unconditioned, no-jump excitation-survival model (the norm decays). The result concerns the infinite-time limit for each fixed finite \(n\), not a joint thermodynamic-time limit, a coined discrete-time walk, or a spatially varying hopping Hamiltonian. An arbitrary nonzero common hopping \(J\) is equivalent by time rescaling with \(\gamma/|J|>0\).

## Proof
Put \(N=n+1\). The normalized one-dimensional path modes are \(f_k(j)=\sqrt{2/N}\sin(\pi kj/N)\), for \(1\le k\le N-1\), with eigenvalues \(u_k=2\cos(\pi k/N)\). The rung eigenvectors \(v_\pm=(|a\rangle\pm|b\rangle)/\sqrt2\) give complete ladder eigenvectors \(\phi_{\pm,k}=v_\pm\otimes f_k\) and energies \(\lambda_{\pm,k}=\pm1+u_k\). Within either rung band the energies are simple. A cross-band equality requires \(u_j-u_k=2\).

We prove the needed rational-angle rigidity lemma independently. If \(u=\zeta+\zeta^{-1}\) and \(v=\eta+\eta^{-1}\), with both \(\zeta,\eta\) roots of unity, \(u,v\in(-2,2)\), and \(u-v=2\), then \(u=1\), \(v=-1\). Indeed every Galois conjugate \(u'\) satisfies \(u'=v'+2\in(0,2)\). Let \(r\) be the order of \(\zeta\), and let \(u_a=\zeta^a+\zeta^{-a}\) for units \(a\bmod r\). Every \(u_a\in(0,2)\), hence the trace \(T_r=\sum_{a\in(\mathbb Z/r\mathbb Z)^\times}u_a(2-u_a)\) is strictly positive. Write \(\varphi\) for Euler's totient and \(\mu\) for the Möbius function. Since \(\sum u_a=2\mu(r)\) and \(\sum u_a^2=2\varphi(r)+2c_r(2)\), where \(c_r(2)=\sum_{(a,r)=1}\zeta^{2a}\) is a Ramanujan sum,
\[
T_r=4\mu(r)-2\varphi(r)-2c_r(2).
\]
If \(r\) is odd and at least three, \(c_r(2)=\mu(r)\), giving \(T_r=2\mu(r)-2\varphi(r)<0\), impossible. If \(4\mid r\), the unit shift \(a\mapsto a+r/2\) changes \(u_a\) to \(-u_a\), contradicting positivity. If \(r=2s\) with \(s\ge5\) odd, then \(c_r(2)=\mu(s)\), \(\mu(r)=-\mu(s)\), and \(T_r=-6\mu(s)-2\varphi(s)\le6-8<0\). Orders one and two are excluded by \(u\in(0,2)\). The only remaining order is six, where \(u=1\), proving the lemma.

Thus the only possible cross-band degeneracy is \(u_j=1\), \(u_k=-1\), namely \(j=N/3\), \(k=2N/3\), present precisely when \(3\mid N\). It is a two-dimensional eigenspace at energy zero. Since every path mode has \(f_k(1)\ne0\), every simple level is fully bright at the corner. If \(N=3t\), the unique corner-dark mode is
\[
\chi=\frac{\phi_{+,2t}-\phi_{-,t}}{\sqrt2}.
\]
The two basis vectors have equal corner amplitude \(c=\sqrt3/(2\sqrt N)\). Their amplitudes at the opposite corner are respectively \(-c\) and \((-1)^t c\). Hence \(\langle\chi|b,n\rangle=-c(1+(-1)^t)/\sqrt2\), and
\[
|\langle\chi|b,n\rangle|^2=\begin{cases}3/(2N),&t\text{ even},\\0,&t\text{ odd}.\end{cases}
\]
Here \(t\) even is equivalent to \(6\mid N\), or \(n\equiv5\pmod6\).

Finally, the dark space is the orthogonal direct sum, over adjacency eigenspaces, of vectors annihilated by the corner projection. It reduces both \(A_n\) and \(H_\gamma\). On its orthogonal complement all eigenvalues of \(H_\gamma\) have strictly negative imaginary part: if \(H_\gamma w=\lambda w\) with \(\operatorname{Im}\lambda=0\), the identity \(\operatorname{Im}\langle w,H_\gamma w\rangle=-\gamma|\langle a,1|w\rangle|^2\) forces \(w\) to be a dark eigenvector of \(A_n\), a contradiction. All Jordan blocks in the complement therefore decay exponentially times a polynomial. The limiting squared norm is exactly the squared dark projection calculated above, independently of \(\gamma>0\).

## Verification
Run `python check.py` from the file's directory; the standalone checker uses NumPy, SymPy and SciPy. It independently constructs the full adjacency matrix, diagonalizes the finite Hamiltonian to calculate the source-to-dark-space projector, computes exact polynomial gcds for the path spectrum by the Chebyshev recurrence, and compares finite-loss matrix-exponential evolution. It reports 93 passing assertions: 59 polynomial tests \(2\le n\le60\), 29 source-projection checks \(2\le n\le30\), and five dissipative-evolution checks. The computational evidence is finite; the claim for every \(n\) follows from the analytical rational-angle lemma and spectral proof above.

## Relationship to prior work
Gönülol et al., arXiv:1008.0085, model survival in discrete-time Hadamard walks with random traps on a one-dimensional substrate. Agliari, arXiv:1102.3994, studies continuous-time trapping with random graphs and trap placements. Mareš et al., arXiv:1908.10173, and Segawa et al., arXiv:2205.13188, investigate source-to-sink survival on ladder graphs, but the model examined there is a coined discrete-time Grover walk on directed arcs, with additional loops and face-cycle dark states, not the site-based continuous-time adjacency Hamiltonian used here. Those mechanisms do not imply the modulo-six result. The underlying projection principle for dark states is established background; the new claim is its explicit, parity-sensitive evaluation for the stated model.

## Limitations
The result assumes identical horizontal and vertical hoppings, one nonzero localized loss, the specified diagonal-corner initialization and fixed finite ladder size before taking large time. It does not assert robustness under asymmetric couplings, disorder or dephasing. The existence of a dark mode does not imply that the specified source excites it, and it does not imply the existence of a physical bound state outside the finite graph. A comprehensive unpublished/unindexed priority search and independent audit have not been performed.

## References
- M. Gönülöl et al., *Survival probability in a one-dimensional quantum walk on a trapped lattice*, arXiv:1008.0085, first posted 2010-07-31, https://arxiv.org/abs/1008.0085.
- E. Agliari, *Trapping of continuous-time quantum walks on Erdős–Rényi graphs*, arXiv:1102.3994, first posted 2011-02-19, https://arxiv.org/abs/1102.3994.
- J. Mareš et al., *A counterintuitive role of geometry in transport by quantum walks*, arXiv:1908.10173, first posted 2019-08-27, https://arxiv.org/abs/1908.10173.
- E. Segawa et al., *Survival probability of the Grover walk on the ladder graph*, arXiv:2205.13188, first posted 2022-05-26, https://arxiv.org/abs/2205.13188.
