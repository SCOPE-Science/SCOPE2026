# Discontinuous and continuous optimal-dephasing onsets in a lossy quantum trimer

## Finding

For a three-site single-excitation chain with an energy detuning only at its middle site, continuous irreversible capture at its right endpoint, and **pure dephasing only at the middle site**, minimizing the mean first-capture time over all nonnegative dephasing strengths has an exact two-regime phase diagram. The transition between a discontinuous jump to positive optimal dephasing and a continuous onset occurs at the dimensionless capture rate
\[
\kappa_\star=32^{1/4}.
\]
Specifically, write the hopping strength as the unit of energy and inverse time, let \(\kappa>0\) be the capture rate, \(\delta\in\mathbb R\) the middle-site energy detuning, and \(\gamma\geq0\) its dephasing rate. Define
\[
\delta_c^2(\kappa)=
\begin{cases}
\displaystyle\frac{3}{\kappa^2}\left(16-\kappa^2+4\sqrt{12-2\kappa^2}\right),&0<\kappa<32^{1/4},\\[2mm]
\displaystyle\frac{12}{\kappa^2-4},&\kappa\geq32^{1/4}.
\end{cases}
\]
If \(\delta^2<\delta_c^2(\kappa)\), zero dephasing is the unique global minimizer of mean capture time. If \(\delta^2>\delta_c^2(\kappa)\), the minimizer is unique and strictly positive. On the equality boundary: for \(0<\kappa<32^{1/4}\), there are **exactly two global minimizers**, zero and
\[
\gamma_c(\kappa)=\frac{4-\kappa^2+2\sqrt{12-2\kappa^2}}{2\kappa}>0;
\]
for \(\kappa\geq32^{1/4}\), zero is the unique global minimizer. Hence the optimal rate jumps by \(\gamma_c(\kappa)\) upon crossing the threshold when \(\kappa<32^{1/4}\), but approaches zero continuously at onset when \(\kappa\geq32^{1/4}\). In the positive-optimum region the unique minimizer is the largest positive root of the explicit stationary equation given below.

## Assumptions and scope

The one-excitation Hilbert space has basis \(|1\rangle,|2\rangle,|3\rangle\). The system starts in \(\rho(0)=|1\rangle\langle1|\) and evolves, before absorption, by the trace-decreasing Lindblad equation
\[
\dot\rho=-i[H,\rho]-\gamma(P_2\rho+\rho P_2-2P_2\rho P_2)-\frac\kappa2(P_3\rho+\rho P_3),
\qquad
H=\begin{pmatrix}0&1&0\\1&\delta&1\\0&1&0\end{pmatrix},
\]
where \(P_j=|j\rangle\langle j|\), \(\kappa>0\), \(\gamma\geq0\), and \(\delta\in\mathbb R\). The middle-site dephasing superoperator damps coherences touching site 2 at rate \(\gamma\) and leaves the outer-outer coherence untouched. Capture occurs only from site 3 at instantaneous rate \(\kappa\rho_{33}(t)\). Its mean time is \(T=\int_0^\infty\operatorname{tr}\rho(t)\,dt\). All statements concern this pulse-injection capture-time objective, not an equilibrium observable or a source-driven current, and no uniform-site dephasing is assumed.

The hopping normalization can be restored from physical hopping \(J>0\): replace \(\kappa,\delta,\gamma\) by the respective physical rates or energies divided by \(J\); multiply the resulting dimensionless \(T\) by \(J^{-1}\) (in units \(\hbar=1\)). The earliest archival source used for this direction was publicly available on 2012-01-25; this is a literature-context date, not a claim of publication of the present result.

## Proof

**(1) Existence of a finite capture mean.** The dissipative evolution is completely positive and trace decreasing, with \(d\operatorname{tr}\rho/dt=-\kappa\rho_{33}\leq0\). There is no nonzero invariant positive state with vanishing sink occupancy: \(\rho_{33}=0\) forces its third row and column to vanish; invariance of the \((2,3)\) entry forces \(\rho_{22}=0\); positivity then eliminates the second row and column, and invariance of the \((1,2)\) entry forces \(\rho_{11}=0\). The finite-dimensional positive semigroup consequently has no nondecaying invariant component; its survival decays exponentially. Thus the integrated density matrix \(M=\int_0^\infty\rho(t)\,dt\) exists and uniquely solves \(\mathcal L(M)=-P_1\).

