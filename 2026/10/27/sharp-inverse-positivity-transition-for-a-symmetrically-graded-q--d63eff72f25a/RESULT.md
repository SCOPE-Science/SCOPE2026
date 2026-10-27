# Sharp inverse-positivity transition for a symmetrically graded \(Q^2\) spectral-element square

## Finding
Consider the \(Q^2\) continuous spectral-element/Gauss–Lobatto discretization of \(-\Delta u=f\), with zero Dirichlet boundary conditions on a square. There are precisely three tensor-product elements along each axis, of respective lengths proportional to \((1,t,1)\), with \(t>0\). With the five interior Gauss–Lobatto nodes on each axis, let \(S(t)\) be the resulting \(25\times25\) stiffness matrix and \(M_2(t)\) its positive diagonal quadrature-mass matrix. The discrete nodal Laplacian is \(L(t)=M_2(t)^{-1}S(t)\).

Define the degree-thirteen integer polynomial
\[
\begin{aligned}
Q(t)={}&192t^{13}+2576t^{12}+13108t^{11}+18631t^{10}\\
&-124198t^9-830730t^8-2554448t^7-4960645t^6\\
&-6543798t^5-5928564t^4-3589936t^3-1356656t^2\\
&-278880t-22464.
\end{aligned}
\]
It has exactly one positive real zero, \(t_*\), satisfying
\[
\frac{41999}{10000}<t_*<\frac{21}{5},\qquad
 t_*=4.1999378918007026413\ldots.
\]
**Exact classification:** for every real \(t>0\),
\[
L(t)^{-1}\ge0\text{ entrywise}\quad\Longleftrightarrow\quad 0<t\le t_*.
\]
For \(0<t<t_*\), all \(625\) entries are strictly positive. At \(t=t_*\), exactly the eight symmetry-related entries in the orbit of \((1,3)\) vanish, using zero-based flattened indices \(5i+j\), and all others are strictly positive. For \(t>t_*\) an entry is negative. In particular, at \(t=5\),
\[
[S(5)^{-1}]_{1,3}=-\frac{29159657937}{68799433880114}<0.
\]
Thus the scheme ceases to satisfy the discrete nodal maximum principle on this explicit finite graded square, despite its symmetric positive-definite stiffness matrix.

## Assumptions and scope
The physical domain may be taken as \((0,1)^2\); use cell lengths \((1,t,1)/(t+2)\) independently in both directions, with constant unit diffusion and homogeneous Dirichlet data. The polynomial degree is two, the local tensor-product quadrature uses all three Gauss–Lobatto nodes per coordinate, and there is no mass-lumping approximation beyond this standard quadrature. The criterion is **inverse positivity of the assembled, mass-inverted discrete elliptic operator**, not positivity of the local stiffness entries or of a time-stepping map. The scaling from \((1,t,1)\) to \((1,t,1)/(t+2)\) leaves the two-dimensional assembled stiffness unchanged. No claim is made for arbitrary nonuniform grids, different element counts, curved cells, variable diffusion, or another finite-element method.

## Proof
For an element of length \(h>0\), direct differentiation of the quadratic nodal basis at the three Gauss–Lobatto points gives local stiffness and diagonal quadrature-mass matrices
\[
K_h=\frac{1}{3h}\begin{pmatrix}7&-8&1\\-8&16&-8\\1&-8&7\end{pmatrix},
\qquad M_h=\frac h6\operatorname{diag}(1,4,1).
\]
Assemble them over the three consecutive intervals \((1,t,1)\), impose zero Dirichlet data, and retain the five interior nodes. Calling the resulting \(5\times5\) matrices \(K(t)\) and diagonal \(M(t)\), the exact two-dimensional matrices are
\[
S(t)=K(t)\otimes M(t)+M(t)\otimes K(t),
\quad M_2(t)=M(t)\otimes M(t),\quad L(t)=M_2(t)^{-1}S(t).
\]
The stiffness is symmetric positive definite because its quadratic form is the positive Gauss–Lobatto discretization of the Dirichlet energy. Since \(M_2(t)\) is positive diagonal, \(L(t)^{-1}=S(t)^{-1}M_2(t)\) has precisely the same entrywise signs as \(S(t)^{-1}\).

