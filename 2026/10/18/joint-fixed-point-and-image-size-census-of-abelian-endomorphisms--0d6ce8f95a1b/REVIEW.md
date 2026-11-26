# Independent mathematical audit

## correctness

PASS

For odd p, an abelian-image endomorphism kills the derived center, so it factors through V. The commutator forces its projected image L to be totally isotropic; the group law then adds the two coordinates without a cross term on that image, proving the converse and linearity of the central functional. Counting successive isotropic basis vectors and dividing by the number of bases gives alpha. For a prescribed t-space T in L, a map fixing T is onto L exactly when its induced V/T to L/T map is onto; its lifts with that restriction have p^{t(2n-t)} choices. For an exact fixed space of dimension s, invert the containment counts in the subspace lattice: each t-space has [t choose s]_p candidate s-spaces, and the interval coefficient is (-1)^{t-s}p^{(t-s)(t-s-1)/2}. This gives precisely X. The fixed subgroup is a graph over ker(I-A), whereas the image rank increases by one exactly when the central functional does not vanish on ker A. This verifies both split factors independently of s, including r=0. The independent arithmetic check gives F(1,p)=p^5-2p^3 and F(2,3)=81(1+40*53+40*3675)=12,078,801. The bounded checks documented in VERIFICATION.md are corroboration; the all-rank conclusion uses the proof, not execution of the supplied script. No inference to isomorphism classes of Yang–Baxter solutions follows.

## originality

PASS

Credit the existing parametrization and marginal projected-rank census. The supported distinct result is the joint fixed-space and group-image-order refinement of that marginal, including its fixed-point-free slice. The examined statements do not determine the refined strata by a parameter substitution or marginalization.

## value

PASS

Fixed-point-free abelian group endomorphisms are explicit inputs to the established Yang–Baxter construction. The formula counts those inputs throughout a natural nonabelian family and distinguishes both fixed-subgroup size and whether the image gains a central dimension. Two maps of the same projected rank need not agree on either statistic. These are useful exact labelled counts, not a claim about the number of inequivalent solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
