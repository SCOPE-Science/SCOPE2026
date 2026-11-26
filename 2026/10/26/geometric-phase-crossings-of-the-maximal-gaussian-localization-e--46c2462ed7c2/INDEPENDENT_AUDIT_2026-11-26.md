# Independent mathematical audit

## correctness

PASS

The normalized disk operator is exactly the sum of three centered averages of normalized Fock projectors; the area normalization gives trace 3 for disjoint disks. The coherent-vector power series and its real derivatives converge locally in Fock norm. Hence disk averaging cancels the first moments and gives O(epsilon^2) in operator norm for both the operator and its R derivative. The cyclic orbit of coherent vectors has one positive Gram level in each character, with off-diagonal magnitude rho=exp(-3R^2/2) and phase sqrt(3)R^2/2 up to choice of cyclic sign. At the stated odd-phase radii the levels are 1+rho twice and 1-2rho once. The derivative difference has magnitude 2 rho times sqrt(3) times sqrt(3) R = 6 R rho. On a small closed interval around each fixed radius the two selected sector branches are simple within their own sectors, and jointly separated from all other levels. Sector Riesz projections and the resolvent identity give C^1 branch errors of O(epsilon^2). Opposite endpoint signs and a derivative of fixed nonzero sign give one transverse zero, the mean-value theorem gives the claimed shift, and the spectral gap persists. The interval and the allowed disk radius can be shrunk to ensure disjointness, independently for each m. This also checks m=0 and leaves no claim uniform in m. The finite quadrature in triad_checker.py is supplemental, not an infinite-dimensional certificate; it was inspected, not run.

## originality

PASS

The supported distinction is the per-resonance small-disk result: local uniqueness, transversality, exact top multiplicity two and quadratic radius shift for the actual disk operator. There is material overlap in coherent Gram phases and qualitative positive-disk doublets with the fixed-disk large-separation Resultary result; neither that statement nor the inspected literature gives the small-disk derivative control or the local crossing law. This is a bounded comparison, not a historical priority certification.

## value

PASS

The multiplicity counts the independent optimal signals for a fixed observation mask. The theorem gives an exact, stable-under-radius-tuning nonuniqueness mechanism for natural equal-area disconnected masks, not merely a repeated eigenvalue of a three-point surrogate. The local location, transverse behavior, and strict gap make the specified result stronger and more informative than a numerical coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
