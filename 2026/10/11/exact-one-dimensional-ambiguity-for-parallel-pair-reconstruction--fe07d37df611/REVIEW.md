# Same-model review

## Correctness

PASS. The source's Theorems 7.4 and 7.5 justify representing a common locus by normalized Jacobians \(J(F,G_i)\). For a parallel pair one may take \(F=(Y-\alpha)(Y-\beta)\), and direct differentiation gives
\[
J(F,H)=-(2Y-\alpha-\beta)(2aX+bY+r)
\]
for a general quadratic \(H=aX^2+bXY+cY^2+rX+sY+t\). Characteristic different from \(2\) makes the first factor nonzero, so the kernel is exactly \(\operatorname{span}\{1,F,Y\}\). The quotient by the two trivial generator directions is therefore one-dimensional. Equality of nets is equivalent to vanishing of that quotient class after Jacobian normalization. The source's Example 7.6 gives the exact nonzero defect \(3/2\).

## Originality

PASS. The primary paper proves the corresponding kernel statement only for a nonparallel pair and then gives a single parallel counterexample. It does not state the parallel kernel or classify the defect. Earlier shared-nine-point-conic and bisector-field literature provides families and context but no covering reconstruction theorem. Targeted searches across source identifiers, aliases, Jacobian-kernel language, and nine-point-conic formulations found no equivalent statement.

## Value

PASS. This is the exact missing companion to a principal reconstruction theorem in the source. Rather than merely observing that the parallel case may fail, it proves that the failure has one and only one additional algebraic degree of freedom and gives an iff criterion for when that defect disappears. The conclusion is structural and applies to all allowed quadrangles over every field of characteristic different from \(2\).

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Olberding--Walker, arXiv:2610.02020v1, especially Theorem 7.5 and Example 7.6. Čerin--Gianella give an older special real family of quadrangles sharing a nine-point conic. Earlier bisector-field papers explain the role of parallel line pairs in pencils.

The result does not assert that every scalar value of the one-dimensional algebraic ambiguity is realized by quadrangles with fixed reconstruction data. Full-text access to one older bisector-field paper timed out, so equivalence under substantially different older terminology remains a residual bibliographic risk.
