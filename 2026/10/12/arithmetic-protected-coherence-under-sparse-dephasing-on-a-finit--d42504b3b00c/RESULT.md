# Arithmetic protected coherence under sparse dephasing on a finite quantum path

## Finding

**Theorem (complete asymptotic-state and position-law classification).** Fix any integer \(N\ge2\), a nonempty set \(S\subseteq\{1,\ldots,N\}\), and arbitrary fixed dephasing rates \(\gamma_r>0\) for every \(r\in S\). On the one-excitation Hilbert space \(\mathbb C^N\), take the open-path nearest-neighbor Hamiltonian and site-projector Lindbladian
\[
H=\sum_{x=1}^{N-1}(|x\rangle\langle x+1|+|x+1\rangle\langle x|),\quad
\mathcal L(X)=-i[H,X]+\sum_{r\in S}\gamma_r\left(P_rXP_r-\tfrac12\{P_r,X\}\right),\quad P_r=|r\rangle\langle r|.
\]
Put \(L=N+1\), \(g=\gcd(L,\{r:r\in S\})\), and \(b=N-g+1\). Define orthonormal path modes
\[
|\phi_\ell\rangle=\sqrt{\frac2L}\sum_{x=1}^N\sin\frac{\pi\ell x}{L}|x\rangle,
\qquad E_\ell=2\cos\frac{\pi\ell}{L}\quad(1\le\ell\le N),
\]
and the projector onto the common unmonitored eigenmode space
\[
D=\sum_{m=1}^{g-1}|\phi_{mL/g}\rangle\langle\phi_{mL/g}|,\qquad B=I-D.
\]
(For \(g=1\), \(D=0\).) The protected Hilbert-space dimension is exactly \(g-1\). There are constants \(C,c>0\), depending only on the fixed finite system and positive rates, such that for every initial density matrix \(\rho\) and every \(t\ge0\),
\[
\left\|e^{t\mathcal L}(\rho)-e^{-itH}D\rho D e^{itH}
-\frac{\operatorname{Tr}(B\rho)}{b}B\right\|_2\le Ce^{-ct}.
\tag{1}
\]
Thus **all** initial states converge to the maximally mixed state \(I/N\) if and only if \(g=1\). For \(g=2\), all trajectories converge, but their limits generally retain initial-state memory. For \(g\ge3\), some site-localized initial states have nonconvergent, persistent oscillations in their site probabilities.

The exact long-time *Cesàro* occupation kernel is also independent of the strictly positive rate values. Let
\[
w_x=\begin{cases}g/L,&g\nmid x,\\0,&g\mid x,\end{cases}
\quad\text{and}\quad
\overline p_{jk}=\lim_{T\to\infty}\frac1T\int_0^T
\langle k|e^{t\mathcal L}(|j\rangle\langle j|)|k\rangle\,dt.
\]
For all \(1\le j,k\le N\),
\[
\boxed{\overline p_{jk}=\frac{(1-w_j)(1-w_k)}{b}
+\frac{g}{L^2}\mathbf1_{g\nmid j}\mathbf1_{g\nmid k}
\left(1+\frac12\mathbf1_{j\equiv k\;(\mathrm{mod}\;g)}
+\frac12\mathbf1_{j\equiv-k\;(\mathrm{mod}\;g)}\right).}
\tag{2}
\]
In particular, any single monitored endpoint forces full equilibration, whereas on an odd path with \(N=2m-1\), monitoring only the midpoint \(m\) preserves exactly \(m-1\) coherent eigenmodes.

## Assumptions and scope

The evolution is finite-dimensional, continuous-time, trace-preserving, Markovian and purely dephasing, without particle absorption or reservoirs exchanging excitations. The Hamiltonian is the path **adjacency** matrix (not the degree-dependent combinatorial Laplacian), with unit real hopping and open boundaries. The monitored positions are distinct vertices; each associated projector has a *strictly positive*, time-independent rate. Initial density matrices may be arbitrary, including coherent and mixed states. Formula (1) uses the Hilbert–Schmidt norm; equivalent norms obey analogous bounds in fixed dimension. Formula (2) concerns a temporal Cesàro average and does not assert pointwise convergence when \(g\ge3\).

## Proof

