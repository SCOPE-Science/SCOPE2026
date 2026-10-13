# A three-region noise-budget phase diagram for GHZ phase metrology

## Finding

Let \(n\ge 2\), and subject an \(n\)-qubit GHZ state to independent, possibly unequal, zero-temperature amplitude-damping channels with decay probabilities \(p_1,\ldots,p_n\in[0,1]\). After damping, encode a **common** phase with \(U_\phi=\exp(-i\phi J_z)\), where \(J_z=\frac12\sum_{j=1}^n Z_j\). Put \(S=\sum_jp_j\), \(Q=\prod_j(1-p_j)\), and \(R=\prod_jp_j\). The exact symmetric-logarithmic-derivative quantum Fisher information (QFI) is
\[
F(\boldsymbol p)=\frac{2n^2Q}{1+Q+R}.
\]
For each fixed total damping budget \(0\le S\le n\), this QFI is Schur-concave in the decay-probability vector, and strictly so for nontrivial majorization comparisons between vectors with all coordinates in the open unit interval. It has the **unique maximum** at \(p_1=\cdots=p_n=S/n\):
\[
F_{\max}(S)=\frac{2n^2(1-S/n)^n}{1+(1-S/n)^n+(S/n)^n}.
\]
The minimum is
\[
F_{\min}(S)=
\begin{cases}
2n^2(1-S)/(2-S),&0\le S<1,\\
0,&1\le S\le n.
\end{cases}
\]
For \(0<S<1\), the minimizers are precisely permutations of \((S,0,\ldots,0)\). For \(1\le S\le n\), the minimizers are precisely vectors with at least one entry equal to \(1\).

Against the **ideal separable shot-noise reference** \(F=n\), define
\[
S_{\mathrm{all}}=\frac{2n-2}{2n-1},
\]
and define \(S_{\mathrm{some}}\in(0,n)\) as the unique solution of
\[
(2n-1)(1-S_{\mathrm{some}}/n)^n
=1+(S_{\mathrm{some}}/n)^n.
\]
Then \(0\le S<S_{\mathrm{all}}\) guarantees \(F>n\) for **every** damping allocation; \(S_{\mathrm{all}}\le S<S_{\mathrm{some}}\) admits **some but not all** allocations with \(F>n\); and \(S\ge S_{\mathrm{some}}\) permits **none**. At the first boundary, a maximally concentrated allocation has \(F=n\), and at the second, the uniform allocation has \(F=n\). Furthermore,
\[
S_{\mathrm{some}}=\log(2n-1)
-\frac{\log^2(2n-1)}{2n}
+O\!\left(\frac{\log^3 n}{n^2}\right)
\quad(n\to\infty).
\]
The final asymptotic is a refinement of the previously known homogeneous-loss threshold, not an independently claimed discovery.

## Assumptions and scope

Take \(|\mathrm{GHZ}_n\rangle=(|0\rangle^{\otimes n}+|1\rangle^{\otimes n})/\sqrt2\). The local channels have Kraus operators \(K_{0,j}=|0\rangle\langle0|+\sqrt{1-p_j}|1\rangle\langle1|\) and \(K_{1,j}=\sqrt{p_j}|0\rangle\langle1|\). Each acts once, independently, **before** the encoding of a single common unknown phase \(\phi\). The QFI concerns that fixed phase direction and is not optimized over input states, encoding directions, measurements, interrogation time, or error correction. The total-loss constraint \(S\) is the sum of probabilities, not the sum of physical damping rates. The reference \(F=n\) is the ideal pure-product state SQL for the specified generator, rather than a recalibrated noisy-local-sensor benchmark.

A vector \(\boldsymbol p\) majorizes \(\boldsymbol q\) when they have equal sum and the sorted partial sums of \(\boldsymbol p\) dominate those of \(\boldsymbol q\). Schur-concavity means that \(\boldsymbol p\) majorizing \(\boldsymbol q\) implies \(F(\boldsymbol p)\le F(\boldsymbol q)\). Strictness is asserted only in the open cube.

## Proof

**Phase-sensitive block.** Applying the Kraus operators to the GHZ density matrix, all matrix elements except the coherence between \(|0^n\rangle\) and \(|1^n\rangle\) become diagonal in the computational basis. The unnormalized corner block on their span is
\[
B=\frac12\begin{pmatrix}1+R&\sqrt Q\\\sqrt Q&Q\end{pmatrix},
\qquad \operatorname{tr}B=\frac{1+Q+R}{2}.
\]
All other blocks commute with \(J_z\) and carry zero QFI for the common phase. The two distinguished basis vectors have \(J_z\)-eigenvalues \(n/2\) and \(-n/2\). Applying the spectral SLD identity (or solving the two-by-two SLD equation for the corner block) gives
\[
F=\frac{4n^2|B_{01}|^2}{\operatorname{tr}B}
=\frac{2n^2Q}{1+Q+R}.
\]
The formula extends by continuity to all channel endpoints, including rank-deficient cases.

**Two-coordinate smoothing.** Fix all but a pair of damping probabilities \(a,b\), let \(s=a+b\), \(t=ab\), \(C=\prod_{k\ne i,j}(1-p_k)\), \(D=\prod_{k\ne i,j}p_k\). On the open cube \(C>0\), with \(Q=C(1-s+t)\) and \(R=Dt\),
\[
\frac{2n^2}{F}=1+\frac{1+Dt}{C(1-s+t)},
\qquad
\frac{\partial}{\partial t}\frac{1+Dt}{C(1-s+t)}
=\frac{D(1-s)-1}{C(1-s+t)^2}<0.
\]
The last inequality holds because \(0<D<1\) for \(n>2\), while for \(n=2\) we have \(D=1\) but \(s>0\). Replacing \((a,b)\) by a more equal pair at fixed \(s\) increases \(t\), hence strictly increases QFI. Elementary finite sequences of such transfers characterize majorization, proving Schur-concavity and interior strictness. Endpoint weak inequalities follow by continuity.

