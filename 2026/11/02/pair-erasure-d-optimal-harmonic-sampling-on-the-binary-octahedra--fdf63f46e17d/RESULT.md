# Pair-erasure D-optimal harmonic sampling on the binary octahedral configuration

## Finding
Let \(Q\) be the binary octahedral group of 48 unit quaternions and let \(X=Q/\{\pm1\}\) be its 24 antipodal classes. At exact spherical-harmonic degree 12, take the real symmetric kernel
\[
B_{x,y}=U_{12}(\langle x,y\rangle),\qquad x,y\in X,
\]
where \(U_{12}\) is the Chebyshev polynomial of the second kind. The even degree makes the entry independent of the chosen representatives. For distinct \(x,y\in X\), let \(B_{\widehat{x,y}}\) be the 22-by-22 principal submatrix obtained by retaining all other points.

**Theorem.** The matrix \(B\) is positive definite and has spectrum
\[
24^{[2]},\quad 12^{[4]},\quad 8^{[9]},\quad 16^{[9]},
\]
where brackets denote multiplicities. Put
\[
\Delta=24^2\,12^4\,8^9\,16^9=\det B.
\]
Identify \(X\) with \(S_4\) via the quotient \(Q/\{\pm1\}\cong S_4\), and classify a deleted unordered pair by the conjugacy class of \(x^{-1}y\). The exact complete two-erasure determinant census is

| Relative conjugacy class | Number of pairs | \(1152^2\det(B_{\widehat{x,y}})/\Delta\) |
| --- | ---: | ---: |
| 3-cycle | 96 | 10185 |
| double transposition | 36 | 10152 |
| 4-cycle | 72 | 10120 |
| transposition | 72 | 10120 |

Thus the **96 and only 96 optimal retained 22-point designs** arise by deleting a pair whose quotient difference is a 3-cycle. The exact best-to-worst retained Gram determinant ratio is \(2037/2024\), and every possible two-erasure design remains nonsingular. The optimality criterion is the determinant (squared volume) of the degree-12 evaluation Gram matrix, rather than any condition-number claim.

## Assumptions and scope
Identify the quaternion units \(1,i,j,k\) with the standard coordinate vectors of \(\mathbb R^4\). Explicitly, \(Q\) consists of
\[
\{\pm1,\pm i,\pm j,\pm k\}\ \cup\
\left\{\frac{\pm1\pm i\pm j\pm k}{2}\right\}\ \cup\
\left\{\frac{\pm e_a\pm e_b}{\sqrt2}:0\le a<b\le3\right\},
\]
with independent choices of signs. These three parts have 8, 16, and 24 elements. The Euclidean inner product on \(\mathbb R^4\) is used. Define \(U_0(t)=1\), \(U_1(t)=2t\), and \(U_{r+1}(t)=2tU_r(t)-U_{r-1}(t)\). The addition theorem on the unit 3-sphere shows that this normalization is a positive multiple of the exact-degree harmonic evaluation Gram kernel, with diagonal value \(U_{12}(1)=13\). Determinants refer to the 24-by-24 kernel on antipodal classes, not to the 48-by-48 matrix on signed points.

The result concerns precisely two deleted classes at harmonic degree 12. It does not characterize other degrees, larger deletion sets, or other objective functions.

## Proof
**Step 1: a central Cayley kernel.** The quotient \(Q/\{\pm1\}\) is the rotation group of the cube, isomorphic to \(S_4\). Distinct quotient elements have quaternion inner-product magnitudes \(0\), \(1/2\), or \(1/\sqrt2\). The latter class consists exactly of the six 4-cycles of \(S_4\). The elementary recurrence gives
\[
U_{12}(1)=13,\qquad U_{12}(0)=U_{12}(1/2)=1,\qquad U_{12}(1/\sqrt2)=-1.
\]
Because the polynomial is even, all sign choices are immaterial. With \(A\) the Cayley adjacency matrix on \(S_4\) using its six 4-cycles, and \(J\) the 24-by-24 all-ones matrix, this yields the exact identity
\[
B=12I+J-2A.
\]

**Step 2: the full spectrum.** In order trivial, sign, two-dimensional, standard three-dimensional, and sign-twisted standard three-dimensional, the irreducible representation dimensions of \(S_4\) are \(1,1,2,3,3\). Their character values on 4-cycles are respectively \(1,-1,0,-1,1\). Central convolution by the six 4-cycles has eigenvalues \(6\chi(4\text{-cycle})/\dim\chi\), i.e. \(6,-6,0,-2,2\); the regular multiplicities are the squared dimensions. The all-ones matrix is 24 on the trivial summand and zero otherwise. Consequently the eigenvalues of \(B\) are, in the same representation order, \(24,24,12,16,8\), with multiplicities \(1,1,4,9,9\). In particular, \(B\) is positive definite and has the stated determinant \(\Delta\).