**Step 1: exact protected eigenmodes.** The discrete sine transform diagonalizes the adjacency matrix, giving the normalized \(\phi_\ell\) and distinct \(E_\ell\) displayed above. A mode is annihilated by every monitored projector exactly when \(\sin(\pi\ell r/L)=0\) for each \(r\in S\), equivalently \(L\mid \ell r\) for all such \(r\). Bézout's identity turns the latter conditions into \(L/g\mid\ell\). Since \(1\le\ell\le L-1\), the solutions are exactly \(\ell=mL/g\), \(1\le m\le g-1\). The resulting \(D\) commutes with \(H\) and satisfies \(P_rD=DP_r=0\).

**Step 2: all peripheral eigenoperators.** For every complex matrix \(X\), direct expansion of the generator gives the Hilbert–Schmidt dissipation identity
\[
\operatorname{Re}\operatorname{Tr}(X^\dagger\mathcal L(X))
=-\frac12\sum_{r\in S}\gamma_r\|[P_r,X]\|_2^2.
\tag{3}
\]
Every eigenoperator with purely imaginary eigenvalue must therefore commute with all \(P_r\). Since the dissipator then vanishes on it, such an eigenoperator also obeys \([H,X]=\omega X\) for some real \(\omega\).

If \(\omega=0\), the path spectrum is simple, so \(X\) is diagonal in the path-energy basis. Writing its diagonal coefficients as \(c_\ell\), the identities \([P_r,X]=0\) become \((c_a-c_b)\phi_a(r)\phi_b(r)=0\). The ground sine mode \(\phi_1\) is nonzero at *every* site, while every energy mode outside \(D\) is nonzero at at least one monitored site. Thus all coefficients outside \(D\) are equal; the stationary eigenoperator space is precisely the span of \(B\) and the dark-mode diagonal projections.

If \(\omega\ne0\), \(X\) has matrix entries only between energy modes of fixed nonzero energy difference. Because each path energy is simple, each row and column of this matrix has at most one nonzero entry; sorting the energies makes \(X\) strictly triangular and hence nilpotent. Commutation with \(P_r\) makes \(|r\rangle\) an eigenvector of \(X\), and nilpotence forces its eigenvalue to vanish, so \(X|r\rangle=0\) and \(\langle r|X=0\). For an entry \(X_{ab}\) with \(b\) outside the dark subspace, choose a monitored \(r\) with \(\phi_b(r)\ne0\); the single-entry property of row \(a\) and \(X|r\rangle=0\) force \(X_{ab}=0\). Applying the column argument similarly eliminates entries with \(a\) outside \(D\). Consequently, every nonstationary peripheral eigenoperator is a combination of dark-to-dark matrix units \(|\phi_a\rangle\langle\phi_b|\), with frequency \(E_a-E_b\).

**Step 3: convergence of the remainder.** Identity (3) implies that the full matrix semigroup is a Hilbert–Schmidt contraction. This rules out nontrivial Jordan blocks at imaginary-axis eigenvalues. The classification in Step 2 leaves every other eigenvalue strictly in the open left half-plane. The dark matrix units and \(B\) are also eigenoperators of the Hilbert–Schmidt adjoint with the appropriate conjugate imaginary eigenvalues; they are mutually orthogonal except for the ordinary basis overlaps internal to their span. Their coefficients in a general initial state are exactly the dark block \(D\rho D\) and the scalar \(\operatorname{Tr}(B\rho)/b\) on the bright block. Finite-dimensional spectral expansion therefore gives (1), with a positive exponential rate chosen below the spectral gap. Both the generator and its adjoint preserve \(D\) and \(B\), so no decaying term can feed back into this peripheral part.

**Step 4: exact Cesàro kernel.** Put \(w_j=\langle j|D|j\rangle\). The bright limit contributes \((1-w_j)(1-w_k)/b\). Since all dark energies are distinct, time averaging removes cross terms between different dark eigenmodes. The remaining dark probability contribution is
\[
\sum_{m=1}^{g-1}|\langle j|\phi_{mL/g}\rangle|^2
|\langle k|\phi_{mL/g}\rangle|^2
=\frac{4}{L^2}\sum_{m=1}^{g-1}
\sin^2\frac{\pi m j}{g}\sin^2\frac{\pi m k}{g}.
\]
The elementary finite Fourier sum \(\sum_{m=1}^{g-1}\cos(2\pi ma/g)=-1+g\mathbf1_{g\mid a}\), together with \(4\sin^2u\sin^2v=1-\cos2u-\cos2v+\tfrac12\cos2(u-v)+\tfrac12\cos2(u+v)\), evaluates the contribution to the second term of (2). The same sum gives \(w_x=g/L\) when \(g\nmid x\), otherwise zero. This proves (2) for all initial/target sites, including the boundary case \(g=1\).

