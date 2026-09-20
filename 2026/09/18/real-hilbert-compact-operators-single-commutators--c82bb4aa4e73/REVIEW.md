# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**Passed.**

The argument was checked against the theorem-level structure of Liu's arXiv:2609.20672 and Tran's arXiv:2609.20161.

Tran supplies exactly the field-sensitive finite-dimensional input needed in Liu's zero-diagonal construction: a dimension-free commutator bound with real factors for real traceless matrices. Liu's subsequent scalar shifts, Sylvester equations, direct sums, compactness estimates, and block assembly are valid over the real field.

The main real obstruction is the non-trace-class skew-adjoint case. The calculation
\[
\operatorname{Sym}\!\left(
\operatorname{diag}(1/2,2)
\begin{pmatrix}0&-s\\s&0\end{pmatrix}
\operatorname{diag}(2,1/2)
\right)
=
\frac{15s}{8}\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
was checked directly. The resulting trace norm is \(15s/4\), so a non-trace-class skew-adjoint compact operator acquires a non-trace-class symmetric part under a fixed uniformly bounded real similarity.

The trace-class trace-zero step was treated through a real self-adjoint carry-rotation lemma rather than by silently importing the complex diagonal theorem. The trace-nonzero branch was also checked for a hidden field issue: Liu invokes polarization to find \(u\) with \(\langle Tu,u\rangle\ne0\), which is false for a nonzero real skew-adjoint operator. In the branch where the lemma is actually used, \(\operatorname{Tr}T\ne0\), so the symmetric part is nonzero and the required real vector exists.

Anderson's rank-one construction has explicit real block coefficients; therefore Liu's finite-rank tensor amplification can be performed over \(\mathbb R\).

## Originality

**Passed, to the best of our knowledge.**

Liu explicitly assumes complex Hilbert spaces and states the compact-commutator theorem only in that setting. Tran proves the required real estimate only for finite matrices. Searches for "real Hilbert", "compact operators", "commutator of compact operators", "Pearcy--Topping", and zero-diagonal/similarity variants did not locate the infinite-dimensional real theorem with universal factor control.

The SCOPE repository was searched by the identifiers arXiv:2609.20672 and arXiv:2609.20161, by "real Hilbert compact commutator", and by synonymous commutator terminology; no overlapping successful record was found before publication.

Residual prior-art risk remains in older sources. In particular, the full original texts of Anderson (1977) and Fan--Fong (1987) were not exhaustively checked for a separately stated global real-field theorem. General real operator-algebra literature could also formulate the same conclusion in different language. No such coverage was found in the searches performed.

## Value

**Passed.**

The result closes the scalar-field gap in a newly solved classical compact-commutator problem while retaining dimension-free quantitative control. The extension is mathematically substantive rather than formal: the real skew-adjoint branch requires a new fixed-conditioning similarity that converts skew mass into symmetric mass.

## Limitations

The constant is not optimized. The theorem is restricted to separable infinite-dimensional real Hilbert spaces and does not address smaller prescribed operator ideals, arbitrary real Banach spaces, or nonseparable Hilbert spaces.