**Step 3: exact inverse correlations.** For \(h=x^{-1}y\), the central Fourier inverse is
\[
(B^{-1})_{x,y}=\frac1{24}\sum_{\chi\in\widehat{S_4}}
\frac{\dim\chi}{\lambda_\chi}\chi(h),
\]
where \(\lambda_\chi\) is the eigenvalue from Step 2. The needed character values on the four nonidentity classes, in the same representation order, are
\[
\begin{array}{c|rrrrr}
&\mathbf 1&\mathrm{sgn}&\mathrm{dim}2&\mathrm{std}&\mathrm{std}\otimes\mathrm{sgn}\\\hline
(abc)&1&1&-1&0&0\\
(ab)(cd)&1&1&2&-1&-1\\
(abcd)&1&-1&0&-1&1\\
(ab)&1&-1&0&1&-1
\end{array}
\]
so direct substitution gives
\[
(B^{-1})_{x,x}=\frac{101}{1152},\quad
(B^{-1})_{x,y}=\frac1{1152}
\begin{cases}
-4,&h\text{ a 3-cycle},\\
-7,&h\text{ a double transposition},\\
+9,&h\text{ a 4-cycle},\\
-9,&h\text{ a transposition}.
\end{cases}
\]

**Step 4: every two-erasure determinant and all optimizers.** Jacobi's complementary principal-minor identity for an invertible matrix gives
\[
\frac{\det(B_{\widehat{x,y}})}{\det B}
=\det\begin{pmatrix}(B^{-1})_{x,x}&(B^{-1})_{x,y}\\
(B^{-1})_{y,x}&(B^{-1})_{y,y}\end{pmatrix}
=\frac{101^2-b_h^2}{1152^2},
\]
where \(b_h\in\{-4,-7,9,-9\}\) is determined in Step 3. The four numerator values are \(10185,10152,10120,10120\). Every element has exactly 8, 3, 6, and 6 distinct partners in the respective conjugacy classes. Dividing the 24 times these values by two gives exactly 96, 36, 72, and 72 unordered pairs, whose sum is \(\binom{24}{2}=276\). Only the 3-cycle class maximizes the determinant, proving the complete census and all equality cases. All numerators are positive, so every retained Gram is nonsingular. The ratio between the maximal and minimal determinants reduces to \(10185/10120=2037/2024\). \(\square\)

## Verification
Run `python check_erasure.py` with Python 3, NumPy, and SymPy. The standalone program builds the 48 explicit unit quaternions, chooses 24 antipodal representatives, computes the degree-12 Chebyshev Gram entries from the recurrence, classifies every one of the 276 unordered pairs from quaternion multiplication, and verifies the integer matrix \(12I+J-2A\). It then computes the exact characteristic polynomial and rational inverse of the resulting 24-by-24 integer matrix, checks every inverse pair entry and its class count, and computes one exact 22-by-22 principal determinant for **each of the four classes**. All assertions passed. Floating arithmetic is used only for recognizing explicitly listed quaternion-coordinate classes; the matrix spectrum, inverse, and determinant tests are exact integers/rationals. The infinite or general-group conclusions used here follow from the analytic character argument, not extrapolation from the program.

## Relationship to prior work
Weeks (2005), especially Section 11, explicitly constructs binary-octahedral invariant spherical eigenmodes on a homogeneous space. That is distinct from the point-evaluation Gram and selection determinants for the 24 antipodal classes in the group itself. Evans and Pugh (2009) give classical affine-McKay and character/spectral-measure data for the binary octahedral group, which explain the representation-theoretic ingredients but do not provide the two-erasure determinant census. Hirao, Nozaki, and Tasaka (2025) analyze spherical design properties of finite quaternionic unit groups; their design-strength results are also distinct from D-optimal two-point deletion. The group and its characters, the harmonic addition formula, and Jacobi's identity are classical inputs, not asserted as new. The only claimed contribution here is their exact combination into the 24-point degree-12 two-erasure design classification, including its optimizer geometry and census.

## Limitations
The theorem does not establish novelty beyond the inspected and searched sources: an older treatment of association-scheme principal minors, finite spherical interpolation, or statistical D-optimality could contain an equivalent formula. The numerical advantage of the optimal over the worst two-erasure pattern is modest; mathematical interest lies in classifying **all** geometrically inequivalent pair losses and all exact optimal designs for a canonical configuration. An independent mathematical audit has not been performed. No general statement is claimed for three or more erasures.

## References
1. J. R. Weeks, *Exact Polynomial Eigenmodes for Homogeneous Spherical 3-Manifolds*, arXiv:math/0502566 (first public 2005-02-27), Section 11: https://arxiv.org/abs/math/0502566.
2. D. E. Evans and M. Pugh, *Spectral Measures and Generating Series for Nimrep Graphs in Subfactor Theory*, arXiv:0906.4314 (first public 2009-06-23): https://arxiv.org/abs/0906.4314.
3. T. Hirao, H. Nozaki, and K. Tasaka, *Spherical designs for finite quaternionic unit groups and their applications to modular forms*, arXiv:2507.01358 (first public 2025-07-02): https://arxiv.org/abs/2507.01358.
