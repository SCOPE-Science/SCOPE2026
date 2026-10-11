# Scientific review

## Correctness — PASS

The projection-width identity follows directly from the cube's support function. On the sphere each sign orthant converts the width event into a diagonal spherical cap. The cap lies inside its orthant exactly at and above the first threshold; below it, exclusion across two different faces is impossible until the second threshold, so the one-face subtraction is exact. Rescaling the small spherical segment gives the sharp coefficient, and an explicit spherical circular-segment computation gives the full three-dimensional distribution. Differentiation yields its stated density and endpoint normalization. The standalone verifier independently integrates octant polar arcs, computes near-threshold spherical segments, and checks generated directions; these numerical checks supplement the proof rather than justify its quantifiers.

## Originality — PASS, with residual historical risk

The closest source is Kabluchko--Litvak--Zaporozhets (arXiv:1511.08479), which has all-dimensional higher-moment identities for cube projection length and limiting distribution theorems; because the width is bounded, these moments implicitly determine its law, but the inspected full-text sections do not state the displayed finite-dimensional elementary density or the first cap-face correction constant. Finch (arXiv:1110.0671) supplied low moments and discussed the lack of a cube width density formula. Paouris--Pivovarov--Zinn (arXiv:1210.7012) treats high-dimensional projection asymptotics. Geometric cap-overlap and small-cap methods are standard; they are not asserted to be original. A derivation of the same three-dimensional law hidden in another treatment of spherical \(\ell_1\) norms or spherical cap intersections remains a historical risk.

## Value — PASS

The three-dimensional explicit density resolves a concrete fixed-dimensional distributional question for one of the canonical regular polytopes, rather than merely recomputing its moments. The sharp all-dimensional cap transition explains why the high-width distribution has a simple form and quantifies how it fails immediately below tangency; this provides a structural geometrical description with a precise exponent and coefficient. The result does not depend on arbitrary sampled parameter choices.

## Scope and status

The all-dimensional statement stops at the first spherical-face overlap; an exact lower-tail decomposition for all higher dimensions is not asserted. The analytical proof is distinguished from supporting numerical tests. Historical completeness is not guaranteed by database searches.

Same-model review: passed. Independent audit: not yet performed.
