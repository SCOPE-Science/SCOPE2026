# Exact two-site dark-state arithmetic on a magnetic quantum cycle

## Finding
Fix integers \(N\ge 3\) and \(1\le d<N\), a hopping amplitude \(J>0\), magnetic flux \(\phi\in\mathbb R/(2\pi\mathbb Z)\), and absorption strength \(\gamma>0\). On the cycle \(\mathbb Z/N\mathbb Z\), put
\[
H_\phi|j\rangle=J e^{-i\phi/N}|j+1\rangle+J e^{i\phi/N}|j-1\rangle,
\qquad K_\phi=H_\phi-i\gamma\bigl(|0\rangle\langle0|+|d\rangle\langle d|\bigr).
\]
Define \(\mathcal D_\phi\) as the sum of all eigenspaces of \(H_\phi\) vanishing at both sites \(0\) and \(d\), and let \(\nu(N,d,\phi)=\dim\mathcal D_\phi\). This is precisely the nondecaying subspace of the lossy dynamics \(e^{-itK_\phi}\). Write \(h=\gcd(N,d)\) and \(g=\gcd(N,2d)\). Then the **complete all-size, all-separation, all-flux dark-state classification** is
\[
\boxed{\nu(N,d,\phi)=
\begin{cases}
\lfloor(g-1)/2\rfloor,&\phi\equiv0\pmod{2\pi},\\[2pt]
\lfloor h/2\rfloor,&\phi\equiv\pi\pmod{2\pi}\ \text{and}\ N/h\ \text{odd},\\[2pt]
0,&\text{otherwise}.
\end{cases}}
\]
In particular, for the mixed initial state uniform over the \(N-2\) untrapped vertices, the exact infinite-time mean survival probability is
\[
\boxed{\lim_{t\to\infty}\frac1{N-2}\sum_{j\notin\{0,d\}}\|e^{-itK_\phi}|j\rangle\|^2=\frac{\nu(N,d,\phi)}{N-2}.}
\]
It does not depend on \(J>0\) or \(\gamma>0\). Away from the two isolated magnetic-flux classes \(0\) and \(\pi\), eventual absorption occurs for every initial state.

There is an additional **flux-switch trichotomy**. If \(N\) is odd, \(\nu(N,d,0)=\nu(N,d,\pi)=(h-1)/2\). If \(N\) is even and \(N/h\) is odd, then \(\nu(N,d,\pi)=\nu(N,d,0)+1=h/2\). If \(N\) and \(N/h\) are both even, then \(\nu(N,d,\pi)=0\), whereas \(\nu(N,d,0)=h-1\). Thus \(\pi\) flux may create exactly one additional protected mode or annihilate all protected modes, depending only on trap separation arithmetic. Adjacent absorbers have \(\nu=0\) at every flux.

## Assumptions and scope
The Hilbert space is \(\mathbb C^N\) with periodic indexing; the positive edge weights are all exactly \(J\). The flux is the total Peierls phase around the cycle and is implemented uniformly along edges. There are exactly two distinct lossy vertices and both have the same strictly positive absorption strength. The non-Hermitian evolution is the standard no-detection/absorption survival evolution; squared vector norm is its unabsorbed probability. The dark dimension and average asymptotic survival are asserted for every integer \(N\ge3\), every admissible separation, all real fluxes modulo \(2\pi\), and all positive \(J,\gamma\). No statements about finite-time absorption rates are made.

## Proof
**1. The nondecaying space is the dark eigenspace.** For any eigenpair \(K_\phi u=zu\),
\[
\operatorname{Im}(z)\|u\|^2=-\gamma(|u_0|^2+|u_d|^2)\le0.
\]
Equality holds precisely when both amplitudes vanish. Then \(K_\phi u=H_\phi u\), so every eigenvector with real eigenvalue is an eigenvector of the Hermitian \(H_\phi\) with zero amplitudes at both sinks, and conversely. The joint dark eigenspace reduces both \(H_\phi\) and the trap projector: the projector annihilates the dark space and sends its orthogonal complement into itself. The lossy generator is therefore a direct sum of a Hermitian restriction on \(\mathcal D_\phi\) and a finite dissipative restriction on its orthogonal complement with all eigenvalues in the strict lower half plane. In finite dimension the latter semigroup decays to zero (possible Jordan blocks do not change the limit). Hence the exact asymptotic survival of an initial vector \(\psi\) is \(\|P_{\mathcal D_\phi}\psi\|^2\). Since \(P_{\mathcal D_\phi}\) vanishes on the two sink basis vectors, averaging over the other \(N-2\) basis vectors gives \(\operatorname{Tr}(P_{\mathcal D_\phi})/(N-2)=\nu/(N-2)\).

**2. Fourier diagonalization.** The normalized Fourier characters \(u_k(j)=N^{-1/2}e^{2\pi i kj/N}\), \(k=0,\ldots,N-1\), are eigenvectors of the circulant Hermitian Hamiltonian, with energies
\[
E_k=2J\cos\!\left(\frac{2\pi k+\phi}{N}\right)
\]
A single Fourier character has nonzero amplitude at vertex \(0\), and cannot be dark. Two distinct characters have equal energy only when their phases are opposite modulo \(2\pi\). The resulting congruence is \(k+\ell+\phi/\pi\equiv0\pmod N\). Therefore a degeneracy is possible only at \(\phi\equiv0\) or \(\pi\) modulo \(2\pi\). At other fluxes, all energy eigenspaces are one-dimensional, and the dark dimension is zero.

