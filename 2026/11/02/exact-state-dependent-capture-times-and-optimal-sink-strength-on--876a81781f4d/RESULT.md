# Exact state-dependent capture times and optimal sink strength on finite quantum paths

## Finding
For a uniform finite quantum path with irreversible absorption at its last vertex, the full integrated survival operator is an elementary three-term matrix whose entries are determined by position, parity, and the two positive rates. This yields the exact mean absorption time for every (including coherent and mixed) single-excitation initial state, a unique finite optimal sink rate except for states initially entirely on the sink, and a parity-selective insensitivity principle for optimization.

Write \(n\ge2\), \(J>0\), \(\kappa>0\). For \(1\le p\le q\le n\), define Hermitian matrices \(F,G,C\) by
\[
(F_{pq},G_{pq},C_{pq})=
\begin{cases}
(p(n+1-q),\ p(n-q),\ 0),&q-p\text{ even},\\
(0,\ 0,\ -\mathrm{i}p/2),&q-p\text{ odd}.
\end{cases}
\]
For \(p>q\), use complex conjugate transposition. Then the integrated survival operator is
\[
\boxed{M=\frac{F}{\kappa}+\frac{\kappa G}{4J^2}+\frac{C}{J}.}
\]
For any density matrix \(\rho\), set \(a=\operatorname{Tr}(\rho F)\), \(b=\operatorname{Tr}(\rho G)\), \(c=\operatorname{Tr}(\rho C)\). These are real, with \(a>0\) and \(b\ge0\), and
\[
\boxed{T_\rho(\kappa)=\frac a\kappa+\frac{\kappa b}{4J^2}+\frac cJ.}
\]
If \(b>0\), the **unique** global minimizer over \(\kappa>0\) and its minimum are
\[
\boxed{\kappa_*=2J\sqrt{a/b},\qquad T_{\min}=\frac{\sqrt{ab}+c}{J}.}
\]
If \(b=0\), the initial state must be the terminal projector, and \(T=n/\kappa\) strictly decreases without a finite minimizer. The optimizing \(\kappa\) ignores coherences between positions of opposite parity, because such coherences enter only the \(C\) term, independent of \(\kappa\).

For a localized source \(|j\rangle\), this specializes to
\[
\boxed{T_j=\frac{n+(j-1)(n-j)}{\kappa}+\frac{\kappa j(n-j)}{4J^2}.}
\]
In particular, the first site has \(T_1=n/\kappa+\kappa(n-1)/(4J^2)\), optimal \(\kappa_*=2J\sqrt{n/(n-1)}\), and minimum \(\sqrt{n(n-1)}/J\).

## Assumptions and scope
The single-excitation Hilbert space is \(\mathbb C^n\) with orthonormal site basis \(|1\rangle,\ldots,|n\rangle\). The coherent Hamiltonian is the nearest-neighbor uniform path matrix
\[
H=J\sum_{p=1}^{n-1}(|p\rangle\langle p+1|+|p+1\rangle\langle p|).
\]
The irreversible sink removes excitation at site \(n\) at population rate \(\kappa\), represented by the trace-decreasing no-jump generator \(L=-\mathrm{i}H-\kappa Q/2\), \(Q=|n\rangle\langle n|\), with \(\hbar=1\). For a normalized positive-semidefinite \(\rho\) with trace one, the survival probability is \(\operatorname{Tr}(e^{Lt}\rho e^{L^\dagger t})\), and the mean absorption time is its time integral. No pure dephasing, other losses, energy detunings or multiple traps are assumed. An arbitrary initial coherent superposition is allowed.

## Proof
**1. Complete capture.** Every eigenvalue \(\lambda\) of \(L\), with eigenvector \(v\), satisfies \(2\operatorname{Re}\lambda\|v\|^2=-\kappa|v_n|^2\). Equality would force \(v_n=0\). The last row of the eigenvector equation then forces \(v_{n-1}=0\), and backward induction forces every component to vanish. Hence all eigenvalues have strictly negative real part, so \(e^{Lt}\to0\) exponentially and the mean exists. The matrix \(M=\int_0^\infty e^{L^\dagger t}e^{Lt}\,dt\) is the unique Hermitian solution of \(L^\dagger M+ML=-I\).

