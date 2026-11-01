# Scientific review

## Correctness — PASS

The event is the obtuse-angle criterion, and polar integration gives one-cell direction density \(\sec^2(t)/(2\tan(\pi/n))\). Squared Fourier coefficients determine the angle-difference distribution. The uniform cosine-coefficient expansion follows from the even analytic expansion of \(\sec^2\) and two integrations by parts with vanishing integer-frequency endpoint sines. This step is needed: a fixed-Fourier-mode expansion alone would not justify summation over infinitely many modes. The coefficient squares have a \(k^{-4}\) summable bound; the prefactor then produces errors \(O(n^{-9})\) after two displayed terms. The exact Dirichlet beta evaluations independently give \(5\pi^4/192\) and \(7\pi^6/720\). All higher coefficients follow by the same uniform expansion argument. For even polygon order, central symmetry gives exactly \(1/2\).

A standalone numerical checker was executed from the current package, with independent FFT angular autocorrelation compared to coefficient quadrature. Odd orders \(3,5,7,9,11,15,21\) and even orders \(4,6,8,10\) passed, including the independent equilateral value. These finite experiments do not establish the asymptotic theorem.

## Originality — PASS, with a substantive prior-formula risk

The October 2025 Mathematics Stack Exchange discussion explicitly contains both the parity observation and an all-orders-in-frequency *exact Fourier representation* for each polygon. These are prior results, not new claims. Rabinowitz (arXiv:2608.27491, first posted 2026-08-26) proves the exact triangle formula and the angular transfer principle. The proposed new statement is instead an **all-orders asymptotic in the polygon order** with uniform Fourier-index control, strict allowed-power structure, explicit first two coefficients, and quantitative remainder. Neither inspected source states these asymptotic coefficients or proves termwise uniform expansion. Their exact representations make the values theoretically computable, so a reviewer may reasonably view this as an analytic refinement of existing formulas rather than independent foundational novelty. The distinction is not concealed.

The computational spherical-depth paper arXiv:1702.07399 was inspected for definitions and its finite-sample algorithms; it does not state this large-order expansion. No exact matching entry was found in the searched mathematical-record descriptions. That absence is not proof of priority.

## Value — PASS

The signed probability of an obtuse angle made by two uniform polygon points is a geometrically motivated population invariant. The exact \(n^{-5}\) rate, rather than the usual second-order polygon-to-disk geometric approximation rate, quantifies a substantial cancellation from angular Fourier squaring, while the \(n^{-7}\) coefficient and all-orders structure identify the fine convergence profile. This is a reproducible infinite-family benchmark directly connected to the recent triangle depth problem, not an arbitrary selection of small polygon orders. It does not resolve global spherical-depth extremality or arbitrary polygons.

## Closest literature and limitations

- S. Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk*, https://arxiv.org/abs/2608.27491, §§2–4 and appendix: triangle depth and cone measure, not an odd-polygon-order asymptotic.
- *What planar convex shape maximizes the probability that a random circle contains the centre?*, https://math.stackexchange.com/questions/5101873/what-planar-convex-shape-maximizes-the-probability-that-a-random-circle-contains, detailed answers: exact radial/Fourier formulas, regular polygon sign law, and triangle maximum comparisons; these are explicitly credited.
- Bremner and Shahsavarifar, *An Optimal Algorithm for Computing the Spherical Depth of Points in the Plane*, https://arxiv.org/abs/1702.07399: finite input algorithms rather than large-order regular population polygons.

Historical priority of the coefficient expansion has not been independently verified. The numerical checker establishes only finite consistency, and an independent scientific audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
