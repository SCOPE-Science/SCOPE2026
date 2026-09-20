# Review

## Correctness

The affine map was evaluated exactly on all 24 source vertices. Every image coordinate is integral, its linear determinant is \(1/60\), and the resulting coordinate spans are \(156,168,168\).

For the lower bound, the transformed vertex-difference lattice has index one in \(\mathbb Z^3\), certified by the gcd of all full-rank \(3\times3\) minors. Therefore any further affine map taking all transformed vertices to integer points has an integer linear part. The three displayed vertex differences give rigorous coefficient bounds for every integer covector of width at most \(167\), reducing the width classification to 74 vectors. Exact enumeration leaves only the two parallel covectors \(\pm(1,0,0)\). Hence three independent coordinate rows of span at most \(167\) are impossible, while the displayed realization attains span \(168\).

An invertible affine map preserves polygon planarity, simple-face topology, incidences, and intersections, so the transformed coordinates inherit the source realization's polyhedral-surface properties.

## Originality

The primary source, arXiv:2609.17700, was read through its theorem, coordinate table, verification section, and stated limitations. It gives the integer realization and explicitly says that its certificate does not establish coordinate minimality. Targeted searches for the title and author together with "affine", "grid", "integer coordinates", "coordinate minimality", and the value 84 found no prior affine-lattice compression or equivalent optimality theorem for this realization.

Older work on coordinate-minimal triangulated genus-3 surfaces concerns different combinatorial objects and does not imply the affine-orbit statement proved here.

No internal SCOPE record matching the source object, affine-lattice normalization, or this claim family was found immediately before publication.

Residual risk remains because the motivating preprint was submitted only on 15 September 2026 and an unindexed parallel observation could exist.

## Value

The result converts a recent explicit integer realization into a substantially smaller exact grid model and, more importantly, proves a sharp optimality statement over its entire affine-integer orbit rather than merely reporting a smaller coordinate table. The lattice-width certificate is compact and reusable for coordinate compression questions for other integral polyhedral realizations.

## Scope of the claim

This does not prove globally smallest coordinates among all realizations of the combinatorial type. It proves the exact optimum among invertible affine images of the specific source realization with integral transformed vertices.

Same-model review: passed. Independent audit: not yet performed.
