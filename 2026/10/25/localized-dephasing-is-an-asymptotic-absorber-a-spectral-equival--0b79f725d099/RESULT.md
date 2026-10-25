# Localized dephasing is an asymptotic absorber: a spectral equivalence and arithmetic ring law

## Finding

**Theorem (exact asymptotic dephasing–absorber equivalence).** Let \(G=(V,E)\) be any finite connected undirected graph. Let \(H=H^\ast\) be its real-symmetric single-excitation tight-binding matrix, with strictly positive hopping weights along every edge and arbitrary real on-site potentials. Choose nonempty absorbing set \(F\subseteq V\) with fixed rates \(\gamma_f>0\) and a possibly empty position-dephasing set \(S\subseteq V\) with fixed rates \(\kappa_s>0\) for all \(s\in S\). Let \(P_v=|v\rangle\langle v|\), and define the trace-decreasing quantum generator
\[
\mathcal L(X)=-i[H,X]-\sum_{f\in F}\gamma_f\{P_f,X\}
+\sum_{s\in S}\kappa_s(P_sXP_s-\tfrac12\{P_s,X\}).
\]
For every positive semidefinite initial matrix \(\rho\), write \(D=\{\psi:\langle v|H^k\psi\rangle=0\ \text{for every }v\in F\cup S,\ 0\le k<|V|\}\), and let \(P_D\) be its orthogonal projector. Then
\[
\lim_{t\to\infty}\operatorname{tr}(e^{t\mathcal L}\rho)
=\operatorname{tr}(P_D\rho).
\]
This is **exactly the infinite-time survival probability** of the purely coherent model in which all sites of \(F\cup S\) instead carry positive absorption (of arbitrary positive strengths). Thus at infinite time a strictly positive *single-site dephaser* imposes the same spectral dark-state exclusion as an additional sink, despite the two having different finite-time dynamics. All strengths affect decay rates but not the limiting fraction.

**Corollary (complete single-dephaser ring classification).** For the adjacency quantum walk on the unweighted cycle \(C_n\), \(n\ge3\), with sole absorber at \(0\), sole dephasing site \(s\in\{1,\ldots,n-1\}\), and any strictly positive sink and dephasing rates, put \(g=\gcd(n,2s)\). The protected Hilbert-space dimension is
\[
\dim D=\left\lfloor\frac{g-1}{2}\right\rfloor.
\]
For a particle initially at \(a\in\{0,\ldots,n-1\}\), its exact survival probability is
\[
S_{n,s}(a)=\begin{cases}
\dfrac{g}{2n},&g\nmid 2a,\[2pt]
0,&g\mid 2a.
\end{cases}
\]
In particular **eventual absorption is certain for all initial states exactly when \(g\le2\)**. A dephaser adjacent to the sink always enforces this, while an antipodal dephaser on an even cycle preserves every coherent sink-dark mode.

## Assumptions and scope

The Hilbert space is \(\mathbb C^{|V|}\), not a many-particle Fock space. Every hopping coefficient on an edge is positive and real; diagonal site energies can be arbitrary real numbers. The edge-weight positivity and graph connectivity are essential for the shortest-path argument. Position dephasing is local and Markovian, with jump operator \(\sqrt{\kappa_s}P_s\); the absorbing term has amplitude convention \(-\gamma_f\{P_f,X\}\). The trace is nonincreasing. The limit is taken at fixed finite graph and strictly positive listed rates, before any rate tends to zero. A state \(\rho\) can be mixed and have coherences; normalized input has trace one. There is at least one absorber. The case \(S=\varnothing\) agrees with standard coherent dark-space trapping.

## Proof

**1. Cyclic annihilator.** Set \(C=\operatorname{span}\{H^k|v\rangle:v\in F\cup S,\ 0\le k<|V|\}\). Cayley–Hamilton makes \(C\) invariant under \(H\), and Hermiticity makes \(D=C^\perp\) invariant and reducing. Hence \(P_D\) commutes with \(H\). For every \(v\in F\cup S\), \(P_vP_D=P_DP_v=0\). Therefore every matrix supported on \(D\) evolves unitarily under \(\mathcal L\), and \(\mathcal L^\ast(P_D)=0\). In particular, \(\operatorname{tr}(P_D e^{t\mathcal L}\rho)=\operatorname{tr}(P_D\rho)\) at every \(t\ge0\).

**2. No other peripheral modes.** Work in the Hilbert–Schmidt matrix space. A direct calculation gives, for every complex matrix \(X\),
\[
\operatorname{Re}\langle X,\mathcal L X\rangle_{HS}
=-\sum_{f\in F}\gamma_f(\|P_fX\|_2^2+\|XP_f\|_2^2)
-\tfrac12\sum_{s\in S}\kappa_s\|[P_s,X]\|_2^2\le0.
\]
Thus the semigroup is a Hilbert–Schmidt contraction. Suppose \(\mathcal LX=i\omega X\) for real \(\omega\). Equality forces \(P_fX=XP_f=0\) for every absorber and \([P_s,X]=0\) for every dephaser. The equation then reduces to \([H,X]=-\omega X\), so \(XH=HX+\omega X\). Induction from \(X|f\rangle=0\) gives \(XH^k|f\rangle=0\) for all \(k\ge0\) and all \(f\in F\). Similarly \(X^\ast H^k|f\rangle=0\), using the adjoint commutator equation.

