# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS.

For a B-linear leakage map `ell:F -> V`, the set of field elements preserving `ker(ell)` is closed under addition and multiplication, contains B, and is closed under inverses because multiplication by a nonzero field element preserves the dimension of the kernel. It is therefore a subfield. Kernel preservation is exactly what is needed for multiplication by a coefficient to descend to a well-defined B-linear map on the leaked value.

If every coefficient of a systematic computation matrix belongs to the intersection of these stabilizer fields, the leakage of each computed share coordinate is a B-linear function of the corresponding input leakages. Hence the full leakage vector factors through the input-block leakage vector, while the latter is also a projection of the full vector. No information is added by the computed blocks. Restricting a product-code reconstruction to one nonzero input block proves the base-code implication; the converse follows by repairing the input blocks separately.

For `ell_beta(x)=Tr_{F/B}(beta x)` with `beta != 0`, the quotient by the kernel is one-dimensional. Kernel preservation therefore gives `Tr(beta a x)=lambda Tr(beta x)` for some `lambda in B` and every `x`. Nondegeneracy of the finite-field trace pairing forces `a=lambda`, so the stabilizer is exactly B.

The matrix corollary follows independently from the same mechanism. With identical diagonal leakage matrices and `G_comp` over B, the generalized matrices are Kronecker products after base-field expansion. Kronecker rank multiplicativity gives a generalized rank gap equal to K times the base rank gap. Thus the generalized full-rank condition holds exactly when the base full-rank condition holds.

The finite verification artifact checks the trace stabilizer and representative rank-factor identities over GF(8)/GF(2). It also exhibits the complementary phenomenon that multiplication by an element outside GF(2) can make a second trace leakage linearly independent of the first. These finite checks support, but do not replace, the general proof.

## Originality

PASS, to the best of our knowledge.

The primary source inspected in full is Aoutouf--Augot, arXiv:2609.19929v1, submitted 17 September 2026. It proves the no-improvement statement for identical leakage under the simple relation `u+v=w`, says the same observation appears to extend to its array-summation example, and reports simulation evidence that identical leakage can work for more general coefficient relations and an LFSR. It gives a general rank criterion for arbitrary linear computation codes, but does not state a stabilizer-field theorem, the all-base-field-computations obstruction, or the exact Kronecker rank-factorization corollary.

The preceding WCC 2026 paper by the same authors was also inspected. It treats the single-codeword/base LERS construction via subfield subcodes and does not contain the multiple-computation setting addressed here.

Targeted literature searches used the motivating title and arXiv identifier together with `identical leakage`, `same leakage`, `base field`, `subfield`, `linear computation`, `trace leakage`, `stabilizer`, and `linear exact repair`, as well as exact phrases around the general rank criterion. No source located stated the present general obstruction or its stabilizer-field formulation. Searches of the current SCOPE repository by Massey, secret-sharing leakage, identical leakage, and linear exact repair terminology found no overlapping successful record. Recent repository changes were also checked before acceptance.

No specifically identified inaccessible paper emerged as a likely source of exact prior coverage. The dominant originality risk is temporal: arXiv:2609.19929 is extremely recent, so a near-simultaneous note, author revision, or not-yet-indexed response could independently contain the same observation. A secondary risk is that the kernel-stabilizer argument may exist in more abstract leakage or module language without being indexed under Massey secret sharing or LERS terminology.

The novelty claim is deliberately narrow: the general stabilizer-field obstruction for identical B-linear leakage, the proof that trace leakage has stabilizer exactly B, and the resulting exact rank-factorization/collapse for all base-field-defined computation codes. The underlying Massey construction, LERS framework, trace leakage, and the simple-addition no-improvement result are credited to prior work.

## Value

PASS.

The result replaces a single-operation phenomenon with an exact structural boundary. It proves the array-summation extension suggested by the motivating paper, covers arbitrary base-field linear circuits and intermediate values, and explains why extension-field coefficients can behave differently. The trace specialization is sharp: coefficients inside B can add no leakage information, while coefficients outside B are precisely where the kernel obstruction disappears. This directly narrows the search space for realistic identical-leakage attacks and clarifies how to interpret simulation evidence for general linear relations.

The general leakage-stabilizer formulation is also reusable beyond one-symbol traces: it identifies the largest subfield over which a reused B-linear leakage map commutes with scalar computation.

## Limitations

The theorem concerns identical leakage maps reused across computation blocks. It does not constrain attacks that choose independent leakage maps per block. Outside-stabilizer coefficients are necessary for computed blocks to add information but are not sufficient for successful secret recovery. Nonlinear computations and multiplication are not treated. The finding has no cross-model or independent validation.
