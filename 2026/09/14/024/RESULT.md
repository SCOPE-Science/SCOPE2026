# Finite-size Cardy/RSW window for the 4x2 rectangle: exact crossing probability

## Statement

For critical Bernoulli bond percolation at p=1/2 on the finite 4-by-2 rectangle graph, the left-right open crossing probability satisfies 0.25 <= P(H) <= 0.45. In fact P(H) = 1550368/2^22 = 48449/131072 ≈ 0.36963654.

## Context

In critical planar percolation, Russo–Seymour–Welsh theory gives uniform positivity of rectangle crossings depending only on aspect ratio, and Cardy's formula describes the continuum-limit crossing function. Finite-size exact values for very small rectangles are natural benchmarks for finite-size corrections, small-grid reliability polynomials, and verification of simulation methods. The 2:1 rectangle is the standard first nontrivial aspect ratio beyond the square.

## Definitions

Vertices are integer lattice points (x,y) with 0<=x<=4 and 0<=y<=2, giving 5x3=15 vertices. Edges are nearest-neighbour pairs with both endpoints in the rectangle: 3 rows x 4 horizontal edges = 12 plus 5 columns x 2 vertical edges = 10, total n=22 edges. Each edge is open independently with probability 1/2. H is the event that some open path using only internal edges joins the left side {0}x[0,2] to the right side {4}x[0,2].

Edge indexing for the certificate: horizontal edge ((x,y),(x+1,y)) has index y*4+x (0..11); vertical edge ((x,y),(x,y+1)) has index 12+y*5+x (12..21).

## Result

Theorem: with P_{1/2} the product measure at p=1/2, 0.25 <= P_{1/2}(H) <= 0.45, with the exact value 1550368/4194304 = 48449/131072 ≈ 0.3696365356.

The exact count N_H = 1550368 is the number of edge-subsets containing a left-right open path. The reduced fraction uses gcd(1550368,4194304)=32.

## Proof / evidence

At p=1/2 every one of the 2^22=4194304 configurations is equiprobable, so P(H)=N_H/2^22 and exact enumeration is a rigorous determination. Two independent C programs exhaust all masks 0<=m<2^22. Program 1 (enumerate.c) runs breadth-first search from the three left-boundary vertices along open edges and records whether x=4 is reached. Program 2 (verifier2.c) builds the same edge set with transposed loop order, unions endpoints of open edges with union-find, and declares H iff some left and some right vertex share a root. Both output count=1550368 total=4194304. Integer bound check: 0.25*4194304=1048576<=1550368 and 1550368<=0.45*4194304=1887436.8, both strict with margins about 0.11964 and 0.08036, so rounding is irrelevant. No sampling, asymptotics, or floating-point decisions enter; the printed decimal is only display.

## Limitations

The certificate applies only to the stated finite 4x2 bond graph at p=1/2. It implies nothing about other aspect ratios, larger boxes, site percolation, or continuum Cardy limits. Correctness rests on the archived programs faithfully encoding the 22-edge graph, mitigated by dual independent implementations and exact integer counting.

## Reproducibility

Compile and run either archived source with one command, e.g. gcc -O2 -o enumerate output/artifacts/enumerate.c && ./enumerate; similarly for verifier2.c. Deterministic, no input, no randomness, runs in well under a second. Both sources are archived under output/artifacts/.

## References

- Cardy continuum crossing formula and Watts extensions (continuum-limit background, not used in proof).
- Russo–Seymour–Welsh theory for uniform rectangle-crossing bounds (motivation only).
- R. M. Ziff, Phys. Rev. E 54:2547 (1996), numerical finite-size crossing-function corrections for large lattices (background contrast: approximate large-size vs. exact 22-edge result here).
