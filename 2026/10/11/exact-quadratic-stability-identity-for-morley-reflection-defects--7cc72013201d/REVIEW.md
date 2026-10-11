# Same-model review

## Correctness

PASS. The source gives
\[
a\cdot v=(q-1)(t_i+t_j),
\qquad
|a|^2=(q-1)^2(q+2),
\]
for
\[
a=n_i-n_j,
\qquad
v=M_j-M_i.
\]
Subtracting the squared component along \(v\) shows that the perpendicular component has squared norm exactly
\[
(q-1)^2\varepsilon_{ij}.
\]
The remaining vertices of the regular Morley simplex, measured from the midpoint of \(M_iM_j\), have Gram matrix
\[
\frac{L^2}{4}(2I+J),
\]
whose inverse is explicit. This gives the claimed quadratic identity exactly. The scale and pointwise estimates follow from the source's second projection inequality and Cauchy--Schwarz. No finite experiment is used as a proof.

## Originality

PASS. Proposition 3.2 of the primary source introduces \(\varepsilon_{ij}\) as a zero/nonzero reflection test. It derives equality of the relevant rows only in the zero case. The inspected full text does not state a norm identity for positive defect or any square-root stability estimate. Targeted searches by source identifier, reflection-defect terminology, approximate symmetry, and weighted row differences found no covering result.

## Value

PASS. The source's reflection defects are used to formulate and attack its principal symmetry questions. Replacing an exact-zero test by an exact positive-defect energy gives a meaningful quantitative tool: it measures how far one candidate transposition is from reflection symmetry in the natural Morley coordinates and supplies explicit stability constants useful in further analytic or certified numerical work.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Tran, arXiv:2610.01216v1, especially Proposition 3.2. The companion tetrahedron preprint studies converse symmetry questions in dimension three, but the inspected result summary contains no all-dimensional positive-defect identity.

The result assumes that the Morley simplex itself is exactly regular, controls only one transposition at a time, and directly controls weighted rather than unweighted row differences. It does not resolve the open reflection conjectures.
