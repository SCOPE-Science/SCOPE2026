# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The determinant identity was checked algebraically and against random numerical tests over positive-definite \(2\times2\) matrices and Hermitian partners.

The proof does not rely on an unverified inheritance or complementability assertion. After unitary diagonalization of \(A\), write
\[
X=BA^2B,\qquad Y=AB^2A.
\]
These are respectively \(|AB|^2\) and \(|BA|^2\). Since \(BA=(AB)^*\), \(X\) and \(Y\) have the same spectrum. In dimension two, the functional calculus difference \(X^{p/2}-Y^{p/2}\) is a scalar divided difference times \(X-Y\). The diagonal entries of \(X-Y\) are computed explicitly, and the two added matrices have equal determinant. Expanding a \(2\times2\) determinant then gives
\[
\Delta_{k,p}
=
\alpha_p |z|^2(b^2-a^2)(b^k-a^k).
\]
The divided difference has the sign of \(p\), and the second factor has the sign of \(k\). The equality condition for nonzero \(k,p\) reduces exactly to \(A\) and \(B\) commuting. Negative exponents are used only when the relevant matrices are invertible.

The positive-exponent semidefinite extension is justified by continuity. No numerical experiment is used in place of proof.

## Originality — PASS

Lin's 2017 work introduced the determinant-comparison direction. Ghabries–Abbas–Mourad (2020) proved the \(k=2\), \(p\ge0\) inequality in the Hermitian setting. Abbas–Ghabries–Mourad (2021) established related arbitrary-\(k\) statements for a different comparison involving \((AB)^2\). Ghabries's 2022 thesis explicitly formulates the broader \(k,p\ge0\) comparison and records only partial parameter ranges; it also formulates the reverse nonpositive-\(p\) comparison under invertibility assumptions.

The 2026 Ghabries normal-matrix preprint was checked at the level of its stated main determinant application. It extends a \(k=2\)-type result to normal matrices but does not state the arbitrary-\(k\) two-dimensional phase law.

Targeted searches using the exact determinant expressions, the thesis conjecture numbering, two-dimensional/2×2 terminology, positive and negative powers, and equality/commutation formulations did not locate the exact order-two formula or the full sign-\(kp\) phase diagram. Because low-dimensional matrix inequalities are classical and dispersed, an older equivalent observation cannot be excluded. Originality is therefore asserted only to the best of our knowledge.

## Value — PASS

The result converts two parameter-range conjectures into a complete and sharp two-dimensional classification. It supplies an explicit gap formula, includes both positive and negative exponents in one statement, identifies the exact strictness boundary by commutation, and explains why dimension two is special. This is stronger and more informative than merely verifying a few unresolved parameter values.

## Limitations checked

No claim is made for dimensions \(n\ge3\). The proof mechanism depends essentially on two spectral values and the degree-two determinant expansion. For negative matrix powers, \(A\) and \(B\) are assumed invertible. The result does not settle the separate comparison with \(A^pB^p\).
