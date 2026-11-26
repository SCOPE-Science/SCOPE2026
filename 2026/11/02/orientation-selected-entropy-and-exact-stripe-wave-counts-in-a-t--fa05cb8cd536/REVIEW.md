# Independent mathematical audit

## correctness

PASS

The shift condition forces forward increments in {0,1}, and every compatible binary block has exactly three color lifts; this preserves word-growth entropy. For axial stripes only the successor column contributes, with multiplicity three. The adjacency I+P at thresholds 1–3 is primitive; the spectrum 2 and exp(±i pi/3) gives the trace and zeta formulas. At n=3, repeating the increment 1 produces a primitive color 3-cycle; for n>3 a cyclic block of three ones followed by zeros has just one 0-to-1 transition and hence primitive period n. There are no primitive 2-cycles because the fixed counts at powers 1 and 2 coincide. For the diagonal families the actual Moore index offsets have multiplicities 1,2,2,2,1. The two-site look-back contributes exactly for two consecutive ones and the two-site look-ahead exactly for one of two ones, yielding the four-bit criterion. Independently applying the color rule to each window in /workspace/evidence/4_transfer.py reproduces the four characteristic-polynomial regimes, the primitive eight-state component at threshold 2, the golden-mean cyclic component and all-one cycle at threshold 3, and the listed constant cycles at thresholds 1 and 4–8. At threshold 1 an increment zero forces every following bit zero and forbids two ones immediately before it, excluding a nonconstant transition from the all-one cycle. At thresholds 4–8 the only cyclic component is the all-zero loop, so a bi-infinite path cannot leave it and return through any transient state. The positive quartic root is 1.866760399173862… . These exact local and finite-state arguments prove the full infinite stripe claim, not the entropy of the 2D automaton; finite cylinder counts presume the stated no-aliasing dimensions. The frozen checker was read, not run.

## originality

PASS

Pass for the complete orientation comparison and diagonal stripe classification, in particular the two distinct positive diagonal entropies and the threshold-one obstruction. The axial propagation cutoff is prior, and the axial shift and its finite census at threshold three have material coverage in a distinct Resultary work; do not count those as independently established originality, or infer priority from record dates. No inspected source gives or implies the two diagonal regimes from that axial result.

## value

PASS

The natural question is whether equally fast rigid waves in two lattice orientations have equally diverse families, not just whether either has a single example. The result distinguishes exponential from zero growth at threshold one and gives two genuinely different diagonal growth laws at thresholds two and three. The explicit finite-state description is useful for further stripe-size and period questions even without a claim about the full 2D system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