For each \(s\in S\), the commutation with \(P_s\) shows \(X|s\rangle=x_s|s\rangle\) and \(\langle s|X=x_s\langle s|\) for some scalar \(x_s\). Fix any \(f\in F\) and let \(d=\operatorname{dist}_G(f,s)\). All paths of length \(d\) from \(f\) to \(s\) use positive edge weights; on-site loops cannot enter a path of this minimal length. Hence \(\langle s|H^d|f\rangle>0\) (including \(d=0\) if \(s=f\)). But
\[
0=\langle s|XH^d|f\rangle=x_s\langle s|H^d|f\rangle,
\]
so \(x_s=0\). Thus \(X|s\rangle=X^\ast|s\rangle=0\), and the previous commutator induction applies to every vertex of \(F\cup S\). Therefore \(X=P_DXP_D\). All eigenoperators with imaginary-axis eigenvalues are supported entirely on \(D\).

The Hilbert–Schmidt contraction rules out nontrivial Jordan blocks on the imaginary axis: any such block would cause polynomial growth of a contracted orbit. Finite dimensionality then implies that every complementary spectral component decays exponentially. The trace of the remaining unitary part equals the conserved \(\operatorname{tr}(P_D\rho)\), proving the limit. Replacing the original generator by any coherent-generator-plus-loss model absorbing on \(F\cup S\) gives the identical cyclic annihilator \(D\) by the same argument with no dephasers; hence its asymptotic trace is identical.

**3. Arithmetic on a ring.** For an unweighted cycle, energy eigenvalues are \(2\cos(2\pi k/n)\). The eigenspace that is invisible at vertex \(0\) for each non-self-conjugate pair \(k,n-k\) is spanned by the normalized sine mode
\[
 u_k(j)=\sqrt{2/n}\,\sin(2\pi kj/n),\qquad
 1\le k\le\lfloor(n-1)/2\rfloor.
\]
The self-conjugate modes (\(k=0\), and \(k=n/2\) for even \(n\)) are visible at vertex \(0\). Sine mode \(u_k\) also vanishes at \(s\) precisely when \(n\mid 2ks\), equivalently \(n/g\mid k\) for \(g=\gcd(n,2s)\). Write \(k=t n/g\); admissible indices are exactly \(1\le t\le\lfloor(g-1)/2\rfloor\), giving the dimension formula. For a starting vertex \(a\), orthogonality of the modes gives
\[
\langle a|P_D|a\rangle=\frac2n\sum_{t=1}^{\lfloor(g-1)/2\rfloor}\sin^2(2\pi t a/g).
\]
For \(g\ge3\), pairing \(t\) with \(g-t\) and summing roots of unity yields \(\sum_{t=1}^{\lfloor(g-1)/2\rfloor}\sin^2(2\pi t a/g)=g/4\) if \(g\nmid 2a\), and zero otherwise. When \(g=1,2\), there are no admissible indices. This proves the stated piecewise formula and the complete-absorption criterion.

## Verification

The standalone program `verify_sparse_dephasing.py` builds the exact finite-dimensional Lindblad superoperator and independently computes its peripheral spectral projector. It checks the projected long-time survival against the common Krylov-annihilator projector on cycles, positive weighted paths, and asymmetric stars, including multiple dephasing sites. On cycles it also compares the derived gcd formula. The recorded run passed 1,198 finite-dimensional comparisons, maximum absolute discrepancy \(3.109\times10^{-15}\). Execute with Python 3.10 or newer and the packages in `requirements.txt`:

```sh
python verify_sparse_dephasing.py
```

These finite tests are corroborative. The all-graph and all-cycle statements are proved by the preceding analytic steps.

## Relationship to prior work

Rebentrost and coauthors (arXiv:0807.0929v1) model pure dephasing and local extraction as distinct channels and study environmental assistance numerically on biological and tree networks. Agliari, Mülken and Blumen (arXiv:0903.3288v1) obtain coherent ring trapping formulas; their analysis already anticipates much of the *coherent two-absorber ring arithmetic*. Le, Donati, Severini and Caruso (2018, DOI below) analyze dark states and noise-assisted trapping, primarily with homogeneous noise and graph perturbations. The present finding is specifically the exact all-connected-positive-weight-graph equivalence of sparse positive local dephasing to the *addition* of coherent absorbers for infinite-time survival, with the ring statement an explicit consequence. It does not claim the zero-noise two-trap spectral formula itself as new. Close prior work already establishes many general dark-state notions and dephasing-enhanced transport; historical priority for this precise equivalence is not independently certified.

## Limitations

The theorem is finite-dimensional, single-excitation and Markovian; hopping weights on all connected edges are positive real, not magnetic Peierls phases with cancellations. It does not equate finite-time dynamics, mean absorption times, weak-rate limiting processes or the complete state after conditioning on survival. Exact zeros in noise rates alter the noise support and may change the infinite-time answer discontinuously. It does not establish originality relative to unlocated general Lindblad invariant-subspace theorems, which are an acknowledged residual risk.

## References

- P. Rebentrost et al., *Environment-Assisted Quantum Transport*, arXiv:0807.0929v1 (first public 2008-07-07), https://arxiv.org/abs/0807.0929.
- E. Agliari, O. Mülken, A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288v1 (first public 2009-03-19), https://arxiv.org/abs/0903.3288.
- L. Celardo et al., *Interplay of Superradiance and Disorder in the Anderson Model*, arXiv:1403.5660v1 (first public 2014-03-22), https://arxiv.org/abs/1403.5660.
- N. Behzadi, B. Ahansaz, H. Kasani, *Dephasing-assisted selective incoherent quantum transport*, arXiv:1412.3745v1 (first public 2014-12-11), https://arxiv.org/abs/1412.3745.
- T. P. Le et al., *How to suppress dark states in quantum networks and bio-engineered structures*, J. Phys. A 51 (2018) 365306, https://doi.org/10.1088/1751-8121/aad3e6, especially sections 2, 3.3 and 6.2. [Later comparison source; not an archive-date anchor.]