**Step 5: sharp mixing trichotomy.** If \(g=1\), then \(D=0\) and \(B=I\), so (1) yields convergence to \(I/N\) from every initial state. For \(g>1\), taking an initial dark-mode projection gives an unmixed stationary state, disproving universal convergence to \(I/N\). If \(g=2\), \(D\) has rank one and its conjugation by \(e^{-itH}\) is constant, so all trajectories converge. If \(g\ge3\), a walker initially at vertex \(1\) overlaps positively with every dark sine mode; in the return probability the highest dark Bohr frequency occurs uniquely with a positive coefficient. Hence the surviving trigonometric polynomial is nonconstant and has no ordinary limit as \(t\to\infty\). The final placement statements follow directly from the gcd formula.

## Verification

The standalone `verify.py` reconstructs the complete complex Lindblad generator from tensor/Kronecker products, independently diagonalizes it for every one-site and two-site monitoring set on paths with \(2\le N\le7\), and compares all localized initial states with both the operator-level asymptotic projection and the closed-form kernel (2). It also checks that every numerical peripheral eigenvalue lies at a predicted dark-mode Bohr frequency. The observed run prints `VERIFY_OK monitor_sets=83 initial_sites=461 peripheral_eigenvalues=105`. Use Python 3, install the two declared dependencies from `requirements.txt`, and run `python verify.py`. These finite numerical comparisons are supplementary checks; Steps 1–5 are the proof for arbitrary finite \(N\) and positive rates.

## Relationship to prior work

The protected-subspace idea is consistent with the general noise-eigenvector criteria in Lidar and Whaley [1], but those criteria do not supply the path-specific gcd dimension, full bright/dark asymptotic state or residue-resolved position kernel. Solenov and Fedichkin [2] studied continuous monitoring at *every* vertex of a cycle, rather than monitoring an arbitrary subset of vertices of an open path. Rodríguez-Rosario, Whitfield and Aspuru-Guzik [3] introduced quantum stochastic walks and illustrated a different environmental evolution on an infinite line; their model does not yield (1)–(2). Bressanini, Benedetti and Paris [4] studied full-position-basis Haken–Strobl dephasing on graph classes and its uniform asymptotic classicalization, whereas selective monitoring can leave exact protected coherences. Hoyer [5, Ch. 2] treated site-dependent dephasing and infinite-chain diffusion, not the present finite-chain arithmetic asymptotic kernel. The closed-form all-site-set classification is not asserted to be new solely because the words or parameters differ: the scope and implication of these earlier results are distinguished above. Independent literature priority adjudication has not been performed.

## Limitations

The result does not cover a graph Laplacian with boundary-dependent site energies, periodic boundaries, disordered hopping, incoherent jumps, absorption, non-Markovian dephasing, time-varying rates or infinite chains. Convergence is not uniform as a monitored rate approaches zero, and no sharp quantitative lower bound on the spectral relaxation gap is claimed. The numeric verifier is finite; independent verification of scientific originality remains outstanding. The long-time Cesàro formula need not describe a finite-time probability when the protected subspace supports multiple energies.

## References

[1] D. A. Lidar and K. B. Whaley, *Decoherence-Free Subspaces and Subsystems* (2003), arXiv:quant-ph/0301032, especially the Lindblad formulation and Section 5.

[2] D. Solenov and L. Fedichkin, *Continuous-time Quantum Walks on a Cycle Graph* (first arXiv release 13 June 2005), arXiv:quant-ph/0506096, especially Eqs. (5) and (18).

[3] C. A. Rodríguez-Rosario, J. D. Whitfield and A. Aspuru-Guzik, *Quantum stochastic walks: A generalization of classical random walks and quantum walks* (2009), arXiv:0905.2942, main-text quantum-walk example.

[4] G. Bressanini, C. Benedetti and M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs* (2022), arXiv:2204.01836, Sections 2 and 4, DOI 10.1007/s11128-022-03647-x.

[5] S. Hoyer, *Understanding and manipulating electronic quantum coherence in photosynthetic light-harvesting*, University of California, Berkeley dissertation (2013), Chapter 2, especially Section 2.6, https://escholarship.org/uc/item/7h5340b9.
