# Self-review

**Correctness — PASS.** The exact radial-boundary equation and polar Jacobian yield the two-point exceedance coefficient by dominated convergence. For every fixed factorial moment, edge collections with shared labels vanish by the explicit spanning-tree estimate \(O(n^{(2-v)/5})\) for connected components with \(v\ge3\); this proves the Poisson limit without assuming pairwise independence. The limiting intensity, its disk endpoint, and its two distinct asymptotic powers have been independently recomputed. Computations in `verify.py` are illustrative checks, not replacements for the argument.

**Originality — PASS (best-knowledge, qualified).** Appel–Najim–Russo (2002) and Mayer–Molchanov (2006) address fixed underlying sampling bodies/measures; the latter's full text explicitly declares its sampling law fixed and gives only the \(\lambda=0\) disk member. Jammalamadaka–Janson (2015) handles fixed spherically symmetric laws. None of the materially inspected full texts or available abstracts establish the triangular-array, center-shift \(\lambda n^{-4/5}\), or its non-Weibull angular-intensity formula. General Poisson extremal-pair arguments and the disk member are acknowledged as prior. The full 2002 paper was unavailable and historical-priority uncertainty remains.

**Value — PASS.** This is a parameter-uniformly formulated critical geometry/probability crossover: the perturbation of disk shape is precisely of the order of the extreme-diameter deficit, and the theorem gives the entire non-Weibull limit distribution, not just a numerical constant or a special case. Its angular support transition at \(t=2\lambda\), the exact constants, and the distinct endpoint exponents specify the stable regime where disk and fixed-lens asymptotics compete.

**Limitations.** Fixed \(\lambda\) only; no quantitative rate, divergent parameter, or higher-dimensional statement. The finite simulations are supportive only. Independent historical-priority validation remains open.

Self-review: passed. Independent audit: not yet performed.
