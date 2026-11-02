# Two-defect phonon thresholds and sharp quarter-chain placement

## Finding

For every integer \(N\geq3\), take a chain of \(N\) particles with free ends and identical nearest-neighbor spring constants \(K>0\). All particles have mass \(m>0\), except particles at distinct positions \(1\leq a<b\leq N\), each of which has mass \(m'=(1-\delta)m\), where \(0<\delta<1\). The free homogeneous infinite-chain phonon-band upper edge is \(\omega_\mathrm{edge}^2=4K/m\).

Define the symmetric matrix \(B\) with indices \(i,j\in\{a,b\}\) by
\[
B_{ij}=\frac{(-1)^{i+j}(2\min(i,j)-1)[2(N-\max(i,j))+1]}{4N}.
\]
Let \(\beta_+>\beta_->0\) be its two eigenvalues, given explicitly by
\[
\beta_\pm=\frac{B_{aa}+B_{bb}\pm\sqrt{(B_{aa}-B_{bb})^2+4B_{ab}^2}}2,
\qquad \delta_\pm=\frac1{4\beta_\pm}.
\]
The number of vibrational normal modes with \(\omega^2>4K/m\), counting multiplicities, is **exactly**
\[
\boxed{\mathbf 1_{\{\delta>\delta_+\}}+\mathbf 1_{\{\delta>\delta_-\}}.}
\]
In particular, \(0<\delta_+<\delta_-<1\). When \(\delta\) equals a critical contrast, the corresponding squared frequency equals the band edge and is **not** counted as above-band.

The second-mode threshold has a sharp, placement-independent bound
\[
\boxed{\delta_-(a,b)\geq\frac2N.}
\]
Equality holds **if and only if** \(N\equiv2\pmod 4\) and the two defects are at
\[
\boxed{a=(N+2)/4,\qquad b=(3N+2)/4.}
\]
For all other lengths, the bound is strict. Nevertheless, selecting \(a\) to be any nearest integer to \((N+2)/4\), and \(b=N+1-a\), yields
\[
\frac2N\leq\min_{1\leq a<b\leq N}\delta_-(a,b)
\leq \frac{2N}{N^2-4}.
\]
Thus the best achievable two-mode onset contrast is \(2/N+O(N^{-3})\) as \(N\to\infty\), with exact attainment along lengths congruent to two modulo four.

## Assumptions and scope

Number the sites from \(1\) to \(N\). The springs all obey the same linear Hooke law and no site is pinned to a substrate. The ends are **both free** (not fixed, periodic, or mixed). There are exactly two equal light-mass defects. The underlying spring matrix is the path Laplacian \(L_N\), whose diagonal entries are \(1\) at the ends and \(2\) elsewhere, and whose nearest-neighbor off-diagonal entries are \(-1\).

Write \(P=e_ae_a^{\mathsf T}+e_be_b^{\mathsf T}\) and \(M_\delta=I-\delta P\). The normal-mode problem is \(L_Nu=E M_\delta u\), with \(E=m\omega^2/K\). All mass eigenvalues are strictly positive in the stated domain. The comparison threshold \(E=4\) is the upper edge of the infinite *homogeneous* monatomic chain; it is not the largest eigenvalue of the homogeneous finite chain, which is strictly smaller than \(4\). The term **above-band** always refers to \(E>4\).

## Proof

**1. Rank-two inertia reduction.** The real symmetric positive matrix \(M_\delta\) gives an ordinary symmetric eigenproblem after conjugation by \(M_\delta^{-1/2}\). Sylvester's inertia law therefore identifies the number of generalized eigenvalues \(E>4\) with the positive inertia of
\[
H_\delta=L_N-4M_\delta=-(4I-L_N)+4\delta P.
\]
Set \(T=4I-L_N\). The homogeneous free-chain eigenvalues are \(2-2\cos(k\pi/N)\), for \(k=0,\ldots,N-1\), all strictly below \(4\); hence \(T\) is positive definite. Congruence by \(T^{-1/2}\) converts \(H_\delta\) to
\[
-I+4\delta T^{-1/2}PT^{-1/2}.
\]
The only nonzero eigenvalues of \(T^{-1/2}PT^{-1/2}\) coincide, with multiplicity, with those of the two-by-two compression \(B=(e_i^{\mathsf T}T^{-1}e_j)_{i,j\in\{a,b\}}\). Thus precisely one positive direction emerges when \(4\delta\beta_+>1\) and the second when \(4\delta\beta_->1\). At equality the corresponding direction is null, proving the strict inequalities in the stated count.

**2. Explicit boundary Green function.** Conjugate \(T\) by \(S=\operatorname{diag}((-1)^i)_{i=1}^N\). The resulting matrix has diagonal \(3\) at the two endpoints, \(2\) in the interior and nearest-neighbor off-diagonal entries \(-1\). Its Green kernel is
\[
(S T S)^{-1}_{ij}=\frac{(2\min(i,j)-1)[2(N-\max(i,j))+1]}{4N}.
\]
Indeed, as a function of \(i\), the numerator is affine separately to the left and right of \(j\), satisfies the endpoint relations \(3g_1-g_2=0\) and \(3g_N-g_{N-1}=0\) off the source, and has the unit discrete derivative jump at \(i=j\). The formula remains valid when the source is at an endpoint, where the corresponding endpoint equation has unit right side. Conjugating back supplies the displayed \(B_{ij}\). As a principal compression of \(T^{-1}\), \(B\) is positive definite; since its off-diagonal element is never zero, \(\beta_+>\beta_->0\).

**3. Both thresholds are physically attainable.** At \(\delta=1\), consider the auxiliary symmetric matrix \(H_1=L_N-4(I-P)\) (only as the continuous endpoint of the matrix family, not as a physical zero-mass normal-mode model). The quadratic form of \(H_1\) on vectors supported at \(\{a,b\}\) is exactly that of the principal two-site submatrix of \(L_N\), and is strictly positive. This follows from the connected path and the nonempty complement: the energy \(\sum_{i=1}^{N-1}(u_i-u_{i+1})^2\) cannot vanish for a nonzero vector supported on only two sites when \(N\ge3\). Hence \(H_1\) has two positive eigenvalues. By the rank-two reduction, \(4\beta_->1\), so \(\delta_-<1\). Trivially \(0<\delta_+<\delta_-\).

**4. Sharp optimal placement.** Let
\[
x=\frac{2a-1}{2N},\quad y=\frac{2(N-b)+1}{2N},\quad z=\frac{b-a}{N}.
\]
These numbers are strictly positive and satisfy \(x+y+z=1\). Multiplying \(B\) by the sign of its off-diagonal, without changing its spectrum, yields
\[
\widetilde B=N\begin{pmatrix}x(1-x)&xy\\xy&y(1-y)\end{pmatrix}.
\]
Let \(s=x+y\in(0,1)\). The Rayleigh quotient at \((1,-1)/\sqrt2\) is exactly
\[
\frac{N}{2}[x(1-x)+y(1-y)-2xy]
=\frac{N}{2}s(1-s)\leq \frac N8.
\]
Consequently \(\beta_-\leq N/8\), proving \(\delta_-\geq2/N\). Equality requires \(s=1/2\) and requires \((1,-1)\) to be an eigenvector for the minimum eigenvalue. The latter is equivalent to \(x(1-x)=y(1-y)\). Since \(x+y=s<1\), this forces \(x=y=1/4\). Conversely this configuration gives eigenvalues \(N/4\) and \(N/8\), so it does achieve equality. The positions are then \(a=(N+2)/4\), \(b=(3N+2)/4\), both integers precisely for \(N\equiv2\pmod4\).

For the last approximation claim, take \(b=N+1-a\), so \(x=y\), and let \(a\) be a nearest integer to \((N+2)/4\). A direct substitution gives
\[
\beta_- = \frac{N}{8}-\frac2N\left(a-\frac{N+2}{4}\right)^2
\geq\frac{N^2-4}{8N}.
\]
Inversion yields the claimed bound \(\delta_-\leq2N/(N^2-4)\). This completes the proof.

## Verification

The accompanying `CHECK.py` uses only the Python 3 standard library. Execute `python3 CHECK.py` from its containing directory. It checks the Green inverse identity using exact rational arithmetic, compares the rank-two threshold prediction with exact \(LDL^{\mathsf T}\)-inertia counts for independently constructed full matrices, tests the Rayleigh identity, and verifies sharp-site witnesses. The executed version returned: **2,104** exact Green-inverse entry checks; **6,544** geometric Rayleigh checks; **39,264** rank-two/full-inertia comparisons; **25** sharp quarter-site witnesses; **0** skipped singular cases. The proof above, not this finite diagnostic, establishes the all-\(N\) theorem.

For a concrete instance, \(N=6\) and \((a,b)=(2,5)\) give \(\beta_-=3/4\), so a second super-band mode appears exactly for \(\delta>1/3\). The same threshold cannot be improved by another pair of sites at this length.

## Relationship to prior work

Theocharis et al., arXiv:0906.4094 (first public 2009-06-22), study one and two defects in precompressed granular chains and demonstrate the qualitative transition from one to two localized modes as bead sizes and their separation change. Their contact spring constants also change with bead radii, and their central results concern nonlinear breathers, stability and selected finite configurations. The exact arbitrary-site two-by-two free-end threshold and sharp placement extremum established here are not stated in Section IV.1 of that work.

Boechler et al., arXiv:1103.2483 (first public 2011-03-12), combine experiments, direct finite eigenanalysis and small-cluster approximations for light defects in a left-fixed/right-free granular chain. Their Section V describes the two-mode split and explicitly restricts its analytic approximation to a nearest-neighbor four-particle reduction. It does not furnish the present exact all-position threshold for a homogeneous-spring, free/free chain.

Luo, arXiv:1607.06946 (first public 2016-07-23), gives the exact one-defect band-edge threshold for the finite homogeneous-spring open chain: \(\delta_c=N/[(2a-1)(2(N-a)+1)]\). The one-site version of the present Green function reproduces this already-known identity exactly. The new content concerns the coupled second threshold, exact two-mode count and optimal relative placement, which cannot be inferred by independently applying the one-defect condition.

## Limitations

The claim is an **exact theorem for the stated finite, free/free, constant-spring model**. It is not a theorem for nonlinear Hertzian contacts, different spring constants around impurities, mixed or periodic boundaries, nonidentical defect masses, damping, the infinite-defect-spacing limit, or nonlinear mode stability. A squared frequency just above the infinite-host threshold can have a long decay length, so **above-band** should not be read as a uniform quantitative localization estimate. Finite numerical checking is not a substitute for the analytical count. Historical priority beyond the primary texts inspected is not certified; other lattice Green-function and isotope-pair analyses, including older surface-defect work, may contain equivalent specializations.

## References

1. G. Theocharis, M. Kavousanakis, P. G. Kevrekidis, C. Daraio, M. A. Porter, and I. G. Kevrekidis, *Localized Breathing Modes in Granular Crystals with Defects* (arXiv:0906.4094, first submitted 2009-06-22), Sections III–IV. https://arxiv.org/abs/0906.4094
2. N. Boechler, G. Theocharis, Y. Man, P. G. Kevrekidis, and C. Daraio, *Defect Modes in One-Dimensional Granular Crystals* (arXiv:1103.2483, first submitted 2011-03-12), Sections III–V. https://arxiv.org/abs/1103.2483
3. Q. Luo, *Local Vibrational Mode of Impurity in a Monatomic Linear Chain under Open and Periodic Boundary Conditions* (arXiv:1607.06946, first submitted 2016-07-23), Section 3.2. https://arxiv.org/abs/1607.06946
