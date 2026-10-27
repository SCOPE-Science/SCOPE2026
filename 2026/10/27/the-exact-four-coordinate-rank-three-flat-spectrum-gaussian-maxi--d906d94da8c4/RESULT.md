# The exact four-coordinate rank-three flat-spectrum Gaussian maximum

## Finding

Let \(\mathcal R_{4,3}\) be the class of real positive-semidefinite correlation matrices of order four with spectrum \((4/3,4/3,4/3,0)\). For every \(R\in\mathcal R_{4,3}\), let \(X\sim N(0,R)\). Then the sharp first nondivisible rank-three flat-spectrum value is

\[
\boxed{\min_{R\in\mathcal R_{4,3}}\mathbb E\max_{1\le i\le4}X_i=\frac{2\sqrt6}{3\sqrt\pi}.}
\]

Equality holds exactly for simultaneous coordinate permutations of

\[
R_* =\frac13\begin{pmatrix}
3&-1&1&1\\
-1&3&1&1\\
1&1&3&-1\\
1&1&-1&3
\end{pmatrix}.
\]

The entire feasible class has three permutation orbits, each with one Gaussian-width value. Their respective widths in the order of four, three, and two identical null-vector signs are

\[
\begin{aligned}
W_{4,0}&=\frac{\sqrt3}{\pi^{3/2}}\left(\pi+2\arcsin\frac13\right),\\
W_{3,1}&=\frac1{\sqrt{2\pi}}\left(\frac{\sqrt6+\sqrt3}{2}+\frac{\sqrt6}{\pi}\arcsin\frac1{\sqrt3}\right),\\
W_{2,2}&=\frac{2\sqrt6}{3\sqrt\pi},
\qquad W_{2,2}<W_{3,1}<W_{4,0}.
\end{aligned}
\]

Numerically these values are approximately \(1.1886202974\), \(1.0255440989\), and \(0.9213177319\). In particular, the exact gap above the rank-three independent-normal baseline \(a_3=3/(2\sqrt\pi)\) is

\[
\frac{2\sqrt{2/3}-3/2}{\sqrt\pi}=0.0750333566\ldots.
\]

## Assumptions and scope

A *correlation matrix* is a real symmetric positive-semidefinite matrix with unit diagonal. The spectrum includes algebraic multiplicities. All Gaussian vectors are centered; the coordinates need not be independent and the covariance is allowed to be singular. The spectral constraint is exact, not approximate. Equality refers to the covariance, not to an arbitrary orthogonal realization of its Gram vectors. The statement evaluates a natural fixed-spectrum extremum and does not make an assertion about other dimensions or ranks.

## Proof

**1. Exhaustion of all admissible covariance matrices.** The prescribed spectrum makes \(P=(3/4)R\) a rank-three orthogonal projection in \(\mathbb R^4\). It has the form \(P=I-vv^{\mathsf T}\), with \(\|v\|_2=1\). Each diagonal identity \(1=(4/3)(1-v_i^2)\) forces \(v_i^2=1/4\). Hence \(v=s/2\) for a sign vector \(s\in\{-1,1\}^4\), and

\[
R=\frac43 I-\frac13ss^{\mathsf T}.
\]

Conversely every such sign vector produces an admissible covariance. Replacing \(s\) by \(-s\) leaves \(R\) unchanged; relabeling coordinates permutes its signs. Thus there are precisely three orbits, labeled by sign multiplicities \((4,0)\), \((3,1)\), and \((2,2)\).

**2. An exact Gaussian facet identity.** Choose four unit Gram vectors \(u_i\in\mathbb R^3\) with \(u_i\cdot u_j=R_{ij}\). For \(g\sim N(0,I_3)\), set \(F(g)=\max_i u_i\cdot g\). This function is continuous, positively homogeneous of degree one, and piecewise linear. Euler's identity, Gaussian integration by parts and approximation by smooth convex functions give

\[
\mathbb EF(g)=\mathbb E[g\cdot\nabla F(g)]=\mathbb E\Delta F(g).
\]

As a distribution, the Laplacian of \(F\) is concentrated on the active equality facets between maximizing vertices. For each pair \(i<j\), its density relative to two-dimensional area on the hyperplane \((u_i-u_j)\cdot g=0\) is \(d_{ij}=\|u_i-u_j\|_2\), but only where this tied pair dominates the two other vertices. Triple-tie sets have zero Gaussian surface measure. The standard Gaussian surface integral over that hyperplane is \(1/\sqrt{2\pi}\) times the probability of domination for its intrinsic standard two-dimensional Gaussian. Write \(\Pi_{ij}\) for orthogonal projection onto \((u_i-u_j)^\perp\) and let \(\{\ell,m\}=\{1,2,3,4\}\setminus\{i,j\}\). The projected differences \(\Pi_{ij}(u_i-u_\ell)\) and \(\Pi_{ij}(u_i-u_m)\) have normalized correlation \(\rho_{ij}\). Their joint positive quadrant probability is \(Q(\rho)=1/4+\arcsin(\rho)/(2\pi)\), including the degenerate endpoints by continuity. Therefore

\[
\mathbb E F(g)=\frac1{\sqrt{2\pi}}\sum_{i<j}d_{ij}\left(\frac14+\frac{\arcsin\rho_{ij}}{2\pi}\right).
\tag{1}
\]

For reproducibility, all quantities in (1) are computed from the covariance alone. Define \(D_{ab,cd}=R_{ac}-R_{ad}-R_{bc}+R_{bd}\). Then \(d_{ij}^2=D_{ij,ij}\), and with \(a=(i,\ell)\), \(b=(i,m)\), \(d=(i,j)\),