**(2) Exact residence-time formula.** Put
\[
P(\gamma)=2\kappa\gamma^2+(\kappa^2+8)\gamma+2\kappa>0.
\]
Direct substitution into the nine real linear equations for \(\mathcal L(M)=-P_1\) yields
\[
M_{33}=\frac1\kappa,\quad
\operatorname{Im}M_{12}=\operatorname{Im}M_{23}=\frac12,\quad
\operatorname{Re}M_{13}=0,
\]
\[
\operatorname{Im}M_{13}=-\frac{\delta(4\gamma+\kappa)}{P},\qquad
\operatorname{Re}M_{12}=-\frac{\delta\kappa(2\gamma+\kappa)}{2P},\qquad
\operatorname{Re}M_{23}=\frac{\delta\gamma\kappa}{P},
\]
with remaining diagonal elements fixed by
\[
M_{22}=M_{33}+\delta\operatorname{Re}M_{23}+\frac{\gamma+\kappa/2}{2},\qquad
M_{11}=M_{22}+\frac\gamma2-\delta\operatorname{Re}M_{12}.
\]
These values are valid also at \(\gamma=0\), by direct substitution (no division by \(\gamma\)). Taking the trace gives the exact identity
\[
\boxed{T(\gamma;\kappa,\delta)=\frac{3\gamma}{2}+\frac{\kappa^2+6}{2\kappa}
+\frac{\delta^2\kappa(6\gamma+\kappa)}{2P(\gamma)}.}
\]
In particular, \(T(0)=(\delta^2\kappa^2+2\kappa^2+12)/(4\kappa)\), and \(T(\gamma)\to\infty\) as \(\gamma\to\infty\), so a global minimizer exists.

