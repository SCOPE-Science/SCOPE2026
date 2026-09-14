# One-step girth-frozen Ramanujan 2-lifts: a certified branch-choice obstruction

## Context

The target asks whether every degree d >= 3 admits an infinite tower of connected d-regular bipartite
Ramanujan graphs by iterated 2-lifts with logarithmic girth. Marcus-Spielman-Srivastava guarantee a
Ramanujan signing at each step but give no girth control. The natural greedy strategy is: take a
Ramanujan lift, then choose the next signing to raise girth. This work derives the exact one-step
girth calculus and discovers that the greedy step can already stall at 12 vertices.

## Definitions

Let G be finite d-regular bipartite of girth g. A 2-lift H is given by a signing s: E(G) -> {+1,-1}:
V(H) = V(G) x {0,1}, with parallel or crossed edges according as s_e = +1 or -1. The spectrum of H
is the union of Spec(G) and Spec(A_s), where A_s is the signed adjacency matrix. A 2-lift of a
Ramanujan G is Ramanujan iff rho(A_s) <= 2*sqrt(d-1). For a g-cycle C, its signing product is
prod_{e in C} s_e; with x_e = (1-s_e)/2 in F_2, odd product is the linear equation sum_{e in C} x_e = 1.

## Result

Lemma (monotonicity and doubling): g <= girth(H) <= 2g. Lemma (count): the number of g-cycles of H
equals twice the number of evenly-signed g-cycles of G. Corollary (criterion): girth(H) > g iff every
g-cycle of G is oddly signed, an F_2 linear system with one equation per g-cycle; if UNSAT then every
immediate 2-lift stays at girth g (one-step girth-frozen).

Theorem: There exist connected 3-regular bipartite Ramanujan graphs H of girth 4, explicit 2-lifts of
K_{3,3}, that are one-step girth-frozen. With V(K_{3,3}) = {0,1,2} U {3,4,5} in networkx edge order,
s(0) = (+1,+1,-1,+1,-1,+1,+1,-1,+1) lifts K_{3,3} to a connected Ramanujan H_0 on 12 vertices, girth 4,
ten 4-cycles, whose 10x18 F_2 odd-product system has rank 6 and is UNSAT (exact elimination derives
0 = 1). A second witness s(2) = (-1,+1,-1,+1,-1,+1,+1,+1,+1) is certified identically. Hence every
immediate 2-lift of H_0 (resp. H_2) has girth exactly 4.

Companion sharpness: K_{d,d} for d >= 3 is one-step frozen (three 4-cycles sum to 0 = 1 in F_2; UNSAT
for d = 3, 4, satisfiable only for degenerate d = 2); a third Ramanujan lift of K_{3,3} is provably
raisable; exactly 128/4096 signings of the cube Q_3 give connected Ramanujan lifts of girth 6.

## Proof / evidence

Exact integer-bitmask GF(2) Gaussian elimination in output/artifacts/certify_emergent.py; connectivity
by BFS; girth by BFS shortest-cycle; Ramanujan bound rho(A_s) <= 2*sqrt(2) by numpy eigvalsh with
margin about 0.27. Independently re-verified: connected, girth 4, signed max 2.5616, ten 4-cycles,
UNSAT rank 6 for both witnesses. K_{d,d} UNSAT re-verified for d = 3, 4. Cube census 128/4096
independently confirmed by exhaustive enumeration.

## Limitations

One step only: girth-4 children of a frozen witness may themselves be raisable (escape probe, seed
123, 400 samples: hundreds of connected girth-4 children, of which a substantial fraction have
satisfiable systems), so longer towers may recover and the target is neither proved nor disproved.
Certified for explicit d = 3 graphs plus K_{d,d}; not an all-d classification. Spectra use floating
point with large margin; UNSAT uses exact arithmetic.

## Reproducibility

python3 output/artifacts/certify_emergent.py; python3 output/artifacts/kdd_obstruction.py;
python3 output/artifacts/enumerate_lifts.py. Requires only numpy and networkx (or the self-contained
numpy-only recomputation described in the audit).

## References

Marcus-Spielman-Srivastava, Interlacing families I: Bipartite Ramanujan graphs of all degrees,
Annals 2015 (arXiv:1304.4132). Bilu-Linial 2-lift framework. Lu-Wu arXiv:2109.02830 (rank vs girth,
checked as non-covering).
