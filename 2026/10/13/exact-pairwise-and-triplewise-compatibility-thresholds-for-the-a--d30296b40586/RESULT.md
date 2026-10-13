# Exact pairwise and triplewise compatibility thresholds for the amplitude-damped Pauli triad

## Finding
For the standard zero-temperature qubit amplitude-damping channel with survival parameter \(q\in[0,1]\), the three binary measurements obtained by applying the adjoint channel to the sharp Pauli \(X\), \(Y\), and \(Z\) measurements have the following **complete compatibility hierarchy**:
\[
\begin{aligned}
\text{each of the three pairs is jointly measurable}&\iff q\le \tfrac12,\\
\text{all three are jointly measurable}&\iff q\le\tfrac13.
\end{aligned}
\]
Consequently, for every \(1/3<q\le1/2\), all three pairs admit joint POVMs but no eight-outcome joint POVM for the full triple exists. For a Markovian damping semigroup \(q=e^{-\Gamma t}\), this is exactly the nonempty interval \(\ln 2/\Gamma\le t<\ln 3/\Gamma\). The thresholds include equality.

## Assumptions and scope
Let \(X,Y,Z\) be the Pauli matrices, \(I\) the identity, \(P=|1\rangle\langle1|=(I-Z)/2\), and \(r=\sqrt q\). Use the Kraus operators
\[
K_0=|0\rangle\langle0|+r|1\rangle\langle1|,\qquad K_1=\sqrt{1-q}|0\rangle\langle1|.
\]
Write \(\Phi_q^*(B)=K_0^\dagger B K_0+K_1^\dagger B K_1\). The binary effects for outcomes \(a,b,z\in\{+1,-1\}\) are
\[
A_a=\frac{I+a\sqrt q X}{2},\quad
B_b=\frac{I+b\sqrt q Y}{2},\quad
C_z=\frac{I+z((1-q)I+qZ)}{2}.
\]
In particular, \(C_{-1}=qP\) and \(C_{+1}=Z_+=I-qP\). Compatibility means a family of positive semidefinite effects with the prescribed marginals, not a sequential or restricted measurement scheme. The claim is about the specified three observables, **not** all POVMs and not whether the channel is generally incompatibility breaking.

## Proof
**Pair \(X,Y\).** If positive effects \(H_{ab}\) jointly realize \(A\) and \(B\), then \(\sum_{a,b}aH_{ab}=\sqrt q X\) and \(\sum_{a,b}bH_{ab}=\sqrt q Y\). Therefore
\[
4\sqrt q=\sum_{a,b}\operatorname{Tr}[H_{ab}(aX+bY)]
\le\sqrt2\sum_{a,b}\operatorname{Tr}H_{ab}=2\sqrt2,
\]
since each \(aX+bY\) has largest eigenvalue \(\sqrt2\). Hence \(q\le1/2\). Conversely the effects \(H_{ab}=(I+a\sqrt q X+b\sqrt q Y)/4\) are positive exactly when \(q\le1/2\) and have the correct marginals.

**Pairs \(X,Z\) and \(Y,Z\).** If an \(X,Z\) joint POVM exists, its two effects in the \(z=-1\) branch must be \(tP\) and \((q-t)P\), with \(0\le t\le q\), because their sum is the rank-one effect \(qP\). The remaining effects are \(A_{+1}-tP\) and \(A_{-1}-(q-t)P\). Positivity of their determinants gives respectively
\[
t\le\frac{1-q}{2},\qquad t\ge\frac{3q-1}{2},
\]
which can simultaneously hold only if \(q\le1/2\). For every \(q\le1/2\) the explicit joint effects
\[
F_{a,+1}=\frac{Z_++a\sqrt q X}{2},\qquad
F_{a,-1}=\frac q2 P
\]
are positive and have the required marginals; the upper-block determinants are \((1-2q)/4\). Replacing \(X\) with \(Y\) establishes the identical result for \(Y,Z\).

**The triple, sufficiency.** For each \(a,b\in\{\pm1\}\), set
\[
G_{a,b,+1}=\frac{Z_++a\sqrt q X+b\sqrt q Y}{4},\qquad
G_{a,b,-1}=\frac q4P.
\]
These eight effects sum to \(I\), and sums over any two indices give precisely \(A_a,B_b,C_z\). The smallest eigenvalue of every \(G_{a,b,+1}\) is nonnegative exactly when its determinant \((1-3q)/16\) is nonnegative (the diagonal entries are nonnegative). Thus the construction works for \(q\le1/3\).

