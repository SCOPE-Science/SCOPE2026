# Antipodal absorption resonances on Möbius quantum ladders

## Finding

For every integer \(n\ge3\), let \(M_{2n}\) be the graph on the cyclic labels \(0,1,\ldots,2n-1\) with edges joining each \(j\) to \(j+1\), \(j-1\), and \(j+n\), all modulo \(2n\). This is the cubic Möbius ladder, namely the circulant graph \(\operatorname{Ci}_{2n}(1,n)\). Its adjacency matrix is \(A_n\). Fix any positive absorption strength \(\gamma>0\), put an absorbing site at \(0\), and start a one-particle continuous-time quantum walk at the rung-opposite vertex \(n\). The effective Hamiltonian is
\[
K_{n,\gamma}=A_n-i\gamma |0\rangle\langle0|.
\]

The eventual survival probability exists and satisfies the exact arithmetic law
\[
\boxed{\lim_{t\to\infty}\|e^{-itK_{n,\gamma}}|n\rangle\|^2 =
\begin{cases}
\dfrac{2}{n}, & n\equiv3\pmod6,\\[4pt]
\dfrac{4}{3n}, & n\equiv2\pmod4,\\[4pt]
0,&\text{otherwise}.
\end{cases}}
\]

The identity holds for each fixed \(n\) and **every** \(\gamma>0\); no statement of uniform convergence in \(\gamma\) or \(n\) is made. In particular, an initially rung-adjacent particle is absorbed with probability one for all sizes outside the two specified arithmetic classes, despite the presence of many nondecaying modes for every size.

The subspace on which absorption occurs (the spectral, or bright, subspace) has exact dimension
\[
\boxed{R_n=n+1-\mathbf1_{\{n\equiv3\;(\mathrm{mod}\;6)\;\text{or}\;n\equiv2\;(\mathrm{mod}\;4)\}}.}
\]
Thus the complementary dark subspace has dimension \(2n-R_n\). This latter dimension describes arbitrary initial states, whereas the displayed survival law concerns the specific initial vertex \(n\).

## Assumptions and scope

The graph is simple and unweighted, with \(n\ge3\); hopping is governed by the self-adjoint adjacency matrix, not a discrete-time coined walk. There is one non-Hermitian loss term of strictly positive strength at vertex \(0\). The source \(|n\rangle\) and trap \(|0\rangle\) are endpoints of the added antipodal rung. Units set the hopping magnitude and \(\hbar\) to one. Survival refers to the limiting squared norm of the unnormalized state under the absorbing evolution. The graph is regular of degree three; replacing \(A_n\) by \(3I-A_n\) changes only the energy convention and does not change the invariant bright/dark spaces.

## Proof

**1. Dissipation and spectral projections.** For a finite real symmetric matrix \(A\) and one trap \(|0\rangle\), decompose the state space into the orthogonal direct sum of \(\mathcal B=\operatorname{span}\{E_\lambda|0\rangle:\lambda\in\operatorname{spec}(A)\}\) and \(\mathcal D=\mathcal B^\perp\), with \(E_\lambda\) the orthogonal spectral projector for each **distinct** eigenvalue. Both spaces reduce \(A\) and the trap projector. The trap projector vanishes on \(\mathcal D\), while \(A\) acts unitarily there. On \(\mathcal B\), no eigenvector of \(A\) is orthogonal to \(|0\rangle\), by construction. If \(K=A-i\gamma|0\rangle\langle0|\) has eigenvector \(v\) and eigenvalue \(z\), then
\[
\operatorname{Im}z=-\gamma\frac{|\langle0|v\rangle|^2}{\|v\|^2}\le0.
\]
Equality requires \(v\) to be a trap-invisible eigenvector of \(A\), which is impossible on \(\mathcal B\). Every eigenvalue on \(\mathcal B\) therefore has strictly negative imaginary part, so every Jordan block of \(e^{-itK}\) there decays. Consequently the limiting survival probability is exactly \(\|P_{\mathcal D}|n\rangle\|^2\), and \(\dim\mathcal B\) is the number of distinct eigenvalues because each Fourier eigenvector has nonzero amplitude at \(0\).

**2. Two Fourier parity branches.** Write \(N=2n\). The normalized Fourier vector \(|k\rangle\), with amplitude \(e^{\pi i k j/n}/\sqrt{N}\) at vertex \(j\), is an eigenvector with eigenvalue
\[
\lambda_k=2\cos(\pi k/n)+(-1)^k,\qquad 0\le k<N.
\]
Within either parity branch, equal eigenvalues occur exactly for \(\ell\equiv\pm k\pmod N\). A collision between an **even** label \(k\) and an **odd** label \(\ell\) requires
\[
2\cos(\pi\ell/n)-2\cos(\pi k/n)=2. \tag{1}
\]

**3. Cyclotomic sign lemma.** Suppose \(z\) is a root of unity of exact order \(q\), and \(a=z+z^{-1}\) is real. If every algebraic conjugate of \(a\) is nonnegative, then \(a\in\{0,1,2\}\). If they are all nonpositive, then \(a\in\{-2,-1,0\}\). Indeed, \(a=0\) entails \(q=4\). Otherwise all conjugates have the same strict sign; the absolute norm, the product of their positive absolute values in \(\mathbb Q(z)\), is a nonzero integer and hence is at least one. By arithmetic-geometric mean, the arithmetic average of these absolute values is at least one. But the average of \(z+z^{-1}\) over automorphisms of \(\mathbb Q(z)\) equals \(2\mu(q)/\varphi(q)\) (sum of primitive \(q\)-th roots), where \(\mu\) and \(\varphi\) are the Möbius and Euler functions. Thus \(\varphi(q)\le2\) and the Möbius value has the required sign. The only possibilities are \(q=1,2,3,6\), producing \(a=2,-2,-1,1\), respectively, or \(q=4\), producing zero. This proves the lemma without an unproved classification of trigonometric identities.

