# Exact long-time survival of two lossy bosons on a cycle: parity and antipodal selection

## Finding
Let two identical soft-core bosons hop coherently on the cycle \(C_n\), \(n\ge3\), with nonzero real hopping \(J\) and strictly positive onsite two-body loss rate \(\gamma\). Write \(S_n(x,y)\) for the probability that the two initially separated bosons at vertices \(x\ne y\) have suffered no pair-annihilation jump as time tends to infinity. With \(d=y-x\pmod n\), the exact law is
\[
 S_n(x,y)=\begin{cases}
 0,&n\text{ odd},\\
 2/n,&n\equiv0\pmod4\text{ and }d=n/2,\\
 0,&n\equiv2\pmod4\text{ and }d=n/2,\\
 1/n,&n\text{ even and }d\ne n/2.
 \end{cases}
\]
An initially doubly occupied vertex has zero long-time survival probability for every \(n\). The exact dimension of the nondecaying two-boson space is zero when \(n\) is odd, \(n/2\) when \(n\equiv0\pmod4\), and \(n/2-1\) when \(n\equiv2\pmod4\). In particular, diametrically separated bosons either double or entirely lose the usual \(1/n\) survival depending on the residue of the circumference modulo four.

## Assumptions and scope
The one-particle site space is \(\mathbb C^n\), with standard cyclic indices \(x\in\mathbb Z/n\mathbb Z\). The two-particle Hilbert space is its symmetric square. With canonical bosonic operators, take the hopping Hamiltonian and Lindblad jumps to be
\[
 H=J\sum_{x\in\mathbb Z/n\mathbb Z}(b_{x+1}^{\dagger}b_x+b_x^{\dagger}b_{x+1}),\qquad L_x=\sqrt\gamma\,b_x^2.
\]
There is no elastic onsite interaction or additional external potential. The two-particle normalized basis vector at distinct sites is \(|x,y\rangle=b_x^\dagger b_y^\dagger|\Omega\rangle\); for coincident sites it is \(|x,x\rangle=(b_x^\dagger)^2|\Omega\rangle/\sqrt2\). Let \(P=\sum_x|x,x\rangle\langle x,x|\) and \(K=H-i\gamma P\). The survival \(S_n(x,y)\) is exactly \(\lim_{t\to\infty}\|e^{-itK}|x,y\rangle\|^2\), which is the no-jump probability for the Lindblad process started with two particles. The formula is valid for every fixed \(n\ge3\), \(J\in\mathbb R\setminus\{0\}\), and \(\gamma>0\), with no strong-loss or weak-loss limit.

## Proof
**1. The nondecaying subspace.** For every solution \(\psi(t)=e^{-itK}\psi(0)\), differentiation gives \(d\|\psi(t)\|^2/dt=-2\gamma\langle\psi(t),P\psi(t)\rangle\le0\). A real eigenvalue of \(K\) therefore has an eigenvector killed by \(P\), and such a vector is an eigenvector of the Hermitian operator \(H\). Conversely every \(H\)-eigenvector in \(\ker P\) evolves unitarily under \(K\). As \(K\) is a finite-dimensional dissipative matrix and its evolution is contractive, all other spectral contributions decay; a nontrivial Jordan block at a real eigenvalue would violate contractivity. The long-time survival of any initial vector is the squared orthogonal projection onto the direct sum \(\mathcal D=\bigoplus_E(\ker(H-E)\cap\ker P)\). Orthogonality of the decaying and nondecaying spaces follows more directly because every \(u\in\mathcal D\) satisfies both \(Ku=Eu\) and \(K^\dagger u=Eu\), so its orthogonal complement is invariant for \(K\) and contains no real eigenvalues.

**2. Momentum decomposition.** Let \(T\) shift both particle positions forward by one. Total momentum sectors are indexed by \(Q=2\pi s/n\), \(s=0,\ldots,n-1\). A symmetrized pair of single-particle momenta \(k,l\), with \(k+l=Q\pmod{2\pi}\), has energy
\[
 E_{k,l}=2J(\cos k+\cos l)=4J\cos(Q/2)\cos(k-Q/2).
\]
For \(Q\ne\pi\), two such energies coincide only if their unordered momentum pairs coincide: equality of the final cosine implies \(k'=k\) or \(k'=Q-k\) modulo \(2\pi\). Thus all symmetric energy eigenspaces within that sector are one-dimensional. Every such symmetrized momentum-pair eigenvector has a nonzero amplitude at coincident positions \((x,x)\) and is not in \(\ker P\). If a degenerate energy spans more than one total-momentum sector, their diagonal amplitudes carry distinct characters \(e^{iQx}\); Fourier orthogonality prevents cancellations between sectors. There are consequently no dark states outside \(Q=\pi\).

