# Scientific review: sharp angle-dependent unit-strut bounds for parallelograms

## Correctness — PASS

The parameterization of a nondegenerate parallelogram gives the *unique* inward-side candidate for an equidistant unit witness on a given edge. Solving two affine coordinate inequalities yields exactly two quadratic feasibility inequalities and two side-length bounds. The only feasible vertex-only boundary triple is explicitly excluded under the source definition. For the fixed-angle infimum, the large-cosine branch follows from the separate bounds on both side lengths; the small-cosine branch uses a strictly convex quadratic on a compact interval and proves uniqueness at equality. The special \(60^\circ\) configuration is rejected, rather than mislabeled as an attained optimum. A separate arithmetic/geometric checker corroborates these steps for 720 parameter triples and additional sharp cases. The proof is analytic for all real input parameters, not extrapolated from the tests.

## Originality — PASS, with residual risk

The nearest source, Nikonorov and Nikonorova, arXiv:2209.05940, introduces unit side struts and proves the coarse universal lower bound \(3\). Its Theorems 1–3 and relevant proofs do not present an iff classification for parallelograms, an exact angle-resolved perimeter minimum, or the loss of attainment at the \(60^\circ\) nonvertex threshold. In Balestro et al., arXiv:2010.06315, the farthest-point minimax quantity is not an equivalent formulation of sidewise unit struts. Targeted searches for these exact parameters, geometric aliases, and proposed equality cases located no stronger direct coverage. Unindexed specialized calculations and papers not read in full remain the principal risk; no claim is made that negative search results prove uniqueness.

## Mathematical value — PASS

The strut condition arises from an established perimeter-extremal question. A complete two-parameter classification of the natural centrally symmetric quadrilateral subfamily answers both membership and sharp optimization questions, yielding a rigid square global minimum and a genuine angle-dependent transition where a limiting witness becomes an inadmissible vertex. The exact exceptional boundary cases are necessary for the source definition and cannot be omitted as cosmetic qualifications. The result does not resolve the general polygon conjecture, and that narrower scope is explicit.

Self-review: passed. Independent audit: not yet performed.
