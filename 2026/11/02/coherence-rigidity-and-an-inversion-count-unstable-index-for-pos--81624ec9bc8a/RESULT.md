# Coherence rigidity and an inversion-count unstable index for positive matrix logistic maps

## Finding

Consider the matrix-valued logistic map
\[
F_B(H)=BH(I-H)B
\]
on the real vector space of complex Hermitian \(N\times N\) matrices, where \(N\ge 1\), \(B=B^*\succ0\), and \(I\) denotes the identity. The physically relevant state interval is \(\mathcal D=\{H=H^*:0\preceq H\preceq I\}\). If \(B^2\preceq4I\), the map preserves \(\mathcal D\); the fixed-point statements below remain valid for every positive-definite \(B\), whether or not that extra bound holds.

**Theorem (complete positive fixed-point set and stability).** Let \(E_\beta\) be the orthogonal spectral projection onto the eigenspace of \(B\) with eigenvalue \(\beta>0\). Then:

1. Every fixed point \(H\in\mathcal D\) commutes with \(B\). More precisely, the complete set is
\[
\operatorname{Fix}(F_B)\cap\mathcal D
=\left\{\sum_{\beta>1}(1-\beta^{-2})P_\beta:\ P_\beta=P_\beta^*=P_\beta^2,\quad 0\preceq P_\beta\preceq E_\beta\right\}.
\]
For a gain eigenvalue \(\beta>1\) of multiplicity \(d_\beta\), its rank-\(k_\beta\) fixed-point component is the complex Grassmannian \(\mathrm{Gr}(k_\beta,d_\beta)\); the complete strata are products of these components. No off-eigenspace coherent fixed point exists, even though general trajectories need not commute with \(B\).

2. Let \(\beta_i\) and \(h_i\) be joint eigenvalues of \(B\) and a fixed point \(H\), counting multiplicity. The derivative on the \(N^2\)-dimensional **real Hermitian** state space has multipliers
\[
\lambda_{ii}=\beta_i^2(1-2h_i),\qquad
\lambda_{ij}=\beta_i\beta_j(1-h_i-h_j)\quad(i<j),
\]
where each \(\lambda_{ij}\) for \(i<j\) occurs twice as a real eigenvalue (real and imaginary off-diagonal modes).

3. Suppose \(B\) has simple spectrum and its squared gains obey \(1<a_1<\cdots<a_N<3\), where \(a_i=\beta_i^2\). Then there are exactly \(2^N\) isolated positive-semidefinite fixed points, indexed by \(S\subseteq\{1,\ldots,N\}\):
\[
H_S=\sum_{i\in S}(1-a_i^{-1})E_{\beta_i}.
\]
Every one is hyperbolic. Set \(m=N-|S|\). The dimension of its expanding eigenspace is exactly
\[
\boxed{\quad
\nu(H_S)=m^2+2\#\{(i,j):i\in S,\ j\notin S,\ a_j>a_i\}
\quad}
\]
The remaining \(N^2-\nu(H_S)\) real directions contract. The unique hyperbolic sink is the full-support point \(H_{\{1,\ldots,N\}}=I-B^{-2}\), and the zero matrix is a source. Thus two fixed points with the same rank can have different unstable dimensions, determined by an exact gain-order inversion count.

4. More generally, for arbitrary positive-definite \(B\), a **hyperbolic sink exists if and only if** every eigenvalue \(a\) of \(B^2\) lies in \((0,3)\setminus\{1\}\). When this holds, it is unique and equals
\[
H_*=(I-B^{-2})_+,
\]
where the positive part is defined spectrally. The bound \(3\) is sharp: if any squared gain reaches \(3\), the corresponding active diagonal multiplier reaches \(-1\); if it exceeds \(3\), every fixed point has an expanding direction. At squared gain \(1\), every fixed point has a neutral diagonal multiplier \(+1\).

## Assumptions and scope

The state space is the vector space of all complex Hermitian matrices, so stability refers to every Hermitian perturbation, including noncommuting and imaginary off-diagonal modes, not merely to diagonal perturbations. Positive fixed points are required to satisfy \(0\preceq H\preceq I\); this includes rank-deficient states. For the finite-state-space dynamical interpretation, one may impose \(B^2\preceq4I\), because \(0\preceq H(I-H)\preceq I/4\) on \(\mathcal D\). The classification itself does not require that bound. A hyperbolic sink means that all derivative eigenvalues have modulus strictly below one; it does not imply global attraction. The unstable dimension counts real derivative eigenvectors with eigenvalues of modulus strictly above one.