**Global extrema.** Every vector of sum \(S\) majorizes the uniform vector, so smoothing proves that only the uniform vector maximizes QFI when \(0<S<n\); boundary values \(S=0,n\) are singleton feasible sets. If \(0\le S<1\), the concentrated vector \((S,0,\ldots,0)\) majorizes all feasible vectors and has \(Q=1-S\), \(R=0\). Any nontrivial splitting of its positive component strictly increases QFI because it leaves all decay probabilities below one and \(C>0\); this proves the stated complete set of minimizers. If \(S\ge1\), a feasible allocation can put one probability at one and has \(Q=0\), \(F=0\). Conversely a zero QFI entails \(Q=0\), hence at least one probability equals one.

**Three SQL regions.** For \(0\le S<1\), \(F_{\min}(S)>n\) is equivalent to \(2n(1-S)>2-S\), i.e. \(S<S_{\mathrm{all}}\). For \(S\ge1\), the minimum is already zero. The maximum exceeds \(n\) exactly when \((2n-1)(1-S/n)^n>1+(S/n)^n\). Its left side is strictly decreasing and its right side increasing in \(S\in(0,n)\); the inequality holds at \(S=0\) and fails at \(S=n\). Therefore it has one crossover \(S_{\mathrm{some}}\), and \(S_{\mathrm{all}}<S_{\mathrm{some}}\) follows from the strict increase under smoothing of the nonuniform worst-case vector at \(S_{\mathrm{all}}>0\). The three regions and equality cases follow.

**Large-system threshold.** Set \(L_n=\log(2n-1)\). The threshold equation rewrites as
\[
n\log(1-S_{\mathrm{some}}/n)
=-L_n+\log\!\left(1+(S_{\mathrm{some}}/n)^n\right).
\]
The exact root satisfies \(S_{\mathrm{some}}=n\{1-\exp[-(L_n-\delta_n)/n]\}\), where \(\delta_n=\log[1+(S_{\mathrm{some}}/n)^n]\ge0\). This identity gives \(S_{\mathrm{some}}\le n(1-e^{-L_n/n})\le L_n\). In particular, \((S_{\mathrm{some}}/n)^n\le(L_n/n)^n=o(n^{-m})\) for any fixed \(m>0\). Taylor's theorem then gives the remainder. The leading \(\log n\) behavior is already implicit in the established homogeneous ADC formula.

## Verification

Run `python3 verify.py` with NumPy installed (verified with NumPy). The program constructs amplitude-damped density matrices using the actual local Kraus maps and computes SLD QFI independently by diagonalization, then checks pair smoothing, extremal envelopes, unique SQL threshold, and finite-size asymptotic consistency. A successful run prints `VERIFY_OK 4042 direct_density_QFI 48 majorization 1200 extrema 2750 threshold 38 asymptotics 6`. The proof, not the finite tests, establishes the all-\(n\) assertion.

## Relationship to prior work

Farokhi (2026) proves a QFI trade-off for distributed sensing with pure GHZ and other probe states, but does not consider noise allocation. Bugalho, Hassani, Omar and Markham (preprint 2024; journal 2025), especially Section 4.5 and equation (51), explicitly supply the **general inhomogeneous amplitude-damped GHZ corner matrix and QFI framework**. Thus neither that state formula nor its ordinary QFI evaluation is claimed as new here. Ma, Huang, Wang and Sun (2011), equations (24)–(27), give homogeneous amplitude-damping QFI and the leading large-register shot-noise crossover. The new claim is the **sharp majorization ordering, both global envelopes under a fixed sum of heterogeneous probabilities, and the guarantee/possible/impossible partition**; none is stated in these inspected sources. General spectral and variational quantum-metrology work on asymmetric probes does not establish this fixed-GHZ, fixed-sum ordering. Priority remains conditional on the checked literature, not certified globally.

## Limitations

The bound is on a fixed initial GHZ state, phase encoded after independent zero-temperature damping; it is not a globally optimized sensing protocol. The ideal separable benchmark does not account for the same hardware-dependent damping applied to alternative local probes. The quantity \(S\) is a mathematical sum of decay probabilities, not necessarily an experimentally transferable attenuation budget. At least one fully damped qubit destroys this specific phase-sensitive GHZ coherence; no conclusion is drawn about unrelated metrological directions. The 2024 general matrix formula makes the present allocation theorem accessible to an independent algebraic derivation, and unindexed earlier statements cannot be excluded. Independent audit has not been performed.

## References

1. F. Farokhi, “Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality,” arXiv:2605.20765, first submitted 2026-05-20. https://arxiv.org/abs/2605.20765
2. L. Bugalho, M. Hassani, Y. Omar, D. Markham, “Private and Robust States for Distributed Quantum Sensing,” arXiv:2407.21701 (first submitted 2024-07-31), Quantum **9**, 1596 (2025), Section 4.5, equation (51). https://arxiv.org/abs/2407.21701
3. J. Ma, Y.-x. Huang, X. Wang, C. P. Sun, “Quantum Fisher information of the Greenberger-Horne-Zeilinger state in decoherence channels,” Phys. Rev. A **84**, 022302 (2011), especially equations (24)–(27). https://doi.org/10.1103/PhysRevA.84.022302
4. B. Koczor, S. Endo, T. Jones, Y. Matsuzaki, S. C. Benjamin, “Variational-State Quantum Metrology,” New J. Phys. **22**, 083038 (2020), discussion of amplitude damping and inhomogeneous errors. https://doi.org/10.1088/1367-2630/ab965e
