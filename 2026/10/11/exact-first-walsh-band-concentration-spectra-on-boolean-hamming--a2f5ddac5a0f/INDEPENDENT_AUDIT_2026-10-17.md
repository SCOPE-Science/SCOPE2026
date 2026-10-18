# Independent mathematical audit

## correctness

PASS

Walsh Gram matrix has scalar p, one-coordinate s and two-coordinate t exactly from conditioning on Bin(n-1,1/2) and Bin(n-2,1/2). Coordinate-sum-zero sector gives p-t with multiplicity n-1; the radial 2x2 block gives p+(n-1)t/2±sqrt(ns²+(n-1)²t²/4). Since t=s(n-1-2r)/(n-1) and determinant at p-t is n(t²-s²)<0 for 1<=r<=n-2, the sectors strictly interlace. Evaluate radius-one affine Walsh polynomials to show rank n+1 for r>=1. Direct boundary substitution gives r=0,n-1,n. Local and global binomial CLTs give the 2 Hermite-halfline eigenvalues, with central-binomial ratio <1 for odd half-balls. Independent exact rational Gram reconstruction checked all 39 (n,r) cases n=3..8; this is corroboration, not proof of all n.

## originality

PASS

The all-radius closed three-sector spectrum and Gaussian/condition-number limit survive statement-level comparison. Hogan–Lakey’s established general rank criterion already covers injectivity, and its eigenbasis reduction is not claimed as original; neither that literature nor other Resultary Hamming shell/graph concentration records gives the complete same-operator all-radii formulas and crossover.

## value

PASS

Determines exact sampling singular values/conditioning for the most basic nonconstant Walsh band on natural Hamming balls, including boundary and asymptotic transitions, rather than an arbitrary slice or a merely numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