**3. Zero flux.** At \(\phi=0\), each nontrivial degenerate pair is \((k,N-k)\), with \(1\le k<N/2\). (The characters \(k=0\), and also \(k=N/2\) when \(N\) is even, are nondegenerate.) The unique one-dimensional combination vanishing at \(0\) is proportional to \(u_k-u_{N-k}\). It vanishes at \(d\) exactly when \(N\mid2kd\). Writing \(g=\gcd(N,2d)\), this is equivalent to \(N/g\mid k\). Among integers \(1\le k<N/2\), the multiples of \(N/g\) number exactly \(\lfloor(g-1)/2\rfloor\), proving the zero-flux formula.

**4. Half flux.** At \(\phi=\pi\), energy pairs satisfy \(\ell\equiv-k-1\pmod N\). The unique combination vanishing at \(0\) also vanishes at \(d\) precisely when \(N\mid(2k+1)d\). Let \(h=\gcd(N,d)\) and \(b=N/h\). The condition becomes \(b\mid2k+1\), impossible when \(b\) is even. If \(b\) is odd, the list of odd integers \(2k+1\), for \(0\le k<N\), contains exactly \(h\) multiples of \(b\). Pairing \(k\) with \(N-1-k\) counts two indices per dark dimension. When \(N\) is odd, exactly one of these indices is a self-paired nondegenerate character (\(2k+1=N\)), which cannot vanish at \(0\). Thus the dimension is \(h/2\) for even \(N\), and \((h-1)/2\) for odd \(N\), i.e. \(\lfloor h/2\rfloor\). This also shows that all listed dark modes are linearly independent and that none were omitted.

**5. Flux-switch trichotomy.** If \(N\) is odd then \(g=h\), both odd, and \(N/h\) is odd. If \(N\) is even and \(N/h\) is odd, then \(h\) is even and \(g=h\). If \(N/h\) is even, then \(g=2h\), so the zero-flux count is \(h-1\) while the half-flux count is zero. This proves each remaining assertion. When \(d=1\), \(g=\gcd(N,2)\) and \(h=1\), so both exceptional dimensions vanish as well.

## Verification
The standalone `checker.py` constructs the Hermitian magnetic-cycle matrix without invoking the arithmetic formula, groups degenerate eigenspaces numerically, computes the two-site evaluation-map nullities by singular values, and checks the dissipative eigenvalue count. It checks all separations for \(3\le N\le45\) at flux \(0\), \(\pi\), and \(\pi/3\), and explicitly compares late-time survival for six representative geometries. Its 5,473 numerical assertions all passed. Run `python checker.py` with Python 3.10+, NumPy, and SciPy. The proof above, not these finite numerical tests, establishes the all-parameter theorem.

## Relationship to prior work
Agliari, Mülken, and Blumen studied continuous-time quantum walks on rings with one or many lossy traps, including perturbative formulas for trap configurations at zero flux; their Eq. (22) already identifies zero-leading-width degenerate modes for even rings and implies important zero-flux special cases of the present classification. Those zero-flux special cases are not asserted as separately new. Thiel, Mualem, Meidan, Barkai, and Kessler developed general bright/dark-state criteria for repeated quantum detection, including cycle and flux examples with single-vertex detection. The specific evaluated **two-distinct-absorber, arbitrary-separation half-flux counting law** and the all-flux arithmetic creation/annihilation trichotomy are the contribution assessed here. More general spectral machinery can in principle recover the result, and an unlocated explicit previous specialization cannot be ruled out.

## Limitations
Exact equal hopping strengths, a single cycle, precisely two absorbing sites, and uniform Peierls flux are essential to the formula. The dark dimension is a statement about asymptotic no-click survival with the absorptive non-Hermitian generator, not an unconditional statement about every finite-interval projective measurement protocol. The existence of nondecaying modes does not imply that every initial state survives. Adding disorder, extra absorbers, nonuniform magnetic bond phases with the same total flux (up to appropriate gauge transformation of sink amplitudes), or dephasing may alter the conclusions. The earliest motivating work below does not itself contain the full count established here; the earlier 2009 trapped-ring paper does cover a substantial zero-flux subset. Independent literature-priority assessment has not been performed.

## References
1. F. Thiel, I. Mualem, D. Meidan, E. Barkai, and D. A. Kessler, *Dark states of quantum search cause imperfect detection*, arXiv:1906.08112v1, first posted 19 June 2019; Phys. Rev. Research 2, 043107 (2020). https://arxiv.org/abs/1906.08112
2. E. Agliari, O. Mülken, and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288v1, first posted 19 March 2009. https://arxiv.org/abs/0903.3288
3. F. Thiel, I. Mualem, D. A. Kessler, and E. Barkai, *Quantum total detection probability from repeated measurements II: Exploiting symmetry*, arXiv:1909.02114v1, first posted 4 September 2019. https://arxiv.org/abs/1909.02114
