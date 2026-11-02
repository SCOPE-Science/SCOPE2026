# The sharp \(1+1/n\) two-sweep positivity frontier for SOR

## Finding

For each integer \(n\ge2\), consider ordinary forward successive overrelaxation (SOR), in a fixed coordinate order, starting from \(x^{(0)}=0\), on any real nonsingular \(n\)-by-\(n\) \(M\)-matrix \(A\) with right-hand side \(b\ge0\). Let the relaxation parameter satisfy \(0<\omega<2\). Then the second iterate is nonnegative for **every** such \(A,b\) if and only if
\[
\boxed{0<\omega\le 1+\frac1n.}
\]
The first iterate is always nonnegative. More precisely, whenever \(\omega>1+1/n\) but \(\omega<2\), a *symmetric positive-definite tridiagonal Stieltjes matrix* provides a counterexample with a positive first iterate, a strictly positive exact solution, and a negative coordinate in the second iterate. The right-hand side can also be chosen strictly positive.

There is an ordering-sensitive refinement: write \(A=D-E-F\), with \(D\) its positive diagonal, \(E\ge0\) strictly lower triangular, and \(F\ge0\) strictly upper triangular. If the nilpotency index of \(L=D^{-1}E\) is \(q\), meaning \(L^q=0\) and \(L^{q-1}\ne0\) (or \(q=1\) if \(L=0\)), then every such system has a nonnegative second iterate throughout
\[
0<\omega<2,\qquad \omega\le1+\frac1q.
\]
The dimension-only frontier is sharp because increasing-order path matrices realize \(q=n\). The refinement is a sufficient guarantee for a specified sparsity/order pattern, not a claimed necessary bound for every fixed matrix.

As the dimension grows, the best universal positive overrelaxation margin for this two-sweep property shrinks exactly like \(1/n\), despite the larger classical SOR convergence range on symmetric positive-definite systems.

## Assumptions and scope

The statement uses **two full forward sweeps**, with the same fixed ordering on both sweeps, no projection onto the nonnegative cone, and an initial vector equal to zero. All inequalities between vectors or matrices are coordinatewise. The class of nonsingular \(M\)-matrices has positive diagonal, nonpositive off-diagonal entries, and nonnegative inverse. Symmetry is not needed for the universal sufficient bound. Counterexamples are symmetric positive definite.

Normalize the strict parts by defining \(L=D^{-1}E\), \(U=D^{-1}F\), and \(g=D^{-1}b\). Both \(L\) and \(U\) are nonnegative, and \(L\) is nilpotent. Ordinary forward SOR is
\[
(I-\omega L)x^{(k+1)}=((1-\omega)I+\omega U)x^{(k)}+\omega g.
\]
This is **not** a claim that every later iterate remains nonnegative, or that general nonsymmetric \(M\)-matrix SOR converges for every \(0<\omega<2\). For the symmetric positive-definite sharpness witnesses, convergence throughout that range is classical.

## Proof

Put \(R=(I-\omega L)^{-1}\). Since \(L^q=0\),
\[
R=\sum_{j=0}^{q-1}(\omega L)^j\ge0.
\]
Starting from zero gives \(x^{(1)}=\omega Rg\ge0\). One additional SOR sweep yields the exact response
\[
\begin{aligned}
x^{(2)}
&=\omega\bigl(R+(1-\omega)R^2+\omega RUR\bigr)g.
\end{aligned}
\]
All factors in \(RUR\) are nonnegative. The finite geometric-series identity and its square give
\[
R+(1-\omega)R^2
=\sum_{j=0}^{q-1}\bigl(j+2-(j+1)\omega\bigr)(\omega L)^j.
\]
For \(0<\omega\le1\), every coefficient is positive. For \(1<\omega\le1+1/q\), the smallest coefficient occurs at \(j=q-1\) and equals \(q+1-q\omega\ge0\). Hence \(x^{(2)}\ge0\) whenever \(\omega\le1+1/q\). As \(q\le n\), the uniform guarantee \(\omega\le1+1/n\) follows.

