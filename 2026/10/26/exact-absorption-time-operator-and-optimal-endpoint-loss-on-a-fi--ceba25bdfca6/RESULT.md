# Exact absorption-time operator and optimal endpoint loss on a finite quantum path

## Finding

The integrated survival time of an open quantum chain with a single lossy endpoint admits an exact matrix formula for *every* chain length, every positive loss strength, and every initial coherent or mixed state. For localized sources away from the absorber, the globally optimal absorber strength depends only on source position, not on the length of the chain.

Let \(Q_{n,\gamma}\) be the integrated survival operator defined below. For every integer \(n\ge2\), every \(\gamma>0\), and every \(1\le r\le s\le n\),

\[
(Q_{n,\gamma})_{rs}=\frac{n-s+1}{2}
\begin{cases}
(r-1)\gamma+r/\gamma,&s-r\text{ even},\\[2pt]
\mathrm i,&s-r\text{ odd},
\end{cases}
\qquad
(Q_{n,\gamma})_{sr}=\overline{(Q_{n,\gamma})_{rs}}.
\]

In particular, for the localized initial state \(|a\rangle\),

\[
T_{n,a}(\gamma)=\frac{n-a+1}{2}\left((a-1)\gamma+\frac a\gamma\right).
\]

For \(2\le a\le n\), its unique global minimizer and minimum are

\[
\gamma_*(a)=\sqrt{\frac a{a-1}},\qquad
T_{n,a}(\gamma_*(a))=(n-a+1)\sqrt{a(a-1)}.
\]

For \(a=1\), \(T_{n,1}(\gamma)=n/(2\gamma)\) decreases strictly with \(\gamma\), so there is no finite positive minimizer.

## Assumptions and scope

The Hilbert space is \(\mathbb C^n\), with orthonormal site basis \(|1\rangle,\ldots,|n\rangle\). The Hermitian hopping matrix \(H\) has \(H_{r,s}=1\) if \(|r-s|=1\) and zero otherwise; this is the *adjacency*, not the graph Laplacian, Hamiltonian. Set \(P=|1\rangle\langle1|\), let \(\gamma>0\) be fixed, and take the effective no-jump generator

\[
A=-\mathrm iH-\gamma P.
\]

The associated local irreversible sink has jump intensity \(2\gamma\) when the particle occupies site \(1\). For any positive semidefinite \(\rho\) with \(\operatorname{tr}\rho=1\), the survival probability at time \(t\ge0\) is

\[
S_\rho(t)=\operatorname{tr}\left(e^{At}\rho e^{A^\dagger t}\right).
\]

The integrated survival time is \(T_{n,\gamma}(\rho)=\int_0^\infty S_\rho(t)\,dt\). When eventual absorption is certain, it is also the mean random absorption time in the corresponding jump process. Coherence is not discarded or replaced by a classical random walk. All assertions are finite-dimensional, fixed-\(n\), and uniform over the stated range of positive \(\gamma\).

## Proof

**1. Eventual complete absorption.** If \(Av=\lambda v\) for a nonzero vector \(v\), then

\[
\operatorname{Re}\lambda=-\gamma\frac{|v_1|^2}{\|v\|^2}\le0.
\]

Equality requires \(v_1=0\). The first-row eigenvector equation then gives \(v_2=0\). The next row gives \(v_3=0\), and induction down the open chain gives \(v=0\), a contradiction. Every eigenvalue of \(A\) therefore lies strictly in the left half-plane, so \(e^{At}\to0\) exponentially. In particular \(S_\rho(t)\to0\) for every initial density matrix and the integral defining \(Q\) converges:

\[
Q=\int_0^\infty e^{A^\dagger t}e^{At}\,dt.
\]

It is Hermitian positive definite and solves the continuous Lyapunov equation

\[
A^\dagger Q+QA=-I.
\]

Because \(A^\dagger=\mathrm iH-\gamma P\), this is equivalent to

\[
\gamma(PQ+QP)-\mathrm i[H,Q]=I,\qquad [H,Q]=HQ-QH.
\]

The Lyapunov equation has a unique solution because \(A\) is strictly stable: if \(A^\dagger X+XA=0\), then \(e^{A^\dagger t}Xe^{At}\) is constant and its limit is zero, hence \(X=0\).

**2. Exact explicit solution.** Define a Hermitian matrix \(B\) by, for \(1\le r\le s\le n\),

\[
B_{rs}=\frac{n-s+1}{2}
\begin{cases}
(r-1)\gamma+r/\gamma,&s-r\text{ even},\\
\mathrm i,&s-r\text{ odd},
\end{cases}
\quad B_{sr}=\overline{B_{rs}}.
\]

For the path adjacency matrix, use \([H,B]_{rs}=B_{r-1,s}+B_{r+1,s}-B_{r,s-1}-B_{r,s+1}\), with out-of-range entries set to zero. Direct substitution into the two parity cases, including the endpoint terms, gives the following identities (their adjoints give the lower triangle):

\[
[H,B]_{11}=-\mathrm i(n-1),\qquad
[H,B]_{rr}=\mathrm i\quad (2\le r\le n),
\]

\[
[H,B]_{1s}=-\mathrm i\gamma B_{1s}\quad (2\le s\le n),\qquad
[H,B]_{rs}=0\quad (2\le r<s\le n).
\]

