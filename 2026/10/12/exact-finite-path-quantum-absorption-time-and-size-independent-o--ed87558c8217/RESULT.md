# Exact finite-path quantum absorption time and size-independent optimal sink

## Finding

For every integer \(N\ge 2\), let a single coherent excitation hop with amplitude \(J>0\) between adjacent sites of the open path \(1,\ldots,N\), and let site \(1\) lose the excitation irreversibly at Lindblad rate \(\kappa>0\). If the walker starts at site \(s\in\{1,\ldots,N\}\), its first absorption is almost sure, with **exact mean time**
\[
\boxed{\tau_{N,s}(\kappa,J)
=(N+1-s)\left(\frac{s}{\kappa}
+\frac{(s-1)\kappa}{4J^2}\right).}
\]
For each \(2\le s\le N\), this function has a unique global minimum over all positive sink rates, at
\[
\boxed{\kappa_{\mathrm{opt}}(s)=2J\sqrt{\frac{s}{s-1}},\qquad
\min_{\kappa>0}\tau_{N,s}=\frac{N+1-s}{J}\sqrt{s(s-1)}.}
\]
**The optimal sink rate is independent of the length \(N\)** for every fixed starting index \(s\). For a walker initially at the lossy site \(s=1\), the mean is instead \(N/\kappa\), strictly decreases in \(\kappa\), and has no finite-rate minimizer. The formula holds without excluding non-Hermitian exceptional points.

## Assumptions and scope