Apply every Galois automorphism of \(\mathbb Q(e^{\pi i/n})\) to (1). Its exponent multiplier is odd and coprime to \(2n\), hence preserves the two parities. Since every conjugated cosine double lies in \([-2,2]\), equation (1) forces all conjugates of the even-branch double cosine to be nonpositive and all those of the odd-branch double cosine to be nonnegative. The lemma restricts their ordered pair to
\[
(-2,0),\qquad(-1,1),\qquad(0,2).
\]
The third is impossible: an odd Fourier label cannot have cosine double equal to \(2\), which occurs only at label \(0\) modulo \(2n\). For \((-2,0)\), the even label is \(k=n\), and the odd labels are \(\ell=n/2,3n/2\), which are odd precisely if \(n\equiv2\pmod4\). For \((-1,1)\), the even labels are \(2n/3,4n/3\) and the odd labels are \(n/3,5n/3\), which have the required parity precisely when \(n\equiv3\pmod6\). Conversely these displayed labels give collisions by direct substitution. These are **all** cross-parity collisions, and there is exactly one collision eigenvalue in each exceptional case.

**4. Exact bright dimension.** The even and odd Fourier branches together contain \(n+1\) distinct energies if cross-parity collisions are disregarded: each branch is paired under \(k\leftrightarrow2n-k\), with one fixed label at \(0\), and a second fixed label at \(n\) (whose branch depends on parity of \(n\)). The unique cross-parity collision in each exceptional size reduces the distinct-energy count by one. This gives the asserted bright and dark dimensions.

**5. Projection of the antipodal source.** At any distinct energy, let \(m_e\) and \(m_o\) be the numbers of even and odd Fourier labels having that energy, and let \(m=m_e+m_o\). The projections of \(|0\rangle\) and \(|n\rangle\) onto that eigenspace have squared norm \(m/(2n)\) each and mutual inner product \((m_e-m_o)/(2n)\). Hence the dark-state contribution at this energy is exactly
\[
\frac{m}{2n}-\frac{(m_e-m_o)^2}{2nm}=\frac{2m_em_o}{n(m_e+m_o)}.
\]
It is zero unless both parities occur. For \(n\equiv2\pmod4\), the sole collision has \((m_e,m_o)=(1,2)\), yielding \(4/(3n)\). For \(n\equiv3\pmod6\), it has \((m_e,m_o)=(2,2)\), yielding \(2/n\). All other sizes have no cross-parity collision, yielding zero. Together with step 1 this completes the all-size, all-strength proof.

## Verification

The accompanying standalone `verify_mobius.py` constructs the graph independently from its edges and computes its Fourier-independent real-symmetric spectral decomposition. For every \(3\le n\le80\) it compares the predicted survival and bright-subspace dimensions with numerical spectral projectors. For \(3\le n\le10\) it also computes the bright rank **exactly over the rationals** as an integer Krylov-matrix rank. For selected sizes and two positive loss strengths it confirms the expected count of eigenvalues with zero imaginary part. The completed checks were 78 spectral cases, eight exact-rank cases, and ten dissipative-spectrum cases. The finite checks only corroborate the self-contained infinite proof. Execute with Python, NumPy, and SymPy via `python verify_mobius.py`.

## Relationship to prior work

Solenov and Fedichkin (2005) treated coherent walks on a finite simple cycle with monitoring-induced decoherence; their system has neither Möbius rungs nor a single irreversible absorbing site. Krapivsky, Luck, and Mallick (2013) give a detailed treatment of single-site and multiple-site traps on ordinary cycles, including exact survival projections. Razzoli, Paris, and Bordone (2020) give a general spectral/Krylov transport-efficiency framework and worked examples on complete bipartite, strongly regular, and joined graphs. The general projection principle used here is **known**, not a new physical mechanism. The result assessed here is the complete cyclotomic classification of the parity-mixed energies of the Möbius ladder and the resulting all-size, source-specific absorbing probability, which is not given by those inspected examples. The Möbius ladder is a distinct graph family from the untwisted circular ladder or ordinary ring. The circulation and spectral equivalences were checked; the full historical literature is not exhaustively certified.

## Limitations

This concerns one-particle adjacency dynamics on finite, unweighted Möbius ladders, one site-local purely absorbing loss, fixed positive strength, and the source opposite the sink across one rung. It does not compute the finite-time survival curve, mean absorption time, decoherence effects, nonuniform couplings, arbitrary trap placements, or simultaneous size/loss limits. A more general, currently unidentified spectral-observability theorem might imply the arithmetic law; mathematical priority remains provisional pending independent literature review. The spectral and cyclotomic arguments here prove the stated result without numerical extrapolation.

## References

1. D. Solenov and L. Fedichkin, *Continuous-time Quantum Walks on a Cycle Graph*, arXiv:quant-ph/0506096 (first public submission 2005-06-13), https://arxiv.org/abs/quant-ph/0506096.
2. P. L. Krapivsky, J. M. Luck, and K. Mallick, *Survival of classical and quantum particles in the presence of traps*, arXiv:1311.6298 (first public submission 2013-11-25), https://arxiv.org/abs/1311.6298, particularly sections 4–5.
3. L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794 (first public submission 2020-11-27), https://arxiv.org/abs/2011.13794, sections 3–4 and appendices A–B.
