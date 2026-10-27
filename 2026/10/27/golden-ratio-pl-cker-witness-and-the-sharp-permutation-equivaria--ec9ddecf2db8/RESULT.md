# Golden-ratio Plücker witness and the sharp permutation-equivariant determinant profile

## Finding

The real, third-order Plücker-coordinate bound admits an exact optimization on its canonical permutation-equivariant matrix family. For every real \(2<p<\infty\), let \(r_p\in(0,1)\) be the unique solution of
\[
r_p+r_p^{p-1}=1.
\]
For the real two-dimensional space of matrices
\[
\mathcal E=\{aI_3+b(J_3-I_3):a,b\in\mathbb R\},
\]
where \(J_3\) is the all-one matrix, one has
\[
\sup_{0\ne A\in\mathcal E}
\frac{|\det A|}{\prod_{j=1}^3\|Ae_j\|_p}
=(1+r_p)\big((1+r_p)(2-r_p)\big)^{1-3/p}
=: B_p.
\]
Exactly the nonzero scalar multiples of
\[
M_{r_p}=\begin{pmatrix}r_p&-1&-1\\-1&r_p&-1\\-1&-1&r_p\end{pmatrix}
\]
attain this supremum. In particular, \(r_3=(\sqrt5-1)/2\) and \(B_3=(1+\sqrt5)/2\), the golden ratio.

For real \(\ell_p\), let \(C^{\mathbb R}_{3,p}\) denote the optimal constant in the bound on the \(\ell_p\) norm of all three-index Plücker minors of three vectors by the product of their \(\ell_p\) norms. The three-coordinate witness gives
\[
C^{\mathbb R}_{3,p}\ge B_p,
\quad C^{\mathbb R}_{3,3}\ge \frac{1+\sqrt5}{2}>4^{1/3}.
\]
The exact full real endpoint constants are \(C^{\mathbb R}_{3,2}=1\) and \(C^{\mathbb R}_{3,\infty}=4\). Thus the proposed geometric interpolation inequality from these two *sharp real* endpoint constants fails at \(p=3\); this does not contradict complex multilinear interpolation.

## Assumptions and scope

All scalar entries and the coordinate spaces in the present theorem are **real**. There are three columns and \(2<p<\infty\) in the invariant-family theorem. The columns in the normalized quotient must be nonzero. If one column vanishes, the quotient is not defined and the corresponding determinant inequality is vacuous. \(\ell_p\) has its ordinary coordinate norm. The all-one matrix is \(J_3\), and \(e_j\) are the standard coordinate vectors.

The Plücker-coordinate map is
\[
\mathcal P_3(v_1,v_2,v_3)=
\bigl(\det(v_j(i_k))_{k,j=1}^3\bigr)_{i_1<i_2<i_3},
\]
with its \(\ell_p\) norm for finite \(p\) and supremum norm for \(p=\infty\). The full real constant \(C^{\mathbb R}_{3,p}\) is its operator norm as a real trilinear map. The theorem computes the supremum only on \(\mathcal E\), and supplies **a lower bound** for the unrestricted Plücker constant; it does not claim unrestricted sharpness.

## Proof

**Step 1 (reduction to one real parameter).** Every member of \(\mathcal E\) has diagonal \(a\) and off-diagonal \(b\). If \(b=0\) and \(a\ne0\), the normalized quotient equals \(1\). If \(b\ne0\), divide the matrix by \(-b\). The quotient is unchanged by nonzero scalar multiplication, leaving precisely \(M_r\), whose diagonal is \(r=-a/b\) and whose off-diagonal entries are \(-1\), for a real \(r\). The eigenvalues of \(M_r\) are \(r-2\) (once) and \(r+1\) (twice); each column has norm \((|r|^p+2)^{1/p}\). Hence the quotient is
\[
F_p(r)=\frac{|(r+1)^2(r-2)|}{(|r|^p+2)^{3/p}}.
\]

**Step 2 (global exclusion of negative and large positive parameters).** For \(r=-t\) with \(0\le t\le1\), one has \((1-t)^2(t+2)=2-3t+t^3\le2\) and \((t^p+2)^{3/p}\ge2^{3/p}\), so \(F_p(-t)\le F_p(0)\). For \(t\ge1\), the numerator \((t-1)^2(t+2)=t^3-3t+2\le t^3\), while the denominator strictly exceeds \(t^3\), hence \(F_p(-t)<1\). For \(r\ge2\), the numerator \((r+1)^2(r-2)=r^3-3r-2<r^3\), and again \(F_p(r)<1\) unless \(r=2\), when it is zero.

