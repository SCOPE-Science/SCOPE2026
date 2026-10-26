# Global four-mode threshold and detuning cusp in a saturable lossy dimer

## Finding

For the normalized, passive, saturable two-resonator eigenproblem of Gu, Qu and Zhang [1], the entire detuning line admits exactly two or four distinct nonlinear eigenpairs away from the sharp fold boundaries. The distinction is decided by one explicit nonlinear-strength threshold:
\[
  g_c=\frac92\sqrt{J^2-\Gamma^2}.
\]
Here \(0<\Gamma<J\) and \(g\ge0\). For \(g\le g_c\), every real detuning has exactly two eigenpairs (modulo global phase). For \(g>g_c\), there is a unique positive fold detuning \(\delta_*(g)\), with four eigenpairs for \(|\delta|<\delta_*\), three at \(|\delta|=\delta_*\), and two outside.

The exact boundary is specified without numerical root selection. Define
\[
 F(s)=s\sqrt{\frac{J^2}{1-s^2}-\Gamma^2},\qquad
 R(x)=\frac{(9-x)^2}{2(9+x)}F'(\sqrt x),\quad 0\le x<1.
\]
For \(g>g_c\), the unique \(s_*\in(0,1)\) satisfying \(R(s_*^2)=g\) yields
\[
\delta_*(g)=\frac{2gs_*}{9-s_*^2}-F(s_*)>0.
\]
The fold half-width has the sharp cusp and large-nonlinearity asymptotics
\[
 \delta_*(g)\sim \frac{8}{27\sqrt3}
 \sqrt{\frac{\sqrt{J^2-\Gamma^2}}{7J^2+2\Gamma^2}}\,(g-g_c)^{3/2}
 \quad(g\downarrow g_c),
 \qquad \lim_{g\to\infty}\frac{\delta_*(g)}g=\frac14.
\]
In particular, four modes occur even though \(J>\Gamma\) precludes the underlying linear exceptional point; nonlinear mode folds must not be confused with matrix exceptional points.

## Assumptions and scope

Fix real \(J,\Gamma,g,\delta\) with \(0<\Gamma<J\), \(g\ge0\), and \(\delta\in\mathbb R\). A nonlinear eigenpair is \((\mu,\psi)\in\mathbb C\times\mathbb C^2\) with \(\|\psi\|_2=1\), modulo \(\psi\sim e^{i\vartheta}\psi\), satisfying
\[
 H(\psi)\psi=\mu\psi,\qquad
 H(\psi)=\begin{pmatrix}
 \delta-2i\Gamma+\dfrac{g}{1+|\psi_1|^2}&J\\
 J&-\delta+\dfrac{g}{1+|\psi_2|^2}
 \end{pmatrix}.
\]
The eigenvalue \(\mu\) may be complex. This is a fixed-norm nonlinear spectral problem, not a statement about norm-preserving trajectories of the lossy evolution. Both components of \(\psi\) are necessarily nonzero because \(J>0\).

## Proof

**1. Parametrize every eigenpair.** Fix the gauge \(\psi_1>0\) real, and let \(s=|\psi_1|^2-|\psi_2|^2\in(-1,1)\), \(\psi_1=\sqrt{(1+s)/2}\), \(\psi_2=\sqrt{(1-s)/2}\,e^{i\phi}\). Subtracting the imaginary parts of the two scalar eigenvalue equations yields
\[
 \sin\phi=\frac\Gamma J\sqrt{1-s^2}.
\]
Since \(\Gamma<J\), there are precisely two possible phases, indexed by \(\sigma\in\{-1,1\}\), with
\[
 \cos\phi=\sigma\sqrt{1-\frac{\Gamma^2(1-s^2)}{J^2}}.
\]
Equality of real parts is then exactly
\[
 \delta=\delta_\sigma(s):=
 \frac{2gs}{9-s^2}+\sigma s\sqrt{\frac{J^2}{1-s^2}-\Gamma^2}.
 \tag{1}
\]
Conversely, every \(s\in(-1,1)\) satisfying (1), together with its specified phase, satisfies both scalar equations with the same eigenvalue
\[
 \mu=\delta+\frac{2g}{3+s}
 +J\sqrt{\frac{1-s}{1+s}}\cos\phi-i\Gamma(1+s).
\]
Thus counting the roots of (1) for the two signs counts all eigenpairs, without loss or extraneous roots (also at \(s=0\)).