## Proof

**Step 1: positivity forces fixed-point commutation.** Fix \(H\in\mathcal D\) with \(H=BH(I-H)B\), and write \(C=B^{-1}\succ0\). Congruence gives
\[
CHC=H-H^2.
\]
The left side has rank \(\operatorname{rank}H\), while the right side has nonzero eigenvalues \(h(1-h)\) for the nonzero eigenvalues \(h\) of \(H\). Therefore \(H\) cannot have eigenvalue \(1\). Let \(\mathcal S=\operatorname{ran}H\). Both sides have range \(\mathcal S\), but \(\operatorname{ran}(CHC)=C\mathcal S\). Hence \(C\mathcal S=\mathcal S\). Because \(C\) is Hermitian, the orthogonal complement \(\mathcal S^\perp\) is invariant too.

On \(\mathcal S\), the restriction \(H_{\mathcal S}\) is strictly positive and has eigenvalues less than one. Put \(Y=H_{\mathcal S}^{1/2}C_{\mathcal S}H_{\mathcal S}^{1/2}\succ0\). The congruence identity implies
\[
Y^2=H_{\mathcal S}^2(I-H_{\mathcal S}).
\]
The unique positive square root of the right side is \(H_{\mathcal S}(I-H_{\mathcal S})^{1/2}\); consequently \(C_{\mathcal S}=(I-H_{\mathcal S})^{1/2}\). In particular \(C\), hence \(B\), commutes with \(H\) on \(\mathcal S\), and the commutator vanishes on its orthogonal complement. Moreover \(H_{\mathcal S}=I-B_{\mathcal S}^{-2}\succ0\), forcing active gains \(\beta>1\). Spectral decomposition of the commuting Hermitian pair gives the displayed formula with arbitrary orthogonal projections \(P_\beta\) supported in each gain eigenspace. Conversely, each such matrix satisfies the fixed-point equation directly. Choosing the rank of each \(P_\beta\) yields the Grassmannian strata.

**Step 2: complete derivative spectrum.** Differentiating the quadratic map in a Hermitian direction \(E\) gives
\[
DF_B(H)[E]=B(E-HE-EH)B.
\]
Diagonalize \(B\) and \(H\) jointly. Matrix units on the diagonal are eigenvectors with multiplier \(\beta_i^2(1-2h_i)\). Each complex off-diagonal pair supplies two real Hermitian eigenvectors, \(E_{ij}+E_{ji}\) and \(\mathrm{i}(E_{ij}-E_{ji})\), with the same real multiplier \(\beta_i\beta_j(1-h_i-h_j)\). The total real count is \(N+2\binom N2=N^2\), so this is the full spectrum, including multiplicities.

**Step 3: gain-order inversion count.** Suppose all distinct squared gains lie strictly between \(1\) and \(3\). At \(H_S\), selected diagonal multipliers are \(2-a_i\in(-1,1)\), while omitted diagonal multipliers are \(a_j>1\). If both indices are omitted, the off-diagonal multiplier is \(\sqrt{a_i a_j}>1\). If one index \(i\) is selected and the other \(j\) omitted, its multiplier equals \(\sqrt{a_j/a_i}\), and is expanding precisely when \(a_j>a_i\); the two real off-diagonal modes contribute two unstable dimensions. If both are selected, their multiplier is
\[
\psi(a_i,a_j)=\frac{a_i+a_j-a_ia_j}{\sqrt{a_i a_j}}.
\]
For \(1<a,b<3\), \(\partial_a\psi(a,b)=[a(1-b)-b]/(2a\sqrt{ab})<0\) and likewise for \(\partial_b\psi\). Since \(\psi(1,1)=1\) and \(\psi(3,3)=-1\), all selected-selected modes strictly contract. Distinct gains exclude unit-modulus selected/omitted modes. Therefore all equilibria are hyperbolic. With \(m\) omitted indices, the omitted diagonal modes and omitted/omitted pairs give \(m+2\binom m2=m^2\) unstable real directions; the selected/omitted inversions give the remaining term of the formula. Only \(S=\{1,\ldots,N\}\) has no omitted gains and therefore no unstable directions.