Let \(\{|j\rangle:1\le j\le N\}\) be the one-excitation basis and use units \(\hbar=1\). Set
\[
H=J\sum_{j=1}^{N-1}(|j\rangle\langle j+1|+|j+1\rangle\langle j|),\quad
P=|1\rangle\langle1|,\quad
K=-iH-\frac{\kappa}{2}P.
\]
The irreversible Lindblad jump is \(\sqrt\kappa\,|\mathrm{vac}\rangle\langle1|\). The unnormalized conditional surviving vector is \(e^{Kt}|s\rangle\); define survival \(S_s(t)=\|e^{Kt}|s\rangle\|^2\), first-absorption density \(f_s(t)=-S_s'(t)=\kappa|\langle1|e^{Kt}|s\rangle|^2\), and mean \(\tau_{N,s}=\int_0^\infty t f_s(t)\,dt=\int_0^\infty S_s(t)\,dt\). There is no bulk dissipation, dephasing, onsite disorder, periodic edge, repeated projective measurement, or coherent control other than uniform hopping.

## Proof

**1. Decay and the passage-time operator.** For any eigenpair \(Kv=\lambda v\),
\[
2\operatorname{Re}\lambda\,\|v\|^2=-\kappa|v_1|^2.
\]
If \(\operatorname{Re}\lambda=0\), then \(v_1=0\). The first row of the eigenvalue equation forces \(v_2=0\) since \(J>0\); successive rows force all components to vanish, a contradiction. Thus all eigenvalues of \(K\) have strictly negative real parts, even if \(K\) is not diagonalizable. Consequently \(S_s(t)\to0\), absorption is almost sure, and
\[
T=\int_0^\infty e^{K^\dagger t}e^{Kt}\,dt
\]
exists, is Hermitian, and is the unique solution of
\[
K^\dagger T+TK=-I.
\]
In particular \(\tau_{N,s}=T_{ss}\).

**2. An explicit solution of the entire matrix equation.** Put \(b_j=N+1-j\) and \(a_j=j/\kappa+\kappa(j-1)/(4J^2)\). Define a Hermitian matrix by, for \(1\le i\le j\le N\),
\[
T_{ij}=\begin{cases}
b_j a_i,&j-i\text{ even},\\[2pt]
\displaystyle \frac{\mathrm{i}\,b_j}{2J},&j-i\text{ odd},
\end{cases}\qquad T_{ji}=\overline{T_{ij}}.
\]
The odd-separation entry uses the imaginary unit \(\mathrm{i}\), not the site index. The sequences satisfy
\[
a_{i+1}-a_i=\frac1\kappa+\frac\kappa{4J^2},\quad
b_j-b_{j+1}=1,\quad
a_2-2a_1=\frac\kappa{4J^2}.
\]
We check all entries directly. Writing \(A\) for the path adjacency matrix, the equation is
\[
iJ(AT-TA)-\frac\kappa2(PT+TP)=-I.
\]
For every off-diagonal \(i<j\) with \(i>1\), the four neighboring matrix elements cancel because \(a_i\) and \(b_j\) are affine. This also holds for adjacent and right-end entries, by replacing out-of-range neighbors with zero and using \(b_{N+1}=0\). For the off-diagonal first row \(i=1<j\), the hopping commutator equals \(\kappa T_{1j}/2\): for even separation this uses \(a_1=1/\kappa\) and \(b_{j-1}+b_{j+1}=2b_j\); for odd separation it uses \(a_2-2a_1=\kappa/(4J^2)\). It cancels the sink term. For each interior diagonal \(2\le i\le N\), the neighboring imaginary entries give \(iJ(AT-TA)_{ii}=-1\) because \(b_i-b_{i+1}=1\), taking \(b_{N+1}=0\) at the right end. At the sink diagonal \(i=1\), the commutator gives \(N-1\) and the sink term gives \(-\kappa T_{11}=-N\), hence \(-1\). Thus the displayed matrix solves the Lyapunov equation everywhere. Uniqueness proves it is the integral operator defined above.

**3. Sharp optimization.** Taking \(i=j=s\) yields
\[
T_{ss}=(N+1-s)\left(\frac{s}{\kappa}+
\frac{(s-1)\kappa}{4J^2}\right).
\]
For \(s\ge2\), the prefactor is positive and the expression is a strictly convex sum of a positive inverse-rate term and a positive rate term. Differentiation or arithmetic-geometric mean proves that equality in the minimum occurs exactly when \(\kappa=2J\sqrt{s/(s-1)}\). Its minimum is the value in the Finding section. For \(s=1\), the rate term vanishes, giving the stated boundary exception.

## Verification

The accompanying standalone `verify_mean_absorption.py` uses only Python's standard-library rational arithmetic. Running `python3 verify_mean_absorption.py` gives `VERIFY_OK 88560 exact rational Lyapunov matrix entries`. It tests the displayed full-matrix identity, not just the diagonal values, for every \(1\le N\le40\) at four independent positive rational pairs of hopping and sink strengths. This is a finite algebraic cross-check; the proof above verifies the identity for arbitrary \(N,J,\kappa\). Independent numerical solutions of the finite continuous Lyapunov equation for \(2\le N\le8\) also reproduce the diagonal formula at multiple rates, but those floating-point checks are not necessary for the theorem.

## Relationship to prior work

Riberi's boundary-sink quantum walk (arXiv:2605.08056, first public 2026-05-08) is solved on the **semi-infinite** line and characterizes total absorption probability, transient propagation, and approximate weak/strong loss duality. Its exact solution does not supply the finite open-path mean-first-passage formula or the length-independent optimizer proved here. The present finite-chain observable has full absorption, whereas the semi-infinite source allows nonzero survival at infinite time.

Silva (arXiv:2601.09628) derives a Wronskian criterion and geometric parity effects for exceptional points of **finite** arrays with localized loss. That spectral criterion neither evaluates the integrated survival time nor proves the optimizing rate law here. Krapivsky, Luck, and Mallick (arXiv:1311.6298) analyze classical and coherent trapped walks mainly on infinite lines and **finite rings**; the latter admit undamped dark sectors, unlike the singly absorbed open path here. Varbanov, Krovi, and Brun (arXiv:0803.3446) give general Poisson-measurement hitting-time formulas and small-graph examples, but their repeated presence/absence measurements generate a different conditional dynamics, and they do not prove this path-specific Lindblad result. Peter et al. (arXiv:2403.00058) study optimal excitation trapping in chains with radiative channels and realistic dipolar couplings, with a different objective and without this exact arbitrary-length passage-time formula. A general Lyapunov solver could in principle be specialized to the stated model; the evaluation and length-independent sharp optimization are the substantive claims here.

## Limitations

The formula relies on uniform coherent nearest-neighbor hopping, a single terminal Markovian sink, a localized single-excitation initial state, and no other dissipation. It does not assert the same optimizer for superposed inputs, internal sinks, graphs with branching, disordered couplings, or other detection protocols. Its dependence on \(N\) is linear at fixed \(s\), consistent with increasingly long absorption times as the reflecting end is moved away. Equality of an optimized **mean** does not imply pointwise faster absorption at every time. Despite comparisons, an unindexed equivalent finite-path calculation remains a residual originality risk; independent review has not been performed.

## References

1. F. Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056 (2026), https://arxiv.org/abs/2605.08056.
2. J. R. Silva, *Parity-Induced Exceptional Points with Localized Loss*, arXiv:2601.09628 (2026), https://arxiv.org/abs/2601.09628.
3. P. L. Krapivsky, J. M. Luck, K. Mallick, *Survival of classical and quantum particles in the presence of traps*, arXiv:1311.6298 (2013), https://arxiv.org/abs/1311.6298.
4. M. Varbanov, H. Krovi, T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (2008), https://arxiv.org/abs/0803.3446.
5. J. S. Peter, R. Holzinger, S. Ostermann, S. F. Yelin, *Examining the quantum signatures of optimal excitation energy transfer*, arXiv:2403.00058 (2024), https://arxiv.org/abs/2403.00058.