**(3) Exact global comparison.** Define \(S(\gamma)=\kappa^2+2\kappa\gamma-4\). Algebra gives
\[
T(\gamma)-T(0)=\frac{\gamma\left(6P(\gamma)-\delta^2\kappa S(\gamma)\right)}{4P(\gamma)}.
\]
Thus positive dephasing improves on zero dephasing precisely when \(S(\gamma)>0\) and
\[
\delta^2>G_\kappa(\gamma):=\frac{6P(\gamma)}{\kappa S(\gamma)}.
\]
On its admissible domain \(\gamma\geq0\), \(S(\gamma)>0\), the sign of the derivative of \(G_\kappa\) is the sign of
\[
K_\kappa(\gamma)=4\kappa^2\gamma^2+4\kappa(\kappa^2-4)\gamma+\kappa^4-32.
\]
If \(0<\kappa<32^{1/4}\), this upward quadratic has precisely one positive root, namely \(\gamma_c\) above, and that root lies in \(S>0\) (because \(K<0\) at any positive zero of \(S\)). Accordingly \(G_\kappa\) has a unique interior minimum at \(\gamma_c\). The stationarity relation \(P'S=2\kappa P\) reduces its value to
\[
G_\kappa(\gamma_c)=\frac{3}{\kappa^2}\left(16-\kappa^2+4\sqrt{12-2\kappa^2}\right).
\]
For \(\kappa\geq32^{1/4}\), every coefficient of \(K_\kappa\) is nonnegative and the coefficients of positive powers are strictly positive. Hence \(G_\kappa\) increases for positive \(\gamma\) and has infimum at zero, equal to \(12/(\kappa^2-4)\). This proves the threshold and all equality claims: when \(\kappa<32^{1/4}\), \(G_\kappa\) attains its minimum only at \(\gamma_c>0\), while for larger \(\kappa\) it is strictly larger than its limiting value for each \(\gamma>0\).

**(4) Uniqueness of the positive optimum.** Let \(Q(\gamma)=12\gamma^2+4\kappa\gamma+\kappa^2-4\). Direct differentiation gives
\[
T'(\gamma)=\frac{3P(\gamma)^2-\delta^2\kappa^2 Q(\gamma)}{2P(\gamma)^2}.
\]
If \(Q\leq0\) the derivative is positive. On the interval \(Q>0\), roots are exactly the solutions of
\[
\boxed{3P(\gamma)^2=\delta^2\kappa^2 Q(\gamma).}
\]
The threshold function \(3P^2/(\kappa^2Q)\) can decrease then increase but cannot have more than one local minimum: the sign of its derivative is that of \(R=2P'Q-PQ'\), while \(R'=12\kappa Q>0\). Thus \(T'\) has at most two positive roots. The larger root, whenever the mean is improved below \(T(0)\), is the sole positive local minimum and hence the unique positive global minimizer. At a coexistence threshold the same argument makes \(\gamma_c\) its sole positive local minimum. Continuity of the unique larger positive root in the parameters establishes the stated positive jump for \(\kappa<32^{1/4}\) and onset tending to zero for \(\kappa\geq32^{1/4}\). This completes all global cases.

## Verification

The attached standalone `check.py` independently builds the full complex \(9\times9\) Liouvillian on the space of matrices, solves its resolvent, verifies the seven integrated-state identities symbolically, and checks the rational survival-time formula for 96 randomly sampled positive capture/dephasing rates and real detunings. It also checks the exact global-comparison factorization and derivative identities symbolically, then numerically tests 56 threshold and coexistence configurations. The checker requires Python with SymPy, NumPy, and SciPy and is run with `python check.py`. It passed at package preparation. Neither finite numerical testing nor the symbolic checker replaces the stated algebraic proof of uniqueness.

## Relationship to prior work

Environment-assisted transport and Haken–Strobl local dephasing are established. Kassal and Aspuru-Guzik (2012), whose full open article was inspected, examine trap efficiency with **uniform dephasing at all sites** and homogeneous energies; their end-to-end no-enhancement observation does not cover middle detuning combined with selective dephasing and mean first capture. Contreras-Pulido, Bruderer, Huelga and Plenio (2014), also inspected in full, analyze a detuned linear triple quantum dot with equal dephasing on all three dots and continuous source/drain current, deriving a related dephasing-assisted transport threshold. Their published formula is not the selective-middle-site pulse-capture formula: outer-outer coherence is additionally damped in their model, and their source-driven current addresses a different objective. For example, after taking their rapid-source limit and matching each dephased link's rate, at \((\kappa,\gamma,\delta)=(1,1,2)\), the corresponding all-site mean is \(7.210526\ldots\), while the selective-middle-site mean above is \(6.076923\ldots\). This is a model and implication comparison, not a claim that only the title is different. Giusteri, Celardo and Borgonovi (2016), inspected in its public manuscript, examine a different trimer geometry, an initially subradiant state, and finite-time transfer efficiency with fluorescence and noise. Their results do not imply this exact global zero-versus-positive dephasing optimizer classification.

The newly assessed result is the sharp complete **global capture-time optimization with a discontinuous-to-continuous onset transition**, not the observation that dephasing-assisted quantum transport exists. Equivalence under another choice of terminology or an unlocated older source remains a historical-priority risk; literature/database searches cannot prove priority.

## Limitations

The theorem assumes a single excitation, a three-site **linear** chain, equal nearest-neighbor hopping, detuning confined to the middle site, phase noise acting only there, a Markovian continuous sink at site 3, and pulse injection at site 1. Generalization to uniform dephasing, multi-site noise, repeated injection, dissipation from other sites, finite-temperature environments, dephasing with memory, unequal hoppings, or longer chains is unproved. The discontinuous threshold describes a mathematical optimizer in this ideal model and does not assert a thermodynamic phase transition, laboratory accessibility of all rates, or robustness to arbitrary model perturbations. Independent audit has not been performed.

## References

1. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202 (first public version 2012-01-25), New Journal of Physics **14**, 053041 (2012). https://arxiv.org/html/1201.5202v2
2. L. D. Contreras-Pulido, M. Bruderer, S. F. Huelga and M. B. Plenio, *Dephasing-assisted transport in linear triple quantum dots*, arXiv:1407.0924 (first public version 2014-07-03), New Journal of Physics **16**, 113061 (2014). https://arxiv.org/abs/1407.0924
3. G. G. Giusteri, G. L. Celardo and F. Borgonovi, *Optimal efficiency of quantum transport in a disordered trimer*, arXiv:1603.01373 (first public version 2016-03-04), Physical Review E **93**, 032136 (2016). https://arxiv.org/abs/1603.01373