**Step 3 (unique global maximizer).** For \(0<r<2\), direct logarithmic differentiation gives exactly
\[
\frac{F'_p(r)}{F_p(r)}
=\frac{6(1-r-r^{p-1})}{(1+r)(2-r)(r^p+2)}.
\]
The map \(r\mapsto r+r^{p-1}\) increases strictly from zero to a value above one on \((0,2)\), so there is exactly one critical parameter \(r_p\in(0,1)\), at which the derivative changes from positive to negative. Therefore this point uniquely maximizes \(F_p\) over \([0,2]\), with strict improvement over \(F_p(0)\).

Moreover \(F_p(r_p)>1\): at \(p=2\) the matrix \(M_{1/2}\) has pairwise orthogonal columns and quotient \(1\); for \(p>2\), its three-entry columns have strictly smaller \(\ell_p\) norm than \(\ell_2\) norm, with their determinant unchanged. Hence \(F_p(1/2)>1\) at every such exponent. Step 2 then excludes every \(r\notin[0,2]\) and the diagonal-only case. Thus precisely the stated scalar multiples maximize on \(\mathcal E\).

At the critical point, \(r_p^p=r_p(1-r_p)\), so
\[
r_p^p+2=(1+r_p)(2-r_p),\qquad
F_p(r_p)=(1+r_p)((1+r_p)(2-r_p))^{1-3/p}.
\]
For \(p=3\), \(r_3^2+r_3=1\); the unique positive root is \((\sqrt5-1)/2\), and the displayed expression reduces to \(B_3=1+r_3=(1+\sqrt5)/2\).

**Step 4 (the Plücker consequence).** Put the three columns of \(M_{r_p}\) into the first three coordinates of real \(\ell_p\), with all subsequent coordinates zero. There is exactly one nonzero three-coordinate minor, so its Plücker quotient equals \(B_p\). This proves \(C^{\mathbb R}_{3,p}\ge B_p\).

**Step 5 (sharp real endpoints and strict interpolation obstruction).** At \(p=2\), Cauchy–Binet and the Gram determinant inequality give \(C^{\mathbb R}_{3,2}=1\), attained by the standard coordinate frame. At \(p=\infty\), any real \(3\)-by-\(3\) minor of a frame with sup-norm-one columns has entries in \([-1,1]\). Multiaffinity of its determinant in the nine entries implies a maximum at some sign matrix. Subtract the first row from each other row; the last two rows then have even entries, so the determinant is divisible by \(4\). Hadamard's Euclidean bound is \(3^{3/2}<8\). Thus the determinant magnitude is at most \(4\), and the sign matrix
\[
\begin{pmatrix}1&1&1\\1&-1&1\\1&1&-1\end{pmatrix}
\]
attains magnitude \(4\). Consequently \(C^{\mathbb R}_{3,\infty}=4\).

Interpolating these two **real endpoint values as though their sharp norms were log-convex with constant one** would predict \(C^{\mathbb R}_{3,3}\le4^{1/3}\), because \(1/3=(2/3)/2+(1/3)/\infty\). But \(\varphi=(1+\sqrt5)/2\) satisfies \(\varphi^3=2+\sqrt5>4\). The explicit real witness therefore disproves that proposed interpolation inequality. Ordinary multilinear *complex* interpolation is unaffected: complex Fourier matrices give a larger complex endpoint constant \(3^{3/2}\), rather than the real endpoint \(4\).

## Verification

The exact determinant is checked by the eigenvalue factorization of \(M_r\); the derivative calculation is a rational identity in \(r\) and \(r^{p-1}\). The three-region argument covers all real \(r\), including negative values and the diagonal subfamily. The finite-dimensional witness embeds isometrically in any real coordinate \(\ell_p\). A standalone \`verification.py\` script performs exact integer sign-matrix enumeration for the sharp \(\ell_\infty\) endpoint, tests determinant identities at rational arguments, and numerically checks the critical-point identity for several exponents. These computations corroborate, rather than replace, the complete analytic proof.

## Relationship to prior work

D. V. Feldman (arXiv:2608.00983, first public August 2, 2026) establishes the Plücker-coordinate boundedness theorem, unit sharp constant up to the Hilbert exponent, and the Hadamard-sign-matrix lower bound above it. Its Problem P1 asks for sharp super-Hilbert constants. The present theorem does not claim to determine those unrestricted real constants: it gives an exact optimization over the natural simultaneous-permutation commutant and, at the first odd order, improves the elementary sign-matrix witness. At \(p=3\), the sign-matrix lower bound in dimension three is \(4/3\), while the present lower bound is \(\varphi\).

The separate publicly available note *Exact complex Plücker constants above the Hilbert exponent* proves \(C^{\mathbb C}_{n,p}=n^{n(1/2-1/p)}\) for complex scalar fields and supplies the upper bound \(C^{\mathbb R}_{n,p}\le C^{\mathbb C}_{n,p}\). At \(n=p=3\), this gives the **upper** bound \(\sqrt3\), not the lower bound \(\varphi\) or its unique real permutation-equivariant extremizer. Complex interpolation does not recover the smaller real endpoint constant \(4\).

The classical Hadamard maximal-determinant problem and its modern survey concern sign matrices, i.e. the real \(\ell_\infty\) endpoint; the non-sign interior maximizing matrix at finite \(p\) is the novel object here. No conclusion of priority beyond the particular compared sources is claimed.

## Limitations

The unrestricted real constant \(C^{\mathbb R}_{3,p}\) is not proved equal to \(B_p\), even at \(p=3\). Global extremizers outside \(\mathcal E\) are not classified. The counterexample concerns the formal interpolation of *sharp real endpoint constants*, not complex multilinear interpolation. The isolated parameter formula is for three columns, and no higher-order classification is asserted. The closest publicly indexed result's statement was checked in full, but equivalents in older determinant and real tensor-norm literature remain a residual priority risk.

## References

1. D. V. Feldman, *Plücker coordinates of finite-dimensional subspaces of \(\ell^p\) and its direct sums: summability, reconstruction, stratification*, arXiv:2608.00983 (submitted August 2, 2026). https://arxiv.org/abs/2608.00983
2. *Exact complex Plücker constants above the Hilbert exponent* (September 17, 2026), public mathematical note. https://github.com/Resultary/2026/blob/main/2026/9/17/SCOPE-complex-plucker-sharp-constants--7196b90b39f6/RESULT.md
3. P. Browne, R. Egan, F. Hegarty, and P. Ó Catháin, *A Survey of the Hadamard Maximal Determinant Problem*, Electron. J. Combin. 28(4), P4.41 (2021). https://doi.org/10.37236/10367