For clarity, the first off-diagonal identity can be checked without an induction. When \(s\) is even, \(B_{1s}=\mathrm i(n-s+1)/2\); inserting the neighboring odd-distance entries yields \([H,B]_{1s}=\gamma(n-s+1)/2\). When \(s\ge3\) is odd, \(B_{1s}=(n-s+1)/(2\gamma)\), and the neighboring even-distance entries give \([H,B]_{1s}=-\mathrm i(n-s+1)/2\). At \(s=n\) the vanishing out-of-range term preserves the same expressions. At \(r,s\ge2\), the four-neighbor terms cancel in pairs according to their parity; on the diagonal, their anti-Hermitian difference is always \(\mathrm i\). These identities include \(n=2\).

The diagonal equations of \(\gamma(PB+BP)-\mathrm i[H,B]=I\) now follow: at \((1,1)\), \(2\gamma B_{11}=n\) and \(-\mathrm i[H,B]_{11}=-(n-1)\); at every other diagonal the latter term is one. Every off-diagonal equation also holds: at \((1,s)\), the two terms cancel, and when both indices exceed one each is zero. Thus \(B\) is the unique Lyapunov solution, so \(Q=B\).

**3. Initial-state and optimization conclusions.** Cyclicity of the trace yields, for any density matrix \(\rho\),

\[
T_{n,\gamma}(\rho)=\operatorname{tr}(Q\rho).
\]

For \(\rho=|a\rangle\langle a|\), this selects the diagonal entry \(Q_{aa}\) and gives the stated formula. If \(a\ge2\), strict positivity of both coefficients in \((a-1)\gamma+a/\gamma\) implies strict convexity in the appropriate one-dimensional minimization, and

\[
(a-1)\gamma+\frac a\gamma\ge 2\sqrt{a(a-1)}
\]

with equality at the single positive \(\gamma=\sqrt{a/(a-1)}\). For \(a=1\), only the decreasing reciprocal term remains. This establishes all claims, including the independence of \(\gamma_*\) from \(n\).

## Verification

A standalone script `verify_path_lifetime.py` and dependency list `requirements.txt` reproduce the finite-dimensional checks. The program constructs the proposed \(Q\), checks its exact rational/symbolic Lyapunov residual, and independently solves the complex Lyapunov equation numerically. `verification_report.json` contains the recorded outcomes: 7,475 exactly checked matrix entries, 1,375 independent diagonal comparisons, 110 complete-matrix numerical comparisons, with maximum absolute matrix discrepancy approximately \(3.35\times10^{-10}\). These finite tests are corroboration, not an infinite-family proof. The proof above is dimension-independent.

## Relationship to prior work

Varbanov, Krovi and Brun (arXiv:0803.3446, publicly posted 24 March 2008) defined mean hitting time with Poisson-spaced measurements and a quantum measurement map. Their general inverse-superoperator approach concerns a different detection process and does not state this all-source integrated no-jump operator for open paths. Friedman, Kessler and Barkai (arXiv:1603.02046) treated stroboscopic first detection, including lines and rings; sampling and measurement reset distinguish that setting.

Burke, Wiersig and Haque (arXiv:1910.07439) analyzed local imaginary potentials in tight-binding lattices, including finite chains and absorption/scattering. Their near-central impurity and wave-packet scattering observables differ from an absorbing endpoint and an exact mean lifetime for all localized or coherent sources. The newer semi-infinite boundary-sink model arXiv:2605.08056 also shares the continuous-absorption construction but lacks the finite-path second endpoint and has a different survival regime. Wiersig's 2018 work on localized losses (doi:10.1103/PhysRevA.98.052105) is particularly plausible related literature; only its abstract was accessible, so it cannot be declared not to cover this result. The general Lyapunov representation is standard; the asserted contribution is the *specific all-size closed matrix, exact positional lifetime, and analytic optimum*, not the existence of a Lyapunov equation or of the quantum Zeno effect.

## Limitations

The formula assumes unit nearest-neighbor adjacency hopping, a finite *open* path, one absorber at the endpoint, an onsite effective loss \(-\mathrm i\gamma\), and no competing dephasing or energy disorder. It does not establish time-resolved survival laws, higher moments of absorption time, a corresponding optimum for arbitrary coherent initial states, or extensions to variable hoppings/interior losses. A related inaccessible primary full text leaves a residual possibility of earlier coverage. The result has undergone self-review only; no independent validation or historical-priority certification is claimed.

## References

1. M. Varbanov, H. Krovi, and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (first posted 2008-03-24), https://arxiv.org/abs/0803.3446.
2. H. Friedman, D. A. Kessler, and E. Barkai, *Quantum Renewal Equation for the first detection time of a quantum walk*, arXiv:1603.02046 (first posted 2016-03-07), https://arxiv.org/abs/1603.02046.
3. P. C. Burke, J. Wiersig, and M. Haque, *Non-Hermitian scattering on a tight-binding lattice*, arXiv:1910.07439 (first posted 2019-10-16), https://arxiv.org/abs/1910.07439.
4. J. Wiersig, *Role of nonorthogonality of energy eigenstates in quantum systems with localized losses*, Physical Review A 98, 052105 (2018), https://doi.org/10.1103/PhysRevA.98.052105 (abstract inspected; primary full text unavailable).
5. A. Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk* (originally circulated as *An Exactly Solvable Absorbing Quantum Walk*), arXiv:2605.08056 (2026), https://arxiv.org/abs/2605.08056.
