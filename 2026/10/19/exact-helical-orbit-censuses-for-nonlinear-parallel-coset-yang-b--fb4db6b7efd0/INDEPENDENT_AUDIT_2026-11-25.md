# Independent mathematical audit

## correctness

PASS

The normalized mask either swaps or fixes each two-element coset, so its translated f is bijective. R adds the same increment K(s) to both arguments, preserving s and squaring to the identity. K depends only on the quotient and its quotient is the constant h. In the quantum identity each extreme pair uses its original sum quotient (zero or two shifts by h), and the middle pair uses its sum shifted by h on both sides, so the total increments match. This is the unbraided identity: for h≠0 the two sides of the unswapped braid relation have different first-coordinate shifts on the quotient. In the sweep the quotient of the mask argument shifts by (N+1)h each time. Thus four sweeps cancel, and for odd N two cancel. Given the carrier, each site's initial mask argument in W is independent with two lifts; matching consecutive flags is exactly the even-N two-sweep fixed-state test. The carrier displacement is the sum of the site displacements, so no extra fixed-state constraint is lost. The normalization recovers c as the unique preimage of zero, and a nonzero mask determines d by its nonzero displacement relative to translation. Linear masks here mean F₂-linear on W; there are q/2 of them, with q/4 noninvariant for each nonzero h. Counting normalized shift-invariant flags on W/<h> and excluding the duplicate unmasked translations gives all the stated distinct-map counts. A fresh disjoint-orbit traversal recovered (C₁,C₂,C₄)=(0,64,96) in the given q=8, N=2 example and (0,2048,0) for N=3. A different multiple-coset mask at q=16, N=2 gave (0,128,960).

## originality

PASS

The supported distinct content is the all-dimension full-state and distinct-rule census for arbitrary masks in the translated single-direction family, especially genuinely nonlinear shifted masks with h≠0. The functional identity, helical update, affine census, single-transposition census and unshifted common-displacement sector have substantial existing coverage and are not independently credited.

## value

PASS

For helical Yang–Baxter automata, maximal period alone does not determine the prevalence of short orbits. Here the explicit dependence on mask equality across a quotient shift gives an exact distribution for an unbounded, genuinely nonlinear family, and the rule census quantifies when even widths actually have order four. This adds scientifically useful information beyond the affine and single-transposition cases or a finite table of maximal periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
