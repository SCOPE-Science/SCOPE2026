# Review of the characteristic-five Picard rank-zero boundary theorem

## Correctness

**PASS.** The precise claim is a coefficient-space theorem over an algebraically closed field of characteristic five, not a theorem about coarse moduli. The Cartier basis has three forms, with the only needed cubic coefficients \([x^4]f^3=3A\) and \([x^9]f^3=3b\). Semilinear Cartier iteration gives rank zero exactly on \(H=V(A)\). The new boundary calculation is anchored by the exact identity \(\Delta=(a^2+c)A-2b^2(ac+b^2)\). On \(H\), it combines with \(a(ac+b^2)=-c^2\), leaving only two support curves. Their generic discriminant orders are \(6\) and \(2\). The exact coordinate change \(z=c+3a^2\) gives the \(D_5\) equation \(z^2+ab^2+a^4\); the odd \(a\)-valuation of the quadratic discriminant proves geometric irreducibility, and the derivative equations prove its isolated singular point. Normality follows from the hypersurface \(S_2\) and codimension-one regularity. Two separately implemented exact checkers passed and can be run from the accompanying paths.

## Originality

**PASS for the boundary geometry only, with a named priority risk.** The general Cartier matrix, the characteristic-five rank dichotomy, and the auxiliary \(a\)-number calculation are background: their formulas or stronger rank statements are already present in relevant literature and historical records. The closest accessible prior mathematical claims already identify the same rank-zero polynomial \(A\), smooth locus and point counts. Those statements do **not** imply the normal surface's isolated \(D_5\) analytic equation or the scheme-theoretic discriminant divisor with unequal coefficients \(6\) and \(2\). The published work of Bouw et al. treats Picard discriminants and models; Nourozi and Rahmati study Cartier ranks. Their inspected sections do not compute this codimension-one boundary. Estrada-Sarlabous (1991) is a plausible uninspected prior source for general rank conditions, and its full text was not accessible. This is a residual priority risk, not evidence for independence or uniqueness.

## Value

**PASS.** The boundary of the Picard rank-zero degeneration is a naturally defined object; its two degeneration components have sharply different Weil vanishing orders and meet at a rational double point of type \(D_5\). Exact multiplicities are germane to discriminant divisors, boundary intersection theory and possible compactification comparisons. The assertion is structural and infinite-geometric, not a check of one arbitrary coefficient tuple. No global moduli-quotient or extension to other characteristics is claimed.

## Limitations and closest literature

The geometric statement is restricted to the displayed marked affine parameter space. The vertex is not a smooth Picard curve, and the theorem does not describe semistable reduction. Priority is unresolved with respect to the inaccessible full 1991 Estrada-Sarlabous paper and potentially unindexed specialized degeneration studies. Relevant accessible literature: Bouw–Koutsianas–Sijsling–Wewers (arXiv:1902.09624, first public 2019-02-25), Nourozi–Rahmati (arXiv:2306.07823, first public 2023-06-13), and the 2015 Kazemifard–Tafazolian study of selected Picard Newton polygons.

Self-review: passed. Independent audit: not yet performed.