**2. Explicit Lyapunov solution.** Put \(S=H/J\), so \(S\) has ones only on adjacent off-diagonals. Using \([X,Y]=XY-YX\) and \(\{X,Y\}=XY+YX\), the displayed formulas for \(F,G,C\) obey the four finite identities
\[
[S,F]=0,\qquad \mathrm{i}[S,C]-\tfrac12\{Q,F\}=-I,
\]
\[
\mathrm{i}[S,G]=2\{Q,C\},\qquad \{Q,G\}=0.
\]
These are direct entrywise identities for every integer \(n\ge2\); here is a reproducible reduction rather than an appeal to numerical tests. Extend all matrix entries outside \(1,\ldots,n\) by zero. For every pair \((p,q)\), compute \([S,X]_{pq}=X_{p-1,q}+X_{p+1,q}-X_{p,q-1}-X_{p,q+1}\). Substituting the two parity cases for \(F,G,C\) and splitting at \(p<q\), \(p=q\), and the boundary \(p=n\) or \(q=n\) yields the four stated identities; the only surviving diagonal contribution of \(\mathrm{i}[S,C]\) equals \(-1\) away from the terminal site, while its terminal contribution equals \(n-1\), canceled to \(-1\) by \(-F_{nn}=-n\). Off-diagonal terminal contributions from the commutators cancel the corresponding \(Q\) anticommutators. All other entries vanish. Inserting \(M=F/\kappa+\kappa G/(4J^2)+C/J\) into
\[
L^\dagger M+ML=\mathrm{i}J[S,M]-\tfrac\kappa2\{Q,M\}
\]
and grouping powers of \(\kappa\) gives \(-I\) exactly. Complete capture gives uniqueness, establishing the matrix formula for every dimension, not merely those tested numerically.

**3. Positivity and optimization.** The matrix with entries \(\min(p,q)-pq/\ell\) is a strictly positive Brownian-bridge covariance kernel for distinct integer indices strictly between \(0\) and \(\ell\). On equal-parity blocks, \(F\) consists of \((n+1)\) times the corresponding principal covariance submatrices for \(\ell=n+1\); therefore \(F\) is strictly positive definite. Likewise \(G\) is \(n\) times the covariance kernel at \(\ell=n\), with its last row and column zero. Hence \(G\) is positive semidefinite with kernel exactly \(\operatorname{span}\{|n\rangle\}\). For a density matrix, \(a>0\), and \(b=0\) exactly when \(\rho=|n\rangle\langle n|\). For \(b>0\), the strict second derivative of \(a/\kappa+b\kappa/(4J^2)\) or the arithmetic–geometric mean inequality gives its unique minimum at \(2J\sqrt{a/b}\). The independent term \(c/J\) leaves the optimum unchanged. The diagonal entries of \(F,G,C\) give the localized-source formula.

## Verification
The accompanying self-contained `check_endpoint_path_capture.py` checks the four exact finite-matrix structural identities and definiteness for dimensions 2 through 30. It independently constructs each generator and solves the continuous Lyapunov equation (SciPy) for 180 combinations of dimension, hopping and sink rate, then tests 900 random coherent initial states. The maximum observed matrix or equation residual is about \(6.1\times10^{-10}\). Execute `python check_endpoint_path_capture.py` with NumPy and SciPy. Finite tests are diagnostics; the entrywise commutator identities and stability argument above constitute the proof for all dimensions.

## Relationship to prior work
Mülken and coauthors [1] established the non-Hermitian trapping framework and analyzed finite linear systems with two trapped endpoints, principally through decay and ensemble-averaged survival; their inspected treatment does not give this one-end, every-state integrated survival matrix or the parity-sensitive optimizer. Varbanov, Krovi, and Brun [2] study Poisson-timed projective observations, a different absorbing protocol, so their hitting-time formulas do not directly imply this continuous-loss identity. Krapivsky, Luck, and Mallick [3] analyze absorbing quantum walks with different geometries and trapping ensembles. Riberi [4] gives an exact semi-infinite boundary-sink solution and describes finite-geometry extensions as a further question; the finite-path global-time operator is neither asserted nor implied by the semi-infinite result. Standard Lyapunov-operator methods and Brownian-bridge covariance positivity are used, not claimed as novel.

## Limitations
This theorem concerns the trace-decreasing, continuously absorbing one-end finite uniform path. It does not calculate arbitrary finite-time capture distributions, multi-sink geometry, detuning, or dephasing. Some older quantum-transport publications, especially Parris [5], could not be inspected in full and might contain equivalent specializations; comprehensive historical priority and independent validation are not established. A previously studied three-site path is a special case, not a claim of novelty for that single dimension.

## References
[1] O. Mülken et al., *Survival Probabilities in Coherent Exciton Transfer with Trapping* (2007), arXiv:0705.3700, first public version 2007-05-25, https://arxiv.org/abs/0705.3700.

[2] M. Varbanov, H. Krovi and T. A. Brun, *Hitting time for the continuous quantum walk* (2008), arXiv:0803.3446, https://arxiv.org/abs/0803.3446.

[3] P. Krapivsky, J. M. Luck and K. Mallick, *Survival of quantum particles in the presence of absorbing traps* (2013), arXiv:1311.6298, https://arxiv.org/abs/1311.6298.

[4] F. Riberi, *An Exactly Solvable Absorbing Quantum Walk* (2026), arXiv:2605.08056, https://arxiv.org/abs/2605.08056.

[5] P. E. Parris, *One-dimensional quantum transport in the presence of traps*, Physical Review B 40 (1989) 4928, DOI:10.1103/PhysRevB.40.4928. Full text not inspected.