\[
\rho_{ij}=\frac{D_{a,b}-D_{a,d}D_{b,d}/D_{d,d}}
{\sqrt{(D_{a,a}-D_{a,d}^2/D_{d,d})(D_{b,b}-D_{b,d}^2/D_{d,d})}}.
\tag{2}
\]

The denominators are strictly positive for every covariance in the three orbits; all degeneracy occurs only at the allowable boundary correlations \(\rho=\pm1\).

**3. Exhaustive evaluation.** A *same-sign pair* means \(s_i=s_j\); it has distance \(2\sqrt6/3\). An *opposite-sign pair* has distance \(2\sqrt3/3\). Direct substitution into (2), with exact rational arithmetic, gives the following exhaustive facet table (pair counts are among all six unordered pairs):

| Sign orbit | Same-sign pairs and correlations | Opposite-sign pairs and correlations |
|---|---|---|
| \((4,0)\) | \(6\) pairs, \(\rho=1/3\) | \(0\) pairs |
| \((3,1)\) | \(3\) pairs, \(\rho=1/\sqrt3\) | \(3\) pairs, \(\rho=0\) |
| \((2,2)\) | \(2\) pairs, \(\rho=-1\) | \(4\) pairs, \(\rho=1\) |

In the balanced case the same-sign pairs are nonexposed diagonals, because \(Q(-1)=0\); each opposite-sign pair contributes \((2\sqrt3/3)/2\), since \(Q(1)=1/2\). Substitution of every row into (1) produces the three displayed closed forms, not numerical conjectures.

**4. Strict minimization and uniqueness.** Put \(\theta=\arcsin(1/\sqrt3)\), \(\psi=\arcsin(1/3)\). Because \(\theta>1/\sqrt3\) and \(\pi<4\),

\[
\sqrt{2\pi}W_{3,1}>
\frac{\sqrt6+\sqrt3}{2}+\frac{\sqrt2}{4}>
\frac{4\sqrt3}{3}=\sqrt{2\pi}W_{2,2}.
\]

The second strict inequality follows after multiplying by twelve and squaring positive sides: \((6\sqrt6+3\sqrt2)^2=234+72\sqrt3>300=(10\sqrt3)^2\). Also \(\sin(2\psi)=4\sqrt2/9>1/\sqrt3=\sin\theta\), with both angles in \((0,\pi/2)\); hence \(2\psi>\theta\). Consequently

\[
\sqrt{2\pi}W_{4,0}=\sqrt6\left(1+\frac{2\psi}{\pi}\right)>
\frac{\sqrt6+\sqrt3}{2}+\frac{\sqrt6\theta}{\pi}=
\sqrt{2\pi}W_{3,1}.
\]

The class enumeration and strict inequalities force the unique balanced-sign covariance orbit as the complete equality set. Finally, for independent standard Gaussian variables \(G_1,G_2,G_3\), elementary one-dimensional Gaussian integration yields \(\mathbb E\max(G_1,G_2,G_3)=3/(2\sqrt\pi)\), giving the exact gap stated above. \(\square\)

## Verification

The accompanying standalone `verify.py` constructs the exact rational Gram matrix for each of the \(16\) sign vectors, checks the projection formula and all six facet correlations symbolically, confirms the three orbit sizes \(2,8,6\), and simplifies each expectation to its stated closed form. It completes \(261\) deterministic assertions. Separately, a reproducible scrambled Sobol Gaussian quadrature checks all three numerical values to within \(0.006\) without invoking the facet formula. The output is recorded in `verification_output.txt`. Numerical integration is corroboration, not proof; the infinite Gaussian integral follows analytically from the weak Laplacian identity.

## Relationship to prior work

Paatur, *Linear stability and divisibility gaps for Gaussian maxima* (2026), defines exactly this fixed-flat-spectrum objective, proves the divisible-rank equality and a positive but nonsharp nondivisibility bound, and develops the planar large-size limit. It does not state the rank-three four-coordinate constant or its equality covariance. Sun, Hu and Lan, *The 4-D Gaussian Random Vector Maximum Conjecture and the 3-D Simplex Mean Width Conjecture* (2020), prove the **unconstrained maximum** of this Gaussian objective and give an explicit formula for the expectation at general four-dimensional correlation matrices. Those formulas already cover evaluation at any specified covariance; no general four-variable formula, Gaussian facet identity, or regular-simplex maximum is claimed as new here. The specific contribution is the complete sharp **minimum under an exact rank-three flat spectrum**, with equality classification and nondivisibility gap. Li and Huang's mean-width inequalities for isotropic measures (2022) have different centering/projection hypotheses and do not determine this exact constrained extremum. Historical priority for a previously computed specialization in frame geometry remains a residual uncertainty.

## Limitations

The result applies only to four coordinates and exact rank-three flat spectrum; the technique relies on the exceptional discrete sign-orbit classification of the rank-one null space and does not resolve the general higher-rank asymptotic constants. The value does not imply stochastic ordering of the maximum across covariance classes. Independent mathematical validation has not been performed. Earlier broad Gaussian maximum formulas can be specialized to this finite feasible set; the novelty rests on the isolated spectral-optimization/equality classification, not on a claim of a new general integral formula.

## References

1. C. Paatur, *Linear stability and divisibility gaps for Gaussian maxima*, arXiv:2610.14086v1, first posted 2026-10-08. https://arxiv.org/abs/2610.14086
2. W. Sun, Z.-C. Hu, and G. Lan, *The 4-D Gaussian Random Vector Maximum Conjecture and the 3-D Simplex Mean Width Conjecture*, arXiv:2008.04827v2, 2020. https://arxiv.org/abs/2008.04827
3. A.-J. Li and Q. Huang, *Mean width inequalities of sections and projections of convex bodies for isotropic measures*, arXiv:2111.10729v2, 2022. https://arxiv.org/abs/2111.10729