The only non-immediate step is an **exact finite symbolic sign classification** of the \(625\) entries. Reflection about either coordinate midpoint, exchange of the two coordinates, and matrix transposition reduce these entries to \(55\) symmetry classes. In each class, rational block inversion using the even/odd reflection subspaces gives a rational function \(N(t)/D(t)\) with integer polynomial numerator and denominator. Every denominator has nonnegative coefficients and is strictly positive on \(t>0\); every numerator has a strictly positive constant term. Exact symbolic coefficient inspection shows that \(45\) numerators have no sign variation and \(10\) have one sign variation, in descending powers. All \(54\) representatives other than \((1,3)\) have positive numerator value at \(t=21/5\). By Descartes' rule of signs, a polynomial with no sign variation is positive throughout \(t>0\); a polynomial with exactly one sign variation and positive values at both \(0\) and \(21/5\) is strictly positive throughout \((0,21/5]\). These are exhaustive assertions using exact rational arithmetic, rederived and checked from the two local element matrices by the companion program `verify_q2_threshold.py` (no numerical root search enters the universal sign proof).

For the distinguished entry, exact elimination gives
\[
[S(t)^{-1}]_{1,3}=
-\frac{3Q(t)}{2(t+2)^2(4t+3)F(t)H(t)},
\]
where
\[
F(t)=12t^5+81t^4+200t^3+265t^2+180t+44,
\]
\[
H(t)=48t^7+488t^6+2003t^5+4420t^4+5799t^3+4500t^2+1792t+216.
\]
All denominator factors are strictly positive for \(t>0\). The coefficients of \(Q\), in descending powers, exhibit exactly one sign change; moreover \(Q(41999/10000)<0<Q(21/5)\). Therefore \(Q\) has exactly one positive root, in the displayed rational bracket. The distinguished entry is positive before this root, zero there, and negative afterward. Every other symmetry class is strictly positive up to \(21/5\). These facts establish the complete stated equivalence and the equality case. Substituting \(t=5\) yields the displayed rational counterexample.

## Verification
The standalone source `verify_q2_threshold.py` constructs the local element matrices symbolically, assembles the exact \(25\times25\) stiffness, decomposes it into parity blocks of dimensions \(9,6,6,4\), checks exact block inverses, generates all \(55\) symmetry orbits, and tests all polynomial coefficient signs and the witness identity. The verified results are \(45\) zero-sign-variation and \(10\) one-sign-variation classes; exactly one class has a numerator negative at \(21/5\). Running `python verify_q2_threshold.py` requires Python 3.10+ and SymPy 1.11+; the assertions use symbolic rational arithmetic. The decimal value of \(t_*\) is illustrative and is not used for certification. The proof is restricted to this one-parameter finite mesh family.

## Relationship to prior work
Cross and Zhang, arXiv:2310.15341 (2023), formulate the same \(Q^2\) Gauss–Lobatto method and establish inverse positivity under sufficient, nonsharp quasi-uniform mesh constraints (Theorem 4.1). Their Section 5.2 numerically observes loss of inverse positivity on a different \(5\times5\)-element family. The present result gives an exact necessary-and-sufficient transition, including the equality case, on the natural smaller symmetric \(3\times3\)-element family. It neither reproves nor supersedes the source's results for arbitrary quasi-uniform meshes. Cross and Zhang, arXiv:2010.07282 (2020; revised 2024), study the related \(Q^3\) scheme, principally for uniform meshes. Hao Li's 2021 thesis discusses \(Q^2\) monotonicity, but its complete text was not available for a definitive comparison; that is an outstanding priority risk.

## Limitations
This is a finite-dimensional, one-parameter exact classification, not a general sharp condition for arbitrary graded rectangular meshes. The symbolic calculations are independently reproducible from the local element matrices but have not undergone external mathematical validation. The thesis full-text access limitation leaves publication priority uncertain. There is no assertion that the method loses stability or accuracy whenever entrywise inverse positivity fails; the conclusion is specifically about the nodal discrete maximum principle.

## References
1. L. J. Cross and X. Zhang, *On the monotonicity of \(Q^2\) spectral element method for Laplacian on quasi-uniform rectangular meshes*, arXiv:2310.15341, publicly submitted 2023-10-23; Communications in Computational Physics 35 (2024), 160–180, DOI:10.4208/cicp.oa-2023-0206.
2. L. J. Cross and X. Zhang, *Monotonicity of \(Q^3\) spectral element method for discrete Laplacian*, arXiv:2010.07282, publicly submitted 2020-10-14.
3. H. Li, *Accuracy and Monotonicity of Spectral Element Method on Structured Meshes*, PhD thesis, Purdue University, posted 2021-05-03, DOI:10.25394/PGS.14529456.