To show the dimension-only bound is sharp, fix \(n\ge2\) and \(1+1/n<\omega<2\). Let \(T_n\) be the adjacency matrix of the ordinary \(n\)-vertex path, and put
\[
A_\varepsilon=I-\varepsilon T_n,
\qquad0<\varepsilon<\frac12,
\qquad b=e_1.
\]
The matrix is symmetric, strictly diagonally dominant, positive definite and a nonsingular \(M\)-matrix. Its strict normalized lower part is \(L=\varepsilon\sum_{j=1}^{n-1}e_{j+1}e_j^{\mathsf T}\), and its upper part is \(U=L^{\mathsf T}\). The unique increasing lower-triangular path from coordinate \(1\) to coordinate \(n\) has length \(n-1\). Thus the \((n,1)\) entry of \(\omega[R+(1-\omega)R^2]\) equals exactly
\[
\omega^n\varepsilon^{n-1}(n+1-n\omega).
\]
Every walk contributing to the \((n,1)\) entry of \(\omega^2RUR\) uses an upper step, and therefore at least \(n+1\) path edges. Its contribution is nonnegative and \(O(\varepsilon^{n+1})\) for fixed \(n,\omega\). Consequently,
\[
(x^{(2)})_n
=\omega^n\varepsilon^{n-1}(n+1-n\omega)
+O(\varepsilon^{n+1})<0
\]
for all sufficiently small positive \(\varepsilon\). The first iterate is strictly positive, since \(Re_1\) has positive entries in all positions. The exact solution is strictly positive by the Neumann series
\[
A_\varepsilon^{-1}e_1=\sum_{k=0}^\infty\varepsilon^kT_n^ke_1>0.
\]
Since the inequality in the second iterate is strict, replacing \(e_1\) by \(e_1+\delta\mathbf1\) for a sufficiently small \(\delta>0\) preserves the failure and makes the right-hand side strictly positive. This completes sharpness for every \(n\) and every parameter above the frontier in the classical convergent range.

A concrete three-dimensional example takes \(n=3\), \(\varepsilon=1/10\), \(\omega=3/2\), and \(b=e_1\). Exact arithmetic gives
\[
(x^{(2)})_3=-\frac{2457}{160000}<0,
\]
even though \(\omega=3/2<2\) and the matrix is symmetric positive definite.

## Verification

The standalone `verify.py` reconstitutes the two forward sweeps directly from their component recurrence and independently computes the finite-resolvent expression. It compares the resulting response matrices over rational tests in dimensions \(1\) through \(12\), including both symmetric and nonsymmetric nonnegative strict parts, exact endpoint and nearby relaxation values, and several sparse patterns. It then checks symmetric positive-definite tridiagonal path witnesses in dimensions \(2\) through \(20\), including strict negativity above the frontier and entrywise nonnegativity at the frontier. Execution with Python 3 yields `VERIFY_OK exact assertions = 11368`.

The finite tests are not the proof for arbitrary dimension or all matrices. The proof is the nilpotent coefficient identity and the \(\varepsilon\)-asymptotic path argument above. No numerical optimization, symbolic black box, or external dependency is required.

## Relationship to prior work

Vigna's 2014 arXiv study of step-asynchronous SOR on \(M\)-matrices establishes computable error-norm convergence bounds and the general matrix-splitting setting, not the universal coordinatewise sign of the second forward iterate. Classical SOR convergence treatments, including James and Riha (1975), concern long-run convergence and generalized diagonal dominance.

The published finding *A sharp three-halves second-iterate positivity frontier for SOR* (2026) already covers the full \(2\)-dimensional symmetric positive-definite case. Its threshold \(3/2\) agrees with the \(n=2\) specialization here, and that specialization is not claimed as new. The result here is the dimension-sharp theorem **simultaneously for all \(n\ge3\), including nonsymmetric nonsingular \(M\)-matrices**, together with the nilpotency-index refinement and path-matrix sharpness for every dimension. The earlier two-dimensional theorem explicitly does not claim higher-dimensional coverage.

Yun's 2005 result that overrelaxed \(M\)-matrix SOR splittings are not weak regular for \(\omega>1\) is not inconsistent with a positive *two-sweep response* on a nontrivial interval above \(1\): weak regularity controls a different splitting-positivity condition. The precise comparison with earlier inaccessible full texts is recorded as a residual risk, not as evidence of noncoverage.

## Limitations

The guaranteed property is only at the **second iterate from zero**, not the whole SOR trajectory, and it is relative to a fixed forward order. The nilpotency-index bound may be conservative on an individual matrix because its upper-triangular correction can prevent negativity. The symmetric path witnesses use arbitrarily weak coupling; they are not statements about how commonly negativity appears in well-coupled applications. The mathematical proof is exact, but independent review and exhaustive historical coverage have not occurred. In particular, older monographs and inaccessible specialized articles may contain equivalent finite-sweep facts.

## References

1. S. Vigna, *Supremum-Norm Convergence for Step-Asynchronous Successive Overrelaxation on M-matrices*, arXiv:1404.3327, first posted 2014-04-12, https://arxiv.org/abs/1404.3327.
2. K. R. James and W. Riha, *Convergence Criteria for Successive Overrelaxation*, SIAM J. Numer. Anal. 12 (1975), 137–143, DOI:10.1137/0712013.
3. J. H. Yun, *A Note on SOR(ω) Splitting of an M-Matrix*, J. Comput. Appl. Math. 176 (2005), 461–462, DOI:10.1016/j.cam.2004.07.029.
4. *A sharp three-halves second-iterate positivity frontier for SOR* (2026), published record: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-sharp-three-halves-second-iterate-positivity-frontier-for-sor--7f04f29ca2ea.