**2. Monotonicity.** The positive branch
\[
 \delta_+(s)=\frac{2gs}{9-s^2}+F(s)
\]
is strictly increasing from \(-\infty\) to \(+\infty\), and therefore contributes one eigenpair for every detuning. For the negative branch,
\[
 \delta_-'(s)=\frac{2(9+s^2)}{(9-s^2)^2}\,[g-R(s^2)].\tag{2}
\]
Set \(\Delta=\sqrt{J^2-\Gamma^2}>0\), \(x=s^2\) and \(u=\Gamma^2/\Delta^2\). The positive derivative \(B(x)=F'(\sqrt x)\) is
\[
 B(x)=\frac{\Delta[1+ux(2-x)]}{(1-x)^{3/2}\sqrt{1+ux}}.
\]
An exact logarithmic derivative is
\[
 \frac{d}{dx}\log B(x)=\frac{(1+u)(ux^2+2ux+3)}{2(1-x)(1+ux)[1+ux(2-x)]}.
\]
It strictly exceeds \(1/[2(1-x)]\), because the corresponding numerator difference is
\[
 u^2x(x^2-x+2)+u(2x^2-x+3)+2>0.
\]
Meanwhile
\[
 \frac{d}{dx}\log\frac{9+x}{(9-x)^2}=
 \frac1{9+x}+\frac2{9-x}\le\frac{13}{36}<\frac12.
\]
Consequently \(R\) is strictly increasing on \([0,1)\), from \(R(0)=9\Delta/2=g_c\) to \(+\infty\). This proves that (2) has no zero for \(g<g_c\), just one zero at \(s=0\) for \(g=g_c\), and precisely two symmetric simple zeros \(\pm s_*\) for \(g>g_c\).

**3. Count globally, including boundaries.** The negative branch is odd and tends to \(+\infty\) as \(s\to-1\) and \(-\infty\) as \(s\to1\). If \(g\le g_c\), it is strictly decreasing and contributes exactly one root at every detuning. If \(g>g_c\), it has exactly one local minimum \(-\delta_*(g)\) at \(-s_*\) and one local maximum \(\delta_*(g)>0\) at \(s_*\). Horizontal-line intersections of this complete three-monotonicity-interval graph number three, two, or one depending on whether \(|\delta|<\delta_*\), \(|\delta|=\delta_*\), or \(|\delta|>\delta_*\). Adding the one positive-branch root proves the theorem. At a fold the repeated scalar root represents only one distinct eigenpair.

**4. Calculate the cusp coefficient.** Put \(g=g_c+\varepsilon\), with fixed \(J>\Gamma>0\), and expand (1) on its negative branch at \(s=0\):
\[
 \delta_-(s)=\frac{2\varepsilon}{9}s
 -\frac{7J^2+2\Gamma^2}{18\Delta}s^3
 +O(\varepsilon s^3+s^5).
\]
The unique positive fold satisfies
\[
 s_*\sim\frac2{\sqrt3}\sqrt{\frac{\Delta\varepsilon}{7J^2+2\Gamma^2}}.
\]
Substituting in the cubic normal form gives precisely the stated \(3/2\) cusp coefficient. For \(g\to\infty\), \(R(s_*^2)=g\) forces \(s_*\to1\). Equation (2) shows \(F(s_*)/g\to0\), while \(2s_*/(9-s_*^2)\to1/4\); hence \(\delta_*/g\to1/4\).

## Verification

The standalone `CHECK.py` reconstructs the two-component complex nonlinear eigenvalue equations from roots of (1) for 100 deterministic pseudorandom parameter/detuning samples. It verifies the exact logarithmic-derivative identity symbolically, the cubic coefficient, root counts at zero detuning on either side of the threshold, and the fold \(3/2\)-asymptotic against direct bisection. Execute using `python CHECK.py` with Python 3 and SymPy. The proof above, not the finite numerical sample, establishes the global quantifiers.

For example, at \(J=1\), \(\Gamma=1/2\), \(g=5\), the threshold is \(g_c=9\sqrt3/4\approx3.8971143\) and the fold half-width is \(\delta_*\approx0.06486841\). The exact mode count is four for \(|\delta|<\delta_*\) and two for \(|\delta|>\delta_*\).

## Relationship to prior work

Gu, Qu and Zhang [1] introduced this exact normalized saturable lossy dimer, derived an eighth-degree population-imbalance polynomial, identified exceptional-point locations and showed numerical examples with multiple nonlinear eigenvectors. Their focus is the linear-EP section \(J=\Gamma\); the present theorem instead assumes the strict non-EP regime \(J>\Gamma\), counts *all* normalized complex-eigenvalue stationary modes at *all* detunings, and proves the exact multi-mode onset and fold widths. The implicit eighth-degree equation alone does not state or establish the global monotonicity and sharp mode-count partition proved here.

Related studies of Kerr nonlinear dimers [2] and saturable nonlinear transmission through side-coupled chains [3] concern different nonlinearities or scattering questions. A recent general catastrophe-theoretic study [4] treats universal local topology near nonlinear exceptional points; its qualitative cusp vocabulary does not yield this specific global non-EP threshold or the explicit cusp coefficient. An additional balanced-gain/loss saturable-dimer study [5] discusses equilibrium families; its potentially relevant mode-count formulas warrant further direct comparison. The present claim is restricted to normalized eigenpairs, not dynamical stability, equilibrium trajectories, or exceptional-point classification.

## Limitations

The count holds for the equal saturable coefficients, the particular denominator \(1+|\psi_j|^2\), positive \(g\), and \(0<\Gamma<J\). The limit \(J\downarrow\Gamma\) is singular and is not covered uniformly. A fold of the nonlinear eigenvector equation does not imply a linear-matrix exceptional point. No claims are made about dynamical stability, experimental reachability, or completeness of the literature beyond the cited comparisons. An equivalent implicit branch classification in independent nonlinear-optics literature cannot be excluded without further full-text comparison.

## References

[1] Q. Gu, C. Qu, Y. Zhang, *Adjusting exceptional points using saturable nonlinearities*, arXiv:2402.15792 (first posted 2024-02-24); Results in Physics 61 (2024), 107736. https://arxiv.org/abs/2402.15792

[2] J. Pickton and H. Susanto, *Integrability of PT-symmetric dimers*, Phys. Rev. A 88 (2013), 063840. https://doi.org/10.1103/PhysRevA.88.063840

[3] T. F. Assunção, E. M. Nascimento, M. L. Lyra, *Nonreciprocal transmission through a saturable nonlinear asymmetric dimer*, Phys. Rev. E 90 (2014), 022901. https://doi.org/10.1103/PhysRevE.90.022901

[4] *Universal topology of exceptional points in nonlinear non-Hermitian systems*, Nature Communications 17 (2026), article 7051. https://doi.org/10.1038/s41467-026-72854-2

[5] S. M. Liberona-Urquieta, F. R. Humire, R. Riveros-Ávila, *Gain-loss deformation of equilibrium families in a PT-symmetric saturable optical dimer*, Physica Scripta 101 (2026), 185202. https://doi.org/10.1088/1402-4896/ae6426
