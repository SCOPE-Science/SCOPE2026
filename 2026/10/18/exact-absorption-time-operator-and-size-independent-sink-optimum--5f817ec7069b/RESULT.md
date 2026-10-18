# Exact absorption-time operator and size-independent sink optimum on quantum paths

## Finding

Let a coherent single excitation occupy the open path of \(n\ge2\) sites labelled \(0,\ldots,n-1\), with constant hopping \(J>0\) and a single irreversible Lindblad sink of rate \(\gamma>0\) at site \(0\). Write \(T\) for the first absorption-jump time. For a localized initial excitation at site \(j\), the exact mean is

\[
\boxed{\mathbb E_j T=(n-j)\left(\frac{j+1}{\gamma}+\frac{\gamma j}{4J^2}\right),\qquad 0\le j<n.}
\]

Every excitation is eventually absorbed with probability one. For each \(1\le j<n\), there is exactly one rate minimizing its mean absorption time:

\[
\boxed{\gamma_j^{\mathrm{opt}}=2J\sqrt{\frac{j+1}{j}},\quad
\min_{\gamma>0}\mathbb E_j T=\frac{n-j}{J}\sqrt{j(j+1)}.}
\]

The optimizing rate depends on the distance \(j\) from the absorber but **not** on the total path length \(n\). At the absorbing site, \(\mathbb E_0T=n/\gamma\) is strictly decreasing, so there is no finite optimal rate. In particular, the optimal rates for increasingly distant localized sources decrease strictly toward \(2J\).

More strongly, the full time-integrated survival operator is elementary. Put \(a=\min(r,s)\), \(b=\max(r,s)\), with \(0\le r,s<n\). Then

\[
\boxed{X_{rs}=\begin{cases}
(n-b)\left(\frac{a+1}{\gamma}+\frac{\gamma a}{4J^2}\right),& r\equiv s\pmod2,\\[5pt]
\frac{\mathrm{i}\operatorname{sgn}(s-r)(n-b)}{2J},& r\not\equiv s\pmod2.
\end{cases}}
\]

For an arbitrary normalized initial density matrix \(\rho\) on the path, \(\mathbb E_\rho T=\operatorname{tr}(X\rho)\). Hence the theorem evaluates coherent-superposition as well as site-localized initial conditions, rather than only a collection of diagonal means.

For the uniform incoherent initial state, the exact average and its unique rate optimum are

\[
\mathbb E_{I/n}T=\frac{(n+1)(n+2)}{6\gamma}+\frac{\gamma(n^2-1)}{24J^2},\qquad
\gamma_{\mathrm{uniform}}^{\mathrm{opt}}=2J\sqrt{\frac{n+2}{n-1}}.
\]

## Assumptions and scope

Use units with \(\hbar=1\). The single-excitation Hamiltonian is \(H=J\sum_{r=0}^{n-2}(|r\rangle\langle r+1|+|r+1\rangle\langle r|)\). Add an absorbing state \(|\varnothing\rangle\), decoupled from \(H\), and a single jump \(L=\sqrt{\gamma}\,|\varnothing\rangle\langle0|\). The full dynamics is the trace-preserving Lindblad evolution associated with \(H\) and \(L\). Neither repeated projective interrogation nor site dephasing is imposed. The stated first-jump time is the actual irreversible absorption event. The path has open ends and **no** hopping edge connecting \(0\) to \(n-1\). All results hold for every integer \(n\ge2\) and all real \(J,\gamma>0\); the zero-hopping and zero-loss limits are excluded.