**The triple, necessity.** Let \(0\le q<1\), and suppose some eight-outcome joint POVM exists. Average it over the four rotations by multiples of \(\pi/2\) around \(Z\), while cyclically relabelling the four \((a,b)\) combinations. Such transformations preserve all three marginal POVMs, since a quarter-turn sends \(X\mapsto Y\), \(Y\mapsto-X\), and fixes \(Z\). Every effect in the \(z=-1\) branch is a nonnegative multiple of the rank-one projector \(P\). The average consequently makes **all four** such effects equal to \(qP/4\).

The four remaining effects \(G_{a,b,+1}\) sum to the strictly positive operator \(Z_+=I-qP\) and have marginals
\[
\sum_bG_{a,b,+1}=\frac{Z_++a\sqrt q X}{2},\qquad
\sum_aG_{a,b,+1}=\frac{Z_++b\sqrt q Y}{2}.
\]
Congruence by \(Z_+^{-1/2}\) therefore turns these four operators into a joint POVM of **unbiased**, orthogonal Pauli effects with common sharpness \(\eta=\sqrt{q/(1-q)}\). Indeed, \(Z_+^{-1/2}XZ_+^{-1/2}=X/\sqrt{1-q}\), and the analogous identity holds for \(Y\). The first paragraph's trace witness, with \(\sqrt q\) replaced by \(\eta\), forces \(\eta\le1/\sqrt2\). Equivalently, \(3q\le1\). At \(q=1\), the sharp \(X,Y\) pair is incompatible, so the triple is also incompatible. This proves necessity over the entire closed domain.

## Verification
Run `python verify.py` with SymPy. It checks the Heisenberg Kraus identities, symbolic normalization and every marginal of the eight proposed effects, all determinant identities, the equatorial pair construction, and an exact rational point \(q=2/5\) inside the pairwise-only interval. The output is `VERIFY_OK symbolic_marginals=passed Kraus_dual=passed pair_and_triple_determinants=passed rational_Specker_witness=2/5`. These checks corroborate the proof; the global nonexistence statements follow from the inequalities and symmetry reduction above, not finite sampling.

## Relationship to prior work
Heinosaari–Kiukas–Reitzner–Schultz (2015) introduce incompatibility-breaking channels and analyze white-noise thresholds, including the distinction between two- and three-measurement breaking. The present statement instead classifies one physically distinguished triad under **nonunital amplitude damping**. Andrejic–Kunjwal (2020) construct qubit Specker structures and give general sufficient conditions for biased POVMs, not the damping-specific sharp two-threshold classification here. Kiukas–Lahti–Pellonpää (2023) study critical times under open-system dynamics, with explicit examples for qubit **dephasing** and pair compatibility, not this biased amplitude-damped triple. Kumari–Mukherjee–Prabhu (2026) analyze contextuality-breaking witnesses under amplitude damping rather than the exact joint-POVM threshold of the three Heisenberg images. Chitambar–Zhang (2026) develop a broader zonoid framework for dichotomic compatibility; without complete accessible text, equivalent coverage cannot be excluded.

## Limitations
The result does not claim the channel is \(2\)-incompatibility breaking or \(3\)-incompatibility breaking for **all** measurement collections. It treats only the sharp input Pauli Cartesian triad under zero-temperature qubit damping. Similar numerical thresholds may occur for unrelated unital noise without implying operational equivalence. A broad 2026 zonoid analysis and other differently parametrized compatibility formulas present unresolved literature-overlap risks.

## References
1. T. Heinosaari, J. Kiukas, D. Reitzner, J. Schultz, *Incompatibility breaking quantum channels* (2015), arXiv:1504.05768, https://arxiv.org/html/1504.05768v2 (first public 2015-04-22 UTC).
2. N. Andrejic and R. Kunjwal, *Joint measurability structures realizable with qubit measurements: incompatibility via marginal surgery* (2020), arXiv:2003.00785, https://arxiv.org/pdf/2003.00785.
3. J. Kiukas, P. Lahti and J.-P. Pellonpää, *Joint measurability in Lindbladian open quantum systems* (2023), arXiv:2309.06040, https://arxiv.org/html/2309.06040v1.
4. S. Kumari, S. Mukherjee and R. Prabhu, *Connection between the contextuality breaking and incompatibility breaking qubit channels* (2026), arXiv:2604.04899, https://arxiv.org/html/2604.04899v1.
5. E. Chitambar and Y. Zhang, *Destroying and Preserving Measurement Incompatibility over a Quantum Channel* (2026), arXiv:2610.06642, https://arxiv.org/abs/2610.06642 (abstract-level comparison only).
