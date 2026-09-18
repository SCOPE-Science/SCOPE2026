# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.** The core operator inequality follows from the standard positive block
\[
\begin{bmatrix}|X_j^*|&X_j\\X_j^*&|X_j|\end{bmatrix}\ge0
\]
and the polar decomposition of the invertible sum \(X=\sum_jX_j\). It gives
\[
U^*PU+Q\ge2|X|\ge2a1.
\]
If the low spectral projection \(E=\mathbf1_{[0,a)}(P+Q)\) met its polar-unitary conjugate nontrivially, a vector in the intersection would make both the \(Q\) and \(U^*PU\) quadratic forms strictly smaller than \(a\), contradicting the displayed lower bound. Thus \(E\wedge U^*EU=0\).

For a finite von Neumann algebra, modularity of center-valued dimension on projections and unitary invariance give
\[
2\operatorname{Tr}_Z(E)=\operatorname{Tr}_Z(E\vee U^*EU)\le1.
\]
The polar-Hermitian strengthening is checked separately: adding the basic inequality to its conjugate yields
\[
\mathsf S+V\mathsf S V\ge2a1,
\]
so the same intersection argument works at threshold \(a\). The \(M_3\) examples in Aouichaoui--Lee verify sharpness of the general \(a/2\) threshold, and their one-sided-modulus example verifies that symmetrization cannot simply be removed.

Potential edge cases were checked: invertibility of \(X\) makes the polar factor unitary; the spectral interval is open at the threshold, which is needed for the strict quadratic-form contradiction; no compactness or discreteness of the spectrum is used; and finiteness is invoked only for the center-valued dimension conclusion, not for the meet-zero statement.

## Originality

**PASS, to the best of our knowledge.** Aouichaoui--Lee arXiv:2609.20094v1 proves the finite-matrix median eigenvalue inequality and sharpness but does not state a von Neumann algebra, spectral-projection, Murray--von Neumann comparison, or center-valued-trace version. Bourin--Lee arXiv:2602.19607v1 develops the symmetric modulus for matrices and proves stronger finite-matrix statements for polar-Hermitian sums, but likewise does not state the projection-wandering formulation.

Targeted searches for combinations of "symmetric modulus", finite/semifinite von Neumann algebras, spectral projections, center-valued traces, and polar-unitary projection intersections did not locate the theorem above. Related operator-algebra literature does exist: Nurahemet--Ospanov, DOI 10.7153/oam-2023-17-45, extends several \(2\times2\) positive-block and generalized-singular-number inequalities to tau-measurable operators. The available article text and theorem descriptions were inspected for a matching symmetric-modulus median or polar-wandering statement, and none was located. This is the principal prior-art risk because generalized-singular-number technology can often reproduce matrix eigenvalue arguments in semifinite algebras.

No specifically identified inaccessible paper produced concrete evidence of coverage. The remaining uncertainty is broader terminology risk: a spectral-scale or generalized-\(s\)-number paper could contain an equivalent half-distribution inequality without using "symmetric modulus" or "polar-wandering" language. For that reason the originality claim is limited to the specific structural formulation and center-valued consequence, not to the standard block-positivity ingredients.

## Value

**PASS.** The result turns a sharp finite-dimensional median eigenvalue inequality into an operator-algebraic packing principle:
\[
E\wedge U^*EU=0.
\]
That statement survives in arbitrary von Neumann algebras. In finite algebras it immediately gives a center-valued half-dimension bound and hence Murray--von Neumann subequivalence \(E\precsim1-E\), covering type II settings where an ordered list of eigenvalues does not exist. The same mechanism also yields the sharper polar-Hermitian threshold and cleanly explains why the matrix result is a median phenomenon. Sharpness and failure of the one-sided-modulus analogue are inherited from explicit low-dimensional examples.

## Limitations

The theorem is a structural extension of recent matrix inequalities, not a claim that the positive-block method itself is new. It does not establish a full Fack--Kosaki singular-value inequality, does not treat arbitrary unbounded tau-measurable summands, and gives no normalized half-dimension statement in properly infinite algebras. The main originality risk is equivalent coverage in the literature on generalized singular values or spectral scales under different terminology.
