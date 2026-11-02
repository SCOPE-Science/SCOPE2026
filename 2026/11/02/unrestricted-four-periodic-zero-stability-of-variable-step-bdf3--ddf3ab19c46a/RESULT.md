# Unrestricted four-periodic zero stability of variable-step BDF3

## Finding

Let third-order backward differentiation (BDF3) be formed by differentiating the unique cubic interpolant through the four most recent time levels. For every fixed positive repeating four-step pattern \(h_0,h_1,h_2,h_3\), its two-dimensional parasitic difference-mode monodromy \(F\) has
\[
\rho(F)<1\qquad(h_0,h_1,h_2,h_3>0).
\]
Consequently the full BDF3 recurrence for \(y'=0\) has a simple constant mode and strictly damped parasitic modes, without any restriction on the ratios of neighboring steps. The bound is sharp but nonuniform:
\[
\sup_{h_0,h_1,h_2,h_3>0}\rho(F)=1.
\]
For the geometric reset pattern \((h_0,h_1,h_2,h_3)=(1,r,r^2,r^3)\),
\[
\rho(F)=1-6r+O(r^2)\qquad(r\downarrow0).
\]
These assertions are about **each fixed repeated grid**, not the stability of arbitrary changing grids or a uniform estimate over all four-step patterns.

## Assumptions and scope

Fix four real numbers \(h_0,h_1,h_2,h_3>0\), extended periodically by \(h_{j+4}=h_j\). The time points have successive spacings \(h_j\). At every step the variable-coefficient BDF3 formula is the derivative at the newest time point of the cubic Lagrange interpolant at the newest point and the three preceding points. Study the homogeneous test equation \(y'=0\), with arbitrary three initial nodal values. The difference variables are \(d_j=y_j-y_{j-1}\).

For \(a,b,c>0\) put
\[
\begin{aligned}
q(a,b,c)&=3a^2+4ab+2ac+b^2+bc,\\
D(a,b,c)&=bc(b+c)q(a,b,c),\\
P(a,b,c)&=a^2c(a^2+4ab+2ac+3b^2+3bc+c^2),\\
U(a,b,c)&=a^2b(a+b)^2.
\end{aligned}
\]
All \(D,P,U\) are strictly positive. With indices modulo four, abbreviate \(D_i=D(h_i,h_{i-1},h_{i-2})\), and likewise \(P_i,U_i\). Define
\[
N_i=\begin{pmatrix}P_i&-U_i\\D_i&0\end{pmatrix},\qquad
F=\frac{N_3N_2N_1N_0}{D_3D_2D_1D_0}.
\]
The cyclic starting index changes \(F\) only by similarity because every one-step matrix is invertible.

## Proof

**Step 1: exact BDF3 difference transfer.** Write the interpolation nodes relative to the newest level as \(0,-a,-a-b,-a-b-c\). If \(\alpha_j\) is the derivative at zero of the \(j\)-th Lagrange cardinal polynomial, direct differentiation gives
\[
\alpha_0=\frac{3a^2+4ab+2ac+b^2+bc}{a(a+b)(a+b+c)},
\quad
\alpha_2=\frac{a(a+b+c)}{bc(a+b)},
\quad
\alpha_3=-\frac{a(a+b)}{c(b+c)(a+b+c)}.
\]
The coefficients sum to zero because constant data differentiate to zero. Hence \(\sum_{j=0}^3\alpha_j y_{n-j}=0\) becomes
\[
 d_n=\frac{\alpha_2+\alpha_3}{\alpha_0}d_{n-1}
      +\frac{\alpha_3}{\alpha_0}d_{n-2}
    =\frac{P(a,b,c)}{D(a,b,c)}d_{n-1}
      -\frac{U(a,b,c)}{D(a,b,c)}d_{n-2}.
\]
Thus the asserted one-step matrix \(N_i/D_i\) is exact; the order of multiplication in \(F\) follows chronological stepping.

**Step 2: an exact algebraic positivity certificate.** Put
\[
\Delta=\prod_{i=0}^{3}D_i,
\quad E=\prod_{i=0}^{3}U_i,
\quad T=\operatorname{tr}(N_3N_2N_1N_0).
\]
Then \(\operatorname{tr}F=T/\Delta\) and \(\det F=E/\Delta\). The real second-degree Schur--Jury criterion says that the roots of \(\lambda^2-(T/\Delta)\lambda+E/\Delta\) lie strictly in the unit disk if and only if
\[
\boxed{\Delta-T+E>0,\qquad \Delta+T+E>0,\qquad \Delta-E>0.}
\]
Each left-hand side is a homogeneous polynomial of degree twenty in \(h_0,h_1,h_2,h_3\). Expand exactly in the monomial basis \(h_0^{i_0}h_1^{i_1}h_2^{i_2}h_3^{i_3}\). The complete, explicitly given integer coefficient table is in `certificates/schur_coefficients.tsv`. Every listed coefficient is strictly positive; respectively the three expansions have 271, 267 and 271 nonzero monomials, with minimum positive coefficients 6, 6 and 3. The table is an exhaustive exact algebraic certificate, **not** a finite sampling of step lengths. Its reproducibility is described below. Since the step lengths are positive, all three inequalities are strict. This proves \(\rho(F)<1\). The full nodal recurrence also has the constant solution \(y_j=1\). Differences decay geometrically along periods, and their cumulative sum converges, proving the simple neutral constant mode and zero stability on the fixed periodic grid.

**Step 3: sharp boundary.** For \((h_0,h_1,h_2,h_3)=(1,r,r^2,r^3)\), substitute into the same rational transfer matrices and expand at \(r=0^+\):
\[
\operatorname{tr}F=-1+6r-\frac{74}{3}r^2+O(r^3),
\qquad
\det F=\frac{r^5}{3}+O(r^6).
\]
The two eigenvalues therefore tend to \(-1\) and zero, respectively. The one near \(-1\) equals \(-1+6r+O(r^2)\), whereas the other is \(O(r^5)\). Thus the spectral radius equals \(1-6r+O(r^2)\) for small \(r>0\). Combining this limit with strict stability for each positive quadruple yields the supremum one.

## Verification

`verify.py` is a Python standard-library-only exact integer-polynomial reproducer: it builds \(D_i,P_i,U_i\), multiplies the four polynomial matrices, forms the three Schur numerators, compares **every** computed exponent/coefficient with `certificates/schur_coefficients.tsv`, and requires strict coefficient positivity. It additionally compares the direct rational Lagrange differentiation coefficients with the closed transfer formula for eight independent triples. Executing `python verify.py` prints a passing certificate with the three monomial counts and the SHA-256 of the coefficient table. `verify_sympy.py` independently reconstructs and checks every coefficient using SymPy and checks the geometric-limit expansions symbolically. Neither numerical eigenvalue sampling nor an unverified textual log is used as proof of the all-parameters result.

## Relationship to prior work

The variable-step BDF framework and ratio-restricted stability theory are classical. Calvo, Grande and Grigorieff (1990) establish sufficient step-ratio bounds; Guglielmi and Zennaro (2001) analyze BDF3 by joint spectral-radius methods; Calvo and Grigorieff (2002) give stability bounds for parabolic time discretization under ratio and variation restrictions. Li and Liao (2022) give a perturbed-stability theorem under a threshold near \(2.553\), while Söderlind, Fekete and Faragó (2018) prove stability on sufficiently smooth variable grids. Those inspected statements do not imply a ratio-unrestricted four-periodic Floquet result. Earlier results for two- and three-periodic BDF3 grids also do not by themselves prove the new four-period result: four independently chosen positive step lengths create an additional free parameter and require new strict polynomial inequalities. Original specialist coverage remains a priority risk because the complete Guglielmi--Zennaro (2001) and Calvo--Grande--Grigorieff (1990) texts could not be inspected.

## Limitations

The theorem is for BDF3 formed by cubic interpolation, for \(y'=0\), and a fixed positive four-periodic spacing pattern. It proves neither BDF3 zero stability on arbitrary or higher-period grids nor convergence or inhomogeneous stability for general differential equations. The supremum one rules out a parameter-independent strict Floquet damping margin; the result makes no uniform assertion when step patterns degenerate with mesh refinement. The exhaustive coefficient certificate is a finite exact identity proof, not a substitute for independently audited mathematical review. The focal author's public copy has a verified upload date of January 30, 2015; its underlying journal article appeared in 1990, and the upload date is not asserted to be the original discovery date.

## References

1. M. Calvo, T. Grande and R. D. Grigorieff, *On the zero stability of the variable order variable stepsize BDF-formulas*, Numerische Mathematik 57 (1990), 39--50, https://doi.org/10.1007/BF01386395 ; publicly dated author upload https://www.researchgate.net/publication/226854075_On_the_zero_stability_of_the_variable_order_variable_stepsize_BDF-Formulas .
2. N. Guglielmi and M. Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach*, Numerische Mathematik 88 (2001), 445--458, https://arts.units.it/handle/11368/1703201 .
3. M. Calvo and R. D. Grigorieff, *Time Discretisation of Parabolic Problems with the Variable 3-Step BDF*, BIT 42 (2002), 689--701, https://doi.org/10.1023/A:1021992101967 .
4. G. Söderlind, I. Fekete and I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, BIT 58 (2018), 1125--1143, https://doi.org/10.1007/s10543-018-0716-y .
5. Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, SIAM Journal on Numerical Analysis 60 (2022), 2253--2272, https://arxiv.org/abs/2201.00527 .