**3. The exceptional flat sector.** The value \(Q=\pi\) occurs if and only if \(n\) is even. There \(\cos(Q/2)=0\), so \(H\) is identically zero on the entire two-boson sector \(\mathcal H_\pi\). The onsite projector restricted to this sector has rank one, with its image spanned by the normalized alternating doublon
\[
 |D_\pi\rangle=n^{-1/2}\sum_x(-1)^x|x,x\rangle.
\]
Therefore \(\mathcal D=\mathcal H_\pi\cap|D_\pi\rangle^\perp\). The involution on the allowed one-particle momenta \(k\mapsto\pi-k\) has no fixed points when \(n\equiv2\pmod4\) and two fixed points when \(n\equiv0\pmod4\). Hence \(\dim\mathcal H_\pi=n/2\) or \(n/2+1\), respectively. Removing its one bright doublon gives exactly the stated dark dimensions. All onsite basis vectors project into the bright one-dimensional doublon in this sector, so their dark projection is zero.

**4. Initial separated particles.** The total-momentum-\(\pi\) orthogonal projector is the translation average
\[
 \Pi_\pi=\frac1n\sum_{t=0}^{n-1}(-1)^tT^t.
\]
For \(x\ne y\), its projection has no doublon component and is automatically dark. Thus \(S_n(x,y)=\langle x,y|\Pi_\pi|x,y\rangle\) when \(n\) is even. For a nonantipodal unordered pair the simultaneous translation orbit has length \(n\), with only \(t=0\) fixing the basis vector; the projector's diagonal entry is \(1/n\). For an antipodal pair, both \(t=0\) and \(t=n/2\) fix it, giving \([1+(-1)^{n/2}]/n\). For odd \(n\), the \(\pi\) sector is absent, so the survival is zero. This proves every stated case.

## Verification
The supplied `verify.py` independently constructs the normalized two-boson Fock-basis Hamiltonian, diagonal doublon projector, and each energy eigenspace. Within each eigenspace, an independent numerical singular-value calculation selects the vectors killed by the doublon projector; their orthogonal projector is compared with the closed formula for every localized two-boson basis vector. Running `python verify.py` with NumPy and SciPy passes 360 basis-state survival comparisons and all ten dark-space dimension comparisons for cycle lengths \(3\le n\le12\). Matrix checks are finite consistency checks; the all-size statement follows from the momentum-sector proof above.

## Relationship to prior work
García-Ripoll et al., arXiv:0809.3679v1 (first posted 2008-09-22), derive the master equation with onsite quadratic boson loss and nearest-neighbor hopping, and concentrate on the strong-loss Tonks–Girardeau reduction and effective decay rate. Their model motivates the present exact finite-size question, but the inspected sections do not derive this parity-sensitive asymptotic no-jump survival or the exceptional \(Q=\pi\) sector. Ates et al., arXiv:1207.6291 (2012), study dissipative binding through distance-selective losses, which differ from the onsite loss considered here. Coherent two-particle quantum walks and hard-core absorbing-walk models are not mathematically equivalent to unrestricted onsite pair annihilation. The proposed statement is limited to the particular model and observables defined above, not a general classification of dissipative two-particle quantum systems.

## Limitations
The result assumes free nearest-neighbor hopping, exact translation symmetry, symmetric two-boson statistics, strictly positive onsite pair-annihilation strength, and no onsite elastic interaction. A site potential or additional interactions can destroy the flat sector. The theorem determines the ultimate no-jump probability and the dimension of the no-loss subspace, not the finite-time decay rate or a thermodynamic many-body loss law. Finite computation does not establish novelty, and related dark-state constructions in other specialized literature remain a bibliographic risk. No independent external audit has been performed.

## References
1. J. J. García-Ripoll, S. Dürr, N. Syassen, D. M. Bauer, M. Lettner, G. Rempe, and J. I. Cirac, *Dissipation induced Tonks-Girardeau gas in an optical lattice*, arXiv:0809.3679v1 (2008-09-22), New Journal of Physics 11 (2009), 013053. https://arxiv.org/abs/0809.3679
2. C. Ates, B. Olmos, W. Li, and I. Lesanovsky, *Dissipative Binding of Lattice Bosons through Distance-Selective Pair Loss*, arXiv:1207.6291 (2012). https://arxiv.org/abs/1207.6291
3. X. Qin et al., *Quantum Walks of Two Interacting Particles in One Dimension*, arXiv:1402.3349 (2014); coherent-walk background, not used as proof of literature noncoverage. https://arxiv.org/abs/1402.3349