**Step 4: the sharp general sink criterion.** For an arbitrary spectrum in \((0,3)\setminus\{1\}\), let \(H_*\) activate every gain above one and omit every gain below one. Its diagonal multipliers have modulus below one. For two omitted gains below one, the off-diagonal multiplier is \(\sqrt{a_i a_j}<1\); for an activated gain \(a_i>1\) and omitted gain \(a_j<1\), it is \(\sqrt{a_j/a_i}<1\); for two activated gains, Step 3 gives strict contraction, including repeated gains. Thus \(H_*\) is a hyperbolic sink. Every other positive fixed point omits at least one direction with gain exceeding one, producing the expanding diagonal multiplier \(a_i>1\).

Conversely, a squared gain equal to one cannot activate any nonzero component, and its diagonal mode has multiplier \(+1\). If a squared gain \(a\ge3\) is omitted, its diagonal multiplier is \(a>1\); if activated, it is \(2-a\le-1\). At least one of these possibilities occurs at every fixed point, including with eigenspace multiplicity. Therefore no hyperbolic sink exists in either boundary or supercritical case. This proves the exact criterion.

## Verification

The standalone standard-library program `verify_matrix_logistic.py` performs independent **exact rational-arithmetic** checks of the polynomial fixed-point equation, commutation, every derivative eigendirection, and the unstable-index formula. It conjugates three distinct rational gains by a non-diagonal rational orthogonal matrix; for all eight fixed-point choices it checks all nine real mode slots. Its observed expanding dimensions, in bitmask order, are \((9,8,6,5,4,3,1,0)\), exactly matching the formula. It also verifies an off-diagonal projector within a repeated-gain eigenspace, two mixed subcritical-gain sinks, and rational supercritical/neutral gain tests. Execution requires Python 3 only, using `fractions.Fraction`, and reports `All exact rational checks passed.` The exact program is embedded alongside this document. These are finite witnesses; the classifications for all matrix sizes and gains follow from Steps 1–4, not the program.

## Relationship to prior work

Pawela and Życzkowski introduced \(H\mapsto BH(I-H)B^*\) and studied its spectral measures, graph-dependent coupling, and numerical transfer of chaos [1]. The positive-Hermitian choice \(B=B^*\succ0\) investigated here is a natural subfamily of their coupling model, but still allows noncommuting initial states. Their section on coupling and two-dimensional appendix concern numerical invariant distributions, not the complete positive fixed-point set or real-Hermitian unstable-index census derived here. Navickas and collaborators [2] studied the scalar-gain matrix map \(H\mapsto aH(I-H)\), whose fixed-point spectral projection phenomenon is a special case; the unequal positive gain eigenvalues and the inversion-dependent unstable indices do not follow merely from that scalar case. Cánovas [3] considers a different coordinate-coupled pair of scalar logistic maps. The present formula does not assert originality for the familiar scalar logistic fixed point or the general finite-dimensional linear stability test; the claimed contribution is their exact combination with noncommutative equilibrium rigidity and all-mode index counting for positive matrix coupling.

## Limitations

The theorem is limited to positive-definite **Hermitian** coupling matrices \(B\). For nonnormal or non-Hermitian coupling \(B\), the reduction \(B^{-1}HB^{-1}\) is unavailable and additional fixed-point behavior may occur. The classification concerns positive-semidefinite states with spectrum in \([0,1]\), not all indefinite Hermitian or non-Hermitian fixed points. The sink criterion is local and hyperbolic; it makes no assertion about global basins, nonlinear behavior at neutral gains \(1\) and \(3\), periodic points of higher period, or convergence of matrix spectral distributions. The gain-order index law requires simple squared gains in \((1,3)\); at repeated gains, continuous Grassmannian strata generally carry neutral modes. General matrix-equation identities or unindexed published derivations might overlap with the rigidity lemma; the inspection described in the review does not establish absolute publication priority. Independent validation has not been performed.

## References

[1] Ł. Pawela and K. Życzkowski, *Matrix logistic map: fractal spectral distributions and transfer of chaos*, arXiv:2303.06176 (first public version 2023-03-10), https://arxiv.org/abs/2303.06176 . Journal version: *Chaos* 36 (2026), 033139, DOI: 10.1063/5.0298024.

[2] Z. Navickas, R. Smidtaite, A. Vainoras, and M. Ragulskis, *The logistic map of matrices*, *Discrete and Continuous Dynamical Systems B* 16 (2011), 927–944, DOI: 10.3934/dcdsb.2011.16.927, https://www.aimsciences.org/article/doi/10.3934/dcdsb.2011.16.927 .

[3] J. S. Cánovas, *The dynamics of coupled logistic maps*, *Networks and Heterogeneous Media*, DOI: 10.3934/nhm.2023010, https://doi.org/10.3934/nhm.2023010 .