Writing \(P=|0\rangle\langle0|\), the unnormalized no-jump amplitude evolves by \(K=-\mathrm{i}H-\gamma P/2\). The survival probability for state \(\rho\) is \(S_\rho(t)=\operatorname{tr}(e^{Kt}\rho e^{K^\dagger t})\), and its first-jump density is \(f_\rho(t)=-S'_\rho(t)=\gamma\langle0|e^{Kt}\rho e^{K^\dagger t}|0\rangle\).

## Proof

**Decay and moment representation.** Every eigenvalue of \(K\) has nonpositive real part, since \(K+K^\dagger=-\gamma P\). If an eigenvector had a purely imaginary eigenvalue, equality in the dissipation identity would force its site-\(0\) amplitude to vanish. The site-\(0\) eigenvalue equation would then force its site-\(1\) amplitude to vanish, and induction along the path would force all amplitudes to vanish. Therefore all eigenvalues of \(K\) have strictly negative real part, including when \(K\) is nonnormal. Hence \(S_\rho(t)\to0\), the first-jump distribution is normalized, and

\[
X=\int_0^\infty e^{K^\dagger t}e^{Kt}\,dt
\]

is well defined. Differentiating the integrand gives the Lyapunov equation

\[
K^\dagger X+XK=-I.
\]

Its Hermitian solution is unique because \(K\) is exponentially stable. Also \(\mathbb E_\rho T=\int_0^\infty S_\rho(t)\,dt=\operatorname{tr}(X\rho)\).

**Explicit all-size Lyapunov solution.** Define \(A_r=(r+1)/\gamma+\gamma r/(4J^2)\), an affine function of the integer index. Define the displayed Hermitian matrix \(X\). It remains to check

\[
\mathrm{i}J(HX/J-XH/J)_{rs}-\frac{\gamma}{2}(PX+XP)_{rs}=-\delta_{rs}.
\]

For \(1\le r<s\le n-1\), the damping term vanishes. If \(s-r\) is even, the four adjacent entries in the commutator are imaginary and cancel because \((n-s)+(n-s)=(n-s+1)+(n-s-1)\). If \(s-r\) is odd, those entries are real and cancel because \(A_{r-1}+A_{r+1}=2A_r\). The same calculation applies for \(s=r+1\), where the two central entries are diagonal, and at the right endpoint, where the formally out-of-range factors \(n-s-1\) vanish.

At \(r=s\ge1\), the purely imaginary adjacent entries give \(\mathrm{i}J[(X_{r-1,r}+X_{r+1,r})-(X_{r,r-1}+X_{r,r+1})]=-1\), with nonexistent endpoint entries read as zero. At \(r=s=0\), the two terms are \(-\gamma X_{00}=-n\) and \(\mathrm{i}J(X_{10}-X_{01})=n-1\), summing to \(-1\).

For \(r=0<s\), direct substitution of the displayed entries gives \(\mathrm{i}J(X_{1s}-X_{0,s-1}-X_{0,s+1})=\gamma X_{0s}/2\), whether \(s\) is even or odd. At \(s=1\) use the diagonal \(X_{11}\); at \(s=n-1\) the out-of-range term is zero. These boundary contributions exactly cancel the damping term. Hermitian symmetry handles \(s<r\). This exhausts the entries, proving the claimed \(X\) by uniqueness.

**Optimization.** Taking the diagonal gives the claimed sitewise means. For \(j\ge1\), the mean is a positive coefficient times \(1/\gamma\) plus a positive coefficient times \(\gamma\). Strict convexity in \(\gamma>0\), or arithmetic–geometric mean equality, gives the unique minimizer and minimum. Summing the diagonal and using \(\sum_{j=0}^{n-1}(n-j)(j+1)=n(n+1)(n+2)/6\) and \(\sum_{j=0}^{n-1}j(n-j)=n(n^2-1)/6\) gives the uniform-state formula and its optimum.

## Verification

The accompanying program `verify_path_absorption.py` constructs the path Hamiltonian and loss matrix from their definitions, separately constructs the explicit \(X\), and checks the Lyapunov residual exactly with rational arithmetic for every \(2\le n\le14\) at three parameter pairs: 39 complete matrix identities. It also solves the Lyapunov equation independently using a floating-point linear-algebra routine for every \(2\le n\le12\) at three further parameter pairs: 33 complete matrix comparisons. All checks passed. The all-size proof above is a direct finite-difference identity and stability argument; the finite computations are corroboration, not extrapolation.

Run with `python verify_path_absorption.py` using Python 3, SymPy, NumPy and SciPy. No experimental data or external numerical certificates enter the theorem.

## Relationship to prior work

Varbanov, Krovi and Brun (arXiv:0803.3446, first public version March 24, 2008) derive a general hitting-time construction using Poisson-triggered **projective measurements** and work out small graph examples, including short paths. Their interrogation generator is not the autonomous endpoint-jump Lindblad generator used here. In particular, their small-path expressions do not provide the stated arbitrary-size \(X\) or length-independent optimum.

Chia, Paterek and Kwek (arXiv:1608.05510) supply general first-jump formulas for open quantum walks in terms of superoperator inverses and examples on small graphs. The present mean is formally representable within such a general first-jump framework. What is evaluated here is the nontrivial explicit inverse for **every** path length and initial density matrix, revealing a closed two-term loss-rate law and the site-resolved, size-independent optimum. This is not a claim to have invented the general Lindblad-jump moment method.

Riberi (arXiv:2605.08056) analyzes the **same physical boundary-sink mechanism** on a semi-infinite homogeneous tight-binding line, obtaining propagators and absorption probabilities, including incomplete absorption. The finite path has a remote reflecting endpoint and complete absorption; the exact finite-size integrated-survival kernel and minimizing loss rates above do not follow by identifying the two geometries or by inserting an infinite-line expression. Ranjith and Kumar (arXiv:1302.4669) study a separate integral-equation definition of quantum first-passage probability on few-state and infinite tight-binding systems; only abstract-level material was accessible in this comparison.

## Limitations

This is a finite single-excitation result. It does not treat arbitrary onsite energies, unequal hopping, multiple or interior sinks, dephasing, many-body interactions, or the full time-dependent hitting-time distribution. The general matrix-inverse formula for first-jump moments is established prior work, and differently indexed exact finite-path evaluations cannot be ruled out by searches alone. The mean formula must not be transferred to Poissonian projective-monitoring or infinite-chain first-passage protocols.

## References

1. M. Varbanov, H. Krovi, and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446v1 (2008), DOI: 10.1103/PhysRevA.78.022324.
2. A. Chia, T. Paterek, and L. C. Kwek, *Hitting statistics from quantum jumps*, arXiv:1608.05510 (2016), DOI: 10.22331/q-2017-07-21-19.
3. F. Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056 (2026), revision v4.
4. V. Ranjith and N. Kumar, *Quantum First-Passage Time: Exact Solutions for a Class of Tight-Binding Hamiltonian Systems*, arXiv:1302.4669 (2013).
